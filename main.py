"""BREAKOUT CLONE

A clone written in Python with the Pygame Module"""
import sys

import pygame

from settings import Settings
from paddle import Paddle
from ball import Ball


class Breakout:
    """Main game class."""
    def __init__(self):
        pygame.init()
        self.setup = Settings()
        self._initialize_screen()
        self.clock = pygame.time.Clock()
        self.ball = Ball(self)
        self.paddle = Paddle(self)

    def _initialize_screen(self):
        self.screen = pygame.display.set_mode(self.setup.resolution)
        pygame.display.set_caption('Tc |## Break ## Out ## |')
        self.bg_surface = pygame.Surface(self.setup.resolution)
        self.bg_surface.fill(self.setup.color['background'])

    def run(self):
        """Main game loop."""
        pygame.mouse.set_visible(False)
        self.ball.drop()
        while True:
            self.paddle.update()
            self.ball.update()
            self.check_input_events()
            self._update_screen()

    def check_input_events(self):
        """Watch for player input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_LEFT:
            self.setup.paddle['moving_left'] = True
        elif event.key == pygame.K_RIGHT:
            self.setup.paddle['moving_right'] = True

    def _check_keyup_events(self, event):
        """Respond to keyreleases."""
        if event.key == pygame.K_LEFT:
            self.setup.paddle['moving_left'] = False
        if event.key == pygame.K_RIGHT:
            self.setup.paddle['moving_right'] = False

    def _update_screen(self):
        """Refresh objects on screen, draw the new screen."""
        self.screen.blit(self.bg_surface, (0, 0))
        self.paddle.draw()
        self.ball.draw()
        pygame.display.update()
        self.clock.tick_busy_loop(60)


if __name__ == '__main__':
    game = Breakout()
    game.run()
