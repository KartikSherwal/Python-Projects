import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.dimensions
        self.image = pygame.image.load('Alien_invasion/Images/sUfO1 (1).bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right>= screen_rect.right or self.rect.left <= 0:
            return True
    def update(self):
         self.y+= (self.settings.alien_speed * self.settings.fleet_direction)
         self.rect.y = self.y
