# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pingpong.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pingpong.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0epingpong.proto\"\x15\n\x04Ping\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\x15\n\x04Pong\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"%\n\x07Numbers\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x1b\n\tSumResult\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32)\n\x0fPingPongService\x12\x16\n\x04ping\x12\x05.Ping\x1a\x05.Pong\"\x00\x32,\n\x0bMathService\x12\x1d\n\x03sum\x12\x08.Numbers\x1a\n.SumResult\"\x00\x62\x06proto3'
)




_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='Ping.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=39,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='Pong.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=62,
)


_NUMBERS = _descriptor.Descriptor(
  name='Numbers',
  full_name='Numbers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num1', full_name='Numbers.num1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num2', full_name='Numbers.num2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=101,
)


_SUMRESULT = _descriptor.Descriptor(
  name='SumResult',
  full_name='SumResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SumResult.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
DESCRIPTOR.message_types_by_name['Numbers'] = _NUMBERS
DESCRIPTOR.message_types_by_name['SumResult'] = _SUMRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), {
  'DESCRIPTOR' : _PING,
  '__module__' : 'pingpong_pb2'
  # @@protoc_insertion_point(class_scope:Ping)
  })
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'pingpong_pb2'
  # @@protoc_insertion_point(class_scope:Pong)
  })
_sym_db.RegisterMessage(Pong)

Numbers = _reflection.GeneratedProtocolMessageType('Numbers', (_message.Message,), {
  'DESCRIPTOR' : _NUMBERS,
  '__module__' : 'pingpong_pb2'
  # @@protoc_insertion_point(class_scope:Numbers)
  })
_sym_db.RegisterMessage(Numbers)

SumResult = _reflection.GeneratedProtocolMessageType('SumResult', (_message.Message,), {
  'DESCRIPTOR' : _SUMRESULT,
  '__module__' : 'pingpong_pb2'
  # @@protoc_insertion_point(class_scope:SumResult)
  })
_sym_db.RegisterMessage(SumResult)



_PINGPONGSERVICE = _descriptor.ServiceDescriptor(
  name='PingPongService',
  full_name='PingPongService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=132,
  serialized_end=173,
  methods=[
  _descriptor.MethodDescriptor(
    name='ping',
    full_name='PingPongService.ping',
    index=0,
    containing_service=None,
    input_type=_PING,
    output_type=_PONG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PINGPONGSERVICE)

DESCRIPTOR.services_by_name['PingPongService'] = _PINGPONGSERVICE


_MATHSERVICE = _descriptor.ServiceDescriptor(
  name='MathService',
  full_name='MathService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=175,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='sum',
    full_name='MathService.sum',
    index=0,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_SUMRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MATHSERVICE)

DESCRIPTOR.services_by_name['MathService'] = _MATHSERVICE

# @@protoc_insertion_point(module_scope)
