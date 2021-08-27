import numpy as np 
import cv2

canvas = np.zeros((400,400,3), dtype = "uint8")

blue = (255,0,0)
line = cv2.line(canvas, (0,0), (400, 200), blue)

teal = (255,255,0)
line = cv2.line(canvas, (200,400), (400, 200), teal, 10)

purple = (255,0,255)
cv2.rectangle(canvas, (150, 150), (250,250), purple, -1)

canvas = np.zeros((400,400,3), dtype = "uint8")
(x, y) = (canvas.shape[1]//2, canvas.shape[0]//2)
for r in range(0,255, 5):
    cv2.circle(canvas, (x,y), r, (r,0,0))

canvas = np.zeros((400,400,3), dtype = "uint8")
for i in range(0,25,1):
    rand_radius = np.random.randint(0, high=200)
    rand_color = np.random.randint(0, high=256, size=(3,)).tolist()
    rand_point = np.random.randint(0, high=400, size=(2,))

    cv2.circle(canvas, tuple(rand_point), rand_radius, rand_color, -1)



cv2.imshow("Art!", canvas)
cv2.waitKey(0)