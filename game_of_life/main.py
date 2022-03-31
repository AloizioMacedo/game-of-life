import time

import matplotlib.pyplot as plt

from game_rules import Game
from screen import Screen


def main():
    screen = Screen()
    game = Game(screen)
    plt.imshow(screen.get_screen(31, 31))
    plt.show()

    while True:
        game.update_candidates()
        game.kill()
        game.reproduce()
        plt.imshow(screen.get_screen(31, 31))
        plt.show()
        time.sleep(1)


if __name__ == "__main__":
    main()
