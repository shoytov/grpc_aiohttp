from app.config import ENVIRONMENT
from app.repositories.user.base import AbstractUserRepository
from app.repositories.user.user_fake_repository import UserFakeRepository
from app.repositories.user.user_mongodb import MongodbUserRepository


def initial_user_repository() -> AbstractUserRepository:
    """
    Инициализация репозитория пользователя.
    """
    case = {
        'PRODUCTION': MongodbUserRepository(),
        'TEST': UserFakeRepository()
    }

    return case.get(ENVIRONMENT)

