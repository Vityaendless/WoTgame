import pygame

class Fireball(pygame.sprite.Sprite):

    def __init__(self, screen, moiraine):
        """created fireball"""
        super(Fireball, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.radius = 10
        self.color = 232, 157, 16
        self.speed = 4.5
        self.rect.centerx = moiraine.rect.centerx-50
        self.rect.top = moiraine.rect.top+50
        self.y = float(self.rect.y)

    def update(self):
        """fireball flying"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_fireball(self):
        """drawing fireball"""
        pygame.draw.circle(self.screen, self.color, [self.rect.centerx, self.rect.top], self.radius)