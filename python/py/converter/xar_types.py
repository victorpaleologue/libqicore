#!/usr/bin/env python

## Copyright (c) 2012 Aldebaran Robotics. All rights reserved.
## Use of this source code is governed by a BSD-style license that can be
## found in the COPYING file.

""" Contains types used in the xar format and meaning of some fields
.. module:: converter
"""


class attributes:
    """ Helping class to handle optionnal values
    """

    def __init__(self, attrs):
        self._attrs = attrs

    def getValue(self, name):
        if (name in self._attrs.keys()):
            return self._attrs.getValue(name)
        else:
            return None


class IO:
    """ Used to represent a input or output
    """

    def __init__(self, name, type, type_size, nature, stm_value_name, inner, tooltip, id):
        self.name = name
        self.type = type
        self.type_size = type_size
        self.nature = nature
        self.stm_value_name = stm_value_name
        self.inner = inner
        self.tooltip = tooltip
        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class resource:

    def __init__(self, name, lock_type, timeout):
        self.name = name
        self.lock_type = lock_type
        self.timeout = int(timeout)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class choice:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class tangent:

    def __init__(self, side, interpType, abscissaParam, ordinateParam):
        self.side = side
        self.interpType = interpType
        self.abscissaParam = abscissaParam
        self.ordinateParam = ordinateParam

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class link:

    def __init__(self, emitterID, indexofinput, receiverID, indexofoutput):
        self.emitterID = emitterID
        self.indexofinput = indexofinput
        self.receiverID = receiverID
        self.indexofoutput = indexofoutput
        self.emitterName = ""
        self.signalName = ""
        self.receiverName = ""
        self.slotName = ""

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class IOType:
    DYNAMIC = u"0"
    BANG = u"1"
    NUMBER = u"2"
    STRING = u"3"
    BITMAP = u"4"
    SOUND = u"5"


class InputNature:
    ONLOAD = u"0"
    UNDEF = u"1"
    ONSTART = u"2"
    ONSTOP = u"3"
    STMVALUE = u"4"


class OutputNature:
    UNDEF = u"0"
    STOPPED = u"1"
    PUNCTUAL = u"2"
    RECURRENT = u"3"


class ParameterType:
    BOOL = u"0"
    INT = u"1"
    DOUBLE = u"2"
    STRING = u"3"
    RESOURCE = u"4"


class ResourceMode:
    LOCK = u"Lock"
    STOP_ON_DEMAND = u"Stop on demand"
    PAUSE_ON_DEMAND = u"Pause on demand"
    CALLBACK_ON_DEMAND = u"Callback on demand"


class ScriptLanguage:
    CPLUSPLUS = u"0"
    URBI = u"1"
    RUBY = u"2"
    DYNAMIC_LIBRARY = u"3"
    PYTHON = u"4"
    QICHAT = u"5"
    NO_SCRIPT = u"6"


class ContentType:
    PYTHON_SCRIPT = u"0"
    QICHAT_SCRIPT = u"1"
    FLOW_DIAGRAM = u"2"
    BEHAVIOR_SEQUENCE = u"3"
    ANIMATION = u"4"
