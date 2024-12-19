@echo off
REM Check if venv already exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists. Skipping creation.
)

REM Activate the virtual environment
call venv\Scripts\activate
REM Keep the virtual environment active for user interaction
echo Virtual environment activated. You can now run your scripts.

REM Install the required packages
echo Installing required packages...
pip install -r requirements.txt