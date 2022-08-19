from abc import ABC, abstractmethod

from pydantic.networks import EmailStr


class AbstractUserRepository(ABC):
    @abstractmethod
    async def registration(self, email: EmailStr, username: str, password: str, token: str) -> str:
        """
        Регистрация (создание) нового пользователя.
        Возвращает ID документа(записи).
        """
        raise NotImplementedError()

    @abstractmethod
    async def authorization(self, email: EmailStr, password: str) -> str:
        """
        Авторизация пользователя. Принимает почту и пароль, возвращает токен.
        """
        raise NotImplementedError()
