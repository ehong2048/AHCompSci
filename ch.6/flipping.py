import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to the image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Joseph", img)

flipped_img = cv2.flip(img, 1)
cv2.imshow("Flipped Horizontally", flipped_img)


flipped_img = cv2.flip(img, 0)
cv2.imshow("Flipped Vertically", flipped_img)

flipped_img = cv2.flip(img, -1)
cv2.imshow("Flipped Both Ways", flipped_img)

cv2.waitKey(0)