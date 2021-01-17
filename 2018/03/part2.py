from pathlib import Path

puzzle_input_raw = (Path(__file__).parent / "input.txt").read_text()

import re
from collections import defaultdict

claims = [tuple(int(x) for x in re.findall(r"(\d+)", x)[1:]) for x in puzzle_input_raw.splitlines()]

fabric = defaultdict(int)
for x, y, w, h in claims:
    for xf in range(x, x + w):
        for yf in range(y, y + h):
            fabric[(xf, yf)] += 1


for claim, (x, y, w, h) in enumerate(claims, start=1):
    if all(fabric[(xf, yf)] == 1 for xf in range(x, x + w) for yf in range(y, y + h)):
        print(claim)
        break