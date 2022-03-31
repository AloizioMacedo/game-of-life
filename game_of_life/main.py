import time

import matplotlib.pyplot as plt

from game_rules import Game
from screen import Screen

WIDTH = 31
HEIGHT = 31


def main():
    screen = Screen()
    game = Game(screen)
    fig, ax = plt.subplots()
    ax.imshow(screen.get_screen(WIDTH, HEIGHT), extent=(
        (- (WIDTH-1)/2, (WIDTH-1)/2,
         - (HEIGHT-1)/2, (HEIGHT-1)/2)
        ))
    plt.ion()
    plt.show()

    while True:
        game.update_candidates()
        game.reproduce()
        game.kill()
        ax.imshow(screen.get_screen(WIDTH, HEIGHT), extent=(
            (- (WIDTH-1)/2, (WIDTH-1)/2,
             - (HEIGHT-1)/2, (HEIGHT-1)/2)
            ))
        fig.canvas.flush_events()
        time.sleep(1)


if __name__ == "__main__":
    main()
