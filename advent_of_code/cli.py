"""Main entrypoint for Advent of Code exercises in Python."""

from datetime import datetime, timezone, timedelta
from pathlib import Path

import click

AOC_MIN_YEAR = 2015
AOC_TZ = timezone(timedelta(hours=-5))
LOCAL_TZ = timezone(timedelta(hours=11))

local_dt = datetime.now(tz=LOCAL_TZ)
current_year = int(local_dt.strftime("%Y"))
AOC_MAX_DAY = 25
aoc_current_start = datetime(current_year, 12, 1, 0, 0, 0, tzinfo=AOC_TZ)
aoc_current_end = datetime(current_year, 12, 25, 0, 0, 0, tzinfo=AOC_TZ)
if local_dt < aoc_current_start:
    aoc_max_year = current_year - 1
else:
    aoc_max_year = current_year
    if local_dt >= aoc_current_end:
        aoc_current_max_day = 25
    else:
        aoc_current_max_day = int(local_dt.strftime("%d"))

@click.group()
def main():
    click.echo('Advent of Code')

@main.command()
@click.option("--aoc-year", type=click.IntRange(AOC_MIN_YEAR, aoc_max_year), default=aoc_max_year, show_default=True)
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
    click.echo('Years available:')
    for year in range(AOC_MIN_YEAR, aoc_max_year+1):
        click.echo(year)

# @main.command()
# @click.option("--aoc-year", type=click.IntRange(AOC_MIN_YEAR, aoc_max_year), default=aoc_max_year, show_default=True)
# @click.option("--aoc-day", type=click.IntRange(1, AOC_MAX_DAY), default=AOC_MAX_DAY, show_default=True)
# def run(aoc_year: int, aoc_day: int):
    # Run code for given year and day.
    # If not provided, set puzzle year to current year.
    # if aoc_year is None:
    #     aoc_year = current_year
    # click.echo("Advent of code " + str(aoc_year))
    # if aoc_year == current_year and local_dt < aoc_current_start:
    #     click.echo("Too early, try a previous year")
    # else:
    #     # Work out puzzle day if not provided.
    #     if aoc_day is None:
    #         if aoc_year == current_year:
    #             aoc_day = aoc_current_max_day
    #         else:
    #             aoc_day = AOC_MAX_DAY

if __name__ == "__main__":
    main()
