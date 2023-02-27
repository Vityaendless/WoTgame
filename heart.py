import pygame
from pygame.sprite import Sprite

class Heart(Sprite):

    def __init__(self, screen):
        super(Heart, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()