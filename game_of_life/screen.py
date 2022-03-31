from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from random import randint
from typing import Dict, List, Tuple


@dataclass
class Cell:
    x: int
    y: int
    alive: bool

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.alive))


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

    def get_screen(self, lines: int, columns: int) -> List[List[int]]:
        """Lines and columns must be odd integers."""
        if lines % 2 == 0 or columns % 2 == 0:
            raise ValueError("Not odd.")
        initialized_screen = [[0 for j in range(columns)]
                              for i in range(lines)]
        for x in range(-(lines-1)//2, (lines-1)//2):
            for y in range(-(columns-1)//2, (columns-1)//2):
                cell = self.alive_cells_hashmap.get(
                    (x, y),
                    None)
                if cell is not None:
                    initialized_screen[
                        x + (lines-1)//2
                        ][y + (columns-1)//2] = 1
        return initialized_screen

    def print_screen(self, lines: int, columns: int) -> None:
        screen = self.get_screen(lines, columns)
        for line in screen:
            print("".join([str(x) for x in line]))
