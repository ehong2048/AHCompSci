import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, thresInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse Threshold Binary", thresInv)

cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = thresInv))

cv2.waitKey(0)