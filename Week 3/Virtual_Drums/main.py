"""Python program for a virtual drum system. Uses a camera and draws boxes for the drums.
Then uses color masks to track drumsticks and plays sounds when they hit the boxes."""
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
                       help='Number for video capture device selection.')

my_parser.add_argument('--confpath',
                       type=str,
                       default='./config.cfg',
                       help='Path to the config file.')

my_parser.add_argument('--hflip',
                       type=bool,
                       default=False,
                       help='Horizontal flip of the video capture.')

my_parser.add_argument('--vflip',
                       type=bool,
                       default=False,
                       help='Vertical flip of the video capture.')


class NotInt(Exception):
    pass


class ColorCodeWrong(Exception):
    pass


class WrongLength(Exception):
    pass


def int_check(check_list):
    """Checks if all values in a list are integers."""
    try:
        check_list = [int(i) for i in check_list]
        return check_list
    except ValueError:
        raise NotInt


def color_check(check_list):
    """Checks if a list is divisible by 3 (contains color codes)"""
    if not (len(check_list) % 3) == 0:
        raise ColorCodeWrong
    return True


def length_check(check_list, number):
    """Checks if the length of a list matches a number."""
    if not (len(check_list) == number):
        raise WrongLength
    return True


def main():
    # Parse arguments
    args = my_parser.parse_args()
    # Open config file
    config_obj = configparser.ConfigParser()
    config_obj.read(args.confpath)
    sounds = config_obj['sounds']
    color = config_obj['color']

    # Create a list of tuples containing the name of a color mask and np arrays of the lower
    # and upper bounds of the color in hsv for every mask.
    mask_name = color['color_name'].split(',')
    lower_bound = color['lower_bound'].split(',')
    upper_bound = color['upper_bound'].split(',')
    # Create a tuple for each of the box colors.
    hihat_off = color['hihat_off'].split(',')
    hihat_on = color['hihat_on'].split(',')
    drum_off = color['drum_off'].split(',')
    drum_on = color['drum_on'].split(',')
    color_list = [lower_bound, upper_bound, hihat_off, hihat_on, drum_off, drum_on]
    list_names = ['lower_bound', 'upper_bound', 'hihat_off', 'hihat_on', 'drum_off', 'drum_off']
    # Perform checks for the input
    for i, item in enumerate(color_list):
        try:
            item = int_check(item)
            color_check(item)
            if (list_names[i] == 'lower_bound') or (list_names[i] == 'upper_bound'):
                length_check(item, len(mask_name) * 3)
                color_list[i] = [np.array(item[j:j + 3]) for j in range(0, len(item), 3)]
            else:
                length_check(item, 3)
                color_list[i] = tuple(item)

        except NotInt:
            print(f"Non-integers in {list_names[i]}, check config file.")
            exit(1)
        except ColorCodeWrong:
            print(f"Incorrect amount of values in {list_names[i]}, check config file.")
            exit(1)
        except WrongLength:
            if (list_names[i] == 'lower_bound') or (list_names[i] == 'upper_bound'):
                print(f"Amount of values in {list_names[i]} does not match amount of " \
                      "color_name. 3 values per color expected, check config file.")
            else:
                print(f"Unexpected amount of values in {list_names[i]}. 3 values per color expected, check config file.")
            exit(1)
    lower_bound = color_list[0]
    upper_bound = color_list[1]
    mask_list = list(zip(mask_name, lower_bound, upper_bound))
    hihat_off = color_list[2]
    hihat_on = color_list[3]
    drum_off = color_list[4]
    drum_on = color_list[5]

    # Read the sound folder and amount of channels for the mixer
    sound_folder = sounds['sound_folder']
    num_channels = int(sounds['mixer_channels'])
    assert num_channels >= 0, "Negative amount of mixer_channels selected, check config file."
    # Start up the audio mixer
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.set_num_channels(num_channels)
    print(f"{num_channels} mixer channels initiated.")
    audio_folder = sound_folder
    # Tries to initiate the audio system.
    try:
        audio_sys = AudioSys(audio_folder)
    except FileNotFoundError:
        print("The sound_folder path did not point to the correct files expected by audiosys.py, check config file.")
        exit(1)
    # Initiates command pattern
    command = Command(audio_sys, hihat_off, hihat_on, drum_on)

    # Create video capture
    cap = cv2.VideoCapture(args.capture)
    assert cap.isOpened(), "Incorrect video capture device selected, check arguments."

    # Create a new camera
    drum_cam = DrumCam(cap, mask_list, command, hihat_off, drum_off, args.hflip, args.vflip)
    drum_cam.cam_loop()


if __name__ == '__main__':
    main()
