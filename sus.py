
import cv2 

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret , frame = cam.read()
    ret1,frame1 = cam.read()
    diff = cv2.absdiff(frame,frame1)
    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    ray = cv2.cvtColor(frame1,cv2.COLOR_RGB2GRAY)
    asa = cv2.absdiff(gray,ray)
    url = cv2.GaussianBlur(asa,(5,5),0)
    blur = cv2.GaussianBlur(ray,(5,5),1)
    _, thresh = cv2.threshold(url,25,255,cv2.THRESH_BINARY_INV)
    _, resh = cv2.threshold(url,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=1)
    ilat = cv2.dilate(thresh,None,iterations=1)
    was = cv2. absdiff(thresh,resh)
    lat =cv2.dilate(was,None,iterations=3)
    contours, _ = cv2.findContours(ilat,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    contour, _ = cv2.findContours(dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    
    
    
    
    cv2.drawContours(frame1,contours,-1,(0,0,255),2)
    for c in contours:
        if cv2.contourArea(c)>100001:
           # print("Movement captured")
            ...
        elif cv2.contourArea(c)>100:
            #import gomail <-- this program made by me with the help of google and youtube and python docs
            ...
    cv2.drawContours(frame,contours,-1,(255,0,255),1)
    for d in contour:
        if cv2.contourArea(c)>100000000000:
           # print("Movement captured")
           ...
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2,3)
        
    

    if cv2.waitKey(10) == ord('q'):
        break

    cv2.imshow('Security cam1',frame1)
    