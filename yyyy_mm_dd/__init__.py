import datetime
from dateutil.relativedelta import relativedelta
import re
import math
from typing import Tuple


def move_yyyy(yyyy_mm_dd: str, by: int) -> str:
    """
    Increases or decreases a date by a certain number of years

    >>> move_yyyy('2020', 1)
    '2021'
    >>> move_yyyy('2020', -1)
    '2019'
    >>> move_yyyy('2020-02', 1)
    '2021-02'
    >>> move_yyyy('2020-02-14', 1)
    '2021-02-14'
    >>> move_yyyy('2020-02-14T10:20:30', 1)
    '2021-02-14T10:20:30'
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y")
    date += relativedelta(years=by)
    return date.strftime(pattern)


def move_yyyy_mm(yyyy_mm_dd: str, by: int) -> str:
    """
    Increases or decreases a date by a certain number of months

    >>> move_yyyy_mm('2020-02', 1)
    '2020-03'
    >>> move_yyyy_mm('2020-02', -1)
    '2020-01'
    >>> move_yyyy_mm('2020-12-14', 1)
    '2021-01-14'
    >>> move_yyyy_mm('2020-02-14T10:20:30', 1)
    '2020-03-14T10:20:30'
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m")
    date += relativedelta(months=by)
    return date.strftime(pattern)


def move_yyyy_mm_dd(yyyy_mm_dd: str, by: int) -> str:
    """
    Increases or decreases a date by a certain number of days

    >>> move_yyyy_mm_dd('2020-12-31', 1)
    '2021-01-01'
    >>> move_yyyy_mm_dd('2020-12-31', -1)
    '2020-12-30'
    >>> move_yyyy_mm_dd('2020-02-29T10:20:30', 1)
    '2020-03-01T10:20:30'
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m-%d")
    date += relativedelta(days=by)
    return date.strftime(pattern)


def move_yyyy_mm_dd_hh(yyyy_mm_dd_hh_mm_ss: str, by: int) -> str:
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H")
    date += relativedelta(hours=by)
    return date.strftime(pattern)


def move_yyyy_mm_dd_hh_mm(yyyy_mm_dd_hh_mm_ss: str, by: int) -> str:
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M")
    date += relativedelta(minutes=by)
    return date.strftime(pattern)


def move_yyyy_mm_dd_hh_mm_ss(yyyy_mm_dd_hh_mm_ss: str, by: int) -> str:
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M:%S")
    date += relativedelta(seconds=by)
    return date.strftime(pattern)


def diff_yyyy(a: str, b: str) -> int:
    date_a, _ = _parse(a, at_least="%Y")
    date_b, _ = _parse(b, at_least="%Y")
    return relativedelta(date_b, date_a).years


def diff_yyyy_mm(a: str, b: str) -> int:
    date_a, _ = _parse(a, at_least="%Y-%m")
    date_b, _ = _parse(b, at_least="%Y-%m")
    return relativedelta(date_b, date_a).years * 12 + relativedelta(date_b, date_a).months


def diff_yyyy_mm_dd(a: str, b: str) -> int:
    date_a, _ = _parse(a, at_least="%Y-%m-%d")
    date_b, _ = _parse(b, at_least="%Y-%m-%d")
    return (date_b - date_a).days


def diff_yyyy_mm_dd_hh(a: str, b: str) -> int:
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H")
    return math.floor((date_b - date_a).total_seconds() / 3600)


def diff_yyyy_mm_dd_hh_mm(a: str, b: str) -> int:
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M")
    return math.floor((date_b - date_a).total_seconds() / 60)


def diff_yyyy_mm_dd_hh_mm_ss(a: str, b: str) -> int:
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M:%S")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M:%S")
    return math.floor((date_b - date_a).total_seconds())


def today() -> str:
    return datetime.date.today().strftime("%Y-%m-%d")


def yesterday() -> str:
    return move_yyyy_mm_dd(today(), -1)


def tomorrow() -> str:
    return move_yyyy_mm_dd(today(), 1)


def now() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def _parse(yyyy_mm_dd: str, at_least: str) -> Tuple[datetime.datetime, str]:
    pattern = ""
    match = re.match(r"(\d{4})?-?(\d{2})?-?(\d{2})?T?(\d{2})?:?(\d{2})?:?(\d{2})?", yyyy_mm_dd)
    if not match:
        raise ValueError("Could not parse date, it should be in YYYY-MM-DDTHH:MM:SS format")
    year, month, day, hour, minute, second = match.groups()
    if year is not None:
        pattern += "%Y"
    if month is not None:
        pattern += "-%m"
    if day is not None:
        pattern += "-%d"
    if hour is not None:
        pattern += "T%H"
    if minute is not None:
        pattern += ":%M"
    if second is not None:
        pattern += ":%S"
    if at_least not in pattern:
        raise ValueError("Could not parse date for operation, you should provide at least %s" % at_least)

    return (datetime.datetime.strptime(yyyy_mm_dd, pattern), pattern)

if __name__ == "__main__":
    import doctest
    doctest.testmod()