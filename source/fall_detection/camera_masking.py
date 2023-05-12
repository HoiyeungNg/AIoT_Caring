import os
import cv2
import numpy as np
import tkinter
import tkinter.messagebox
import csv
from config import DATA_DIR


def _load_dataset_images(dataset: str ):
    """ loads the dataset image """
    img_dir = os.path.join(DATA_DIR, DATASET, dataset)
    img = cv2.imread(img_dir)
    return img

class _select_points_interface:
    def __init__(self, image: np.ndarray, image_window_name: str,save_file: os.path):
        CoordinateX = []  # Coordinate Set for X
        CoordinateY = []  # Coordinate Set for Y
        show_img=image.copy()
        params=[show_img,save_file,CoordinateX,CoordinateY]
        cv2.namedWindow(image_window_name, 0)
        cv2.setMouseCallback(image_window_name, self._mouse_event,param=params)

        while True:
            cv2.imshow(image_window_name, show_img)

            if len(CoordinateX) > 1:
                cv2.line(show_img, (CoordinateX[-2], CoordinateY[-2]), (CoordinateX[-1], CoordinateY[-1]), (0, 255, 0), 1)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                csvFile = open(save_file, "w", encoding='utf8', newline='')  #
                writer = csv.writer(csvFile)  #
                writer.writerow(['point_x', 'point_y'])
                for i in range(0, len(CoordinateX)):
                    writer.writerow([CoordinateX[i], CoordinateY[i]])
                csvFile.close()
                break
        cv2.destroyAllWindows()

    def _mouse_event(self,event, x, y, flags, param):

        image, save_file, CoordinateX, CoordinateY = param[0], param[1], param[2], param[3]

        if event == cv2.EVENT_LBUTTONDOWN:  # & flags<3:

            xy = "%d,%d" % (x, y)
            cv2.circle(image, (x, y), 2, (0, 0, 255), thickness=-1)
            cv2.putText(image, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (255, 0, 0), thickness=2)
            CoordinateX.append(x)
            CoordinateY.append(y)

def main():
    dataset = os.path.join(DATA_DIR, DATASET)
    
    image_ori = _load_dataset_images(dataset=image_name+".jpg")
    _select_points_interface(image=image_ori, image_window_name='Original_image',
                            save_file=os.path.join(dataset, image_name+'_points.csv'))
    
    cv2.waitKey(1)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    DATASET, image_name = 'background', "still_cam"
    main()
