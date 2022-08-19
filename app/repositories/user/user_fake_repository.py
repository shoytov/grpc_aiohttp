import uuid

from aiohttp.web import HTTPBadRequest
from pydantic.networks import EmailStr

from .base import AbstractUserRepository


class UserFakeRepository(AbstractUserRepository):
    users = []

    async def registration(self, email: EmailStr, username: str, password: str, token: str) -> str:
        _id = uuid.uuid4().hex

        self.users.append(
            {
                'id': _id,
                'email': email,
                'username': username,
                'password': password,
                'token': token
            }
        )

        return _id

    async def authorization(self, email: EmailStr, password: str) -> str:
        try:
            return self.users[0].get('token')
        except IndexError:
            raise HTTPBadRequest(text='User not found')
