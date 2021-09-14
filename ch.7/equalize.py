import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(img)

cv2.imshow("Histogram Equalization", np.hstack([img, eq]))
cv2.waitKey(0)