# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db_handler.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x62_handler.proto\x12\ndb_service\"0\n\x16\x43heckUserExistsRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\")\n\x17\x43heckUserExistsResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\".\n\x14GetExpireTimeRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\"B\n\x15GetExpireTimeResponse\x12\x13\n\x0b\x65xpire_time\x18\x01 \x01(\x05\x12\x14\n\x0ctime_created\x18\x02 \x01(\x05\"(\n\x0eGetUUIDRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\"\x1f\n\x0fGetUUIDResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x86\x01\n\x14SetAccessDataRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x15\n\rsession_state\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x05\x12\x16\n\x0eschool_user_id\x18\x05 \x01(\t\"<\n\x15SetAccessDataResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"\x91\x01\n\x11SetNewUserRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x12\n\nexpires_in\x18\x03 \x01(\x05\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\t\x12\x15\n\rrefresh_token\x18\x05 \x01(\t\x12\x15\n\rsession_state\x18\x06 \x01(\t\"L\n\x12SetNewUserResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x11\n\tcapy_uuid\x18\x03 \x01(\t\"+\n\x1bGetAccessTokenByUUIDRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x9a\x01\n\x1cGetAccessTokenByUUIDResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0eschool_user_id\x18\x02 \x01(\t\x12\x13\n\x0btime_create\x18\x03 \x01(\x05\x12\x12\n\nexpires_in\x18\x04 \x01(\x05\x12\x0e\n\x06status\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t2\x9c\x04\n\tDBService\x12\\\n\x11\x63heck_user_exists\x12\".db_service.CheckUserExistsRequest\x1a#.db_service.CheckUserExistsResponse\x12V\n\x0fget_expire_time\x12 .db_service.GetExpireTimeRequest\x1a!.db_service.GetExpireTimeResponse\x12\x43\n\x08get_uuid\x12\x1a.db_service.GetUUIDRequest\x1a\x1b.db_service.GetUUIDResponse\x12V\n\x0fset_access_data\x12 .db_service.SetAccessDataRequest\x1a!.db_service.SetAccessDataResponse\x12M\n\x0cset_new_user\x12\x1d.db_service.SetNewUserRequest\x1a\x1e.db_service.SetNewUserResponse\x12m\n\x18get_access_token_by_uuid\x12\'.db_service.GetAccessTokenByUUIDRequest\x1a(.db_service.GetAccessTokenByUUIDResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'db_handler_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHECKUSEREXISTSREQUEST']._serialized_start=32
  _globals['_CHECKUSEREXISTSREQUEST']._serialized_end=80
  _globals['_CHECKUSEREXISTSRESPONSE']._serialized_start=82
  _globals['_CHECKUSEREXISTSRESPONSE']._serialized_end=123
  _globals['_GETEXPIRETIMEREQUEST']._serialized_start=125
  _globals['_GETEXPIRETIMEREQUEST']._serialized_end=171
  _globals['_GETEXPIRETIMERESPONSE']._serialized_start=173
  _globals['_GETEXPIRETIMERESPONSE']._serialized_end=239
  _globals['_GETUUIDREQUEST']._serialized_start=241
  _globals['_GETUUIDREQUEST']._serialized_end=281
  _globals['_GETUUIDRESPONSE']._serialized_start=283
  _globals['_GETUUIDRESPONSE']._serialized_end=314
  _globals['_SETACCESSDATAREQUEST']._serialized_start=317
  _globals['_SETACCESSDATAREQUEST']._serialized_end=451
  _globals['_SETACCESSDATARESPONSE']._serialized_start=453
  _globals['_SETACCESSDATARESPONSE']._serialized_end=513
  _globals['_SETNEWUSERREQUEST']._serialized_start=516
  _globals['_SETNEWUSERREQUEST']._serialized_end=661
  _globals['_SETNEWUSERRESPONSE']._serialized_start=663
  _globals['_SETNEWUSERRESPONSE']._serialized_end=739
  _globals['_GETACCESSTOKENBYUUIDREQUEST']._serialized_start=741
  _globals['_GETACCESSTOKENBYUUIDREQUEST']._serialized_end=784
  _globals['_GETACCESSTOKENBYUUIDRESPONSE']._serialized_start=787
  _globals['_GETACCESSTOKENBYUUIDRESPONSE']._serialized_end=941
  _globals['_DBSERVICE']._serialized_start=944
  _globals['_DBSERVICE']._serialized_end=1484
# @@protoc_insertion_point(module_scope)
