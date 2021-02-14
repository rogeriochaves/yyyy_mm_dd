# yyyy_mm_dd

Helper functions for easy string-based manipulation of dates in python

DRAFT

RFC 3339 https://tools.ietf.org/html/rfc3339

## Contributing

Any contributions are very welcome.

The code has no dependencies. To run the tests simply execute:

```
python -m unittest tests/test_yyyy_mm_dd.py
```

If you want to check the type hints:

```
pip install mypy
mypy yyyy_mm_dd
```

If you want to regenerate docs:

```
pip install pdoc3
pdoc --html -o ./docs yyyy_mm_dd
```
