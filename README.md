# Introduction

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is one of the most famous examples of a [zero-player game](https://en.wikipedia.org/wiki/Zero-player_game).

To put it simply, we start with "cells" positioned in the plane. Following certain rules related to the number of nearby cells, some of those cells die while new ones are born.


The Game of Life has generated a substantial amount of mathematical research and has a (perhaps counter-intuitive) complex nature.

# Rules

To each point of the plane (integer coordinates), we associate a state: *live* or *dead*. Live points are considered "cells", representing the interpretation of the game as some kind of evolution of populations of cells.

For each point, the set of the eight points that are immediately adjacent to it is called its *neighbours*.

The transition from one state to the other of the game is then characterized by the following rules:

1. Every live point with exactly two or three neighbours remain live in the next state.
2. Every other live point becomes dead.
3. Every dead point with exactly three neighbours becomes live. 

Note that by "dead point" in (3) we mean dead **in the previous state**. So points that will become dead because of rule 2 are not counted here.


# Constants in the algorithm

The width and height of the screen displayed in the algorithm can be controlled by the `WIDTH` and `HEIGHT` constants, respectively. This applies if `BOUNDED_SCREEN`is set to `True`, in which case the screen will be limited to those dimensions.

If `BOUNDED_SCREEN` is set to `False`, then the screen size dinamically changes to adapt to the positions of the cells that
spawn/despawn.
# Unboundedness of the algorithm

The algorithm implemented in this repository is by nature **unbounded**, in the following sense: Even when `BOUNDED_SCREEN` is set to `False`, the algorithm is not being restricted to only verifying a bounded region of the plane; what is happening is that only a bounded region of the plane is **displayed**. 

This is due to the fact that live cells are stored as arrays and neighbours are checked in each step by means of the coordinates, so this does not depend on the selected size of what to display. This contrasts with another strategy which consists of selecting a region of the plane as a 2d-array and updating this region instead of the individual cells.

For more details, see [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Algorithms).