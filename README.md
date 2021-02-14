# yyyy_mm_dd

Easy string-based date manipulation library for Python

[Documentation](https://rogeriochaves.github.io/yyyy_mm_dd/yyyy_mm_dd/index.html)

## Installation

    $ pip install yyyy_mm_dd

## Why?

When writing some python code for a quick investigation in a notebook, do you also think it's a lot of boilerplate to work with dates? Like, to add +1 day to a date? Do you always have to google the solution and copy it from stackoverflow because you never remember and just want the most quick and easy solution?

If you answered yes, then you are going to love this library. In yyyy_mm_dd you can work with strings directly, no need to convert back and forth:

```python
>>> from yyyy_mm_dd import *
>>> move_yyyy_mm_dd("2020-03-14", 1)
"2020-03-15"
```

There are many operations in the library that you can do with a single functions, no need to think on how to compose them, the most common operations should have a function available, for example the amount of days between two dates:

```python
>>> diff_yyyy_mm_dd("2020-03-14", "2020-03-16")
2
```

Same operations can be done at various levels, and the name is easy to remember, just using the pattern of the date itself. For example the difference in months between two dates:

```python
>>> diff_yyyy_mm("2020-03", "2020-07")
4
>>> diff_yyyy_mm("2020-03-01", "2020-07-01")
4
```

DRAFT

RFC 3339 https://tools.ietf.org/html/rfc3339

## Contributing

Any contributions are very welcome.

The tests are inside the docs, to run them simply execute:

```
python yyyy_mm_dd/__init__.py
```

If you want to check the type hints:

```
pip install mypy
mypy yyyy_mm_dd
```

If you want to regenerate docs:

```
pip install pdoc3
pdoc --html -o ./docs yyyy_mm_dd --force
```
