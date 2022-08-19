import grpc

from app.config import GRPC_PORT
from app.grpc_app.auth_pb2 import UserRequest, AuthUserRequest
from app.grpc_app.auth_pb2_grpc import RegistrationStub, AuthorizationStub

channel = grpc.insecure_channel(f'localhost:{GRPC_PORT}')
registration_stub = RegistrationStub(channel)
authorization_stub = AuthorizationStub(channel)

data = UserRequest(
    email='test@mail.ru',
    username='testuser',
    password='12345'
)

data_for_login = AuthUserRequest(
    email='test6@mail.ru',
    password='12345'
)
