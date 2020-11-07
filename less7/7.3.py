class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        cells_result = self.cells + other.cells
        return cells_result

    def __sub__(self, other):
        cells_result = self.cells - other.cells
        if cells_result > 0:
            return cells_result
        else:
            raise ValueError("Из меньшего нельзя вычесть большее")

    def __mul__(self, other):
        cells_result = self.cells * other.cells
        return Cell(cells_result)

    def __truediv__(self, other):
        cells_result = self.cells // other.cells
        return Cell(cells_result)

    def make_order(self, max_cell):
        line = self.cells // max_cell
        residue = self.cells % max_cell
        print(("*" * max_cell + "\n") * line + ("*" * residue))


if __name__ == "__main__":
    a = Cell(16)
    b = Cell(9)
    c = a / b
    a.make_order(4)
