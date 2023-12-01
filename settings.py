"""Module to manage all configurable settings for the game."""


class Settings:
    """Class containing configurable game settings."""
    def __init__(self):
        """Initialize game settings."""
        self.resolution = {'window': (1024, 768),
                           # TODO: scale the next two to a percent of window
                           'button': (100, 50),
                           'font_size': 50,
                           }
        self.color = {'background': (0, 0, 150),
                      'paddle': (255, 255, 10),
                      'ball': (10, 155, 155),
                      # In general, button_bg same as background
                      'button_bg': (0, 0, 150),
                      'text': (255, 255, 10),
                      }

        self.paddle = {'speed': 20,
                       'moving_left': False,
                       'moving_right': False,
                       'width': self.resolution['window'][0] * .03,
                       'height': self.resolution['window'][1] * .13,
                       }
