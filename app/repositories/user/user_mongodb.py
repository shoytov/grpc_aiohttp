from aiohttp.web import HTTPBadRequest
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic.networks import EmailStr
from pymongo.errors import DuplicateKeyError

from app.config import MONGODB_USER, MONGODB_PASSWORD, MONGODB_DB, MONGODB_HOST, MONGODB_PORT, USER_COLLECTION
from .base import AbstractUserRepository


class MongodbUserRepository(AbstractUserRepository):
    def __init__(self):
        self.client = AsyncIOMotorClient(self.connection_string)
        self.db = self.client[MONGODB_DB]

        # создаем индексы, если их нет
        collection = self.db[USER_COLLECTION]
        collection.create_index('email', unique=True)

    def __del__(self):
        self.client.close()

    @property
    def connection_string(self) -> str:
        if MONGODB_USER and MONGODB_PASSWORD:
            _connection_string = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}"
        else:
            _connection_string = f"mongodb://{MONGODB_HOST}:{MONGODB_PORT}"

        return _connection_string

    async def registration(self, email: EmailStr, username: str, password: str, token: str) -> str:
        collection = self.db[USER_COLLECTION]
        data = {
            'email': email,
            'username': username,
            'password': password,
            'token': token
        }

        try:
            user = await collection.insert_one(data)
        except DuplicateKeyError:
            raise HTTPBadRequest(text='User already exist')
        else:
            return user.inserted_id
