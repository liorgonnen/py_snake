from collections import deque
import pygame
from pygame import Surface
from src.const import *
from src.game_objects.game_object import GameObject
from src.utils import add


class Snake(GameObject):
    __direction: Direction
    __last_direction: Direction
    __segments: deque
    __can_change_direction: bool
    __grow_cycles_left: int

    def __init__(self):
        self.__segments = deque((MID_BOARD_X + x, MID_BOARD_Y) for x in range(3))
        self.__direction = Direction.RIGHT
        self.__last_direction = Direction.RIGHT
        self.__grow_cycles_left = 0

    def draw(self, surface: Surface):
        for segment in self.__segments:
            x = segment[0] * SNAKE_WIDTH
            y = segment[1] * SNAKE_WIDTH
            pygame.draw.rect(surface, color=WHITE, rect=(x, y, SNAKE_WIDTH, SNAKE_WIDTH))

    def update(self):
        # Remove the tail
        if self.__grow_cycles_left > 0:
            self.__grow_cycles_left -= 1
        else:
            self.__segments.popleft()

        new_head = add(self.head_position, self.__direction.vector)
        self.__segments.append(new_head)
        self.__last_direction = self.__direction

    def set_direction(self, direction: Direction):
        if self.__last_direction.directionality() != direction.directionality():
            self.__direction = direction
            self.__can_change_direction = False

    def grow(self, size: int):
        self.__grow_cycles_left += size

    @property
    def head_position(self):
        return self.__segments[-1]

    def is_colliding_with(self, pos: tuple) -> bool:
        return any(map(lambda segment: segment == pos, self.__segments))

    @property
    def is_self_colliding(self) -> bool:
        head = self.head_position
        return any(map(lambda pos: pos == head and pos is not head, self.__segments))


