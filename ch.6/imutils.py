import numpy as np
import cv2

def translate(img, x, y):
    mat = np.float32([[1,0,x],[0,1,y]])
    shifted_img = cv2.warpAffine(img, mat, (img.shape[1], img.shape[0]))
    return shifted_img

def rotate(img, angle, center = None, scale=1.0):
    (height, width) = img.shape[:2]

    if center is None:
        center = (width//2, height//2)

    mat = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(img, mat, (width, height))

    return rotated_img