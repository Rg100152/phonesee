@echo off
REM PhoneSee Installation Script
REM Created by Raj Gautam

echo PhoneSee - Phone Number Intelligence Tool
echo Installing dependencies...
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing requirements...
pip install -r requirements.txt

REM Create necessary directories
echo Creating directories...
if not exist reports mkdir reports
if not exist .cache mkdir .cache
if not exist logs mkdir logs
if not exist exports mkdir exports

REM Copy .env.example to .env if not exists
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
    echo Please edit .env with your API keys
)

echo.
echo Installation complete!
echo Run 'python phonesee.py' to start PhoneSee
pause