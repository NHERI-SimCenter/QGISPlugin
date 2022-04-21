'''Wrapper for imagery.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_imagery.7.8 D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/imagery.h D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h -o OBJ.x86_64-w64-mingw32/imagery.py

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

_libs["grass_imagery.7.8"] = load_library("grass_imagery.7.8")

# 1 libraries
# End libraries

# No modules

# D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/stdio.h: 33
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

FILE = struct__iobuf # D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/stdio.h: 47

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/gis.h: 413
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

CELL = c_int # D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/gis.h: 603

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 10
class struct_Ref_Color(Structure):
    pass

struct_Ref_Color.__slots__ = [
    'table',
    'index',
    'buf',
    'fd',
    'min',
    'max',
    'n',
]
struct_Ref_Color._fields_ = [
    ('table', POINTER(c_ubyte)),
    ('index', POINTER(c_ubyte)),
    ('buf', POINTER(c_ubyte)),
    ('fd', c_int),
    ('min', CELL),
    ('max', CELL),
    ('n', c_int),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 20
class struct_Ref_Files(Structure):
    pass

struct_Ref_Files.__slots__ = [
    'name',
    'mapset',
]
struct_Ref_Files._fields_ = [
    ('name', c_char * 256),
    ('mapset', c_char * 256),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 26
class struct_Ref(Structure):
    pass

struct_Ref.__slots__ = [
    'nfiles',
    'file',
    'red',
    'grn',
    'blu',
]
struct_Ref._fields_ = [
    ('nfiles', c_int),
    ('file', POINTER(struct_Ref_Files)),
    ('red', struct_Ref_Color),
    ('grn', struct_Ref_Color),
    ('blu', struct_Ref_Color),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 33
class struct_Tape_Info(Structure):
    pass

struct_Tape_Info.__slots__ = [
    'title',
    'id',
    'desc',
]
struct_Tape_Info._fields_ = [
    ('title', c_char * 75),
    ('id', (c_char * 75) * 2),
    ('desc', (c_char * 75) * 5),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 40
class struct_Control_Points(Structure):
    pass

struct_Control_Points.__slots__ = [
    'count',
    'e1',
    'n1',
    'z1',
    'e2',
    'n2',
    'z2',
    'status',
]
struct_Control_Points._fields_ = [
    ('count', c_int),
    ('e1', POINTER(c_double)),
    ('n1', POINTER(c_double)),
    ('z1', POINTER(c_double)),
    ('e2', POINTER(c_double)),
    ('n2', POINTER(c_double)),
    ('z2', POINTER(c_double)),
    ('status', POINTER(c_int)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 52
class struct_One_Sig(Structure):
    pass

struct_One_Sig.__slots__ = [
    'desc',
    'npoints',
    'mean',
    'var',
    'status',
    'r',
    'g',
    'b',
    'have_color',
]
struct_One_Sig._fields_ = [
    ('desc', c_char * 100),
    ('npoints', c_int),
    ('mean', POINTER(c_double)),
    ('var', POINTER(POINTER(c_double))),
    ('status', c_int),
    ('r', c_float),
    ('g', c_float),
    ('b', c_float),
    ('have_color', c_int),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 63
class struct_Signature(Structure):
    pass

struct_Signature.__slots__ = [
    'nbands',
    'nsigs',
    'title',
    'sig',
]
struct_Signature._fields_ = [
    ('nbands', c_int),
    ('nsigs', c_int),
    ('title', c_char * 100),
    ('sig', POINTER(struct_One_Sig)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 71
class struct_SubSig(Structure):
    pass

struct_SubSig.__slots__ = [
    'N',
    'pi',
    'means',
    'R',
    'Rinv',
    'cnst',
    'used',
]
struct_SubSig._fields_ = [
    ('N', c_double),
    ('pi', c_double),
    ('means', POINTER(c_double)),
    ('R', POINTER(POINTER(c_double))),
    ('Rinv', POINTER(POINTER(c_double))),
    ('cnst', c_double),
    ('used', c_int),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 82
class struct_ClassData(Structure):
    pass

struct_ClassData.__slots__ = [
    'npixels',
    'count',
    'x',
    'p',
]
struct_ClassData._fields_ = [
    ('npixels', c_int),
    ('count', c_int),
    ('x', POINTER(POINTER(c_double))),
    ('p', POINTER(POINTER(c_double))),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 90
class struct_ClassSig(Structure):
    pass

struct_ClassSig.__slots__ = [
    'classnum',
    'title',
    'used',
    'type',
    'nsubclasses',
    'SubSig',
    'ClassData',
]
struct_ClassSig._fields_ = [
    ('classnum', c_long),
    ('title', String),
    ('used', c_int),
    ('type', c_int),
    ('nsubclasses', c_int),
    ('SubSig', POINTER(struct_SubSig)),
    ('ClassData', struct_ClassData),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 101
class struct_SigSet(Structure):
    pass

struct_SigSet.__slots__ = [
    'nbands',
    'nclasses',
    'title',
    'ClassSig',
]
struct_SigSet._fields_ = [
    ('nbands', c_int),
    ('nclasses', c_int),
    ('title', String),
    ('ClassSig', POINTER(struct_ClassSig)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 138
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'cat',
    'name',
    'color',
    'nbands',
    'ncells',
    'band_min',
    'band_max',
    'band_sum',
    'band_mean',
    'band_stddev',
    'band_product',
    'band_histo',
    'band_range_min',
    'band_range_max',
    'nstd',
]
struct_anon_8._fields_ = [
    ('cat', c_int),
    ('name', String),
    ('color', String),
    ('nbands', c_int),
    ('ncells', c_int),
    ('band_min', POINTER(c_int)),
    ('band_max', POINTER(c_int)),
    ('band_sum', POINTER(c_float)),
    ('band_mean', POINTER(c_float)),
    ('band_stddev', POINTER(c_float)),
    ('band_product', POINTER(POINTER(c_float))),
    ('band_histo', POINTER(POINTER(c_int))),
    ('band_range_min', POINTER(c_int)),
    ('band_range_max', POINTER(c_int)),
    ('nstd', c_float),
]

IClass_statistics = struct_anon_8 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 138

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 171
class struct_scScatts(Structure):
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 149
class struct_scCats(Structure):
    pass

struct_scCats.__slots__ = [
    'type',
    'n_cats',
    'n_bands',
    'n_scatts',
    'n_a_cats',
    'cats_ids',
    'cats_idxs',
    'cats_arr',
]
struct_scCats._fields_ = [
    ('type', c_int),
    ('n_cats', c_int),
    ('n_bands', c_int),
    ('n_scatts', c_int),
    ('n_a_cats', c_int),
    ('cats_ids', POINTER(c_int)),
    ('cats_idxs', POINTER(c_int)),
    ('cats_arr', POINTER(POINTER(struct_scScatts))),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 186
class struct_scdScattData(Structure):
    pass

struct_scScatts.__slots__ = [
    'n_a_scatts',
    'scatts_bands',
    'scatt_idxs',
    'scatts_arr',
]
struct_scScatts._fields_ = [
    ('n_a_scatts', c_int),
    ('scatts_bands', POINTER(c_int)),
    ('scatt_idxs', POINTER(c_int)),
    ('scatts_arr', POINTER(POINTER(struct_scdScattData))),
]

struct_scdScattData.__slots__ = [
    'n_vals',
    'b_conds_arr',
    'scatt_vals_arr',
]
struct_scdScattData._fields_ = [
    ('n_vals', c_int),
    ('b_conds_arr', POINTER(c_ubyte)),
    ('scatt_vals_arr', POINTER(c_uint)),
]

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_malloc'):
        continue
    I_malloc = _lib.I_malloc
    I_malloc.argtypes = [c_size_t]
    I_malloc.restype = POINTER(c_ubyte)
    I_malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_realloc'):
        continue
    I_realloc = _lib.I_realloc
    I_realloc.argtypes = [POINTER(None), c_size_t]
    I_realloc.restype = POINTER(c_ubyte)
    I_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_free'):
        continue
    I_free = _lib.I_free
    I_free.argtypes = [POINTER(None)]
    I_free.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_alloc_double2'):
        continue
    I_alloc_double2 = _lib.I_alloc_double2
    I_alloc_double2.argtypes = [c_int, c_int]
    I_alloc_double2.restype = POINTER(POINTER(c_double))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_alloc_int'):
        continue
    I_alloc_int = _lib.I_alloc_int
    I_alloc_int.argtypes = [c_int]
    I_alloc_int.restype = POINTER(c_int)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_alloc_int2'):
        continue
    I_alloc_int2 = _lib.I_alloc_int2
    I_alloc_int2.argtypes = [c_int, c_int]
    I_alloc_int2.restype = POINTER(POINTER(c_int))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_free_int2'):
        continue
    I_free_int2 = _lib.I_free_int2
    I_free_int2.argtypes = [POINTER(POINTER(c_int))]
    I_free_int2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_free_double2'):
        continue
    I_free_double2 = _lib.I_free_double2
    I_free_double2.argtypes = [POINTER(POINTER(c_double))]
    I_free_double2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_alloc_double3'):
        continue
    I_alloc_double3 = _lib.I_alloc_double3
    I_alloc_double3.argtypes = [c_int, c_int, c_int]
    I_alloc_double3.restype = POINTER(POINTER(POINTER(c_double)))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_free_double3'):
        continue
    I_free_double3 = _lib.I_free_double3
    I_free_double3.argtypes = [POINTER(POINTER(POINTER(c_double)))]
    I_free_double3.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_to_eol'):
        continue
    I_get_to_eol = _lib.I_get_to_eol
    I_get_to_eol.argtypes = [String, c_int, POINTER(FILE)]
    I_get_to_eol.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_group'):
        continue
    I_find_group = _lib.I_find_group
    I_find_group.argtypes = [String]
    I_find_group.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_group2'):
        continue
    I_find_group2 = _lib.I_find_group2
    I_find_group2.argtypes = [String, String]
    I_find_group2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_group_file'):
        continue
    I_find_group_file = _lib.I_find_group_file
    I_find_group_file.argtypes = [String, String]
    I_find_group_file.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_group_file2'):
        continue
    I_find_group_file2 = _lib.I_find_group_file2
    I_find_group_file2.argtypes = [String, String, String]
    I_find_group_file2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_subgroup'):
        continue
    I_find_subgroup = _lib.I_find_subgroup
    I_find_subgroup.argtypes = [String, String]
    I_find_subgroup.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_subgroup2'):
        continue
    I_find_subgroup2 = _lib.I_find_subgroup2
    I_find_subgroup2.argtypes = [String, String, String]
    I_find_subgroup2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 26
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_subgroup_file'):
        continue
    I_find_subgroup_file = _lib.I_find_subgroup_file
    I_find_subgroup_file.argtypes = [String, String, String]
    I_find_subgroup_file.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 27
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_subgroup_file2'):
        continue
    I_find_subgroup_file2 = _lib.I_find_subgroup_file2
    I_find_subgroup_file2.argtypes = [String, String, String, String]
    I_find_subgroup_file2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 28
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_find_signature_file'):
        continue
    I_find_signature_file = _lib.I_find_signature_file
    I_find_signature_file.argtypes = [String, String, String, String]
    I_find_signature_file.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 31
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_group_file_new'):
        continue
    I_fopen_group_file_new = _lib.I_fopen_group_file_new
    I_fopen_group_file_new.argtypes = [String, String]
    I_fopen_group_file_new.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 32
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_group_file_append'):
        continue
    I_fopen_group_file_append = _lib.I_fopen_group_file_append
    I_fopen_group_file_append.argtypes = [String, String]
    I_fopen_group_file_append.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_group_file_old'):
        continue
    I_fopen_group_file_old = _lib.I_fopen_group_file_old
    I_fopen_group_file_old.argtypes = [String, String]
    I_fopen_group_file_old.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_group_file_old2'):
        continue
    I_fopen_group_file_old2 = _lib.I_fopen_group_file_old2
    I_fopen_group_file_old2.argtypes = [String, String, String]
    I_fopen_group_file_old2.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 35
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_subgroup_file_new'):
        continue
    I_fopen_subgroup_file_new = _lib.I_fopen_subgroup_file_new
    I_fopen_subgroup_file_new.argtypes = [String, String, String]
    I_fopen_subgroup_file_new.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 36
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_subgroup_file_append'):
        continue
    I_fopen_subgroup_file_append = _lib.I_fopen_subgroup_file_append
    I_fopen_subgroup_file_append.argtypes = [String, String, String]
    I_fopen_subgroup_file_append.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 37
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_subgroup_file_old'):
        continue
    I_fopen_subgroup_file_old = _lib.I_fopen_subgroup_file_old
    I_fopen_subgroup_file_old.argtypes = [String, String, String]
    I_fopen_subgroup_file_old.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 38
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_subgroup_file_old2'):
        continue
    I_fopen_subgroup_file_old2 = _lib.I_fopen_subgroup_file_old2
    I_fopen_subgroup_file_old2.argtypes = [String, String, String, String]
    I_fopen_subgroup_file_old2.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 41
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_compute_georef_equations'):
        continue
    I_compute_georef_equations = _lib.I_compute_georef_equations
    I_compute_georef_equations.argtypes = [POINTER(struct_Control_Points), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    I_compute_georef_equations.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_georef'):
        continue
    I_georef = _lib.I_georef
    I_georef.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    I_georef.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_compute_georef_equations_tps'):
        continue
    I_compute_georef_equations_tps = _lib.I_compute_georef_equations_tps
    I_compute_georef_equations_tps.argtypes = [POINTER(struct_Control_Points), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(POINTER(c_double))]
    I_compute_georef_equations_tps.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 48
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_georef_tps'):
        continue
    I_georef_tps = _lib.I_georef_tps
    I_georef_tps.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_Control_Points), c_int]
    I_georef_tps.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 52
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_group'):
        continue
    I_get_group = _lib.I_get_group
    I_get_group.argtypes = [String]
    I_get_group.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_put_group'):
        continue
    I_put_group = _lib.I_put_group
    I_put_group.argtypes = [String]
    I_put_group.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 54
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_subgroup'):
        continue
    I_get_subgroup = _lib.I_get_subgroup
    I_get_subgroup.argtypes = [String, String]
    I_get_subgroup.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_put_subgroup'):
        continue
    I_put_subgroup = _lib.I_put_subgroup
    I_put_subgroup.argtypes = [String, String]
    I_put_subgroup.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 56
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_group_ref'):
        continue
    I_get_group_ref = _lib.I_get_group_ref
    I_get_group_ref.argtypes = [String, POINTER(struct_Ref)]
    I_get_group_ref.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_group_ref2'):
        continue
    I_get_group_ref2 = _lib.I_get_group_ref2
    I_get_group_ref2.argtypes = [String, String, POINTER(struct_Ref)]
    I_get_group_ref2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 58
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_subgroup_ref'):
        continue
    I_get_subgroup_ref = _lib.I_get_subgroup_ref
    I_get_subgroup_ref.argtypes = [String, String, POINTER(struct_Ref)]
    I_get_subgroup_ref.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_subgroup_ref2'):
        continue
    I_get_subgroup_ref2 = _lib.I_get_subgroup_ref2
    I_get_subgroup_ref2.argtypes = [String, String, String, POINTER(struct_Ref)]
    I_get_subgroup_ref2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 60
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_init_ref_color_nums'):
        continue
    I_init_ref_color_nums = _lib.I_init_ref_color_nums
    I_init_ref_color_nums.argtypes = [POINTER(struct_Ref)]
    I_init_ref_color_nums.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_put_group_ref'):
        continue
    I_put_group_ref = _lib.I_put_group_ref
    I_put_group_ref.argtypes = [String, POINTER(struct_Ref)]
    I_put_group_ref.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 62
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_put_subgroup_ref'):
        continue
    I_put_subgroup_ref = _lib.I_put_subgroup_ref
    I_put_subgroup_ref.argtypes = [String, String, POINTER(struct_Ref)]
    I_put_subgroup_ref.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_add_file_to_group_ref'):
        continue
    I_add_file_to_group_ref = _lib.I_add_file_to_group_ref
    I_add_file_to_group_ref.argtypes = [String, String, POINTER(struct_Ref)]
    I_add_file_to_group_ref.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 64
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_transfer_group_ref_file'):
        continue
    I_transfer_group_ref_file = _lib.I_transfer_group_ref_file
    I_transfer_group_ref_file.argtypes = [POINTER(struct_Ref), c_int, POINTER(struct_Ref)]
    I_transfer_group_ref_file.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_init_group_ref'):
        continue
    I_init_group_ref = _lib.I_init_group_ref
    I_init_group_ref.argtypes = [POINTER(struct_Ref)]
    I_init_group_ref.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_free_group_ref'):
        continue
    I_free_group_ref = _lib.I_free_group_ref
    I_free_group_ref.argtypes = [POINTER(struct_Ref)]
    I_free_group_ref.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 69
class struct_Map_info(Structure):
    pass

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 70
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_analysis'):
        continue
    I_iclass_analysis = _lib.I_iclass_analysis
    I_iclass_analysis.argtypes = [POINTER(IClass_statistics), POINTER(struct_Ref), POINTER(struct_Map_info), String, String, String]
    I_iclass_analysis.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 71
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_init_group'):
        continue
    I_iclass_init_group = _lib.I_iclass_init_group
    I_iclass_init_group.argtypes = [String, String, POINTER(struct_Ref)]
    I_iclass_init_group.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_create_raster'):
        continue
    I_iclass_create_raster = _lib.I_iclass_create_raster
    I_iclass_create_raster.argtypes = [POINTER(IClass_statistics), POINTER(struct_Ref), String]
    I_iclass_create_raster.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 75
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_nbands'):
        continue
    I_iclass_statistics_get_nbands = _lib.I_iclass_statistics_get_nbands
    I_iclass_statistics_get_nbands.argtypes = [POINTER(IClass_statistics), POINTER(c_int)]
    I_iclass_statistics_get_nbands.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 76
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_cat'):
        continue
    I_iclass_statistics_get_cat = _lib.I_iclass_statistics_get_cat
    I_iclass_statistics_get_cat.argtypes = [POINTER(IClass_statistics), POINTER(c_int)]
    I_iclass_statistics_get_cat.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 77
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_name'):
        continue
    I_iclass_statistics_get_name = _lib.I_iclass_statistics_get_name
    I_iclass_statistics_get_name.argtypes = [POINTER(IClass_statistics), POINTER(POINTER(c_char))]
    I_iclass_statistics_get_name.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 78
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_color'):
        continue
    I_iclass_statistics_get_color = _lib.I_iclass_statistics_get_color
    I_iclass_statistics_get_color.argtypes = [POINTER(IClass_statistics), POINTER(POINTER(c_char))]
    I_iclass_statistics_get_color.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 79
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_ncells'):
        continue
    I_iclass_statistics_get_ncells = _lib.I_iclass_statistics_get_ncells
    I_iclass_statistics_get_ncells.argtypes = [POINTER(IClass_statistics), POINTER(c_int)]
    I_iclass_statistics_get_ncells.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 80
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_max'):
        continue
    I_iclass_statistics_get_max = _lib.I_iclass_statistics_get_max
    I_iclass_statistics_get_max.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_max.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_range_max'):
        continue
    I_iclass_statistics_get_range_max = _lib.I_iclass_statistics_get_range_max
    I_iclass_statistics_get_range_max.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_range_max.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 82
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_min'):
        continue
    I_iclass_statistics_get_min = _lib.I_iclass_statistics_get_min
    I_iclass_statistics_get_min.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_min.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 83
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_range_min'):
        continue
    I_iclass_statistics_get_range_min = _lib.I_iclass_statistics_get_range_min
    I_iclass_statistics_get_range_min.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_range_min.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_sum'):
        continue
    I_iclass_statistics_get_sum = _lib.I_iclass_statistics_get_sum
    I_iclass_statistics_get_sum.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_float)]
    I_iclass_statistics_get_sum.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_mean'):
        continue
    I_iclass_statistics_get_mean = _lib.I_iclass_statistics_get_mean
    I_iclass_statistics_get_mean.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_float)]
    I_iclass_statistics_get_mean.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_stddev'):
        continue
    I_iclass_statistics_get_stddev = _lib.I_iclass_statistics_get_stddev
    I_iclass_statistics_get_stddev.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_float)]
    I_iclass_statistics_get_stddev.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_nstd'):
        continue
    I_iclass_statistics_get_nstd = _lib.I_iclass_statistics_get_nstd
    I_iclass_statistics_get_nstd.argtypes = [POINTER(IClass_statistics), POINTER(c_float)]
    I_iclass_statistics_get_nstd.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 88
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_set_nstd'):
        continue
    I_iclass_statistics_set_nstd = _lib.I_iclass_statistics_set_nstd
    I_iclass_statistics_set_nstd.argtypes = [POINTER(IClass_statistics), c_float]
    I_iclass_statistics_set_nstd.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 89
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_histo'):
        continue
    I_iclass_statistics_get_histo = _lib.I_iclass_statistics_get_histo
    I_iclass_statistics_get_histo.argtypes = [POINTER(IClass_statistics), c_int, c_int, POINTER(c_int)]
    I_iclass_statistics_get_histo.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 90
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_statistics_get_product'):
        continue
    I_iclass_statistics_get_product = _lib.I_iclass_statistics_get_product
    I_iclass_statistics_get_product.argtypes = [POINTER(IClass_statistics), c_int, c_int, POINTER(c_float)]
    I_iclass_statistics_get_product.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 91
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_init_statistics'):
        continue
    I_iclass_init_statistics = _lib.I_iclass_init_statistics
    I_iclass_init_statistics.argtypes = [POINTER(IClass_statistics), c_int, String, String, c_float]
    I_iclass_init_statistics.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 92
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_free_statistics'):
        continue
    I_iclass_free_statistics = _lib.I_iclass_free_statistics
    I_iclass_free_statistics.argtypes = [POINTER(IClass_statistics)]
    I_iclass_free_statistics.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 95
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_init_signatures'):
        continue
    I_iclass_init_signatures = _lib.I_iclass_init_signatures
    I_iclass_init_signatures.argtypes = [POINTER(struct_Signature), POINTER(struct_Ref)]
    I_iclass_init_signatures.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_add_signature'):
        continue
    I_iclass_add_signature = _lib.I_iclass_add_signature
    I_iclass_add_signature.argtypes = [POINTER(struct_Signature), POINTER(IClass_statistics)]
    I_iclass_add_signature.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 97
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_iclass_write_signatures'):
        continue
    I_iclass_write_signatures = _lib.I_iclass_write_signatures
    I_iclass_write_signatures.argtypes = [POINTER(struct_Signature), String, String, String]
    I_iclass_write_signatures.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 100
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_list_group'):
        continue
    I_list_group = _lib.I_list_group
    I_list_group.argtypes = [String, POINTER(struct_Ref), POINTER(FILE)]
    I_list_group.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 101
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_list_group_simple'):
        continue
    I_list_group_simple = _lib.I_list_group_simple
    I_list_group_simple.argtypes = [POINTER(struct_Ref), POINTER(FILE)]
    I_list_group_simple.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 104
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_list_subgroups'):
        continue
    I_list_subgroups = _lib.I_list_subgroups
    I_list_subgroups.argtypes = [String, POINTER(c_int)]
    I_list_subgroups.restype = POINTER(POINTER(c_char))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 105
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_list_subgroups2'):
        continue
    I_list_subgroups2 = _lib.I_list_subgroups2
    I_list_subgroups2.argtypes = [String, String, POINTER(c_int)]
    I_list_subgroups2.restype = POINTER(POINTER(c_char))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 106
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_list_subgroup'):
        continue
    I_list_subgroup = _lib.I_list_subgroup
    I_list_subgroup.argtypes = [String, String, POINTER(struct_Ref), POINTER(FILE)]
    I_list_subgroup.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 107
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_list_subgroup_simple'):
        continue
    I_list_subgroup_simple = _lib.I_list_subgroup_simple
    I_list_subgroup_simple.argtypes = [POINTER(struct_Ref), POINTER(FILE)]
    I_list_subgroup_simple.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 110
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_location_info'):
        continue
    I_location_info = _lib.I_location_info
    I_location_info.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        I_location_info.restype = ReturnString
    else:
        I_location_info.restype = String
        I_location_info.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 113
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_new_control_point'):
        continue
    I_new_control_point = _lib.I_new_control_point
    I_new_control_point.argtypes = [POINTER(struct_Control_Points), c_double, c_double, c_double, c_double, c_int]
    I_new_control_point.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 115
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_control_points'):
        continue
    I_get_control_points = _lib.I_get_control_points
    I_get_control_points.argtypes = [String, POINTER(struct_Control_Points)]
    I_get_control_points.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 116
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_put_control_points'):
        continue
    I_put_control_points = _lib.I_put_control_points
    I_put_control_points.argtypes = [String, POINTER(struct_Control_Points)]
    I_put_control_points.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 119
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_group_ref_new'):
        continue
    I_fopen_group_ref_new = _lib.I_fopen_group_ref_new
    I_fopen_group_ref_new.argtypes = [String]
    I_fopen_group_ref_new.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 120
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_group_ref_old'):
        continue
    I_fopen_group_ref_old = _lib.I_fopen_group_ref_old
    I_fopen_group_ref_old.argtypes = [String]
    I_fopen_group_ref_old.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 121
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_group_ref_old2'):
        continue
    I_fopen_group_ref_old2 = _lib.I_fopen_group_ref_old2
    I_fopen_group_ref_old2.argtypes = [String, String]
    I_fopen_group_ref_old2.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 122
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_subgroup_ref_new'):
        continue
    I_fopen_subgroup_ref_new = _lib.I_fopen_subgroup_ref_new
    I_fopen_subgroup_ref_new.argtypes = [String, String]
    I_fopen_subgroup_ref_new.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 123
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_subgroup_ref_old'):
        continue
    I_fopen_subgroup_ref_old = _lib.I_fopen_subgroup_ref_old
    I_fopen_subgroup_ref_old.argtypes = [String, String]
    I_fopen_subgroup_ref_old.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 124
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_subgroup_ref_old2'):
        continue
    I_fopen_subgroup_ref_old2 = _lib.I_fopen_subgroup_ref_old2
    I_fopen_subgroup_ref_old2.argtypes = [String, String, String]
    I_fopen_subgroup_ref_old2.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 127
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_sc_init_cats'):
        continue
    I_sc_init_cats = _lib.I_sc_init_cats
    I_sc_init_cats.argtypes = [POINTER(struct_scCats), c_int, c_int]
    I_sc_init_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 128
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_sc_free_cats'):
        continue
    I_sc_free_cats = _lib.I_sc_free_cats
    I_sc_free_cats.argtypes = [POINTER(struct_scCats)]
    I_sc_free_cats.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 129
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_sc_add_cat'):
        continue
    I_sc_add_cat = _lib.I_sc_add_cat
    I_sc_add_cat.argtypes = [POINTER(struct_scCats)]
    I_sc_add_cat.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 130
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_sc_insert_scatt_data'):
        continue
    I_sc_insert_scatt_data = _lib.I_sc_insert_scatt_data
    I_sc_insert_scatt_data.argtypes = [POINTER(struct_scCats), POINTER(struct_scdScattData), c_int, c_int]
    I_sc_insert_scatt_data.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 132
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_scd_init_scatt_data'):
        continue
    I_scd_init_scatt_data = _lib.I_scd_init_scatt_data
    I_scd_init_scatt_data.argtypes = [POINTER(struct_scdScattData), c_int, c_int, POINTER(None)]
    I_scd_init_scatt_data.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 135
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_compute_scatts'):
        continue
    I_compute_scatts = _lib.I_compute_scatts
    I_compute_scatts.argtypes = [POINTER(struct_Cell_head), POINTER(struct_scCats), POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), c_int, POINTER(struct_scCats), POINTER(POINTER(c_char))]
    I_compute_scatts.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 138
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_create_cat_rast'):
        continue
    I_create_cat_rast = _lib.I_create_cat_rast
    I_create_cat_rast.argtypes = [POINTER(struct_Cell_head), String]
    I_create_cat_rast.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 139
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_insert_patch_to_cat_rast'):
        continue
    I_insert_patch_to_cat_rast = _lib.I_insert_patch_to_cat_rast
    I_insert_patch_to_cat_rast.argtypes = [String, POINTER(struct_Cell_head), String]
    I_insert_patch_to_cat_rast.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 141
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_id_scatt_to_bands'):
        continue
    I_id_scatt_to_bands = _lib.I_id_scatt_to_bands
    I_id_scatt_to_bands.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int)]
    I_id_scatt_to_bands.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 142
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_bands_to_id_scatt'):
        continue
    I_bands_to_id_scatt = _lib.I_bands_to_id_scatt
    I_bands_to_id_scatt.argtypes = [c_int, c_int, c_int, POINTER(c_int)]
    I_bands_to_id_scatt.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 144
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_merge_arrays'):
        continue
    I_merge_arrays = _lib.I_merge_arrays
    I_merge_arrays.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_uint, c_double]
    I_merge_arrays.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 145
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_apply_colormap'):
        continue
    I_apply_colormap = _lib.I_apply_colormap
    I_apply_colormap.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, POINTER(c_ubyte), POINTER(c_ubyte)]
    I_apply_colormap.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 146
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_rasterize'):
        continue
    I_rasterize = _lib.I_rasterize
    I_rasterize.argtypes = [POINTER(c_double), c_int, c_ubyte, POINTER(struct_Cell_head), POINTER(c_ubyte)]
    I_rasterize.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 149
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_init_signatures'):
        continue
    I_init_signatures = _lib.I_init_signatures
    I_init_signatures.argtypes = [POINTER(struct_Signature), c_int]
    I_init_signatures.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 150
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_new_signature'):
        continue
    I_new_signature = _lib.I_new_signature
    I_new_signature.argtypes = [POINTER(struct_Signature)]
    I_new_signature.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 151
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_free_signatures'):
        continue
    I_free_signatures = _lib.I_free_signatures
    I_free_signatures.argtypes = [POINTER(struct_Signature)]
    I_free_signatures.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 152
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_read_one_signature'):
        continue
    I_read_one_signature = _lib.I_read_one_signature
    I_read_one_signature.argtypes = [POINTER(FILE), POINTER(struct_Signature)]
    I_read_one_signature.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 153
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_read_signatures'):
        continue
    I_read_signatures = _lib.I_read_signatures
    I_read_signatures.argtypes = [POINTER(FILE), POINTER(struct_Signature)]
    I_read_signatures.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 154
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_write_signatures'):
        continue
    I_write_signatures = _lib.I_write_signatures
    I_write_signatures.argtypes = [POINTER(FILE), POINTER(struct_Signature)]
    I_write_signatures.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 157
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_signature_file_new'):
        continue
    I_fopen_signature_file_new = _lib.I_fopen_signature_file_new
    I_fopen_signature_file_new.argtypes = [String, String, String]
    I_fopen_signature_file_new.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 158
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_signature_file_old'):
        continue
    I_fopen_signature_file_old = _lib.I_fopen_signature_file_old
    I_fopen_signature_file_old.argtypes = [String, String, String]
    I_fopen_signature_file_old.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 161
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_SigSetNClasses'):
        continue
    I_SigSetNClasses = _lib.I_SigSetNClasses
    I_SigSetNClasses.argtypes = [POINTER(struct_SigSet)]
    I_SigSetNClasses.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 162
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_AllocClassData'):
        continue
    I_AllocClassData = _lib.I_AllocClassData
    I_AllocClassData.argtypes = [POINTER(struct_SigSet), POINTER(struct_ClassSig), c_int]
    I_AllocClassData.restype = POINTER(struct_ClassData)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 163
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_InitSigSet'):
        continue
    I_InitSigSet = _lib.I_InitSigSet
    I_InitSigSet.argtypes = [POINTER(struct_SigSet)]
    I_InitSigSet.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 164
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_SigSetNBands'):
        continue
    I_SigSetNBands = _lib.I_SigSetNBands
    I_SigSetNBands.argtypes = [POINTER(struct_SigSet), c_int]
    I_SigSetNBands.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 165
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_NewClassSig'):
        continue
    I_NewClassSig = _lib.I_NewClassSig
    I_NewClassSig.argtypes = [POINTER(struct_SigSet)]
    I_NewClassSig.restype = POINTER(struct_ClassSig)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 166
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_NewSubSig'):
        continue
    I_NewSubSig = _lib.I_NewSubSig
    I_NewSubSig.argtypes = [POINTER(struct_SigSet), POINTER(struct_ClassSig)]
    I_NewSubSig.restype = POINTER(struct_SubSig)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 167
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_ReadSigSet'):
        continue
    I_ReadSigSet = _lib.I_ReadSigSet
    I_ReadSigSet.argtypes = [POINTER(FILE), POINTER(struct_SigSet)]
    I_ReadSigSet.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 168
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_SetSigTitle'):
        continue
    I_SetSigTitle = _lib.I_SetSigTitle
    I_SetSigTitle.argtypes = [POINTER(struct_SigSet), String]
    I_SetSigTitle.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 169
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_GetSigTitle'):
        continue
    I_GetSigTitle = _lib.I_GetSigTitle
    I_GetSigTitle.argtypes = [POINTER(struct_SigSet)]
    I_GetSigTitle.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 170
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_SetClassTitle'):
        continue
    I_SetClassTitle = _lib.I_SetClassTitle
    I_SetClassTitle.argtypes = [POINTER(struct_ClassSig), String]
    I_SetClassTitle.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 171
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_GetClassTitle'):
        continue
    I_GetClassTitle = _lib.I_GetClassTitle
    I_GetClassTitle.argtypes = [POINTER(struct_ClassSig)]
    I_GetClassTitle.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 172
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_WriteSigSet'):
        continue
    I_WriteSigSet = _lib.I_WriteSigSet
    I_WriteSigSet.argtypes = [POINTER(FILE), POINTER(struct_SigSet)]
    I_WriteSigSet.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 175
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_sigset_file_new'):
        continue
    I_fopen_sigset_file_new = _lib.I_fopen_sigset_file_new
    I_fopen_sigset_file_new.argtypes = [String, String, String]
    I_fopen_sigset_file_new.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 176
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_fopen_sigset_file_old'):
        continue
    I_fopen_sigset_file_old = _lib.I_fopen_sigset_file_old
    I_fopen_sigset_file_old.argtypes = [String, String, String]
    I_fopen_sigset_file_old.restype = POINTER(FILE)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 179
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_target'):
        continue
    I_get_target = _lib.I_get_target
    I_get_target.argtypes = [String, String, String]
    I_get_target.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 180
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_put_target'):
        continue
    I_put_target = _lib.I_put_target
    I_put_target.argtypes = [String, String, String]
    I_put_target.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 183
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_get_group_title'):
        continue
    I_get_group_title = _lib.I_get_group_title
    I_get_group_title.argtypes = [String, String, c_int]
    I_get_group_title.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 184
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_put_group_title'):
        continue
    I_put_group_title = _lib.I_put_group_title
    I_put_group_title.argtypes = [String, String]
    I_put_group_title.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 187
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_variance'):
        continue
    I_variance = _lib.I_variance
    I_variance.argtypes = [c_double, c_double, c_int]
    I_variance.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 188
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_stddev'):
        continue
    I_stddev = _lib.I_stddev
    I_stddev.argtypes = [c_double, c_double, c_int]
    I_stddev.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/gis.h: 167
try:
    GNAME_MAX = 256
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 8
try:
    INAME_LEN = GNAME_MAX
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 142
try:
    SC_SCATT_DATA = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 143
try:
    SC_SCATT_CONDITIONS = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 197
try:
    SIGNATURE_TYPE_MIXED = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 199
try:
    GROUPFILE = 'CURGROUP'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 200
try:
    SUBGROUPFILE = 'CURSUBGROUP'
except:
    pass

Ref_Color = struct_Ref_Color # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 10

Ref_Files = struct_Ref_Files # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 20

Ref = struct_Ref # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 26

Tape_Info = struct_Tape_Info # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 33

Control_Points = struct_Control_Points # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 40

One_Sig = struct_One_Sig # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 52

Signature = struct_Signature # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 63

SubSig = struct_SubSig # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 71

ClassData = struct_ClassData # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 82

ClassSig = struct_ClassSig # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 90

SigSet = struct_SigSet # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 101

scScatts = struct_scScatts # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 171

scCats = struct_scCats # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 149

scdScattData = struct_scdScattData # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 186

Map_info = struct_Map_info # D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 69

# No inserted files

