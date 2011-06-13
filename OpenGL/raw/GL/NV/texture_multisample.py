'''OpenGL extension NV.texture_multisample

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_texture_multisample'
_DEPRECATED = False
GL_TEXTURE_COVERAGE_SAMPLES_NV = constant.Constant( 'GL_TEXTURE_COVERAGE_SAMPLES_NV', 0x9045 )
GL_TEXTURE_COLOR_SAMPLES_NV = constant.Constant( 'GL_TEXTURE_COLOR_SAMPLES_NV', 0x9046 )
glTexImage2DMultisampleCoverageNV = platform.createExtensionFunction( 
'glTexImage2DMultisampleCoverageNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLsizei,constants.GLint,constants.GLsizei,constants.GLsizei,constants.GLboolean,),
doc='glTexImage2DMultisampleCoverageNV(GLenum(target), GLsizei(coverageSamples), GLsizei(colorSamples), GLint(internalFormat), GLsizei(width), GLsizei(height), GLboolean(fixedSampleLocations)) -> None',
argNames=('target','coverageSamples','colorSamples','internalFormat','width','height','fixedSampleLocations',),
deprecated=_DEPRECATED,
)

glTexImage3DMultisampleCoverageNV = platform.createExtensionFunction( 
'glTexImage3DMultisampleCoverageNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLsizei,constants.GLint,constants.GLsizei,constants.GLsizei,constants.GLsizei,constants.GLboolean,),
doc='glTexImage3DMultisampleCoverageNV(GLenum(target), GLsizei(coverageSamples), GLsizei(colorSamples), GLint(internalFormat), GLsizei(width), GLsizei(height), GLsizei(depth), GLboolean(fixedSampleLocations)) -> None',
argNames=('target','coverageSamples','colorSamples','internalFormat','width','height','depth','fixedSampleLocations',),
deprecated=_DEPRECATED,
)

glTextureImage2DMultisampleNV = platform.createExtensionFunction( 
'glTextureImage2DMultisampleNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLsizei,constants.GLint,constants.GLsizei,constants.GLsizei,constants.GLboolean,),
doc='glTextureImage2DMultisampleNV(GLuint(texture), GLenum(target), GLsizei(samples), GLint(internalFormat), GLsizei(width), GLsizei(height), GLboolean(fixedSampleLocations)) -> None',
argNames=('texture','target','samples','internalFormat','width','height','fixedSampleLocations',),
deprecated=_DEPRECATED,
)

glTextureImage3DMultisampleNV = platform.createExtensionFunction( 
'glTextureImage3DMultisampleNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLsizei,constants.GLint,constants.GLsizei,constants.GLsizei,constants.GLsizei,constants.GLboolean,),
doc='glTextureImage3DMultisampleNV(GLuint(texture), GLenum(target), GLsizei(samples), GLint(internalFormat), GLsizei(width), GLsizei(height), GLsizei(depth), GLboolean(fixedSampleLocations)) -> None',
argNames=('texture','target','samples','internalFormat','width','height','depth','fixedSampleLocations',),
deprecated=_DEPRECATED,
)

glTextureImage2DMultisampleCoverageNV = platform.createExtensionFunction( 
'glTextureImage2DMultisampleCoverageNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLsizei,constants.GLsizei,constants.GLint,constants.GLsizei,constants.GLsizei,constants.GLboolean,),
doc='glTextureImage2DMultisampleCoverageNV(GLuint(texture), GLenum(target), GLsizei(coverageSamples), GLsizei(colorSamples), GLint(internalFormat), GLsizei(width), GLsizei(height), GLboolean(fixedSampleLocations)) -> None',
argNames=('texture','target','coverageSamples','colorSamples','internalFormat','width','height','fixedSampleLocations',),
deprecated=_DEPRECATED,
)

glTextureImage3DMultisampleCoverageNV = platform.createExtensionFunction( 
'glTextureImage3DMultisampleCoverageNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLsizei,constants.GLsizei,constants.GLint,constants.GLsizei,constants.GLsizei,constants.GLsizei,constants.GLboolean,),
doc='glTextureImage3DMultisampleCoverageNV(GLuint(texture), GLenum(target), GLsizei(coverageSamples), GLsizei(colorSamples), GLint(internalFormat), GLsizei(width), GLsizei(height), GLsizei(depth), GLboolean(fixedSampleLocations)) -> None',
argNames=('texture','target','coverageSamples','colorSamples','internalFormat','width','height','depth','fixedSampleLocations',),
deprecated=_DEPRECATED,
)


def glInitTextureMultisampleNV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )