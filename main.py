import cv2
import numpy as np


def getContours(image: np.ndarray):
    lpf_kernel = np.ones((5, 5), np.float32) / 25
    image_gray: np.ndarray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(src=image_gray, ksize=(5, 5),
                                  sigmaX=1)  # low pass filter with average grey level invariance
    # Canny Filter
    # Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a
    # 5x5 Gaussian filter. We have already seen this in previous chapters.


def run(status: bool = True, webcam: bool = False):
    path = "phone_aruco_marker.jpg"  # path to default image
    cap = cv2.VideoCapture(0)  # ts argument can be either the device index or the name of a video file.
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 160)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1600)
    while status:
        if webcam:
            success, image = cap.read()
        else:
            image = cv2.imread(path)
        image = cv2.resize(src=image, dsize=(0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Original", mat=image)
        key: int = int(cv2.waitKey(delay=1))
        if key == 27:
            break


run()
