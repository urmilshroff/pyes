import sys
import shlex, subprocess #for running shell commands

try:
    import cv2 #opencv for face and video analysis
    import numpy as np #numerical python library required for opencv
    
    import kivy #for gui
    kivy.require("1.10.0")
    from kivy.app import App
    from kivy.uix.gridlayout import GridLayout
    
    dependencies_exist=True
    
except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))

    if input("Would you like to install Kivy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install Kivy")) #script to install Kivy

    if input("Would you like to install OpenCV? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install opencv-python")) #script to install OpenCV

    if input("Would you like to install Numpy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install numpy")) #script to install Numpy

    print("Please restart the program") #regardless of dependency existence
    dependencies_exist=False

if dependencies_exist: #only if everything is installed, program will continue to run

    class PyesRecognitionLogic:
        
        def __init__(self): #constructor
            self.face_cascade=cv2.CascadeClassifier("haar_cascades/face_cascade.xml") #declares the face cascade
            self.eye_cascade=cv2.CascadeClassifier("haar_cascades/eyes_cascade.xml") #declares the eye cascade
            self.nose_cascade=cv2.CascadeClassifier("haar_cascades/nose_cascade.xml") #declares the nose cascade
            self.hand_cascade=cv2.CascadeClassifier("haar_cascades/hand_cascade.xml") #declares the hand cascade
            self.clock_cascade=cv2.CascadeClassifier("haar_cascades/clock_cascade.xml") #declares the clock cascade
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
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Eye",(ex,ey-7),font,1,(0,255,255),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting eyes",color_frame)
    
                if cv2.waitKey(1) and 0xFF==ord("q"): #just syntax
                    break
    
        def nose_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.nose=self.nose_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (nx,ny,nw,nh) in self.nose:
                    cv2.rectangle(color_frame,(nx,ny),(nx+nw,ny+nh),(0,255,0),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Nose",(nx,ny-7),font,1,(0,255,0),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting nose",color_frame)
    
                if cv2.waitKey(1) and 0xFF==ord("q"): #just syntax
                    break
    
        def hand_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.hand=self.hand_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (hx,hy,hw,hh) in self.hand:
                    cv2.rectangle(color_frame,(hx,hy),(hx+hw,hy+hh),(0,0,200),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"Hand",(hx,hy-7),font,1,(0,0,200),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting hand",color_frame)
    
                if cv2.waitKey(1) and 0xFF==ord("q"): #just syntax
                    break
    
        def clock_detector(self):
            while True:
                ret, color_frame=self.cap.read() #returns each frame of the video
                gray_frame=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY) #converts each frame to grayscale
                self.clock=self.clock_cascade.detectMultiScale(gray_frame,1.3,5)
    
                for (hx,hy,hw,hh) in self.clock:
                    cv2.rectangle(color_frame,(hx,hy),(hx+hw,hy+hh),(0,0,200),3) #BGR values
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(color_frame,"clock",(hx,hy-7),font,1,(0,0,200),2,cv2.LINE_AA)
    
                cv2.imshow("Detecting clock",color_frame)
    
                if cv2.waitKey(1) and 0xFF==ord("q"): #just syntax
                    break
                    

    # obj=PyesRecognitionLogic() #creates object of the class PyesRecognitionLogic
    # 
    # while True:
    # 
    #     try:
    #         choice=int(input("\nWhat objects would you like to detect?\n1. Face\n2. Eyes\n3. Nose\n4. Hand\n5. Clock\nPress any number to exit.\n"))
    # 
    #         if choice==1:
    #             print("\nLooking for faces...")
    #             obj.face_detector()
    # 
    #         elif choice==2:
    #             print("\nLooking for eyes...")
    #             obj.eye_detector()
    # 
    #         elif choice==3:
    #             print("\nLooking for nose...")
    #             obj.nose_detector()
    # 
    #         elif choice==4:
    #             print("\nLooking for hand...")
    #             obj.hand_detector()
    # 
    #         elif choice==5:
    #             print("\nLooking for clock...")
    #             obj.clock_detector()
    # 
    #         else:
    #             break
    # 
    #     except ValueError:
    #         print("\nSorry, invalid input!")


    class PyesGridLayout(GridLayout,PyesRecognitionLogic):
        def nothing(self):
            if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    class PyesApp(App):
        def build(self):
            return PyesGridLayout()

    pyes=PyesApp()
    pyes.run()