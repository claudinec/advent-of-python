"""Main entrypoint for Advent of Code exercises in Python."""

from datetime import datetime, timezone, timedelta

import click

AOC_MIN_YEAR = 2015
AOC_TZ = timezone(timedelta(hours=-5))
LOCAL_TZ = timezone(timedelta(hours=11))

local_dt = datetime.now(tz=LOCAL_TZ)
current_year = local_dt.strftime("%Y")

@click.command()
@click.option("--aoc-year", type=click.IntRange(AOC_MIN_YEAR, current_year))
def main(aoc_year):
    """Placeholder main function."""
    aoc_start = datetime(aoc_year, 12, 1, 0, 0, 0, tzinfo=AOC_TZ)
    click.echo("Advent of code " + str(aoc_year))
    if local_dt < aoc_start and aoc_year == current_year:
        click.echo("Too early, try a previous year")
    else:
        aoc_dir = "aoc" + str(aoc_year)
        # check or create directory

if __name__ == "__main__":
    main()
