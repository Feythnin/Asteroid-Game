import pygame
from asteroid import *

class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.score_num = 0
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, 32)  # Use default font, or path to font file
        self.update_text()
    
    def update_text(self):
        self.text = self.font.render(f'Score: {self.score_num}', True, 'green')
        self.textRect = self.text.get_rect()
        self.textRect.topleft = (self.x, self.y)
    
    def draw(self, screen):
        screen.blit(self.text, self.textRect)
    
    def add_points(self, points):
        self.score_num += points
        self.update_text()