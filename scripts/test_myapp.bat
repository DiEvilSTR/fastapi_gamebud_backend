@echo off

rem Activate the virtual environment
rem ./venv/Scripts/activate.bat

rem Run Alembic migrations
alembic -x test=true revision --autogenerate -m "Test migrations"
alembic -x test=true upgrade head

rem Run the unit tests
pytest -v user_profile_module/

rem Deactivate the virtual environment
rem ./venv/Scripts/deactivate.bat