from __future__ import print_function
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required=True, help = "image path")

args = vars(parser.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original Groot <3", image)


(b, g, r) = image[0, 0]
print(f'Pixel Value at (0,0)\nBlue: {b}\nGreen: {g}\nRed {r}')

image[0,0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print(f'\nPixel Value at (0,0)\nBlue: {b}\nGreen: {g}\nRed {r}')

cv2.imshow("Damaged Groot :(", image)


im_corner = image[0:300, 500:800]
cv2.imshow("Groot Face!", im_corner)


image[0:300, 500:800] = (0,0,0)
cv2.imshow("Groot in hiding", image)
cv2.waitKey(0)