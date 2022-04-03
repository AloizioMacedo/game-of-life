import time

from game_rules import Game
from plane import Plane
from plot import prepare_fig_and_imshow, update_display

BOUNDED_SCREEN = True
WIDTH = 65
HEIGHT = 65

PERIOD = 0.2


def main():
    plane = Plane()
    game = Game(plane)
    fig, imshow = prepare_fig_and_imshow(plane, game,
                                         WIDTH, HEIGHT,
                                         bounded_screen=BOUNDED_SCREEN)

    while game.on:
        start_of_loop = time.time()

        game.update_candidates()
        game.game_step()

        update_display(plane, WIDTH, HEIGHT, fig, imshow,
                       bounded_screen=BOUNDED_SCREEN)

        end_of_loop = time.time()
        if end_of_loop - start_of_loop <= PERIOD:
            time.sleep(PERIOD - (end_of_loop - start_of_loop))

    exit()


if __name__ == "__main__":
    main()
