import pygame
import pytest
from audiosys import AudioSys

pygame.mixer.init()
pygame.init()
pygame.mixer.set_num_channels(16)
audio_sys = AudioSys('../sounds')


# since the audio system is wrapped into a try except statement in main.py
def init_audio_sys(audio_folder):
    try:
        AudioSys(audio_folder)
    except FileNotFoundError:
        return False
    else:
        return True


# Only test for pass, because the user is unable to manually play files in the system.
@pytest.mark.parametrize('file', ['Hi-Hat-Closed.wav', 'Crash-Cymbal.wav', 'Floor-Tom.wav'])
def test_play_pass(file):
    sound = pygame.mixer.Sound(audio_sys.path + '/' + file)
    result = audio_sys.play(sound)
    assert result


def test_audiosys_pass():
    assert init_audio_sys('../sounds')


@pytest.mark.parametrize('path', ['Does.wav', 'Not.wav', 'Exist.wav'])
def test_audiosys_fail(path):
    assert not init_audio_sys(path)



