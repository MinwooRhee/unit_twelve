import pygame, sys, player, coin, enemy
from pygame.locals import *
from settings import *


def main():

    pygame.init()
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption(TITLE)
    main_surface.fill(WHITE)

    my_ball = player.Player(RADIUS_OF_BALL)
    my_ball.rect.x = 20
    my_ball.rect.y = APPLICATION_HEIGHT - 20

    coin_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    for x in range(10):
        my_coin = coin.Coin()
        my_coin.rect.x = APPLICATION_WIDTH/2
        my_coin.rect.y = APPLICATION_HEIGHT/2
        coin_group.add(my_coin)

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    my_ball.y_speed = - 6

                if len(coin_group) == 0:
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
            my_ball.collide(coin_group, enemy_group)

            for x in coin_group:
                x.move()
                main_surface.blit(x.image, x.rect)

            for x in enemy_group:
                x.move()
                main_surface.blit(x.image, x.rect)

            pygame.display.update()

main()
