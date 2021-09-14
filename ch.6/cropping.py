import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
print(img.shape)
cv2.imshow("Joseph", img)

cropped_img = img[150:300, 350:500]
cv2.imshow("Joseph + Scissors", cropped_img)

cv2.waitKey(0)


