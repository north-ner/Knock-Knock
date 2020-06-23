# **Knock-Knock**
Knock-Knock is a *Python* coded and *Open-CV* based **Face Recognization Application** that will help the administration in keeping a 
track of the people coming and going in a particular vicinity. It provides the authority with the option of keeping track 
of movements of named individuals.
**Knock-Knock** comes with modules for *Data collection, Dataset creation, and Face Recognization.* 
It also allows *storing of the Attendance in a "%.CSV" file* and an option to *Send it via Email.* 
**Knock-Knock** has a default feature of *sounding an alarm if the face is recognized* which can be easily turned OFF/ON. 
## Installation/Required Library
1. Python 3.x+
2. Pip
  1. time   
  2. smtplib
  3. email
  4. colorama
  5. termcolo
  6. pyfiglet
  7. getpass
  8. numpy 
  9. os
  10. PIL
  11. cv2
  12. sys
  13. pickle
  14. csv
  15. pandas
  16. datetime
  17. pygame
  18. imutils
  
  **for ease of installation open pip and run**
  
  $pip install time,smtplib,email,colorama,termcolo,pyfiglet,getpass,numpy,os,PIL,cv2,sys,pickle,csv,pandas,datetime,pygame,imutils
  
  ## Usage
  Running the Software is easy just direct your terminal to the directory **Knock-Knock** and run
  
  *$ python/python3 front.py*
  
  ![Knock-Knock front interface](https://github.com/north-ner/Knock-Knock/blob/master/readme/1.png)
  
  ### Options
  **Option <1>.** This is used to open the camera and start the monitoring or attendance taking once you have created the **dataset** *<3>* and **trained it** *<2>*.
  
  This provides the main functionality of the application. It opens up the camera and starts to detect faces while trying to recognize them
  and if it recogniges the face it makes the entry in the **"%.csv"** file along with sounding an alarm by default.
  
  It asks you "if you want to turn off the alarm? "
  
  
  ![module1 alarm on/off ](https://github.com/north-ner/Knock-Knock/blob/master/readme/al.JPG)
  
  Don't forget to press "y" if you don't want a cacophony as soon as face is detected. 
  
  Then it starts to scan for faces and Recognise them also. If recognized, it do and entry in the "%.csv" file.
  
  ![module1 face recognization ](https://github.com/north-ner/Knock-Knock/blob/master/readme/rec.JPG)
  
  Entry in the *"%.csv"*.
  
  
  ![module1 entry in csv ](https://github.com/north-ner/Knock-Knock/blob/master/readme/entry.JPG)
  
  **Option <2>.** This as the name defines is used to call the second module which train the classifer and make the *"%.yml"* file for first module to learn from.
  
  This step-
  1. Take images and make a dataset out of them.
  2. Create an **"%.pkl"**, **"%.yml"**, **"%.csv"** file containing Lables, Dataset and the Attendance.
  3. Train the classifier using the provided data.
  
  ![module2 creating dataset and training ](https://github.com/north-ner/Knock-Knock/blob/master/readme/4.JPG)
  
  **Option <3>.** This module opens up the camera and starts to "Detect" the face of a person then you can take the *snaps by pressing the key 
  *k*.* In this phase, the Application creates the folder by the provided name and store all the images into it which are later used to *create the dataset*.
  
  First, it will ask you to enter the name of a new student whose entry has to be done.
  
  
  ![module 3 running](https://github.com/north-ner/Knock-Knock/blob/master/readme/2.png)
  
  Then a camera window will open scanning and decting faces.
  
  ![module 3.2 running](https://github.com/north-ner/Knock-Knock/blob/master/readme/3.JPG)
  
  At this time when a face is detected press **'k'** to take the snap of the faces.
  
  **Option <4>.** This module helps you to send the attendance file to someone *via Email*.
  
  While using Gmail address, at first it might show authentication error cause Google doesn't allow *non-Google apps* to do the signup for security reasons.
  
  But you can change that cause as soon as you will try to send the mail you will receive another mail from Google.
  
  ![module 4 google error](https://github.com/north-ner/Knock-Knock/blob/master/readme/sc.jpg)
  
  So you need to allow access to other *third-part apps* from here.
  
  ## License
  Licensed under MIT
  
  Copyright (c) 2020 northner
