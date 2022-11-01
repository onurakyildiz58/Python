import cv2
from datetime import datetime

filename = "videos\\ASL_8.1.mp4"
cap = cv2.VideoCapture(filename)
fps = cap.get(cv2.CAP_PROP_FPS)

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

origin = "00:00:00"
start = "00:03:30"  # başlangıç
end = "00:05:15"  # bitiş

originTime = datetime.strptime(origin, "%H:%M:%S")
startTime = datetime.strptime(start, "%H:%M:%S")
endTime = datetime.strptime(end, "%H:%M:%S")

startFrame = fps * (startTime - originTime).total_seconds()
endFrame = fps * (endTime - originTime).total_seconds()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter(filename.replace("8.1", "8.12"), fourcc, fps, (width, height))

counter = 1
while (cap.isOpened()):

    ret, frame = cap.read()
    if frame is None:
        break

    frame = cv2.resize(frame, (width, height))
    if counter >= startFrame and counter <= endFrame:
        out1.write(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    counter += 1

out1.release()
cv2.destroyAllWindows()
