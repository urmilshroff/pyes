import sys
import shlex, subprocess #for running shell scripts

try:
    import cv2 #OpenCV for face and video analysis
    import numpy as np #numerical Python library required for OpenCV
    
    import kivy #for gui application
    kivy.require("1.10.0")
    from kivy.app import App
    from kivy.uix.gridlayout import GridLayout
    
    dependencies_exist=True #boolean to mark if dependencies are available
    
except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))

    if input("Would you like to install Kivy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install Kivy")) #command to install Kivy

    if input("Would you like to install OpenCV? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install opencv-python")) #command to install OpenCV

    if input("Would you like to install Numpy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install numpy")) #command to install Numpy

    print("Please restart the program")
    dependencies_exist=False

if dependencies_exist: #only if everything is installed, program will continue to run

    class PyesRecognitionLogic: #contains object detection functions
        
        def __init__(self): #initializes Haar Cascades
            self.face_cascade=cv2.CascadeClassifier("haar_cascades/face_cascade.xml")
            self.eye_cascade=cv2.CascadeClassifier("haar_cascades/eyes_cascade.xml")
            self.nose_cascade=cv2.CascadeClassifier("haar_cascades/nose_cascade.xml")
            self.hand_cascade=cv2.CascadeClassifier("haar_cascades/hand_cascade.xml")
            self.clock_cascade=cv2.CascadeClassifier("haar_cascades/clock_cascade.xml")
            
            self.cap=cv2.VideoCapture(0) #0 is id of webcam
    
        def face_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.face=self.face_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (fx,fy,fw,fh) in self.face:
                    cv2.rectangle(color_frame,(fx,fy),(fx+fw,fy+fh),(255,255,0),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Face",(fx,fy-7),font,1,(255,255,0),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting faces",color_frame)
    
                if cv2.waitKey(1) & 0xFF==ord("q"): #quits when pressing Q
                    break
                    
            pyes.Exit() #exits Kivy app
    
        def eye_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.eye=self.eye_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (ex,ey,ew,eh) in self.eye:
                    cv2.rectangle(color_frame,(ex,ey),(ex+ew,ey+eh),(0,255,255),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Eye",(ex,ey-7),font,1,(0,255,255),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting eyes",color_frame)
    
                if cv2.waitKey(1) & 0xFF==ord("q"): #quits when pressing Q
                    break

            pyes.Exit() #exits Kivy app
    
        def nose_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.nose=self.nose_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (nx,ny,nw,nh) in self.nose:
                    cv2.rectangle(color_frame,(nx,ny),(nx+nw,ny+nh),(0,255,0),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Nose",(nx,ny-7),font,1,(0,255,0),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting noses",color_frame)
    
                if cv2.waitKey(1) & 0xFF==ord("q"): #quits when pressing Q
                    break
                    
            pyes.Exit() #exits Kivy app
            
        def hand_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.hand=self.hand_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (hx,hy,hw,hh) in self.hand:
                    cv2.rectangle(color_frame,(hx,hy),(hx+hw,hy+hh),(0,0,200),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Fist",(hx,hy-7),font,1,(0,0,200),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting fists",color_frame)
    
                if cv2.waitKey(1) & 0xFF==ord("q"): #quits when pressing Q
                    break
                    
            pyes.Exit() #exits Kivy app
    
        def clock_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.clock=self.clock_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (hx,hy,hw,hh) in self.clock:
                    cv2.rectangle(color_frame,(hx,hy),(hx+hw,hy+hh),(100,50,200),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Clock",(hx,hy-7),font,1,(100,50,200),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting clocks",color_frame)
    
                if cv2.waitKey(1) & 0xFF==ord("q"): #quits when pressing Q
                    break
                    
            pyes.Exit() #exits Kivy app
                    
    class PyesGridLayout(GridLayout,PyesRecognitionLogic): #initializes the application
        pass

    class PyesApp(App):
        def build(self): #builder method
            return PyesGridLayout()

    pyes=PyesApp()
    pyes.run()