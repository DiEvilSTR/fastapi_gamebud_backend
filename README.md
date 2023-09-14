# GameBud Backend Application

GameBud Backend Application

## Description

This is a simple RESTful API for a GameBud Backend application. The API is built using FastAPI, SQLAlchemy ORM, PostgreSQL and JWT authentication.

## Features

- Create a new user and user profile
- Login using JWT authentication
- View the your user profiles

## Technologies

- Python
- FastAPI web framework
- SQLAlchemy database toolkit
- PostgreSQL database
- Pytest for testing
- JWT authentication for user authorization

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment: `virtualenv venv`
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up your PostgreSQL database and create the `.env` file with all the necessary configuration variables (check `.env.example`).
5. Run migrations using `.scripts/run_migration.bat`.
6. Start the server using `uvicorn main:app --reload` and navigate to `http://localhost:8000` to use the application.


## API Endpoints

### Users
- POST `/user/login`: Returns a JWT token for authentication
- POST `/user/logout`: Deletes authentication cookies
- POST `/user/create`: Creates a new user
- GET `/user/me`: Returns current user's profile
- PATCH `/user/me`: Updates current user's profile
- DELETE `/user/me`: Deletes current user, user's profile, and all user's tasks

### Game base
- POST `/game_genre`: Add a new game genre
- GET `/game_genre`: Returns a list of all game genres
- GET `/game_genre/{game_genre_id}`: Returns a specific game genre by ID
- PATCH `/game_genre/{game_genre_id}`: Updates a specific game genre by ID
- DELETE `/game_genre/{game_genre_id}`: Deletes a specific game genre by ID
- POST `/game`: Add a new game
- GET `/game`: Returns a list of all games
- GET `/game/{game_id}`: Returns a specific game by ID
- PATCH `/game/{game_id}`: Updates a specific game by ID
- DELETE `/game/{game_id}`: Deletes a specific game by ID


## Testing
To run tests for the API, use the command `.scripts/test_myapp.bat`. This will run the automated tests in every module of app.


## License

This project is licensed under the MIT License - see the `LICENSE` file for details.