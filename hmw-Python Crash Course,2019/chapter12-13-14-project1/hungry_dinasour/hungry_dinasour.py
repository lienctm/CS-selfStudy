import sys
import pygame
from setting import Settings
from dinasour import Dinasour

class HungryDinasour:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_height, self.setting.screen_width))
        pygame.display.set_caption("Hungry Dinasour")
        self.dinasour = Dinasour(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.setting.bg_color)
        self.dinasour.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    hd = HungryDinasour()
    hd.run_game()
