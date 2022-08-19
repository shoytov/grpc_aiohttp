import pytest

from .initial import registration_stub, data, authorization_stub, data_for_login


@pytest.mark.asyncio
class TestAuth:
    async def test_registration(self):
        response = registration_stub.registration(data)
        assert response.email == data.email
        assert response.username == data.username

    async def test_authorization(self):
        response = authorization_stub.authorization(data_for_login)
        assert response.token is not None
