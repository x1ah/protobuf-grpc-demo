>Protobuf 和 gRPC 的一个 Demo，一个简单的餐厅订单系统。待完善....

### 生成代码
```shell
$ pip install grpcio-tools
$ python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ restaurant.proto
```

### run server
```shell
$ python server.py
```

### client
```shell
> from client import ResClient
> client = ResClient('127.0.0.1', '8888')
> client.get_order()
> client.place_order()
```
