# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:27:44 2020

@author: northner
"""

import time
import cv2
import sys
from time import sleep
import imutils
from imutils.video import VideoStream
import os
from colorama import Fore, Back, Style
BASE_DIR=os.path.dirname(os.path.abspath(__file__))


dir_name=input("Enter the name of the new student")
path = BASE_DIR+"/images/"+str(dir_name)
#print(path)

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
# load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far
print("[INFO] starting video stream...")
print("[INFO] press ""k"" to take SNAPS while the face is detected and a red box is shown over face ")
print("[INFO] take atleast 50 images with different angles")
print("")
print("[INFO] press  <q>  to QUIT")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
total = 0


# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream, clone it, (just
	# in case we want to write it to disk), and then resize the frame
	# so we can apply face detection faster
	frame = vs.read()
	orig = frame.copy()
	# detect faces in the grayscale frame
	rects = detector.detectMultiScale(
		cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))
	# loop over the face detections and draw them on the frame
	for (x, y, w, h) in rects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0, 255), 2)
        
        
        
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `k` key was pressed, write the *original* frame to disk
	# so we can later process it and use it for face recognition
	if key == ord("k"):
		p = os.path.sep.join([path, "{}.png".format(str(total).zfill(1))])
		cv2.imwrite(p, orig)
		total += 1
        
	elif key == ord("q"):
		break
        
        
# print the total faces saved and do a bit of cleanup
print("[INFO] {} face images stored".format(total))
print("")
print("[INFO] cleaning up...")
print("")
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
vs.stop()

cv2.destroyAllWindows()
