import pygame
from pygame import display, K_SPACE
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    QUIT,
)
from const import *


class Game:

    def __init__(self):
        from game_logic import GameLogic
        pygame.init()
        pygame.font.init()
        display.set_caption(WINDOW_TITLE)
        self.__screen = display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__quit = False
        self.__game_logic = GameLogic(self)

    def run_game_loop(self):
        clock = pygame.time.Clock()

        while not self.__quit:
            self.process_events()
            self.update_game_state()
            self.draw_frame()
            clock.tick(15)

    def update_game_state(self):
        self.__game_logic.update()

    def draw_frame(self):
        self.__screen.fill(BLACK)
        self.__game_logic.draw(self.__screen)
        display.flip()

    def process_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                self.__quit = True

        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            self.__game_logic.on_direction_key(Direction.UP)
        if keys[K_DOWN]:
            self.__game_logic.on_direction_key(Direction.DOWN)
        if keys[K_LEFT]:
            self.__game_logic.on_direction_key(Direction.LEFT)
        if keys[K_RIGHT]:
            self.__game_logic.on_direction_key(Direction.RIGHT)

        if keys[K_SPACE]:
            self.__game_logic.on_key(K_SPACE)


