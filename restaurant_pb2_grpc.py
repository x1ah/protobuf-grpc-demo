# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import restaurant_pb2 as restaurant__pb2


class RestaurantOrderSysStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOrderList = channel.unary_stream(
        '/RestaurantOrderSys.RestaurantOrderSys/GetOrderList',
        request_serializer=restaurant__pb2.GetOrderListReq.SerializeToString,
        response_deserializer=restaurant__pb2.Order.FromString,
        )
    self.PlaceOrder = channel.unary_unary(
        '/RestaurantOrderSys.RestaurantOrderSys/PlaceOrder',
        request_serializer=restaurant__pb2.Order.SerializeToString,
        response_deserializer=restaurant__pb2.PlaceOrderResp.FromString,
        )
    self.CancelOrder = channel.unary_unary(
        '/RestaurantOrderSys.RestaurantOrderSys/CancelOrder',
        request_serializer=restaurant__pb2.Order.SerializeToString,
        response_deserializer=restaurant__pb2.PlaceOrderResp.FromString,
        )
    self.GetOrder = channel.unary_unary(
        '/RestaurantOrderSys.RestaurantOrderSys/GetOrder',
        request_serializer=restaurant__pb2.GetOrderListReq.SerializeToString,
        response_deserializer=restaurant__pb2.Order.FromString,
        )


class RestaurantOrderSysServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOrderList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PlaceOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RestaurantOrderSysServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOrderList': grpc.unary_stream_rpc_method_handler(
          servicer.GetOrderList,
          request_deserializer=restaurant__pb2.GetOrderListReq.FromString,
          response_serializer=restaurant__pb2.Order.SerializeToString,
      ),
      'PlaceOrder': grpc.unary_unary_rpc_method_handler(
          servicer.PlaceOrder,
          request_deserializer=restaurant__pb2.Order.FromString,
          response_serializer=restaurant__pb2.PlaceOrderResp.SerializeToString,
      ),
      'CancelOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CancelOrder,
          request_deserializer=restaurant__pb2.Order.FromString,
          response_serializer=restaurant__pb2.PlaceOrderResp.SerializeToString,
      ),
      'GetOrder': grpc.unary_unary_rpc_method_handler(
          servicer.GetOrder,
          request_deserializer=restaurant__pb2.GetOrderListReq.FromString,
          response_serializer=restaurant__pb2.Order.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'RestaurantOrderSys.RestaurantOrderSys', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))