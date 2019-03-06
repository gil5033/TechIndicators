# Technical Indicator Package

A package aimed at providing a wrapper for Technical Indicator calculations. It uses the TA-lib package and develop a
wrapper for this package and a framework to custom indicators.

## Dependencies

This library it is build on top of [TA-lib](https://mrjbq7.github.io/ta-lib/install.html), and leverages the python packages [pandas](https://pandas.pydata.org/pandas-docs/version/0.22/install.html) and [numpy](https://scipy.org/install.html).

It is build on Python 2.7. If you want to develop for Python 3.x, we can start that together.

## Using the Package

It has a factory instance that accepts the values "all", "default", and a list of char strings of names which is
defined on the factory list. The "all" argument calculates all available techind and the "default" calculates a
pre-determined list of technical indicators.

The input it is standardized to be a pandas DataFrame with OHLCV valeus, with column names in lower case.

`df = pandas.DataFrame(columns=['open', 'high', 'low', 'close', 'volume'])`

## Creating New Indicators

All new indicators have to be created in the file TechIndCUSTOM.py as a new class. All the specific parameters have to
be defined in the instance and have default values. To the technical indicator to be called, it needs to be inserted in
the factory list.

## AUTHOR

Developed by [Pedro Veronezi](https://github.com/veronezipedro)
