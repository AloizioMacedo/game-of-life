from typing import List, Set

from plane import Cell, Plane


class Game:

    def __init__(self, plane: Plane) -> None:
        self.plane = plane
        self.on = True
        self.candidates_to_be_born: Set[Cell] = set()
        self.candidates_to_die: Set[Cell] = set()

    def update_candidates(self) -> None:
        self.candidates_to_be_born.clear()
        self.candidates_to_die.clear()

        for cell in self.plane.alive_cells:
            cells = self.plane.get_neighbours(cell)
            self.candidates_to_be_born.update([cell for cell in cells
                                               if not cell.alive])
        self.candidates_to_die.update(self.plane.alive_cells)
        return None

    def game_step(self) -> None:
        who_dies = self.determine_who_dies()
        who_is_born = self.determine_who_is_born()

        for cell in who_dies:
            self.plane.remove_cell(cell)
        for cell in who_is_born:
            self.plane.add_cell(cell)

        return None

    def determine_who_dies(self) -> List[Cell]:
        to_die: List[Cell] = []
        for cell in self.candidates_to_die:
            neighbours = self.plane.get_neighbours(cell)
            if len([cell for cell in neighbours if cell.alive]) in [2, 3]:
                continue
            else:
                to_die.append(cell)
        return to_die

    def determine_who_is_born(self) -> List[Cell]:
        to_be_born: List[Cell] = []
        for cell in self.candidates_to_be_born:
            neighbours = self.plane.get_neighbours(cell)
            if len([cell2 for cell2 in neighbours if cell2.alive]) == 3:
                spawned_cell = Cell(cell.x, cell.y, True)
                to_be_born.append(spawned_cell)
        return to_be_born
