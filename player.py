import pygame, sys
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, radius):
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = RED
        self.x_speed = 0
        self.y_speed = 0

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.

        self.image = pygame.Surface((RADIUS_OF_BALL * 2, RADIUS_OF_BALL * 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius, 0)

    def move(self):

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.bottom > APPLICATION_HEIGHT - RADIUS_OF_BALL:
            self.y_speed = - 10

        if self.rect.y < APPLICATION_HEIGHT - RADIUS_OF_BALL:
            self.y_speed += 0.3
