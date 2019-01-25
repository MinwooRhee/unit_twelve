import pygame
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, radius):
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = RED
        self.x_speed = 0
        self.y_speed = 0
        self.lives = 3
        self.coin_sound = pygame.mixer.Sound("nice-work.wav")

        # creating a surface and getting rect coordinate
        self.image = pygame.Surface((RADIUS_OF_BALL * 2, RADIUS_OF_BALL * 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, RED, (radius, radius), radius, 0)

    def move(self):

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left <= 0 :
            self.x_speed = 1
        if self.rect.right >= APPLICATION_WIDTH:
            self.x_speed = - 1

        if self.rect.top <= 0:
            self.y_speed = - self.y_speed

        if self.rect.bottom > APPLICATION_HEIGHT:
            self.y_speed = - 1

        if self.rect.y < APPLICATION_HEIGHT - RADIUS_OF_BALL:
            self.y_speed += 0.3

    def collide(self, coin_group, enemy_group):

        if pygame.sprite.spritecollide(self, coin_group, True):
            self.coin_sound.play()
            pass
        if pygame.sprite.spritecollide(self, enemy_group, False):
            self.lives -= 1
            self.rect.x = 20
            self.rect.y = APPLICATION_HEIGHT - 20
            if self.lives == 0:
                exit()
