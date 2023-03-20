#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from codecs import open
from os import path

try:
    with open(path.join(path.dirname(__file__), 'VERSION'), encoding='utf-8') as infile:
        __version__ = infile.read().strip()
except NameError:
    __version__ = 'unknown'
except IOError as ex:
    __version__ = "unknown (%s)" % ex

from .tail import Tail as Tail
