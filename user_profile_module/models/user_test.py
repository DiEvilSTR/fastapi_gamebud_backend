import pytest

from datetime import datetime

from user_profile_module.models.user import User
from tests.conftest import get_test_db

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


def test_user_model(get_test_db):
    with get_test_db as db:
        # Create a new user and save it to the database
        nickname = test_user_1["nickname"]
        email = test_user_1["email"]
        hashed_password = password
        user = User(nickname=nickname, email=email,
                    hashed_password=hashed_password)
        db.add(user)
        db.commit()

        # Retrieve the user from the database and check that its attributes match the input
        db_test_user = db.query(User).filter_by(email=email).first()
        assert db_test_user.nickname == nickname, \
            f"Expected username to be {nickname}, got {db_test_user.nickname}"
        assert db_test_user.email == email, \
            f"Expected email to be {email}, got {db_test_user.email}"
        assert db_test_user.hashed_password == password, \
            f"Expected hashed_password to be {password}, got {db_test_user.hashed_password}"

        # Test that the UUID column was automatically populated
        assert isinstance(db_test_user.uuid, str), \
            f"Expected uuid to be str, got {type(db_test_user.uuid)}"
        assert len(db_test_user.uuid) == 36, \
            f"Expected uuid to be 36 characters long, got {len(db_test_user.uuid)}"

        # Test that the Boolean columns were automatically populated
        assert isinstance(db_test_user.is_active, bool), \
            f"Expected is_active to be bool, got {type(db_test_user.is_active)}"
        assert isinstance(db_test_user.is_superuser, bool), \
            f"Expected is_superuser to be bool, got {type(db_test_user.is_superuser)}"

        # Test that the bio columns were created and is None
        assert db_test_user.bio is None, \
            f"Expected bio to be None, got {db_test_user.bio}"

        # Test that the Timestamp columns were automatically populated
        assert isinstance(db_test_user.created_at, datetime), \
            f"Expected created_at to be datetime, got {type(db_test_user.created_at)}"
        assert isinstance(db_test_user.updated_at, datetime), \
            f"Expected updated_at to be datetime, got {type(db_test_user.updated_at)}"
        assert db_test_user.created_at == db_test_user.updated_at, \
            "Expected created_at and updated_at to be equal"

        # Delete the user from the database
        db.delete(db_test_user)
        db.commit()
