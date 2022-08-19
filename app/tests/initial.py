import grpc

from app.config import GRPC_PORT
from app.grpc_app.auth_pb2 import UserRequest
from app.grpc_app.auth_pb2_grpc import RegistrationStub

channel = grpc.insecure_channel(f'localhost:{GRPC_PORT}')
registration_stub = RegistrationStub(channel)

data = UserRequest(
    email='test@mail.ru',
    username='testuser',
    password='12345'
)
