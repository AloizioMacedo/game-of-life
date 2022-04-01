import time

import matplotlib.pyplot as plt

from game_rules import Game
from screen import Screen

BOUNDED_SCREEN = True
WIDTH = 65
HEIGHT = 65

PERIOD = 0.2


def exit_on_window_closure(event, game: Game) -> None:
    game.on = False


def update_display(screen, fig, imshow):
    imshow.set_data(screen.get_screen(WIDTH, HEIGHT,
                                      bounded_screen=BOUNDED_SCREEN))
    fig.canvas.draw()
    plt.pause(0.01)  # type: ignore


def prepare_fig_and_imshow(screen, game):
    fig, ax = plt.subplots()

    if not BOUNDED_SCREEN:
        imshow = ax.imshow(screen.get_screen(WIDTH, HEIGHT,
                                             bounded_screen=False))
    else:
        imshow = ax.imshow(screen.get_screen(WIDTH, HEIGHT), extent=(
            (-(WIDTH-1)/2, (WIDTH-1)/2,
             -(HEIGHT-1)/2, (HEIGHT-1)/2)
            ))

    plt.ion()
    plt.show()

    fig.canvas.mpl_connect('close_event',
                           lambda event: exit_on_window_closure(event, game))

    return fig, imshow


def main():
    screen = Screen()
    game = Game(screen)
    fig, imshow = prepare_fig_and_imshow(screen, game)

    while game.on:
        start_of_loop = time.time()

        game.update_candidates()
        game.game_step()

        update_display(screen, fig, imshow)

        end_of_loop = time.time()
        if end_of_loop - start_of_loop <= PERIOD:
            time.sleep(PERIOD - (end_of_loop - start_of_loop))

    exit()


if __name__ == "__main__":
    main()
