# DESIGN_PROJECT-face_recognition
import cv2
import numpy as np
facec=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
while(True):
   ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facec.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
         break;
cap.release()
cv2.destroyAllWindows()

