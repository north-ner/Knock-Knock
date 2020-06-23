# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 10:46:33 2020

@author: northner
"""

#import numpy as np
import cv2
import pandas as pd
import pickle
face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
from datetime import date
import csv
from time import sleep
import sys
import pygame
from colorama import Fore, Back, Style
row0=0
atten_id = 0
atten_label = 0
atten_name = 0
today=date.today()
atte={"name":0}
alarm=input(Fore.WHITE +Back.BLUE+" Turn off the ALARM ?\n"+Fore.RED +Back.WHITE+"<y>"+Fore.WHITE +Back.BLUE+ "for yes and"+Fore.RED +Back.WHITE+" <n>"+Fore.WHITE +Back.BLUE+" for no\n")
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
lables={"person_name":1}
with open("lables.pkl",'rb')as f:
    lables=pickle.load(f)
    lables={v:k for k,v in lables.items()}
    atten_label=lables


    #attendance 
    csvfile = pd.read_csv('attendance.csv', encoding='utf-8')
    
    
    #opening row out of the csv file 
    with open('attendance.csv', newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)  # gets the first line
  # now do something here 
  # if first row is the header, then you can do one more next() to get the next row:
  # row2 = next(f)

# opening a column out of a csv file
saved_column = csvfile.First_Name
#print(saved_column)     this is a series
#converting series to a list
list_first_name=saved_column.tolist()
itr=len(list_first_name)#for running the for loop iterating over the first column of dataframe


cap=cv2.VideoCapture(0)
while(True):
    #capturing frame by frame
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray=gray[y:y+h, x:x+w] #here (y_coordinate_start:Y_coord_end) same for x 
       
        
        
        id_,conf=recognizer.predict(roi_gray)
        if conf>55:
            #print(id_)
            #print(lables[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=lables[id_]
            color=(0,255,0)
            stroke=2
            cv2.putText(frame,name,(x,y), font, 1, color, stroke, cv2.LINE_AA)
            atten_id=id_
            atten_name=name
            #code for alarm if  person from dataset is found is found
            if (alarm!="y"):
                pygame.mixer.init()
                pygame.mixer.music.load('sound.wav')
                pygame.mixer.music.play(1)
        
        img_item="my-image.png"
        cv2.imwrite(img_item, roi_gray)
        
        color=(0,0,255)#color of rectangle BGR format
        stroke=2
        width=x+w
        height=y+h
        cv2.rectangle(frame,(x,y),(width,height), color, stroke)
    

        
    #display resulting frame
    cv2.imshow('frame',frame)
    
    #looping through the first column and if the name appear on the screen doing the entry
    
    print(atten_name)
    csvfile.loc[csvfile['First_Name'] == atten_name, today] = 1  
    csvfile.loc[csvfile['First_Name'] != atten_name, today] = 0
    
    
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


#output writing 
'''myFile = open('attendance.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)'''


print(csvfile)
#fuc
csvfile.to_csv('attendance.csv', encoding='utf-8', index=False) 
print("[INFO] cleaning up...")
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
cap.release()
cv2.destroyAllWindows()
