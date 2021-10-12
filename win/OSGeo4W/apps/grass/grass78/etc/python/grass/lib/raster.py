'''Wrapper for raster.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_raster.7.8 D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/raster.h D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h -o OBJ.x86_64-w64-mingw32/raster.py

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

_libs["grass_raster.7.8"] = load_library("grass_raster.7.8")

# 1 libraries
# End libraries

# No modules

# D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/x86_64-w64-mingw32/include/stdio.h: 33
class struct__iobuf(Structure):
    pass

struct__iobuf.__slots__ = [
    '_ptr',
    '_cnt',
    '_base',
    '_flag',
    '_file',
    '_charbuf',
    '_bufsiz',
    '_tmpfname',
]
struct__iobuf._fields_ = [
    ('_ptr', String),
    ('_cnt', c_int),
    ('_base', String),
    ('_flag', c_int),
    ('_file', c_int),
    ('_charbuf', c_int),
    ('_bufsiz', c_int),
    ('_tmpfname', String),
]

FILE = struct__iobuf # D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/x86_64-w64-mingw32/include/stdio.h: 47

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

CELL = c_int # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 603

DCELL = c_double # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 604

FCELL = c_float # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 605

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

RASTER_MAP_TYPE = c_int # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 25

INTERP_TYPE = c_int # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 28

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 31
class struct_Reclass(Structure):
    pass

struct_Reclass.__slots__ = [
    'name',
    'mapset',
    'type',
    'num',
    'min',
    'max',
    'table',
]
struct_Reclass._fields_ = [
    ('name', String),
    ('mapset', String),
    ('type', c_int),
    ('num', c_int),
    ('min', CELL),
    ('max', CELL),
    ('table', POINTER(CELL)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 42
class struct_FPReclass_table(Structure):
    pass

struct_FPReclass_table.__slots__ = [
    'dLow',
    'dHigh',
    'rLow',
    'rHigh',
]
struct_FPReclass_table._fields_ = [
    ('dLow', DCELL),
    ('dHigh', DCELL),
    ('rLow', DCELL),
    ('rHigh', DCELL),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 52
class struct_FPReclass(Structure):
    pass

struct_FPReclass.__slots__ = [
    'defaultDRuleSet',
    'defaultRRuleSet',
    'infiniteLeftSet',
    'infiniteRightSet',
    'rRangeSet',
    'maxNofRules',
    'nofRules',
    'defaultDMin',
    'defaultDMax',
    'defaultRMin',
    'defaultRMax',
    'infiniteDLeft',
    'infiniteDRight',
    'infiniteRLeft',
    'infiniteRRight',
    'dMin',
    'dMax',
    'rMin',
    'rMax',
    'table',
]
struct_FPReclass._fields_ = [
    ('defaultDRuleSet', c_int),
    ('defaultRRuleSet', c_int),
    ('infiniteLeftSet', c_int),
    ('infiniteRightSet', c_int),
    ('rRangeSet', c_int),
    ('maxNofRules', c_int),
    ('nofRules', c_int),
    ('defaultDMin', DCELL),
    ('defaultDMax', DCELL),
    ('defaultRMin', DCELL),
    ('defaultRMax', DCELL),
    ('infiniteDLeft', DCELL),
    ('infiniteDRight', DCELL),
    ('infiniteRLeft', DCELL),
    ('infiniteRRight', DCELL),
    ('dMin', DCELL),
    ('dMax', DCELL),
    ('rMin', DCELL),
    ('rMax', DCELL),
    ('table', POINTER(struct_FPReclass_table)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 76
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

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 109
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

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 84
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

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 127
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

enum_History_field = c_int # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_MAPID = 0 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_TITLE = (HIST_MAPID + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_MAPSET = (HIST_TITLE + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_CREATOR = (HIST_MAPSET + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_MAPTYPE = (HIST_CREATOR + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_DATSRC_1 = (HIST_MAPTYPE + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_DATSRC_2 = (HIST_DATSRC_1 + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_KEYWRD = (HIST_DATSRC_2 + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

HIST_NUM_FIELDS = (HIST_KEYWRD + 1) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 157

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 180
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

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 192
class struct_Cell_stats_node(Structure):
    pass

struct_Cell_stats_node.__slots__ = [
    'idx',
    'count',
    'left',
    'right',
]
struct_Cell_stats_node._fields_ = [
    ('idx', c_int),
    ('count', POINTER(c_long)),
    ('left', c_int),
    ('right', c_int),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 190
class struct_Cell_stats(Structure):
    pass

struct_Cell_stats.__slots__ = [
    'node',
    'tlen',
    'N',
    'curp',
    'null_data_count',
    'curoffset',
]
struct_Cell_stats._fields_ = [
    ('node', POINTER(struct_Cell_stats_node)),
    ('tlen', c_int),
    ('N', c_int),
    ('curp', c_int),
    ('null_data_count', c_long),
    ('curoffset', c_int),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 211
class struct_Histogram_list(Structure):
    pass

struct_Histogram_list.__slots__ = [
    'cat',
    'count',
]
struct_Histogram_list._fields_ = [
    ('cat', CELL),
    ('count', c_long),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 207
class struct_Histogram(Structure):
    pass

struct_Histogram.__slots__ = [
    'num',
    'list',
]
struct_Histogram._fields_ = [
    ('num', c_int),
    ('list', POINTER(struct_Histogram_list)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 218
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

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 225
class struct_Range(Structure):
    pass

struct_Range.__slots__ = [
    'min',
    'max',
    'first_time',
    'rstats',
]
struct_Range._fields_ = [
    ('min', CELL),
    ('max', CELL),
    ('first_time', c_int),
    ('rstats', struct_R_stats),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 233
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

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 241
class struct_FP_stats(Structure):
    pass

struct_FP_stats.__slots__ = [
    'geometric',
    'geom_abs',
    'flip',
    'count',
    'min',
    'max',
    'stats',
    'total',
]
struct_FP_stats._fields_ = [
    ('geometric', c_int),
    ('geom_abs', c_int),
    ('flip', c_int),
    ('count', c_int),
    ('min', DCELL),
    ('max', DCELL),
    ('stats', POINTER(c_ulong)),
    ('total', c_ulong),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 251
class struct_GDAL_link(Structure):
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 252
class struct_R_vrt(Structure):
    pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_align_window'):
        continue
    Rast_align_window = _lib.Rast_align_window
    Rast_align_window.argtypes = [POINTER(struct_Cell_head), POINTER(struct_Cell_head)]
    Rast_align_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_cell_size'):
        continue
    Rast_cell_size = _lib.Rast_cell_size
    Rast_cell_size.argtypes = [RASTER_MAP_TYPE]
    Rast_cell_size.restype = c_size_t
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_buf'):
        continue
    Rast_allocate_buf = _lib.Rast_allocate_buf
    Rast_allocate_buf.argtypes = [RASTER_MAP_TYPE]
    Rast_allocate_buf.restype = POINTER(c_ubyte)
    Rast_allocate_buf.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_c_buf'):
        continue
    Rast_allocate_c_buf = _lib.Rast_allocate_c_buf
    Rast_allocate_c_buf.argtypes = []
    Rast_allocate_c_buf.restype = POINTER(CELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_f_buf'):
        continue
    Rast_allocate_f_buf = _lib.Rast_allocate_f_buf
    Rast_allocate_f_buf.argtypes = []
    Rast_allocate_f_buf.restype = POINTER(FCELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_d_buf'):
        continue
    Rast_allocate_d_buf = _lib.Rast_allocate_d_buf
    Rast_allocate_d_buf.argtypes = []
    Rast_allocate_d_buf.restype = POINTER(DCELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_null_buf'):
        continue
    Rast_allocate_null_buf = _lib.Rast_allocate_null_buf
    Rast_allocate_null_buf.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_allocate_null_buf.restype = ReturnString
    else:
        Rast_allocate_null_buf.restype = String
        Rast_allocate_null_buf.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__allocate_null_bits'):
        continue
    Rast__allocate_null_bits = _lib.Rast__allocate_null_bits
    Rast__allocate_null_bits.argtypes = [c_int]
    Rast__allocate_null_bits.restype = POINTER(c_ubyte)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 19
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__null_bitstream_size'):
        continue
    Rast__null_bitstream_size = _lib.Rast__null_bitstream_size
    Rast__null_bitstream_size.argtypes = [c_int]
    Rast__null_bitstream_size.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_input_buf'):
        continue
    Rast_allocate_input_buf = _lib.Rast_allocate_input_buf
    Rast_allocate_input_buf.argtypes = [RASTER_MAP_TYPE]
    Rast_allocate_input_buf.restype = POINTER(c_ubyte)
    Rast_allocate_input_buf.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_c_input_buf'):
        continue
    Rast_allocate_c_input_buf = _lib.Rast_allocate_c_input_buf
    Rast_allocate_c_input_buf.argtypes = []
    Rast_allocate_c_input_buf.restype = POINTER(CELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_f_input_buf'):
        continue
    Rast_allocate_f_input_buf = _lib.Rast_allocate_f_input_buf
    Rast_allocate_f_input_buf.argtypes = []
    Rast_allocate_f_input_buf.restype = POINTER(FCELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_d_input_buf'):
        continue
    Rast_allocate_d_input_buf = _lib.Rast_allocate_d_input_buf
    Rast_allocate_d_input_buf.argtypes = []
    Rast_allocate_d_input_buf.restype = POINTER(DCELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_null_input_buf'):
        continue
    Rast_allocate_null_input_buf = _lib.Rast_allocate_null_input_buf
    Rast_allocate_null_input_buf.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_allocate_null_input_buf.restype = ReturnString
    else:
        Rast_allocate_null_input_buf.restype = String
        Rast_allocate_null_input_buf.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 27
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_output_buf'):
        continue
    Rast_allocate_output_buf = _lib.Rast_allocate_output_buf
    Rast_allocate_output_buf.argtypes = [RASTER_MAP_TYPE]
    Rast_allocate_output_buf.restype = POINTER(c_ubyte)
    Rast_allocate_output_buf.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 28
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_c_output_buf'):
        continue
    Rast_allocate_c_output_buf = _lib.Rast_allocate_c_output_buf
    Rast_allocate_c_output_buf.argtypes = []
    Rast_allocate_c_output_buf.restype = POINTER(CELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_f_output_buf'):
        continue
    Rast_allocate_f_output_buf = _lib.Rast_allocate_f_output_buf
    Rast_allocate_f_output_buf.argtypes = []
    Rast_allocate_f_output_buf.restype = POINTER(FCELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_d_output_buf'):
        continue
    Rast_allocate_d_output_buf = _lib.Rast_allocate_d_output_buf
    Rast_allocate_d_output_buf.argtypes = []
    Rast_allocate_d_output_buf.restype = POINTER(DCELL)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 31
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_allocate_null_output_buf'):
        continue
    Rast_allocate_null_output_buf = _lib.Rast_allocate_null_output_buf
    Rast_allocate_null_output_buf.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_allocate_null_output_buf.restype = ReturnString
    else:
        Rast_allocate_null_output_buf.restype = String
        Rast_allocate_null_output_buf.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__check_for_auto_masking'):
        continue
    Rast__check_for_auto_masking = _lib.Rast__check_for_auto_masking
    Rast__check_for_auto_masking.argtypes = []
    Rast__check_for_auto_masking.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 35
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_suppress_masking'):
        continue
    Rast_suppress_masking = _lib.Rast_suppress_masking
    Rast_suppress_masking.argtypes = []
    Rast_suppress_masking.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 36
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_unsuppress_masking'):
        continue
    Rast_unsuppress_masking = _lib.Rast_unsuppress_masking
    Rast_unsuppress_masking.argtypes = []
    Rast_unsuppress_masking.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 39
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_cats'):
        continue
    Rast_read_cats = _lib.Rast_read_cats
    Rast_read_cats.argtypes = [String, String, POINTER(struct_Categories)]
    Rast_read_cats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 40
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_vector_cats'):
        continue
    Rast_read_vector_cats = _lib.Rast_read_vector_cats
    Rast_read_vector_cats.argtypes = [String, String, POINTER(struct_Categories)]
    Rast_read_vector_cats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 41
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_max_c_cat'):
        continue
    Rast_get_max_c_cat = _lib.Rast_get_max_c_cat
    Rast_get_max_c_cat.argtypes = [String, String]
    Rast_get_max_c_cat.restype = CELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 42
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_cats_title'):
        continue
    Rast_get_cats_title = _lib.Rast_get_cats_title
    Rast_get_cats_title.argtypes = [POINTER(struct_Categories)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_cats_title.restype = ReturnString
    else:
        Rast_get_cats_title.restype = String
        Rast_get_cats_title.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_c_cat'):
        continue
    Rast_get_c_cat = _lib.Rast_get_c_cat
    Rast_get_c_cat.argtypes = [POINTER(CELL), POINTER(struct_Categories)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_c_cat.restype = ReturnString
    else:
        Rast_get_c_cat.restype = String
        Rast_get_c_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 44
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_f_cat'):
        continue
    Rast_get_f_cat = _lib.Rast_get_f_cat
    Rast_get_f_cat.argtypes = [POINTER(FCELL), POINTER(struct_Categories)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_f_cat.restype = ReturnString
    else:
        Rast_get_f_cat.restype = String
        Rast_get_f_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 45
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_d_cat'):
        continue
    Rast_get_d_cat = _lib.Rast_get_d_cat
    Rast_get_d_cat.argtypes = [POINTER(DCELL), POINTER(struct_Categories)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_d_cat.restype = ReturnString
    else:
        Rast_get_d_cat.restype = String
        Rast_get_d_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_cat'):
        continue
    Rast_get_cat = _lib.Rast_get_cat
    Rast_get_cat.argtypes = [POINTER(None), POINTER(struct_Categories), RASTER_MAP_TYPE]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_cat.restype = ReturnString
    else:
        Rast_get_cat.restype = String
        Rast_get_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 47
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_unmark_cats'):
        continue
    Rast_unmark_cats = _lib.Rast_unmark_cats
    Rast_unmark_cats.argtypes = [POINTER(struct_Categories)]
    Rast_unmark_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 48
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_mark_c_cats'):
        continue
    Rast_mark_c_cats = _lib.Rast_mark_c_cats
    Rast_mark_c_cats.argtypes = [POINTER(CELL), c_int, POINTER(struct_Categories)]
    Rast_mark_c_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 49
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_mark_f_cats'):
        continue
    Rast_mark_f_cats = _lib.Rast_mark_f_cats
    Rast_mark_f_cats.argtypes = [POINTER(FCELL), c_int, POINTER(struct_Categories)]
    Rast_mark_f_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 50
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_mark_d_cats'):
        continue
    Rast_mark_d_cats = _lib.Rast_mark_d_cats
    Rast_mark_d_cats.argtypes = [POINTER(DCELL), c_int, POINTER(struct_Categories)]
    Rast_mark_d_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_mark_cats'):
        continue
    Rast_mark_cats = _lib.Rast_mark_cats
    Rast_mark_cats.argtypes = [POINTER(None), c_int, POINTER(struct_Categories), RASTER_MAP_TYPE]
    Rast_mark_cats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 52
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_rewind_cats'):
        continue
    Rast_rewind_cats = _lib.Rast_rewind_cats
    Rast_rewind_cats.argtypes = [POINTER(struct_Categories)]
    Rast_rewind_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_next_marked_d_cat'):
        continue
    Rast_get_next_marked_d_cat = _lib.Rast_get_next_marked_d_cat
    Rast_get_next_marked_d_cat.argtypes = [POINTER(struct_Categories), POINTER(DCELL), POINTER(DCELL), POINTER(c_long)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_next_marked_d_cat.restype = ReturnString
    else:
        Rast_get_next_marked_d_cat.restype = String
        Rast_get_next_marked_d_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_next_marked_c_cat'):
        continue
    Rast_get_next_marked_c_cat = _lib.Rast_get_next_marked_c_cat
    Rast_get_next_marked_c_cat.argtypes = [POINTER(struct_Categories), POINTER(CELL), POINTER(CELL), POINTER(c_long)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_next_marked_c_cat.restype = ReturnString
    else:
        Rast_get_next_marked_c_cat.restype = String
        Rast_get_next_marked_c_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_next_marked_f_cat'):
        continue
    Rast_get_next_marked_f_cat = _lib.Rast_get_next_marked_f_cat
    Rast_get_next_marked_f_cat.argtypes = [POINTER(struct_Categories), POINTER(FCELL), POINTER(FCELL), POINTER(c_long)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_next_marked_f_cat.restype = ReturnString
    else:
        Rast_get_next_marked_f_cat.restype = String
        Rast_get_next_marked_f_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_next_marked_cat'):
        continue
    Rast_get_next_marked_cat = _lib.Rast_get_next_marked_cat
    Rast_get_next_marked_cat.argtypes = [POINTER(struct_Categories), POINTER(None), POINTER(None), POINTER(c_long), RASTER_MAP_TYPE]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_next_marked_cat.restype = ReturnString
    else:
        Rast_get_next_marked_cat.restype = String
        Rast_get_next_marked_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_c_cat'):
        continue
    Rast_set_c_cat = _lib.Rast_set_c_cat
    Rast_set_c_cat.argtypes = [POINTER(CELL), POINTER(CELL), String, POINTER(struct_Categories)]
    Rast_set_c_cat.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 62
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_f_cat'):
        continue
    Rast_set_f_cat = _lib.Rast_set_f_cat
    Rast_set_f_cat.argtypes = [POINTER(FCELL), POINTER(FCELL), String, POINTER(struct_Categories)]
    Rast_set_f_cat.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_d_cat'):
        continue
    Rast_set_d_cat = _lib.Rast_set_d_cat
    Rast_set_d_cat.argtypes = [POINTER(DCELL), POINTER(DCELL), String, POINTER(struct_Categories)]
    Rast_set_d_cat.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 64
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_cat'):
        continue
    Rast_set_cat = _lib.Rast_set_cat
    Rast_set_cat.argtypes = [POINTER(None), POINTER(None), String, POINTER(struct_Categories), RASTER_MAP_TYPE]
    Rast_set_cat.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_cats'):
        continue
    Rast_write_cats = _lib.Rast_write_cats
    Rast_write_cats.argtypes = [String, POINTER(struct_Categories)]
    Rast_write_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 67
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_vector_cats'):
        continue
    Rast_write_vector_cats = _lib.Rast_write_vector_cats
    Rast_write_vector_cats.argtypes = [String, POINTER(struct_Categories)]
    Rast_write_vector_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 68
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_ith_d_cat'):
        continue
    Rast_get_ith_d_cat = _lib.Rast_get_ith_d_cat
    Rast_get_ith_d_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(DCELL), POINTER(DCELL)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_ith_d_cat.restype = ReturnString
    else:
        Rast_get_ith_d_cat.restype = String
        Rast_get_ith_d_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 70
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_ith_f_cat'):
        continue
    Rast_get_ith_f_cat = _lib.Rast_get_ith_f_cat
    Rast_get_ith_f_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(None), POINTER(None)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_ith_f_cat.restype = ReturnString
    else:
        Rast_get_ith_f_cat.restype = String
        Rast_get_ith_f_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 71
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_ith_c_cat'):
        continue
    Rast_get_ith_c_cat = _lib.Rast_get_ith_c_cat
    Rast_get_ith_c_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(None), POINTER(None)]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_ith_c_cat.restype = ReturnString
    else:
        Rast_get_ith_c_cat.restype = String
        Rast_get_ith_c_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_ith_cat'):
        continue
    Rast_get_ith_cat = _lib.Rast_get_ith_cat
    Rast_get_ith_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(None), POINTER(None), RASTER_MAP_TYPE]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_ith_cat.restype = ReturnString
    else:
        Rast_get_ith_cat.restype = String
        Rast_get_ith_cat.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 74
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_cats'):
        continue
    Rast_init_cats = _lib.Rast_init_cats
    Rast_init_cats.argtypes = [String, POINTER(struct_Categories)]
    Rast_init_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 75
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_cats_title'):
        continue
    Rast_set_cats_title = _lib.Rast_set_cats_title
    Rast_set_cats_title.argtypes = [String, POINTER(struct_Categories)]
    Rast_set_cats_title.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 76
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_cats_fmt'):
        continue
    Rast_set_cats_fmt = _lib.Rast_set_cats_fmt
    Rast_set_cats_fmt.argtypes = [String, c_double, c_double, c_double, c_double, POINTER(struct_Categories)]
    Rast_set_cats_fmt.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 78
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_free_cats'):
        continue
    Rast_free_cats = _lib.Rast_free_cats
    Rast_free_cats.argtypes = [POINTER(struct_Categories)]
    Rast_free_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 79
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_copy_cats'):
        continue
    Rast_copy_cats = _lib.Rast_copy_cats
    Rast_copy_cats.argtypes = [POINTER(struct_Categories), POINTER(struct_Categories)]
    Rast_copy_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 80
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_number_of_cats'):
        continue
    Rast_number_of_cats = _lib.Rast_number_of_cats
    Rast_number_of_cats.argtypes = [POINTER(struct_Categories)]
    Rast_number_of_cats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_sort_cats'):
        continue
    Rast_sort_cats = _lib.Rast_sort_cats
    Rast_sort_cats.argtypes = [POINTER(struct_Categories)]
    Rast_sort_cats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_cell_stats'):
        continue
    Rast_init_cell_stats = _lib.Rast_init_cell_stats
    Rast_init_cell_stats.argtypes = [POINTER(struct_Cell_stats)]
    Rast_init_cell_stats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_update_cell_stats'):
        continue
    Rast_update_cell_stats = _lib.Rast_update_cell_stats
    Rast_update_cell_stats.argtypes = [POINTER(CELL), c_int, POINTER(struct_Cell_stats)]
    Rast_update_cell_stats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_find_cell_stat'):
        continue
    Rast_find_cell_stat = _lib.Rast_find_cell_stat
    Rast_find_cell_stat.argtypes = [CELL, POINTER(c_long), POINTER(struct_Cell_stats)]
    Rast_find_cell_stat.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_rewind_cell_stats'):
        continue
    Rast_rewind_cell_stats = _lib.Rast_rewind_cell_stats
    Rast_rewind_cell_stats.argtypes = [POINTER(struct_Cell_stats)]
    Rast_rewind_cell_stats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 88
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_next_cell_stat'):
        continue
    Rast_next_cell_stat = _lib.Rast_next_cell_stat
    Rast_next_cell_stat.argtypes = [POINTER(CELL), POINTER(c_long), POINTER(struct_Cell_stats)]
    Rast_next_cell_stat.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 89
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_stats_for_null_value'):
        continue
    Rast_get_stats_for_null_value = _lib.Rast_get_stats_for_null_value
    Rast_get_stats_for_null_value.argtypes = [POINTER(c_long), POINTER(struct_Cell_stats)]
    Rast_get_stats_for_null_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 90
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_free_cell_stats'):
        continue
    Rast_free_cell_stats = _lib.Rast_free_cell_stats
    Rast_free_cell_stats.argtypes = [POINTER(struct_Cell_stats)]
    Rast_free_cell_stats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 93
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_cell_title'):
        continue
    Rast_get_cell_title = _lib.Rast_get_cell_title
    Rast_get_cell_title.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_get_cell_title.restype = ReturnString
    else:
        Rast_get_cell_title.restype = String
        Rast_get_cell_title.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_cell_stats_histo_eq'):
        continue
    Rast_cell_stats_histo_eq = _lib.Rast_cell_stats_histo_eq
    Rast_cell_stats_histo_eq.argtypes = [POINTER(struct_Cell_stats), CELL, CELL, CELL, CELL, c_int, CFUNCTYPE(UNCHECKED(None), CELL, CELL, CELL)]
    Rast_cell_stats_histo_eq.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 100
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_close'):
        continue
    Rast_close = _lib.Rast_close
    Rast_close.argtypes = [c_int]
    Rast_close.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 101
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_unopen'):
        continue
    Rast_unopen = _lib.Rast_unopen
    Rast_unopen.argtypes = [c_int]
    Rast_unopen.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 102
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__unopen_all'):
        continue
    Rast__unopen_all = _lib.Rast__unopen_all
    Rast__unopen_all.argtypes = []
    Rast__unopen_all.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__close_null'):
        continue
    Rast__close_null = _lib.Rast__close_null
    Rast__close_null.argtypes = [c_int]
    Rast__close_null.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 106
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_ryg_colors'):
        continue
    Rast_make_ryg_colors = _lib.Rast_make_ryg_colors
    Rast_make_ryg_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_ryg_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 107
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_ryg_fp_colors'):
        continue
    Rast_make_ryg_fp_colors = _lib.Rast_make_ryg_fp_colors
    Rast_make_ryg_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_ryg_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 108
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_aspect_colors'):
        continue
    Rast_make_aspect_colors = _lib.Rast_make_aspect_colors
    Rast_make_aspect_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_aspect_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 109
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_aspect_fp_colors'):
        continue
    Rast_make_aspect_fp_colors = _lib.Rast_make_aspect_fp_colors
    Rast_make_aspect_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_aspect_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 110
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_byr_colors'):
        continue
    Rast_make_byr_colors = _lib.Rast_make_byr_colors
    Rast_make_byr_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_byr_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 111
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_byr_fp_colors'):
        continue
    Rast_make_byr_fp_colors = _lib.Rast_make_byr_fp_colors
    Rast_make_byr_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_byr_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 112
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_bgyr_colors'):
        continue
    Rast_make_bgyr_colors = _lib.Rast_make_bgyr_colors
    Rast_make_bgyr_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_bgyr_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 113
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_bgyr_fp_colors'):
        continue
    Rast_make_bgyr_fp_colors = _lib.Rast_make_bgyr_fp_colors
    Rast_make_bgyr_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_bgyr_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 114
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_byg_colors'):
        continue
    Rast_make_byg_colors = _lib.Rast_make_byg_colors
    Rast_make_byg_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_byg_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 115
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_byg_fp_colors'):
        continue
    Rast_make_byg_fp_colors = _lib.Rast_make_byg_fp_colors
    Rast_make_byg_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_byg_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 116
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_grey_scale_colors'):
        continue
    Rast_make_grey_scale_colors = _lib.Rast_make_grey_scale_colors
    Rast_make_grey_scale_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_grey_scale_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 117
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_grey_scale_fp_colors'):
        continue
    Rast_make_grey_scale_fp_colors = _lib.Rast_make_grey_scale_fp_colors
    Rast_make_grey_scale_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_grey_scale_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 118
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_gyr_colors'):
        continue
    Rast_make_gyr_colors = _lib.Rast_make_gyr_colors
    Rast_make_gyr_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_gyr_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 119
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_gyr_fp_colors'):
        continue
    Rast_make_gyr_fp_colors = _lib.Rast_make_gyr_fp_colors
    Rast_make_gyr_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_gyr_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 120
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_rainbow_colors'):
        continue
    Rast_make_rainbow_colors = _lib.Rast_make_rainbow_colors
    Rast_make_rainbow_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_rainbow_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 121
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_rainbow_fp_colors'):
        continue
    Rast_make_rainbow_fp_colors = _lib.Rast_make_rainbow_fp_colors
    Rast_make_rainbow_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_rainbow_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 122
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_ramp_colors'):
        continue
    Rast_make_ramp_colors = _lib.Rast_make_ramp_colors
    Rast_make_ramp_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_ramp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 123
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_ramp_fp_colors'):
        continue
    Rast_make_ramp_fp_colors = _lib.Rast_make_ramp_fp_colors
    Rast_make_ramp_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_ramp_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 124
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_wave_colors'):
        continue
    Rast_make_wave_colors = _lib.Rast_make_wave_colors
    Rast_make_wave_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_wave_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 125
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_wave_fp_colors'):
        continue
    Rast_make_wave_fp_colors = _lib.Rast_make_wave_fp_colors
    Rast_make_wave_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]
    Rast_make_wave_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 128
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_free_colors'):
        continue
    Rast_free_colors = _lib.Rast_free_colors
    Rast_free_colors.argtypes = [POINTER(struct_Colors)]
    Rast_free_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 129
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__color_free_rules'):
        continue
    Rast__color_free_rules = _lib.Rast__color_free_rules
    Rast__color_free_rules.argtypes = [POINTER(struct__Color_Info_)]
    Rast__color_free_rules.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 130
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__color_free_lookup'):
        continue
    Rast__color_free_lookup = _lib.Rast__color_free_lookup
    Rast__color_free_lookup.argtypes = [POINTER(struct__Color_Info_)]
    Rast__color_free_lookup.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 131
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__color_free_fp_lookup'):
        continue
    Rast__color_free_fp_lookup = _lib.Rast__color_free_fp_lookup
    Rast__color_free_fp_lookup.argtypes = [POINTER(struct__Color_Info_)]
    Rast__color_free_fp_lookup.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 132
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__color_reset'):
        continue
    Rast__color_reset = _lib.Rast__color_reset
    Rast__color_reset.argtypes = [POINTER(struct_Colors)]
    Rast__color_reset.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 135
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_color'):
        continue
    Rast_get_color = _lib.Rast_get_color
    Rast_get_color.argtypes = [POINTER(None), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors), RASTER_MAP_TYPE]
    Rast_get_color.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 137
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_c_color'):
        continue
    Rast_get_c_color = _lib.Rast_get_c_color
    Rast_get_c_color.argtypes = [POINTER(CELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]
    Rast_get_c_color.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 138
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_f_color'):
        continue
    Rast_get_f_color = _lib.Rast_get_f_color
    Rast_get_f_color.argtypes = [POINTER(FCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]
    Rast_get_f_color.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 139
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_d_color'):
        continue
    Rast_get_d_color = _lib.Rast_get_d_color
    Rast_get_d_color.argtypes = [POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]
    Rast_get_d_color.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 140
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_null_value_color'):
        continue
    Rast_get_null_value_color = _lib.Rast_get_null_value_color
    Rast_get_null_value_color.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]
    Rast_get_null_value_color.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 141
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_default_color'):
        continue
    Rast_get_default_color = _lib.Rast_get_default_color
    Rast_get_default_color.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]
    Rast_get_default_color.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 144
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_histogram_eq_colors'):
        continue
    Rast_make_histogram_eq_colors = _lib.Rast_make_histogram_eq_colors
    Rast_make_histogram_eq_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Cell_stats)]
    Rast_make_histogram_eq_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 145
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_histogram_log_colors'):
        continue
    Rast_make_histogram_log_colors = _lib.Rast_make_histogram_log_colors
    Rast_make_histogram_log_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Cell_stats), c_int, c_int]
    Rast_make_histogram_log_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 148
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_colors'):
        continue
    Rast_init_colors = _lib.Rast_init_colors
    Rast_init_colors.argtypes = [POINTER(struct_Colors)]
    Rast_init_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 151
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__insert_color_into_lookup'):
        continue
    Rast__insert_color_into_lookup = _lib.Rast__insert_color_into_lookup
    Rast__insert_color_into_lookup.argtypes = [CELL, c_int, c_int, c_int, POINTER(struct__Color_Info_)]
    Rast__insert_color_into_lookup.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 154
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_invert_colors'):
        continue
    Rast_invert_colors = _lib.Rast_invert_colors
    Rast_invert_colors.argtypes = [POINTER(struct_Colors)]
    Rast_invert_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 157
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_lookup_c_colors'):
        continue
    Rast_lookup_c_colors = _lib.Rast_lookup_c_colors
    Rast_lookup_c_colors.argtypes = [POINTER(CELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors)]
    Rast_lookup_c_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 160
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_lookup_colors'):
        continue
    Rast_lookup_colors = _lib.Rast_lookup_colors
    Rast_lookup_colors.argtypes = [POINTER(None), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors), RASTER_MAP_TYPE]
    Rast_lookup_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 163
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_lookup_f_colors'):
        continue
    Rast_lookup_f_colors = _lib.Rast_lookup_f_colors
    Rast_lookup_f_colors.argtypes = [POINTER(FCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors)]
    Rast_lookup_f_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 166
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_lookup_d_colors'):
        continue
    Rast_lookup_d_colors = _lib.Rast_lookup_d_colors
    Rast_lookup_d_colors.argtypes = [POINTER(DCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors)]
    Rast_lookup_d_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 169
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__lookup_colors'):
        continue
    Rast__lookup_colors = _lib.Rast__lookup_colors
    Rast__lookup_colors.argtypes = [POINTER(None), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors), c_int, c_int, RASTER_MAP_TYPE]
    Rast__lookup_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 172
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__interpolate_color_rule'):
        continue
    Rast__interpolate_color_rule = _lib.Rast__interpolate_color_rule
    Rast__interpolate_color_rule.argtypes = [DCELL, POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(struct__Color_Rule_)]
    Rast__interpolate_color_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 176
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__organize_colors'):
        continue
    Rast__organize_colors = _lib.Rast__organize_colors
    Rast__organize_colors.argtypes = [POINTER(struct_Colors)]
    Rast__organize_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 179
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_print_colors'):
        continue
    Rast_print_colors = _lib.Rast_print_colors
    Rast_print_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL, POINTER(FILE), c_int]
    Rast_print_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 182
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_random_colors'):
        continue
    Rast_make_random_colors = _lib.Rast_make_random_colors
    Rast_make_random_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]
    Rast_make_random_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 185
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_c_color_range'):
        continue
    Rast_set_c_color_range = _lib.Rast_set_c_color_range
    Rast_set_c_color_range.argtypes = [CELL, CELL, POINTER(struct_Colors)]
    Rast_set_c_color_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 186
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_d_color_range'):
        continue
    Rast_set_d_color_range = _lib.Rast_set_d_color_range
    Rast_set_d_color_range.argtypes = [DCELL, DCELL, POINTER(struct_Colors)]
    Rast_set_d_color_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 187
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_c_color_range'):
        continue
    Rast_get_c_color_range = _lib.Rast_get_c_color_range
    Rast_get_c_color_range.argtypes = [POINTER(CELL), POINTER(CELL), POINTER(struct_Colors)]
    Rast_get_c_color_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 188
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_d_color_range'):
        continue
    Rast_get_d_color_range = _lib.Rast_get_d_color_range
    Rast_get_d_color_range.argtypes = [POINTER(DCELL), POINTER(DCELL), POINTER(struct_Colors)]
    Rast_get_d_color_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 191
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_colors'):
        continue
    Rast_read_colors = _lib.Rast_read_colors
    Rast_read_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Rast_read_colors.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 192
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__read_colors'):
        continue
    Rast__read_colors = _lib.Rast__read_colors
    Rast__read_colors.argtypes = [String, String, String, POINTER(struct_Colors)]
    Rast__read_colors.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 193
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_mark_colors_as_fp'):
        continue
    Rast_mark_colors_as_fp = _lib.Rast_mark_colors_as_fp
    Rast_mark_colors_as_fp.argtypes = [POINTER(struct_Colors)]
    Rast_mark_colors_as_fp.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 196
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_remove_colors'):
        continue
    Rast_remove_colors = _lib.Rast_remove_colors
    Rast_remove_colors.argtypes = [String, String]
    Rast_remove_colors.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 199
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_d_color_rule'):
        continue
    Rast_add_d_color_rule = _lib.Rast_add_d_color_rule
    Rast_add_d_color_rule.argtypes = [POINTER(DCELL), c_int, c_int, c_int, POINTER(DCELL), c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_add_d_color_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 202
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_f_color_rule'):
        continue
    Rast_add_f_color_rule = _lib.Rast_add_f_color_rule
    Rast_add_f_color_rule.argtypes = [POINTER(FCELL), c_int, c_int, c_int, POINTER(FCELL), c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_add_f_color_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 205
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_c_color_rule'):
        continue
    Rast_add_c_color_rule = _lib.Rast_add_c_color_rule
    Rast_add_c_color_rule.argtypes = [POINTER(CELL), c_int, c_int, c_int, POINTER(CELL), c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_add_c_color_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 208
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_color_rule'):
        continue
    Rast_add_color_rule = _lib.Rast_add_color_rule
    Rast_add_color_rule.argtypes = [POINTER(None), c_int, c_int, c_int, POINTER(None), c_int, c_int, c_int, POINTER(struct_Colors), RASTER_MAP_TYPE]
    Rast_add_color_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 211
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_modular_d_color_rule'):
        continue
    Rast_add_modular_d_color_rule = _lib.Rast_add_modular_d_color_rule
    Rast_add_modular_d_color_rule.argtypes = [POINTER(DCELL), c_int, c_int, c_int, POINTER(DCELL), c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_add_modular_d_color_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 214
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_modular_f_color_rule'):
        continue
    Rast_add_modular_f_color_rule = _lib.Rast_add_modular_f_color_rule
    Rast_add_modular_f_color_rule.argtypes = [POINTER(FCELL), c_int, c_int, c_int, POINTER(FCELL), c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_add_modular_f_color_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 217
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_modular_c_color_rule'):
        continue
    Rast_add_modular_c_color_rule = _lib.Rast_add_modular_c_color_rule
    Rast_add_modular_c_color_rule.argtypes = [POINTER(CELL), c_int, c_int, c_int, POINTER(CELL), c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_add_modular_c_color_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 220
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_modular_color_rule'):
        continue
    Rast_add_modular_color_rule = _lib.Rast_add_modular_color_rule
    Rast_add_modular_color_rule.argtypes = [POINTER(None), c_int, c_int, c_int, POINTER(None), c_int, c_int, c_int, POINTER(struct_Colors), RASTER_MAP_TYPE]
    Rast_add_modular_color_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 225
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_colors_count'):
        continue
    Rast_colors_count = _lib.Rast_colors_count
    Rast_colors_count.argtypes = [POINTER(struct_Colors)]
    Rast_colors_count.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 226
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_fp_color_rule'):
        continue
    Rast_get_fp_color_rule = _lib.Rast_get_fp_color_rule
    Rast_get_fp_color_rule.argtypes = [POINTER(DCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(DCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(struct_Colors), c_int]
    Rast_get_fp_color_rule.restype = c_int
    break

read_rule_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), DCELL, DCELL, POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 232

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 234
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_parse_color_rule'):
        continue
    Rast_parse_color_rule = _lib.Rast_parse_color_rule
    Rast_parse_color_rule.argtypes = [DCELL, DCELL, String, POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast_parse_color_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 236
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_parse_color_rule_error'):
        continue
    Rast_parse_color_rule_error = _lib.Rast_parse_color_rule_error
    Rast_parse_color_rule_error.argtypes = [c_int]
    Rast_parse_color_rule_error.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 237
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_color_rule'):
        continue
    Rast_read_color_rule = _lib.Rast_read_color_rule
    Rast_read_color_rule.argtypes = [POINTER(None), DCELL, DCELL, POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast_read_color_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 239
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_color_rules'):
        continue
    Rast_read_color_rules = _lib.Rast_read_color_rules
    Rast_read_color_rules.argtypes = [POINTER(struct_Colors), DCELL, DCELL, POINTER(read_rule_fn), POINTER(None)]
    Rast_read_color_rules.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 240
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_load_colors'):
        continue
    Rast_load_colors = _lib.Rast_load_colors
    Rast_load_colors.argtypes = [POINTER(struct_Colors), String, CELL, CELL]
    Rast_load_colors.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 241
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_load_fp_colors'):
        continue
    Rast_load_fp_colors = _lib.Rast_load_fp_colors
    Rast_load_fp_colors.argtypes = [POINTER(struct_Colors), String, DCELL, DCELL]
    Rast_load_fp_colors.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 242
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_colors'):
        continue
    Rast_make_colors = _lib.Rast_make_colors
    Rast_make_colors.argtypes = [POINTER(struct_Colors), String, CELL, CELL]
    Rast_make_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 243
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_fp_colors'):
        continue
    Rast_make_fp_colors = _lib.Rast_make_fp_colors
    Rast_make_fp_colors.argtypes = [POINTER(struct_Colors), String, DCELL, DCELL]
    Rast_make_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 246
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_c_color'):
        continue
    Rast_set_c_color = _lib.Rast_set_c_color
    Rast_set_c_color.argtypes = [CELL, c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_set_c_color.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 247
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_d_color'):
        continue
    Rast_set_d_color = _lib.Rast_set_d_color
    Rast_set_d_color.argtypes = [DCELL, c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_set_d_color.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 248
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_null_value_color'):
        continue
    Rast_set_null_value_color = _lib.Rast_set_null_value_color
    Rast_set_null_value_color.argtypes = [c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_set_null_value_color.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 249
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_default_color'):
        continue
    Rast_set_default_color = _lib.Rast_set_default_color
    Rast_set_default_color.argtypes = [c_int, c_int, c_int, POINTER(struct_Colors)]
    Rast_set_default_color.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 252
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_shift_c_colors'):
        continue
    Rast_shift_c_colors = _lib.Rast_shift_c_colors
    Rast_shift_c_colors.argtypes = [CELL, POINTER(struct_Colors)]
    Rast_shift_c_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 253
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_shift_d_colors'):
        continue
    Rast_shift_d_colors = _lib.Rast_shift_d_colors
    Rast_shift_d_colors.argtypes = [DCELL, POINTER(struct_Colors)]
    Rast_shift_d_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 256
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_colors'):
        continue
    Rast_write_colors = _lib.Rast_write_colors
    Rast_write_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Rast_write_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 257
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__write_colors'):
        continue
    Rast__write_colors = _lib.Rast__write_colors
    Rast__write_colors.argtypes = [POINTER(FILE), POINTER(struct_Colors)]
    Rast__write_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 260
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_histogram_eq_colors'):
        continue
    Rast_histogram_eq_colors = _lib.Rast_histogram_eq_colors
    Rast_histogram_eq_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), POINTER(struct_Cell_stats)]
    Rast_histogram_eq_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 262
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_histogram_eq_fp_colors'):
        continue
    Rast_histogram_eq_fp_colors = _lib.Rast_histogram_eq_fp_colors
    Rast_histogram_eq_fp_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), POINTER(struct_FP_stats)]
    Rast_histogram_eq_fp_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 264
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_log_colors'):
        continue
    Rast_log_colors = _lib.Rast_log_colors
    Rast_log_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), c_int]
    Rast_log_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 265
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_abs_log_colors'):
        continue
    Rast_abs_log_colors = _lib.Rast_abs_log_colors
    Rast_abs_log_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), c_int]
    Rast_abs_log_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 268
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__check_format'):
        continue
    Rast__check_format = _lib.Rast__check_format
    Rast__check_format.argtypes = [c_int]
    Rast__check_format.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 269
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__read_row_ptrs'):
        continue
    Rast__read_row_ptrs = _lib.Rast__read_row_ptrs
    Rast__read_row_ptrs.argtypes = [c_int]
    Rast__read_row_ptrs.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 270
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__read_null_row_ptrs'):
        continue
    Rast__read_null_row_ptrs = _lib.Rast__read_null_row_ptrs
    Rast__read_null_row_ptrs.argtypes = [c_int, c_int]
    Rast__read_null_row_ptrs.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 271
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__write_row_ptrs'):
        continue
    Rast__write_row_ptrs = _lib.Rast__write_row_ptrs
    Rast__write_row_ptrs.argtypes = [c_int]
    Rast__write_row_ptrs.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 272
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__write_null_row_ptrs'):
        continue
    Rast__write_null_row_ptrs = _lib.Rast__write_null_row_ptrs
    Rast__write_null_row_ptrs.argtypes = [c_int, c_int]
    Rast__write_null_row_ptrs.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 275
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_clear'):
        continue
    Rast_fpreclass_clear = _lib.Rast_fpreclass_clear
    Rast_fpreclass_clear.argtypes = [POINTER(struct_FPReclass)]
    Rast_fpreclass_clear.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 276
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_reset'):
        continue
    Rast_fpreclass_reset = _lib.Rast_fpreclass_reset
    Rast_fpreclass_reset.argtypes = [POINTER(struct_FPReclass)]
    Rast_fpreclass_reset.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 277
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_init'):
        continue
    Rast_fpreclass_init = _lib.Rast_fpreclass_init
    Rast_fpreclass_init.argtypes = [POINTER(struct_FPReclass)]
    Rast_fpreclass_init.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 278
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_set_domain'):
        continue
    Rast_fpreclass_set_domain = _lib.Rast_fpreclass_set_domain
    Rast_fpreclass_set_domain.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]
    Rast_fpreclass_set_domain.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 279
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_set_range'):
        continue
    Rast_fpreclass_set_range = _lib.Rast_fpreclass_set_range
    Rast_fpreclass_set_range.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]
    Rast_fpreclass_set_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 280
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_get_limits'):
        continue
    Rast_fpreclass_get_limits = _lib.Rast_fpreclass_get_limits
    Rast_fpreclass_get_limits.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL), POINTER(DCELL), POINTER(DCELL)]
    Rast_fpreclass_get_limits.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 282
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_nof_rules'):
        continue
    Rast_fpreclass_nof_rules = _lib.Rast_fpreclass_nof_rules
    Rast_fpreclass_nof_rules.argtypes = [POINTER(struct_FPReclass)]
    Rast_fpreclass_nof_rules.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 283
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_get_ith_rule'):
        continue
    Rast_fpreclass_get_ith_rule = _lib.Rast_fpreclass_get_ith_rule
    Rast_fpreclass_get_ith_rule.argtypes = [POINTER(struct_FPReclass), c_int, POINTER(DCELL), POINTER(DCELL), POINTER(DCELL), POINTER(DCELL)]
    Rast_fpreclass_get_ith_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 285
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_set_neg_infinite_rule'):
        continue
    Rast_fpreclass_set_neg_infinite_rule = _lib.Rast_fpreclass_set_neg_infinite_rule
    Rast_fpreclass_set_neg_infinite_rule.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]
    Rast_fpreclass_set_neg_infinite_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 286
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_get_neg_infinite_rule'):
        continue
    Rast_fpreclass_get_neg_infinite_rule = _lib.Rast_fpreclass_get_neg_infinite_rule
    Rast_fpreclass_get_neg_infinite_rule.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL)]
    Rast_fpreclass_get_neg_infinite_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 288
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_set_pos_infinite_rule'):
        continue
    Rast_fpreclass_set_pos_infinite_rule = _lib.Rast_fpreclass_set_pos_infinite_rule
    Rast_fpreclass_set_pos_infinite_rule.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]
    Rast_fpreclass_set_pos_infinite_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 289
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_get_pos_infinite_rule'):
        continue
    Rast_fpreclass_get_pos_infinite_rule = _lib.Rast_fpreclass_get_pos_infinite_rule
    Rast_fpreclass_get_pos_infinite_rule.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL)]
    Rast_fpreclass_get_pos_infinite_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 291
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_add_rule'):
        continue
    Rast_fpreclass_add_rule = _lib.Rast_fpreclass_add_rule
    Rast_fpreclass_add_rule.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL, DCELL, DCELL]
    Rast_fpreclass_add_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 292
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_reverse_rule_order'):
        continue
    Rast_fpreclass_reverse_rule_order = _lib.Rast_fpreclass_reverse_rule_order
    Rast_fpreclass_reverse_rule_order.argtypes = [POINTER(struct_FPReclass)]
    Rast_fpreclass_reverse_rule_order.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 293
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_get_cell_value'):
        continue
    Rast_fpreclass_get_cell_value = _lib.Rast_fpreclass_get_cell_value
    Rast_fpreclass_get_cell_value.argtypes = [POINTER(struct_FPReclass), DCELL]
    Rast_fpreclass_get_cell_value.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 294
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_di'):
        continue
    Rast_fpreclass_perform_di = _lib.Rast_fpreclass_perform_di
    Rast_fpreclass_perform_di.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(CELL), c_int]
    Rast_fpreclass_perform_di.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 296
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_df'):
        continue
    Rast_fpreclass_perform_df = _lib.Rast_fpreclass_perform_df
    Rast_fpreclass_perform_df.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(FCELL), c_int]
    Rast_fpreclass_perform_df.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 298
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_dd'):
        continue
    Rast_fpreclass_perform_dd = _lib.Rast_fpreclass_perform_dd
    Rast_fpreclass_perform_dd.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL), c_int]
    Rast_fpreclass_perform_dd.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 300
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_fi'):
        continue
    Rast_fpreclass_perform_fi = _lib.Rast_fpreclass_perform_fi
    Rast_fpreclass_perform_fi.argtypes = [POINTER(struct_FPReclass), POINTER(FCELL), POINTER(CELL), c_int]
    Rast_fpreclass_perform_fi.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 302
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_ff'):
        continue
    Rast_fpreclass_perform_ff = _lib.Rast_fpreclass_perform_ff
    Rast_fpreclass_perform_ff.argtypes = [POINTER(struct_FPReclass), POINTER(FCELL), POINTER(FCELL), c_int]
    Rast_fpreclass_perform_ff.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 304
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_fd'):
        continue
    Rast_fpreclass_perform_fd = _lib.Rast_fpreclass_perform_fd
    Rast_fpreclass_perform_fd.argtypes = [POINTER(struct_FPReclass), POINTER(FCELL), POINTER(DCELL), c_int]
    Rast_fpreclass_perform_fd.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 306
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_ii'):
        continue
    Rast_fpreclass_perform_ii = _lib.Rast_fpreclass_perform_ii
    Rast_fpreclass_perform_ii.argtypes = [POINTER(struct_FPReclass), POINTER(CELL), POINTER(CELL), c_int]
    Rast_fpreclass_perform_ii.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 308
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_if'):
        continue
    Rast_fpreclass_perform_if = _lib.Rast_fpreclass_perform_if
    Rast_fpreclass_perform_if.argtypes = [POINTER(struct_FPReclass), POINTER(CELL), POINTER(FCELL), c_int]
    Rast_fpreclass_perform_if.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 310
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_fpreclass_perform_id'):
        continue
    Rast_fpreclass_perform_id = _lib.Rast_fpreclass_perform_id
    Rast_fpreclass_perform_id.argtypes = [POINTER(struct_FPReclass), POINTER(CELL), POINTER(DCELL), c_int]
    Rast_fpreclass_perform_id.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 313
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_gdal'):
        continue
    Rast_init_gdal = _lib.Rast_init_gdal
    Rast_init_gdal.argtypes = []
    Rast_init_gdal.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 314
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_gdal_link'):
        continue
    Rast_get_gdal_link = _lib.Rast_get_gdal_link
    Rast_get_gdal_link.argtypes = [String, String]
    Rast_get_gdal_link.restype = POINTER(struct_GDAL_link)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 315
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_create_gdal_link'):
        continue
    Rast_create_gdal_link = _lib.Rast_create_gdal_link
    Rast_create_gdal_link.argtypes = [String, RASTER_MAP_TYPE]
    Rast_create_gdal_link.restype = POINTER(struct_GDAL_link)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 316
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_close_gdal_link'):
        continue
    Rast_close_gdal_link = _lib.Rast_close_gdal_link
    Rast_close_gdal_link.argtypes = [POINTER(struct_GDAL_link)]
    Rast_close_gdal_link.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 317
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_close_gdal_write_link'):
        continue
    Rast_close_gdal_write_link = _lib.Rast_close_gdal_write_link
    Rast_close_gdal_write_link.argtypes = [POINTER(struct_GDAL_link)]
    Rast_close_gdal_write_link.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 320
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_cellhd'):
        continue
    Rast_get_cellhd = _lib.Rast_get_cellhd
    Rast_get_cellhd.argtypes = [String, String, POINTER(struct_Cell_head)]
    Rast_get_cellhd.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 323
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_row_nomask'):
        continue
    Rast_get_row_nomask = _lib.Rast_get_row_nomask
    Rast_get_row_nomask.argtypes = [c_int, POINTER(None), c_int, RASTER_MAP_TYPE]
    Rast_get_row_nomask.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 324
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_c_row_nomask'):
        continue
    Rast_get_c_row_nomask = _lib.Rast_get_c_row_nomask
    Rast_get_c_row_nomask.argtypes = [c_int, POINTER(CELL), c_int]
    Rast_get_c_row_nomask.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 325
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_f_row_nomask'):
        continue
    Rast_get_f_row_nomask = _lib.Rast_get_f_row_nomask
    Rast_get_f_row_nomask.argtypes = [c_int, POINTER(FCELL), c_int]
    Rast_get_f_row_nomask.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 326
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_d_row_nomask'):
        continue
    Rast_get_d_row_nomask = _lib.Rast_get_d_row_nomask
    Rast_get_d_row_nomask.argtypes = [c_int, POINTER(DCELL), c_int]
    Rast_get_d_row_nomask.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 327
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_row'):
        continue
    Rast_get_row = _lib.Rast_get_row
    Rast_get_row.argtypes = [c_int, POINTER(None), c_int, RASTER_MAP_TYPE]
    Rast_get_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 328
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_c_row'):
        continue
    Rast_get_c_row = _lib.Rast_get_c_row
    Rast_get_c_row.argtypes = [c_int, POINTER(CELL), c_int]
    Rast_get_c_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 329
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_f_row'):
        continue
    Rast_get_f_row = _lib.Rast_get_f_row
    Rast_get_f_row.argtypes = [c_int, POINTER(FCELL), c_int]
    Rast_get_f_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 330
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_d_row'):
        continue
    Rast_get_d_row = _lib.Rast_get_d_row
    Rast_get_d_row.argtypes = [c_int, POINTER(DCELL), c_int]
    Rast_get_d_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 331
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_null_value_row'):
        continue
    Rast_get_null_value_row = _lib.Rast_get_null_value_row
    Rast_get_null_value_row.argtypes = [c_int, String, c_int]
    Rast_get_null_value_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 332
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__read_null_bits'):
        continue
    Rast__read_null_bits = _lib.Rast__read_null_bits
    Rast__read_null_bits.argtypes = [c_int, c_int, POINTER(c_ubyte)]
    Rast__read_null_bits.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 335
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_row_colors'):
        continue
    Rast_get_row_colors = _lib.Rast_get_row_colors
    Rast_get_row_colors.argtypes = [c_int, c_int, POINTER(struct_Colors), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte)]
    Rast_get_row_colors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 339
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_histogram_eq'):
        continue
    Rast_histogram_eq = _lib.Rast_histogram_eq
    Rast_histogram_eq.argtypes = [POINTER(struct_Histogram), POINTER(POINTER(c_ubyte)), POINTER(CELL), POINTER(CELL)]
    Rast_histogram_eq.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 343
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_histogram'):
        continue
    Rast_init_histogram = _lib.Rast_init_histogram
    Rast_init_histogram.argtypes = [POINTER(struct_Histogram)]
    Rast_init_histogram.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 344
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_histogram'):
        continue
    Rast_read_histogram = _lib.Rast_read_histogram
    Rast_read_histogram.argtypes = [String, String, POINTER(struct_Histogram)]
    Rast_read_histogram.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 345
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_histogram'):
        continue
    Rast_write_histogram = _lib.Rast_write_histogram
    Rast_write_histogram.argtypes = [String, POINTER(struct_Histogram)]
    Rast_write_histogram.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 346
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_histogram_cs'):
        continue
    Rast_write_histogram_cs = _lib.Rast_write_histogram_cs
    Rast_write_histogram_cs.argtypes = [String, POINTER(struct_Cell_stats)]
    Rast_write_histogram_cs.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 347
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_make_histogram_cs'):
        continue
    Rast_make_histogram_cs = _lib.Rast_make_histogram_cs
    Rast_make_histogram_cs.argtypes = [POINTER(struct_Cell_stats), POINTER(struct_Histogram)]
    Rast_make_histogram_cs.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 348
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_histogram_num'):
        continue
    Rast_get_histogram_num = _lib.Rast_get_histogram_num
    Rast_get_histogram_num.argtypes = [POINTER(struct_Histogram)]
    Rast_get_histogram_num.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 349
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_histogram_cat'):
        continue
    Rast_get_histogram_cat = _lib.Rast_get_histogram_cat
    Rast_get_histogram_cat.argtypes = [c_int, POINTER(struct_Histogram)]
    Rast_get_histogram_cat.restype = CELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 350
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_histogram_count'):
        continue
    Rast_get_histogram_count = _lib.Rast_get_histogram_count
    Rast_get_histogram_count.argtypes = [c_int, POINTER(struct_Histogram)]
    Rast_get_histogram_count.restype = c_long
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 351
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_free_histogram'):
        continue
    Rast_free_histogram = _lib.Rast_free_histogram
    Rast_free_histogram.argtypes = [POINTER(struct_Histogram)]
    Rast_free_histogram.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 352
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_sort_histogram'):
        continue
    Rast_sort_histogram = _lib.Rast_sort_histogram
    Rast_sort_histogram.argtypes = [POINTER(struct_Histogram)]
    Rast_sort_histogram.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 353
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_sort_histogram_by_count'):
        continue
    Rast_sort_histogram_by_count = _lib.Rast_sort_histogram_by_count
    Rast_sort_histogram_by_count.argtypes = [POINTER(struct_Histogram)]
    Rast_sort_histogram_by_count.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 354
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_remove_histogram'):
        continue
    Rast_remove_histogram = _lib.Rast_remove_histogram
    Rast_remove_histogram.argtypes = [String]
    Rast_remove_histogram.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 355
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_add_histogram'):
        continue
    Rast_add_histogram = _lib.Rast_add_histogram
    Rast_add_histogram.argtypes = [CELL, c_long, POINTER(struct_Histogram)]
    Rast_add_histogram.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 356
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_histogram'):
        continue
    Rast_set_histogram = _lib.Rast_set_histogram
    Rast_set_histogram.argtypes = [CELL, c_long, POINTER(struct_Histogram)]
    Rast_set_histogram.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 357
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_extend_histogram'):
        continue
    Rast_extend_histogram = _lib.Rast_extend_histogram
    Rast_extend_histogram.argtypes = [CELL, c_long, POINTER(struct_Histogram)]
    Rast_extend_histogram.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 358
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_zero_histogram'):
        continue
    Rast_zero_histogram = _lib.Rast_zero_histogram
    Rast_zero_histogram.argtypes = [POINTER(struct_Histogram)]
    Rast_zero_histogram.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 361
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__read_history'):
        continue
    Rast__read_history = _lib.Rast__read_history
    Rast__read_history.argtypes = [POINTER(struct_History), POINTER(FILE)]
    Rast__read_history.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 362
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_history'):
        continue
    Rast_read_history = _lib.Rast_read_history
    Rast_read_history.argtypes = [String, String, POINTER(struct_History)]
    Rast_read_history.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 363
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__write_history'):
        continue
    Rast__write_history = _lib.Rast__write_history
    Rast__write_history.argtypes = [POINTER(struct_History), POINTER(FILE)]
    Rast__write_history.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 364
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_history'):
        continue
    Rast_write_history = _lib.Rast_write_history
    Rast_write_history.argtypes = [String, POINTER(struct_History)]
    Rast_write_history.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 365
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_short_history'):
        continue
    Rast_short_history = _lib.Rast_short_history
    Rast_short_history.argtypes = [String, String, POINTER(struct_History)]
    Rast_short_history.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 366
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_command_history'):
        continue
    Rast_command_history = _lib.Rast_command_history
    Rast_command_history.argtypes = [POINTER(struct_History)]
    Rast_command_history.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 367
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_append_history'):
        continue
    Rast_append_history = _lib.Rast_append_history
    Rast_append_history.argtypes = [POINTER(struct_History), String]
    Rast_append_history.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 368
for _lib in _libs.values():
    if hasattr(_lib, 'Rast_append_format_history'):
        _func = _lib.Rast_append_format_history
        _restype = None
        _errcheck = None
        _argtypes = [POINTER(struct_History), String]
        Rast_append_format_history = _variadic_function(_func,_restype,_argtypes,_errcheck)

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 370
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_history'):
        continue
    Rast_get_history = _lib.Rast_get_history
    Rast_get_history.argtypes = [POINTER(struct_History), c_int]
    Rast_get_history.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 371
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_history'):
        continue
    Rast_set_history = _lib.Rast_set_history
    Rast_set_history.argtypes = [POINTER(struct_History), c_int, String]
    Rast_set_history.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 372
for _lib in _libs.values():
    if hasattr(_lib, 'Rast_format_history'):
        _func = _lib.Rast_format_history
        _restype = None
        _errcheck = None
        _argtypes = [POINTER(struct_History), c_int, String]
        Rast_format_history = _variadic_function(_func,_restype,_argtypes,_errcheck)

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 374
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_clear_history'):
        continue
    Rast_clear_history = _lib.Rast_clear_history
    Rast_clear_history.argtypes = [POINTER(struct_History)]
    Rast_clear_history.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 375
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_free_history'):
        continue
    Rast_free_history = _lib.Rast_free_history
    Rast_free_history.argtypes = [POINTER(struct_History)]
    Rast_free_history.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 376
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_history_length'):
        continue
    Rast_history_length = _lib.Rast_history_length
    Rast_history_length.argtypes = [POINTER(struct_History)]
    Rast_history_length.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 377
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_history_line'):
        continue
    Rast_history_line = _lib.Rast_history_line
    Rast_history_line.argtypes = [POINTER(struct_History), c_int]
    Rast_history_line.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 380
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init'):
        continue
    Rast_init = _lib.Rast_init
    Rast_init.argtypes = []
    Rast_init.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 381
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__check_init'):
        continue
    Rast__check_init = _lib.Rast__check_init
    Rast__check_init.argtypes = []
    Rast__check_init.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 382
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_all'):
        continue
    Rast_init_all = _lib.Rast_init_all
    Rast_init_all.argtypes = []
    Rast_init_all.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 383
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__init'):
        continue
    Rast__init = _lib.Rast__init
    Rast__init.argtypes = []
    Rast__init.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 384
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__error_handler'):
        continue
    Rast__error_handler = _lib.Rast__error_handler
    Rast__error_handler.argtypes = [POINTER(None)]
    Rast__error_handler.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 387
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_interp_linear'):
        continue
    Rast_interp_linear = _lib.Rast_interp_linear
    Rast_interp_linear.argtypes = [c_double, DCELL, DCELL]
    Rast_interp_linear.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 388
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_interp_bilinear'):
        continue
    Rast_interp_bilinear = _lib.Rast_interp_bilinear
    Rast_interp_bilinear.argtypes = [c_double, c_double, DCELL, DCELL, DCELL, DCELL]
    Rast_interp_bilinear.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 389
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_interp_cubic'):
        continue
    Rast_interp_cubic = _lib.Rast_interp_cubic
    Rast_interp_cubic.argtypes = [c_double, DCELL, DCELL, DCELL, DCELL]
    Rast_interp_cubic.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 390
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_interp_bicubic'):
        continue
    Rast_interp_bicubic = _lib.Rast_interp_bicubic
    Rast_interp_bicubic.argtypes = [c_double, c_double, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL]
    Rast_interp_bicubic.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 394
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_interp_lanczos'):
        continue
    Rast_interp_lanczos = _lib.Rast_interp_lanczos
    Rast_interp_lanczos.argtypes = [c_double, c_double, POINTER(DCELL)]
    Rast_interp_lanczos.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 395
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_interp_cubic_bspline'):
        continue
    Rast_interp_cubic_bspline = _lib.Rast_interp_cubic_bspline
    Rast_interp_cubic_bspline.argtypes = [c_double, DCELL, DCELL, DCELL, DCELL]
    Rast_interp_cubic_bspline.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 396
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_interp_bicubic_bspline'):
        continue
    Rast_interp_bicubic_bspline = _lib.Rast_interp_bicubic_bspline
    Rast_interp_bicubic_bspline.argtypes = [c_double, c_double, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL]
    Rast_interp_bicubic_bspline.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 400
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_option_to_interp_type'):
        continue
    Rast_option_to_interp_type = _lib.Rast_option_to_interp_type
    Rast_option_to_interp_type.argtypes = [POINTER(struct_Option)]
    Rast_option_to_interp_type.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 403
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_mask_info'):
        continue
    Rast_mask_info = _lib.Rast_mask_info
    Rast_mask_info.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_mask_info.restype = ReturnString
    else:
        Rast_mask_info.restype = String
        Rast_mask_info.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 404
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__mask_info'):
        continue
    Rast__mask_info = _lib.Rast__mask_info
    Rast__mask_info.argtypes = [String, String]
    Rast__mask_info.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 407
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_maskfd'):
        continue
    Rast_maskfd = _lib.Rast_maskfd
    Rast_maskfd.argtypes = []
    Rast_maskfd.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 417
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__set_null_value'):
        continue
    Rast__set_null_value = _lib.Rast__set_null_value
    Rast__set_null_value.argtypes = [POINTER(None), c_int, c_int, RASTER_MAP_TYPE]
    Rast__set_null_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 418
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_null_value'):
        continue
    Rast_set_null_value = _lib.Rast_set_null_value
    Rast_set_null_value.argtypes = [POINTER(None), c_int, RASTER_MAP_TYPE]
    Rast_set_null_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 419
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_c_null_value'):
        continue
    Rast_set_c_null_value = _lib.Rast_set_c_null_value
    Rast_set_c_null_value.argtypes = [POINTER(CELL), c_int]
    Rast_set_c_null_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 420
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_f_null_value'):
        continue
    Rast_set_f_null_value = _lib.Rast_set_f_null_value
    Rast_set_f_null_value.argtypes = [POINTER(FCELL), c_int]
    Rast_set_f_null_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 421
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_d_null_value'):
        continue
    Rast_set_d_null_value = _lib.Rast_set_d_null_value
    Rast_set_d_null_value.argtypes = [POINTER(DCELL), c_int]
    Rast_set_d_null_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 422
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_is_null_value'):
        continue
    Rast_is_null_value = _lib.Rast_is_null_value
    Rast_is_null_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]
    Rast_is_null_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 432
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_insert_null_values'):
        continue
    Rast_insert_null_values = _lib.Rast_insert_null_values
    Rast_insert_null_values.argtypes = [POINTER(None), String, c_int, RASTER_MAP_TYPE]
    Rast_insert_null_values.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 433
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_insert_c_null_values'):
        continue
    Rast_insert_c_null_values = _lib.Rast_insert_c_null_values
    Rast_insert_c_null_values.argtypes = [POINTER(CELL), String, c_int]
    Rast_insert_c_null_values.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 434
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_insert_f_null_values'):
        continue
    Rast_insert_f_null_values = _lib.Rast_insert_f_null_values
    Rast_insert_f_null_values.argtypes = [POINTER(FCELL), String, c_int]
    Rast_insert_f_null_values.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 435
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_insert_d_null_values'):
        continue
    Rast_insert_d_null_values = _lib.Rast_insert_d_null_values
    Rast_insert_d_null_values.argtypes = [POINTER(DCELL), String, c_int]
    Rast_insert_d_null_values.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 436
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__check_null_bit'):
        continue
    Rast__check_null_bit = _lib.Rast__check_null_bit
    Rast__check_null_bit.argtypes = [POINTER(c_ubyte), c_int, c_int]
    Rast__check_null_bit.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 437
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__convert_01_flags'):
        continue
    Rast__convert_01_flags = _lib.Rast__convert_01_flags
    Rast__convert_01_flags.argtypes = [String, POINTER(c_ubyte), c_int]
    Rast__convert_01_flags.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 438
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__convert_flags_01'):
        continue
    Rast__convert_flags_01 = _lib.Rast__convert_flags_01
    Rast__convert_flags_01.argtypes = [String, POINTER(c_ubyte), c_int]
    Rast__convert_flags_01.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 439
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__init_null_bits'):
        continue
    Rast__init_null_bits = _lib.Rast__init_null_bits
    Rast__init_null_bits.argtypes = [POINTER(c_ubyte), c_int]
    Rast__init_null_bits.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 442
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_open_old'):
        continue
    Rast_open_old = _lib.Rast_open_old
    Rast_open_old.argtypes = [String, String]
    Rast_open_old.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 443
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__open_old'):
        continue
    Rast__open_old = _lib.Rast__open_old
    Rast__open_old.argtypes = [String, String]
    Rast__open_old.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 444
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_open_c_new'):
        continue
    Rast_open_c_new = _lib.Rast_open_c_new
    Rast_open_c_new.argtypes = [String]
    Rast_open_c_new.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 445
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_open_c_new_uncompressed'):
        continue
    Rast_open_c_new_uncompressed = _lib.Rast_open_c_new_uncompressed
    Rast_open_c_new_uncompressed.argtypes = [String]
    Rast_open_c_new_uncompressed.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 446
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_want_histogram'):
        continue
    Rast_want_histogram = _lib.Rast_want_histogram
    Rast_want_histogram.argtypes = [c_int]
    Rast_want_histogram.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 447
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_cell_format'):
        continue
    Rast_set_cell_format = _lib.Rast_set_cell_format
    Rast_set_cell_format.argtypes = [c_int]
    Rast_set_cell_format.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 448
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_cell_format'):
        continue
    Rast_get_cell_format = _lib.Rast_get_cell_format
    Rast_get_cell_format.argtypes = [CELL]
    Rast_get_cell_format.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 449
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_open_fp_new'):
        continue
    Rast_open_fp_new = _lib.Rast_open_fp_new
    Rast_open_fp_new.argtypes = [String]
    Rast_open_fp_new.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 450
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_open_fp_new_uncompressed'):
        continue
    Rast_open_fp_new_uncompressed = _lib.Rast_open_fp_new_uncompressed
    Rast_open_fp_new_uncompressed.argtypes = [String]
    Rast_open_fp_new_uncompressed.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 451
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_fp_type'):
        continue
    Rast_set_fp_type = _lib.Rast_set_fp_type
    Rast_set_fp_type.argtypes = [RASTER_MAP_TYPE]
    Rast_set_fp_type.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 452
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_map_is_fp'):
        continue
    Rast_map_is_fp = _lib.Rast_map_is_fp
    Rast_map_is_fp.argtypes = [String, String]
    Rast_map_is_fp.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 453
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_map_type'):
        continue
    Rast_map_type = _lib.Rast_map_type
    Rast_map_type.argtypes = [String, String]
    Rast_map_type.restype = RASTER_MAP_TYPE
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 454
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__check_fp_type'):
        continue
    Rast__check_fp_type = _lib.Rast__check_fp_type
    Rast__check_fp_type.argtypes = [String, String]
    Rast__check_fp_type.restype = RASTER_MAP_TYPE
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 455
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_map_type'):
        continue
    Rast_get_map_type = _lib.Rast_get_map_type
    Rast_get_map_type.argtypes = [c_int]
    Rast_get_map_type.restype = RASTER_MAP_TYPE
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 456
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_open_new'):
        continue
    Rast_open_new = _lib.Rast_open_new
    Rast_open_new.argtypes = [String, RASTER_MAP_TYPE]
    Rast_open_new.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 457
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_open_new_uncompressed'):
        continue
    Rast_open_new_uncompressed = _lib.Rast_open_new_uncompressed
    Rast_open_new_uncompressed.argtypes = [String, RASTER_MAP_TYPE]
    Rast_open_new_uncompressed.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 458
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_quant_rules'):
        continue
    Rast_set_quant_rules = _lib.Rast_set_quant_rules
    Rast_set_quant_rules.argtypes = [c_int, POINTER(struct_Quant)]
    Rast_set_quant_rules.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 459
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__open_null_write'):
        continue
    Rast__open_null_write = _lib.Rast__open_null_write
    Rast__open_null_write.argtypes = [String]
    Rast__open_null_write.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 462
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_put_cellhd'):
        continue
    Rast_put_cellhd = _lib.Rast_put_cellhd
    Rast_put_cellhd.argtypes = [String, POINTER(struct_Cell_head)]
    Rast_put_cellhd.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 465
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_put_row'):
        continue
    Rast_put_row = _lib.Rast_put_row
    Rast_put_row.argtypes = [c_int, POINTER(None), RASTER_MAP_TYPE]
    Rast_put_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 466
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_put_c_row'):
        continue
    Rast_put_c_row = _lib.Rast_put_c_row
    Rast_put_c_row.argtypes = [c_int, POINTER(CELL)]
    Rast_put_c_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 467
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_put_f_row'):
        continue
    Rast_put_f_row = _lib.Rast_put_f_row
    Rast_put_f_row.argtypes = [c_int, POINTER(FCELL)]
    Rast_put_f_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 468
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_put_d_row'):
        continue
    Rast_put_d_row = _lib.Rast_put_d_row
    Rast_put_d_row.argtypes = [c_int, POINTER(DCELL)]
    Rast_put_d_row.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 469
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__write_null_bits'):
        continue
    Rast__write_null_bits = _lib.Rast__write_null_bits
    Rast__write_null_bits.argtypes = [c_int, POINTER(c_ubyte)]
    Rast__write_null_bits.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 472
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_put_cell_title'):
        continue
    Rast_put_cell_title = _lib.Rast_put_cell_title
    Rast_put_cell_title.argtypes = [String, String]
    Rast_put_cell_title.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 475
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_clear'):
        continue
    Rast_quant_clear = _lib.Rast_quant_clear
    Rast_quant_clear.argtypes = [POINTER(struct_Quant)]
    Rast_quant_clear.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 476
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_free'):
        continue
    Rast_quant_free = _lib.Rast_quant_free
    Rast_quant_free.argtypes = [POINTER(struct_Quant)]
    Rast_quant_free.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 477
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__quant_organize_fp_lookup'):
        continue
    Rast__quant_organize_fp_lookup = _lib.Rast__quant_organize_fp_lookup
    Rast__quant_organize_fp_lookup.argtypes = [POINTER(struct_Quant)]
    Rast__quant_organize_fp_lookup.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 478
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_init'):
        continue
    Rast_quant_init = _lib.Rast_quant_init
    Rast_quant_init.argtypes = [POINTER(struct_Quant)]
    Rast_quant_init.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 479
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_is_truncate'):
        continue
    Rast_quant_is_truncate = _lib.Rast_quant_is_truncate
    Rast_quant_is_truncate.argtypes = [POINTER(struct_Quant)]
    Rast_quant_is_truncate.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 480
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_is_round'):
        continue
    Rast_quant_is_round = _lib.Rast_quant_is_round
    Rast_quant_is_round.argtypes = [POINTER(struct_Quant)]
    Rast_quant_is_round.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 481
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_truncate'):
        continue
    Rast_quant_truncate = _lib.Rast_quant_truncate
    Rast_quant_truncate.argtypes = [POINTER(struct_Quant)]
    Rast_quant_truncate.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 482
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_round'):
        continue
    Rast_quant_round = _lib.Rast_quant_round
    Rast_quant_round.argtypes = [POINTER(struct_Quant)]
    Rast_quant_round.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 483
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_get_limits'):
        continue
    Rast_quant_get_limits = _lib.Rast_quant_get_limits
    Rast_quant_get_limits.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(DCELL), POINTER(CELL), POINTER(CELL)]
    Rast_quant_get_limits.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 485
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_nof_rules'):
        continue
    Rast_quant_nof_rules = _lib.Rast_quant_nof_rules
    Rast_quant_nof_rules.argtypes = [POINTER(struct_Quant)]
    Rast_quant_nof_rules.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 486
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_get_ith_rule'):
        continue
    Rast_quant_get_ith_rule = _lib.Rast_quant_get_ith_rule
    Rast_quant_get_ith_rule.argtypes = [POINTER(struct_Quant), c_int, POINTER(DCELL), POINTER(DCELL), POINTER(CELL), POINTER(CELL)]
    Rast_quant_get_ith_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 488
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_set_neg_infinite_rule'):
        continue
    Rast_quant_set_neg_infinite_rule = _lib.Rast_quant_set_neg_infinite_rule
    Rast_quant_set_neg_infinite_rule.argtypes = [POINTER(struct_Quant), DCELL, CELL]
    Rast_quant_set_neg_infinite_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 489
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_get_neg_infinite_rule'):
        continue
    Rast_quant_get_neg_infinite_rule = _lib.Rast_quant_get_neg_infinite_rule
    Rast_quant_get_neg_infinite_rule.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(CELL)]
    Rast_quant_get_neg_infinite_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 490
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_set_pos_infinite_rule'):
        continue
    Rast_quant_set_pos_infinite_rule = _lib.Rast_quant_set_pos_infinite_rule
    Rast_quant_set_pos_infinite_rule.argtypes = [POINTER(struct_Quant), DCELL, CELL]
    Rast_quant_set_pos_infinite_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 491
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_get_pos_infinite_rule'):
        continue
    Rast_quant_get_pos_infinite_rule = _lib.Rast_quant_get_pos_infinite_rule
    Rast_quant_get_pos_infinite_rule.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(CELL)]
    Rast_quant_get_pos_infinite_rule.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 492
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_add_rule'):
        continue
    Rast_quant_add_rule = _lib.Rast_quant_add_rule
    Rast_quant_add_rule.argtypes = [POINTER(struct_Quant), DCELL, DCELL, CELL, CELL]
    Rast_quant_add_rule.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 493
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_reverse_rule_order'):
        continue
    Rast_quant_reverse_rule_order = _lib.Rast_quant_reverse_rule_order
    Rast_quant_reverse_rule_order.argtypes = [POINTER(struct_Quant)]
    Rast_quant_reverse_rule_order.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 494
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_get_cell_value'):
        continue
    Rast_quant_get_cell_value = _lib.Rast_quant_get_cell_value
    Rast_quant_get_cell_value.argtypes = [POINTER(struct_Quant), DCELL]
    Rast_quant_get_cell_value.restype = CELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 495
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_perform_d'):
        continue
    Rast_quant_perform_d = _lib.Rast_quant_perform_d
    Rast_quant_perform_d.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(CELL), c_int]
    Rast_quant_perform_d.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 496
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quant_perform_f'):
        continue
    Rast_quant_perform_f = _lib.Rast_quant_perform_f
    Rast_quant_perform_f.argtypes = [POINTER(struct_Quant), POINTER(FCELL), POINTER(CELL), c_int]
    Rast_quant_perform_f.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 497
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__quant_get_rule_for_d_raster_val'):
        continue
    Rast__quant_get_rule_for_d_raster_val = _lib.Rast__quant_get_rule_for_d_raster_val
    Rast__quant_get_rule_for_d_raster_val.argtypes = [POINTER(struct_Quant), DCELL]
    Rast__quant_get_rule_for_d_raster_val.restype = POINTER(struct_Quant_table)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 501
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__quant_import'):
        continue
    Rast__quant_import = _lib.Rast__quant_import
    Rast__quant_import.argtypes = [String, String, POINTER(struct_Quant)]
    Rast__quant_import.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 502
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__quant_export'):
        continue
    Rast__quant_export = _lib.Rast__quant_export
    Rast__quant_export.argtypes = [String, String, POINTER(struct_Quant)]
    Rast__quant_export.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 505
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_truncate_fp_map'):
        continue
    Rast_truncate_fp_map = _lib.Rast_truncate_fp_map
    Rast_truncate_fp_map.argtypes = [String, String]
    Rast_truncate_fp_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 506
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_round_fp_map'):
        continue
    Rast_round_fp_map = _lib.Rast_round_fp_map
    Rast_round_fp_map.argtypes = [String, String]
    Rast_round_fp_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 507
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quantize_fp_map'):
        continue
    Rast_quantize_fp_map = _lib.Rast_quantize_fp_map
    Rast_quantize_fp_map.argtypes = [String, String, CELL, CELL]
    Rast_quantize_fp_map.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 508
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_quantize_fp_map_range'):
        continue
    Rast_quantize_fp_map_range = _lib.Rast_quantize_fp_map_range
    Rast_quantize_fp_map_range.argtypes = [String, String, DCELL, DCELL, CELL, CELL]
    Rast_quantize_fp_map_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 510
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_quant'):
        continue
    Rast_write_quant = _lib.Rast_write_quant
    Rast_write_quant.argtypes = [String, String, POINTER(struct_Quant)]
    Rast_write_quant.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 511
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_quant'):
        continue
    Rast_read_quant = _lib.Rast_read_quant
    Rast_read_quant.argtypes = [String, String, POINTER(struct_Quant)]
    Rast_read_quant.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 514
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__remove_fp_range'):
        continue
    Rast__remove_fp_range = _lib.Rast__remove_fp_range
    Rast__remove_fp_range.argtypes = [String]
    Rast__remove_fp_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 515
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_construct_default_range'):
        continue
    Rast_construct_default_range = _lib.Rast_construct_default_range
    Rast_construct_default_range.argtypes = [POINTER(struct_Range)]
    Rast_construct_default_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 516
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_fp_range'):
        continue
    Rast_read_fp_range = _lib.Rast_read_fp_range
    Rast_read_fp_range.argtypes = [String, String, POINTER(struct_FPRange)]
    Rast_read_fp_range.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 517
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_range'):
        continue
    Rast_read_range = _lib.Rast_read_range
    Rast_read_range.argtypes = [String, String, POINTER(struct_Range)]
    Rast_read_range.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 518
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_range'):
        continue
    Rast_write_range = _lib.Rast_write_range
    Rast_write_range.argtypes = [String, POINTER(struct_Range)]
    Rast_write_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 519
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_fp_range'):
        continue
    Rast_write_fp_range = _lib.Rast_write_fp_range
    Rast_write_fp_range.argtypes = [String, POINTER(struct_FPRange)]
    Rast_write_fp_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 520
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_update_range'):
        continue
    Rast_update_range = _lib.Rast_update_range
    Rast_update_range.argtypes = [CELL, POINTER(struct_Range)]
    Rast_update_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 521
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_update_fp_range'):
        continue
    Rast_update_fp_range = _lib.Rast_update_fp_range
    Rast_update_fp_range.argtypes = [DCELL, POINTER(struct_FPRange)]
    Rast_update_fp_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 522
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_row_update_range'):
        continue
    Rast_row_update_range = _lib.Rast_row_update_range
    Rast_row_update_range.argtypes = [POINTER(CELL), c_int, POINTER(struct_Range)]
    Rast_row_update_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 523
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__row_update_range'):
        continue
    Rast__row_update_range = _lib.Rast__row_update_range
    Rast__row_update_range.argtypes = [POINTER(CELL), c_int, POINTER(struct_Range), c_int]
    Rast__row_update_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 524
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_row_update_fp_range'):
        continue
    Rast_row_update_fp_range = _lib.Rast_row_update_fp_range
    Rast_row_update_fp_range.argtypes = [POINTER(None), c_int, POINTER(struct_FPRange), RASTER_MAP_TYPE]
    Rast_row_update_fp_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 526
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_range'):
        continue
    Rast_init_range = _lib.Rast_init_range
    Rast_init_range.argtypes = [POINTER(struct_Range)]
    Rast_init_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 527
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_range_min_max'):
        continue
    Rast_get_range_min_max = _lib.Rast_get_range_min_max
    Rast_get_range_min_max.argtypes = [POINTER(struct_Range), POINTER(CELL), POINTER(CELL)]
    Rast_get_range_min_max.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 528
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_init_fp_range'):
        continue
    Rast_init_fp_range = _lib.Rast_init_fp_range
    Rast_init_fp_range.argtypes = [POINTER(struct_FPRange)]
    Rast_init_fp_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 529
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_fp_range_min_max'):
        continue
    Rast_get_fp_range_min_max = _lib.Rast_get_fp_range_min_max
    Rast_get_fp_range_min_max.argtypes = [POINTER(struct_FPRange), POINTER(DCELL), POINTER(DCELL)]
    Rast_get_fp_range_min_max.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 531
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_rstats'):
        continue
    Rast_read_rstats = _lib.Rast_read_rstats
    Rast_read_rstats.argtypes = [String, String, POINTER(struct_R_stats)]
    Rast_read_rstats.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 532
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_rstats'):
        continue
    Rast_write_rstats = _lib.Rast_write_rstats
    Rast_write_rstats.argtypes = [String, POINTER(struct_R_stats)]
    Rast_write_rstats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 535
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_raster_cmp'):
        continue
    Rast_raster_cmp = _lib.Rast_raster_cmp
    Rast_raster_cmp.argtypes = [POINTER(None), POINTER(None), RASTER_MAP_TYPE]
    Rast_raster_cmp.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 536
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_raster_cpy'):
        continue
    Rast_raster_cpy = _lib.Rast_raster_cpy
    Rast_raster_cpy.argtypes = [POINTER(None), POINTER(None), c_int, RASTER_MAP_TYPE]
    Rast_raster_cpy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 537
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_c_value'):
        continue
    Rast_set_c_value = _lib.Rast_set_c_value
    Rast_set_c_value.argtypes = [POINTER(None), CELL, RASTER_MAP_TYPE]
    Rast_set_c_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 538
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_f_value'):
        continue
    Rast_set_f_value = _lib.Rast_set_f_value
    Rast_set_f_value.argtypes = [POINTER(None), FCELL, RASTER_MAP_TYPE]
    Rast_set_f_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 539
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_d_value'):
        continue
    Rast_set_d_value = _lib.Rast_set_d_value
    Rast_set_d_value.argtypes = [POINTER(None), DCELL, RASTER_MAP_TYPE]
    Rast_set_d_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 540
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_c_value'):
        continue
    Rast_get_c_value = _lib.Rast_get_c_value
    Rast_get_c_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]
    Rast_get_c_value.restype = CELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 541
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_f_value'):
        continue
    Rast_get_f_value = _lib.Rast_get_f_value
    Rast_get_f_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]
    Rast_get_f_value.restype = FCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 542
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_d_value'):
        continue
    Rast_get_d_value = _lib.Rast_get_d_value
    Rast_get_d_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]
    Rast_get_d_value.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 545
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_units'):
        continue
    Rast_read_units = _lib.Rast_read_units
    Rast_read_units.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_read_units.restype = ReturnString
    else:
        Rast_read_units.restype = String
        Rast_read_units.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 546
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_read_vdatum'):
        continue
    Rast_read_vdatum = _lib.Rast_read_vdatum
    Rast_read_vdatum.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Rast_read_vdatum.restype = ReturnString
    else:
        Rast_read_vdatum.restype = String
        Rast_read_vdatum.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 547
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_units'):
        continue
    Rast_write_units = _lib.Rast_write_units
    Rast_write_units.argtypes = [String, String]
    Rast_write_units.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 548
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_write_vdatum'):
        continue
    Rast_write_vdatum = _lib.Rast_write_vdatum
    Rast_write_vdatum.argtypes = [String, String]
    Rast_write_vdatum.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 551
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_map_to_img_str'):
        continue
    Rast_map_to_img_str = _lib.Rast_map_to_img_str
    Rast_map_to_img_str.argtypes = [String, c_int, POINTER(c_ubyte)]
    Rast_map_to_img_str.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 554
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_is_reclass'):
        continue
    Rast_is_reclass = _lib.Rast_is_reclass
    Rast_is_reclass.argtypes = [String, String, String, String]
    Rast_is_reclass.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 555
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_is_reclassed_to'):
        continue
    Rast_is_reclassed_to = _lib.Rast_is_reclassed_to
    Rast_is_reclassed_to.argtypes = [String, String, POINTER(c_int), POINTER(POINTER(POINTER(c_char)))]
    Rast_is_reclassed_to.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 556
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_reclass'):
        continue
    Rast_get_reclass = _lib.Rast_get_reclass
    Rast_get_reclass.argtypes = [String, String, POINTER(struct_Reclass)]
    Rast_get_reclass.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 557
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_free_reclass'):
        continue
    Rast_free_reclass = _lib.Rast_free_reclass
    Rast_free_reclass.argtypes = [POINTER(struct_Reclass)]
    Rast_free_reclass.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 558
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_put_reclass'):
        continue
    Rast_put_reclass = _lib.Rast_put_reclass
    Rast_put_reclass.argtypes = [String, POINTER(struct_Reclass)]
    Rast_put_reclass.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 561
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_sample_nearest'):
        continue
    Rast_get_sample_nearest = _lib.Rast_get_sample_nearest
    Rast_get_sample_nearest.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int]
    Rast_get_sample_nearest.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 562
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_sample_bilinear'):
        continue
    Rast_get_sample_bilinear = _lib.Rast_get_sample_bilinear
    Rast_get_sample_bilinear.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int]
    Rast_get_sample_bilinear.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 563
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_sample_cubic'):
        continue
    Rast_get_sample_cubic = _lib.Rast_get_sample_cubic
    Rast_get_sample_cubic.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int]
    Rast_get_sample_cubic.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 564
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_sample'):
        continue
    Rast_get_sample = _lib.Rast_get_sample
    Rast_get_sample.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int, INTERP_TYPE]
    Rast_get_sample.restype = DCELL
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 567
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__init_window'):
        continue
    Rast__init_window = _lib.Rast__init_window
    Rast__init_window.argtypes = []
    Rast__init_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 568
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_window'):
        continue
    Rast_set_window = _lib.Rast_set_window
    Rast_set_window.argtypes = [POINTER(struct_Cell_head)]
    Rast_set_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 569
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_unset_window'):
        continue
    Rast_unset_window = _lib.Rast_unset_window
    Rast_unset_window.argtypes = []
    Rast_unset_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 570
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_output_window'):
        continue
    Rast_set_output_window = _lib.Rast_set_output_window
    Rast_set_output_window.argtypes = [POINTER(struct_Cell_head)]
    Rast_set_output_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 571
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_set_input_window'):
        continue
    Rast_set_input_window = _lib.Rast_set_input_window
    Rast_set_input_window.argtypes = [POINTER(struct_Cell_head)]
    Rast_set_input_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 574
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_vrt'):
        continue
    Rast_get_vrt = _lib.Rast_get_vrt
    Rast_get_vrt.argtypes = [String, String]
    Rast_get_vrt.restype = POINTER(struct_R_vrt)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 575
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_close_vrt'):
        continue
    Rast_close_vrt = _lib.Rast_close_vrt
    Rast_close_vrt.argtypes = [POINTER(struct_R_vrt)]
    Rast_close_vrt.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 576
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_vrt_row'):
        continue
    Rast_get_vrt_row = _lib.Rast_get_vrt_row
    Rast_get_vrt_row.argtypes = [c_int, POINTER(None), c_int, RASTER_MAP_TYPE]
    Rast_get_vrt_row.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 579
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_window'):
        continue
    Rast_get_window = _lib.Rast_get_window
    Rast_get_window.argtypes = [POINTER(struct_Cell_head)]
    Rast_get_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 580
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_input_window'):
        continue
    Rast_get_input_window = _lib.Rast_get_input_window
    Rast_get_input_window.argtypes = [POINTER(struct_Cell_head)]
    Rast_get_input_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 581
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_get_output_window'):
        continue
    Rast_get_output_window = _lib.Rast_get_output_window
    Rast_get_output_window.argtypes = [POINTER(struct_Cell_head)]
    Rast_get_output_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 582
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_window_rows'):
        continue
    Rast_window_rows = _lib.Rast_window_rows
    Rast_window_rows.argtypes = []
    Rast_window_rows.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 583
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_window_cols'):
        continue
    Rast_window_cols = _lib.Rast_window_cols
    Rast_window_cols.argtypes = []
    Rast_window_cols.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 584
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_input_window_rows'):
        continue
    Rast_input_window_rows = _lib.Rast_input_window_rows
    Rast_input_window_rows.argtypes = []
    Rast_input_window_rows.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 585
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_input_window_cols'):
        continue
    Rast_input_window_cols = _lib.Rast_input_window_cols
    Rast_input_window_cols.argtypes = []
    Rast_input_window_cols.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 586
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_output_window_rows'):
        continue
    Rast_output_window_rows = _lib.Rast_output_window_rows
    Rast_output_window_rows.argtypes = []
    Rast_output_window_rows.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 587
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_output_window_cols'):
        continue
    Rast_output_window_cols = _lib.Rast_output_window_cols
    Rast_output_window_cols.argtypes = []
    Rast_output_window_cols.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 588
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_northing_to_row'):
        continue
    Rast_northing_to_row = _lib.Rast_northing_to_row
    Rast_northing_to_row.argtypes = [c_double, POINTER(struct_Cell_head)]
    Rast_northing_to_row.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 589
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_easting_to_col'):
        continue
    Rast_easting_to_col = _lib.Rast_easting_to_col
    Rast_easting_to_col.argtypes = [c_double, POINTER(struct_Cell_head)]
    Rast_easting_to_col.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 590
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_row_to_northing'):
        continue
    Rast_row_to_northing = _lib.Rast_row_to_northing
    Rast_row_to_northing.argtypes = [c_double, POINTER(struct_Cell_head)]
    Rast_row_to_northing.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 591
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_col_to_easting'):
        continue
    Rast_col_to_easting = _lib.Rast_col_to_easting
    Rast_col_to_easting.argtypes = [c_double, POINTER(struct_Cell_head)]
    Rast_col_to_easting.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 594
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast__create_window_mapping'):
        continue
    Rast__create_window_mapping = _lib.Rast__create_window_mapping
    Rast__create_window_mapping.argtypes = [c_int]
    Rast__create_window_mapping.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 595
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_row_repeat_nomask'):
        continue
    Rast_row_repeat_nomask = _lib.Rast_row_repeat_nomask
    Rast_row_repeat_nomask.argtypes = [c_int, c_int]
    Rast_row_repeat_nomask.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 598
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_zero_buf'):
        continue
    Rast_zero_buf = _lib.Rast_zero_buf
    Rast_zero_buf.argtypes = [POINTER(None), RASTER_MAP_TYPE]
    Rast_zero_buf.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 599
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_zero_input_buf'):
        continue
    Rast_zero_input_buf = _lib.Rast_zero_input_buf
    Rast_zero_input_buf.argtypes = [POINTER(None), RASTER_MAP_TYPE]
    Rast_zero_input_buf.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 600
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Rast_zero_output_buf'):
        continue
    Rast_zero_output_buf = _lib.Rast_zero_output_buf
    Rast_zero_output_buf.argtypes = [POINTER(None), RASTER_MAP_TYPE]
    Rast_zero_output_buf.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 7
try:
    RECLASS_TABLE = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 8
try:
    RECLASS_RULES = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 9
try:
    RECLASS_SCALE = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 11
try:
    CELL_TYPE = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 12
try:
    FCELL_TYPE = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 13
try:
    DCELL_TYPE = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 19
try:
    INTERP_UNKNOWN = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 20
try:
    INTERP_NEAREST = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 21
try:
    INTERP_BILINEAR = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 22
try:
    INTERP_BICUBIC = 3
except:
    pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 410
def Rast_is_c_null_value(cellVal):
    return ((cellVal[0]) == 2147483648)

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 412
def Rast_is_f_null_value(fcellVal):
    return ((fcellVal[0]) != (fcellVal[0]))

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/raster.h: 414
def Rast_is_d_null_value(dcellVal):
    return ((dcellVal[0]) != (dcellVal[0]))

Reclass = struct_Reclass # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 31

FPReclass_table = struct_FPReclass_table # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 42

FPReclass = struct_FPReclass # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 52

Quant_table = struct_Quant_table # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 76

Quant = struct_Quant # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 84

Categories = struct_Categories # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 127

History = struct_History # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 180

Cell_stats_node = struct_Cell_stats_node # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 192

Cell_stats = struct_Cell_stats # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 190

Histogram_list = struct_Histogram_list # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 211

Histogram = struct_Histogram # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 207

R_stats = struct_R_stats # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 218

Range = struct_Range # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 225

FPRange = struct_FPRange # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 233

FP_stats = struct_FP_stats # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 241

GDAL_link = struct_GDAL_link # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 251

R_vrt = struct_R_vrt # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\raster.h: 252

# No inserted files

