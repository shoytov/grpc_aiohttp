import pytest

from app.main import application
from app.repositories.user.user_fake_repository import UserFakeRepository
from app.services.user_service import GrpcAuthorizationService, GrpcUserRegistrationService
from .initial import data, data_for_login, stream


@pytest.mark.asyncio
class TestAuth:
    async def test_registration(self):
        service = GrpcUserRegistrationService(application, UserFakeRepository())
        response = await service.registration(data, stream)  # noqa

        assert response.email == data.email
        assert response.username == data.username

    async def test_authorization(self):
        service = GrpcAuthorizationService(application, UserFakeRepository())
        response = await service.authorization(data_for_login, stream)  # noqa

        assert response.token is not None
