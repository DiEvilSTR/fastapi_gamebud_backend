import pytest

from datetime import datetime
from unittest.mock import MagicMock, patch

from core.config import settings
from user_profile_module.models.user import User
from tests.conftest import get_test_db, test_client

user_data = {
    "nickname": "test_user_1",
    "email": "test@test.com",
    "password": "test_password"
}

auth_data = {
    "email": "test@test.com",
    "password": "test_password"
}

updated_user_data = {
    "nickname": "updated_one",
    "bio": "Test bio",
}

auth_headers = None


# System test the entire system end-to-end, from the user's perspective


def test_user_signup(test_client):
    # 1 Create a new user and user profile
    response = test_client.post(
        f"{settings.API_V1_STR}/user/signup/",
        json=user_data
    )
    # Test that the user was created successfully
    assert response.status_code == 201, \
        "The response should contain a success status code"
    assert response is not None, \
        "The response should not be None"
    assert response.json()["nickname"] == user_data["nickname"], \
        "The response should contain the username"
    assert response.json()["email"] == user_data["email"], \
        "The response should contain the email"
    assert "hashed_password" not in response.json(), \
        "The response should not contain the hashed_password"

    # Test that the UUID column was automatically populated
    assert "uuid" in response.json(), \
        "The response should contain uuid"
    assert len(response.json()["uuid"]) == 36, \
        f"Expected uuid to be 36 characters long, got {len(response.json()['uuid'])}"

    # Test that the bio column was automatically populated
    assert "bio" in response.json(), \
        "The response should contain bio"
    assert response.json()["bio"] is None, \
        "The bio in response should be None"

    # Test that the Boolean columns were automatically populated
    assert "is_active" in response.json(), \
        "The response should contain is_active"
    assert response.json()["is_active"] is True, \
        "The default value for is_active should be True"
    assert "is_superuser" in response.json(), \
        "The response should contain is_superuser"
    assert response.json()["is_superuser"] is False, \
        "The default value for is_superuser should be False"

    # Test that the Timestamp columns were automatically populated
    assert "created_at" in response.json(), \
        "The response should contain created_at"
    assert "updated_at" in response.json(), \
        "The response should contain updated_at"


def test_user_login(test_client):
    # 2 Login with the new user
    response = test_client.post(
        f"{settings.API_V1_STR}/user/login/",
        json=auth_data
    )

    # Test that the user was logged in successfully
    assert response.status_code == 200, \
        "The response should contain a success status code"
    assert response is not None, \
        "The response should not be None"
    assert response.json()["access_token"] is not None, \
        "The response should contain the access token"
    assert response.json()["token_type"] == "bearer", \
        "The response should contain the token type"

    # Save the auth headers for future requests
    auth_token = response.json()["access_token"]
    global auth_headers
    auth_headers = {"Authorization": f"Bearer {auth_token}"}


def test_read_current_user(test_client):
    # 3 Retrieve the user profile
    response = test_client.get(
        f"{settings.API_V1_STR}/user/me/",
        headers=auth_headers
    )

    # Test that the user profile was retrieved successfully
    assert response.status_code == 200, \
        "The response should contain a success status code"
    assert response is not None, \
        "The response should not be None"
    assert response.json()["email"] == user_data["email"], \
        "The response should contain right email"
    assert "hashed_password" not in response.json(), \
        "The response should not contain the hashed_password"


def test_update_current_user(test_client):
    # 4 Update the user profile
    response = test_client.patch(
        f"{settings.API_V1_STR}/user/me/",
        headers=auth_headers,
        json=updated_user_data
    )

    # Test that the user was updated successfully
    assert response.status_code == 200, \
        "The response should contain a success status code"
    assert response is not None, \
        "The response should not be None"
    assert response.json()["email"] == user_data["email"], \
        "The response should contain the right email"
    assert response.json()["nickname"] == updated_user_data["nickname"], \
        "The response should contain the updated nickname"
    assert response.json()["bio"] == updated_user_data["bio"], \
        "The response should contain the updated bio"

    # Test that the Timestamp columns were automatically updated
    assert response.json()["created_at"] != response.json()["updated_at"], \
        "The created_at and updated_at should be different"


def test_user_logout(test_client):
    # 5 Logout
    response = test_client.post(
        f"{settings.API_V1_STR}/user/logout/",
        headers=auth_headers
    )

    # Test that the user was logged out successfully
    assert response.status_code == 200, \
        "The response should contain a success status code"


def test_delete_current_user(get_test_db, test_client):
    # 6 Delete the user
    response = test_client.delete(
        f"{settings.API_V1_STR}/user/me",
        headers=auth_headers,
    )

    # Test that response was successful
    assert response.status_code == 200, \
        "The response should contain a success status code"

    # Test that the user was deleted successfully
    test_user = get_test_db.query(User).filter(
        User.email == user_data["email"]).first()
    assert test_user is None, \
        "The response should be None"
