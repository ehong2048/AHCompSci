from __future__ import print_function
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required=True, help = "image path")

args = vars(parser.parse_args())

image = cv2.imread(args['image'])
print(image.shape)
print(f'width: {image.shape[1]}')
print(f'height: {image.shape[0]}')
print(f'channels: {image.shape[2]}')

cv2.imshow("Groot!", image)
cv2.waitKey(0)

cv2.imwrite("groot_image.jpg", image)
