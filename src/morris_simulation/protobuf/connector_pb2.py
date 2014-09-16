# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connector.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='connector.proto',
  package='',
  serialized_pb='\n\x0f\x63onnector.proto\"\x9a\x01\n\x07\x43ommand\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x14.Command.CommandType:\x07getInfo\x12\r\n\x05\x61ngle\x18\x02 \x01(\x05\"S\n\x0b\x43ommandType\x12\x0c\n\x08\x64oAction\x10\x00\x12\n\n\x06rotate\x10\x01\x12\x0b\n\x07getInfo\x10\x02\x12\x0e\n\nstartRobot\x10\x03\x12\r\n\tstopRobot\x10\x04\"7\n\x08Landmark\x12\n\n\x02id\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x02\x12\t\n\x01y\x18\x03 \x02(\x02\x12\t\n\x01z\x18\x04 \x02(\x02\"\x1a\n\x0b\x41\x66\x66ordances\x12\x0b\n\x03\x61\x66\x66\x18\x01 \x03(\x08\"P\n\x08Response\x12\n\n\x02ok\x18\x01 \x02(\x08\x12\x1c\n\tlandmarks\x18\x02 \x03(\x0b\x32\t.Landmark\x12\x1a\n\x04\x61\x66\x66s\x18\x03 \x01(\x0b\x32\x0c.AffordancesB\x19\n\x17\x65\x64u.usf.ratsim.protobuf')



_COMMAND_COMMANDTYPE = _descriptor.EnumDescriptor(
  name='CommandType',
  full_name='Command.CommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='doAction', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='rotate', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='getInfo', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='startRobot', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stopRobot', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=91,
  serialized_end=174,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Command.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle', full_name='Command.angle', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMAND_COMMANDTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=20,
  serialized_end=174,
)


_LANDMARK = _descriptor.Descriptor(
  name='Landmark',
  full_name='Landmark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Landmark.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='Landmark.x', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Landmark.y', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='Landmark.z', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=176,
  serialized_end=231,
)


_AFFORDANCES = _descriptor.Descriptor(
  name='Affordances',
  full_name='Affordances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aff', full_name='Affordances.aff', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=233,
  serialized_end=259,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='Response.ok', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='landmarks', full_name='Response.landmarks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='affs', full_name='Response.affs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=261,
  serialized_end=341,
)

_COMMAND.fields_by_name['type'].enum_type = _COMMAND_COMMANDTYPE
_COMMAND_COMMANDTYPE.containing_type = _COMMAND;
_RESPONSE.fields_by_name['landmarks'].message_type = _LANDMARK
_RESPONSE.fields_by_name['affs'].message_type = _AFFORDANCES
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Landmark'] = _LANDMARK
DESCRIPTOR.message_types_by_name['Affordances'] = _AFFORDANCES
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

class Command(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMAND

  # @@protoc_insertion_point(class_scope:Command)

class Landmark(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LANDMARK

  # @@protoc_insertion_point(class_scope:Landmark)

class Affordances(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AFFORDANCES

  # @@protoc_insertion_point(class_scope:Affordances)

class Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE

  # @@protoc_insertion_point(class_scope:Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\027edu.usf.ratsim.protobuf')
# @@protoc_insertion_point(module_scope)
