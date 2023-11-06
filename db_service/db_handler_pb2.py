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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x62_handler.proto\x12\ndb_service\"8\n\x12GetSchoolIdRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"M\n\x13GetSchoolIdResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x11\n\tschool_id\x18\x03 \x01(\t\"0\n\x16\x43heckUserExistsRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\")\n\x17\x43heckUserExistsResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\".\n\x14GetExpireTimeRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\"B\n\x15GetExpireTimeResponse\x12\x13\n\x0b\x65xpire_time\x18\x01 \x01(\x05\x12\x14\n\x0ctime_created\x18\x02 \x01(\x05\"(\n\x0eGetUUIDRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\"\x1f\n\x0fGetUUIDResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x86\x01\n\x14SetAccessDataRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x15\n\rsession_state\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x05\x12\x16\n\x0eschool_user_id\x18\x05 \x01(\t\"<\n\x15SetAccessDataResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x32\xb0\x03\n\tDBService\x12P\n\rget_school_id\x12\x1e.db_service.GetSchoolIdRequest\x1a\x1f.db_service.GetSchoolIdResponse\x12\\\n\x11\x63heck_user_exists\x12\".db_service.CheckUserExistsRequest\x1a#.db_service.CheckUserExistsResponse\x12V\n\x0fget_expire_time\x12 .db_service.GetExpireTimeRequest\x1a!.db_service.GetExpireTimeResponse\x12\x43\n\x08get_uuid\x12\x1a.db_service.GetUUIDRequest\x1a\x1b.db_service.GetUUIDResponse\x12V\n\x0fset_access_data\x12 .db_service.SetAccessDataRequest\x1a!.db_service.SetAccessDataResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'db_handler_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETSCHOOLIDREQUEST']._serialized_start=32
  _globals['_GETSCHOOLIDREQUEST']._serialized_end=88
  _globals['_GETSCHOOLIDRESPONSE']._serialized_start=90
  _globals['_GETSCHOOLIDRESPONSE']._serialized_end=167
  _globals['_CHECKUSEREXISTSREQUEST']._serialized_start=169
  _globals['_CHECKUSEREXISTSREQUEST']._serialized_end=217
  _globals['_CHECKUSEREXISTSRESPONSE']._serialized_start=219
  _globals['_CHECKUSEREXISTSRESPONSE']._serialized_end=260
  _globals['_GETEXPIRETIMEREQUEST']._serialized_start=262
  _globals['_GETEXPIRETIMEREQUEST']._serialized_end=308
  _globals['_GETEXPIRETIMERESPONSE']._serialized_start=310
  _globals['_GETEXPIRETIMERESPONSE']._serialized_end=376
  _globals['_GETUUIDREQUEST']._serialized_start=378
  _globals['_GETUUIDREQUEST']._serialized_end=418
  _globals['_GETUUIDRESPONSE']._serialized_start=420
  _globals['_GETUUIDRESPONSE']._serialized_end=451
  _globals['_SETACCESSDATAREQUEST']._serialized_start=454
  _globals['_SETACCESSDATAREQUEST']._serialized_end=588
  _globals['_SETACCESSDATARESPONSE']._serialized_start=590
  _globals['_SETACCESSDATARESPONSE']._serialized_end=650
  _globals['_DBSERVICE']._serialized_start=653
  _globals['_DBSERVICE']._serialized_end=1085
# @@protoc_insertion_point(module_scope)
