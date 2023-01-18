import pygame.font
from pygame.surface import Surface

from src.const import *
from src.game_objects.game_object import GameObject


class GameOverBanner(GameObject):

    __text: Surface

    def __init__(self):
        self.__is_visible = False
        font = pygame.font.SysFont(FONT, SNAKE_WIDTH)
        self.__text = font.render(GAME_OVER_TEXT, True, WHITE)

    def set_visible(self, is_over):
        self.__is_visible = is_over

    def draw(self, surface: Surface):
        if self.__is_visible:
            x = (SCREEN_WIDTH - self.__text.get_width()) // 2
            y = (SCREEN_HEIGHT - self.__text.get_height()) // 2
            surface.blit(self.__text, (x, y))
