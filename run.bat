@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python extract_improved.py
pause