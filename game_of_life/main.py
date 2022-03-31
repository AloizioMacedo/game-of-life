import time

import matplotlib.pyplot as plt

from game_rules import Game
from screen import Screen

WIDTH = 61
HEIGHT = 61

PERIOD = 0.2


def main():
    screen = Screen()
    game = Game(screen)
    fig, ax = plt.subplots()
    imshow = ax.imshow(screen.get_screen(WIDTH, HEIGHT), extent=(
        (- (WIDTH-1)/2, (WIDTH-1)/2,
         - (HEIGHT-1)/2, (HEIGHT-1)/2)
        ))
    plt.ion()
    plt.show()

    while True:
        start_of_loop = time.time()

        game.update_candidates()
        game.game_step()

        imshow.set_data(screen.get_screen(WIDTH, HEIGHT))
        fig.canvas.draw()
        plt.pause(0.01)  # type: ignore

        end_of_loop = time.time()
        if end_of_loop - start_of_loop <= PERIOD:
            time.sleep(PERIOD - (end_of_loop - start_of_loop))


if __name__ == "__main__":
    main()
