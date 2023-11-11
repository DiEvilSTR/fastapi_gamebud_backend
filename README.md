# GameBud Backend Application

GameBud Backend Application

## Description

This is a simple RESTful API for a GameBud Backend application. The API is built using FastAPI, SQLAlchemy ORM, PostgreSQL and JWT authentication.

## Features

- Create a new user and user profile
- Login using JWT authentication
- View the your user profiles
- Add a new game to your user profile
- View the games in your user profile
- View the games by genre
- Fetch gamebud list
- Give potential gamebud a like or dislike
- Match with gamebud
- View your matches
- Chat with your matches

## Technologies

- Python
- FastAPI web framework
- SQLAlchemy database toolkit
- PostgreSQL database
- Pytest for testing
- JWT authentication for user authorization
- Websockets for real-time communication

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment: `virtualenv venv`
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up your PostgreSQL database and create the `.env` file with all the necessary configuration variables (check `.env.example`).
5. Run migrations using `.scripts/run_migration.bat`.
6. Start the server using `uvicorn main:app --reload` and navigate to `http://localhost:8000` to use the application.


## API Endpoints

### Swagger UI
- Swagger UI: `http://localhost:8000/docs`


## Project Structure

### Modules
```bash
└───app
    ├───alembic
    │   ├───versions
    │   │   └───migration.py
    │   └───env.py
    ├───module
    │   ├───crud
    │   │   └───crud.py
    │   ├───models
    │   │   ├───model.py
    │   │   └───model_test.py
    │   ├───schemas
    │   │   └───schema.py
    │   ├───endpoints.py
    │   ├───endpoints_test.py
    │   └───module_test.py
    ├───fixtures
    │   ├───data_for_db.py
    │   └───generate_game_genre_base.py
    ├───scripts
    │   ├───run_migration.bat
    │   └───test_myapp.bat
    ├───tests
    │   └───conftest.py
    ├───.env
    ├───.gitignore
    ├───alembic.ini
    ├───LICENSE
    ├───main.py
    ├───populate_db.py
    ├───README.md
    └───requirements.txt
```


## Testing
To run tests for the API, use the command `.scripts/test_myapp.bat`. This will run the automated tests in every module of app.


## License

This project is licensed under the MIT License - see the `LICENSE` file for details.