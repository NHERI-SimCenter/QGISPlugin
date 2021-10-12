'''Wrapper for segment.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_segment.7.8 D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/segment.h D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h -o OBJ.x86_64-w64-mingw32/segment.py

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

_libs["grass_segment.7.8"] = load_library("grass_segment.7.8")

# 1 libraries
# End libraries

# No modules

off_t = c_int64 # D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/x86_64-w64-mingw32/include/_mingw_off_t.h: 24

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\segment.h: 14
class struct_aq(Structure):
    pass

struct_aq.__slots__ = [
    'cur',
    'younger',
    'older',
]
struct_aq._fields_ = [
    ('cur', c_int),
    ('younger', POINTER(struct_aq)),
    ('older', POINTER(struct_aq)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\segment.h: 45
class struct_scb(Structure):
    pass

struct_scb.__slots__ = [
    'buf',
    'dirty',
    'age',
    'n',
]
struct_scb._fields_ = [
    ('buf', String),
    ('dirty', c_char),
    ('age', POINTER(struct_aq)),
    ('n', c_int),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\segment.h: 63
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'open',
    'nrows',
    'ncols',
    'len',
    'srows',
    'scols',
    'srowscols',
    'size',
    'spr',
    'spill',
    'fast_adrs',
    'scolbits',
    'srowbits',
    'segbits',
    'fast_seek',
    'lenbits',
    'sizebits',
    'address',
    'seek',
    'fname',
    'fd',
    'scb',
    'load_idx',
    'nfreeslots',
    'freeslot',
    'agequeue',
    'youngest',
    'oldest',
    'nseg',
    'cur',
    'offset',
    'cache',
]
struct_anon_7._fields_ = [
    ('open', c_int),
    ('nrows', off_t),
    ('ncols', off_t),
    ('len', c_int),
    ('srows', c_int),
    ('scols', c_int),
    ('srowscols', c_int),
    ('size', c_int),
    ('spr', c_int),
    ('spill', c_int),
    ('fast_adrs', c_int),
    ('scolbits', off_t),
    ('srowbits', off_t),
    ('segbits', off_t),
    ('fast_seek', c_int),
    ('lenbits', c_int),
    ('sizebits', c_int),
    ('address', CFUNCTYPE(UNCHECKED(c_int), )),
    ('seek', CFUNCTYPE(UNCHECKED(c_int), )),
    ('fname', String),
    ('fd', c_int),
    ('scb', POINTER(struct_scb)),
    ('load_idx', POINTER(c_int)),
    ('nfreeslots', c_int),
    ('freeslot', POINTER(c_int)),
    ('agequeue', POINTER(struct_aq)),
    ('youngest', POINTER(struct_aq)),
    ('oldest', POINTER(struct_aq)),
    ('nseg', c_int),
    ('cur', c_int),
    ('offset', c_int),
    ('cache', String),
]

SEGMENT = struct_anon_7 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\segment.h: 63

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 4
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_open'):
        continue
    Segment_open = _lib.Segment_open
    Segment_open.argtypes = [POINTER(SEGMENT), String, off_t, off_t, c_int, c_int, c_int, c_int]
    Segment_open.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_close'):
        continue
    Segment_close = _lib.Segment_close
    Segment_close.argtypes = [POINTER(SEGMENT)]
    Segment_close.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_flush'):
        continue
    Segment_flush = _lib.Segment_flush
    Segment_flush.argtypes = [POINTER(SEGMENT)]
    Segment_flush.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_format'):
        continue
    Segment_format = _lib.Segment_format
    Segment_format.argtypes = [c_int, off_t, off_t, c_int, c_int, c_int]
    Segment_format.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_format_nofill'):
        continue
    Segment_format_nofill = _lib.Segment_format_nofill
    Segment_format_nofill.argtypes = [c_int, off_t, off_t, c_int, c_int, c_int]
    Segment_format_nofill.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_get'):
        continue
    Segment_get = _lib.Segment_get
    Segment_get.argtypes = [POINTER(SEGMENT), POINTER(None), off_t, off_t]
    Segment_get.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_get_row'):
        continue
    Segment_get_row = _lib.Segment_get_row
    Segment_get_row.argtypes = [POINTER(SEGMENT), POINTER(None), off_t]
    Segment_get_row.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_init'):
        continue
    Segment_init = _lib.Segment_init
    Segment_init.argtypes = [POINTER(SEGMENT), c_int, c_int]
    Segment_init.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_put'):
        continue
    Segment_put = _lib.Segment_put
    Segment_put.argtypes = [POINTER(SEGMENT), POINTER(None), off_t, off_t]
    Segment_put.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_put_row'):
        continue
    Segment_put_row = _lib.Segment_put_row
    Segment_put_row.argtypes = [POINTER(SEGMENT), POINTER(None), off_t]
    Segment_put_row.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/segment.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_release'):
        continue
    Segment_release = _lib.Segment_release
    Segment_release.argtypes = [POINTER(SEGMENT)]
    Segment_release.restype = c_int
    break

aq = struct_aq # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\segment.h: 14

scb = struct_scb # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\segment.h: 45

# No inserted files

