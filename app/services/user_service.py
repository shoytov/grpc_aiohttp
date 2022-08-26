import hashlib
from abc import ABC, abstractmethod
from typing import Optional

import grpc
import jwt
from aiohttp.web import Application
from pydantic.networks import EmailStr

from app.config import JWT_KEY
from app.domain.entities.user import CreatedUser
from app.grpc_app.auth_pb2 import UserCreatedResponse, UserRequest, AuthUserRequest, TokenResponse
from app.grpc_app.auth_pb2_grpc import RegistrationServicer, AuthorizationServicer
from app.initial import initial_user_repository
from app.repositories.user.base import AbstractUserRepository


class AbstractUserService(ABC):
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    @classmethod
    def make_password(cls, raw_password: str) -> str:
        """
        Хэширование пароля.
        """
        return hashlib.md5(raw_password.encode('utf-8')).hexdigest()

    @abstractmethod
    async def registration(self, email: EmailStr, username: str, password: str) -> CreatedUser:
        """
        Регистрация нового пользователя. Возвращает объект созданного пользователя.
        """
        raise NotImplementedError()

    @abstractmethod
    async def authorization(self, email: EmailStr, password: str) -> str:
        """
        Авторизация пользователя. Возвращает токен.
        """
        raise NotImplementedError()


class UserService(AbstractUserService):
    async def registration(self, email: EmailStr, username: str, password: str) -> CreatedUser:
        token = jwt.encode({'email': email}, JWT_KEY, algorithm="HS256")

        user_id = await self.user_repository.registration(email, username, self.make_password(password), token)

        user = CreatedUser(
            id=str(user_id),
            email=email,
            username=username,
            token=token
        )

        return user

    async def authorization(self, email: EmailStr, password: str) -> str:
        return await self.user_repository.authorization(email, self.make_password(password))


class GrpcUserRegistrationService(RegistrationServicer):
    def __init__(self, app: Application, repository: Optional[AbstractUserRepository] = None) -> None:
        self.app = app

        if repository is None:
            self.service = UserService(initial_user_repository())
        else:
            self.service = UserService(repository)

    async def registration(self, request: UserRequest, context: grpc.aio.ServicerContext) -> UserCreatedResponse:
        created_user = await self.service.registration(request.email, request.username, request.password)
        return UserCreatedResponse(**created_user.dict())


class GrpcAuthorizationService(AuthorizationServicer):
    def __init__(self, app: Application, repository: Optional[AbstractUserRepository] = None) -> None:
        self.app = app

        if repository is None:
            self.service = UserService(initial_user_repository())
        else:
            self.service = UserService(repository)

    async def authorization(self, request: AuthUserRequest, context: grpc.aio.ServicerContext) -> TokenResponse:
        token = await self.service.authorization(request.email, request.password)
        return TokenResponse(token=token)
