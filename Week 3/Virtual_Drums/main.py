import cv2
import numpy as np
from stream import DrumCam
from command import Command
from audiosys import AudioSys
import pygame


def main():
    # Create a new video capture on the external webcam
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.set_num_channels(16)
    audio_folder = './sounds'
    audio_sys = AudioSys(audio_folder)
    command = Command(audio_sys)

    cap = cv2.VideoCapture(1)
    # Give lower and upper color values (hsv) for all masks
    lower_blue = np.array([95, 130, 110])
    upper_blue = np.array([140, 255, 255])
    lower_red = np.array([170, 180, 180])
    upper_red = np.array([180, 255, 255])
    # Make a list of all masks in the form (name, lower, upper)
    bounds_list = [('blue', lower_blue, upper_blue), ('red', lower_red, upper_red)]
    # Create a new camera
    drum_cam = DrumCam(cap, bounds_list, command)
    drum_cam.cam_loop()


if __name__ == '__main__':
    main()
