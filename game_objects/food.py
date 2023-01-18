from random import randint

import pygame
from pygame.surface import Surface
from const import *
from game_objects.game_object import GameObject


class Food(GameObject):
    __position: tuple

    def __init__(self):
        self.move()

    def update(self):
        super().update()

    def draw(self, surface: Surface):
        x = self.__position[0] * SNAKE_WIDTH + HALF_SNAKE_WIDTH
        y = self.__position[1] * SNAKE_WIDTH + HALF_SNAKE_WIDTH

        pygame.draw.circle(surface, RED, (x, y), HALF_SNAKE_WIDTH)

    @property
    def position(self):
        return self.__position

    def move(self):
        self.__position = (randint(0, BOARD_WIDTH - 1), randint(0, BOARD_HEIGHT - 1))
