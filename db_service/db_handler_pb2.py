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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64\x62_handler.proto\x12\ndb_service\"0\n\x16\x43heckUserExistsRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\")\n\x17\x43heckUserExistsResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\"(\n\x0eGetUUIDRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\"\x1f\n\x0fGetUUIDResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x86\x01\n\x14SetAccessDataRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x15\n\rsession_state\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x05\x12\x16\n\x0eschool_user_id\x18\x05 \x01(\t\"<\n\x15SetAccessDataResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"\x91\x01\n\x11SetNewUserRequest\x12\x16\n\x0eschool_user_id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x12\n\nexpires_in\x18\x03 \x01(\x05\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\t\x12\x15\n\rrefresh_token\x18\x05 \x01(\t\x12\x15\n\rsession_state\x18\x06 \x01(\t\"L\n\x12SetNewUserResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x11\n\tcapy_uuid\x18\x03 \x01(\t\"+\n\x1bGetAccessTokenByUUIDRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x9a\x01\n\x1cGetAccessTokenByUUIDResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0eschool_user_id\x18\x02 \x01(\t\x12\x13\n\x0btime_create\x18\x03 \x01(\x05\x12\x12\n\nexpires_in\x18\x04 \x01(\x05\x12\x0e\n\x06status\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"0\n\x10SetAvatarRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x02 \x01(\t\"8\n\x11SetAvatarResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\" \n\x10GetAvatarRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"H\n\x11GetAvatarResponse\x12\x0e\n\x06\x61vatar\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"<\n\x12GetPeerInfoRequest\x12\x14\n\x0crequest_uuid\x18\x01 \x01(\t\x12\x10\n\x08nickname\x18\x02 \x01(\t\"\x80\x01\n\x13GetPeerInfoResponse\x12\x0e\n\x06\x61vatar\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05login\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\x05\x32\xac\x05\n\tDBService\x12\\\n\x11\x63heck_user_exists\x12\".db_service.CheckUserExistsRequest\x1a#.db_service.CheckUserExistsResponse\x12\x43\n\x08get_uuid\x12\x1a.db_service.GetUUIDRequest\x1a\x1b.db_service.GetUUIDResponse\x12V\n\x0fset_access_data\x12 .db_service.SetAccessDataRequest\x1a!.db_service.SetAccessDataResponse\x12M\n\x0cset_new_user\x12\x1d.db_service.SetNewUserRequest\x1a\x1e.db_service.SetNewUserResponse\x12m\n\x18get_access_token_by_uuid\x12\'.db_service.GetAccessTokenByUUIDRequest\x1a(.db_service.GetAccessTokenByUUIDResponse\x12I\n\nset_avatar\x12\x1c.db_service.SetAvatarRequest\x1a\x1d.db_service.SetAvatarResponse\x12I\n\nget_avatar\x12\x1c.db_service.GetAvatarRequest\x1a\x1d.db_service.GetAvatarResponse\x12P\n\rget_peer_info\x12\x1e.db_service.GetPeerInfoRequest\x1a\x1f.db_service.GetPeerInfoResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'db_handler_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHECKUSEREXISTSREQUEST']._serialized_start=32
  _globals['_CHECKUSEREXISTSREQUEST']._serialized_end=80
  _globals['_CHECKUSEREXISTSRESPONSE']._serialized_start=82
  _globals['_CHECKUSEREXISTSRESPONSE']._serialized_end=123
  _globals['_GETUUIDREQUEST']._serialized_start=125
  _globals['_GETUUIDREQUEST']._serialized_end=165
  _globals['_GETUUIDRESPONSE']._serialized_start=167
  _globals['_GETUUIDRESPONSE']._serialized_end=198
  _globals['_SETACCESSDATAREQUEST']._serialized_start=201
  _globals['_SETACCESSDATAREQUEST']._serialized_end=335
  _globals['_SETACCESSDATARESPONSE']._serialized_start=337
  _globals['_SETACCESSDATARESPONSE']._serialized_end=397
  _globals['_SETNEWUSERREQUEST']._serialized_start=400
  _globals['_SETNEWUSERREQUEST']._serialized_end=545
  _globals['_SETNEWUSERRESPONSE']._serialized_start=547
  _globals['_SETNEWUSERRESPONSE']._serialized_end=623
  _globals['_GETACCESSTOKENBYUUIDREQUEST']._serialized_start=625
  _globals['_GETACCESSTOKENBYUUIDREQUEST']._serialized_end=668
  _globals['_GETACCESSTOKENBYUUIDRESPONSE']._serialized_start=671
  _globals['_GETACCESSTOKENBYUUIDRESPONSE']._serialized_end=825
  _globals['_SETAVATARREQUEST']._serialized_start=827
  _globals['_SETAVATARREQUEST']._serialized_end=875
  _globals['_SETAVATARRESPONSE']._serialized_start=877
  _globals['_SETAVATARRESPONSE']._serialized_end=933
  _globals['_GETAVATARREQUEST']._serialized_start=935
  _globals['_GETAVATARREQUEST']._serialized_end=967
  _globals['_GETAVATARRESPONSE']._serialized_start=969
  _globals['_GETAVATARRESPONSE']._serialized_end=1041
  _globals['_GETPEERINFOREQUEST']._serialized_start=1043
  _globals['_GETPEERINFOREQUEST']._serialized_end=1103
  _globals['_GETPEERINFORESPONSE']._serialized_start=1106
  _globals['_GETPEERINFORESPONSE']._serialized_end=1234
  _globals['_DBSERVICE']._serialized_start=1237
  _globals['_DBSERVICE']._serialized_end=1921
# @@protoc_insertion_point(module_scope)
