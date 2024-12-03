cd c:\temp

python -m nuitka ^
    --onefile ^
    --mingw64 ^
    --lto=no ^
    --windows-icon-from-ico=moon.ico ^
    -o moon_phase_cli.exe ^
    moon_phase_cli.py
pause