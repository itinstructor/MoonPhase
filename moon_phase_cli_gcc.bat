cd c:\temp

python -m nuitka ^
    --onefile ^
    --mingw64 ^
    --lto=no ^
    --windows-icon-from-ico=moon.ico ^
    moon_phase_cli_2.py
pause