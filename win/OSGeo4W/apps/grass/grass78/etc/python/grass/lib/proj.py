'''Wrapper for gprojects.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gproj.7.8 -ID:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/gprojects.h D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h -o OBJ.x86_64-w64-mingw32/proj.py

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

_libs["grass_gproj.7.8"] = load_library("grass_gproj.7.8")

# 1 libraries
# End libraries

# No modules

# D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 220
class struct_PJconsts(Structure):
    pass

PJ = struct_PJconsts # D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 221

PJ_WKT2_2015 = 0 # D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 847

PJ_WKT2_2015_SIMPLIFIED = (PJ_WKT2_2015 + 1) # D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 847

PJ_WKT2_2019 = (PJ_WKT2_2015_SIMPLIFIED + 1) # D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 847

PJ_WKT2_2018 = PJ_WKT2_2019 # D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 847

OGRSpatialReferenceH = POINTER(None) # D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/ogr_srs_api.h: 459

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 69
class struct_pj_info(Structure):
    pass

struct_pj_info.__slots__ = [
    'pj',
    'meters',
    'zone',
    'proj',
    '_def',
    'srid',
    'wkt',
]
struct_pj_info._fields_ = [
    ('pj', POINTER(PJ)),
    ('meters', c_double),
    ('zone', c_int),
    ('proj', c_char * 100),
    ('_def', String),
    ('srid', String),
    ('wkt', String),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 84
class struct_gpj_datum(Structure):
    pass

struct_gpj_datum.__slots__ = [
    'name',
    'longname',
    'ellps',
    'dx',
    'dy',
    'dz',
]
struct_gpj_datum._fields_ = [
    ('name', String),
    ('longname', String),
    ('ellps', String),
    ('dx', c_double),
    ('dy', c_double),
    ('dz', c_double),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 91
class struct_gpj_datum_transform_list(Structure):
    pass

struct_gpj_datum_transform_list.__slots__ = [
    'count',
    'params',
    'where_used',
    'comment',
    'next',
]
struct_gpj_datum_transform_list._fields_ = [
    ('count', c_int),
    ('params', String),
    ('where_used', String),
    ('comment', String),
    ('next', POINTER(struct_gpj_datum_transform_list)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 107
class struct_gpj_ellps(Structure):
    pass

struct_gpj_ellps.__slots__ = [
    'name',
    'longname',
    'a',
    'es',
    'rf',
]
struct_gpj_ellps._fields_ = [
    ('name', String),
    ('longname', String),
    ('a', c_double),
    ('es', c_double),
    ('rf', c_double),
]

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_init_transform'):
        continue
    GPJ_init_transform = _lib.GPJ_init_transform
    GPJ_init_transform.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info), POINTER(struct_pj_info)]
    GPJ_init_transform.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_transform'):
        continue
    GPJ_transform = _lib.GPJ_transform
    GPJ_transform.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info), POINTER(struct_pj_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    GPJ_transform.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_transform_array'):
        continue
    GPJ_transform_array = _lib.GPJ_transform_array
    GPJ_transform_array.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info), POINTER(struct_pj_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    GPJ_transform_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'pj_do_proj'):
        continue
    pj_do_proj = _lib.pj_do_proj
    pj_do_proj.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]
    pj_do_proj.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'pj_do_transform'):
        continue
    pj_do_transform = _lib.pj_do_transform
    pj_do_transform.argtypes = [c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]
    pj_do_transform.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 20
class struct_Key_Value(Structure):
    pass

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'pj_get_kv'):
        continue
    pj_get_kv = _lib.pj_get_kv
    pj_get_kv.argtypes = [POINTER(struct_pj_info), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]
    pj_get_kv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'pj_get_string'):
        continue
    pj_get_string = _lib.pj_get_string
    pj_get_string.argtypes = [POINTER(struct_pj_info), String]
    pj_get_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'set_proj_share'):
        continue
    set_proj_share = _lib.set_proj_share
    set_proj_share.argtypes = [String]
    set_proj_share.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 26
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'pj_print_proj_params'):
        continue
    pj_print_proj_params = _lib.pj_print_proj_params
    pj_print_proj_params.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info)]
    pj_print_proj_params.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_grass_to_wkt'):
        continue
    GPJ_grass_to_wkt = _lib.GPJ_grass_to_wkt
    GPJ_grass_to_wkt.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        GPJ_grass_to_wkt.restype = ReturnString
    else:
        GPJ_grass_to_wkt.restype = String
        GPJ_grass_to_wkt.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_grass_to_wkt2'):
        continue
    GPJ_grass_to_wkt2 = _lib.GPJ_grass_to_wkt2
    GPJ_grass_to_wkt2.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value), c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        GPJ_grass_to_wkt2.restype = ReturnString
    else:
        GPJ_grass_to_wkt2.restype = String
        GPJ_grass_to_wkt2.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 32
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_grass_to_osr'):
        continue
    GPJ_grass_to_osr = _lib.GPJ_grass_to_osr
    GPJ_grass_to_osr.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value)]
    GPJ_grass_to_osr.restype = OGRSpatialReferenceH
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_grass_to_osr2'):
        continue
    GPJ_grass_to_osr2 = _lib.GPJ_grass_to_osr2
    GPJ_grass_to_osr2.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]
    GPJ_grass_to_osr2.restype = OGRSpatialReferenceH
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_set_csv_loc'):
        continue
    GPJ_set_csv_loc = _lib.GPJ_set_csv_loc
    GPJ_set_csv_loc.argtypes = [String]
    GPJ_set_csv_loc.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 35
class struct_Cell_head(Structure):
    pass

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 35
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_osr_to_grass'):
        continue
    GPJ_osr_to_grass = _lib.GPJ_osr_to_grass
    GPJ_osr_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), OGRSpatialReferenceH, c_int]
    GPJ_osr_to_grass.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 38
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_wkt_to_grass'):
        continue
    GPJ_wkt_to_grass = _lib.GPJ_wkt_to_grass
    GPJ_wkt_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), String, c_int]
    GPJ_wkt_to_grass.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 42
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_get_datum_by_name'):
        continue
    GPJ_get_datum_by_name = _lib.GPJ_get_datum_by_name
    GPJ_get_datum_by_name.argtypes = [String, POINTER(struct_gpj_datum)]
    GPJ_get_datum_by_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_get_default_datum_params_by_name'):
        continue
    GPJ_get_default_datum_params_by_name = _lib.GPJ_get_default_datum_params_by_name
    GPJ_get_default_datum_params_by_name.argtypes = [String, POINTER(POINTER(c_char))]
    GPJ_get_default_datum_params_by_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 44
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_get_datum_params'):
        continue
    GPJ_get_datum_params = _lib.GPJ_get_datum_params
    GPJ_get_datum_params.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    GPJ_get_datum_params.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 45
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ__get_datum_params'):
        continue
    GPJ__get_datum_params = _lib.GPJ__get_datum_params
    GPJ__get_datum_params.argtypes = [POINTER(struct_Key_Value), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    GPJ__get_datum_params.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_free_datum'):
        continue
    GPJ_free_datum = _lib.GPJ_free_datum
    GPJ_free_datum.argtypes = [POINTER(struct_gpj_datum)]
    GPJ_free_datum.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 47
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_get_datum_transform_by_name'):
        continue
    GPJ_get_datum_transform_by_name = _lib.GPJ_get_datum_transform_by_name
    GPJ_get_datum_transform_by_name.argtypes = [String]
    GPJ_get_datum_transform_by_name.restype = POINTER(struct_gpj_datum_transform_list)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 48
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_free_datum_transform'):
        continue
    GPJ_free_datum_transform = _lib.GPJ_free_datum_transform
    GPJ_free_datum_transform.argtypes = [POINTER(struct_gpj_datum_transform_list)]
    GPJ_free_datum_transform.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_get_ellipsoid_by_name'):
        continue
    GPJ_get_ellipsoid_by_name = _lib.GPJ_get_ellipsoid_by_name
    GPJ_get_ellipsoid_by_name.argtypes = [String, POINTER(struct_gpj_ellps)]
    GPJ_get_ellipsoid_by_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 52
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_get_ellipsoid_params'):
        continue
    GPJ_get_ellipsoid_params = _lib.GPJ_get_ellipsoid_params
    GPJ_get_ellipsoid_params.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    GPJ_get_ellipsoid_params.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ__get_ellipsoid_params'):
        continue
    GPJ__get_ellipsoid_params = _lib.GPJ__get_ellipsoid_params
    GPJ__get_ellipsoid_params.argtypes = [POINTER(struct_Key_Value), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    GPJ__get_ellipsoid_params.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'GPJ_free_ellps'):
        continue
    GPJ_free_ellps = _lib.GPJ_free_ellps
    GPJ_free_ellps.argtypes = [POINTER(struct_gpj_ellps)]
    GPJ_free_ellps.restype = None
    break

# D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 175
try:
    PROJ_VERSION_MAJOR = 8
except:
    pass

# D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 176
try:
    PROJ_VERSION_MINOR = 2
except:
    pass

# D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 177
try:
    PROJ_VERSION_PATCH = 1
except:
    pass

# D:/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include/proj.h: 181
def PROJ_COMPUTE_VERSION(maj, min, patch):
    return (((maj * 10000) + (min * 100)) + patch)

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 24
try:
    RAD_TO_DEG = 57.29577951308232
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 36
try:
    PROJ_VERSION_NUM = (PROJ_COMPUTE_VERSION (PROJ_VERSION_MAJOR, PROJ_VERSION_MINOR, PROJ_VERSION_PATCH))
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 41
try:
    PJ_WKT2_LATEST = PJ_WKT2_2018
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 62
try:
    ELLIPSOIDTABLE = '/etc/proj/ellipse.table'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 63
try:
    DATUMTABLE = '/etc/proj/datum.table'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 64
try:
    DATUMTRANSFORMTABLE = '/etc/proj/datumtransform.table'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 66
try:
    GRIDDIR = '/etc/proj/nad'
except:
    pass

pj_info = struct_pj_info # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 69

gpj_datum = struct_gpj_datum # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 84

gpj_datum_transform_list = struct_gpj_datum_transform_list # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 91

gpj_ellps = struct_gpj_ellps # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 107

Key_Value = struct_Key_Value # D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 20

Cell_head = struct_Cell_head # D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 35

# No inserted files

