

class Command:
    """Command implementation for access of the audio system, based on box name."""
    def __init__(self, audio_sys):
        self.audio_sys = audio_sys
        self.hi_hat_closed = False

    def __call__(self, box_name):
        if box_name == 'Hi-hat toggle':
            self.hi_hat_closed = not self.hi_hat_closed

        elif box_name == 'Hi-hat':
            if self.hi_hat_closed:
                self.audio_sys.play(self.audio_sys.audio_dict['Hi-hat closed'])
            else:
                self.audio_sys.play(self.audio_sys.audio_dict['Hi-hat open'])

        else:
            self.audio_sys.play(self.audio_sys.audio_dict[box_name])
