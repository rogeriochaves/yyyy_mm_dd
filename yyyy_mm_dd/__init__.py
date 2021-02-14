import datetime
from dateutil.relativedelta import relativedelta
import re
import math
from typing import Tuple


def today() -> str:
    """
    Returns 'yyyy-mm-dd' date for today

    >>> today() == datetime.date.today().strftime('%Y-%m-%d')
    True
    """
    return datetime.date.today().strftime("%Y-%m-%d")


def yesterday() -> str:
    """
    Returns 'yyyy-mm-dd' date for yesterday

    >>> yesterday() == (datetime.date.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    True
    """
    return move_yyyy_mm_dd(today(), -1)


def tomorrow() -> str:
    """
    Returns 'yyyy-mm-dd' date for tomorrow

    >>> tomorrow() == (datetime.date.today() + datetime.timedelta(1)).strftime('%Y-%m-%d')
    True
    """
    return move_yyyy_mm_dd(today(), 1)


def now() -> str:
    """
    Returns current datetime as 'yyyy-mm-ddThh:mm:ss'

    >>> now() == datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    True
    """
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


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
    """
    Increases or decreases a datetime by a certain number of hours

    >>> move_yyyy_mm_dd_hh('2020-12-31T23', 1)
    '2021-01-01T00'
    >>> move_yyyy_mm_dd_hh('2020-12-31T23', -1)
    '2020-12-31T22'
    >>> move_yyyy_mm_dd_hh('2020-02-29T10:20:30', 1)
    '2020-02-29T11:20:30'
    """
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H")
    date += relativedelta(hours=by)
    return date.strftime(pattern)


def move_yyyy_mm_dd_hh_mm(yyyy_mm_dd_hh_mm_ss: str, by: int) -> str:
    """
    Increases or decreases a datetime by a certain number of minutes

    >>> move_yyyy_mm_dd_hh_mm('2020-12-31T23:59', 1)
    '2021-01-01T00:00'
    >>> move_yyyy_mm_dd_hh_mm('2020-12-31T23:59', -1)
    '2020-12-31T23:58'
    >>> move_yyyy_mm_dd_hh_mm('2020-02-29T10:20:30', 1)
    '2020-02-29T10:21:30'
    """
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M")
    date += relativedelta(minutes=by)
    return date.strftime(pattern)


def move_yyyy_mm_dd_hh_mm_ss(yyyy_mm_dd_hh_mm_ss: str, by: int) -> str:
    """
    Increases or decreases a datetime by a certain number of seconds

    >>> move_yyyy_mm_dd_hh_mm_ss('2020-12-31T23:59:59', 1)
    '2021-01-01T00:00:00'
    >>> move_yyyy_mm_dd_hh_mm_ss('2020-12-31T23:59:59', -1)
    '2020-12-31T23:59:58'
    """
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M:%S")
    date += relativedelta(seconds=by)
    return date.strftime(pattern)


def diff_yyyy(a: str, b: str) -> int:
    """
    Returns the amount of years between date A and date B

    >>> diff_yyyy("2020", "2020")
    0
    >>> diff_yyyy("2020-02", "2020-08")
    0
    >>> diff_yyyy("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    1
    >>> diff_yyyy("2021-02-14T10:20:30", "2020-02-14T10:20:30")
    -1
    """
    date_a, _ = _parse(a, at_least="%Y")
    date_b, _ = _parse(b, at_least="%Y")
    return relativedelta(date_b, date_a).years


def diff_yyyy_mm(a: str, b: str) -> int:
    """
    Returns the amount of months between date A and date B

    >>> diff_yyyy_mm("2020-03", "2020-04")
    1
    >>> diff_yyyy_mm("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    12
    >>> diff_yyyy_mm("2020-02-14T10:20:30", "2020-01-14T10:20:30")
    -1
    """
    date_a, _ = _parse(a, at_least="%Y-%m")
    date_b, _ = _parse(b, at_least="%Y-%m")
    return relativedelta(date_b, date_a).years * 12 + relativedelta(date_b, date_a).months


def diff_yyyy_mm_dd(a: str, b: str) -> int:
    """
    Returns the amount of days between date A and date B

    >>> diff_yyyy_mm_dd("2020-02-01", "2020-03-01")
    29
    >>> diff_yyyy_mm_dd("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    366
    >>> diff_yyyy_mm_dd("2020-02-14T10:20:30", "2020-02-13T10:20:30")
    -1
    >>> diff_yyyy_mm_dd("2020-02-14T10", "2020-02-15T09")
    0
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%d")
    date_b, _ = _parse(b, at_least="%Y-%m-%d")
    return (date_b - date_a).days


def diff_yyyy_mm_dd_hh(a: str, b: str) -> int:
    """
    Returns the amount of hours between datetime A and datetime B

    >>> diff_yyyy_mm_dd_hh("2020-02-01T10", "2020-02-01T11")
    1
    >>> diff_yyyy_mm_dd_hh("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    8784
    >>> diff_yyyy_mm_dd_hh("2020-02-14T10:20:30", "2020-02-14T09:20:30")
    -1
    >>> diff_yyyy_mm_dd_hh("2020-02-14T10:30", "2020-02-14T11:29")
    0
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H")
    return math.floor((date_b - date_a).total_seconds() / 3600)


def diff_yyyy_mm_dd_hh_mm(a: str, b: str) -> int:
    """
    Returns the amount of minutes between datetime A and datetime B

    >>> diff_yyyy_mm_dd_hh_mm("2020-02-01T10:20", "2020-02-01T10:21")
    1
    >>> diff_yyyy_mm_dd_hh_mm("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    527040
    >>> diff_yyyy_mm_dd_hh_mm("2020-02-14T10:20:30", "2020-02-14T10:19:30")
    -1
    >>> diff_yyyy_mm_dd_hh_mm("2020-02-14T10:30", "2020-02-14T10:30:30")
    0
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M")
    return math.floor((date_b - date_a).total_seconds() / 60)


def diff_yyyy_mm_dd_hh_mm_ss(a: str, b: str) -> int:
    """
    Returns the amount of seconds between datetime A and datetime B

    >>> diff_yyyy_mm_dd_hh_mm_ss("2020-02-01T10:20:30", "2020-02-01T10:20:31")
    1
    >>> diff_yyyy_mm_dd_hh_mm_ss("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    31622400
    >>> diff_yyyy_mm_dd_hh_mm_ss("2020-02-14T10:20:30", "2020-02-14T10:20:29")
    -1
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M:%S")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M:%S")
    return math.floor((date_b - date_a).total_seconds())


def start_of_yyyy(yyyy_mm_dd: str) -> str:
    """
    Returns first day of the year of a given date

    >>> start_of_yyyy('2020')
    '2020-01-01'
    >>> start_of_yyyy('2020-05-14')
    '2020-01-01'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")

    return "%s-01-01" % date.strftime("%Y")


def start_of_yyyy_mm(yyyy_mm_dd: str) -> str:
    """
    Returns first day of the month of a given date

    >>> start_of_yyyy_mm('2020-05')
    '2020-05-01'
    >>> start_of_yyyy_mm('2020-05-14')
    '2020-05-01'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y-%m")

    return "%s-01" % date.strftime("%Y-%m")


def start_of_yyyy_mm_dd(yyyy_mm_dd: str) -> str:
    """
    Returns first datetime of the day of a given date

    >>> start_of_yyyy_mm_dd('2020-05-14')
    '2020-05-14T00:00:00'
    >>> start_of_yyyy_mm_dd('2020-05-14T13:25:10')
    '2020-05-14T00:00:00'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y-%m-%d")

    return "%sT00:00:00" % date.strftime("%Y-%m-%d")


def end_of_yyyy(yyyy_mm_dd: str) -> str:
    """
    Returns last day of the year of a given date

    >>> end_of_yyyy('2020')
    '2020-12-31'
    >>> end_of_yyyy('2020-05-14')
    '2020-12-31'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")

    return "%s-12-31" % date.strftime("%Y")


def end_of_yyyy_mm(yyyy_mm_dd: str) -> str:
    """
    Returns last day of the month of a given date

    >>> end_of_yyyy_mm('2020-02')
    '2020-02-29'
    >>> end_of_yyyy_mm('2020-05-14')
    '2020-05-31'
    """

    return move_yyyy_mm_dd(start_of_yyyy_mm(move_yyyy_mm(yyyy_mm_dd, 1)), -1)


def end_of_yyyy_mm_dd(yyyy_mm_dd: str) -> str:
    """
    Returns last datetime of the day of a given date

    >>> end_of_yyyy_mm_dd('2020-05-14')
    '2020-05-14T23:59:59'
    >>> end_of_yyyy_mm_dd('2020-05-14T13:25:10')
    '2020-05-14T23:59:59'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")

    return move_yyyy_mm_dd_hh_mm_ss(start_of_yyyy_mm_dd(move_yyyy_mm_dd(yyyy_mm_dd, 1)), -1)


def _parse(yyyy_mm_dd: str, at_least: str) -> Tuple[datetime.datetime, str]:
    """
    >>> _parse('foo', '%Y')
    Traceback (most recent call last):
        ...
    ValueError: Could not parse date for operation, you should provide at least %Y

    >>> _parse('2020-01', '%Y-%m-%d')
    Traceback (most recent call last):
        ...
    ValueError: Could not parse date for operation, you should provide at least %Y-%m-%d

    >>> _parse('2020-01-01foobar', '%Y-%m-%d')
    Traceback (most recent call last):
        ...
    ValueError: unconverted data remains: foobar
    """
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
    failed, _ = doctest.testmod()
    if failed == 0:
        print("All doctests passing!")
