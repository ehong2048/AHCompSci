import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "path to image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Joseph Times Four", image)

print(f'image size {image.shape}')

mask = np.zeros(image.shape[:2], dtype = "uint8")
(centerX, centerY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (centerX-250, centerY-300), (centerX, centerY), 255, -1)
cv2.imshow("Mask", mask)

masked_img = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Joseph", masked_img)

mask_circle = np.zeros(image.shape[:2], dtype = "uint8")
(centerX, centerY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask_circle, (centerX-140, centerY-120), 200, 255, -1)
cv2.imshow("Mask", mask)

masked_img2 = cv2.bitwise_and(image, image, mask=mask_circle)
cv2.imshow("Masked Joseph", masked_img2)

cv2.waitKey(0)
