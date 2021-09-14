from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

T = mahotas.thresholding.otsu(blurred)
print(f"Otsu's threshold: {T}")

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0 
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

cv2.waitKey(0)
