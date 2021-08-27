import numpy as np
import argparse
import imutils
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help="Path to Image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Joseph Joe Aguilar ", img)

aspect_r = 150.0/img.shape[0] #150 pixels divided by old width of image
dim = (150, int(img.shape[1] * aspect_r)) #new image dimensions is 150 by corresponding new resized height
