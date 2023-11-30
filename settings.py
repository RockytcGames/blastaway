"""Module to manage all configurable settings for the game."""


class Settings:
    """Class containing configurable game settings."""
    def __init__(self):
        """Initialize game settings."""
        self.resolution = (1024, 768)
        self.color = {'background': (0, 0, 150),
                      'paddle': (255, 255, 10),
                      'ball': (10, 155, 155),
                      }

        self.paddle = {'speed': 20,
                       'moving_left': False,
                       'moving_right': False,
                       'width': self.resolution[0] * .03,
                       'height': self.resolution[1] * .13,
                       }
