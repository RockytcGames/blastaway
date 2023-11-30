"""BREAKOUT CLONE

A clone written in Python with the Pygame Module"""
import sys

import pygame

from settings import Settings
from paddle import Paddle
from ball import Ball
from input_controls import Keyboard


class Breakout:
    """Main game class."""
    def __init__(self):
        pygame.init()
        self.setup = Settings()
        self._initialize_screen()
        self.clock = pygame.time.Clock()
        self.input = Keyboard()
        self.game_active = False
        self.ball = Ball(self)
        self.paddle = Paddle(self)

    def _initialize_screen(self):
        self.screen = pygame.display.set_mode(self.setup.resolution)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Tc |## Break ## Out ## |')
        self.bg_surface = pygame.Surface(self.setup.resolution)
        self.bg_surface.fill(self.setup.color['background'])

    def run(self):
        """Main game loop."""
        pygame.mouse.set_visible(False)
        self.ball.drop()
        while True:
            self.check_input_events()
            if self.game_active:
                self.paddle.update()
                self.ball.update()
                self.check_ball_paddle_collisions()
                self.check_ball_wall_collisions()
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
        if event.key == self.input.quit:
            sys.exit()
        elif event.key == self.input.pause:
            if self.game_active:
                self.game_active = False
            elif not self.game_active:
                self.game_active = True
        if self.game_active:
            if event.key == self.input.paddle_left:
                self.setup.paddle['moving_left'] = True
            elif event.key == self.input.paddle_right:
                self.setup.paddle['moving_right'] = True

    def _check_keyup_events(self, event):
        """Respond to keyreleases."""
        if event.key == pygame.K_LEFT:
            self.setup.paddle['moving_left'] = False
        if event.key == pygame.K_RIGHT:
            self.setup.paddle['moving_right'] = False

    def check_ball_paddle_collisions(self):
        if self.ball.rect.colliderect(self.paddle):
            self.ball.y_direction = 'up'

    def check_ball_wall_collisions(self):
        """Check collisions between the ball and all sides,
        except the bottom."""
        if self.ball.rect.top < self.screen_rect.top:
            self.ball.y_direction = 'down'
        if self.ball.rect.right > self.screen_rect.right:
            self.ball.x_direction = 'left'
        if self.ball.rect.left < self.screen_rect.left:
            self.ball.x_direction = 'right'

    def _update_screen(self):
        """Refresh objects on screen, draw the new screen."""
        self.screen.blit(self.bg_surface, (0, 0))
        if self.game_active:
            self.paddle.draw()
            self.ball.draw()
        pygame.display.update()
        self.clock.tick_busy_loop(60)


if __name__ == '__main__':
    game = Breakout()
    game.run()
