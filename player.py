import pygame
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, radius):
        """
        creates the red ball that the player controls.
        the ball does not go off the screen.
        :param radius: radius of the ball
        """
        # initialize sprite super class.
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = RED
        self.x_speed = 0
        self.y_speed = 0
        self.life = 3

        # set a sound it will play when the player collects a coin.
        self.coin_sound = pygame.mixer.Sound("nice-work.wav")

        # creating a surface and getting rect coordinate
        self.image = pygame.Surface((RADIUS_OF_BALL * 2, RADIUS_OF_BALL * 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, RED, (radius, radius), radius, 0)

    def move(self):
        """
        The ball does not go off the screen.
        The ball accelerates downward when it is above in the air, as if there is gravity.
        :return: None
        """

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # prevents the ball from going off the screen sideways.
        if self.rect.left <= 0:
            self.x_speed = 1
        if self.rect.right >= APPLICATION_WIDTH:
            self.x_speed = - 1

        # prevents the ball from going off the screen above.
        if self.rect.top <= 0:
            self.y_speed = - self.y_speed

        # prevents the ball from falling off the screen.
        if self.rect.bottom > APPLICATION_HEIGHT:
            self.y_speed = - 1

        # when the ball is above in the air, the speed of the ball increase like how the gravity works.
        if self.rect.y < APPLICATION_HEIGHT - RADIUS_OF_BALL:
            self.y_speed += 0.3

    def collide(self, coin_group, enemy_group):
        """
        when the ball collides with coins, the coins disappear and the sound plays.
        when the ball collides with enemies, a life is lost and the ball is placed back at the starting point.
        when life is 0, exits the program.
        :param coin_group: sprite group of coins
        :param enemy_group: sprite group of enemies
        :return: None
        """

        if pygame.sprite.spritecollide(self, coin_group, True):
            # plays the sound
            self.coin_sound.play()

        if pygame.sprite.spritecollide(self, enemy_group, False):

            # put the ball back at the starting position
            self.rect.x = 20
            self.rect.y = APPLICATION_HEIGHT - 20

            # when life is 0, exits the program.
            self.life -= 1
            if self.life == 0:
                exit()
