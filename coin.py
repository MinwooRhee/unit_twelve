import pygame, random
from settings import *


class Coin(pygame.sprite.Sprite):

    def __init__(self):
        """
        load the image for the coin.
        gives the coin a random velocity.
        :return: None
        """
        # initialize sprite super class.
        super().__init__()

        # the coin moves at a random velocity.
        self.x_speed = random.randint(- 5, 5)
        self.y_speed = random.randint(- 5, 5)

        # load the image file of a coin.
        self.image = pygame.image.load("dollar.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()

    def move(self):
        """
        the coin moves and bounces off the screen.
        :return: None
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left <= 0 or self.rect.right >= APPLICATION_WIDTH:
            self.x_speed = - self.x_speed
        if self.rect.top <= 0 or self.rect.bottom >= APPLICATION_HEIGHT:
            self.y_speed = - self.y_speed
