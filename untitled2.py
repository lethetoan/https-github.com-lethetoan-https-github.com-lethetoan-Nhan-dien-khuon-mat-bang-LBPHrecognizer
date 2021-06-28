import cv2
import sqlite3
import os
#B1 : connect to Database
def insertOrUpdate(ID,Name,Age):
    conn = sqlite3.connect('C:/Users/ACER/Desktop/NewNDKM/NDKM1.db')
    query = 'SELECT * FROM NDKM WHERE ID=' + str(ID)
    cusror = conn.execute(query)
    isRecordExist = 0
    for row in cusror:
        isRecordExist = 1
    if (isRecordExist == 0):
        cmd="INSERT INTO NDKM(ID,Name,Age) Values("+str(ID)+",' "+str(Name)+" ',' "+str(Age)+ " ')"
    else:
        cmd = "UPDATE NDKM SET Name=' " + str(Name) + " ', Age=' " + str(Age) + " 'WHERE ID=" + str(ID)
    conn.execute(cmd)
    conn.commit()
    conn.close()
ID = input('Enter ID:  ')
Name = input('Enter Name:  ')
Age = input('Enter Age:  ')  
insertOrUpdate(ID,Name,Age)
#B2: Cắt ảnh khuôn mặt từ camera để lưu vào database    
face_cascade = cv2.CascadeClassifier('C:/Users/ACER/Downloads/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
sampleNum = 0
while True:
    ret,frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if not os.path.exists('dataset'):
            os.makedirs('dataset')
        sampleNum +=1 
        cv2.imwrite('dataset/User.' + str(ID)+ '.' + str(sampleNum)+'.jpg',gray[y: y+h,x: x+w])
    cv2.imshow('Frame',frame)    
    if cv2.waitKey(1) == ord('q'):
        break
    elif sampleNum > 100:
        break
cap.release()
cv2.destroyAllWindows()   

        