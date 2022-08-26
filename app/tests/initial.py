from app.grpc_app.auth_pb2 import UserRequest, AuthUserRequest

data = UserRequest(
    email='test@mail.ru',
    username='testuser',
    password='12345'
)

data_for_login = AuthUserRequest(
    email='test6@mail.ru',
    password='12345'
)


class DummyStream:
    response = None

    def __init__(self, request):
        self.request = request

    async def recv_message(self):
        return self.request

    async def send_message(self, message):
        self.response = message


stream = DummyStream(None)
