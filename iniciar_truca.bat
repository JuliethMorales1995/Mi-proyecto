@echo off
cd /d "%~dp0Ventas"
if exist "Scripts\activate.bat" call "Scripts\activate.bat"
streamlit run app.py
pause