# coding: utf-8

import time

import grpc

import restaurant_pb2 as rpb
import restaurant_pb2_grpc as rpbrpc


class ResStub:
    '''restaurant order sys stub'''
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(':'.join(map(str, [host, port])))
        self.stub = rpbrpc.RestaurantOrderSysStub(self.channel)


class ResClient:
    '''restaurant order sys client'''
    def __init__(self, host, port):
        self.stub = ResStub(host, port).stub

    def get_order_list(self):
        oids = rpb.GetOrderListReq(orderIds=[1, 2, 3, 4])
        return self.stub.GetOrderList(oids)

    def place_order(self):
        order = rpb.Order(id=1, sku_id=1, status=rpb.OrderStatus.Value('SUCCEED'))
        return self.stub.PlaceOrder(order)

    def cancel_order(self):
        order = rpb.Order(id=1, sku_id=1, status=rpb.OrderStatus.Value('SUCCEED'))
        return self.stub.CancelOrder(order)

    def get_order(self):
        oids = rpb.GetOrderListReq
        oids.orderIds.extend([1, 2, 3, 4])
        return self.stub.GetOrder(oids)
