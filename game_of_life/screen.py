from __future__ import annotations

from itertools import product
from random import randint
from typing import Dict, List, NamedTuple, Tuple

Cell = NamedTuple("Cell", [("x", int),
                           ("y", int),
                           ("alive", bool)])


class Screen:

    def __init__(self,
                 alive_cells: List[Cell] = []) -> None:
        if not alive_cells:
            self.alive_cells = list(set([
                Cell(randint(-7, 7), randint(-7, 7), alive=True)
                for i in range(0, 80)
            ]))
        else:
            self.alive_cells = alive_cells

        self._square_side = 20
        self._min_x = 10
        self._min_y = 10
        self.alive_cells_hashmap: Dict[Tuple[int, int], Cell] = {
            (cell.x, cell.y): cell for cell in self.alive_cells
        }

    def get_neighbours(self, cell: Cell) -> List[Cell]:
        neighbour_cells: List[Cell] = []
        for (x, y) in product([-1, 0, 1], repeat=2):
            if (x, y) != (0, 0):
                if (cell.x + x, cell.y + y) in self.alive_cells_hashmap:
                    neighbour_cells.append(Cell(cell.x + x,
                                                cell.y + y, alive=True))
                else:
                    neighbour_cells.append(Cell(cell.x + x,
                                                cell.y + y, alive=False))
        return neighbour_cells

    def remove_cell(self, cell: Cell) -> None:
        if cell in self.alive_cells:
            self.alive_cells.remove(cell)
            self.alive_cells_hashmap.pop((cell.x, cell.y))

    def add_cell(self, cell: Cell) -> None:
        if cell not in self.alive_cells:
            self.alive_cells.append(cell)
            self.alive_cells_hashmap[(cell.x, cell.y)] = cell

    def get_screen(self, lines: int, columns: int, *,
                   bounded_screen: bool = True) -> List[List[int]]:
        """Lines and columns must be odd integers."""
        if lines % 2 == 0 or columns % 2 == 0:
            raise ValueError("Not odd.")

        if bounded_screen:
            screen = self._get_bounded_screen(lines, columns)
        else:
            screen = self._get_unbounded_screen()

        return screen

    def _get_unbounded_screen(self):
        if not self.alive_cells_hashmap:
            min_x = 0
            min_y = 0
            square_side = 20
        else:
            self._update_dimensions()
            min_x, min_y, square_side = (self._min_x, self._min_y,
                                         self._square_side)

        screen = [[0 for j in range(min_y-5,
                                    min_y+square_side+6)]
                  for i in range(min_x-5,
                                 min_x+square_side+6)]
        for (x, y) in self.alive_cells_hashmap:
            shifted_x = x - (min_x - 5)
            shifted_y = y - (min_y - 5)
            screen[shifted_x][shifted_y] = 1
        return screen

    def _get_bounded_screen(self, lines, columns):
        screen = [[0 for j in range(columns)]
                  for i in range(lines)]
        for (x, y) in self.alive_cells_hashmap:
            if (x in range(-(lines-1)//2, (lines-1)//2) and
                    y in range(-(columns-1)//2, (columns-1)//2)):
                shifted_x = x + (lines-1)//2
                shifted_y = y + (columns-1)//2
                screen[shifted_x][shifted_y] = 1
        return screen

    def _update_dimensions(self) -> None:
        max_x, min_x = (max(x for (x, y) in self.alive_cells_hashmap),
                        min(x for (x, y) in self.alive_cells_hashmap))
        max_y, min_y = (max(y for (x, y) in self.alive_cells_hashmap),
                        min(y for (x, y) in self.alive_cells_hashmap))

        min_x = min(min_x, self._min_x)
        self._min_x = min_x
        min_y = min(min_y, self._min_y)
        self._min_y = min_y

        square_side = max(max_y - min_y, max_x - min_x)
        square_side = max(self._square_side, square_side)
        self._square_side = square_side

    def print_screen(self, lines: int, columns: int) -> None:
        screen = self.get_screen(lines, columns)
        for line in screen:
            print("".join([str(x) for x in line]))
