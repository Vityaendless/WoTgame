import pygame
from pygame.sprite import Sprite

class Moiraine(Sprite):

    def __init__(self, screen):
        """Moiraine inicialization"""
        super(Moiraine, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/moiraine.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_to_right = False
        self.move_to_left = False

    def output(self):
        """add moiraine on screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update position"""
        if self.move_to_right and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.move_to_left and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def moraine_reborn(self):
        self.center = self.screen_rect.centerx