import pytest

from advent_of_code.__main__ import check_valid_year


def test_date_is_in_future():
    with pytest.raises(Exception):
        check_valid_year(2030)


def test_year_not_started():
    with pytest.raises(Exception):
        check_valid_year(2023)


def test_this_year_ok():
    check_valid_year(2022)


def test_past_year_ok():
    check_valid_year(2021)


