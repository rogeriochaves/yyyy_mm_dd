import datetime
from dateutil.relativedelta import relativedelta
import re
import math


def move_yyyy(yyyy_mm_dd: str, by: int) -> str:
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y")
    date += relativedelta(years=by)
    return date.strftime(pattern)


def move_yyyy_mm(yyyy_mm_dd: str, by: int) -> str:
    date, pattern = _parse(yyyy_mm_dd, at_least="%Y-%m")
    date += relativedelta(months=by)
    return date.strftime(pattern)


def move_yyyy_mm_dd(yyyy_mm_dd: str, by: int) -> str:
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


def diff_yyyy(a: str, b: str) -> str:
    date_a, _ = _parse(a, at_least="%Y")
    date_b, _ = _parse(b, at_least="%Y")
    return relativedelta(date_b, date_a).years


def diff_yyyy_mm(a: str, b: str) -> str:
    date_a, _ = _parse(a, at_least="%Y-%m")
    date_b, _ = _parse(b, at_least="%Y-%m")
    return relativedelta(date_b, date_a).years * 12 + relativedelta(date_b, date_a).months


def diff_yyyy_mm_dd(a: str, b: str) -> str:
    date_a, _ = _parse(a, at_least="%Y-%m-%d")
    date_b, _ = _parse(b, at_least="%Y-%m-%d")
    return (date_b - date_a).days


def diff_yyyy_mm_dd_hh(a: str, b: str) -> str:
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H")
    return math.floor((date_b - date_a).total_seconds() / 3600)


def diff_yyyy_mm_dd_hh_mm(a: str, b: str) -> str:
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M")
    return math.floor((date_b - date_a).total_seconds() / 60)


def diff_yyyy_mm_dd_hh_mm_ss(a: str, b: str) -> str:
    date_a, _ = _parse(a, at_least="%Y-%m-%dT%H:%M:%S")
    date_b, _ = _parse(b, at_least="%Y-%m-%dT%H:%M:%S")
    return math.floor((date_b - date_a).total_seconds())


def _parse(yyyy_mm_dd: str, at_least: str) -> str:
    pattern = ""
    match = re.match(r"(\d{4})?-?(\d{2})?-?(\d{2})?T?(\d{2})?:?(\d{2})?:?(\d{2})?", yyyy_mm_dd)
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
