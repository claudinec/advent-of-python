"""Main command-line interface for Advent of Code exercises in Python.
"""

from datetime import datetime, timezone, timedelta
from pathlib import Path

import click

AOC_MIN_YEAR = 2015
AOC_MAX_DAY = 25
AOC_TZ = timezone(timedelta(hours=-5))
LOCAL_TZ = timezone(timedelta(hours=11))
LOCAL_DT = datetime.now(tz=LOCAL_TZ)
CURRENT_YEAR = LOCAL_DT.year
AOC_CURRENT_BEGIN = datetime(CURRENT_YEAR, 12, 1, 0, 0, 0, tzinfo=AOC_TZ)
AOC_CURRENT_END = datetime(CURRENT_YEAR, 12, 25, 0, 0, 0, tzinfo=AOC_TZ)
if LOCAL_DT < AOC_CURRENT_BEGIN:
    AOC_MAX_YEAR = CURRENT_YEAR - 1
else:
    AOC_MAX_YEAR = CURRENT_YEAR
    if LOCAL_DT >= AOC_CURRENT_END:
        AOC_CURRENT_MAX_DAY = 25
    else:
        AOC_CURRENT_MAX_DAY = int(LOCAL_DT.strftime("%d"))

@click.group()
def main():
    click.echo('Advent of Code')

@main.command()
@click.option("--aoc-year", type=click.IntRange(AOC_MIN_YEAR, AOC_MAX_YEAR), default=AOC_MAX_YEAR, show_default=True)
def create(aoc_year: int):
    # Create directory structure for given year.
    aoc_dir = f'aoc{aoc_year:04d}'
    aoc_path = Path(aoc_dir)
    if aoc_path.exists():
        if aoc_path.is_dir():
            click.echo('Directory exists at this path', err=True)
        else:
            click.echo('File exists at this path', err=True)
    else:
        aoc_path.mkdir()
        data_path = aoc_path.joinpath('data')
        data_path.mkdir()
        click.echo('Created directories:')
        click.echo(str(aoc_path))
        click.echo(str(data_path))

@main.command()
def list_years():
    # List available years.
    click.echo('Puzzles are available for these years:')
    for year in range(AOC_MIN_YEAR, AOC_MAX_YEAR + 1):
        click.echo(year)

@main.command()
@click.option("--aoc-year", type=click.IntRange(AOC_MIN_YEAR, AOC_MAX_YEAR), default=AOC_MAX_YEAR, show_default=True)
@click.option("--aoc-day", type=click.IntRange(1, AOC_MAX_DAY), default=AOC_MAX_DAY, show_default=True)
def run(aoc_year: int, aoc_day: int):
    # Run code for given year and day.
    # If not provided, set puzzle year to current year.
    if aoc_year is None:
        aoc_year = CURRENT_YEAR
    if aoc_year == CURRENT_YEAR and LOCAL_DT < AOC_CURRENT_BEGIN:
        click.echo("Too early, try a previous year", err=True)
    else:
        aoc_dir = f'aoc{aoc_year:04d}'
        aoc_path = Path(aoc_dir)
        # Work out puzzle day if not provided.
        if aoc_day is None:
            if aoc_year == CURRENT_YEAR:
                aoc_day = AOC_CURRENT_MAX_DAY
            else:
                aoc_day = AOC_MAX_DAY
        day_str = f'day{aoc_day:02d}'
        code_path = aoc_path.joinpath(f'{day_str}.py')
        data_path = aoc_path.joinpath('data')
        data_dirs = [data_path.joinpath(f'{day_str}-example.txt'), data_path.joinpath(f'{day_str}-input.txt')]

if __name__ == "__main__":
    main()
