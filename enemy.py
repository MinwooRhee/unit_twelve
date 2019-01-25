import pygame, random
from settings import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters

        self.x_speed = random.randint(- 5, 5)
        self.y_speed = random.randint(- 5, 5)

        # Create a surface with the correct height and width
        self.image = pygame.image.load("dragon.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left <= 0 or self.rect.right >= APPLICATION_WIDTH:
            self.x_speed = - self.x_speed
        if self.rect.top <= 0 or self.rect.bottom >= APPLICATION_HEIGHT:
            self.y_speed = - self.y_speed
