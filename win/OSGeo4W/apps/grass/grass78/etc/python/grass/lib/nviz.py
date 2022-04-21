'''Wrapper for nviz.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_nviz.7.8 D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/nviz.h D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h -o OBJ.x86_64-w64-mingw32/nviz.py

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

_libs["grass_nviz.7.8"] = load_library("grass_nviz.7.8")

# 1 libraries
# End libraries

# No modules

# D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/windef.h: 47
class struct_HDC__(Structure):
    pass

struct_HDC__.__slots__ = [
    'unused',
]
struct_HDC__._fields_ = [
    ('unused', c_int),
]

HDC = POINTER(struct_HDC__) # D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/windef.h: 47

# D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/windef.h: 48
class struct_HGLRC__(Structure):
    pass

struct_HGLRC__.__slots__ = [
    'unused',
]
struct_HGLRC__._fields_ = [
    ('unused', c_int),
]

HGLRC = POINTER(struct_HGLRC__) # D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/windef.h: 48

GLubyte = c_ubyte # D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/GL/gl.h: 29

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 76
class struct_anon_354(Structure):
    pass

struct_anon_354.__slots__ = [
    'id',
    'brt',
    'r',
    'g',
    'b',
    'ar',
    'ag',
    'ab',
    'x',
    'y',
    'z',
    'w',
]
struct_anon_354._fields_ = [
    ('id', c_int),
    ('brt', c_float),
    ('r', c_float),
    ('g', c_float),
    ('b', c_float),
    ('ar', c_float),
    ('ag', c_float),
    ('ab', c_float),
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('w', c_float),
]

light_data = struct_anon_354 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 76

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 78
class struct_fringe_data(Structure):
    pass

struct_fringe_data.__slots__ = [
    'id',
    'color',
    'elev',
    'where',
]
struct_fringe_data._fields_ = [
    ('id', c_int),
    ('color', c_ulong),
    ('elev', c_float),
    ('where', c_int * 4),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 86
class struct_arrow_data(Structure):
    pass

struct_arrow_data.__slots__ = [
    'color',
    'size',
    'where',
]
struct_arrow_data._fields_ = [
    ('color', c_ulong),
    ('size', c_float),
    ('where', c_float * 3),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 93
class struct_scalebar_data(Structure):
    pass

struct_scalebar_data.__slots__ = [
    'id',
    'color',
    'size',
    'where',
]
struct_scalebar_data._fields_ = [
    ('id', c_int),
    ('color', c_ulong),
    ('size', c_float),
    ('where', c_float * 3),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 130
class struct_anon_355(Structure):
    pass

struct_anon_355.__slots__ = [
    'zrange',
    'xyrange',
    'num_cplanes',
    'cur_cplane',
    'cp_on',
    'cp_trans',
    'cp_rot',
    'light',
    'num_fringes',
    'fringe',
    'draw_arrow',
    'arrow',
    'num_scalebars',
    'scalebar',
    'bgcolor',
]
struct_anon_355._fields_ = [
    ('zrange', c_float),
    ('xyrange', c_float),
    ('num_cplanes', c_int),
    ('cur_cplane', c_int),
    ('cp_on', c_int * 6),
    ('cp_trans', (c_float * 3) * 6),
    ('cp_rot', (c_float * 3) * 6),
    ('light', light_data * 3),
    ('num_fringes', c_int),
    ('fringe', POINTER(POINTER(struct_fringe_data))),
    ('draw_arrow', c_int),
    ('arrow', POINTER(struct_arrow_data)),
    ('num_scalebars', c_int),
    ('scalebar', POINTER(POINTER(struct_scalebar_data))),
    ('bgcolor', c_int),
]

nv_data = struct_anon_355 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 130

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 132
class struct_render_window(Structure):
    pass

struct_render_window.__slots__ = [
    'displayId',
    'contextId',
    'width',
    'height',
]
struct_render_window._fields_ = [
    ('displayId', HDC),
    ('contextId', HGLRC),
    ('width', c_int),
    ('height', c_int),
]

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_resize_window'):
        continue
    Nviz_resize_window = _lib.Nviz_resize_window
    Nviz_resize_window.argtypes = [c_int, c_int]
    Nviz_resize_window.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_update_ranges'):
        continue
    Nviz_update_ranges = _lib.Nviz_update_ranges
    Nviz_update_ranges.argtypes = [POINTER(nv_data)]
    Nviz_update_ranges.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_viewpoint_position'):
        continue
    Nviz_set_viewpoint_position = _lib.Nviz_set_viewpoint_position
    Nviz_set_viewpoint_position.argtypes = [c_double, c_double]
    Nviz_set_viewpoint_position.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_viewpoint_position'):
        continue
    Nviz_get_viewpoint_position = _lib.Nviz_get_viewpoint_position
    Nviz_get_viewpoint_position.argtypes = [POINTER(c_double), POINTER(c_double)]
    Nviz_get_viewpoint_position.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_viewpoint_height'):
        continue
    Nviz_set_viewpoint_height = _lib.Nviz_set_viewpoint_height
    Nviz_set_viewpoint_height.argtypes = [c_double]
    Nviz_set_viewpoint_height.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_viewpoint_height'):
        continue
    Nviz_get_viewpoint_height = _lib.Nviz_get_viewpoint_height
    Nviz_get_viewpoint_height.argtypes = [POINTER(c_double)]
    Nviz_get_viewpoint_height.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_viewpoint_persp'):
        continue
    Nviz_set_viewpoint_persp = _lib.Nviz_set_viewpoint_persp
    Nviz_set_viewpoint_persp.argtypes = [c_int]
    Nviz_set_viewpoint_persp.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_viewpoint_twist'):
        continue
    Nviz_set_viewpoint_twist = _lib.Nviz_set_viewpoint_twist
    Nviz_set_viewpoint_twist.argtypes = [c_int]
    Nviz_set_viewpoint_twist.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_change_exag'):
        continue
    Nviz_change_exag = _lib.Nviz_change_exag
    Nviz_change_exag.argtypes = [POINTER(nv_data), c_double]
    Nviz_change_exag.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_look_here'):
        continue
    Nviz_look_here = _lib.Nviz_look_here
    Nviz_look_here.argtypes = [c_double, c_double]
    Nviz_look_here.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_modelview'):
        continue
    Nviz_get_modelview = _lib.Nviz_get_modelview
    Nviz_get_modelview.argtypes = [POINTER(c_double)]
    Nviz_get_modelview.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_rotation'):
        continue
    Nviz_set_rotation = _lib.Nviz_set_rotation
    Nviz_set_rotation.argtypes = [c_double, c_double, c_double, c_double]
    Nviz_set_rotation.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_unset_rotation'):
        continue
    Nviz_unset_rotation = _lib.Nviz_unset_rotation
    Nviz_unset_rotation.argtypes = []
    Nviz_unset_rotation.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_init_rotation'):
        continue
    Nviz_init_rotation = _lib.Nviz_init_rotation
    Nviz_init_rotation.argtypes = []
    Nviz_init_rotation.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 19
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_flythrough'):
        continue
    Nviz_flythrough = _lib.Nviz_flythrough
    Nviz_flythrough.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_int), c_int]
    Nviz_flythrough.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_new_cplane'):
        continue
    Nviz_new_cplane = _lib.Nviz_new_cplane
    Nviz_new_cplane.argtypes = [POINTER(nv_data), c_int]
    Nviz_new_cplane.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_on_cplane'):
        continue
    Nviz_on_cplane = _lib.Nviz_on_cplane
    Nviz_on_cplane.argtypes = [POINTER(nv_data), c_int]
    Nviz_on_cplane.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_off_cplane'):
        continue
    Nviz_off_cplane = _lib.Nviz_off_cplane
    Nviz_off_cplane.argtypes = [POINTER(nv_data), c_int]
    Nviz_off_cplane.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_cplane'):
        continue
    Nviz_draw_cplane = _lib.Nviz_draw_cplane
    Nviz_draw_cplane.argtypes = [POINTER(nv_data), c_int, c_int]
    Nviz_draw_cplane.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 26
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_num_cplanes'):
        continue
    Nviz_num_cplanes = _lib.Nviz_num_cplanes
    Nviz_num_cplanes.argtypes = [POINTER(nv_data)]
    Nviz_num_cplanes.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 27
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_current_cplane'):
        continue
    Nviz_get_current_cplane = _lib.Nviz_get_current_cplane
    Nviz_get_current_cplane.argtypes = [POINTER(nv_data)]
    Nviz_get_current_cplane.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 28
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_cplane_rotation'):
        continue
    Nviz_set_cplane_rotation = _lib.Nviz_set_cplane_rotation
    Nviz_set_cplane_rotation.argtypes = [POINTER(nv_data), c_int, c_float, c_float, c_float]
    Nviz_set_cplane_rotation.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_cplane_rotation'):
        continue
    Nviz_get_cplane_rotation = _lib.Nviz_get_cplane_rotation
    Nviz_get_cplane_rotation.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    Nviz_get_cplane_rotation.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_cplane_translation'):
        continue
    Nviz_set_cplane_translation = _lib.Nviz_set_cplane_translation
    Nviz_set_cplane_translation.argtypes = [POINTER(nv_data), c_int, c_float, c_float, c_float]
    Nviz_set_cplane_translation.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 31
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_cplane_translation'):
        continue
    Nviz_get_cplane_translation = _lib.Nviz_get_cplane_translation
    Nviz_get_cplane_translation.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    Nviz_get_cplane_translation.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 32
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_fence_color'):
        continue
    Nviz_set_fence_color = _lib.Nviz_set_fence_color
    Nviz_set_fence_color.argtypes = [POINTER(nv_data), c_int]
    Nviz_set_fence_color.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_cplane_here'):
        continue
    Nviz_set_cplane_here = _lib.Nviz_set_cplane_here
    Nviz_set_cplane_here.argtypes = [POINTER(nv_data), c_int, c_float, c_float]
    Nviz_set_cplane_here.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 37
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_all_surf'):
        continue
    Nviz_draw_all_surf = _lib.Nviz_draw_all_surf
    Nviz_draw_all_surf.argtypes = [POINTER(nv_data)]
    Nviz_draw_all_surf.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 38
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_all_vect'):
        continue
    Nviz_draw_all_vect = _lib.Nviz_draw_all_vect
    Nviz_draw_all_vect.argtypes = []
    Nviz_draw_all_vect.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 39
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_all_site'):
        continue
    Nviz_draw_all_site = _lib.Nviz_draw_all_site
    Nviz_draw_all_site.argtypes = []
    Nviz_draw_all_site.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 40
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_all_vol'):
        continue
    Nviz_draw_all_vol = _lib.Nviz_draw_all_vol
    Nviz_draw_all_vol.argtypes = []
    Nviz_draw_all_vol.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 41
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_all'):
        continue
    Nviz_draw_all = _lib.Nviz_draw_all
    Nviz_draw_all.argtypes = [POINTER(nv_data)]
    Nviz_draw_all.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 42
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_quick'):
        continue
    Nviz_draw_quick = _lib.Nviz_draw_quick
    Nviz_draw_quick.argtypes = [POINTER(nv_data), c_int]
    Nviz_draw_quick.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_load_image'):
        continue
    Nviz_load_image = _lib.Nviz_load_image
    Nviz_load_image.argtypes = [POINTER(GLubyte), c_int, c_int, c_int]
    Nviz_load_image.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 44
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_image'):
        continue
    Nviz_draw_image = _lib.Nviz_draw_image
    Nviz_draw_image.argtypes = [c_int, c_int, c_int, c_int, c_int]
    Nviz_draw_image.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 45
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_2D'):
        continue
    Nviz_set_2D = _lib.Nviz_set_2D
    Nviz_set_2D.argtypes = [c_int, c_int]
    Nviz_set_2D.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_del_texture'):
        continue
    Nviz_del_texture = _lib.Nviz_del_texture
    Nviz_del_texture.argtypes = [c_int]
    Nviz_del_texture.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 47
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_max_texture'):
        continue
    Nviz_get_max_texture = _lib.Nviz_get_max_texture
    Nviz_get_max_texture.argtypes = [POINTER(c_int)]
    Nviz_get_max_texture.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 50
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_exag_height'):
        continue
    Nviz_get_exag_height = _lib.Nviz_get_exag_height
    Nviz_get_exag_height.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Nviz_get_exag_height.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_exag'):
        continue
    Nviz_get_exag = _lib.Nviz_get_exag
    Nviz_get_exag.argtypes = []
    Nviz_get_exag.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 54
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_light_position'):
        continue
    Nviz_set_light_position = _lib.Nviz_set_light_position
    Nviz_set_light_position.argtypes = [POINTER(nv_data), c_int, c_double, c_double, c_double, c_double]
    Nviz_set_light_position.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_light_bright'):
        continue
    Nviz_set_light_bright = _lib.Nviz_set_light_bright
    Nviz_set_light_bright.argtypes = [POINTER(nv_data), c_int, c_double]
    Nviz_set_light_bright.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 56
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_light_color'):
        continue
    Nviz_set_light_color = _lib.Nviz_set_light_color
    Nviz_set_light_color.argtypes = [POINTER(nv_data), c_int, c_int, c_int, c_int]
    Nviz_set_light_color.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_light_ambient'):
        continue
    Nviz_set_light_ambient = _lib.Nviz_set_light_ambient
    Nviz_set_light_ambient.argtypes = [POINTER(nv_data), c_int, c_double]
    Nviz_set_light_ambient.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 58
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_init_light'):
        continue
    Nviz_init_light = _lib.Nviz_init_light
    Nviz_init_light.argtypes = [POINTER(nv_data), c_int]
    Nviz_init_light.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_new_light'):
        continue
    Nviz_new_light = _lib.Nviz_new_light
    Nviz_new_light.argtypes = [POINTER(nv_data)]
    Nviz_new_light.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 60
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_model'):
        continue
    Nviz_draw_model = _lib.Nviz_draw_model
    Nviz_draw_model.argtypes = [POINTER(nv_data)]
    Nviz_draw_model.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_new_map_obj'):
        continue
    Nviz_new_map_obj = _lib.Nviz_new_map_obj
    Nviz_new_map_obj.argtypes = [c_int, String, c_double, POINTER(nv_data)]
    Nviz_new_map_obj.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 64
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_attr'):
        continue
    Nviz_set_attr = _lib.Nviz_set_attr
    Nviz_set_attr.argtypes = [c_int, c_int, c_int, c_int, String, c_double, POINTER(nv_data)]
    Nviz_set_attr.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_surface_attr_default'):
        continue
    Nviz_set_surface_attr_default = _lib.Nviz_set_surface_attr_default
    Nviz_set_surface_attr_default.argtypes = []
    Nviz_set_surface_attr_default.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_vpoint_attr_default'):
        continue
    Nviz_set_vpoint_attr_default = _lib.Nviz_set_vpoint_attr_default
    Nviz_set_vpoint_attr_default.argtypes = []
    Nviz_set_vpoint_attr_default.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 67
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_volume_attr_default'):
        continue
    Nviz_set_volume_attr_default = _lib.Nviz_set_volume_attr_default
    Nviz_set_volume_attr_default.argtypes = []
    Nviz_set_volume_attr_default.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 68
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_unset_attr'):
        continue
    Nviz_unset_attr = _lib.Nviz_unset_attr
    Nviz_unset_attr.argtypes = [c_int, c_int, c_int]
    Nviz_unset_attr.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 71
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_init_data'):
        continue
    Nviz_init_data = _lib.Nviz_init_data
    Nviz_init_data.argtypes = [POINTER(nv_data)]
    Nviz_init_data.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_destroy_data'):
        continue
    Nviz_destroy_data = _lib.Nviz_destroy_data
    Nviz_destroy_data.argtypes = [POINTER(nv_data)]
    Nviz_destroy_data.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 73
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_bgcolor'):
        continue
    Nviz_set_bgcolor = _lib.Nviz_set_bgcolor
    Nviz_set_bgcolor.argtypes = [POINTER(nv_data), c_int]
    Nviz_set_bgcolor.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 74
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_bgcolor'):
        continue
    Nviz_get_bgcolor = _lib.Nviz_get_bgcolor
    Nviz_get_bgcolor.argtypes = [POINTER(nv_data)]
    Nviz_get_bgcolor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 75
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_color_from_str'):
        continue
    Nviz_color_from_str = _lib.Nviz_color_from_str
    Nviz_color_from_str.argtypes = [String]
    Nviz_color_from_str.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 76
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_new_fringe'):
        continue
    Nviz_new_fringe = _lib.Nviz_new_fringe
    Nviz_new_fringe.argtypes = [POINTER(nv_data), c_int, c_ulong, c_double, c_int, c_int, c_int, c_int]
    Nviz_new_fringe.restype = POINTER(struct_fringe_data)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 78
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_fringe'):
        continue
    Nviz_set_fringe = _lib.Nviz_set_fringe
    Nviz_set_fringe.argtypes = [POINTER(nv_data), c_int, c_ulong, c_double, c_int, c_int, c_int, c_int]
    Nviz_set_fringe.restype = POINTER(struct_fringe_data)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 80
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_fringe'):
        continue
    Nviz_draw_fringe = _lib.Nviz_draw_fringe
    Nviz_draw_fringe.argtypes = [POINTER(nv_data)]
    Nviz_draw_fringe.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_arrow'):
        continue
    Nviz_draw_arrow = _lib.Nviz_draw_arrow
    Nviz_draw_arrow.argtypes = [POINTER(nv_data)]
    Nviz_draw_arrow.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 82
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_arrow'):
        continue
    Nviz_set_arrow = _lib.Nviz_set_arrow
    Nviz_set_arrow.argtypes = [POINTER(nv_data), c_int, c_int, c_float, c_uint]
    Nviz_set_arrow.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 83
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_delete_arrow'):
        continue
    Nviz_delete_arrow = _lib.Nviz_delete_arrow
    Nviz_delete_arrow.argtypes = [POINTER(nv_data)]
    Nviz_delete_arrow.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_new_scalebar'):
        continue
    Nviz_new_scalebar = _lib.Nviz_new_scalebar
    Nviz_new_scalebar.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), c_float, c_uint]
    Nviz_new_scalebar.restype = POINTER(struct_scalebar_data)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_scalebar'):
        continue
    Nviz_set_scalebar = _lib.Nviz_set_scalebar
    Nviz_set_scalebar.argtypes = [POINTER(nv_data), c_int, c_int, c_int, c_float, c_uint]
    Nviz_set_scalebar.restype = POINTER(struct_scalebar_data)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_draw_scalebar'):
        continue
    Nviz_draw_scalebar = _lib.Nviz_draw_scalebar
    Nviz_draw_scalebar.argtypes = [POINTER(nv_data)]
    Nviz_draw_scalebar.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_delete_scalebar'):
        continue
    Nviz_delete_scalebar = _lib.Nviz_delete_scalebar
    Nviz_delete_scalebar.argtypes = [POINTER(nv_data), c_int]
    Nviz_delete_scalebar.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 90
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_init_view'):
        continue
    Nviz_init_view = _lib.Nviz_init_view
    Nviz_init_view.argtypes = [POINTER(nv_data)]
    Nviz_init_view.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 91
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_focus_state'):
        continue
    Nviz_set_focus_state = _lib.Nviz_set_focus_state
    Nviz_set_focus_state.argtypes = [c_int]
    Nviz_set_focus_state.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 92
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_focus_map'):
        continue
    Nviz_set_focus_map = _lib.Nviz_set_focus_map
    Nviz_set_focus_map.argtypes = [c_int, c_int]
    Nviz_set_focus_map.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 93
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_has_focus'):
        continue
    Nviz_has_focus = _lib.Nviz_has_focus
    Nviz_has_focus.argtypes = [POINTER(nv_data)]
    Nviz_has_focus.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 94
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_set_focus'):
        continue
    Nviz_set_focus = _lib.Nviz_set_focus
    Nviz_set_focus.argtypes = [POINTER(nv_data), c_float, c_float, c_float]
    Nviz_set_focus.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 95
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_focus'):
        continue
    Nviz_get_focus = _lib.Nviz_get_focus
    Nviz_get_focus.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    Nviz_get_focus.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_xyrange'):
        continue
    Nviz_get_xyrange = _lib.Nviz_get_xyrange
    Nviz_get_xyrange.argtypes = [POINTER(nv_data)]
    Nviz_get_xyrange.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 97
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_zrange'):
        continue
    Nviz_get_zrange = _lib.Nviz_get_zrange
    Nviz_get_zrange.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_float)]
    Nviz_get_zrange.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 98
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_get_longdim'):
        continue
    Nviz_get_longdim = _lib.Nviz_get_longdim
    Nviz_get_longdim.argtypes = [POINTER(nv_data)]
    Nviz_get_longdim.restype = c_float
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 101
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_new_render_window'):
        continue
    Nviz_new_render_window = _lib.Nviz_new_render_window
    Nviz_new_render_window.argtypes = []
    Nviz_new_render_window.restype = POINTER(struct_render_window)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 102
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_init_render_window'):
        continue
    Nviz_init_render_window = _lib.Nviz_init_render_window
    Nviz_init_render_window.argtypes = [POINTER(struct_render_window)]
    Nviz_init_render_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_destroy_render_window'):
        continue
    Nviz_destroy_render_window = _lib.Nviz_destroy_render_window
    Nviz_destroy_render_window.argtypes = [POINTER(struct_render_window)]
    Nviz_destroy_render_window.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 104
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_create_render_window'):
        continue
    Nviz_create_render_window = _lib.Nviz_create_render_window
    Nviz_create_render_window.argtypes = [POINTER(struct_render_window), POINTER(None), c_int, c_int]
    Nviz_create_render_window.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 105
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Nviz_make_current_render_window'):
        continue
    Nviz_make_current_render_window = _lib.Nviz_make_current_render_window
    Nviz_make_current_render_window.argtypes = [POINTER(struct_render_window)]
    Nviz_make_current_render_window.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/ogsf.h: 30
try:
    GS_UNIT_SIZE = 1000.0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 42
try:
    MAP_OBJ_UNDEFINED = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 43
try:
    MAP_OBJ_SURF = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 44
try:
    MAP_OBJ_VOL = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 45
try:
    MAP_OBJ_VECT = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 46
try:
    MAP_OBJ_SITE = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 48
try:
    DRAW_COARSE = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 49
try:
    DRAW_FINE = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 50
try:
    DRAW_BOTH = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 53
try:
    DRAW_QUICK_SURFACE = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 54
try:
    DRAW_QUICK_VLINES = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 55
try:
    DRAW_QUICK_VPOINTS = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 56
try:
    DRAW_QUICK_VOLUME = 8
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 58
try:
    RANGE = (5 * GS_UNIT_SIZE)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 59
try:
    RANGE_OFFSET = (2 * GS_UNIT_SIZE)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 60
try:
    ZRANGE = (3 * GS_UNIT_SIZE)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 61
try:
    ZRANGE_OFFSET = (1 * GS_UNIT_SIZE)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 63
try:
    DEFAULT_SURF_COLOR = 3390463
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 65
try:
    FORMAT_PPM = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 66
try:
    FORMAT_TIF = 2
except:
    pass

fringe_data = struct_fringe_data # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 78

arrow_data = struct_arrow_data # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 86

scalebar_data = struct_scalebar_data # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 93

render_window = struct_render_window # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 132

# No inserted files

