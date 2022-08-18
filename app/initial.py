from app.repositories.user.base import AbstractUserRepository
from app.repositories.user.user_mongodb import MongodbUserRepository


def initial_user_repository() -> AbstractUserRepository:
    """
    Инициализация репозитория пользователя.
    """
    return MongodbUserRepository()
