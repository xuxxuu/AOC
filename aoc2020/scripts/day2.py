from pathlib import Path

tests_dir = Path(__file__).absolute().parent.parent / Path("tests/")
input_dir = Path(__file__).absolute().parent.parent / Path("inputs/")

with open(tests_dir / "2.txt") as f:
    data = f.read().strip().split()