import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        
        self.SCREEN = pygame.display.set_mode((500, 500))
        self.BG_COLOR = 'red'

        self.CLOCK = Clock(60)
    
    def quit(self):
        pygame.quit()
        exit()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            self.SCREEN.fill(self.BG_COLOR)

            pygame.display.update()

            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game('Agario')
    game.run()