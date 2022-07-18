import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide welcome message of pygame.
import pygame


class AudioSys:
    """System for playing sounds. Has a dictionary for sound files.
    Uses pygame to play sounds."""
    def __init__(self, path):
        self.path = path
        self.audio_dict = {}
        self.fill_dict()

    def fill_dict(self):
        """Fills dictionary with certain key strings paired to pygame sounds of .wav files"""
        self.audio_dict['Hi-hat closed'] = pygame.mixer.Sound(self.path + '/' + 'Hi-Hat-Closed.wav')
        self.audio_dict['Hi-hat open'] = pygame.mixer.Sound(self.path + '/' + 'Hi-Hat-Open.wav')
        self.audio_dict['Crash'] = pygame.mixer.Sound(self.path + '/' + 'Crash-Cymbal.wav')
        self.audio_dict['Ride'] = pygame.mixer.Sound(self.path + '/' + 'Ride-Cymbal.wav')
        self.audio_dict['Snare'] = pygame.mixer.Sound(self.path + '/' + 'Snare-Drum.wav')
        self.audio_dict['Bass'] = pygame.mixer.Sound(self.path + '/' + 'Bass-Drum.wav')
        self.audio_dict['High tom'] = pygame.mixer.Sound(self.path + '/' + 'High-Tom.wav')
        self.audio_dict['Mid tom'] = pygame.mixer.Sound(self.path + '/' + 'Mid-Tom.wav')
        self.audio_dict['Floor tom'] = pygame.mixer.Sound(self.path + '/' + 'Floor-Tom.wav')

    def play(self, sound):
        """Plays a given sound on an available channel."""
        pygame.mixer.find_channel(True).play(sound)
        return True

