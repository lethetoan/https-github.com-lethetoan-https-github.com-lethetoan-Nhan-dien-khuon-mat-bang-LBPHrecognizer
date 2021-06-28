import cv2
import os
import numpy as np
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
def getImageWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    face = []
    IDs = []
    for imagepath in imagePaths:
        faceimg = Image.open(imagepath).convert('L')
        facenp = np.array(faceimg,'uint8')
        ID = int(imagepath.split('\\')[1].split('.')[1])
        face.append(facenp)
        IDs.append(ID)  
        cv2.imshow('Training',facenp)
        cv2.waitKey(20)
    return face,IDs
face , IDs = getImageWithID(path)
recognizer.train(face,np.array(IDs))
if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer/trainner.yml')
cv2.destroyAllWindows()    

