# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item_records.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12item_records.proto\"\x0e\n\x0c\x45mptyRequest\"\'\n\x18PingItemsRecordsResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"1\n\x04Item\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x66oo\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\"\'\n\x10GetItemsResponse\x12\x13\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x05.Item2\x81\x01\n\x0cItemsRecords\x12<\n\x10PingItemsRecords\x12\r.EmptyRequest\x1a\x19.PingItemsRecordsResponse\x12\x33\n\x0fGetItemsRecords\x12\r.EmptyRequest\x1a\x11.GetItemsResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'item_records_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYREQUEST._serialized_start=22
  _EMPTYREQUEST._serialized_end=36
  _PINGITEMSRECORDSRESPONSE._serialized_start=38
  _PINGITEMSRECORDSRESPONSE._serialized_end=77
  _ITEM._serialized_start=79
  _ITEM._serialized_end=128
  _GETITEMSRESPONSE._serialized_start=130
  _GETITEMSRESPONSE._serialized_end=169
  _ITEMSRECORDS._serialized_start=172
  _ITEMSRECORDS._serialized_end=301
# @@protoc_insertion_point(module_scope)
