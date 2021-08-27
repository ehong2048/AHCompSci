import numpy as np
import argparse
import imutils
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help="Path to Image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Joseph Joe Aguilar ", img)

(height, width) = img.shape[:2]
center = (width//2, height//2)

rotated = imutils.rotate(img, 45, center, 5.0)
cv2.imshow("Dizzy Joseph Joe Aguilar ", rotated)

cv2.waitKey(0)

