# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1024, 768)
camera.framerate = 30
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# Capture frames continuously from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Grab the raw NumPy array representing the image
    image = frame.array

    # Display the frame using OpenCV
    cv2.imshow("Frame", image)
    #print("show")

    # Wait for keyPress for 1 millisecond
    key = cv2.waitKey(1) & 0xFF

    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # If the `q` key was pressed, break from the loop
    if key == ord("q"):
        break