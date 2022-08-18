from starlette.config import Config

config = Config('.env')

MONGODB_HOST = config.get('MONGODB_HOST', default='mongo')
MONGODB_USER = config.get('MONGODB_USER', default='testuser')
MONGODB_PASSWORD = config.get('MONGODB_PASSWORD', default='testpass')
MONGODB_PORT = config.get('MONGODB_PORT', default=27017)
MONGODB_DB = config.get('MONGODB_DB', default='authorization')
USER_COLLECTION = config.get('USER_COLLECTION', default='user')

JWT_KEY = config.get('JWT_KEY', default='secret')

GRPC_PORT = config.get('GRPC_PORT', default=50051)
