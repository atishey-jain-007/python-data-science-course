import cv2
#0 is the index of the camera
cam=cv2.VideoCapture(0)

while cam.isOpened():
    state,frame = cam.read()
    if not state:
        break
    cv2.imshow("Webcam",frame)
    print(frame.shape)
    print(frame)
    if cv2.waitKey(10) ==ord('q'):
        break