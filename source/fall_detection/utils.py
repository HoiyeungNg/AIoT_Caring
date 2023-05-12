import cv2
import numpy as np 
import matplotlib.pyplot as plt
from config import *
from visualization import draw_prediction_on_image


def cropping_region(image_shape):
    # create a white patch (max intensity) to cover the TV table
    y, x = image_shape[:2]
    mask = np.zeros(image_shape, dtype="uint8")
    x1, x2 = int(950/2592*x), int(1250/2592*x)
    y1, y2 = int(450/1944*y), int(1200/1944*y)
    cv2.rectangle(mask, (x1, y1), (x2, y2), 255, -1)
    whiteImg = np.zeros(image_shape, 'uint8')
    whiteImg[:,:] = (255, 255, 255)
    whiteImg = cv2.bitwise_and(whiteImg, whiteImg, mask=mask)
    return whiteImg

def show_output_overlay(data, file='xxxx.npy', label='normal', figsize=(5, 5)):
    # Results from model inference.
    keypoints_with_scores = data[label][file]
    # Raw image.
    image = cv2.imread(os.path.join(DATA_DIR, 'train', label, file))
    # Add label, if there is any.
    if label:
        image = cv2.putText(image, label, (int(image.shape[0]/10), int(image.shape[1]/10)), cv2.FONT_HERSHEY_SIMPLEX, 
                            4, (255, 255, 0), 6, cv2.LINE_AA)
    # Overlay predicted key points
    output_overlay = draw_prediction_on_image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), keypoints_with_scores)
    # Show image
    plt.figure(figsize=figsize)
    plt.imshow(output_overlay)
    _ = plt.axis('off')

def produce_feature(keypoints_with_scores, 
                    confidence_threshold=0.2, 
                    return_dict=False):
    # Remove low confidence
    head_center_y, body_center_y, foot_center_y = np.nan, np.nan, np.nan
    arr = keypoints_with_scores[:5]
    arr = arr[arr[:, -1] > confidence_threshold]
    if arr.size > 0:
        _, head_center_y, _ = arr.mean(axis=0)

    arr = keypoints_with_scores[5:13]
    arr = arr[arr[:, -1] > confidence_threshold]
    if arr.size > 0:
        _, body_center_y, _ = arr.mean(axis=0)

    arr = keypoints_with_scores[13:]
    arr = arr[arr[:, -1] > confidence_threshold]
    if arr.size > 0:
        _, foot_center_y, _ = arr.mean(axis=0)

    num_points_detected = (keypoints_with_scores[:, -1] > 0.2).sum()

    if return_dict:
        return {
                'head_center_y': head_center_y,
                'body_center_y': body_center_y,
                'foot_center_y': foot_center_y,
                'num_detection': num_points_detected
                }
    else:
        return [head_center_y, body_center_y, foot_center_y, num_points_detected]

def construct_feature(keypoints_with_scores, pre_state=[0,0,0,0]):
    # Construct features: check if head is above the foot, ...
    head_center_y, body_center_y, foot_center_y, num_detection = produce_feature(keypoints_with_scores)
    if head_center_y != head_center_y:
        head_center_y = pre_state[0]
    if body_center_y != body_center_y:
        body_center_y = pre_state[1]
    if foot_center_y != head_center_y:
        foot_center_y = pre_state[2]
        
    curr_state = [head_center_y, body_center_y, foot_center_y, num_detection]
    input_data = [head_center_y, body_center_y, foot_center_y, num_detection,
                  head_center_y > body_center_y, head_center_y < body_center_y, 
                  body_center_y > foot_center_y, body_center_y < foot_center_y,  
                  head_center_y > foot_center_y, head_center_y < foot_center_y]
    return input_data, curr_state