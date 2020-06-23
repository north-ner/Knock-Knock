# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:41:02 2020

@author: northner
"""
import numpy as np
import os
from PIL import Image
import cv2
from time import sleep
import sys
import pickle
import csv
from colorama import Fore, Back, Style
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

image_dir=os.path.join(BASE_DIR,"images")

face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')


recognizer=cv2.face.LBPHFaceRecognizer_create()


current_id=0
label_ids={}

y_lables=[]
x_train=[]
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path=os.path.join(root,file)
            label=os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            
            print(label, path)
            if not label in label_ids:
                label_ids[label]=current_id
                current_id += 1
            id_=label_ids[label]
            print(label_ids)
            
            
           # y_lables.append(label)
           # x_train.append(path)
            pil_image=Image.open(path).convert("L")#"L"convert image to gray scale
            
            size=(550,550)
            final_image=pil_image.resize(size,Image.ANTIALIAS)
            
            image_array=np.array(final_image,"uint8")
            print(image_array)
            faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)
            
            for(x,y,w,h) in faces:
                roi=image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_lables.append(id_)
lis=[]    
            
#print(y_lables)
#print(x_train)
for x in (label_ids):
    lis.append(x)
print("")
print("")
print("The students enlisted are :\n",lis)
lis.insert(0,"First_Name")  
print("")
print("")
#vertical list
lis2=np.array(lis)
myData=np.vstack(lis2)
  
myFile = open('attendance.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
print("Writing complete")

with open("lables.pkl",'wb')as f:
    pickle.dump(label_ids,f)
     
recognizer.train(x_train, np.array(y_lables))
recognizer.save("trainner.yml")
st="Enter your choice-"
for x in st :
    print(Fore.GREEN +Back.CYAN+Style.BRIGHT+x , end='')
    sys.stdout.flush()
    sleep(0.1)
print("")
print("")
print(Fore.RED +Back.WHITE+" <1>."+Fore.WHITE +Back.BLUE+ "  Start Attendance/Search")
print(" " )
print(Fore.RED +Back.WHITE+" <2>."+Fore.WHITE +Back.BLUE+ "  Train the Classifier")
print(" " )
print(Fore.RED +Back.WHITE+" <3>."+Fore.WHITE +Back.BLUE+ "  Add images to the Dataset" )
print("")
print("[INFO] Press"+Fore.RED +Back.WHITE+" <q> "+Fore.WHITE +Back.BLUE+ "to Exit")