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

        circle_radius = 50
        offsetX, offsetY = 10, 10
        player_color = 'orange'

        self.PLAYER = Player(circle_radius, player_color, (circle_radius + offsetX, height - circle_radius - offsetY), width, height)

        e_circle_radius = 30
        enemy_color = 'red'
        self.ENEMIES = [Enemy(e_circle_radius, enemy_color, (300, 300))]
    
    def quit(self):
        pygame.quit()
        exit()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            self.SCREEN.fill(self.BG_COLOR)

            for ENEMY in self.ENEMIES:
                ENEMY.draw(self.SCREEN)

            self.PLAYER.update()
            self.PLAYER.draw(self.SCREEN)

            pygame.display.update()

            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game(50, 70, 'Agario')
    game.run()