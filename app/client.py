import argparse

import grpc

from app.config import GRPC_PORT
from app.grpc_app.auth_pb2 import UserRequest, AuthUserRequest
from app.grpc_app.auth_pb2_grpc import RegistrationStub, AuthorizationStub

# открываем канал и создаем клиент
channel = grpc.insecure_channel(f'localhost:{GRPC_PORT}')
registration_stub = RegistrationStub(channel)
authorization_stub = AuthorizationStub(channel)

data = UserRequest(
    email='test6@mail.ru',
    username='testuser',
    password='12345'
)
data_for_login = AuthUserRequest(
    email='test6@mail.ru',
    password='12345'
)

# аргументы командной строки
parser = argparse.ArgumentParser(description='Client for test grpc')
parser.add_argument('action', type=str, help='Action for grpc')
args = parser.parse_args()

# запрос на регистрацию
if args.action == 'registration':
    response = registration_stub.registration(data)
    print(response)
elif args.action == 'authorization':
    response = authorization_stub.authorization(data_for_login)
    print(response)
