"""Module to manage buttons printed to the screen."""

import pygame.font


class Button:
    """Class for creating and drawing buttons."""
    def __init__(self, game_instance, message):
        """Initialize button attributes"""
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.dimentions = game_instance.setup.resolution['button']
        self.color = {
                'button_bg': game_instance.setup.color['button_bg'],
                'text': game_instance.setup.color['text'],
                }
        self.font_size = game_instance.setup.resolution['font_size']
        self._prepare_message(message, self.font_size)

    def _prepare_message(self, message, font_size):
        """Generate a rendered image from message."""
        self.font = pygame.font.SysFont(None, font_size)
        self.rect = pygame.Rect((0, 0), (self.dimentions))
        self.rect.center = self.screen_rect.center
        self.msg_image = self.font.render(message, True, self.color['text'],
                                          self.color['button_bg'])
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.color['button_bg'], self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
