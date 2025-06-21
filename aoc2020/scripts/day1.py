from pathlib import Path
from itertools import combinations
tests_dir = Path(__file__).absolute().parent.parent / Path("tests/")
input_dir = Path(__file__).absolute().parent.parent / Path("inputs/")

with open(input_dir / "1.txt") as f:
    data = f.read().strip().split("\n")


data = list(map(int, data))

# part 1
target = 2020
pairs = combinations(data, 2)
print("".join(f"{a} * {b} = {a*b}" for a, b in pairs if a + b == target))


# part 2
trips = combinations(data, 3)
print("".join(f"{a} * {b} * {c} = {a*b*c}" for a, b, c in trips if a + b + c == target))