echo Activating virtual environment...
call .\venv\Scripts\activate.bat
echo Virtual environment activated

echo Setting environment variables...
set APP_MODULE=main:app
set HOST=localhost
set PORT=8000
echo Environment variables set

echo Starting server at %HOST%:%PORT%...
uvicorn %APP_MODULE% --host %HOST% --port %PORT% --reload
echo Server started.

pause