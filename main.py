import pygame
from sys import exit
from random import randrange
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

        circleRadius = 50
        offsetX, offsetY = 10, 10
        player_color = 'orange'

        self.PLAYER = Player(circleRadius, player_color, (circleRadius + offsetX, height - circleRadius - offsetY), width, height)

        def generateEnemy(radiusRange, heightStart, heightEnd, widthStart, widthEnd, enemyColor='red'):
            radius = randrange(radiusRange[0], radiusRange[1], 1)
            y = randrange(heightStart + radius, heightEnd - radius, 1)
            x = randrange(widthStart + radius, widthEnd - radius, 1)

            return Enemy(radius, enemyColor, (x, y))
        
        self.ENEMIES = []
        enemyRanges = [
            (40, self.PLAYER.circleRadius - 1),
            (self.PLAYER.circleRadius, self.PLAYER.circleRadius + 10),
            (100, 120)
        ]
        for i in range(0, len(enemyRanges)):
            self.ENEMIES.append(generateEnemy( enemyRanges[i], getPercent(height, 10), height, 0, width))

            while True:
                pointB = self.ENEMIES[i].rect.center
                pointA = self.PLAYER.rect.center

                # distance
                d = getDistance(pointA[0], pointA[1], pointB[0], pointB[1])

                if d < self.PLAYER.circleRadius:
                    self.ENEMIES[i] = generateEnemy( enemyRanges[i], getPercent(height, 10), height, 0, width)
                else:
                    break
                
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

                if d < self.PLAYER.circleRadius:
                    if self.PLAYER.circleRadius < self.ENEMIES[i].circleRadius:
                        self.quit()
                    elif self.PLAYER.circleRadius > self.ENEMIES[i].circleRadius:
                        self.PLAYER.createCircle(self.ENEMIES[i].circleRadius)
                        del self.ENEMIES[i]
                        break

            self.PLAYER.update()
            self.PLAYER.draw(self.SCREEN)

            pygame.display.update()

            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game(50, 70, 'Agario')
    game.run()