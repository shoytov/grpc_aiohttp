from aiohttp import web
from aiohttp_pydantic import PydanticView
from aiohttp_pydantic.oas.typing import r201

from app.api.dependecies.repositories import get_user_repository
from app.domain.entities.user import User, CreatedUser
from app.repositories.user.base import AbstractUserRepository
from app.services.user_service import UserService


class UserRegistration(PydanticView):
    # @routes.post('/registration')
    async def post(self, user: User) -> r201[CreatedUser]:
        """
        description: Регистрация пользователя.
        tags:
        - Auth
        produces:
        - application/json
        parameters:
        - in: body
          name: body
          description: Создание нового пользователя
          required: true
          schema:
            $ref: '#/components/schemas/UserInput'
        responses:
            "201":
                description: Пользователь успешно создан
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/User'
            "400":
                description: Ошибка данных
            "405":
                description: invalid HTTP Method
        """
        repository: AbstractUserRepository = get_user_repository()
        user = await UserService(repository).registration(user.email, user.username, user.password)
        return web.json_response(user.dict())
