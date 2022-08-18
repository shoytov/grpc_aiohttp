from pydantic import BaseModel
from pydantic.networks import EmailStr


class User(BaseModel):
    """
    Пользователь, который создается.
    """
    email: EmailStr
    username: str
    password: str


class CreatedUser(BaseModel):
    """
    Созданный пользователь.
    """
    id: str
    email: EmailStr
    username: str
    token: str
