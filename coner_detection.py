import cv2
cam = cv2.VideoCapture(0)
def no_action(x):
    pass
cv2.namedWindow("Result")
cv2.createTrackbar("blocksize","Result",2 ,10,no_action)
cv2.createTrackbar("Ksize","Result",3,10,no_action)
cv2.createTrackbar("k","Result",4,100, no_action)
while cam.isOpened():
    state, frame =cam.read()
    if not state:
        break
    #logic
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bs =cv2.getTrackbarPos("blocksize","Result")
    ks =cv2.getTrackbarPos("Ksize","Result")
    k =cv2.getTrackbarPos("k","Result")
    try:
        result = cv2.cornerHarris(gray,bs,ks,k/100)
        result=cv2.dilate(result,None)
        frame[result>0.01*result.max()]=[0,0,225]
    except:
        h,w,_=frame.shape
        cv2.rectangle(
            img=frame,
            pt1=(100,100),
            pt2=(w-100,h-100),
            color= (0,0,225),
            thickness= -1
        )
    cv2.imshow("Result",frame)
    if cv2.waitKey(1) == ord("q"):
        break