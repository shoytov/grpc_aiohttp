import grpc

from app.config import GRPC_PORT
from app.grpc_app.auth_pb2 import UserRequest
from app.grpc_app.auth_pb2_grpc import RegistrationStub

# открываем канал и создаем клиент
channel = grpc.insecure_channel(f'localhost:{GRPC_PORT}')
stub = RegistrationStub(channel)

data = UserRequest(
    email='test6@mail.ru',
    username='testuser',
    password='12345'
)

# запрос на регистрацию
response = stub.registration(data)
print(response)
