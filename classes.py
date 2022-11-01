import pygame
import math
from functions import getPercent
class Clock:
    def __init__(self, fps):
        self.clock = pygame.time.Clock()
        self.FPS = fps
    
    def tick(self):
        self.clock.tick(self.FPS)

class Player:
    def __init__(self, circleRadius, color, pos, width, height):
        self.COLOR = color
        self.pos = pos 
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = 10
        self.circleRadius = 0

        self.aboveLineHeight = getPercent(self.HEIGHT, 10)
        self.lineWidth = 5
        self.createCircle(circleRadius)
        self.createLine(self.lineWidth)

    def strCircleArea(self, circleRadius):
        area = math.pow(circleRadius, 2) * math.pi
        area = round(area)
        return 'Total  Circle  Area: ' + str(area) 

    def createCircle(self, circleRadius):
        self.circleRadius += circleRadius

        ballImg = pygame.Surface((2 * self.circleRadius, 2 * self.circleRadius), pygame.SRCALPHA)
        pygame.draw.circle(ballImg, self.COLOR, (self.circleRadius, self.circleRadius) , self.circleRadius)
        self.image = ballImg
        self.rect = self.image.get_rect( center = self.pos )

        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT
        elif self.rect.top < self.aboveLineHeight:
            self.rect.top = self.aboveLineHeight + self.lineWidth

        self.score = self.createText(str(self.circleRadius * 2), getPercent(self.circleRadius, 50))

        areaText = self.strCircleArea(self.circleRadius)
        self.text = self.createText(areaText, getPercent(self.aboveLineHeight, 90))
        self.text_rect = self.text.get_rect( center = (self.WIDTH/2, self.aboveLineHeight / 2) )

    def createLine(self, line_width):
        lineImg = pygame.image.load('./img/line.png').convert()
        self.lineImg = pygame.transform.scale(lineImg, (self.WIDTH, line_width))
        self.lineRect = lineImg.get_rect( topleft = (0, self.aboveLineHeight) )

    def createText(self, text, font_size, color='white'):
        font = pygame.font.Font('./fonts/Pixeltype.ttf', font_size)
        return font.render(text, False, color)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top >= self.lineRect.bottom:
            self.rect.top -= self.SPEED
        elif keys[pygame.K_s] and self.rect.bottom + self.SPEED <= self.HEIGHT:
            self.rect.bottom += self.SPEED
        elif keys[pygame.K_d] and self.rect.right + self.SPEED <= self.WIDTH:
            self.rect.right += self.SPEED
        elif keys[pygame.K_a] and self.rect.left - self.SPEED >= 0:
            self.rect.left -= self.SPEED
        self.scoreRect = self.score.get_rect( center = self.rect.center )
        self.pos = self.rect.center

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.score, self.scoreRect)
        screen.blit(self.lineImg, self.lineRect)
        screen.blit(self.text, self.text_rect)

class Enemy:
    def __init__(self, circleRadius, color, pos):
        ballImg = pygame.Surface((2 * circleRadius, 2 * circleRadius), pygame.SRCALPHA)
        pygame.draw.circle(ballImg, color, (circleRadius, circleRadius) , circleRadius)
        self.image = ballImg
        self.rect = self.image.get_rect( center = pos )

        self.circleRadius = circleRadius

        self.score = self.createText(str(circleRadius * 2), getPercent(circleRadius, 50))
        self.scoreRect = self.score.get_rect( center = self.rect.center )

    def createText(self, text, font_size, color='white'):
        font = pygame.font.Font('./fonts/Pixeltype.ttf', font_size)
        return font.render(text, False, color)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.score, self.scoreRect)