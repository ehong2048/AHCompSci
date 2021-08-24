from __future__ import print_function
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required=True, help = "image path")

args = vars(parser.parse_args())

image = cv2.imread(args['image'])
print("image width: ".format(image.shape[1]))
print("image height: ".format(image.shape[0]))
print("color channels: ".format(image.shape[2]))

cv2.imshow("Image", image)

