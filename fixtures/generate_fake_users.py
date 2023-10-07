from faker import Faker
from sqlalchemy.orm import Session

from core.db import db_setup
from user_profile_module import User, UserGameAssociation
from game_base_module import Game, GameGenre, GameGenreAssociation
from bud_finder_module import BudLike, BudMatch


# Initialize Faker
fake = Faker()

# Generate and insert fake users
num_fake_users = 30


def create_fake_user(db: Session, num_fake_users: int):
    for _ in range(num_fake_users):
        fake_user = User(
            nickname=fake.user_name(),
            email=fake.email(),
            birthday=fake.date_of_birth(),
            gender=fake.random_element(elements=("male", "female", "other")),
            password=fake.password(),
        )
        db.add(fake_user)
        db.commit()


create_fake_user(db_setup.get_db, num_fake_users)
