import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
(B,G,R) = cv2.split(image)
zeros = np.zeros(image.shape[:2], dtype = "uint8")

cv2.imshow("Red Jospeh", cv2.merge([zeros, zeros, R]))
cv2.imshow("Blue Jospeh", cv2.merge([B, zeros, zeros]))
cv2.imshow("Green Jospeh", cv2.merge([zeros, G, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()