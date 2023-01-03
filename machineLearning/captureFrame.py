import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

save = "DataSet2\\Y"
capture = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 25
imageSize = 300
k = 0
xNCal = 0
Gap = 0
counter = 0


while True:
    success, img = capture.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        xP, yP, xN, yN = hand['bbox']
        ratio = yN / xN

        imgWhite = np.ones((imageSize, imageSize, 3), np.uint8)*255
        imgCrop = img[yP - offset:yP + yN + offset, xP - offset:xP + xN + offset]
        imgShape = imgCrop.shape

        if ratio > 1:
            k = imageSize / yN
            xNCal = math.ceil(k * xN)
            imageResize = cv2.resize(imgCrop, (xNCal, imageSize))
            imageResizeShape = imageResize.shape
            xNGap = math.ceil((imageSize-xNCal) / 2)
            imgWhite[:, xNGap:xNCal + xNGap] = imageResize
        else:
            k = imageSize / xN
            yNCal = math.ceil(k * yN)
            imageResize = cv2.resize(imgCrop, (imageSize, yNCal))
            imageResizeShape = imageResize.shape
            yNGap = math.ceil((imageSize - yNCal) / 2)
            imgWhite[yNGap:yNCal + yNGap, :] = imageResize

        cv2.imshow("image crop", imgCrop)
        cv2.imshow("image white", imgWhite)

    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if key == ord("s") or key == ord("S"):
        counter += 1
        cv2.imwrite(f'{save}/{counter}.jpg', imgWhite)
        print(counter)
