import time

import matplotlib.pyplot as plt

from game_rules import Game
from screen import Screen

WIDTH = 65
HEIGHT = 65

PERIOD = 0.2


def exit_on_window_closure(event, game: Game) -> None:
    game.on = False


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
    fig.canvas.mpl_connect('close_event',
                           lambda event: exit_on_window_closure(event, game))

    while game.on:
        start_of_loop = time.time()

        game.update_candidates()
        game.game_step()

        imshow.set_data(screen.get_screen(WIDTH, HEIGHT))
        fig.canvas.draw()
        plt.pause(0.01)  # type: ignore

        end_of_loop = time.time()
        if end_of_loop - start_of_loop <= PERIOD:
            time.sleep(PERIOD - (end_of_loop - start_of_loop))

    exit()


if __name__ == "__main__":
    main()
