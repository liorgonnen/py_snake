import pygame.font
from pygame.surface import Surface

from src.const import *
from src.game_objects.game_object import GameObject


class Score(GameObject):

    __text: Surface

    def __init__(self):
        self.__score = 0
        self.__font = pygame.font.SysFont(FONT, SNAKE_WIDTH)
        self.render()

    def increase(self):
        self.__score += 1
        self.render()

    def draw(self, surface: Surface):
        surface.blit(self.__text, ((SCREEN_WIDTH - self.__text.get_width()) // 2, 0))

    def render(self):
        self.__text = self.__font.render(f"Score: {self.__score}", True, WHITE)
