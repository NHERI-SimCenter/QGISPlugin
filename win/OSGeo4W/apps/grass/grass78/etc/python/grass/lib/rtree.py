'''Wrapper for rtree.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_rtree.7.8 D:/src/osgeo4w/src/grass/grass-7.8.7/dist.x86_64-w64-mingw32/include/grass/rtree.h -o OBJ.x86_64-w64-mingw32/rtree.py

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

_libs["grass_rtree.7.8"] = load_library("grass_rtree.7.8")

# 1 libraries
# End libraries

# No modules

off_t = c_int64 # D:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/_mingw_off_t.h: 24

RectReal = c_double # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 28

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 57
class struct_RTree_Rect(Structure):
    pass

struct_RTree_Rect.__slots__ = [
    'boundary',
]
struct_RTree_Rect._fields_ = [
    ('boundary', POINTER(RectReal)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 77
class struct_RTree_Node(Structure):
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 64
class union_RTree_Child(Union):
    pass

union_RTree_Child.__slots__ = [
    'id',
    'ptr',
    'pos',
]
union_RTree_Child._fields_ = [
    ('id', c_int),
    ('ptr', POINTER(struct_RTree_Node)),
    ('pos', off_t),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 71
class struct_RTree_Branch(Structure):
    pass

struct_RTree_Branch.__slots__ = [
    'rect',
    'child',
]
struct_RTree_Branch._fields_ = [
    ('rect', struct_RTree_Rect),
    ('child', union_RTree_Child),
]

struct_RTree_Node.__slots__ = [
    'count',
    'level',
    'branch',
]
struct_RTree_Node._fields_ = [
    ('count', c_int),
    ('level', c_int),
    ('branch', POINTER(struct_RTree_Branch)),
]

SearchHitCallback = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(struct_RTree_Rect), POINTER(None)) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 91

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 128
class struct_RTree(Structure):
    pass

rt_search_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(SearchHitCallback), POINTER(None)) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 95

rt_insert_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, c_int, POINTER(struct_RTree)) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 97

rt_delete_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, POINTER(struct_RTree)) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 98

rt_valid_child_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(union_RTree_Child)) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 99

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 103
class struct_nstack(Structure):
    pass

struct_nstack.__slots__ = [
    'sn',
    'branch_id',
    'pos',
]
struct_nstack._fields_ = [
    ('sn', POINTER(struct_RTree_Node)),
    ('branch_id', c_int),
    ('pos', off_t),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 111
class struct_NodeBuffer(Structure):
    pass

struct_NodeBuffer.__slots__ = [
    'n',
    'pos',
    'dirty',
]
struct_NodeBuffer._fields_ = [
    ('n', struct_RTree_Node),
    ('pos', off_t),
    ('dirty', c_char),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 119
class struct_RTree_PartitionVars(Structure):
    pass

struct_RTree_PartitionVars.__slots__ = [
    'partition',
    'total',
    'minfill',
    'taken',
    'count',
    'cover',
    'area',
]
struct_RTree_PartitionVars._fields_ = [
    ('partition', c_int * (9 + 1)),
    ('total', c_int),
    ('minfill', c_int),
    ('taken', c_int * (9 + 1)),
    ('count', c_int * 2),
    ('cover', struct_RTree_Rect * 2),
    ('area', RectReal * 2),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 155
class struct__recycle(Structure):
    pass

struct__recycle.__slots__ = [
    'avail',
    'alloc',
    'pos',
]
struct__recycle._fields_ = [
    ('avail', c_int),
    ('alloc', c_int),
    ('pos', POINTER(off_t)),
]

struct_RTree.__slots__ = [
    'fd',
    'ndims',
    'nsides',
    'ndims_alloc',
    'nsides_alloc',
    'nodesize',
    'branchsize',
    'rectsize',
    'n_nodes',
    'n_leafs',
    'rootlevel',
    'nodecard',
    'leafcard',
    'min_node_fill',
    'min_leaf_fill',
    'minfill_node_split',
    'minfill_leaf_split',
    'overflow',
    'free_nodes',
    'nb',
    'used',
    'insert_rect',
    'delete_rect',
    'search_rect',
    'valid_child',
    'root',
    'ns',
    'p',
    'BranchBuf',
    'tmpb1',
    'tmpb2',
    'c',
    'BranchCount',
    'rect_0',
    'rect_1',
    'upperrect',
    'orect',
    'center_n',
    'rootpos',
]
struct_RTree._fields_ = [
    ('fd', c_int),
    ('ndims', c_ubyte),
    ('nsides', c_ubyte),
    ('ndims_alloc', c_ubyte),
    ('nsides_alloc', c_ubyte),
    ('nodesize', c_int),
    ('branchsize', c_int),
    ('rectsize', c_int),
    ('n_nodes', c_int),
    ('n_leafs', c_int),
    ('rootlevel', c_int),
    ('nodecard', c_int),
    ('leafcard', c_int),
    ('min_node_fill', c_int),
    ('min_leaf_fill', c_int),
    ('minfill_node_split', c_int),
    ('minfill_leaf_split', c_int),
    ('overflow', c_char),
    ('free_nodes', struct__recycle),
    ('nb', POINTER(POINTER(struct_NodeBuffer))),
    ('used', POINTER(POINTER(c_int))),
    ('insert_rect', POINTER(rt_insert_fn)),
    ('delete_rect', POINTER(rt_delete_fn)),
    ('search_rect', POINTER(rt_search_fn)),
    ('valid_child', POINTER(rt_valid_child_fn)),
    ('root', POINTER(struct_RTree_Node)),
    ('ns', POINTER(struct_nstack)),
    ('p', struct_RTree_PartitionVars),
    ('BranchBuf', POINTER(struct_RTree_Branch)),
    ('tmpb1', struct_RTree_Branch),
    ('tmpb2', struct_RTree_Branch),
    ('c', struct_RTree_Branch),
    ('BranchCount', c_int),
    ('rect_0', struct_RTree_Rect),
    ('rect_1', struct_RTree_Rect),
    ('upperrect', struct_RTree_Rect),
    ('orect', struct_RTree_Rect),
    ('center_n', POINTER(RectReal)),
    ('rootpos', off_t),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 196
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeSearch'):
        continue
    RTreeSearch = _lib.RTreeSearch
    RTreeSearch.argtypes = [POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(SearchHitCallback), POINTER(None)]
    RTreeSearch.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 198
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeInsertRect'):
        continue
    RTreeInsertRect = _lib.RTreeInsertRect
    RTreeInsertRect.argtypes = [POINTER(struct_RTree_Rect), c_int, POINTER(struct_RTree)]
    RTreeInsertRect.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 199
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeSetRect1D'):
        continue
    RTreeSetRect1D = _lib.RTreeSetRect1D
    RTreeSetRect1D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double]
    RTreeSetRect1D.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 201
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeSetRect2D'):
        continue
    RTreeSetRect2D = _lib.RTreeSetRect2D
    RTreeSetRect2D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double, c_double, c_double]
    RTreeSetRect2D.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 203
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeSetRect3D'):
        continue
    RTreeSetRect3D = _lib.RTreeSetRect3D
    RTreeSetRect3D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double, c_double, c_double, c_double, c_double]
    RTreeSetRect3D.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 206
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeSetRect4D'):
        continue
    RTreeSetRect4D = _lib.RTreeSetRect4D
    RTreeSetRect4D.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]
    RTreeSetRect4D.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 209
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeDeleteRect'):
        continue
    RTreeDeleteRect = _lib.RTreeDeleteRect
    RTreeDeleteRect.argtypes = [POINTER(struct_RTree_Rect), c_int, POINTER(struct_RTree)]
    RTreeDeleteRect.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 210
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreePrintRect'):
        continue
    RTreePrintRect = _lib.RTreePrintRect
    RTreePrintRect.argtypes = [POINTER(struct_RTree_Rect), c_int, POINTER(struct_RTree)]
    RTreePrintRect.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 211
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeCreateTree'):
        continue
    RTreeCreateTree = _lib.RTreeCreateTree
    RTreeCreateTree.argtypes = [c_int, off_t, c_int]
    RTreeCreateTree.restype = POINTER(struct_RTree)
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 212
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeSetOverflow'):
        continue
    RTreeSetOverflow = _lib.RTreeSetOverflow
    RTreeSetOverflow.argtypes = [POINTER(struct_RTree), c_char]
    RTreeSetOverflow.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 213
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeDestroyTree'):
        continue
    RTreeDestroyTree = _lib.RTreeDestroyTree
    RTreeDestroyTree.argtypes = [POINTER(struct_RTree)]
    RTreeDestroyTree.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 214
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeOverlap'):
        continue
    RTreeOverlap = _lib.RTreeOverlap
    RTreeOverlap.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree_Rect), POINTER(struct_RTree)]
    RTreeOverlap.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 215
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeContained'):
        continue
    RTreeContained = _lib.RTreeContained
    RTreeContained.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree_Rect), POINTER(struct_RTree)]
    RTreeContained.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 216
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeContains'):
        continue
    RTreeContains = _lib.RTreeContains
    RTreeContains.argtypes = [POINTER(struct_RTree_Rect), POINTER(struct_RTree_Rect), POINTER(struct_RTree)]
    RTreeContains.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 219
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeAllocNode'):
        continue
    RTreeAllocNode = _lib.RTreeAllocNode
    RTreeAllocNode.argtypes = [POINTER(struct_RTree), c_int]
    RTreeAllocNode.restype = POINTER(struct_RTree_Node)
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 220
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeInitNode'):
        continue
    RTreeInitNode = _lib.RTreeInitNode
    RTreeInitNode.argtypes = [POINTER(struct_RTree), POINTER(struct_RTree_Node), c_int]
    RTreeInitNode.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 221
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeCopyNode'):
        continue
    RTreeCopyNode = _lib.RTreeCopyNode
    RTreeCopyNode.argtypes = [POINTER(struct_RTree_Node), POINTER(struct_RTree_Node), POINTER(struct_RTree)]
    RTreeCopyNode.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 222
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeFreeNode'):
        continue
    RTreeFreeNode = _lib.RTreeFreeNode
    RTreeFreeNode.argtypes = [POINTER(struct_RTree_Node)]
    RTreeFreeNode.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 223
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeDestroyNode'):
        continue
    RTreeDestroyNode = _lib.RTreeDestroyNode
    RTreeDestroyNode.argtypes = [POINTER(struct_RTree_Node), c_int]
    RTreeDestroyNode.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 226
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeAllocRect'):
        continue
    RTreeAllocRect = _lib.RTreeAllocRect
    RTreeAllocRect.argtypes = [POINTER(struct_RTree)]
    RTreeAllocRect.restype = POINTER(struct_RTree_Rect)
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 227
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeFreeRect'):
        continue
    RTreeFreeRect = _lib.RTreeFreeRect
    RTreeFreeRect.argtypes = [POINTER(struct_RTree_Rect)]
    RTreeFreeRect.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 228
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeAllocBoundary'):
        continue
    RTreeAllocBoundary = _lib.RTreeAllocBoundary
    RTreeAllocBoundary.argtypes = [POINTER(struct_RTree)]
    RTreeAllocBoundary.restype = POINTER(RectReal)
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 229
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeFreeBoundary'):
        continue
    RTreeFreeBoundary = _lib.RTreeFreeBoundary
    RTreeFreeBoundary.argtypes = [POINTER(struct_RTree_Rect)]
    RTreeFreeBoundary.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 232
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeReadNode'):
        continue
    RTreeReadNode = _lib.RTreeReadNode
    RTreeReadNode.argtypes = [POINTER(struct_RTree_Node), off_t, POINTER(struct_RTree)]
    RTreeReadNode.restype = c_size_t
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 233
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeWriteNode'):
        continue
    RTreeWriteNode = _lib.RTreeWriteNode
    RTreeWriteNode.argtypes = [POINTER(struct_RTree_Node), POINTER(struct_RTree)]
    RTreeWriteNode.restype = c_size_t
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 234
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeGetNodePos'):
        continue
    RTreeGetNodePos = _lib.RTreeGetNodePos
    RTreeGetNodePos.argtypes = [POINTER(struct_RTree)]
    RTreeGetNodePos.restype = off_t
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 235
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'RTreeFlushBuffer'):
        continue
    RTreeFlushBuffer = _lib.RTreeFlushBuffer
    RTreeFlushBuffer.argtypes = [POINTER(struct_RTree)]
    RTreeFlushBuffer.restype = None
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 35
try:
    TRUE = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 38
try:
    FALSE = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 46
try:
    MAXCARD = 9
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 47
try:
    NODECARD = MAXCARD
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 48
try:
    LEAFCARD = MAXCARD
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 52
try:
    MAXLEVEL = 20
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 55
try:
    NODE_BUFFER_SIZE = 32
except:
    pass

RTree_Rect = struct_RTree_Rect # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 57

RTree_Node = struct_RTree_Node # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 77

RTree_Child = union_RTree_Child # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 64

RTree_Branch = struct_RTree_Branch # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 71

RTree = struct_RTree # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 128

nstack = struct_nstack # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 103

NodeBuffer = struct_NodeBuffer # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 111

RTree_PartitionVars = struct_RTree_PartitionVars # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 119

_recycle = struct__recycle # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.7\\dist.x86_64-w64-mingw32\\include\\grass\\rtree.h: 155

# No inserted files

