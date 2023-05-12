import os
import sys
import shutil
import datetime
import cv2
import numpy as np
from joblib import load
from tflite_support.task import vision
import tflite_runtime.interpreter as tflite

from config import *
from utils import construct_feature
from visualization import draw_prediction_on_image
from web_service import upload_body

output_path = os.path.join(DATA_DIR, 'train', 'capture')
if use_mask:
    # Retrive the mask for masking out the regions for pose analysis
    mask = cv2.imread(mask_path)
# Decision tree classifier
clf = load(classifier_path) 

# Initialize the TFLite interpreter
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

def detect_pose(rgb_img):
    """Runs detection on an input image.
        Args:
        input_image: rgb
        Returns:
        A [1, 1, 17, 3] float numpy array representing the predicted keypoint
        coordinates and scores.
    """
    # Create a TensorImage object from the RGB image.
    resized = cv2.resize(rgb_img, dim, interpolation = cv2.INTER_AREA)
    # print(resized.shape)
    input_image = vision.TensorImage.create_from_array(resized)
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'],
                        np.expand_dims(input_image.buffer.astype(np.float32), axis=0))
    # Invoke inference.
    interpreter.invoke()
    keypoints_with_scores = interpreter.get_tensor(output_details[0]['index'])
    return keypoints_with_scores
    
def convert_img_to_pose(cap, output_alert=True, save_overlay=True, display_image=True):
    # Continuously capture images from the camera and run inference
    output_label = 'normal'
    predicted_labels = []
    print(output_label)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            sys.exit(
                'ERROR: Unable to read from webcam. Please verify your webcam settings.'
            )
        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Detect pose in the unmasked regions
        mask_resized = cv2.resize(mask, dim, interpolation = cv2.INTER_AREA)
        masked = cv2.addWeighted(rgb_img, 1, mask_resized, 1, 1)
        keypoints_with_scores = detect_pose(masked)
        # [1, 1, 17, 3]  -> [17, 3] 
        output_keypoints_with_scores = np.squeeze(keypoints_with_scores, axis=(0, 1))

        if display_image:
            frame = draw_prediction_on_image(cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB), 
                                                output_keypoints_with_scores)
            time_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cv2.putText(frame, time_text, (word_x, word_y), cv2.FONT_HERSHEY_SIMPLEX,1,(55,255,155),2)
            # cv2.imshow("real_time", frame)

        if save_overlay:
            file_name = os.path.join(output_path, datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f'))
            # Save key points
            np.savetxt(file_name+'.npy', output_keypoints_with_scores)
            # Overlay predicted key points
            output_overlay = draw_prediction_on_image(cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB), 
                                                    output_keypoints_with_scores)
            # Save overlay image
            cv2.imwrite(file_name+'.jpg', output_overlay)
            print('saved', file_name)

        if output_alert:
            prev_state = [0, 0, 0, 0]
            input_data, prev_state = construct_feature(output_keypoints_with_scores, prev_state)
            formatted_data = np.expand_dims(input_data, axis=0)
            predicted_label = clf.predict(formatted_data)[0]
            predicted_labels.append(predicted_label)

            # Majority label in past 5 frames
            recent_labels = predicted_labels[-5:]
            output_label = max(set(recent_labels), key=recent_labels.count)
            print(output_label)
            
            # Output signal here
            upload_body(output_label)

        if cv2.waitKey(1) & 0xFF == ord('q'):    #等待按键q按下
            break



if __name__ == '__main__':
    mode = 'test'
    cap = cv2.VideoCapture(-1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, input_size)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, input_size)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('frame_width', frame_width, '\tframe_height', frame_height)

    if mode == 'train':
        word_x = int(frame_width / 100)
        word_y = int(frame_height / 100)
        output_path = os.path.join(DATA_DIR, 'train', 'capture')
        convert_img_to_pose(cap, output_alert=False, save_overlay=True, display_image=True)
    elif mode == 'test':
        output_path = os.path.join(DATA_DIR, 'test', 'capture')
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.makedirs(output_path)
        convert_img_to_pose(cap, output_alert=True, save_overlay=True, display_image=False)
    elif mode == 'deployment':
        convert_img_to_pose(cap, output_alert=True, save_overlay=False, display_image=False)
    else:
        print('Mode not defined.')

