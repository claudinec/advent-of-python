"""Main command-line interface for Advent of Code exercises in Python.
"""


from datetime import datetime, timezone, timedelta
from pathlib import Path

import click


AOC_ROOT = Path(__file__).parent
AOC_MIN_YEAR = 2015
AOC_MAX_DAY = 25
AOC_TZ = timezone(timedelta(hours=-5))
AOC_DT = datetime.now(tz=AOC_TZ)
CURRENT_YEAR = AOC_DT.year
AOC_CURRENT_BEGIN = datetime(CURRENT_YEAR, 12, 1, 0, 0, 0, tzinfo=AOC_TZ)
AOC_CURRENT_END = datetime(CURRENT_YEAR, 12, 25, 0, 0, 0, tzinfo=AOC_TZ)
if AOC_DT < AOC_CURRENT_BEGIN:
    AOC_MAX_YEAR = CURRENT_YEAR - 1
else:
    AOC_MAX_YEAR = CURRENT_YEAR
    if AOC_DT >= AOC_CURRENT_END:
        AOC_CURRENT_MAX_DAY = 25
    else:
        AOC_CURRENT_MAX_DAY = AOC_DT.day


def check_valid_year(year: int):
    if year > CURRENT_YEAR:
        raise Exception("Year is in the future")
    elif year == CURRENT_YEAR and AOC_DT < AOC_CURRENT_BEGIN:
        raise Exception("This year's puzzles haven't started yet")
    else:
        print("Puzzles are available for " + str(year))


@click.group()
def main():
    click.echo("Advent of Code")


@main.command()
@click.option(
    "--year",
    type=click.IntRange(AOC_MIN_YEAR, AOC_MAX_YEAR),
    default=AOC_MAX_YEAR,
    show_default=True,
)
def create(year: int):
    """Create directory structure for given year.
    """
    aoc_dir = f"aoc{year:04d}"
    aoc_path = AOC_ROOT.joinpath(aoc_dir)
    if aoc_path.exists():
        if aoc_path.is_dir():
            click.echo("Directory exists at this path: " + str(aoc_path), err=True)
        else:
            click.echo("File exists at this path: " + str(aoc_path), err=True)
    else:
        aoc_path.mkdir()
        data_path = aoc_path.joinpath("data")
        data_path.mkdir()
        click.echo("Created directories:")
        click.echo(str(aoc_path))
        click.echo(str(data_path))


@main.command()
def list():
    """List available puzzle years.
    """
    click.echo("Puzzles are available for these years:")
    for year in range(AOC_MIN_YEAR, AOC_MAX_YEAR + 1):
        click.echo(year)


@main.command()
@click.option(
    "--year",
    type=click.IntRange(AOC_MIN_YEAR, AOC_MAX_YEAR),
    default=AOC_MAX_YEAR,
    show_default=True,
)
@click.option(
    "--day",
    type=click.IntRange(1, AOC_MAX_DAY),
    default=AOC_MAX_DAY,
    show_default=True,
)
def run(year: int, day: int):
    """Run code for given year and day.
    """
    if year == CURRENT_YEAR and AOC_DT < AOC_CURRENT_BEGIN:
        click.echo("Too early, try a previous year", err=True)
    else:
        aoc_dir = f"aoc{year:04d}"
        aoc_path = Path(aoc_dir)
        if day is None:
            if year == CURRENT_YEAR:
                day = AOC_CURRENT_MAX_DAY
            else:
                day = AOC_MAX_DAY
        day_str = f"day{day:02d}"
        code_path = aoc_path.joinpath(f"{day_str}.py")
        data_path = aoc_path.joinpath("data")
        data_files = [
            data_path.joinpath(f"{day_str}-example.txt"),
            data_path.joinpath(f"{day_str}-input.txt"),
        ]


if __name__ == "__main__":
    main()
