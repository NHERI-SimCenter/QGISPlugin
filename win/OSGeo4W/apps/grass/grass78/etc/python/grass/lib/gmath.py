'''Wrapper for gmath.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gmath.7.8 D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/gmath.h D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h -o OBJ.x86_64-w64-mingw32/gmath.py

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

_libs["grass_gmath.7.8"] = load_library("grass_gmath.7.8")

# 1 libraries
# End libraries

# No modules

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 59
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'values',
    'cols',
    'index',
]
struct_anon_3._fields_ = [
    ('values', POINTER(c_double)),
    ('cols', c_uint),
    ('index', POINTER(c_uint)),
]

G_math_spvector = struct_anon_3 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 59

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_alloc_vector'):
        continue
    G_alloc_vector = _lib.G_alloc_vector
    G_alloc_vector.argtypes = [c_size_t]
    G_alloc_vector.restype = POINTER(c_double)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_alloc_matrix'):
        continue
    G_alloc_matrix = _lib.G_alloc_matrix
    G_alloc_matrix.argtypes = [c_int, c_int]
    G_alloc_matrix.restype = POINTER(POINTER(c_double))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_alloc_fvector'):
        continue
    G_alloc_fvector = _lib.G_alloc_fvector
    G_alloc_fvector.argtypes = [c_size_t]
    G_alloc_fvector.restype = POINTER(c_float)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_alloc_fmatrix'):
        continue
    G_alloc_fmatrix = _lib.G_alloc_fmatrix
    G_alloc_fmatrix.argtypes = [c_int, c_int]
    G_alloc_fmatrix.restype = POINTER(POINTER(c_float))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_free_vector'):
        continue
    G_free_vector = _lib.G_free_vector
    G_free_vector.argtypes = [POINTER(c_double)]
    G_free_vector.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_free_matrix'):
        continue
    G_free_matrix = _lib.G_free_matrix
    G_free_matrix.argtypes = [POINTER(POINTER(c_double))]
    G_free_matrix.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_free_fvector'):
        continue
    G_free_fvector = _lib.G_free_fvector
    G_free_fvector.argtypes = [POINTER(c_float)]
    G_free_fvector.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_free_fmatrix'):
        continue
    G_free_fmatrix = _lib.G_free_fmatrix
    G_free_fmatrix.argtypes = [POINTER(POINTER(c_float))]
    G_free_fmatrix.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_alloc_ivector'):
        continue
    G_alloc_ivector = _lib.G_alloc_ivector
    G_alloc_ivector.argtypes = [c_size_t]
    G_alloc_ivector.restype = POINTER(c_int)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_alloc_imatrix'):
        continue
    G_alloc_imatrix = _lib.G_alloc_imatrix
    G_alloc_imatrix.argtypes = [c_int, c_int]
    G_alloc_imatrix.restype = POINTER(POINTER(c_int))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_free_ivector'):
        continue
    G_free_ivector = _lib.G_free_ivector
    G_free_ivector.argtypes = [POINTER(c_int)]
    G_free_ivector.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_free_imatrix'):
        continue
    G_free_imatrix = _lib.G_free_imatrix
    G_free_imatrix.argtypes = [POINTER(POINTER(c_int))]
    G_free_imatrix.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'fft'):
        continue
    fft = _lib.fft
    fft.argtypes = [c_int, POINTER(c_double) * 2, c_int, c_int, c_int]
    fft.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'fft2'):
        continue
    fft2 = _lib.fft2
    fft2.argtypes = [c_int, POINTER(c_double * 2), c_int, c_int, c_int]
    fft2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_rand_gauss'):
        continue
    G_math_rand_gauss = _lib.G_math_rand_gauss
    G_math_rand_gauss.argtypes = [c_double]
    G_math_rand_gauss.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 28
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_max_pow2'):
        continue
    G_math_max_pow2 = _lib.G_math_max_pow2
    G_math_max_pow2.argtypes = [c_long]
    G_math_max_pow2.restype = c_long
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_min_pow2'):
        continue
    G_math_min_pow2 = _lib.G_math_min_pow2
    G_math_min_pow2.argtypes = [c_long]
    G_math_min_pow2.restype = c_long
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 32
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_srand'):
        continue
    G_math_srand = _lib.G_math_srand
    G_math_srand.argtypes = [c_int]
    G_math_srand.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_srand_auto'):
        continue
    G_math_srand_auto = _lib.G_math_srand_auto
    G_math_srand_auto.argtypes = []
    G_math_srand_auto.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_rand'):
        continue
    G_math_rand = _lib.G_math_rand
    G_math_rand.argtypes = []
    G_math_rand.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 37
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'del2g'):
        continue
    del2g = _lib.del2g
    del2g.argtypes = [POINTER(c_double) * 2, c_int, c_double]
    del2g.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 40
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'getg'):
        continue
    getg = _lib.getg
    getg.argtypes = [c_double, POINTER(c_double) * 2, c_int]
    getg.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_egvorder'):
        continue
    G_math_egvorder = _lib.G_math_egvorder
    G_math_egvorder.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_long]
    G_math_egvorder.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_complex_mult'):
        continue
    G_math_complex_mult = _lib.G_math_complex_mult
    G_math_complex_mult.argtypes = [POINTER(c_double) * 2, c_int, POINTER(c_double) * 2, c_int, POINTER(c_double) * 2, c_int]
    G_math_complex_mult.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 49
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_ludcmp'):
        continue
    G_ludcmp = _lib.G_ludcmp
    G_ludcmp.argtypes = [POINTER(POINTER(c_double)), c_int, POINTER(c_int), POINTER(c_double)]
    G_ludcmp.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 50
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_lubksb'):
        continue
    G_lubksb = _lib.G_lubksb
    G_lubksb.argtypes = [POINTER(POINTER(c_double)), c_int, POINTER(c_int), POINTER(c_double)]
    G_lubksb.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_findzc'):
        continue
    G_math_findzc = _lib.G_math_findzc
    G_math_findzc.argtypes = [POINTER(c_double), c_int, POINTER(c_double), c_double, c_int]
    G_math_findzc.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solv'):
        continue
    G_math_solv = _lib.G_math_solv
    G_math_solv.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_solv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 60
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solvps'):
        continue
    G_math_solvps = _lib.G_math_solvps
    G_math_solvps.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_solvps.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solvtd'):
        continue
    G_math_solvtd = _lib.G_math_solvtd
    G_math_solvtd.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    G_math_solvtd.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 62
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solvru'):
        continue
    G_math_solvru = _lib.G_math_solvru
    G_math_solvru.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_solvru.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_minv'):
        continue
    G_math_minv = _lib.G_math_minv
    G_math_minv.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_minv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 64
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_psinv'):
        continue
    G_math_psinv = _lib.G_math_psinv
    G_math_psinv.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_psinv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_ruinv'):
        continue
    G_math_ruinv = _lib.G_math_ruinv
    G_math_ruinv.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_ruinv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_eigval'):
        continue
    G_math_eigval = _lib.G_math_eigval
    G_math_eigval.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_eigval.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 67
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_eigen'):
        continue
    G_math_eigen = _lib.G_math_eigen
    G_math_eigen.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_eigen.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 68
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_evmax'):
        continue
    G_math_evmax = _lib.G_math_evmax
    G_math_evmax.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_evmax.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 69
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_svdval'):
        continue
    G_math_svdval = _lib.G_math_svdval
    G_math_svdval.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_svdval.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 70
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sv2val'):
        continue
    G_math_sv2val = _lib.G_math_sv2val
    G_math_sv2val.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_sv2val.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 71
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_svduv'):
        continue
    G_math_svduv = _lib.G_math_svduv
    G_math_svduv.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]
    G_math_svduv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sv2uv'):
        continue
    G_math_sv2uv = _lib.G_math_sv2uv
    G_math_sv2uv.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]
    G_math_sv2uv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 73
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_svdu1v'):
        continue
    G_math_svdu1v = _lib.G_math_svdu1v
    G_math_svdu1v.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]
    G_math_svdu1v.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_alloc_spvector'):
        continue
    G_math_alloc_spvector = _lib.G_math_alloc_spvector
    G_math_alloc_spvector.argtypes = [c_int]
    G_math_alloc_spvector.restype = POINTER(G_math_spvector)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 82
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_alloc_spmatrix'):
        continue
    G_math_alloc_spmatrix = _lib.G_math_alloc_spmatrix
    G_math_alloc_spmatrix.argtypes = [c_int]
    G_math_alloc_spmatrix.restype = POINTER(POINTER(G_math_spvector))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 83
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_free_spmatrix'):
        continue
    G_math_free_spmatrix = _lib.G_math_free_spmatrix
    G_math_free_spmatrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]
    G_math_free_spmatrix.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_free_spvector'):
        continue
    G_math_free_spvector = _lib.G_math_free_spvector
    G_math_free_spvector.argtypes = [POINTER(G_math_spvector)]
    G_math_free_spvector.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_add_spvector'):
        continue
    G_math_add_spvector = _lib.G_math_add_spvector
    G_math_add_spvector.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(G_math_spvector), c_int]
    G_math_add_spvector.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_A_to_Asp'):
        continue
    G_math_A_to_Asp = _lib.G_math_A_to_Asp
    G_math_A_to_Asp.argtypes = [POINTER(POINTER(c_double)), c_int, c_double]
    G_math_A_to_Asp.restype = POINTER(POINTER(G_math_spvector))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_Asp_to_A'):
        continue
    G_math_Asp_to_A = _lib.G_math_Asp_to_A
    G_math_Asp_to_A.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]
    G_math_Asp_to_A.restype = POINTER(POINTER(c_double))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 88
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_Asp_to_sband_matrix'):
        continue
    G_math_Asp_to_sband_matrix = _lib.G_math_Asp_to_sband_matrix
    G_math_Asp_to_sband_matrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int, c_int]
    G_math_Asp_to_sband_matrix.restype = POINTER(POINTER(c_double))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 89
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sband_matrix_to_Asp'):
        continue
    G_math_sband_matrix_to_Asp = _lib.G_math_sband_matrix_to_Asp
    G_math_sband_matrix_to_Asp.argtypes = [POINTER(POINTER(c_double)), c_int, c_int, c_double]
    G_math_sband_matrix_to_Asp.restype = POINTER(POINTER(G_math_spvector))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 90
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_print_spmatrix'):
        continue
    G_math_print_spmatrix = _lib.G_math_print_spmatrix
    G_math_print_spmatrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]
    G_math_print_spmatrix.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 91
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_Ax_sparse'):
        continue
    G_math_Ax_sparse = _lib.G_math_Ax_sparse
    G_math_Ax_sparse.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_Ax_sparse.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 94
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_matrix_to_sband_matrix'):
        continue
    G_math_matrix_to_sband_matrix = _lib.G_math_matrix_to_sband_matrix
    G_math_matrix_to_sband_matrix.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]
    G_math_matrix_to_sband_matrix.restype = POINTER(POINTER(c_double))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 95
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sband_matrix_to_matrix'):
        continue
    G_math_sband_matrix_to_matrix = _lib.G_math_sband_matrix_to_matrix
    G_math_sband_matrix_to_matrix.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]
    G_math_sband_matrix_to_matrix.restype = POINTER(POINTER(c_double))
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_Ax_sband'):
        continue
    G_math_Ax_sband = _lib.G_math_Ax_sband
    G_math_Ax_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_Ax_sband.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 99
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_gauss'):
        continue
    G_math_solver_gauss = _lib.G_math_solver_gauss
    G_math_solver_gauss.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_solver_gauss.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 100
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_lu'):
        continue
    G_math_solver_lu = _lib.G_math_solver_lu
    G_math_solver_lu.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_solver_lu.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 101
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_cholesky'):
        continue
    G_math_solver_cholesky = _lib.G_math_solver_cholesky
    G_math_solver_cholesky.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_solver_cholesky.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 102
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_cholesky_sband'):
        continue
    G_math_solver_cholesky_sband = _lib.G_math_solver_cholesky_sband
    G_math_solver_cholesky_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_solver_cholesky_sband.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_jacobi'):
        continue
    G_math_solver_jacobi = _lib.G_math_solver_jacobi
    G_math_solver_jacobi.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_jacobi.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 104
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_gs'):
        continue
    G_math_solver_gs = _lib.G_math_solver_gs
    G_math_solver_gs.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_gs.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 106
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_pcg'):
        continue
    G_math_solver_pcg = _lib.G_math_solver_pcg
    G_math_solver_pcg.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_int]
    G_math_solver_pcg.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 107
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_cg'):
        continue
    G_math_solver_cg = _lib.G_math_solver_cg
    G_math_solver_cg.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_cg.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 108
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_cg_sband'):
        continue
    G_math_solver_cg_sband = _lib.G_math_solver_cg_sband
    G_math_solver_cg_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int, c_double]
    G_math_solver_cg_sband.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 109
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_bicgstab'):
        continue
    G_math_solver_bicgstab = _lib.G_math_solver_bicgstab
    G_math_solver_bicgstab.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_bicgstab.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 110
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_sparse_jacobi'):
        continue
    G_math_solver_sparse_jacobi = _lib.G_math_solver_sparse_jacobi
    G_math_solver_sparse_jacobi.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_sparse_jacobi.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 111
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_sparse_gs'):
        continue
    G_math_solver_sparse_gs = _lib.G_math_solver_sparse_gs
    G_math_solver_sparse_gs.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_sparse_gs.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 112
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_sparse_pcg'):
        continue
    G_math_solver_sparse_pcg = _lib.G_math_solver_sparse_pcg
    G_math_solver_sparse_pcg.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_int]
    G_math_solver_sparse_pcg.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 113
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_sparse_cg'):
        continue
    G_math_solver_sparse_cg = _lib.G_math_solver_sparse_cg
    G_math_solver_sparse_cg.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_sparse_cg.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 114
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_solver_sparse_bicgstab'):
        continue
    G_math_solver_sparse_bicgstab = _lib.G_math_solver_sparse_bicgstab
    G_math_solver_sparse_bicgstab.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_sparse_bicgstab.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 117
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_gauss_elimination'):
        continue
    G_math_gauss_elimination = _lib.G_math_gauss_elimination
    G_math_gauss_elimination.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_gauss_elimination.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 118
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_lu_decomposition'):
        continue
    G_math_lu_decomposition = _lib.G_math_lu_decomposition
    G_math_lu_decomposition.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_lu_decomposition.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 119
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_cholesky_decomposition'):
        continue
    G_math_cholesky_decomposition = _lib.G_math_cholesky_decomposition
    G_math_cholesky_decomposition.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]
    G_math_cholesky_decomposition.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 120
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_cholesky_sband_decomposition'):
        continue
    G_math_cholesky_sband_decomposition = _lib.G_math_cholesky_sband_decomposition
    G_math_cholesky_sband_decomposition.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_cholesky_sband_decomposition.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 121
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_backward_substitution'):
        continue
    G_math_backward_substitution = _lib.G_math_backward_substitution
    G_math_backward_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_backward_substitution.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 122
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_forward_substitution'):
        continue
    G_math_forward_substitution = _lib.G_math_forward_substitution
    G_math_forward_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_forward_substitution.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 123
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_cholesky_sband_substitution'):
        continue
    G_math_cholesky_sband_substitution = _lib.G_math_cholesky_sband_substitution
    G_math_cholesky_sband_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_cholesky_sband_substitution.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 128
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_x_dot_y'):
        continue
    G_math_d_x_dot_y = _lib.G_math_d_x_dot_y
    G_math_d_x_dot_y.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_x_dot_y.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 129
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_asum_norm'):
        continue
    G_math_d_asum_norm = _lib.G_math_d_asum_norm
    G_math_d_asum_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_asum_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 130
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_euclid_norm'):
        continue
    G_math_d_euclid_norm = _lib.G_math_d_euclid_norm
    G_math_d_euclid_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_euclid_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 131
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_max_norm'):
        continue
    G_math_d_max_norm = _lib.G_math_d_max_norm
    G_math_d_max_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_max_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 132
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_ax_by'):
        continue
    G_math_d_ax_by = _lib.G_math_d_ax_by
    G_math_d_ax_by.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_double, c_int]
    G_math_d_ax_by.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 133
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_copy'):
        continue
    G_math_d_copy = _lib.G_math_d_copy
    G_math_d_copy.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_copy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 135
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_x_dot_y'):
        continue
    G_math_f_x_dot_y = _lib.G_math_f_x_dot_y
    G_math_f_x_dot_y.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_x_dot_y.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 136
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_asum_norm'):
        continue
    G_math_f_asum_norm = _lib.G_math_f_asum_norm
    G_math_f_asum_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_asum_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 137
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_euclid_norm'):
        continue
    G_math_f_euclid_norm = _lib.G_math_f_euclid_norm
    G_math_f_euclid_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_euclid_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 138
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_max_norm'):
        continue
    G_math_f_max_norm = _lib.G_math_f_max_norm
    G_math_f_max_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_max_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 139
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_ax_by'):
        continue
    G_math_f_ax_by = _lib.G_math_f_ax_by
    G_math_f_ax_by.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_float, c_float, c_int]
    G_math_f_ax_by.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 140
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_copy'):
        continue
    G_math_f_copy = _lib.G_math_f_copy
    G_math_f_copy.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_copy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 142
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_i_x_dot_y'):
        continue
    G_math_i_x_dot_y = _lib.G_math_i_x_dot_y
    G_math_i_x_dot_y.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_double), c_int]
    G_math_i_x_dot_y.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 143
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_i_asum_norm'):
        continue
    G_math_i_asum_norm = _lib.G_math_i_asum_norm
    G_math_i_asum_norm.argtypes = [POINTER(c_int), POINTER(c_double), c_int]
    G_math_i_asum_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 144
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_i_euclid_norm'):
        continue
    G_math_i_euclid_norm = _lib.G_math_i_euclid_norm
    G_math_i_euclid_norm.argtypes = [POINTER(c_int), POINTER(c_double), c_int]
    G_math_i_euclid_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 145
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_i_max_norm'):
        continue
    G_math_i_max_norm = _lib.G_math_i_max_norm
    G_math_i_max_norm.argtypes = [POINTER(c_int), POINTER(c_int), c_int]
    G_math_i_max_norm.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 146
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_i_ax_by'):
        continue
    G_math_i_ax_by = _lib.G_math_i_ax_by
    G_math_i_ax_by.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int, c_int, c_int]
    G_math_i_ax_by.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 147
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_i_copy'):
        continue
    G_math_i_copy = _lib.G_math_i_copy
    G_math_i_copy.argtypes = [POINTER(c_int), POINTER(c_int), c_int]
    G_math_i_copy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 150
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_ddot'):
        continue
    G_math_ddot = _lib.G_math_ddot
    G_math_ddot.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_ddot.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 151
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sdot'):
        continue
    G_math_sdot = _lib.G_math_sdot
    G_math_sdot.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_sdot.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 152
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sdsdot'):
        continue
    G_math_sdsdot = _lib.G_math_sdsdot
    G_math_sdsdot.argtypes = [POINTER(c_float), POINTER(c_float), c_float, c_int]
    G_math_sdsdot.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 153
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_dnrm2'):
        continue
    G_math_dnrm2 = _lib.G_math_dnrm2
    G_math_dnrm2.argtypes = [POINTER(c_double), c_int]
    G_math_dnrm2.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 154
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_dasum'):
        continue
    G_math_dasum = _lib.G_math_dasum
    G_math_dasum.argtypes = [POINTER(c_double), c_int]
    G_math_dasum.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 155
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_idamax'):
        continue
    G_math_idamax = _lib.G_math_idamax
    G_math_idamax.argtypes = [POINTER(c_double), c_int]
    G_math_idamax.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 156
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_snrm2'):
        continue
    G_math_snrm2 = _lib.G_math_snrm2
    G_math_snrm2.argtypes = [POINTER(c_float), c_int]
    G_math_snrm2.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 157
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sasum'):
        continue
    G_math_sasum = _lib.G_math_sasum
    G_math_sasum.argtypes = [POINTER(c_float), c_int]
    G_math_sasum.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 158
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_isamax'):
        continue
    G_math_isamax = _lib.G_math_isamax
    G_math_isamax.argtypes = [POINTER(c_float), c_int]
    G_math_isamax.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 159
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_dscal'):
        continue
    G_math_dscal = _lib.G_math_dscal
    G_math_dscal.argtypes = [POINTER(c_double), c_double, c_int]
    G_math_dscal.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 160
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_sscal'):
        continue
    G_math_sscal = _lib.G_math_sscal
    G_math_sscal.argtypes = [POINTER(c_float), c_float, c_int]
    G_math_sscal.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 161
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_dcopy'):
        continue
    G_math_dcopy = _lib.G_math_dcopy
    G_math_dcopy.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_dcopy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 162
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_scopy'):
        continue
    G_math_scopy = _lib.G_math_scopy
    G_math_scopy.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_scopy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 163
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_daxpy'):
        continue
    G_math_daxpy = _lib.G_math_daxpy
    G_math_daxpy.argtypes = [POINTER(c_double), POINTER(c_double), c_double, c_int]
    G_math_daxpy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 164
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_saxpy'):
        continue
    G_math_saxpy = _lib.G_math_saxpy
    G_math_saxpy.argtypes = [POINTER(c_float), POINTER(c_float), c_float, c_int]
    G_math_saxpy.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 167
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_Ax'):
        continue
    G_math_d_Ax = _lib.G_math_d_Ax
    G_math_d_Ax.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_d_Ax.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 168
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_Ax'):
        continue
    G_math_f_Ax = _lib.G_math_f_Ax
    G_math_f_Ax.argtypes = [POINTER(POINTER(c_float)), POINTER(c_float), POINTER(c_float), c_int, c_int]
    G_math_f_Ax.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 169
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_x_dyad_y'):
        continue
    G_math_d_x_dyad_y = _lib.G_math_d_x_dyad_y
    G_math_d_x_dyad_y.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_d_x_dyad_y.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 170
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_x_dyad_y'):
        continue
    G_math_f_x_dyad_y = _lib.G_math_f_x_dyad_y
    G_math_f_x_dyad_y.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(POINTER(c_float)), c_int, c_int]
    G_math_f_x_dyad_y.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 171
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_aAx_by'):
        continue
    G_math_d_aAx_by = _lib.G_math_d_aAx_by
    G_math_d_aAx_by.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_double, c_double, POINTER(c_double), c_int, c_int]
    G_math_d_aAx_by.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 172
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_aAx_by'):
        continue
    G_math_f_aAx_by = _lib.G_math_f_aAx_by
    G_math_f_aAx_by.argtypes = [POINTER(POINTER(c_float)), POINTER(c_float), POINTER(c_float), c_float, c_float, POINTER(c_float), c_int, c_int]
    G_math_f_aAx_by.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 173
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_A_T'):
        continue
    G_math_d_A_T = _lib.G_math_d_A_T
    G_math_d_A_T.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_d_A_T.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 174
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_A_T'):
        continue
    G_math_f_A_T = _lib.G_math_f_A_T
    G_math_f_A_T.argtypes = [POINTER(POINTER(c_float)), c_int]
    G_math_f_A_T.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 177
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_aA_B'):
        continue
    G_math_d_aA_B = _lib.G_math_d_aA_B
    G_math_d_aA_B.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_double, POINTER(POINTER(c_double)), c_int, c_int]
    G_math_d_aA_B.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 178
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_aA_B'):
        continue
    G_math_f_aA_B = _lib.G_math_f_aA_B
    G_math_f_aA_B.argtypes = [POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_float, POINTER(POINTER(c_float)), c_int, c_int]
    G_math_f_aA_B.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 179
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_d_AB'):
        continue
    G_math_d_AB = _lib.G_math_d_AB
    G_math_d_AB.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, c_int, c_int]
    G_math_d_AB.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 180
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'G_math_f_AB'):
        continue
    G_math_f_AB = _lib.G_math_f_AB
    G_math_f_AB.argtypes = [POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_int, c_int, c_int]
    G_math_f_AB.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 36
try:
    G_MATH_SOLVER_DIRECT_GAUSS = 'gauss'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 37
try:
    G_MATH_SOLVER_DIRECT_LU = 'lu'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 38
try:
    G_MATH_SOLVER_DIRECT_CHOLESKY = 'cholesky'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 39
try:
    G_MATH_SOLVER_ITERATIVE_JACOBI = 'jacobi'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 40
try:
    G_MATH_SOLVER_ITERATIVE_SOR = 'sor'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 41
try:
    G_MATH_SOLVER_ITERATIVE_CG = 'cg'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 42
try:
    G_MATH_SOLVER_ITERATIVE_PCG = 'pcg'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 43
try:
    G_MATH_SOLVER_ITERATIVE_BICGSTAB = 'bicgstab'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 46
try:
    G_MATH_DIAGONAL_PRECONDITION = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 47
try:
    G_MATH_ROWSCALE_ABSSUMNORM_PRECONDITION = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 48
try:
    G_MATH_ROWSCALE_EUKLIDNORM_PRECONDITION = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 49
try:
    G_MATH_ROWSCALE_MAXNORM_PRECONDITION = 4
except:
    pass

# No inserted files

