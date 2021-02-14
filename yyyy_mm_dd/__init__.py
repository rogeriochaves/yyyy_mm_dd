import datetime
from dateutil.relativedelta import relativedelta

def move_yyyy(yyyymmdd: str, by: int) -> str:
    date = datetime.datetime.strptime(yyyymmdd, "%Y-%m-%d")
    date += relativedelta(years=by)
    return date.strftime("%Y-%m-%d")

def move_yyyy_mm(yyyymmdd: str, by: int) -> str:
    date = datetime.datetime.strptime(yyyymmdd, "%Y-%m-%d")
    date += relativedelta(months=by)
    return date.strftime("%Y-%m-%d")

def move_yyyy_mm_dd(yyyymmdd: str, by: int) -> str:
    date = datetime.datetime.strptime(yyyymmdd, "%Y-%m-%d")
    date += relativedelta(days=by)
    return date.strftime("%Y-%m-%d")