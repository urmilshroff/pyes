import sys

try:
    import cv2
    import numpy as np
    dependencies=True
    
except ImportError:
    print("\nSorry, you don't seem to have OpenCV installed for the following version of Python: {}\n\nYou can try by running 'pip3 install opencv-python'.\n".format(sys.version))
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