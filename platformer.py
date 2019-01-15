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

            main_surface.fill(WHITE)

            position = pygame.mouse.get_pos()

            my_ball.move()
            my_ball.rect.x = position[0] - RADIUS_OF_BALL
            main_surface.blit(my_ball.image, my_ball.rect)

            pygame.display.update()


main()
