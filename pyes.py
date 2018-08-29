import sys
import shlex, subprocess #for running shell commands

try:
    import cv2 #opencv
    import numpy as np #numerical python library required for opencv
    dependencies=True

except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))

    if input("Would you like to install OpenCV? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install opencv-python")) #script to install OpenCV

    if input("Would you like to install Numpy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install numpy")) #script to install Numpy

    print("Please restart the program") #regardless of dependencies
    dependencies=False

if dependencies==True: #only if everything is installed, it will continue to run

    class Pyes:
        def __init__(self): #constructor
            self.face_cascade=cv2.CascadeClassifier("haar_cascades/face_cascade.xml") #declares the face cascade
            self.eye_cascade=cv2.CascadeClassifier("haar_cascades/eyes_cascade.xml") #declares the eye cascade
            self.mouth_cascade=cv2.CascadeClassifier("haar_cascades/mouth_cascade.xml") #declares the mouth cascade
            self.cap=cv2.VideoCapture(0) #0 is id of webcam

        def face_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.face=self.face_cascade.detectMultiScale(gray_frame,1.3,5)

                for (fx,fy,fw,fh) in self.face:
                    cv2.rectangle(color_frame,(fx,fy),(fx+fw,fy+fh),(255,255,0),3) #BGR values

                cv2.imshow("Detecting face",color_frame)

                if cv2.waitKey(1) and 0xFF==ord("q"): #just syntax
                    break

        def eye_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.eye=self.eye_cascade.detectMultiScale(gray_frame,1.3,5)

                for (ex,ey,ew,eh) in self.eye:
                    cv2.rectangle(color_frame,(ex,ey),(ex+ew,ey+eh),(0,255,255),3) #BGR values

                cv2.imshow("Detecting eyes",color_frame)

                if cv2.waitKey(1) and 0xFF==ord("q"): #just syntax
                    break

        def nose_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.mouth=self.mouth_cascade.detectMultiScale(gray_frame,1.3,5)

                for (mx,my,mw,mh) in self.mouth:
                    cv2.rectangle(color_frame,(mx,my),(mx+mw,my+mh),(0,255,0),3) #BGR values

                cv2.imshow("Detecting mouth",color_frame)

                if cv2.waitKey(1) and 0xFF==ord("q"): #just syntax
                    break

    obj=Pyes() #creates object of the class Pyes

    choice=int(input("\nWhat objects would you like to detect?\n1. Face\n2. Eyes\n3. Mouth\n"))

    if choice==1:
        print("\nLooking for faces...")
        obj.face_detector()

    elif choice==2:
        print("\nLooking for eyes...")
        obj.eye_detector()

    elif choice==3:
        print("\nLooking for mouth...")
        obj.mouth_detector()

    else:
        print("\nSorry, invalid input!")