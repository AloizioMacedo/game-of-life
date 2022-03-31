from typing import List, Set

from screen import Cell, Screen


class Game:

    def __init__(self, screen: Screen) -> None:
        self.screen = screen
        self.candidates_to_be_born: Set[Cell] = set()
        self.candidates_to_die: Set[Cell] = set()

    def update_candidates(self) -> None:
        for cell in self.screen.alive_cells:
            cells = self.screen.get_neighbours(cell)
            self.candidates_to_be_born.update([cell for cell in cells
                                               if not cell.alive])
        self.candidates_to_die.update(self.screen.alive_cells)
        return None

    def kill(self) -> None:
        for cell in self.candidates_to_die:
            neighbours = self.screen.get_neighbours(cell)
            if len([cell for cell in neighbours if cell.alive]) in [2, 3]:
                continue
            else:
                self.screen.remove_cell(cell)
        return None

    def reproduce(self) -> None:
        for cell in self.candidates_to_be_born:
            neighbours = self.screen.get_neighbours(cell)
            if len([cell2 for cell2 in neighbours if cell2.alive]) == 3:
                cell.alive = True
                self.screen.add_cell(cell)
        return None