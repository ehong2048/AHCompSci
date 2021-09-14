import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

blurred = np.hstack([
    cv2.blur(image, (3,3)),
    cv2.blur(image, (21,21)),
    cv2.blur(image, (51,51)),
])
cv2.imshow("Averaged", blurred)

blurred = np.hstack([
    cv2.GaussianBlur(image, (3,3), 0),
    cv2.GaussianBlur(image, (21,21), 0),
    cv2.GaussianBlur(image, (51,51), 0),
])
cv2.imshow("Gaussian", blurred)


blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 21),
    cv2.medianBlur(image, 51),
])
cv2.imshow("Median", blurred)

blurred = np.hstack([
    cv2.bilateralFilter(image, 3, 5, 5),
    cv2.bilateralFilter(image, 21, 31, 31),
    cv2.bilateralFilter(image, 51, 51, 51),
])
cv2.imshow("Bilateral", blurred)

cv2.waitKey(0)