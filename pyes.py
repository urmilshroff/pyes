import sys
import shlex, subprocess #for running shell commands
import time

try:
    import cv2 #opencv
    import numpy as np #numerical python library required for opencv
    dependencies=True

except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))
    
    if input("Would you like to install OpenCV? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install opencv-python"))
        
    if input("Would you like to install Numpy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install numpy"))
        
    print("Please restart the program")
    dependencies=False

if dependencies==True:
    
    face_cascade=cv2.CascadeClassifier("haar_cascades/face_cascade.xml")
    eyes_cascade=cv2.CascadeClassifier("haar_cascades/eyes_cascade.xml")
    
    cap=cv2.VideoCapture(0) #0 is id of webcam

    while True:
        ret, frame=cap.read() #returns each frame of the video
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale

        cv2.imshow("Color video",frame)
        cv2.imshow("Gray video",gray_frame)

        if cv2.waitKey(1) & 0xFF==ord("q"): #just syntax
            break