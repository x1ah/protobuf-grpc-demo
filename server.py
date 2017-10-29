# coding: utf-8

import time
from concurrent import futures

import grpc

import restaurant_pb2 as rpb
import restaurant_pb2_grpc as rpbrpc


class RestaurantOrderSysServer(rpbrpc.RestaurantOrderSysServicer):

    def __init__(self):
        self.db = []

    def GetOrderList(self, request, context):
        for i in range(10):
            order = rpb.Order(
                id=i, sku_id=i*10,
                status=1
            )
            yield order

    def PlaceOrder(self, request, context):
        return rpb.PlaceOrderResp(res=1)

    def CancelOrder(self, request, context):
        return rpb.PlaceOrderResp(res=1)

    def GetOrder(self, request, context):
        return rpb.Order(
            id=1, sku_id=1, status=1
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpbrpc.add_RestaurantOrderSysServicer_to_server(
        RestaurantOrderSysServer(), server
    )
    server.add_insecure_port('[::]:8888')
    server.start()
    print('rpc server started...')
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
