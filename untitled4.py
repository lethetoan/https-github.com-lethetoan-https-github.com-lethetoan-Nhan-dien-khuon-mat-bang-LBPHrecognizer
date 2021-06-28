import cv2
import sqlite3         
import os
import numpy as np
from PIL import Image
face_cascade = cv2.CascadeClassifier('C:/Users/ACER/Downloads/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:/Users/ACER/Desktop/NewNDKM/recognizer/trainner.yml')
def getProfile(ID):
    conn=sqlite3.connect('C:/Users/ACER/Desktop/NewNDKM/NDKM1.db')
    query = "SELECT * FROM NDKM WHERE ID=" + str(ID)
    cusror = conn.execute(query)
    profile = None
    for row in cusror:
        profile = row
    conn.close()
    return profile
cap = cv2.VideoCapture(0)
fontface=cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         cat_gray = gray[y: y + h, x: x + w]     
         ID, sai_lech = recognizer.predict(cat_gray)
         if sai_lech < 60:
             profile = getProfile(ID)
             if profile != None:
                 cv2.putText(frame,'Name:'+ str(profile[1]),(x,y + h + 30),fontface,1,(0,255,0),2)
                 cv2.putText(frame,'Age:'+ str(profile[2]),(x,y + h + 60),fontface,1,(0,255,0),2)
             else:
                 cv2.putText(frame,'UNKNOW:'+ str(profile[1]),(x,y + 30),fontface,1,(0,0,255),2)
    cv2.imshow('Cam',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()        
        