@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Run FastAPI server and keep terminal open
python -m uvicorn main:app --reload

REM Keep the terminal open after server stops
pause