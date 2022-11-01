import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

save = "DataSet\\J"
capture = cv2.VideoCapture("videos\\ASL_3.1.mp4")
detector = HandDetector(maxHands=1)
# fixlendi
#asl 2 k den sonra resize error
#asl 3 b den sonra resize error
#asl 4 c den sonra resize error
#asl 8 resize error
# halen devam
#asl 3.1 k den sonra resize error
#asl 4.1 çok hızlı
# done
#1
#2.1
#5
#6.1
#7
#8.11
#8.12

offset = 25
imageSize = 300
k = 0
xNCal = 0
Gap = 0
counter = 268


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
