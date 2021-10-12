'''Wrapper for raster3d.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_g3d.7.8 D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster3d.h D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h -o OBJ.x86_64-w64-mingw32/raster3d.py

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

_libs["grass_g3d.7.8"] = load_library("grass_g3d.7.8")

# 1 libraries
# End libraries

# No modules

NULL = None # <built-in>

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 413
class struct_Cell_head(Structure):
    pass

struct_Cell_head.__slots__ = [
    'format',
    'compressed',
    'rows',
    'rows3',
    'cols',
    'cols3',
    'depths',
    'proj',
    'zone',
    'ew_res',
    'ew_res3',
    'ns_res',
    'ns_res3',
    'tb_res',
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
]
struct_Cell_head._fields_ = [
    ('format', c_int),
    ('compressed', c_int),
    ('rows', c_int),
    ('rows3', c_int),
    ('cols', c_int),
    ('cols3', c_int),
    ('depths', c_int),
    ('proj', c_int),
    ('zone', c_int),
    ('ew_res', c_double),
    ('ew_res3', c_double),
    ('ns_res', c_double),
    ('ns_res3', c_double),
    ('tb_res', c_double),
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 502
class struct_Key_Value(Structure):
    pass

struct_Key_Value.__slots__ = [
    'nitems',
    'nalloc',
    'key',
    'value',
]
struct_Key_Value._fields_ = [
    ('nitems', c_int),
    ('nalloc', c_int),
    ('key', POINTER(POINTER(c_char))),
    ('value', POINTER(POINTER(c_char))),
]

CELL = c_int # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 603

DCELL = c_double # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 604

grass_int64 = c_int64 # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 612

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 624
class struct__Color_Value_(Structure):
    pass

struct__Color_Value_.__slots__ = [
    'value',
    'red',
    'grn',
    'blu',
]
struct__Color_Value_._fields_ = [
    ('value', DCELL),
    ('red', c_ubyte),
    ('grn', c_ubyte),
    ('blu', c_ubyte),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 632
class struct__Color_Rule_(Structure):
    pass

struct__Color_Rule_.__slots__ = [
    'low',
    'high',
    'next',
    'prev',
]
struct__Color_Rule_._fields_ = [
    ('low', struct__Color_Value_),
    ('high', struct__Color_Value_),
    ('next', POINTER(struct__Color_Rule_)),
    ('prev', POINTER(struct__Color_Rule_)),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 644
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'red',
    'grn',
    'blu',
    'set',
    'nalloc',
    'active',
]
struct_anon_5._fields_ = [
    ('red', POINTER(c_ubyte)),
    ('grn', POINTER(c_ubyte)),
    ('blu', POINTER(c_ubyte)),
    ('set', POINTER(c_ubyte)),
    ('nalloc', c_int),
    ('active', c_int),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 654
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
]
struct_anon_6._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct__Color_Rule_))),
    ('nalloc', c_int),
    ('active', c_int),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 639
class struct__Color_Info_(Structure):
    pass

struct__Color_Info_.__slots__ = [
    'rules',
    'n_rules',
    'lookup',
    'fp_lookup',
    'min',
    'max',
]
struct__Color_Info_._fields_ = [
    ('rules', POINTER(struct__Color_Rule_)),
    ('n_rules', c_int),
    ('lookup', struct_anon_5),
    ('fp_lookup', struct_anon_6),
    ('min', DCELL),
    ('max', DCELL),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 666
class struct_Colors(Structure):
    pass

struct_Colors.__slots__ = [
    'version',
    'shift',
    'invert',
    'is_float',
    'null_set',
    'null_red',
    'null_grn',
    'null_blu',
    'undef_set',
    'undef_red',
    'undef_grn',
    'undef_blu',
    'fixed',
    'modular',
    'cmin',
    'cmax',
    'organizing',
]
struct_Colors._fields_ = [
    ('version', c_int),
    ('shift', DCELL),
    ('invert', c_int),
    ('is_float', c_int),
    ('null_set', c_int),
    ('null_red', c_ubyte),
    ('null_grn', c_ubyte),
    ('null_blu', c_ubyte),
    ('undef_set', c_int),
    ('undef_red', c_ubyte),
    ('undef_grn', c_ubyte),
    ('undef_blu', c_ubyte),
    ('fixed', struct__Color_Info_),
    ('modular', struct__Color_Info_),
    ('cmin', DCELL),
    ('cmax', DCELL),
    ('organizing', c_int),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 76
class struct_Quant_table(Structure):
    pass

struct_Quant_table.__slots__ = [
    'dLow',
    'dHigh',
    'cLow',
    'cHigh',
]
struct_Quant_table._fields_ = [
    ('dLow', DCELL),
    ('dHigh', DCELL),
    ('cLow', CELL),
    ('cHigh', CELL),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 109
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
    'inf_dmin',
    'inf_dmax',
    'inf_min',
    'inf_max',
]
struct_anon_7._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct_Quant_table))),
    ('nalloc', c_int),
    ('active', c_int),
    ('inf_dmin', DCELL),
    ('inf_dmax', DCELL),
    ('inf_min', CELL),
    ('inf_max', CELL),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 84
class struct_Quant(Structure):
    pass

struct_Quant.__slots__ = [
    'truncate_only',
    'round_only',
    'defaultDRuleSet',
    'defaultCRuleSet',
    'infiniteLeftSet',
    'infiniteRightSet',
    'cRangeSet',
    'maxNofRules',
    'nofRules',
    'defaultDMin',
    'defaultDMax',
    'defaultCMin',
    'defaultCMax',
    'infiniteDLeft',
    'infiniteDRight',
    'infiniteCLeft',
    'infiniteCRight',
    'dMin',
    'dMax',
    'cMin',
    'cMax',
    'table',
    'fp_lookup',
]
struct_Quant._fields_ = [
    ('truncate_only', c_int),
    ('round_only', c_int),
    ('defaultDRuleSet', c_int),
    ('defaultCRuleSet', c_int),
    ('infiniteLeftSet', c_int),
    ('infiniteRightSet', c_int),
    ('cRangeSet', c_int),
    ('maxNofRules', c_int),
    ('nofRules', c_int),
    ('defaultDMin', DCELL),
    ('defaultDMax', DCELL),
    ('defaultCMin', CELL),
    ('defaultCMax', CELL),
    ('infiniteDLeft', DCELL),
    ('infiniteDRight', DCELL),
    ('infiniteCLeft', CELL),
    ('infiniteCRight', CELL),
    ('dMin', DCELL),
    ('dMax', DCELL),
    ('cMin', CELL),
    ('cMax', CELL),
    ('table', POINTER(struct_Quant_table)),
    ('fp_lookup', struct_anon_7),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 127
class struct_Categories(Structure):
    pass

struct_Categories.__slots__ = [
    'ncats',
    'num',
    'title',
    'fmt',
    'm1',
    'a1',
    'm2',
    'a2',
    'q',
    'labels',
    'marks',
    'nalloc',
    'last_marked_rule',
]
struct_Categories._fields_ = [
    ('ncats', CELL),
    ('num', CELL),
    ('title', String),
    ('fmt', String),
    ('m1', c_float),
    ('a1', c_float),
    ('m2', c_float),
    ('a2', c_float),
    ('q', struct_Quant),
    ('labels', POINTER(POINTER(c_char))),
    ('marks', POINTER(c_int)),
    ('nalloc', c_int),
    ('last_marked_rule', c_int),
]

HIST_MAPID = 0 # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_TITLE = (HIST_MAPID + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_MAPSET = (HIST_TITLE + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_CREATOR = (HIST_MAPSET + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_MAPTYPE = (HIST_CREATOR + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_DATSRC_1 = (HIST_MAPTYPE + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_DATSRC_2 = (HIST_DATSRC_1 + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_KEYWRD = (HIST_DATSRC_2 + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_NUM_FIELDS = (HIST_KEYWRD + 1) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 180
class struct_History(Structure):
    pass

struct_History.__slots__ = [
    'fields',
    'nlines',
    'lines',
]
struct_History._fields_ = [
    ('fields', POINTER(c_char) * HIST_NUM_FIELDS),
    ('nlines', c_int),
    ('lines', POINTER(POINTER(c_char))),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 218
class struct_R_stats(Structure):
    pass

struct_R_stats.__slots__ = [
    'sum',
    'sumsq',
    'count',
]
struct_R_stats._fields_ = [
    ('sum', DCELL),
    ('sumsq', DCELL),
    ('count', grass_int64),
]

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h: 233
class struct_FPRange(Structure):
    pass

struct_FPRange.__slots__ = [
    'min',
    'max',
    'first_time',
    'rstats',
]
struct_FPRange._fields_ = [
    ('min', DCELL),
    ('max', DCELL),
    ('first_time', c_int),
    ('rstats', struct_R_stats),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 62
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
    'rows',
    'cols',
    'depths',
    'ns_res',
    'ew_res',
    'tb_res',
    'proj',
    'zone',
]
struct_anon_8._fields_ = [
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
    ('rows', c_int),
    ('cols', c_int),
    ('depths', c_int),
    ('ns_res', c_double),
    ('ew_res', c_double),
    ('tb_res', c_double),
    ('proj', c_int),
    ('zone', c_int),
]

RASTER3D_Region = struct_anon_8 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 62

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 72
class struct_RASTER3D_Map(Structure):
    pass

resample_fn = CFUNCTYPE(UNCHECKED(None), POINTER(struct_RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 68

struct_RASTER3D_Map.__slots__ = [
    'version',
    'fileName',
    'tempName',
    'mapset',
    'operation',
    'region',
    'window',
    'resampleFun',
    'unit',
    'vertical_unit',
    'tileX',
    'tileY',
    'tileZ',
    'nx',
    'ny',
    'nz',
    'data_fd',
    'type',
    'precision',
    'compression',
    'useLzw',
    'useRle',
    'useXdr',
    'offset',
    'indexOffset',
    'indexLongNbytes',
    'indexNbytesUsed',
    'fileEndPtr',
    'hasIndex',
    'index',
    'tileLength',
    'typeIntern',
    'data',
    'currentIndex',
    'useCache',
    'cache',
    'cacheFD',
    'cacheFileName',
    'cachePosLast',
    'range',
    'numLengthExtern',
    'numLengthIntern',
    'clipX',
    'clipY',
    'clipZ',
    'tileXY',
    'tileSize',
    'nxy',
    'nTiles',
    'useMask',
]
struct_RASTER3D_Map._fields_ = [
    ('version', c_int),
    ('fileName', String),
    ('tempName', String),
    ('mapset', String),
    ('operation', c_int),
    ('region', RASTER3D_Region),
    ('window', RASTER3D_Region),
    ('resampleFun', POINTER(resample_fn)),
    ('unit', String),
    ('vertical_unit', c_int),
    ('tileX', c_int),
    ('tileY', c_int),
    ('tileZ', c_int),
    ('nx', c_int),
    ('ny', c_int),
    ('nz', c_int),
    ('data_fd', c_int),
    ('type', c_int),
    ('precision', c_int),
    ('compression', c_int),
    ('useLzw', c_int),
    ('useRle', c_int),
    ('useXdr', c_int),
    ('offset', c_int),
    ('indexOffset', c_long),
    ('indexLongNbytes', c_int),
    ('indexNbytesUsed', c_int),
    ('fileEndPtr', c_int),
    ('hasIndex', c_int),
    ('index', POINTER(c_long)),
    ('tileLength', POINTER(c_int)),
    ('typeIntern', c_int),
    ('data', String),
    ('currentIndex', c_int),
    ('useCache', c_int),
    ('cache', POINTER(None)),
    ('cacheFD', c_int),
    ('cacheFileName', String),
    ('cachePosLast', c_long),
    ('range', struct_FPRange),
    ('numLengthExtern', c_int),
    ('numLengthIntern', c_int),
    ('clipX', c_int),
    ('clipY', c_int),
    ('clipZ', c_int),
    ('tileXY', c_int),
    ('tileSize', c_int),
    ('nxy', c_int),
    ('nTiles', c_int),
    ('useMask', c_int),
]

RASTER3D_Map = struct_RASTER3D_Map # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 186

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 221
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'elts',
    'nofElts',
    'eltSize',
    'names',
    'locks',
    'autoLock',
    'nofUnlocked',
    'minUnlocked',
    'next',
    'prev',
    'first',
    'last',
    'eltRemoveFun',
    'eltRemoveFunData',
    'eltLoadFun',
    'eltLoadFunData',
    'hash',
]
struct_anon_9._fields_ = [
    ('elts', String),
    ('nofElts', c_int),
    ('eltSize', c_int),
    ('names', POINTER(c_int)),
    ('locks', String),
    ('autoLock', c_int),
    ('nofUnlocked', c_int),
    ('minUnlocked', c_int),
    ('next', POINTER(c_int)),
    ('prev', POINTER(c_int)),
    ('first', c_int),
    ('last', c_int),
    ('eltRemoveFun', CFUNCTYPE(UNCHECKED(c_int), )),
    ('eltRemoveFunData', POINTER(None)),
    ('eltLoadFun', CFUNCTYPE(UNCHECKED(c_int), )),
    ('eltLoadFunData', POINTER(None)),
    ('hash', POINTER(None)),
]

RASTER3D_cache = struct_anon_9 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 221

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 235
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'nofNames',
    'index',
    'active',
    'lastName',
    'lastIndex',
    'lastIndexActive',
]
struct_anon_10._fields_ = [
    ('nofNames', c_int),
    ('index', POINTER(c_int)),
    ('active', String),
    ('lastName', c_int),
    ('lastIndex', c_int),
    ('lastIndexActive', c_int),
]

Rast3d_cache_hash = struct_anon_10 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 235

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 240
class struct__d_interval(Structure):
    pass

struct__d_interval.__slots__ = [
    'low',
    'high',
    'inf',
    'next',
]
struct__d_interval._fields_ = [
    ('low', c_double),
    ('high', c_double),
    ('inf', c_int),
    ('next', POINTER(struct__d_interval)),
]

d_Interval = struct__d_interval # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 245

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 250
class struct__d_mask(Structure):
    pass

struct__d_mask.__slots__ = [
    'list',
]
struct__d_mask._fields_ = [
    ('list', POINTER(d_Interval)),
]

d_Mask = struct__d_mask # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 250

write_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 254

read_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 255

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 266
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'array',
    'sx',
    'sy',
    'sz',
]
struct_anon_11._fields_ = [
    ('array', POINTER(DCELL)),
    ('sx', c_int),
    ('sy', c_int),
    ('sz', c_int),
]

RASTER3D_Array_double = struct_anon_11 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 266

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_reset'):
        continue
    Rast3d_cache_reset = _lib.Rast3d_cache_reset
    Rast3d_cache_reset.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_reset.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_dispose'):
        continue
    Rast3d_cache_dispose = _lib.Rast3d_cache_dispose
    Rast3d_cache_dispose.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_dispose.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_new'):
        continue
    Rast3d_cache_new = _lib.Rast3d_cache_new
    Rast3d_cache_new.argtypes = [c_int, c_int, c_int, POINTER(write_fn), POINTER(None), POINTER(read_fn), POINTER(None)]
    Rast3d_cache_new.restype = POINTER(c_ubyte)
    Rast3d_cache_new.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_set_remove_fun'):
        continue
    Rast3d_cache_set_remove_fun = _lib.Rast3d_cache_set_remove_fun
    Rast3d_cache_set_remove_fun.argtypes = [POINTER(RASTER3D_cache), POINTER(write_fn), POINTER(None)]
    Rast3d_cache_set_remove_fun.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_set_load_fun'):
        continue
    Rast3d_cache_set_load_fun = _lib.Rast3d_cache_set_load_fun
    Rast3d_cache_set_load_fun.argtypes = [POINTER(RASTER3D_cache), POINTER(read_fn), POINTER(None)]
    Rast3d_cache_set_load_fun.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_new_read'):
        continue
    Rast3d_cache_new_read = _lib.Rast3d_cache_new_read
    Rast3d_cache_new_read.argtypes = [c_int, c_int, c_int, POINTER(read_fn), POINTER(None)]
    Rast3d_cache_new_read.restype = POINTER(c_ubyte)
    Rast3d_cache_new_read.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_lock'):
        continue
    Rast3d_cache_lock = _lib.Rast3d_cache_lock
    Rast3d_cache_lock.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_lock.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_lock_intern'):
        continue
    Rast3d_cache_lock_intern = _lib.Rast3d_cache_lock_intern
    Rast3d_cache_lock_intern.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_lock_intern.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_unlock'):
        continue
    Rast3d_cache_unlock = _lib.Rast3d_cache_unlock
    Rast3d_cache_unlock.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_unlock.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_unlock_all'):
        continue
    Rast3d_cache_unlock_all = _lib.Rast3d_cache_unlock_all
    Rast3d_cache_unlock_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_unlock_all.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_lock_all'):
        continue
    Rast3d_cache_lock_all = _lib.Rast3d_cache_lock_all
    Rast3d_cache_lock_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_lock_all.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_autolock_on'):
        continue
    Rast3d_cache_autolock_on = _lib.Rast3d_cache_autolock_on
    Rast3d_cache_autolock_on.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_autolock_on.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_autolock_off'):
        continue
    Rast3d_cache_autolock_off = _lib.Rast3d_cache_autolock_off
    Rast3d_cache_autolock_off.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_autolock_off.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_set_min_unlock'):
        continue
    Rast3d_cache_set_min_unlock = _lib.Rast3d_cache_set_min_unlock
    Rast3d_cache_set_min_unlock.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_set_min_unlock.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 19
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_remove_elt'):
        continue
    Rast3d_cache_remove_elt = _lib.Rast3d_cache_remove_elt
    Rast3d_cache_remove_elt.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_remove_elt.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_flush'):
        continue
    Rast3d_cache_flush = _lib.Rast3d_cache_flush
    Rast3d_cache_flush.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_flush.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_remove_all'):
        continue
    Rast3d_cache_remove_all = _lib.Rast3d_cache_remove_all
    Rast3d_cache_remove_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_remove_all.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_flush_all'):
        continue
    Rast3d_cache_flush_all = _lib.Rast3d_cache_flush_all
    Rast3d_cache_flush_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_flush_all.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_elt_ptr'):
        continue
    Rast3d_cache_elt_ptr = _lib.Rast3d_cache_elt_ptr
    Rast3d_cache_elt_ptr.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_elt_ptr.restype = POINTER(c_ubyte)
    Rast3d_cache_elt_ptr.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_load'):
        continue
    Rast3d_cache_load = _lib.Rast3d_cache_load
    Rast3d_cache_load.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_load.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_get_elt'):
        continue
    Rast3d_cache_get_elt = _lib.Rast3d_cache_get_elt
    Rast3d_cache_get_elt.argtypes = [POINTER(RASTER3D_cache), c_int, POINTER(None)]
    Rast3d_cache_get_elt.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 26
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_put_elt'):
        continue
    Rast3d_cache_put_elt = _lib.Rast3d_cache_put_elt
    Rast3d_cache_put_elt.argtypes = [POINTER(RASTER3D_cache), c_int, POINTER(None)]
    Rast3d_cache_put_elt.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_hash_reset'):
        continue
    Rast3d_cache_hash_reset = _lib.Rast3d_cache_hash_reset
    Rast3d_cache_hash_reset.argtypes = [POINTER(Rast3d_cache_hash)]
    Rast3d_cache_hash_reset.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_hash_dispose'):
        continue
    Rast3d_cache_hash_dispose = _lib.Rast3d_cache_hash_dispose
    Rast3d_cache_hash_dispose.argtypes = [POINTER(Rast3d_cache_hash)]
    Rast3d_cache_hash_dispose.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 31
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_hash_new'):
        continue
    Rast3d_cache_hash_new = _lib.Rast3d_cache_hash_new
    Rast3d_cache_hash_new.argtypes = [c_int]
    Rast3d_cache_hash_new.restype = POINTER(c_ubyte)
    Rast3d_cache_hash_new.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 32
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_hash_remove_name'):
        continue
    Rast3d_cache_hash_remove_name = _lib.Rast3d_cache_hash_remove_name
    Rast3d_cache_hash_remove_name.argtypes = [POINTER(Rast3d_cache_hash), c_int]
    Rast3d_cache_hash_remove_name.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_hash_load_name'):
        continue
    Rast3d_cache_hash_load_name = _lib.Rast3d_cache_hash_load_name
    Rast3d_cache_hash_load_name.argtypes = [POINTER(Rast3d_cache_hash), c_int, c_int]
    Rast3d_cache_hash_load_name.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_hash_name2index'):
        continue
    Rast3d_cache_hash_name2index = _lib.Rast3d_cache_hash_name2index
    Rast3d_cache_hash_name2index.argtypes = [POINTER(Rast3d_cache_hash), c_int]
    Rast3d_cache_hash_name2index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 37
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_change_precision'):
        continue
    Rast3d_change_precision = _lib.Rast3d_change_precision
    Rast3d_change_precision.argtypes = [POINTER(None), c_int, String]
    Rast3d_change_precision.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 40
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_change_type'):
        continue
    Rast3d_change_type = _lib.Rast3d_change_type
    Rast3d_change_type.argtypes = [POINTER(None), String]
    Rast3d_change_type.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_compare_files'):
        continue
    Rast3d_compare_files = _lib.Rast3d_compare_files
    Rast3d_compare_files.argtypes = [String, String, String, String]
    Rast3d_compare_files.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_filename'):
        continue
    Rast3d_filename = _lib.Rast3d_filename
    Rast3d_filename.argtypes = [String, String, String, String]
    Rast3d_filename.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 49
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_fpcompress_print_binary'):
        continue
    Rast3d_fpcompress_print_binary = _lib.Rast3d_fpcompress_print_binary
    Rast3d_fpcompress_print_binary.argtypes = [String, c_int]
    Rast3d_fpcompress_print_binary.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 50
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_fpcompress_dissect_xdr_double'):
        continue
    Rast3d_fpcompress_dissect_xdr_double = _lib.Rast3d_fpcompress_dissect_xdr_double
    Rast3d_fpcompress_dissect_xdr_double.argtypes = [POINTER(c_ubyte)]
    Rast3d_fpcompress_dissect_xdr_double.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_fpcompress_write_xdr_nums'):
        continue
    Rast3d_fpcompress_write_xdr_nums = _lib.Rast3d_fpcompress_write_xdr_nums
    Rast3d_fpcompress_write_xdr_nums.argtypes = [c_int, String, c_int, c_int, String, c_int]
    Rast3d_fpcompress_write_xdr_nums.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 52
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_fpcompress_read_xdr_nums'):
        continue
    Rast3d_fpcompress_read_xdr_nums = _lib.Rast3d_fpcompress_read_xdr_nums
    Rast3d_fpcompress_read_xdr_nums.argtypes = [c_int, String, c_int, c_int, c_int, String, c_int]
    Rast3d_fpcompress_read_xdr_nums.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_malloc'):
        continue
    Rast3d_malloc = _lib.Rast3d_malloc
    Rast3d_malloc.argtypes = [c_int]
    Rast3d_malloc.restype = POINTER(c_ubyte)
    Rast3d_malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 56
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_realloc'):
        continue
    Rast3d_realloc = _lib.Rast3d_realloc
    Rast3d_realloc.argtypes = [POINTER(None), c_int]
    Rast3d_realloc.restype = POINTER(c_ubyte)
    Rast3d_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_free'):
        continue
    Rast3d_free = _lib.Rast3d_free
    Rast3d_free.argtypes = [POINTER(None)]
    Rast3d_free.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 60
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_init_cache'):
        continue
    Rast3d_init_cache = _lib.Rast3d_init_cache
    Rast3d_init_cache.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_cache.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_dispose_cache'):
        continue
    Rast3d_dispose_cache = _lib.Rast3d_dispose_cache
    Rast3d_dispose_cache.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_dispose_cache.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 62
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_flush_all_tiles'):
        continue
    Rast3d_flush_all_tiles = _lib.Rast3d_flush_all_tiles
    Rast3d_flush_all_tiles.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_flush_all_tiles.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_cats'):
        continue
    Rast3d_write_cats = _lib.Rast3d_write_cats
    Rast3d_write_cats.argtypes = [String, POINTER(struct_Categories)]
    Rast3d_write_cats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_cats'):
        continue
    Rast3d_read_cats = _lib.Rast3d_read_cats
    Rast3d_read_cats.argtypes = [String, String, POINTER(struct_Categories)]
    Rast3d_read_cats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 69
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_close'):
        continue
    Rast3d_close = _lib.Rast3d_close
    Rast3d_close.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_close.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_remove_color'):
        continue
    Rast3d_remove_color = _lib.Rast3d_remove_color
    Rast3d_remove_color.argtypes = [String]
    Rast3d_remove_color.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 73
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_colors'):
        continue
    Rast3d_read_colors = _lib.Rast3d_read_colors
    Rast3d_read_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Rast3d_read_colors.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 74
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_colors'):
        continue
    Rast3d_write_colors = _lib.Rast3d_write_colors
    Rast3d_write_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Rast3d_write_colors.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 77
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_compression_mode'):
        continue
    Rast3d_set_compression_mode = _lib.Rast3d_set_compression_mode
    Rast3d_set_compression_mode.argtypes = [c_int, c_int]
    Rast3d_set_compression_mode.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 78
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_compression_mode'):
        continue
    Rast3d_get_compression_mode = _lib.Rast3d_get_compression_mode
    Rast3d_get_compression_mode.argtypes = [POINTER(c_int), POINTER(c_int)]
    Rast3d_get_compression_mode.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 79
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_cache_size'):
        continue
    Rast3d_set_cache_size = _lib.Rast3d_set_cache_size
    Rast3d_set_cache_size.argtypes = [c_int]
    Rast3d_set_cache_size.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 80
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_cache_size'):
        continue
    Rast3d_get_cache_size = _lib.Rast3d_get_cache_size
    Rast3d_get_cache_size.argtypes = []
    Rast3d_get_cache_size.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_cache_limit'):
        continue
    Rast3d_set_cache_limit = _lib.Rast3d_set_cache_limit
    Rast3d_set_cache_limit.argtypes = [c_int]
    Rast3d_set_cache_limit.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 82
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_cache_limit'):
        continue
    Rast3d_get_cache_limit = _lib.Rast3d_get_cache_limit
    Rast3d_get_cache_limit.argtypes = []
    Rast3d_get_cache_limit.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 83
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_file_type'):
        continue
    Rast3d_set_file_type = _lib.Rast3d_set_file_type
    Rast3d_set_file_type.argtypes = [c_int]
    Rast3d_set_file_type.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_file_type'):
        continue
    Rast3d_get_file_type = _lib.Rast3d_get_file_type
    Rast3d_get_file_type.argtypes = []
    Rast3d_get_file_type.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_tile_dimension'):
        continue
    Rast3d_set_tile_dimension = _lib.Rast3d_set_tile_dimension
    Rast3d_set_tile_dimension.argtypes = [c_int, c_int, c_int]
    Rast3d_set_tile_dimension.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_tile_dimension'):
        continue
    Rast3d_get_tile_dimension = _lib.Rast3d_get_tile_dimension
    Rast3d_get_tile_dimension.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_tile_dimension.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_error_fun'):
        continue
    Rast3d_set_error_fun = _lib.Rast3d_set_error_fun
    Rast3d_set_error_fun.argtypes = [CFUNCTYPE(UNCHECKED(None), String)]
    Rast3d_set_error_fun.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 88
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_init_defaults'):
        continue
    Rast3d_init_defaults = _lib.Rast3d_init_defaults
    Rast3d_init_defaults.argtypes = []
    Rast3d_init_defaults.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 91
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_doubles'):
        continue
    Rast3d_write_doubles = _lib.Rast3d_write_doubles
    Rast3d_write_doubles.argtypes = [c_int, c_int, POINTER(c_double), c_int]
    Rast3d_write_doubles.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 92
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_doubles'):
        continue
    Rast3d_read_doubles = _lib.Rast3d_read_doubles
    Rast3d_read_doubles.argtypes = [c_int, c_int, POINTER(c_double), c_int]
    Rast3d_read_doubles.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 95
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_skip_error'):
        continue
    Rast3d_skip_error = _lib.Rast3d_skip_error
    Rast3d_skip_error.argtypes = [String]
    Rast3d_skip_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_print_error'):
        continue
    Rast3d_print_error = _lib.Rast3d_print_error
    Rast3d_print_error.argtypes = [String]
    Rast3d_print_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 97
for _lib in _libs.values():
    if hasattr(_lib, 'Rast3d_fatal_error'):
        _func = _lib.Rast3d_fatal_error
        _restype = None
        _errcheck = None
        _argtypes = [String]
        Rast3d_fatal_error = _variadic_function(_func,_restype,_argtypes,_errcheck)

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 99
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_fatal_error_noargs'):
        continue
    Rast3d_fatal_error_noargs = _lib.Rast3d_fatal_error_noargs
    Rast3d_fatal_error_noargs.argtypes = [String]
    Rast3d_fatal_error_noargs.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 100
for _lib in _libs.values():
    if hasattr(_lib, 'Rast3d_error'):
        _func = _lib.Rast3d_error
        _restype = None
        _errcheck = None
        _argtypes = [String]
        Rast3d_error = _variadic_function(_func,_restype,_argtypes,_errcheck)

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_is_xdr_null_num'):
        continue
    Rast3d_is_xdr_null_num = _lib.Rast3d_is_xdr_null_num
    Rast3d_is_xdr_null_num.argtypes = [POINTER(None), c_int]
    Rast3d_is_xdr_null_num.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 104
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_is_xdr_null_float'):
        continue
    Rast3d_is_xdr_null_float = _lib.Rast3d_is_xdr_null_float
    Rast3d_is_xdr_null_float.argtypes = [POINTER(c_float)]
    Rast3d_is_xdr_null_float.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 105
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_is_xdr_null_double'):
        continue
    Rast3d_is_xdr_null_double = _lib.Rast3d_is_xdr_null_double
    Rast3d_is_xdr_null_double.argtypes = [POINTER(c_double)]
    Rast3d_is_xdr_null_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 106
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_xdr_null_num'):
        continue
    Rast3d_set_xdr_null_num = _lib.Rast3d_set_xdr_null_num
    Rast3d_set_xdr_null_num.argtypes = [POINTER(None), c_int]
    Rast3d_set_xdr_null_num.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 107
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_xdr_null_double'):
        continue
    Rast3d_set_xdr_null_double = _lib.Rast3d_set_xdr_null_double
    Rast3d_set_xdr_null_double.argtypes = [POINTER(c_double)]
    Rast3d_set_xdr_null_double.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 108
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_xdr_null_float'):
        continue
    Rast3d_set_xdr_null_float = _lib.Rast3d_set_xdr_null_float
    Rast3d_set_xdr_null_float.argtypes = [POINTER(c_float)]
    Rast3d_set_xdr_null_float.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 109
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_init_fp_xdr'):
        continue
    Rast3d_init_fp_xdr = _lib.Rast3d_init_fp_xdr
    Rast3d_init_fp_xdr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_fp_xdr.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 110
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_init_copy_to_xdr'):
        continue
    Rast3d_init_copy_to_xdr = _lib.Rast3d_init_copy_to_xdr
    Rast3d_init_copy_to_xdr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_copy_to_xdr.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 111
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_copy_to_xdr'):
        continue
    Rast3d_copy_to_xdr = _lib.Rast3d_copy_to_xdr
    Rast3d_copy_to_xdr.argtypes = [POINTER(None), c_int]
    Rast3d_copy_to_xdr.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 112
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_init_copy_from_xdr'):
        continue
    Rast3d_init_copy_from_xdr = _lib.Rast3d_init_copy_from_xdr
    Rast3d_init_copy_from_xdr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_copy_from_xdr.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 113
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_copy_from_xdr'):
        continue
    Rast3d_copy_from_xdr = _lib.Rast3d_copy_from_xdr
    Rast3d_copy_from_xdr.argtypes = [c_int, POINTER(None)]
    Rast3d_copy_from_xdr.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 116
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_gradient_double'):
        continue
    Rast3d_gradient_double = _lib.Rast3d_gradient_double
    Rast3d_gradient_double.argtypes = [POINTER(RASTER3D_Array_double), POINTER(c_double), POINTER(RASTER3D_Array_double), POINTER(RASTER3D_Array_double), POINTER(RASTER3D_Array_double)]
    Rast3d_gradient_double.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 121
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_history'):
        continue
    Rast3d_write_history = _lib.Rast3d_write_history
    Rast3d_write_history.argtypes = [String, POINTER(struct_History)]
    Rast3d_write_history.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 122
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_history'):
        continue
    Rast3d_read_history = _lib.Rast3d_read_history
    Rast3d_read_history.argtypes = [String, String, POINTER(struct_History)]
    Rast3d_read_history.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 125
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_ints'):
        continue
    Rast3d_write_ints = _lib.Rast3d_write_ints
    Rast3d_write_ints.argtypes = [c_int, c_int, POINTER(c_int), c_int]
    Rast3d_write_ints.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 126
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_ints'):
        continue
    Rast3d_read_ints = _lib.Rast3d_read_ints
    Rast3d_read_ints.argtypes = [c_int, c_int, POINTER(c_int), c_int]
    Rast3d_read_ints.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 129
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_get_int'):
        continue
    Rast3d_key_get_int = _lib.Rast3d_key_get_int
    Rast3d_key_get_int.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_int)]
    Rast3d_key_get_int.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 130
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_get_double'):
        continue
    Rast3d_key_get_double = _lib.Rast3d_key_get_double
    Rast3d_key_get_double.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_double)]
    Rast3d_key_get_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 131
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_get_string'):
        continue
    Rast3d_key_get_string = _lib.Rast3d_key_get_string
    Rast3d_key_get_string.argtypes = [POINTER(struct_Key_Value), String, POINTER(POINTER(c_char))]
    Rast3d_key_get_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 132
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_get_value'):
        continue
    Rast3d_key_get_value = _lib.Rast3d_key_get_value
    Rast3d_key_get_value.argtypes = [POINTER(struct_Key_Value), String, String, String, c_int, c_int, POINTER(c_int)]
    Rast3d_key_get_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 134
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_set_int'):
        continue
    Rast3d_key_set_int = _lib.Rast3d_key_set_int
    Rast3d_key_set_int.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_int)]
    Rast3d_key_set_int.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 135
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_set_double'):
        continue
    Rast3d_key_set_double = _lib.Rast3d_key_set_double
    Rast3d_key_set_double.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_double)]
    Rast3d_key_set_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 136
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_set_string'):
        continue
    Rast3d_key_set_string = _lib.Rast3d_key_set_string
    Rast3d_key_set_string.argtypes = [POINTER(struct_Key_Value), String, POINTER(POINTER(c_char))]
    Rast3d_key_set_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 137
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_key_set_value'):
        continue
    Rast3d_key_set_value = _lib.Rast3d_key_set_value
    Rast3d_key_set_value.argtypes = [POINTER(struct_Key_Value), String, String, String, c_int, c_int, POINTER(c_int)]
    Rast3d_key_set_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 140
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_long_encode'):
        continue
    Rast3d_long_encode = _lib.Rast3d_long_encode
    Rast3d_long_encode.argtypes = [POINTER(c_long), POINTER(c_ubyte), c_int]
    Rast3d_long_encode.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 141
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_long_decode'):
        continue
    Rast3d_long_decode = _lib.Rast3d_long_decode
    Rast3d_long_decode.argtypes = [POINTER(c_ubyte), POINTER(c_long), c_int, c_int]
    Rast3d_long_decode.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 144
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_make_mapset_map_directory'):
        continue
    Rast3d_make_mapset_map_directory = _lib.Rast3d_make_mapset_map_directory
    Rast3d_make_mapset_map_directory.argtypes = [String]
    Rast3d_make_mapset_map_directory.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 147
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_close'):
        continue
    Rast3d_mask_close = _lib.Rast3d_mask_close
    Rast3d_mask_close.argtypes = []
    Rast3d_mask_close.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 148
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_file_exists'):
        continue
    Rast3d_mask_file_exists = _lib.Rast3d_mask_file_exists
    Rast3d_mask_file_exists.argtypes = []
    Rast3d_mask_file_exists.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 149
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_open_old'):
        continue
    Rast3d_mask_open_old = _lib.Rast3d_mask_open_old
    Rast3d_mask_open_old.argtypes = []
    Rast3d_mask_open_old.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 150
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_reopen'):
        continue
    Rast3d_mask_reopen = _lib.Rast3d_mask_reopen
    Rast3d_mask_reopen.argtypes = [c_int]
    Rast3d_mask_reopen.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 151
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_is_masked'):
        continue
    Rast3d_is_masked = _lib.Rast3d_is_masked
    Rast3d_is_masked.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_is_masked.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 152
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_num'):
        continue
    Rast3d_mask_num = _lib.Rast3d_mask_num
    Rast3d_mask_num.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_mask_num.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 153
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_float'):
        continue
    Rast3d_mask_float = _lib.Rast3d_mask_float
    Rast3d_mask_float.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_float)]
    Rast3d_mask_float.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 154
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_double'):
        continue
    Rast3d_mask_double = _lib.Rast3d_mask_double
    Rast3d_mask_double.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_double)]
    Rast3d_mask_double.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 155
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_tile'):
        continue
    Rast3d_mask_tile = _lib.Rast3d_mask_tile
    Rast3d_mask_tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None), c_int]
    Rast3d_mask_tile.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 156
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_on'):
        continue
    Rast3d_mask_on = _lib.Rast3d_mask_on
    Rast3d_mask_on.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_on.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 157
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_off'):
        continue
    Rast3d_mask_off = _lib.Rast3d_mask_off
    Rast3d_mask_off.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_off.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 158
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_is_on'):
        continue
    Rast3d_mask_is_on = _lib.Rast3d_mask_is_on
    Rast3d_mask_is_on.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_is_on.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 159
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_is_off'):
        continue
    Rast3d_mask_is_off = _lib.Rast3d_mask_is_off
    Rast3d_mask_is_off.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_is_off.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 160
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_file'):
        continue
    Rast3d_mask_file = _lib.Rast3d_mask_file
    Rast3d_mask_file.argtypes = []
    Rast3d_mask_file.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 161
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_map_exists'):
        continue
    Rast3d_mask_map_exists = _lib.Rast3d_mask_map_exists
    Rast3d_mask_map_exists.argtypes = []
    Rast3d_mask_map_exists.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 164
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_d_select'):
        continue
    Rast3d_mask_d_select = _lib.Rast3d_mask_d_select
    Rast3d_mask_d_select.argtypes = [POINTER(DCELL), POINTER(d_Mask)]
    Rast3d_mask_d_select.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 165
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_mask_match_d_interval'):
        continue
    Rast3d_mask_match_d_interval = _lib.Rast3d_mask_match_d_interval
    Rast3d_mask_match_d_interval.argtypes = [DCELL, POINTER(d_Interval)]
    Rast3d_mask_match_d_interval.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 166
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_parse_vallist'):
        continue
    Rast3d_parse_vallist = _lib.Rast3d_parse_vallist
    Rast3d_parse_vallist.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(d_Mask))]
    Rast3d_parse_vallist.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 169
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_g3d_type2cell_type'):
        continue
    Rast3d_g3d_type2cell_type = _lib.Rast3d_g3d_type2cell_type
    Rast3d_g3d_type2cell_type.argtypes = [c_int]
    Rast3d_g3d_type2cell_type.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 170
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_copy_float2Double'):
        continue
    Rast3d_copy_float2Double = _lib.Rast3d_copy_float2Double
    Rast3d_copy_float2Double.argtypes = [POINTER(c_float), c_int, POINTER(c_double), c_int, c_int]
    Rast3d_copy_float2Double.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 171
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_copy_double2Float'):
        continue
    Rast3d_copy_double2Float = _lib.Rast3d_copy_double2Float
    Rast3d_copy_double2Float.argtypes = [POINTER(c_double), c_int, POINTER(c_float), c_int, c_int]
    Rast3d_copy_double2Float.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 172
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_copy_values'):
        continue
    Rast3d_copy_values = _lib.Rast3d_copy_values
    Rast3d_copy_values.argtypes = [POINTER(None), c_int, c_int, POINTER(None), c_int, c_int, c_int]
    Rast3d_copy_values.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 173
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_length'):
        continue
    Rast3d_length = _lib.Rast3d_length
    Rast3d_length.argtypes = [c_int]
    Rast3d_length.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 174
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_extern_length'):
        continue
    Rast3d_extern_length = _lib.Rast3d_extern_length
    Rast3d_extern_length.argtypes = [c_int]
    Rast3d_extern_length.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 177
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_is_null_value_num'):
        continue
    Rast3d_is_null_value_num = _lib.Rast3d_is_null_value_num
    Rast3d_is_null_value_num.argtypes = [POINTER(None), c_int]
    Rast3d_is_null_value_num.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 178
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_null_value'):
        continue
    Rast3d_set_null_value = _lib.Rast3d_set_null_value
    Rast3d_set_null_value.argtypes = [POINTER(None), c_int, c_int]
    Rast3d_set_null_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 181
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_open_new_param'):
        continue
    Rast3d_open_new_param = _lib.Rast3d_open_new_param
    Rast3d_open_new_param.argtypes = [String, c_int, c_int, POINTER(RASTER3D_Region), c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_open_new_param.restype = POINTER(c_ubyte)
    Rast3d_open_new_param.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 183
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_open_cell_old_no_header'):
        continue
    Rast3d_open_cell_old_no_header = _lib.Rast3d_open_cell_old_no_header
    Rast3d_open_cell_old_no_header.argtypes = [String, String]
    Rast3d_open_cell_old_no_header.restype = POINTER(c_ubyte)
    Rast3d_open_cell_old_no_header.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 184
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_open_cell_old'):
        continue
    Rast3d_open_cell_old = _lib.Rast3d_open_cell_old
    Rast3d_open_cell_old.argtypes = [String, String, POINTER(RASTER3D_Region), c_int, c_int]
    Rast3d_open_cell_old.restype = POINTER(c_ubyte)
    Rast3d_open_cell_old.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 185
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_open_cell_new'):
        continue
    Rast3d_open_cell_new = _lib.Rast3d_open_cell_new
    Rast3d_open_cell_new.argtypes = [String, c_int, c_int, POINTER(RASTER3D_Region)]
    Rast3d_open_cell_new.restype = POINTER(c_ubyte)
    Rast3d_open_cell_new.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 186
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_open_new_opt_tile_size'):
        continue
    Rast3d_open_new_opt_tile_size = _lib.Rast3d_open_new_opt_tile_size
    Rast3d_open_new_opt_tile_size.argtypes = [String, c_int, POINTER(RASTER3D_Region), c_int, c_int]
    Rast3d_open_new_opt_tile_size.restype = POINTER(c_ubyte)
    Rast3d_open_new_opt_tile_size.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 189
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_standard3d_input_params'):
        continue
    Rast3d_set_standard3d_input_params = _lib.Rast3d_set_standard3d_input_params
    Rast3d_set_standard3d_input_params.argtypes = []
    Rast3d_set_standard3d_input_params.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 190
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_standard3d_params'):
        continue
    Rast3d_get_standard3d_params = _lib.Rast3d_get_standard3d_params
    Rast3d_get_standard3d_params.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_standard3d_params.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 192
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_window_params'):
        continue
    Rast3d_set_window_params = _lib.Rast3d_set_window_params
    Rast3d_set_window_params.argtypes = []
    Rast3d_set_window_params.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 193
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_window_params'):
        continue
    Rast3d_get_window_params = _lib.Rast3d_get_window_params
    Rast3d_get_window_params.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        Rast3d_get_window_params.restype = ReturnString
    else:
        Rast3d_get_window_params.restype = String
        Rast3d_get_window_params.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 196
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_range_update_from_tile'):
        continue
    Rast3d_range_update_from_tile = _lib.Rast3d_range_update_from_tile
    Rast3d_range_update_from_tile.argtypes = [POINTER(RASTER3D_Map), POINTER(None), c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_range_update_from_tile.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 198
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_range'):
        continue
    Rast3d_read_range = _lib.Rast3d_read_range
    Rast3d_read_range.argtypes = [String, String, POINTER(struct_FPRange)]
    Rast3d_read_range.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 199
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_range_load'):
        continue
    Rast3d_range_load = _lib.Rast3d_range_load
    Rast3d_range_load.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_range_load.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 200
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_range_min_max'):
        continue
    Rast3d_range_min_max = _lib.Rast3d_range_min_max
    Rast3d_range_min_max.argtypes = [POINTER(RASTER3D_Map), POINTER(c_double), POINTER(c_double)]
    Rast3d_range_min_max.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 201
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_range_write'):
        continue
    Rast3d_range_write = _lib.Rast3d_range_write
    Rast3d_range_write.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_range_write.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 202
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_range_init'):
        continue
    Rast3d_range_init = _lib.Rast3d_range_init
    Rast3d_range_init.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_range_init.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 205
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_region_value'):
        continue
    Rast3d_get_region_value = _lib.Rast3d_get_region_value
    Rast3d_get_region_value.argtypes = [POINTER(RASTER3D_Map), c_double, c_double, c_double, POINTER(None), c_int]
    Rast3d_get_region_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 206
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_adjust_region'):
        continue
    Rast3d_adjust_region = _lib.Rast3d_adjust_region
    Rast3d_adjust_region.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_adjust_region.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 207
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_region_copy'):
        continue
    Rast3d_region_copy = _lib.Rast3d_region_copy
    Rast3d_region_copy.argtypes = [POINTER(RASTER3D_Region), POINTER(RASTER3D_Region)]
    Rast3d_region_copy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 208
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_incorporate2d_region'):
        continue
    Rast3d_incorporate2d_region = _lib.Rast3d_incorporate2d_region
    Rast3d_incorporate2d_region.argtypes = [POINTER(struct_Cell_head), POINTER(RASTER3D_Region)]
    Rast3d_incorporate2d_region.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 209
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_region_from_to_cell_head'):
        continue
    Rast3d_region_from_to_cell_head = _lib.Rast3d_region_from_to_cell_head
    Rast3d_region_from_to_cell_head.argtypes = [POINTER(struct_Cell_head), POINTER(RASTER3D_Region)]
    Rast3d_region_from_to_cell_head.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 210
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_adjust_region_res'):
        continue
    Rast3d_adjust_region_res = _lib.Rast3d_adjust_region_res
    Rast3d_adjust_region_res.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_adjust_region_res.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 211
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_extract2d_region'):
        continue
    Rast3d_extract2d_region = _lib.Rast3d_extract2d_region
    Rast3d_extract2d_region.argtypes = [POINTER(RASTER3D_Region), POINTER(struct_Cell_head)]
    Rast3d_extract2d_region.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 212
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_region_to_cell_head'):
        continue
    Rast3d_region_to_cell_head = _lib.Rast3d_region_to_cell_head
    Rast3d_region_to_cell_head.argtypes = [POINTER(RASTER3D_Region), POINTER(struct_Cell_head)]
    Rast3d_region_to_cell_head.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 213
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_region_map'):
        continue
    Rast3d_read_region_map = _lib.Rast3d_read_region_map
    Rast3d_read_region_map.argtypes = [String, String, POINTER(RASTER3D_Region)]
    Rast3d_read_region_map.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 214
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_is_valid_location'):
        continue
    Rast3d_is_valid_location = _lib.Rast3d_is_valid_location
    Rast3d_is_valid_location.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double]
    Rast3d_is_valid_location.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 215
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_location2coord'):
        continue
    Rast3d_location2coord = _lib.Rast3d_location2coord
    Rast3d_location2coord.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_location2coord.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 216
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_location2coord_double'):
        continue
    Rast3d_location2coord_double = _lib.Rast3d_location2coord_double
    Rast3d_location2coord_double.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_location2coord_double.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 217
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_location2coord2'):
        continue
    Rast3d_location2coord2 = _lib.Rast3d_location2coord2
    Rast3d_location2coord2.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_location2coord2.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 218
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_coord2location'):
        continue
    Rast3d_coord2location = _lib.Rast3d_coord2location
    Rast3d_coord2location.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_coord2location.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 220
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_nearest_neighbor'):
        continue
    Rast3d_nearest_neighbor = _lib.Rast3d_nearest_neighbor
    Rast3d_nearest_neighbor.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_nearest_neighbor.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 221
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_resampling_fun'):
        continue
    Rast3d_set_resampling_fun = _lib.Rast3d_set_resampling_fun
    Rast3d_set_resampling_fun.argtypes = [POINTER(RASTER3D_Map), CFUNCTYPE(UNCHECKED(None), )]
    Rast3d_set_resampling_fun.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 222
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_resampling_fun'):
        continue
    Rast3d_get_resampling_fun = _lib.Rast3d_get_resampling_fun
    Rast3d_get_resampling_fun.argtypes = [POINTER(RASTER3D_Map), POINTER(CFUNCTYPE(UNCHECKED(None), ))]
    Rast3d_get_resampling_fun.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 223
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_nearest_neighbor_fun_ptr'):
        continue
    Rast3d_get_nearest_neighbor_fun_ptr = _lib.Rast3d_get_nearest_neighbor_fun_ptr
    Rast3d_get_nearest_neighbor_fun_ptr.argtypes = [POINTER(CFUNCTYPE(UNCHECKED(None), ))]
    Rast3d_get_nearest_neighbor_fun_ptr.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 226
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_volume_a'):
        continue
    Rast3d_get_volume_a = _lib.Rast3d_get_volume_a
    Rast3d_get_volume_a.argtypes = [POINTER(None), (((c_double * 3) * 2) * 2) * 2, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_volume_a.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 227
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_volume'):
        continue
    Rast3d_get_volume = _lib.Rast3d_get_volume
    Rast3d_get_volume.argtypes = [POINTER(None), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_volume.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 230
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_aligned_volume'):
        continue
    Rast3d_get_aligned_volume = _lib.Rast3d_get_aligned_volume
    Rast3d_get_aligned_volume.argtypes = [POINTER(None), c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_aligned_volume.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 232
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_make_aligned_volume_file'):
        continue
    Rast3d_make_aligned_volume_file = _lib.Rast3d_make_aligned_volume_file
    Rast3d_make_aligned_volume_file.argtypes = [POINTER(None), String, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int]
    Rast3d_make_aligned_volume_file.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 235
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_value'):
        continue
    Rast3d_get_value = _lib.Rast3d_get_value
    Rast3d_get_value.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 236
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_float'):
        continue
    Rast3d_get_float = _lib.Rast3d_get_float
    Rast3d_get_float.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_float.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 237
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_double'):
        continue
    Rast3d_get_double = _lib.Rast3d_get_double
    Rast3d_get_double.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_double.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 238
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_window_value'):
        continue
    Rast3d_get_window_value = _lib.Rast3d_get_window_value
    Rast3d_get_window_value.argtypes = [POINTER(RASTER3D_Map), c_double, c_double, c_double, POINTER(None), c_int]
    Rast3d_get_window_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 241
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_window_ptr'):
        continue
    Rast3d_window_ptr = _lib.Rast3d_window_ptr
    Rast3d_window_ptr.argtypes = []
    Rast3d_window_ptr.restype = POINTER(RASTER3D_Region)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 242
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_window'):
        continue
    Rast3d_set_window = _lib.Rast3d_set_window
    Rast3d_set_window.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_set_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 243
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_window_map'):
        continue
    Rast3d_set_window_map = _lib.Rast3d_set_window_map
    Rast3d_set_window_map.argtypes = [POINTER(RASTER3D_Map), POINTER(RASTER3D_Region)]
    Rast3d_set_window_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 244
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_window'):
        continue
    Rast3d_get_window = _lib.Rast3d_get_window
    Rast3d_get_window.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_get_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 247
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_use_window_params'):
        continue
    Rast3d_use_window_params = _lib.Rast3d_use_window_params
    Rast3d_use_window_params.argtypes = []
    Rast3d_use_window_params.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 248
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_window'):
        continue
    Rast3d_read_window = _lib.Rast3d_read_window
    Rast3d_read_window.argtypes = [POINTER(RASTER3D_Region), String]
    Rast3d_read_window.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 252
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_block_nocache'):
        continue
    Rast3d_get_block_nocache = _lib.Rast3d_get_block_nocache
    Rast3d_get_block_nocache.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_block_nocache.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 254
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_block'):
        continue
    Rast3d_get_block = _lib.Rast3d_get_block
    Rast3d_get_block.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_block.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 257
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_header'):
        continue
    Rast3d_read_header = _lib.Rast3d_read_header
    Rast3d_read_header.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_char)), POINTER(c_int), POINTER(c_int)]
    Rast3d_read_header.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 261
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_header'):
        continue
    Rast3d_write_header = _lib.Rast3d_write_header
    Rast3d_write_header.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_double, c_double, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, String, c_int, c_int]
    Rast3d_write_header.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 265
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_rewrite_header'):
        continue
    Rast3d_rewrite_header = _lib.Rast3d_rewrite_header
    Rast3d_rewrite_header.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_rewrite_header.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 266
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_cache_size_encode'):
        continue
    Rast3d_cache_size_encode = _lib.Rast3d_cache_size_encode
    Rast3d_cache_size_encode.argtypes = [c_int, c_int]
    Rast3d_cache_size_encode.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 267
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d__compute_cache_size'):
        continue
    Rast3d__compute_cache_size = _lib.Rast3d__compute_cache_size
    Rast3d__compute_cache_size.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d__compute_cache_size.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 268
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_fill_header'):
        continue
    Rast3d_fill_header = _lib.Rast3d_fill_header
    Rast3d_fill_header.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_double, c_double, String, c_int, c_int]
    Rast3d_fill_header.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 273
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_coords_map'):
        continue
    Rast3d_get_coords_map = _lib.Rast3d_get_coords_map
    Rast3d_get_coords_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_coords_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 274
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_coords_map_window'):
        continue
    Rast3d_get_coords_map_window = _lib.Rast3d_get_coords_map_window
    Rast3d_get_coords_map_window.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_coords_map_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 275
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_nof_tiles_map'):
        continue
    Rast3d_get_nof_tiles_map = _lib.Rast3d_get_nof_tiles_map
    Rast3d_get_nof_tiles_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_nof_tiles_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 276
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_region_map'):
        continue
    Rast3d_get_region_map = _lib.Rast3d_get_region_map
    Rast3d_get_region_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_get_region_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 278
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_window_map'):
        continue
    Rast3d_get_window_map = _lib.Rast3d_get_window_map
    Rast3d_get_window_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_get_window_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 280
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_tile_dimensions_map'):
        continue
    Rast3d_get_tile_dimensions_map = _lib.Rast3d_get_tile_dimensions_map
    Rast3d_get_tile_dimensions_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_tile_dimensions_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 281
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_type_map'):
        continue
    Rast3d_tile_type_map = _lib.Rast3d_tile_type_map
    Rast3d_tile_type_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_tile_type_map.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 282
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_file_type_map'):
        continue
    Rast3d_file_type_map = _lib.Rast3d_file_type_map
    Rast3d_file_type_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_file_type_map.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 283
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_precision_map'):
        continue
    Rast3d_tile_precision_map = _lib.Rast3d_tile_precision_map
    Rast3d_tile_precision_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_tile_precision_map.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 284
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_use_cache_map'):
        continue
    Rast3d_tile_use_cache_map = _lib.Rast3d_tile_use_cache_map
    Rast3d_tile_use_cache_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_tile_use_cache_map.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 285
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_print_header'):
        continue
    Rast3d_print_header = _lib.Rast3d_print_header
    Rast3d_print_header.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_print_header.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 286
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_region_struct_map'):
        continue
    Rast3d_get_region_struct_map = _lib.Rast3d_get_region_struct_map
    Rast3d_get_region_struct_map.argtypes = [POINTER(RASTER3D_Map), POINTER(RASTER3D_Region)]
    Rast3d_get_region_struct_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 287
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_unit'):
        continue
    Rast3d_get_unit = _lib.Rast3d_get_unit
    Rast3d_get_unit.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_get_unit.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 288
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_vertical_unit2'):
        continue
    Rast3d_get_vertical_unit2 = _lib.Rast3d_get_vertical_unit2
    Rast3d_get_vertical_unit2.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_get_vertical_unit2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 289
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_vertical_unit'):
        continue
    Rast3d_get_vertical_unit = _lib.Rast3d_get_vertical_unit
    Rast3d_get_vertical_unit.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_get_vertical_unit.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 290
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_unit'):
        continue
    Rast3d_set_unit = _lib.Rast3d_set_unit
    Rast3d_set_unit.argtypes = [POINTER(RASTER3D_Map), String]
    Rast3d_set_unit.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 291
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_vertical_unit'):
        continue
    Rast3d_set_vertical_unit = _lib.Rast3d_set_vertical_unit
    Rast3d_set_vertical_unit.argtypes = [POINTER(RASTER3D_Map), String]
    Rast3d_set_vertical_unit.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 292
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_vertical_unit2'):
        continue
    Rast3d_set_vertical_unit2 = _lib.Rast3d_set_vertical_unit2
    Rast3d_set_vertical_unit2.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_set_vertical_unit2.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 295
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_flush_index'):
        continue
    Rast3d_flush_index = _lib.Rast3d_flush_index
    Rast3d_flush_index.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_flush_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 296
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_init_index'):
        continue
    Rast3d_init_index = _lib.Rast3d_init_index
    Rast3d_init_index.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 299
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_retile'):
        continue
    Rast3d_retile = _lib.Rast3d_retile
    Rast3d_retile.argtypes = [POINTER(None), String, c_int, c_int, c_int]
    Rast3d_retile.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 302
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_rle_count_only'):
        continue
    Rast3d_rle_count_only = _lib.Rast3d_rle_count_only
    Rast3d_rle_count_only.argtypes = [String, c_int, c_int]
    Rast3d_rle_count_only.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 303
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_rle_encode'):
        continue
    Rast3d_rle_encode = _lib.Rast3d_rle_encode
    Rast3d_rle_encode.argtypes = [String, String, c_int, c_int]
    Rast3d_rle_encode.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 304
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_rle_decode'):
        continue
    Rast3d_rle_decode = _lib.Rast3d_rle_decode
    Rast3d_rle_decode.argtypes = [String, String, c_int, c_int, POINTER(c_int), POINTER(c_int)]
    Rast3d_rle_decode.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 307
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_alloc_tiles_type'):
        continue
    Rast3d_alloc_tiles_type = _lib.Rast3d_alloc_tiles_type
    Rast3d_alloc_tiles_type.argtypes = [POINTER(RASTER3D_Map), c_int, c_int]
    Rast3d_alloc_tiles_type.restype = POINTER(c_ubyte)
    Rast3d_alloc_tiles_type.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 308
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_alloc_tiles'):
        continue
    Rast3d_alloc_tiles = _lib.Rast3d_alloc_tiles
    Rast3d_alloc_tiles.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_alloc_tiles.restype = POINTER(c_ubyte)
    Rast3d_alloc_tiles.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 309
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_free_tiles'):
        continue
    Rast3d_free_tiles = _lib.Rast3d_free_tiles
    Rast3d_free_tiles.argtypes = [POINTER(None)]
    Rast3d_free_tiles.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 312
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_tile_ptr'):
        continue
    Rast3d_get_tile_ptr = _lib.Rast3d_get_tile_ptr
    Rast3d_get_tile_ptr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_get_tile_ptr.restype = POINTER(c_ubyte)
    Rast3d_get_tile_ptr.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 313
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_load'):
        continue
    Rast3d_tile_load = _lib.Rast3d_tile_load
    Rast3d_tile_load.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_tile_load.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 314
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d__remove_tile'):
        continue
    Rast3d__remove_tile = _lib.Rast3d__remove_tile
    Rast3d__remove_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d__remove_tile.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 315
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_float_region'):
        continue
    Rast3d_get_float_region = _lib.Rast3d_get_float_region
    Rast3d_get_float_region.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_float_region.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 316
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_double_region'):
        continue
    Rast3d_get_double_region = _lib.Rast3d_get_double_region
    Rast3d_get_double_region.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_double_region.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 317
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_get_value_region'):
        continue
    Rast3d_get_value_region = _lib.Rast3d_get_value_region
    Rast3d_get_value_region.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_value_region.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 320
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_compute_optimal_tile_dimension'):
        continue
    Rast3d_compute_optimal_tile_dimension = _lib.Rast3d_compute_optimal_tile_dimension
    Rast3d_compute_optimal_tile_dimension.argtypes = [POINTER(RASTER3D_Region), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int]
    Rast3d_compute_optimal_tile_dimension.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 321
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_index2tile'):
        continue
    Rast3d_tile_index2tile = _lib.Rast3d_tile_index2tile
    Rast3d_tile_index2tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_tile_index2tile.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 322
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile2tile_index'):
        continue
    Rast3d_tile2tile_index = _lib.Rast3d_tile2tile_index
    Rast3d_tile2tile_index.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_tile2tile_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 323
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_coord_origin'):
        continue
    Rast3d_tile_coord_origin = _lib.Rast3d_tile_coord_origin
    Rast3d_tile_coord_origin.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_tile_coord_origin.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 324
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_index_origin'):
        continue
    Rast3d_tile_index_origin = _lib.Rast3d_tile_index_origin
    Rast3d_tile_index_origin.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_tile_index_origin.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 325
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_coord2tile_coord'):
        continue
    Rast3d_coord2tile_coord = _lib.Rast3d_coord2tile_coord
    Rast3d_coord2tile_coord.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_coord2tile_coord.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 327
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_coord2tile_index'):
        continue
    Rast3d_coord2tile_index = _lib.Rast3d_coord2tile_index
    Rast3d_coord2tile_index.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int)]
    Rast3d_coord2tile_index.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 328
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_coord_in_range'):
        continue
    Rast3d_coord_in_range = _lib.Rast3d_coord_in_range
    Rast3d_coord_in_range.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_coord_in_range.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 329
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_index_in_range'):
        continue
    Rast3d_tile_index_in_range = _lib.Rast3d_tile_index_in_range
    Rast3d_tile_index_in_range.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_tile_index_in_range.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 330
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_tile_in_range'):
        continue
    Rast3d_tile_in_range = _lib.Rast3d_tile_in_range
    Rast3d_tile_in_range.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_tile_in_range.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 331
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_compute_clipped_tile_dimensions'):
        continue
    Rast3d_compute_clipped_tile_dimensions = _lib.Rast3d_compute_clipped_tile_dimensions
    Rast3d_compute_clipped_tile_dimensions.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_compute_clipped_tile_dimensions.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 335
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_null_tile_type'):
        continue
    Rast3d_set_null_tile_type = _lib.Rast3d_set_null_tile_type
    Rast3d_set_null_tile_type.argtypes = [POINTER(RASTER3D_Map), POINTER(None), c_int]
    Rast3d_set_null_tile_type.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 336
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_set_null_tile'):
        continue
    Rast3d_set_null_tile = _lib.Rast3d_set_null_tile
    Rast3d_set_null_tile.argtypes = [POINTER(RASTER3D_Map), POINTER(None)]
    Rast3d_set_null_tile.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 339
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_tile'):
        continue
    Rast3d_read_tile = _lib.Rast3d_read_tile
    Rast3d_read_tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None), c_int]
    Rast3d_read_tile.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 340
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_tile_float'):
        continue
    Rast3d_read_tile_float = _lib.Rast3d_read_tile_float
    Rast3d_read_tile_float.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_read_tile_float.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 341
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_read_tile_double'):
        continue
    Rast3d_read_tile_double = _lib.Rast3d_read_tile_double
    Rast3d_read_tile_double.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_read_tile_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 342
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_lock_tile'):
        continue
    Rast3d_lock_tile = _lib.Rast3d_lock_tile
    Rast3d_lock_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_lock_tile.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 343
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_unlock_tile'):
        continue
    Rast3d_unlock_tile = _lib.Rast3d_unlock_tile
    Rast3d_unlock_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_unlock_tile.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 344
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_unlock_all'):
        continue
    Rast3d_unlock_all = _lib.Rast3d_unlock_all
    Rast3d_unlock_all.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_unlock_all.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 345
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_autolock_on'):
        continue
    Rast3d_autolock_on = _lib.Rast3d_autolock_on
    Rast3d_autolock_on.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_autolock_on.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 346
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_autolock_off'):
        continue
    Rast3d_autolock_off = _lib.Rast3d_autolock_off
    Rast3d_autolock_off.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_autolock_off.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 347
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_min_unlocked'):
        continue
    Rast3d_min_unlocked = _lib.Rast3d_min_unlocked
    Rast3d_min_unlocked.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_min_unlocked.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 348
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_begin_cycle'):
        continue
    Rast3d_begin_cycle = _lib.Rast3d_begin_cycle
    Rast3d_begin_cycle.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_begin_cycle.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 349
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_end_cycle'):
        continue
    Rast3d_end_cycle = _lib.Rast3d_end_cycle
    Rast3d_end_cycle.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_end_cycle.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 352
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_tile'):
        continue
    Rast3d_write_tile = _lib.Rast3d_write_tile
    Rast3d_write_tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None), c_int]
    Rast3d_write_tile.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 353
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_tile_float'):
        continue
    Rast3d_write_tile_float = _lib.Rast3d_write_tile_float
    Rast3d_write_tile_float.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_write_tile_float.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 354
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_tile_double'):
        continue
    Rast3d_write_tile_double = _lib.Rast3d_write_tile_double
    Rast3d_write_tile_double.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_write_tile_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 355
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_flush_tile'):
        continue
    Rast3d_flush_tile = _lib.Rast3d_flush_tile
    Rast3d_flush_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_flush_tile.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 356
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_flush_tile_cube'):
        continue
    Rast3d_flush_tile_cube = _lib.Rast3d_flush_tile_cube
    Rast3d_flush_tile_cube.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_flush_tile_cube.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 357
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_flush_tiles_in_cube'):
        continue
    Rast3d_flush_tiles_in_cube = _lib.Rast3d_flush_tiles_in_cube
    Rast3d_flush_tiles_in_cube.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_flush_tiles_in_cube.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 358
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_put_float'):
        continue
    Rast3d_put_float = _lib.Rast3d_put_float
    Rast3d_put_float.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_float]
    Rast3d_put_float.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 359
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_put_double'):
        continue
    Rast3d_put_double = _lib.Rast3d_put_double
    Rast3d_put_double.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_double]
    Rast3d_put_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 360
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_put_value'):
        continue
    Rast3d_put_value = _lib.Rast3d_put_value
    Rast3d_put_value.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_put_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 363
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast3d_write_ascii'):
        continue
    Rast3d_write_ascii = _lib.Rast3d_write_ascii
    Rast3d_write_ascii.argtypes = [POINTER(None), String]
    Rast3d_write_ascii.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 7
try:
    RASTER3D_MAP_VERSION = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 12
try:
    RASTER3D_TILE_SAME_AS_FILE = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 14
try:
    RASTER3D_NO_COMPRESSION = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 15
try:
    RASTER3D_COMPRESSION = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 17
try:
    RASTER3D_MAX_PRECISION = (-1)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 19
try:
    RASTER3D_NO_CACHE = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 20
try:
    RASTER3D_USE_CACHE_DEFAULT = (-1)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 21
try:
    RASTER3D_USE_CACHE_X = (-2)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 22
try:
    RASTER3D_USE_CACHE_Y = (-3)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 23
try:
    RASTER3D_USE_CACHE_Z = (-4)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 24
try:
    RASTER3D_USE_CACHE_XY = (-5)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 25
try:
    RASTER3D_USE_CACHE_XZ = (-6)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 26
try:
    RASTER3D_USE_CACHE_YZ = (-7)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 27
try:
    RASTER3D_USE_CACHE_XYZ = (-8)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 29
try:
    RASTER3D_DEFAULT_WINDOW = NULL
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 31
try:
    RASTER3D_DIRECTORY = 'grid3'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 32
try:
    RASTER3D_CELL_ELEMENT = 'cell'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 33
try:
    RASTER3D_CATS_ELEMENT = 'cats'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 34
try:
    RASTER3D_RANGE_ELEMENT = 'range'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 35
try:
    RASTER3D_HEADER_ELEMENT = 'cellhd'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 36
try:
    RASTER3D_HISTORY_ELEMENT = 'hist'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 37
try:
    RASTER3D_COLOR_ELEMENT = 'color'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 38
try:
    RASTER3D_COLOR2_DIRECTORY = 'colr2'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 39
try:
    RASTER3D_MASK_MAP = 'RASTER3D_MASK'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 40
try:
    RASTER3D_WINDOW_ELEMENT = 'WIND3'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 41
try:
    RASTER3D_DEFAULT_WINDOW_ELEMENT = 'DEFAULT_WIND3'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 42
try:
    RASTER3D_WINDOW_DATABASE = 'windows3d'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 43
try:
    RASTER3D_PERMANENT_MAPSET = 'PERMANENT'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 268
def RASTER3D_ARRAY_ACCESS(arr, x, y, z):
    return ((arr.contents.array) [((((((arr.contents.sx).value) * ((arr.contents.sy).value)) * z) + (((arr.contents.sx).value) * y)) + x)])

RASTER3D_Map = struct_RASTER3D_Map # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 72

_d_interval = struct__d_interval # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 240

_d_mask = struct__d_mask # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 250

# No inserted files

