#library import

#object of video capture class
# use it inside while loop
import os
import cv2
import sys

path = r"C:\Users\asus\Downloads\UnifiedShareSheet.mp4"
if not os.path.exists(path):
    print(f"File not found: {path}")
    sys.exit(1)

    cam= cv2.VideoCapture(path)
    while True:
        state, frame = cam.read()
        if not state:
            break
        cv2.imshow("video",frame)
        if cv2.waitKey(10) ==ord('q'):
            break
        #resize
        frame1 = cv2.resize(frame,(500,1000))
        frame2 = cv2.resize(frame,(0,0) ,fx=.5, fy=.5)
        cv2.imshow("video .Resized",frame1)
        cv2.imshow("video . Resized by scale ",frame2)
        if cv2.waitKey(10) == ord('q'):
            break

        

