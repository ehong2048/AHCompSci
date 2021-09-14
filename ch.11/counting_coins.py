from __future__ import print_function
import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image", required = True, help = "Path to image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 175)
cv2.imshow("Edges", edged)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"I count {len(cnts)} coins in this image")

coins = image.copy()
#cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)

cv2.drawContours(coins, cnts, 0, (0, 255, 0), 5)
cv2.drawContours(coins, cnts, 1, (255, 0, 0), 5)
cv2.drawContours(coins, cnts, 2, (0, 0, 255), 5)
cv2.imshow("Coins", coins)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)

    print(f"Coin #{i+1}")
    coin = image[y:y+h, x:x+w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)

    # cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]
    cv2.imshow("Mask", mask)
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))


cv2.waitKey(0)