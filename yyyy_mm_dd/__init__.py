import datetime
from dateutil.relativedelta import relativedelta
import re

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
