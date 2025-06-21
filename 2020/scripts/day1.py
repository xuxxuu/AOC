from pathlib import Path
from itertools import combinations

def get_data(year: int, day: int):
    """./inputs/{day}.txt"""
    cwd = Path().cwd()
    year_dir = Path(f"{year}")
    filepath = Path(f"inputs/{day}.txt")
    with open(cwd / year_dir / filepath) as f:
        data = f.read().strip().split("\n")
    
    return data

def get_test_data(year: int, day: int):
    cwd = Path().cwd()
    year_dir = Path(f"{year}")
    filepath = Path(f"tests/{day}_test.txt")
    with open(cwd / year_dir / filepath) as f:
        data = f.read().strip().split("\n")
    
    return data


data = list(map(int, get_data(2020, 1)))

# part 1
target = 2020
pairs = combinations(data, 2)
print("".join(f"{a} * {b} = {a*b}" for a, b in pairs if a + b == target))


# part 2
trips = combinations(data, 3)
print("".join(f"{a} * {b} * {c} = {a*b*c}" for a, b, c in trips if a + b + c == target))