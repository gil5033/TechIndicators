# Technical Indicator sub-Package

A package aimed at providing a wrapper for Technical Indicator calculations. It uses the TA-lib package and develop a
wrapper for this package and a framework to custom indicators.

## USING THE PACKAGE

It has a factory instance that accepts the values "all", "default", and a list of char strings of names which is
defined on the factory list. The "all" argument calculates all available techind and the "default" calculates a
pre-determined list of technical indicators.

## CREATING NEW INDICATORS

All new indicators have to be created in the file TechIndCUSTOM.py as a new class. All the specific parameters have to
be defined in the instance and have default values. To the technical indicator to be called, it needs to be inserted in
the factory list.

## AUTHORS

Developed by [Pedro Veronezi](https://github.com/veronezipedro)