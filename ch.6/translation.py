import numpy as np
import argparse
import imutils
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help="Path to Image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Joseph Joe Aguilar ", img)

shifted_img = imutils.translate(img, 50, 50)
cv2.imshow("Shifted Joseph", shifted_img)


cv2.waitKey(0)