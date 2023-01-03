import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

capture = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("model/keras_model.h5", "model/labels.txt")

offset = 25
imageSize = 300
k = 0
xNCal = 0
Gap = 0

labels = ["A", "B", "C", "D", "E", "F",
          "G", "H", "I", "K", "L", "M",
          "N", "O", "P", "Q", "R", "S",
          "T", "U", "V", "W", "X", "Y"]
word = []
wordSTR = ""
while True:
    success, img = capture.read()
    imgCopy = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        xP, yP, xN, yN = hand['bbox'] # x y w h
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
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            #print(prediction, index)
        else:
            k = imageSize / xN
            yNCal = math.ceil(k * yN)
            imageResize = cv2.resize(imgCrop, (imageSize, yNCal))
            imageResizeShape = imageResize.shape
            yNGap = math.ceil((imageSize - yNCal) / 2)
            imgWhite[yNGap:yNCal + yNGap, :] = imageResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            #print(prediction, index)

        accuracy = str(prediction[index] * 100)

        cv2.rectangle(imgCopy, (xP - offset, yP - offset - 50), (xP - offset + 90, yP - offset), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgCopy, labels[index], (xP, yP-28), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgCopy, (xP - offset + 220, yP - offset - 50), (xP - offset + 90, yP - offset), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgCopy, "%"+accuracy[:4], (xP + 50, yP - 28), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgCopy, (xP - offset, yP - offset), (xP + xN + offset, yP + yN + offset), (255, 0, 255), 4)

        cv2.imshow("image crop", imgCrop)
        cv2.imshow("image white", imgWhite)

    cv2.imshow("image", imgCopy)
    key = cv2.waitKey(1)
    if key == ord("s") or key == ord("S"):
        word.append(labels[index])
        for i in range(len(word)):
            wordSTR = wordSTR + word[i]
    if key == ord("q") or key == ord("Q"):
        print(wordSTR)
        cv2.destroyAllWindows()
