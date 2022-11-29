"""Main entrypoint for Advent of Code exercises in Python."""

from datetime import datetime, timezone, timedelta

import click

AOC_YEAR = 2022
AOC_TZ = timezone(timedelta(hours=-5))
LOCAL_TZ = timezone(timedelta(hours=11))

@click.command()
def main():
    """Placeholder main function."""
    aoc_start = datetime(AOC_YEAR, 12, 1, 0, 0, 0, tzinfo=AOC_TZ)
    local_dt = datetime.now(tz=LOCAL_TZ)
    click.echo("Advent of code " + str(AOC_YEAR))
    if local_dt < aoc_start:
        click.echo("Too early")

if __name__ == "__main__":
    main()
