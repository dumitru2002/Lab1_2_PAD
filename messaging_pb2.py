# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: messaging.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'messaging.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmessaging.proto\"@\n\x0eMessageRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\":\n\x10SubscribeRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x17\n\x0fsubscriber_name\x18\x02 \x01(\t\"A\n\x0fMessageResponse\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t2y\n\x0eMessageService\x12\x33\n\x0ePublishMessage\x12\x0f.MessageRequest\x1a\x10.MessageResponse\x12\x32\n\tSubscribe\x12\x11.SubscribeRequest\x1a\x10.MessageResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messaging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEREQUEST']._serialized_start=19
  _globals['_MESSAGEREQUEST']._serialized_end=83
  _globals['_SUBSCRIBEREQUEST']._serialized_start=85
  _globals['_SUBSCRIBEREQUEST']._serialized_end=143
  _globals['_MESSAGERESPONSE']._serialized_start=145
  _globals['_MESSAGERESPONSE']._serialized_end=210
  _globals['_MESSAGESERVICE']._serialized_start=212
  _globals['_MESSAGESERVICE']._serialized_end=333
# @@protoc_insertion_point(module_scope)
