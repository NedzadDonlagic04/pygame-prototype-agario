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
        self.ENEMIES = [
            Enemy(30, enemy_color, (300, 300)),
            Enemy(70, enemy_color, (500, 500)),
            Enemy(70, enemy_color, (600, 300))
        ]
    
    def quit(self):
        pygame.quit()
        exit()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            self.SCREEN.fill(self.BG_COLOR)

            for i in range(0, len(self.ENEMIES)):
                self.ENEMIES[i].draw(self.SCREEN)

                pointA = self.PLAYER.rect.center
                pointB = self.ENEMIES[i].rect.center

                # distance
                d = getDistance(pointA[0], pointA[1], pointB[0], pointB[1])

                if d < self.PLAYER.circle_radius:
                    if self.PLAYER.circle_radius < self.ENEMIES[i].circle_radius:
                        self.quit()
                    elif self.PLAYER.circle_radius > self.ENEMIES[i].circle_radius:
                        self.PLAYER.createCircle(self.ENEMIES[i].circle_radius)
                        del self.ENEMIES[i]
                        break

            self.PLAYER.update()
            self.PLAYER.draw(self.SCREEN)

            pygame.display.update()

            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game(50, 70, 'Agario')
    game.run()