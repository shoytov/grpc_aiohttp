from aiohttp import web
from aiohttp.web_request import Request


async def ping_endpoint(request: Request) -> web.json_response:
    """
    description: Тест работоспособности сервера.
    tags:
    - Health check
    produces:
    - application/json
    responses:
        "200":
            description: successful operation. Return "ok" in status field
        "405":
            description: invalid HTTP Method
    """
    return web.json_response({'status': 'ok'})
