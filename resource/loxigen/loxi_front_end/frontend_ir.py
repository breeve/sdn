# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.

from generic_utils import find
from collections import namedtuple

# This module is represents the frontend IR.
__all__ = [
    'OFInput',
    'OFClass',
    'OFDataMember',
    'OFTypeMember',
    'OFDiscriminatorMember',
    'OFLengthMember',
    'OFFieldLengthMember',
    'OFPadMember',
    'OFVersionMember',
    'OFEnum',
    'OFEnumEntry'
]

"""
One input file

@param wire_versions Set of integer wire versions this file applies to
@param classes List of OFClass objects in the same order as in the file
@param enums List of Enum objects in the same order as in the file
"""
OFInput = namedtuple('OFInput', ['filename', 'wire_versions', 'classes', 'enums'])

"""
An OpenFlow class

All compound objects like messages, actions, instructions, etc are
uniformly represented by this class.

The members are in the same order as on the wire.

@param name
@param superclass name of the super class
@param members List of *Member objects
@param params optional dictionary of parameters
"""
OFClass = namedtuple('OFClass', ['name', 'superclass', 'members', 'virtual', 'params'])

"""
Normal field

@param name
@param oftype C-like type string

Example: packet_in.buffer_id
"""
OFDataMember = namedtuple('OFDataMember', ['name', 'oftype'])

"""
Field that declares that this is an abstract super-class and
that the sub classes will be discriminated based on this field.
E.g., 'type' is the discriminator member of the abstract superclass
of_action.

@param name
"""
OFDiscriminatorMember = namedtuple('OFDiscriminatorMember', ['name', 'oftype'])

"""
Field used to determine the type of an OpenFlow object

@param name
@param oftype C-like type string
@param value Fixed type value

Example: packet_in.type, flow_add._command
"""
OFTypeMember = namedtuple('OFTypeMember', ['name', 'oftype', 'value'])

"""
Field with the length of the containing object

@param name
@param oftype C-like type string

Example: packet_in.length, action_output.len
"""
OFLengthMember = namedtuple('OFLengthMember', ['name', 'oftype'])

"""
Field with the length of another field in the containing object

@param name
@param oftype C-like type string
@param field_name Peer field whose length this field contains

Example: packet_out.actions_len (only usage)
"""
OFFieldLengthMember = namedtuple('OFFieldLengthMember', ['name', 'oftype', 'field_name'])

"""
Zero-filled padding

@param length Length in bytes

Example: packet_in.pad
"""
OFPadMember = namedtuple('OFPadMember', ['length'])

"""
Field with the version of an OpenFlow object

@param name
@param oftype C-like type string

Example: hello.version
"""
OFVersionMember = namedtuple('OFVersionMember', ['name', 'oftype'])

"""
An OpenFlow enumeration

All values are Python ints.

@param name
@param entries List of OFEnumEntry objects in input order
@params dict of optional params. Currently defined:
       - wire_type: the low_level type of the enum values (uint8,...)
"""
OFEnum = namedtuple('OFEnum', ['name', 'entries', 'params'])
OFEnumEntry = namedtuple('OFEnumEntry', ['name', 'value', 'params'])