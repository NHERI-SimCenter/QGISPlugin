'''Wrapper for stats.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_stats.7.8 D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/stats.h D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h -o OBJ.x86_64-w64-mingw32/stats.py

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

_libs["grass_stats.7.8"] = load_library("grass_stats.7.8")

# 1 libraries
# End libraries

# No modules

DCELL = c_double # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/gis.h: 604

stat_func = CFUNCTYPE(UNCHECKED(None), POINTER(DCELL), POINTER(DCELL), c_int, POINTER(None)) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 4

stat_func_w = CFUNCTYPE(UNCHECKED(None), POINTER(DCELL), POINTER(DCELL * 2), c_int, POINTER(None)) # D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 5

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 7
for _lib in _libs.values():
    try:
        c_ave = (stat_func).in_dll(_lib, 'c_ave')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 8
for _lib in _libs.values():
    try:
        c_count = (stat_func).in_dll(_lib, 'c_count')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 9
for _lib in _libs.values():
    try:
        c_divr = (stat_func).in_dll(_lib, 'c_divr')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 10
for _lib in _libs.values():
    try:
        c_intr = (stat_func).in_dll(_lib, 'c_intr')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 11
for _lib in _libs.values():
    try:
        c_max = (stat_func).in_dll(_lib, 'c_max')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 12
for _lib in _libs.values():
    try:
        c_maxx = (stat_func).in_dll(_lib, 'c_maxx')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 13
for _lib in _libs.values():
    try:
        c_median = (stat_func).in_dll(_lib, 'c_median')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 14
for _lib in _libs.values():
    try:
        c_min = (stat_func).in_dll(_lib, 'c_min')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 15
for _lib in _libs.values():
    try:
        c_minx = (stat_func).in_dll(_lib, 'c_minx')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 16
for _lib in _libs.values():
    try:
        c_mode = (stat_func).in_dll(_lib, 'c_mode')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 17
for _lib in _libs.values():
    try:
        c_stddev = (stat_func).in_dll(_lib, 'c_stddev')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 18
for _lib in _libs.values():
    try:
        c_sum = (stat_func).in_dll(_lib, 'c_sum')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 19
for _lib in _libs.values():
    try:
        c_thresh = (stat_func).in_dll(_lib, 'c_thresh')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 20
for _lib in _libs.values():
    try:
        c_var = (stat_func).in_dll(_lib, 'c_var')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 21
for _lib in _libs.values():
    try:
        c_range = (stat_func).in_dll(_lib, 'c_range')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 22
for _lib in _libs.values():
    try:
        c_reg_m = (stat_func).in_dll(_lib, 'c_reg_m')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 23
for _lib in _libs.values():
    try:
        c_reg_c = (stat_func).in_dll(_lib, 'c_reg_c')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 24
for _lib in _libs.values():
    try:
        c_reg_r2 = (stat_func).in_dll(_lib, 'c_reg_r2')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 25
for _lib in _libs.values():
    try:
        c_reg_t = (stat_func).in_dll(_lib, 'c_reg_t')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 26
for _lib in _libs.values():
    try:
        c_quart1 = (stat_func).in_dll(_lib, 'c_quart1')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 27
for _lib in _libs.values():
    try:
        c_quart3 = (stat_func).in_dll(_lib, 'c_quart3')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 28
for _lib in _libs.values():
    try:
        c_perc90 = (stat_func).in_dll(_lib, 'c_perc90')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 29
for _lib in _libs.values():
    try:
        c_quant = (stat_func).in_dll(_lib, 'c_quant')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 30
for _lib in _libs.values():
    try:
        c_skew = (stat_func).in_dll(_lib, 'c_skew')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 31
for _lib in _libs.values():
    try:
        c_kurt = (stat_func).in_dll(_lib, 'c_kurt')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 33
for _lib in _libs.values():
    try:
        w_ave = (stat_func_w).in_dll(_lib, 'w_ave')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 34
for _lib in _libs.values():
    try:
        w_count = (stat_func_w).in_dll(_lib, 'w_count')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 35
for _lib in _libs.values():
    try:
        w_median = (stat_func_w).in_dll(_lib, 'w_median')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 36
for _lib in _libs.values():
    try:
        w_min = (stat_func_w).in_dll(_lib, 'w_min')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 37
for _lib in _libs.values():
    try:
        w_max = (stat_func_w).in_dll(_lib, 'w_max')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 38
for _lib in _libs.values():
    try:
        w_mode = (stat_func_w).in_dll(_lib, 'w_mode')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 39
for _lib in _libs.values():
    try:
        w_quart1 = (stat_func_w).in_dll(_lib, 'w_quart1')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 40
for _lib in _libs.values():
    try:
        w_quart3 = (stat_func_w).in_dll(_lib, 'w_quart3')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 41
for _lib in _libs.values():
    try:
        w_perc90 = (stat_func_w).in_dll(_lib, 'w_perc90')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 42
for _lib in _libs.values():
    try:
        w_quant = (stat_func_w).in_dll(_lib, 'w_quant')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 43
for _lib in _libs.values():
    try:
        w_reg_m = (stat_func_w).in_dll(_lib, 'w_reg_m')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 44
for _lib in _libs.values():
    try:
        w_reg_c = (stat_func_w).in_dll(_lib, 'w_reg_c')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 45
for _lib in _libs.values():
    try:
        w_reg_r2 = (stat_func_w).in_dll(_lib, 'w_reg_r2')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 46
for _lib in _libs.values():
    try:
        w_reg_t = (stat_func_w).in_dll(_lib, 'w_reg_t')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 47
for _lib in _libs.values():
    try:
        w_stddev = (stat_func_w).in_dll(_lib, 'w_stddev')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 48
for _lib in _libs.values():
    try:
        w_sum = (stat_func_w).in_dll(_lib, 'w_sum')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 49
for _lib in _libs.values():
    try:
        w_var = (stat_func_w).in_dll(_lib, 'w_var')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 50
for _lib in _libs.values():
    try:
        w_skew = (stat_func_w).in_dll(_lib, 'w_skew')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 51
for _lib in _libs.values():
    try:
        w_kurt = (stat_func_w).in_dll(_lib, 'w_kurt')
        break
    except:
        pass

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'sort_cell'):
        continue
    sort_cell = _lib.sort_cell
    sort_cell.argtypes = [POINTER(DCELL), c_int]
    sort_cell.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/stats.h: 54
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'sort_cell_w'):
        continue
    sort_cell_w = _lib.sort_cell_w
    sort_cell_w.argtypes = [POINTER(DCELL * 2), c_int]
    sort_cell_w.restype = c_int
    break

# No inserted files

