cd c:\temp

python -m nuitka ^
    --onefile ^
    --mingw64 ^
    --lto=no ^
    --windows-disable-console ^
    --include-package=babel.numbers ^
    --enable-plugin=tk-inter ^
    --windows-icon-from-ico=moon.ico ^
    -o moon_phase_gui.exe ^
    moon_phase_gui.py
pause

