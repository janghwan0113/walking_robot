import RPi.GPIO as GPIO
import cv2
import numpy as np
import picamera
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

def select_white(image, white):
    lower = np.uint8([white,white,white])
    upper = np.uint8([255,255,255])
    white_mask = cv2.inRange(image, lower, upper)
    return white_mask

camera = PiCamera()
camera.resolution = (320, 240)
camera.vflip = True
camera.hflip = True
camera.framerate = 30


rawCapture = PiRGBArray(camera, size= (320, 240))

time.sleep(.1)
t = time.time()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    #mask_image = select_white(image, 160)
    #cv2.imshow("Processed", mask_image)
    
    cv2.imshow("Raw", image)
 
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)		
    
    if key == ord('q'):		
        break
