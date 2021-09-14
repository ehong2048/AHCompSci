import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 10, 30)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
