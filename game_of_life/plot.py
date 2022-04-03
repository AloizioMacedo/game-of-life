import matplotlib.pyplot as plt

from game_rules import Game
from screen import Screen


def prepare_fig_and_imshow(screen: Screen, game: Game,
                           width: int, height: int, *,
                           bounded_screen: bool):
    fig, ax = plt.subplots()

    if not bounded_screen:
        imshow = ax.imshow(screen.get_screen(width, height,
                                             bounded_screen=False))
    else:
        imshow = ax.imshow(screen.get_screen(width, height), extent=(
            (-(width-1)/2, (width-1)/2,
             -(height-1)/2, (height-1)/2)
            ))

    plt.ion()
    plt.show()

    fig.canvas.mpl_connect('close_event',
                           lambda event: exit_on_window_closure(event, game))

    return fig, imshow


def exit_on_window_closure(event, game: Game) -> None:
    game.on = False


def update_display(screen: Screen, width: int, height: int,
                   fig, imshow, *, bounded_screen: bool):
    imshow.set_data(screen.get_screen(width, height,
                                      bounded_screen=bounded_screen))
    fig.canvas.draw()
    plt.pause(0.01)  # type: ignore
