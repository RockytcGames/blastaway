"""Module to manage the paddle."""

import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    """Class to manage the paddle."""
    def __init__(self, game_instance):
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.setup = game_instance.setup
        self.color = self.setup.color['paddle']
        self.rect = pygame.Rect(0, 0, self.setup.paddle['height'],
                                self.setup.paddle['width'])
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - self.rect.height

    def update(self, *args, **kwargs):
        """Update the paddle location"""
        if (self.setup.paddle['moving_left'] and
                self.rect.left > self.screen_rect.left + 3):
            self.rect.x -= self.setup.paddle['speed']
        if (self.setup.paddle['moving_right'] and
                self.rect.right < self.screen_rect.right - 2):
            self.rect.x += self.setup.paddle['speed']

    def draw(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
