# Moon Phase App

Python CLI and Tkinter GUI programs to calculate moon phases and other moon data.

Uses the Python [ephem](https://pypi.org/project/ephem/) library.

Batch files are included to use [Nuitka](https://pypi.org/project/Nuitka/) to convert the Python .py program to a Windows exe using GCC.

## Requirements

- pip install ephem
- pip install geopy
- pip install tkcalendar

## Version History

- (05-24-24) Tkinter add Double Click on Calendar to show moon phase
- (10-20-23) CLI Moon phase descriptions work
- (07-10-23) Refactor to OOP. Move all ephem moon logic into moon_class.py
- (07-08-23) Initial commit of CLI and GUI

### License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)</a>.

Copyright (c) 2024 William A Loring