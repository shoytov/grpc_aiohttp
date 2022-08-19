import asyncio
from typing import AsyncGenerator

import grpc
from aiohttp.web import Application

from app.config import GRPC_PORT
from app.services.user_service import GrpcUserRegistrationService, GrpcAuthorizationService
from . import auth_pb2_grpc


def _init(app: Application, listen_addr: str) -> grpc.aio.Server:
    server = grpc.aio.server()
    server.add_insecure_port(listen_addr)

    auth_pb2_grpc.add_RegistrationServicer_to_server(GrpcUserRegistrationService(app), server)
    auth_pb2_grpc.add_AuthorizationServicer_to_server(GrpcAuthorizationService(app), server)

    return server


async def _start_grpc_server(server: grpc.aio.Server) -> None:
    await server.start()
    await server.wait_for_termination()


async def grpc_channel_ctx(app: Application) -> AsyncGenerator:
    listen_addr = f'[::]:{GRPC_PORT}'

    server = _init(app, listen_addr)
    task = asyncio.create_task(_start_grpc_server(server))

    yield

    await server.stop(grace=None)
    task.cancel()
    await task
