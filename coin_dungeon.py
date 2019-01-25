# Minwoo Rhee
# 20190125
# 20190125 11:00 AM
# coin_dungeon.py
# player has to dodge enemies and collect coins using mouse

import pygame, sys, player, coin, enemy
from pygame.locals import *
from settings import *


def main():
    """
    set the window, place the ball, coins and enemies and put them in sprite groups.
    ball moves in the direction of the mouse.
    When there are no more coins left, end the program.
    :return: None
    """

    # initializing and setting windows
    pygame.init()
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption(TITLE)
    main_surface.fill(WHITE)

    # placing the ball at the left bottom corner
    my_ball = player.Player(RADIUS_OF_BALL)
    my_ball.rect.x = 20
    my_ball.rect.y = APPLICATION_HEIGHT - 20

    # empty groups to later add coins and enemies
    coin_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    # place coins
    for x in range(15):
        my_coin = coin.Coin()
        my_coin.rect.x = APPLICATION_WIDTH/2
        my_coin.rect.y = APPLICATION_HEIGHT/2
        coin_group.add(my_coin)

    # place enemies
    for x in range(3):
        my_enemy = enemy.Enemy()
        my_enemy.rect.x = APPLICATION_WIDTH / 2
        my_enemy.rect.y = APPLICATION_HEIGHT / 2
        enemy_group.add(my_enemy)

    while True:
            for event in pygame.event.get():

                if event == QUIT:
                    pygame.quit()
                    sys.exit()

                # the ball jumps when player clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    my_ball.y_speed = - 6

                # when all the coins are collected, end the program
                if len(coin_group) == 0:
                    pygame.quit()
                    sys.exit()

                position = pygame.mouse.get_pos()

                # if mouse is near the ball, ball does not move sideways
                if abs(my_ball.rect.x + RADIUS_OF_BALL - position[0]) < 25:
                    my_ball.x_speed = 0

                # if mouse is away from the ball, the ball follows the mouse at a constant speed
                elif my_ball.rect.x + RADIUS_OF_BALL > position[0]:
                    my_ball.x_speed = - 3
                elif my_ball.rect.x + RADIUS_OF_BALL < position[0]:
                    my_ball.x_speed = 3

            # fill the surface to erase the trace of sprites
            main_surface.fill(WHITE)

            # move, collide and blit the ball
            my_ball.move()
            my_ball.collide(coin_group, enemy_group)
            main_surface.blit(my_ball.image, my_ball.rect)

            # move and blit coins
            for x in coin_group:
                x.move()
                main_surface.blit(x.image, x.rect)

            # move and blit enemies
            for x in enemy_group:
                x.move()
                main_surface.blit(x.image, x.rect)

            pygame.display.update()


main()
