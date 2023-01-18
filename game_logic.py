from pygame import K_SPACE
from pygame.surface import Surface

from const import *
from game_objects.game_object import GameObject
from game_objects.food import Food
from game_objects.game_over_banner import GameOverBanner
from game_objects.score import Score
from game_objects.snake import Snake


class GameLogic(GameObject):
    __food: Food
    __snake: Snake
    __score: Score
    __game_over_banner: GameOverBanner
    __game_over: bool
    __game_objects: list

    def __init__(self, game):
        self.__game = game
        self.start_new_game()

    def update(self):
        if not self.__game_over:
            self.update_game_state()

    def update_game_state(self):
        for obj in self.__game_objects:
            obj.update()

        self.detect_wall_collision()
        self.detect_food_collision()
        self.detect_self_collision()

    def detect_wall_collision(self):
        head = self.__snake.head_position
        head_x = head[0]
        head_y = head[1]
        if head_x < 0 or head_y < 0 or head_x >= BOARD_WIDTH or head_y >= BOARD_HEIGHT:
            self.on_game_over()

    def detect_food_collision(self):
        if self.__food.position == self.__snake.head_position:
            self.__snake.grow(2)
            self.__score.increase()
            self.move_food()

    def move_food(self):
        self.__food.move()

        # a quick hack to hopefully prevent the food appearing on top of the snake
        attempts = 5
        while self.__snake.is_colliding_with(self.__food.position) and attempts > 0:
            attempts -= 1
            self.__food.move()

    def detect_self_collision(self):
        if self.__snake.is_self_colliding:
            self.on_game_over()

    def draw(self, surface: Surface):
        for obj in self.__game_objects:
            obj.draw(surface)

    def on_direction_key(self, direction: Direction):
        self.__snake.set_direction(direction)

    def on_key(self, key):
        if self.__game_over and key == K_SPACE:
            self.start_new_game()

    def on_game_over(self):
        self.__game_over = True
        self.__game_over_banner.set_visible(True)

    def start_new_game(self):
        self.__game_over = False
        self.__snake = Snake()
        self.__food = Food()
        self.__score = Score()
        self.__game_over_banner = GameOverBanner()
        self.__game_objects = [self.__snake, self.__food, self.__score, self.__game_over_banner]


