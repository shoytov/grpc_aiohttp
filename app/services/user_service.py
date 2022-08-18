import hashlib
from abc import ABC, abstractmethod

import grpc
import jwt
from aiohttp.web import Application
from pydantic.networks import EmailStr

from app.config import JWT_KEY
from app.domain.entities.user import CreatedUser
from app.grpc_app.auth_pb2 import UserCreatedResponse, UserRequest
from app.grpc_app.auth_pb2_grpc import RegistrationServicer
from app.initial import initial_user_repository
from app.repositories.user.base import AbstractUserRepository


class AbstractUserService(ABC):
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    @abstractmethod
    async def registration(self, email: EmailStr, username: str, password: str) -> CreatedUser:
        raise NotImplementedError()


class UserService(AbstractUserService):
    async def registration(self, email: EmailStr, username: str, password: str) -> CreatedUser:
        token = jwt.encode({'username': username}, JWT_KEY, algorithm="HS256")
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user_id = await self.user_repository.registration(email, username, password, token)

        user = CreatedUser(
            id=str(user_id),
            email=email,
            username=username,
            token=token
        )

        return user


class GrpcUserRegistrationService(RegistrationServicer):
    def __init__(self, app: Application) -> None:
        self.app = app
        self.service = UserService(initial_user_repository())

    async def registration(self, request: UserRequest, context: grpc.aio.ServicerContext) -> UserCreatedResponse:
        created_user = await self.service.registration(request.email, request.username, request.password)
        return UserCreatedResponse(**created_user.dict())
