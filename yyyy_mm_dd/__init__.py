import datetime
from dateutil.relativedelta import relativedelta
import re
import math
from typing import Tuple, Union


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
    return yyyy_mm_dd(move_yyyy_mm_dd(today(), -1))


def tomorrow() -> str:
    """
    Returns 'yyyy-mm-dd' date for tomorrow

    >>> tomorrow() == (datetime.date.today() + datetime.timedelta(1)).strftime('%Y-%m-%d')
    True
    """
    return yyyy_mm_dd(move_yyyy_mm_dd(today(), 1))


def now() -> str:
    """
    Returns current datetime as 'yyyy-mm-ddThh:mm:ss'

    >>> now() == datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    True
    """
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def move_yyyy(yyyy_mm_dd: Union[str, datetime.date], by: int) -> Union[str, datetime.date]:
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
    >>> move_yyyy('2020-02-14T10:20:30', 2)
    '2022-02-14T10:20:30'
    >>> move_yyyy(datetime.date(2020, 2, 14), 1)
    datetime.date(2021, 2, 14)
    >>> move_yyyy(datetime.datetime(2020, 2, 14, 0, 0), 1)
    datetime.datetime(2021, 2, 14, 0, 0)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y")
    date += relativedelta(years=by)
    return _strftime(date, pattern)


def move_yyyy_mm(yyyy_mm_dd: Union[str, datetime.date], by: int) -> Union[str, datetime.date]:
    """
    Increases or decreases a date by a certain number of months

    >>> move_yyyy_mm('2020-02', 1)
    '2020-03'
    >>> move_yyyy_mm('2020-02', -1)
    '2020-01'
    >>> move_yyyy_mm('2020-01-31', 1)
    '2020-02-29'
    >>> move_yyyy_mm('2020-01-31', 25)
    '2022-02-28'
    >>> move_yyyy_mm('2020-02-14T10:20:30', 2)
    '2020-04-14T10:20:30'
    >>> move_yyyy_mm(datetime.date(2020, 2, 14), 1)
    datetime.date(2020, 3, 14)
    >>> move_yyyy_mm(datetime.datetime(2020, 2, 14, 0, 0), 1)
    datetime.datetime(2020, 3, 14, 0, 0)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m")
    date += relativedelta(months=by)
    return _strftime(date, pattern)


def move_yyyy_mm_dd(yyyy_mm_dd: Union[str, datetime.date], by: int) -> Union[str, datetime.date]:
    """
    Increases or decreases a date by a certain number of days

    >>> move_yyyy_mm_dd('2020-12-31', 1)
    '2021-01-01'
    >>> move_yyyy_mm_dd('2020-12-31', -1)
    '2020-12-30'
    >>> move_yyyy_mm_dd('2020-02-29T10:20:30', 2)
    '2020-03-02T10:20:30'
    >>> move_yyyy_mm_dd(datetime.date(2020, 2, 29), 1)
    datetime.date(2020, 3, 1)
    >>> move_yyyy_mm_dd(datetime.datetime(2020, 2, 29, 0, 0), 1)
    datetime.datetime(2020, 3, 1, 0, 0)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m-%d")
    date += relativedelta(days=by)
    return _strftime(date, pattern)


def move_yyyy_mm_dd_hh(yyyy_mm_dd_hh_mm_ss: Union[str, datetime.datetime], by: int) -> Union[str, datetime.date]:
    """
    Increases or decreases a datetime by a certain number of hours

    >>> move_yyyy_mm_dd_hh('2020-12-31T23', 1)
    '2021-01-01T00'
    >>> move_yyyy_mm_dd_hh('2020-12-31T23', -1)
    '2020-12-31T22'
    >>> move_yyyy_mm_dd_hh('2020-02-29T10:20:30', 2)
    '2020-02-29T12:20:30'
    >>> move_yyyy_mm_dd_hh(datetime.datetime(2020, 2, 29, 10, 20, 30), 1)
    datetime.datetime(2020, 2, 29, 11, 20, 30)
    """
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H")
    date += relativedelta(hours=by)
    return _strftime(date, pattern)


def move_yyyy_mm_dd_hh_mm(yyyy_mm_dd_hh_mm_ss: Union[str, datetime.datetime], by: int) -> Union[str, datetime.date]:
    """
    Increases or decreases a datetime by a certain number of minutes

    >>> move_yyyy_mm_dd_hh_mm('2020-12-31T23:59', 1)
    '2021-01-01T00:00'
    >>> move_yyyy_mm_dd_hh_mm('2020-12-31T23:59', -1)
    '2020-12-31T23:58'
    >>> move_yyyy_mm_dd_hh_mm('2020-02-29T10:20:30', 2)
    '2020-02-29T10:22:30'
    >>> move_yyyy_mm_dd_hh_mm(datetime.datetime(2020, 2, 29, 10, 20, 30), 1)
    datetime.datetime(2020, 2, 29, 10, 21, 30)
    """
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M")
    date += relativedelta(minutes=by)
    return _strftime(date, pattern)


def move_yyyy_mm_dd_hh_mm_ss(yyyy_mm_dd_hh_mm_ss: Union[str, datetime.datetime], by: int) -> Union[str, datetime.date]:
    """
    Increases or decreases a datetime by a certain number of seconds

    >>> move_yyyy_mm_dd_hh_mm_ss('2020-12-31T23:59:59', 1)
    '2021-01-01T00:00:00'
    >>> move_yyyy_mm_dd_hh_mm_ss('2020-12-31T23:59:59', -2)
    '2020-12-31T23:59:57'
    >>> move_yyyy_mm_dd_hh_mm_ss(datetime.datetime(2020, 2, 29, 10, 20, 30), 1)
    datetime.datetime(2020, 2, 29, 10, 20, 31)
    """
    date, pattern = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M:%S")
    date += relativedelta(seconds=by)
    return _strftime(date, pattern)


def diff_yyyy(a: Union[str, datetime.date], b: Union[str, datetime.date]) -> int:
    """
    Returns the amount of years between date A and date B

    >>> diff_yyyy("2020", "2021")
    1
    >>> diff_yyyy("2020-02", "2020-08")
    0
    >>> diff_yyyy("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    1
    >>> diff_yyyy("2020-02-14T10:20:30", "2021-02-14T10:20:29")
    0
    >>> diff_yyyy("2021-02-14T10:20:30", "2020-02-14T10:20:30")
    -1
    >>> diff_yyyy(datetime.date(2020, 2, 14), datetime.date(2022, 2, 14))
    2
    """
    date_a, _ = _parse(a, at_least="%Y")
    date_b, _ = _parse(b, at_least="%Y")
    return relativedelta(date_b, date_a).years


def diff_yyyy_mm(a: Union[str, datetime.date], b: Union[str, datetime.date]) -> int:
    """
    Returns the amount of months between date A and date B

    >>> diff_yyyy_mm("2020-03", "2020-04")
    1
    >>> diff_yyyy_mm("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    12
    >>> diff_yyyy_mm("2020-02-14T10:20:30", "2020-01-14T10:20:30")
    -1
    >>> diff_yyyy_mm(datetime.date(2020, 2, 14), datetime.date(2020, 4, 14))
    2
    """
    date_a, _ = _parse(a, at_least="%Y-%m")
    date_b, _ = _parse(b, at_least="%Y-%m")
    return relativedelta(date_b, date_a).years * 12 + relativedelta(date_b, date_a).months


def diff_yyyy_mm_dd(a: Union[str, datetime.date], b: Union[str, datetime.date]) -> int:
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
    >>> diff_yyyy_mm_dd(datetime.date(2020, 2, 14), datetime.date(2020, 2, 16))
    2
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%d")
    date_b, _ = _parse(b, at_least="%Y-%m-%d")
    return (date_b - date_a).days


def diff_yyyy_mm_dd_hh(a: Union[str, datetime.datetime], b: Union[str, datetime.datetime]) -> int:
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
    >>> diff_yyyy_mm_dd_hh(datetime.datetime(2020, 2, 14, 10, 20, 30), datetime.datetime(2020, 2, 14, 12, 20, 30))
    2
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H")
    return math.floor((date_b - date_a).total_seconds() / 3600)


def diff_yyyy_mm_dd_hh_mm(a: Union[str, datetime.datetime], b: Union[str, datetime.datetime]) -> int:
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
    >>> diff_yyyy_mm_dd_hh_mm(datetime.datetime(2020, 2, 14, 10, 20, 30), datetime.datetime(2020, 2, 14, 10, 22, 30))
    2
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M")
    return math.floor((date_b - date_a).total_seconds() / 60)


def diff_yyyy_mm_dd_hh_mm_ss(a: Union[str, datetime.datetime], b: Union[str, datetime.datetime]) -> int:
    """
    Returns the amount of seconds between datetime A and datetime B

    >>> diff_yyyy_mm_dd_hh_mm_ss("2020-02-01T10:20:30", "2020-02-01T10:20:31")
    1
    >>> diff_yyyy_mm_dd_hh_mm_ss("2020-02-14T10:20:30", "2021-02-14T10:20:30")
    31622400
    >>> diff_yyyy_mm_dd_hh_mm_ss("2020-02-14T10:20:30", "2020-02-14T10:20:29")
    -1
    >>> diff_yyyy_mm_dd_hh_mm_ss(datetime.datetime(2020, 2, 14, 10, 20, 30), datetime.datetime(2020, 2, 14, 10, 20, 32))
    2
    """
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M:%S")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M:%S")
    return math.floor((date_b - date_a).total_seconds())


def start_of_yyyy(yyyy_mm_dd: Union[str, datetime.date]) -> Union[str, datetime.date]:
    """
    Returns first day of the year of a given date

    >>> start_of_yyyy('2020')
    '2020-01-01'
    >>> start_of_yyyy('2020-05-14')
    '2020-01-01'
    >>> start_of_yyyy(datetime.date(2020, 5, 14))
    datetime.date(2020, 1, 1)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y")
    date = datetime.datetime(date.year, 1, 1, 0, 0)
    if pattern not in ["date", "datetime"]:
        pattern = "%Y-%m-%d"

    return _strftime(date, pattern)


def start_of_yyyy_mm(yyyy_mm_dd: Union[str, datetime.date]) -> Union[str, datetime.date]:
    """
    Returns first day of the month of a given date

    >>> start_of_yyyy_mm('2020-05')
    '2020-05-01'
    >>> start_of_yyyy_mm('2020-05-14')
    '2020-05-01'
    >>> start_of_yyyy_mm(datetime.date(2020, 5, 14))
    datetime.date(2020, 5, 1)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m")
    date = datetime.datetime(date.year, date.month, 1, 0, 0)
    if pattern not in ["date", "datetime"]:
        pattern = "%Y-%m-%d"

    return _strftime(date, pattern)


def start_of_yyyy_mm_dd(yyyy_mm_dd: Union[str, datetime.date]) -> Union[str, datetime.datetime]:
    """
    Returns first datetime of the day of a given date

    >>> start_of_yyyy_mm_dd('2020-05-14')
    '2020-05-14T00:00:00'
    >>> start_of_yyyy_mm_dd('2020-05-14T13:25:10')
    '2020-05-14T00:00:00'
    >>> start_of_yyyy_mm_dd(datetime.date(2020, 5, 14))
    datetime.datetime(2020, 5, 14, 0, 0)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m-%d")
    date = datetime.datetime(date.year, date.month, date.day, 0, 0)
    if pattern in ["date", "datetime"]:
        return date
    return date.strftime("%Y-%m-%dT%H:%M:%S")


def start_of_yyyy_mm_dd_hh(yyyy_mm_dd: Union[str, datetime.datetime]) -> Union[str, datetime.datetime]:
    """
    Returns the start of the hour of a given datetime

    >>> start_of_yyyy_mm_dd_hh('2020-05-14T13:25:10')
    '2020-05-14T13:00:00'
    >>> start_of_yyyy_mm_dd_hh(datetime.datetime(2020, 5, 14, 23, 59))
    datetime.datetime(2020, 5, 14, 23, 0)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m-%dT%H")
    date = datetime.datetime(date.year, date.month, date.day, date.hour, 0)
    if pattern in ["date", "datetime"]:
        return date
    return date.strftime("%Y-%m-%dT%H:%M:%S")


def start_of_yyyy_mm_dd_hh_mm(yyyy_mm_dd: Union[str, datetime.datetime]) -> Union[str, datetime.datetime]:
    """
    Returns the same datetime but with seconds at 0

    >>> start_of_yyyy_mm_dd_hh_mm('2020-05-14T13:25:10')
    '2020-05-14T13:25:00'
    >>> start_of_yyyy_mm_dd_hh_mm(datetime.datetime(2020, 5, 14, 23, 59, 59))
    datetime.datetime(2020, 5, 14, 23, 59)
    """
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m-%dT%H:%M")
    date = datetime.datetime(date.year, date.month,
                             date.day, date.hour, date.minute)
    if pattern in ["date", "datetime"]:
        return date
    return date.strftime("%Y-%m-%dT%H:%M:%S")


def end_of_yyyy(yyyy_mm_dd: Union[str, datetime.date]) -> Union[str, datetime.date]:
    """
    Returns last day of the year of a given date

    >>> end_of_yyyy('2020')
    '2020-12-31'
    >>> end_of_yyyy('2020-05-14')
    '2020-12-31'
    >>> end_of_yyyy(datetime.date(2020, 5, 14))
    datetime.date(2020, 12, 31)
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")

    return move_yyyy_mm_dd(start_of_yyyy(move_yyyy(yyyy_mm_dd, 1)), -1)


def end_of_yyyy_mm(yyyy_mm_dd: Union[str, datetime.date]) -> Union[str, datetime.date]:
    """
    Returns last day of the month of a given date

    >>> end_of_yyyy_mm('2020-02')
    '2020-02-29'
    >>> end_of_yyyy_mm('2020-05-14')
    '2020-05-31'
    >>> end_of_yyyy_mm(datetime.date(2020, 5, 14))
    datetime.date(2020, 5, 31)
    """

    return move_yyyy_mm_dd(start_of_yyyy_mm(move_yyyy_mm(yyyy_mm_dd, 1)), -1)


def end_of_yyyy_mm_dd(yyyy_mm_dd: Union[str, datetime.date]) -> Union[str, datetime.date]:
    """
    Returns last datetime of the day of a given date

    >>> end_of_yyyy_mm_dd('2020-05-14')
    '2020-05-14T23:59:59'
    >>> end_of_yyyy_mm_dd('2020-05-14T13:25:10')
    '2020-05-14T23:59:59'
    >>> end_of_yyyy_mm_dd(datetime.date(2020, 5, 14))
    datetime.datetime(2020, 5, 14, 23, 59, 59)
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")

    return move_yyyy_mm_dd_hh_mm_ss(start_of_yyyy_mm_dd(move_yyyy_mm_dd(yyyy_mm_dd, 1)), -1)


def yyyy(yyyy_mm_dd: Union[str, datetime.date]) -> str:
    """
    Extracts the year of a given date

    >>> yyyy('2020-05-14')
    '2020'
    >>> yyyy(datetime.date(2020, 5, 14))
    '2020'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")
    return date.strftime("%Y")


def yyyy_mm(yyyy_mm_dd: Union[str, datetime.date]) -> str:
    """
    Extracts the year and month of a given date

    >>> yyyy_mm('2020-05-14')
    '2020-05'
    >>> yyyy_mm(datetime.date(2020, 5, 14))
    '2020-05'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y-%m")
    return date.strftime("%Y-%m")


def yyyy_mm_dd(yyyy_mm_dd: Union[str, datetime.date]) -> str:
    """
    Extracts the date of a given datetime

    >>> yyyy_mm_dd('2020-05-14T10:20:30')
    '2020-05-14'
    >>> yyyy_mm_dd(datetime.date(2020, 5, 14))
    '2020-05-14'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y-%m-%d")
    return date.strftime("%Y-%m-%d")


def hh_mm_ss(yyyy_mm_dd_hh_mm_ss: Union[str, datetime.datetime]) -> str:
    """
    Extracts the time of a given datetime

    >>> hh_mm_ss('2020-05-14T10:20:30')
    '10:20:30'
    >>> hh_mm_ss(datetime.datetime(2020, 5, 14, 10, 20, 30))
    '10:20:30'
    """
    date, _ = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M:%S")
    return date.strftime("%H:%M:%S")


def hh_mm(yyyy_mm_dd_hh_mm_ss: Union[str, datetime.datetime]) -> str:
    """
    Extracts the hour and minute of a given datetime

    >>> hh_mm('2020-05-14T10:20:30')
    '10:20'
    >>> hh_mm(datetime.datetime(2020, 5, 14, 10, 20, 30))
    '10:20'
    """
    date, _ = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H:%M")
    return date.strftime("%H:%M")


def year(yyyy_mm_dd: Union[str, datetime.date]) -> int:
    """
    Extracts the year of a given date, similar to yyyy function but returns an int

    >>> year('2020-05-14')
    2020
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")
    return date.year


def month(yyyy_mm_dd: Union[str, datetime.date]) -> int:
    """
    Extracts the month of a given date

    >>> month('2020-05-14')
    5
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y-%m")
    return date.month


def day(yyyy_mm_dd: Union[str, datetime.date]) -> int:
    """
    Extracts the day of a given date

    >>> day('2020-05-14')
    14
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y-%m-%d")
    return date.day


def hour(yyyy_mm_dd_hh_mm_ss: Union[str, datetime.datetime]) -> int:
    """
    Extracts the hour of a given datetime

    >>> hour('2020-05-14T05:10:58')
    5
    """
    date, _ = _parse(yyyy_mm_dd_hh_mm_ss, at_least="%Y-%m-%dT%H")
    return date.hour


def from_yyyymmdd(yyyymmdd: str) -> str:
    """
    Converts a yyyymmdd date format (no dashes) to yyyy-mm-dd date format (with dashes)

    >>> from_yyyymmdd('20200514')
    '2020-05-14'
    """
    return datetime.datetime.strptime(yyyymmdd, "%Y%m%d").strftime("%Y-%m-%d")


def to_yyyymmdd(yyyy_mm_dd: Union[str, datetime.date]) -> str:
    """
    Converts any partial or full yyyy-mm-ddThh:mm:ss to yyyymmdd date format (no dashes)

    >>> to_yyyymmdd('2020-05-14')
    '20200514'
    >>> to_yyyymmdd(datetime.date(2020, 5, 14))
    '20200514'
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")
    return date.strftime("%Y%m%d")


def to_datetime(yyyy_mm_dd: Union[str, datetime.date]) -> datetime.datetime:
    """
    Converts any partial or full yyyy-mm-ddThh:mm:ss to python datetime

    >>> to_datetime('2020-05')
    datetime.datetime(2020, 5, 1, 0, 0)
    >>> to_datetime('2020-05-14')
    datetime.datetime(2020, 5, 14, 0, 0)
    >>> to_datetime('2020-05-14T10:20:30')
    datetime.datetime(2020, 5, 14, 10, 20, 30)
    """
    date, _ = _parse(yyyy_mm_dd, at_least="%Y")
    return date


def _parse(yyyy_mm_dd: Union[str, datetime.date, datetime.datetime], at_least: str) -> Tuple[datetime.datetime, str]:
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
    if isinstance(yyyy_mm_dd, datetime.datetime):
        return (yyyy_mm_dd, "datetime")
    if isinstance(yyyy_mm_dd, datetime.date):
        return (datetime.datetime(yyyy_mm_dd.year, yyyy_mm_dd.month, yyyy_mm_dd.day), "datetime" if "%H" in at_least else "date")

    pattern = ""
    match = re.match(
        r"(\d{4})?-?(\d{2})?-?(\d{2})?T?(\d{2})?:?(\d{2})?:?(\d{2})?", yyyy_mm_dd)
    if not match:
        raise ValueError(
            "Could not parse date, it should be in YYYY-MM-DDTHH:MM:SS format")
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
        raise ValueError(
            "Could not parse date for operation, you should provide at least %s" % at_least)

    return (datetime.datetime.strptime(yyyy_mm_dd, pattern), pattern)


def _strftime(date: datetime.datetime, pattern: str) -> Union[str, datetime.date]:
    if pattern == "date" and isinstance(date, datetime.datetime):
        return datetime.date(date.year, date.month, date.day)
    if pattern == "datetime":
        return date
    return date.strftime(pattern)
