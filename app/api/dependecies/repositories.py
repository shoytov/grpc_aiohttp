from app.initial import initial_user_repository
from app.repositories.user.base import AbstractUserRepository


def get_user_repository() -> AbstractUserRepository:
    return initial_user_repository()
