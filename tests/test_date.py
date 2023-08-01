import pytest

from advent_of_code.__main__ import is_day_valid, is_year_valid


def test_year_is_in_future():
    with pytest.raises(Exception):
        is_year_valid(2030)


def test_year_not_started():
    with pytest.raises(Exception):
        is_year_valid(2023)


def test_this_year_ok():
    is_year_valid(2022)


def test_past_year_ok():
    is_year_valid(2021)


def test_boxing_day():
    with pytest.raises(Exception):
        is_day_valid(2021, 26)
