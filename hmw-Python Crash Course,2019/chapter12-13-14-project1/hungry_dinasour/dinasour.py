import pygame

class Dinasour:
    def __init__(self, hd_game):
        self.screen = hd_game.screen
        self.screen_rect = hd_game.screen.get_rect()
        self.image = pygame.image.load('images/dinasour.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)