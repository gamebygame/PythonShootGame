#!/usr/bin/env python3

import pygame
from pygame.locals import *
from sys import exit


UI_WIDTH = 480
UI_HEIGHT = 800


pygame.init()
ui = pygame.display.set_mode((UI_WIDTH, UI_HEIGHT))
pygame.display.set_caption('shoot plan yeah!')

# background image
background = pygame.image.load('resources/image/background.png')

# plan image
plane_img = pygame.image.load('resources/image/shoot.png')
player_rect = pygame.Rect(0, 99, 102, 126)
player = plane_img.subsurface(player_rect)
player_pos = [200, 600]


while True:
    ui.blit(background, (0, 0))
    ui.blit(player, player_pos)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # listen keyboard interaction
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_UP]:
        player_pos[1] -= 3
    if key_pressed[K_DOWN]:
        player_pos[1] += 3
    if key_pressed[K_LEFT]:
        player_pos[0] -= 3
    if key_pressed[K_RIGHT]:
        player_pos[0] += 3
