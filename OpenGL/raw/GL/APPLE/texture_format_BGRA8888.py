'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_APPLE_texture_format_BGRA8888'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_APPLE_texture_format_BGRA8888')
GL_BGRA8_EXT=_C('GL_BGRA8_EXT',0x93A1)
GL_BGRA_EXT=_C('GL_BGRA_EXT',0x80E1)
