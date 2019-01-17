import pygame, sys, player
from pygame.locals import *
from settings import *


def main():

    pygame.init()
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption(TITLE)
    main_surface.fill(WHITE)

    my_ball = player.Player(RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH/2
    my_ball.rect.y = APPLICATION_HEIGHT/2

    while True:
            for event in pygame.event.get():

                if event == QUIT:
                    pygame.quit()
                    sys.exit()

                position = pygame.mouse.get_pos()

                if abs(my_ball.rect.x + RADIUS_OF_BALL - position[0]) < 25:
                    my_ball.x_speed = 0
                elif my_ball.rect.x + RADIUS_OF_BALL > position[0]:
                    my_ball.x_speed = - 3
                elif my_ball.rect.x + RADIUS_OF_BALL < position[0]:
                    my_ball.x_speed = 3



            main_surface.fill(WHITE)


            my_ball.move()
            main_surface.blit(my_ball.image, my_ball.rect)

            pygame.display.update()


clock = pygame.time.Clock()
clock.tick(300)

main()
