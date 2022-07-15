import cv2
import numpy as np
from stream import DrumCam
from command import Command
from audiosys import AudioSys
import configparser
import pygame
import argparse

my_parser = argparse.ArgumentParser(description='Virtual Drums.')

my_parser.add_argument('--capture',
                       type=int,
                       default=0,
                       help='Number for video capture selection.')

my_parser.add_argument('--confpath',
                       type=str,
                       default='./config.cfg',
                       help='Path to the config file.')


def main():
    # Parse arguments
    args = my_parser.parse_args()
    # Open config file
    config_obj = configparser.ConfigParser()
    config_obj.read(args.confpath)
    sounds = config_obj['sounds']
    color = config_obj['color']

    # Read the sound folder and amount of channels for the mixer
    sound_folder = sounds['sound_folder']
    num_channels = int(sounds['mixer_channels'])

    # Create a list of tuples containing the name of a color mask and np arrays of the lower
    # and upper bounds of the color in hsv for every mask.
    mask_name = color['color_name'].split(',')
    lower_bound = color['lower_bound'].split(',')
    lower_bound = [int(i) for i in lower_bound]
    lower_bound = [np.array(lower_bound[i:i + 3]) for i in range(0, len(lower_bound), 3)]
    upper_bound = color['upper_bound'].split(',')
    upper_bound = [int(i) for i in upper_bound]
    upper_bound = [np.array(upper_bound[i:i + 3]) for i in range(0, len(upper_bound), 3)]
    mask_list = list(zip(mask_name, lower_bound, upper_bound))
    # Create a new video capture on the external webcam
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.set_num_channels(num_channels)
    audio_folder = sound_folder
    audio_sys = AudioSys(audio_folder)
    command = Command(audio_sys)

    # Create video capture
    cap = cv2.VideoCapture(args.capture)

    # Create a new camera
    drum_cam = DrumCam(cap, mask_list, command)
    drum_cam.cam_loop()


if __name__ == '__main__':
    main()
