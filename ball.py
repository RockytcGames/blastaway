"""Module to manage the ball."""

import time
import random

import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """Class to represent the breakout ball."""
    def __init__(self, game_instance):
        """Initialize the ball."""
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.setup = game_instance.setup
        self.rect = pygame.Rect(0, 0, 30, 30)  # RADIUS 10,10
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        pygame.draw.rect(self.surface, self.setup.color['ball'], self.rect)
        self.speed = 10
        self.x_direction = None
        self.y_direction = 'down'

    def drop(self):
        """Put the ball on screen center, then start it moving."""
        time.sleep(0.5)
        self.rect.center = self.screen_rect.center
        self.x_direction = None

    def update(self, *args, **kwargs):
        """Update the ball's position on screen."""
        if self.y_direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.x_direction == 'right':
            self.rect.x += self.speed
        elif self.x_direction == 'left':
            self.rect.x -= self.speed
        elif self.x_direction == None:
            self.rect.centerx = self.screen_rect.centerx

    def draw(self):
        """Draw the ball to the screen."""
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))
