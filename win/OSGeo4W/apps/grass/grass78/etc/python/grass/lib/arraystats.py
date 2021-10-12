'''Wrapper for arraystats.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_arraystats.7.8 D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/arraystats.h D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h -o OBJ.x86_64-w64-mingw32/arraystats.py

Do not modify this file.
'''

__docformat__ = 'restructuredtext'


_libs = {}
_libdirs = []

from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function
from .ctypes_loader import *

add_library_search_dirs([])

# Begin libraries

_libs["grass_arraystats.7.8"] = load_library("grass_arraystats.7.8")

# 1 libraries
# End libraries

# No modules

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 532
class struct_Option(Structure):
    pass

struct_Option.__slots__ = [
    'key',
    'type',
    'required',
    'multiple',
    'options',
    'opts',
    'key_desc',
    'label',
    'description',
    'descriptions',
    'descs',
    'answer',
    '_def',
    'answers',
    'next_opt',
    'gisprompt',
    'guisection',
    'guidependency',
    'checker',
    'count',
]
struct_Option._fields_ = [
    ('key', String),
    ('type', c_int),
    ('required', c_int),
    ('multiple', c_int),
    ('options', String),
    ('opts', POINTER(POINTER(c_char))),
    ('key_desc', String),
    ('label', String),
    ('description', String),
    ('descriptions', String),
    ('descs', POINTER(POINTER(c_char))),
    ('answer', String),
    ('_def', String),
    ('answers', POINTER(POINTER(c_char))),
    ('next_opt', POINTER(struct_Option)),
    ('gisprompt', String),
    ('guisection', String),
    ('guidependency', String),
    ('checker', CFUNCTYPE(UNCHECKED(c_int), String)),
    ('count', c_int),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 11
class struct_GASTATS(Structure):
    pass

struct_GASTATS.__slots__ = [
    'count',
    'min',
    'max',
    'sum',
    'sumsq',
    'sumabs',
    'mean',
    'meanabs',
    'var',
    'stdev',
]
struct_GASTATS._fields_ = [
    ('count', c_double),
    ('min', c_double),
    ('max', c_double),
    ('sum', c_double),
    ('sumsq', c_double),
    ('sumabs', c_double),
    ('mean', c_double),
    ('meanabs', c_double),
    ('var', c_double),
    ('stdev', c_double),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_eqdrt'):
        continue
    AS_eqdrt = _lib.AS_eqdrt
    AS_eqdrt.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_eqdrt.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_basic_stats'):
        continue
    AS_basic_stats = _lib.AS_basic_stats
    AS_basic_stats.argtypes = [POINTER(c_double), c_int, POINTER(struct_GASTATS)]
    AS_basic_stats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_option_to_algorithm'):
        continue
    AS_option_to_algorithm = _lib.AS_option_to_algorithm
    AS_option_to_algorithm.argtypes = [POINTER(struct_Option)]
    AS_option_to_algorithm.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_class_apply_algorithm'):
        continue
    AS_class_apply_algorithm = _lib.AS_class_apply_algorithm
    AS_class_apply_algorithm.argtypes = [c_int, POINTER(c_double), c_int, POINTER(c_int), POINTER(c_double)]
    AS_class_apply_algorithm.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_class_interval'):
        continue
    AS_class_interval = _lib.AS_class_interval
    AS_class_interval.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_interval.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_class_quant'):
        continue
    AS_class_quant = _lib.AS_class_quant
    AS_class_quant.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_quant.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_class_discont'):
        continue
    AS_class_discont = _lib.AS_class_discont
    AS_class_discont.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_discont.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_class_stdev'):
        continue
    AS_class_stdev = _lib.AS_class_stdev
    AS_class_stdev.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_stdev.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_class_equiprob'):
        continue
    AS_class_equiprob = _lib.AS_class_equiprob
    AS_class_equiprob.argtypes = [POINTER(c_double), c_int, POINTER(c_int), POINTER(c_double)]
    AS_class_equiprob.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'AS_class_frequencies'):
        continue
    AS_class_frequencies = _lib.AS_class_frequencies
    AS_class_frequencies.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double), POINTER(c_int)]
    AS_class_frequencies.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 25
try:
    CLASS_INTERVAL = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 26
try:
    CLASS_STDEV = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 27
try:
    CLASS_QUANT = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 28
try:
    CLASS_EQUIPROB = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 29
try:
    CLASS_DISCONT = 5
except:
    pass

GASTATS = struct_GASTATS # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 11

# No inserted files

