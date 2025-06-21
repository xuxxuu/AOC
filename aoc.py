import typer
from pathlib import Path

app = typer.Typer()


@app.command()
def initialize_directory(year: int):
    """Folder Name: Year of the event
    contents: day{day_number}.py for each day,
    {day_number}_test.txt, {day_number}.txt"""
    Path(f"./{year}/scripts/").mkdir(parents=True)
    Path(f"./{year}/tests/").mkdir()
    Path(f"./{year}/inputs/").mkdir()
    for day in range(1, 26):
        Path(f"./{year}/scripts/day{day}.py").touch()
        Path(f"./{year}/tests/{day}_test.txt").touch()
        Path(f"./{year}/inputs/{day}.txt").touch()
 

if __name__ == '__main__':
    app()