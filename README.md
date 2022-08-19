# Simple auth service example based on aiohttp and grpc

- python 3.9
- aiohttp
- aiohttp-pydantic
- mongodb

Command for generate/update python code for use grpc:
```shell
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. auth.proto
```
