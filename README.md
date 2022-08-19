# Simple auth service example based on aiohttp and grpc

- python 3.9
- aiohttp
- aiohttp-pydantic
- mongodb

This example contains 2 actions:
- registration
- authorization

Command for generate/update python code for use grpc:
```shell
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. auth.proto
```

run:
```shell
docker-compose up -d
```

stop:
```shell
docker-compose down
```

## Tests
If you want to run tests uncomment this in .env file
```shell
ENVIRONMENT=TEST
```
then run:
```shell
pytest
```
___

Also, you may start client.py in ```PRODUCTION``` environment:
- for registration
```shell
python app/client.py registration
```
- for authorization
```shell
python app/client.py authorization
```
