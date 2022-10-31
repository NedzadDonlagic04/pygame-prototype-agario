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
    def __init__(self, circle_radius, color, pos, width, height):
        self.COLOR = color
        self.pos = pos 
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = 10

        self.createCircle(circle_radius)
        self.createLine(width, height, 5, 10)

    def createCircle(self, circle_radius):
        ball_img = pygame.Surface((2 * circle_radius, 2 * circle_radius), pygame.SRCALPHA)
        pygame.draw.circle(ball_img, self.COLOR, (circle_radius, circle_radius) , circle_radius)
        self.image = ball_img
        self.rect = self.image.get_rect( center = self.pos )

        self.createScore(str(circle_radius * 2), getPercent(circle_radius, 50))

    def createLine(self, width, height, line_height, screen_percent):
        line_img = pygame.image.load('./img/line.png').convert()
        self.line_img = pygame.transform.scale(line_img, (width, line_height))
        self.line_rect = line_img.get_rect( topleft = (0, getPercent(height, screen_percent)) )

    def createScore(self, text, font_size, color='white'):
        font = pygame.font.Font('./fonts/Pixeltype.ttf', font_size)
        self.text = font.render(text, False, color)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top >= self.line_rect.bottom:
            self.rect.top -= self.SPEED
        elif keys[pygame.K_s] and self.rect.bottom + self.SPEED <= self.HEIGHT:
            self.rect.bottom += self.SPEED
        elif keys[pygame.K_d] and self.rect.right + self.SPEED <= self.WIDTH:
            self.rect.right += self.SPEED
        elif keys[pygame.K_a] and self.rect.left - self.SPEED >= 0:
            self.rect.left -= self.SPEED
        self.text_rect = self.text.get_rect( center = self.rect.center )

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.line_img, self.line_rect)