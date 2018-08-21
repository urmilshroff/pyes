import sys
import shlex, subprocess
import time

try:
    import cv2 #opencv
    import numpy as np
    dependencies=True

except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))
    
    if input("Would you like to install OpenCV? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install opencv-python"))
        time.sleep(5)
        
    if input("Would you like to install Numpy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install numpy"))
        time.sleep(5)
        
    print("Please restart the program")
    dependencies=False

if dependencies==True:
    
    cap=cv2.VideoCapture(0) #0 is id of webcam

    while True:
        ret, frame=cap.read() #returns each frame of the video
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale

        cv2.imshow("Color video",frame)
        cv2.imshow("Gray video",gray_frame)

        if cv2.waitKey(1) and 0xFF==ord("q"): #pressing "q" kills the video
            break