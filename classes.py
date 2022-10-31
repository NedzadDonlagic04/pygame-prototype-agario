import pygame

class Clock:
    def __init__(self, fps):
        self.clock = pygame.time.Clock()
        self.FPS = fps
    
    def tick(self):
        self.clock.tick(self.FPS)

class Player(pygame.sprite.Sprite):
    def __init__(self, circle_radius, color, pos, width, height):
        super().__init__()
        self.COLOR = color
        self.pos = pos 
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = 10

        self.updateCircle(circle_radius)

    def updateCircle(self, circle_radius):
        ball_img = pygame.Surface((2 * circle_radius, 2 * circle_radius), pygame.SRCALPHA)
        pygame.draw.circle(ball_img, self.COLOR, (circle_radius, circle_radius) , circle_radius)
        self.image = ball_img
        self.rect = self.image.get_rect( center = self.pos )

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top - self.SPEED >= 0:
            self.rect.top -= self.SPEED
        elif keys[pygame.K_s] and self.rect.bottom + self.SPEED <= self.HEIGHT:
            self.rect.bottom += self.SPEED
        elif keys[pygame.K_d] and self.rect.right + self.SPEED <= self.WIDTH:
            self.rect.right += self.SPEED
        elif keys[pygame.K_a] and self.rect.left - self.SPEED >= 0:
            self.rect.left -= self.SPEED