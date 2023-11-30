"""Module containing bindings for keyboard input."""

import pygame

class Keyboard:
    """Keybindings for input."""

    def __init__(self):
        """Initialize keybindings."""
        self.quit = pygame.K_q
        self.paddle_left = pygame.K_LEFT
        self.paddle_right = pygame.K_RIGHT
        self.pause = pygame.K_p
