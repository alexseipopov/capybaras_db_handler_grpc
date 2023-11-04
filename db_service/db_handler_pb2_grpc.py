# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import db_service.db_handler_pb2 as db__handler__pb2


class DBServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_school_id = channel.unary_unary(
                '/db_service.DBService/get_school_id',
                request_serializer=db__handler__pb2.GetSchoolIdRequest.SerializeToString,
                response_deserializer=db__handler__pb2.GetSchoolIdResponse.FromString,
                )
        self.check_user_exists = channel.unary_unary(
                '/db_service.DBService/check_user_exists',
                request_serializer=db__handler__pb2.CheckUserExistsRequest.SerializeToString,
                response_deserializer=db__handler__pb2.CheckUserExistsResponse.FromString,
                )


class DBServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_school_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def check_user_exists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_school_id': grpc.unary_unary_rpc_method_handler(
                    servicer.get_school_id,
                    request_deserializer=db__handler__pb2.GetSchoolIdRequest.FromString,
                    response_serializer=db__handler__pb2.GetSchoolIdResponse.SerializeToString,
            ),
            'check_user_exists': grpc.unary_unary_rpc_method_handler(
                    servicer.check_user_exists,
                    request_deserializer=db__handler__pb2.CheckUserExistsRequest.FromString,
                    response_serializer=db__handler__pb2.CheckUserExistsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'db_service.DBService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_school_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db_service.DBService/get_school_id',
            db__handler__pb2.GetSchoolIdRequest.SerializeToString,
            db__handler__pb2.GetSchoolIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def check_user_exists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/db_service.DBService/check_user_exists',
            db__handler__pb2.CheckUserExistsRequest.SerializeToString,
            db__handler__pb2.CheckUserExistsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
