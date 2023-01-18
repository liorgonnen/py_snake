from enum import Enum

WINDOW_TITLE = "PySnake"
GAME_OVER_TEXT = "Game Over"
FONT = "Courier New"

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

SNAKE_WIDTH = 20
HALF_SNAKE_WIDTH = SNAKE_WIDTH // 2

BOARD_WIDTH = SCREEN_WIDTH // SNAKE_WIDTH
BOARD_HEIGHT = SCREEN_HEIGHT // SNAKE_WIDTH

MID_BOARD_X = BOARD_WIDTH // 2
MID_BOARD_Y = BOARD_HEIGHT // 2


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

SCREEN_DIRECTION = [
    (0, -1),  # Direction.UP
    (0, 1),  # Direction.DOWN
    (-1, 0),  # Direction.LEFT
    (1, 0)  # Direction.RIGHT
]


class Directionality(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @property
    def vector(self) -> tuple:
        return SCREEN_DIRECTION[self.value]

    def directionality(self) -> Directionality:
        return Directionality.HORIZONTAL if self in [Direction.LEFT, Direction.RIGHT] else Directionality.VERTICAL
