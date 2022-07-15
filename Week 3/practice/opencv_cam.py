import cv2
import numpy as np
import math

# width: 640
# height: 480

cap = cv2.VideoCapture(1)
width = cap.get(3)  # float `width`
height = cap.get(4)  # float `height`
print(f"width: {width}")
print(f"height: {height}")
lower_blue = np.array([95,130,110])
upper_blue = np.array([140,255,255])
lower_red = np.array([170,180,180])
upper_red = np.array([180,255,255])

while True:
    success, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bluemask = cv2.inRange(hsv, lower_blue, upper_blue)
    redmask = cv2.inRange(hsv, lower_red, upper_red)
    altimg = cv2.rectangle(img, (0, 0), (2 * math.floor(width/11), math.floor(height/5)), (255, 0, 0), 1)
    cv2.imshow("Output", altimg)
    contours1, hierarchy1 = cv2.findContours(bluemask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy2 = cv2.findContours(redmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours1:
        c = max(contours1, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        center1 = (math.floor(x + 0.5 * w), math.floor(y + 0.5 * h))
        cv2.circle(img, center1, 1, (255, 255, 0), 2)

    if contours2:
        c2 = max(contours2, key=cv2.contourArea)
        x2, y2, w2, h2 = cv2.boundingRect(c2)
        center2 = (math.floor(x2 + 0.5 * w2), math.floor(y2 + 0.5 * h2))
        # draw the biggest contour (c) in green
        cv2.circle(img, center2, 1, (255, 255, 0), 2)

    cv2.imshow("Output", img)
    cv2.imshow("hsv", hsv)
    cv2.imshow("red", redmask)
    cv2.imshow("blue", bluemask)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
