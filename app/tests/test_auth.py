import pytest

from .initial import registration_stub, data


@pytest.mark.asyncio
class TestAuth:
    async def test_registration(self):
        response = registration_stub.registration(data)
        assert response.email == data.email
        assert response.username == data.username
