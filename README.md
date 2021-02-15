# yyyy_mm_dd

[![Build Status](https://img.shields.io/github/workflow/status/rogeriochaves/yyyy_mm_dd/Python%20package?style=for-the-badge)](https://github.com/rogeriochaves/yyyy_mm_dd/actions)

Easy string-based date manipulation library for Python

[Documentation](https://rogeriochaves.github.io/yyyy_mm_dd/yyyy_mm_dd/index.html)

## Installation

    $ pip install yyyy_mm_dd

## Why?

When writing some python code for a quick investigation in a notebook, do you also think it's a lot of boilerplate to work with dates? Do you always have to google the solution and copy it from stackoverflow because you never remember and just want the most quick and easy solution?

If you answered yes, then you are going to love this library. In yyyy_mm_dd you can work with strings directly, no need to convert back and forth, like to add +1 day to a date:

```python
>>> from yyyy_mm_dd import *
>>> move_yyyy_mm_dd("2020-03-14", 1)
'2020-03-15'
```

There are many operations in the library that you can do with a single functions, no need to think on how to compose them, the most common operations should have a function available, for example the amount of days between two dates:

```python
>>> diff_yyyy_mm_dd("2020-03-14", "2020-03-16")
2
```

Same operations can be done at various levels, and the name is easy to remember, just using the pattern of the date itself (operation + yyyy_mm, yyyy_mm_dd, yyyy_mm_dd_hh_mm_ss, etc). For example the difference in months between two dates:

```python
>>> diff_yyyy_mm("2020-03", "2020-07")
4
>>> diff_yyyy_mm("2020-03-01", "2020-07-01")
4
```

Or to add a month:

```python
>>> move_yyyy_mm("2020-03-14", 1)
'2020-04-14'
```

But not only strings, you can also pass a datetime as argument in case you already have it, and there is no need for any conversion:

```python
>>> import datetime
>>> move_yyyy_mm_dd_hh(datetime.datetime(2020, 3, 14, 5, 0), 1)
datetime.datetime(2020, 3, 14, 6, 0)
```

Check the [documentation](https://rogeriochaves.github.io/yyyy_mm_dd/yyyy_mm_dd/index.html) to see all functions available, and if there is an operation you regularly need to do which is not there, please [open an issue](https://github.com/rogeriochaves/yyyy_mm_dd/issues)

## TODO:

- Support timezones
- Make it fully compatible with [RFC 3339](https://tools.ietf.org/html/rfc3339)

## Contributing

Any contributions are very welcome. To run locally, install the dependencies:

```
pip install -r requirements.txt
```

The tests are inside the docs, to run them simply execute:

```
python -m doctest yyyy_mm_dd/__init__.py
```

If you want to check the type hints:

```
mypy yyyy_mm_dd
```

If you want to regenerate docs:

```
pdoc --html -o ./docs yyyy_mm_dd --force
```
