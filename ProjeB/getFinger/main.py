import cv2
from cvzone.SerialModule import SerialObject
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)#el algılama
mySerial = SerialObject("COM3", 9600, 1)#serial port haberleşme

while True:
    success, image = cap.read()
    hands, image = detector.findHands(image)

    if hands:
        hands = hands[0]
        fingers = detector.fingersUp(hands)
        print(fingers)
        mySerial.sendData(fingers)

    cv2.imshow("image", image)  # display
    key = cv2.waitKey(1)

    if key == ord('q') or key == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()









