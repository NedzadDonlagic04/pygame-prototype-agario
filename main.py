import pygame
from sys import exit
from classes import *
from functions import *

class Game:
    def __init__(self, width_percent, height_percent, title):
        pygame.init()
        pygame.display.set_caption(title)

        info = pygame.display.Info()

        width = getPercent(info.current_w, width_percent)
        height = getPercent(info.current_h, height_percent)
        
        self.SCREEN = pygame.display.set_mode((width, height))
        self.BG_COLOR = 'black'

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
    game = Game(50, 70, 'Agario')
    game.run()