

class Command:
    """Command implementation for access of the audio system, based on box name."""
    def __init__(self, audio_sys, *colors):
        self.audio_sys = audio_sys
        self.hi_hat_closed = False
        self.hihat_close_color, self.hihat_open_color, self.box_on_color = colors

    def __call__(self, box_name, color):
        if box_name == 'Hi-hat toggle':
            self.hi_hat_closed = not self.hi_hat_closed
            if color == self.hihat_close_color:
                return self.hihat_open_color
            return self.hihat_close_color

        elif box_name == 'Hi-hat':
            if self.hi_hat_closed:
                self.audio_sys.play(self.audio_sys.audio_dict['Hi-hat closed'])
            else:
                self.audio_sys.play(self.audio_sys.audio_dict['Hi-hat open'])

        else:
            self.audio_sys.play(self.audio_sys.audio_dict[box_name])
        return self.box_on_color
