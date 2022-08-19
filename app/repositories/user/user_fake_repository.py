import uuid

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
                'password': password
            }
        )

        return _id
