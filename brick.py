"""Module to manage the bricks."""

import pygame
from pygame.sprite import Sprite

class Brick(Sprite):
    """Class to represent a single brick."""
    def __init__(self, game_instance):
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.setup = game_instance.setup
        self.color = self.setup.color['brick']
        self.image = pygame.Surface([self.setup.paddle['height'],
                                     self.setup.paddle['width']])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        # Start each brick on the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
