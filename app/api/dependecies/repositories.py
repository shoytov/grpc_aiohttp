from app.repositories.user.base import AbstractUserRepository
from app.repositories.user.user_mongodb import MongodbUserRepository


def get_user_repository() -> AbstractUserRepository:
    return MongodbUserRepository()
