from aiohttp import web
from aiohttp_pydantic import oas
from aiohttp_swagger import setup_swagger

from app.api.routes.auth import UserRegistration
from app.api.routes.ping import ping_endpoint
from app.api.schemas import schemas
from app.grpc_app.grpc_server import grpc_channel_ctx


async def init():
    app = web.Application()
    app.router.add_route('GET', "/ping", ping_endpoint)
    app.router.add_view("/registration", UserRegistration)

    setup_swagger(app, swagger_url="/docs", title="Swagger", ui_version=3, definitions=schemas)
    oas.setup(app, version_spec="1.0.1", title_spec="My App")

    app.cleanup_ctx.append(grpc_channel_ctx)

    return app

application = init()


async def app_factory():
    """
    Для локальной разработки при запуске через "adev runserver".
    """
    return await init()

if __name__ == "__main__":
    web.run_app(application, port=8000)
