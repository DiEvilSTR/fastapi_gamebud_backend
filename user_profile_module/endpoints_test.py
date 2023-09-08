import pytest
from unittest.mock import MagicMock, patch, ANY

from core.config import settings
from core.jwt_authentication.jwt_bearer import jwt_scheme
from main import app
from tests.conftest import test_client

test_user_1 = {
    "nickname": "test_user_1",
    "uuid": "test_uuid_1",
    "email": "test@test.com",
    "bio": "test bio",
    "is_active": True,
    "is_superuser": False,
    "created_at": "2038-01-19T03:14:07.123456",
    "updated_at": "2038-01-19T03:14:07.123456"
}

password = "test_password"


# Add the is_active attribute to the test_user_obj_1 object


class TestUser:
    def __setattr__(self, key, value):
        self.__dict__[key] = value


test_user_obj_1 = TestUser()
test_user_obj_1.__dict__.update(test_user_1)
test_user_obj_1.is_active = test_user_1.get(
    'is_active', test_user_1["is_active"])


# Override the JWT scheme dependency in the test environment


def mock_jwt_scheme():
    return test_user_1["email"]


app.dependency_overrides[jwt_scheme] = mock_jwt_scheme


def test_user_login(test_client):
    # 1 Test the user_login endpoint for calling the crud.authenticate function and sign_jwt function
    mock_authenticate = MagicMock(return_value=True)
    mock_sign_jwt = MagicMock(
        return_value={"access_token": "test_token", "token_type": "bearer"})
    mock_get_user_by_email = MagicMock(return_value=test_user_obj_1)
    with patch("user_profile_module.crud.user_crud.authenticate", mock_authenticate), \
            patch("core.jwt_authentication.jwt_handler.sign_jwt", mock_sign_jwt), \
    patch("user_profile_module.crud.user_crud.get_user_by_email", mock_get_user_by_email):
        response = test_client.post(
            f"{settings.API_V1_STR}/user/login/",
            json={"email": test_user_1["email"], "password": password}
        )
        mock_authenticate.assert_called_once(), \
            "The crud's authenticate function should be called"
        mock_get_user_by_email.assert_called_once(), \
            "The crud's get_user_by_email function should be called"
        mock_sign_jwt.assert_called_once(), \
            "The jwt_handler's sign_jwt function should be called"
        assert response.status_code == 200, \
            "The response should contain a success status code"
        assert response.json() == {"access_token": "test_token", "token_type": "bearer"}, \
            "The response should contain the access token"


def test_user_signup(test_client):
    # 2 Test the user_signup endpoint for calling the crud.create_user function
    mock_get_user_by_email = MagicMock(return_value=None)
    mock_create_user = MagicMock(return_value=test_user_1)
    with patch("user_profile_module.crud.user_crud.get_user_by_email", mock_get_user_by_email), \
            patch("user_profile_module.crud.user_crud.create_user", mock_create_user):
        response = test_client.post(
            f"{settings.API_V1_STR}/user/signup/",
            json={"nickname": test_user_1["nickname"],
                  "email": test_user_1["email"], "password": password}
        )
        mock_get_user_by_email.assert_called_once(), \
            "The crud's get_user function should be called"
        mock_create_user.assert_called_once(), \
            "The crud's create_user function should be called"
        assert response.status_code == 201, \
            "The response should contain a created status code"
        assert response.json() == test_user_1, \
            "The response should be a dict containing Test user"


def test_read_current_user(test_client):
    # 3 Test the read_current_user endpoint for calling the crud_user_profile.user_profile_get function
    mock_get_user_by_email = MagicMock(return_value=test_user_1)
    with patch("user_profile_module.crud.user_crud.get_user_by_email", mock_get_user_by_email):
        response = test_client.get(
            f"{settings.API_V1_STR}/user/me/",
            headers={"Authorization": "Bearer test_token"}
        )
        mock_get_user_by_email.assert_called_once_with(db=ANY, email=test_user_1['email']), \
            "The crud's get_user_by_email function should be called with the test_user1 email"
        assert response.status_code == 200, \
            "The response should contain a success status code"
        assert response.json() == test_user_1, \
            "The response should be a dict containing Test user profile"


def test_update_user_profile(test_client):
    # 4 Test the update_current_user endpoint for calling the crud_user_profile's user_profile_get and user_profile_update functions
    mock_get_user_by_email = MagicMock(return_value=test_user_1)
    mock_update_user = MagicMock(return_value=test_user_1)
    with patch("user_profile_module.crud.user_crud.get_user_by_email", mock_get_user_by_email), \
            patch("user_profile_module.crud.user_crud.update_user", mock_update_user):
        response = test_client.patch(
            f"{settings.API_V1_STR}/user/me/",
            headers={"Authorization": "Bearer test_token"},
            json={"nickname": "test_user_1", "bio": "test bio"}
        )
        mock_get_user_by_email.assert_called_once_with(db=ANY, email=test_user_1['email']), \
            "The crud's get_user_by_email function should be called with the test_user_1 email"
        mock_update_user.assert_called_once_with(
            db=ANY,
            user=ANY,
            email=test_user_1['email']
        ), \
            "The crud's get_user_by_email function should be called with the test_user_1 user"
        assert response.status_code == 200, \
            "The response should contain a success status code"
        assert response.json() == test_user_1, \
            "The response should be a dict containing Test user profile"


def test_delete_current_user(test_client):
    # 5 Test the delete_current_user endpoint for calling the crud_user's delete_user function
    mock_get_user_by_email = MagicMock(return_value=test_user_1)
    mock_delete_user = MagicMock(return_value=test_user_1)
    with patch("user_profile_module.crud.user_crud.get_user_by_email", mock_get_user_by_email), \
            patch("user_profile_module.crud.user_crud.delete_user", mock_delete_user):
        response = test_client.delete(
            f"{settings.API_V1_STR}/user/me/",
            headers={"Authorization": "Bearer test_token"}
        )
        mock_get_user_by_email.assert_called_once_with(db=ANY, email=test_user_1['email']), \
            "The crud's get_user_by_email function should be called with the test_user_1 email"
        mock_delete_user.assert_called_once_with(db=ANY, email=test_user_1['email']), \
            "The crud's delete_user function should be called with the test_user_1 email"
        assert response.status_code == 200, \
            "The response should contain a success status code"
        assert response.json() == {"detail": f"User with email {test_user_1['email']} deleted successfully."}, \
            "The response should be a dict containing a success message"
