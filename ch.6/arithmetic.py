from __future__ import print_function
import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Joseph", img)

print(f'max of 255 {cv2.add(np.uint8([200]), np.uint8([100]))}')
print(f'min of 0 {cv2.subtract(np.uint8([50]), np.uint8([100]))}')

print(f'wrap around: {np.uint8([200]) + np.uint8([100])}')
print(f'wrap around: {np.uint8([50]) - np.uint8([100])}')

Mat = np.ones(img.shape, dtype = "uint8") * 100
added = cv2.add(img, Mat)
cv2.imshow("Added", added)

Mat = np.ones(img.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(img, Mat)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)

