from pathlib import Path

from rich import print

with (Path(__file__).parent / "input.txt").open() as puzzle_input_file:
    puzzle_input_raw = puzzle_input_file.read()

import re
import functools

grid_data, fold_data = puzzle_input_raw.split("\n\n")
grid = {(int(x), int(y)) for x, y in (c.split(",") for c in grid_data.splitlines())}
folds = [re.search(r"(x|y)=(\d+)$", x).groups() for x in fold_data.splitlines()]
folds = [(d, int(n)) for d, n in folds]

def fold(grid, fold_instr):
    direction, middle_line = fold_instr
    if direction == "x":
        grid = {(x, y) for x, y in grid if x < middle_line} | {(middle_line - (x - middle_line), y) for x, y in grid if x > middle_line}
    else:
        grid = {(x, y) for x, y in grid if y < middle_line} | {(x, middle_line - (y - middle_line)) for x, y in grid if y > middle_line}
    return grid

grid = functools.reduce(fold, folds, grid)

x_max = max(pos[0] for pos in grid)
y_max = max(pos[1] for pos in grid)
for y in range(y_max + 1):
    for x in range(x_max + 1):
        print("█" if (x, y) in grid else " ", end="")
    print()