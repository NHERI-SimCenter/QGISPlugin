'''Wrapper for dbmi.h

Generated with:
./ctypesgen.py --cpp x86_64-w64-mingw32-gcc -E -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include -D_FILE_OFFSET_BITS=64      -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -I/d/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_dbmiclient.7.8 -lgrass_dbmibase.7.8 D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/dbmi.h D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h -o OBJ.x86_64-w64-mingw32/dbmi.py

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

_libs["grass_dbmiclient.7.8"] = load_library("grass_dbmiclient.7.8")
_libs["grass_dbmibase.7.8"] = load_library("grass_dbmibase.7.8")

# 2 libraries
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

dbAddress = POINTER(None) # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 144

dbToken = c_int # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 145

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 151
class struct__db_string(Structure):
    pass

struct__db_string.__slots__ = [
    'string',
    'nalloc',
]
struct__db_string._fields_ = [
    ('string', String),
    ('nalloc', c_int),
]

dbString = struct__db_string # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 151

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 153
class struct__dbmscap(Structure):
    pass

struct__dbmscap.__slots__ = [
    'driverName',
    'startup',
    'comment',
    'next',
]
struct__dbmscap._fields_ = [
    ('driverName', c_char * 256),
    ('startup', c_char * 256),
    ('comment', c_char * 256),
    ('next', POINTER(struct__dbmscap)),
]

dbDbmscap = struct__dbmscap # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 159

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 166
class struct__db_dirent(Structure):
    pass

struct__db_dirent.__slots__ = [
    'name',
    'isdir',
    'perm',
]
struct__db_dirent._fields_ = [
    ('name', dbString),
    ('isdir', c_int),
    ('perm', c_int),
]

dbDirent = struct__db_dirent # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 166

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 173
class struct__db_driver(Structure):
    pass

struct__db_driver.__slots__ = [
    'dbmscap',
    'send',
    'recv',
    'pid',
]
struct__db_driver._fields_ = [
    ('dbmscap', dbDbmscap),
    ('send', POINTER(FILE)),
    ('recv', POINTER(FILE)),
    ('pid', c_int),
]

dbDriver = struct__db_driver # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 173

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 180
class struct__db_handle(Structure):
    pass

struct__db_handle.__slots__ = [
    'dbName',
    'dbSchema',
]
struct__db_handle._fields_ = [
    ('dbName', dbString),
    ('dbSchema', dbString),
]

dbHandle = struct__db_handle # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 180

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 191
class struct__db_date_time(Structure):
    pass

struct__db_date_time.__slots__ = [
    'current',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'seconds',
]
struct__db_date_time._fields_ = [
    ('current', c_char),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('seconds', c_double),
]

dbDateTime = struct__db_date_time # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 191

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 200
class struct__db_value(Structure):
    pass

struct__db_value.__slots__ = [
    'isNull',
    'i',
    'd',
    's',
    't',
]
struct__db_value._fields_ = [
    ('isNull', c_char),
    ('i', c_int),
    ('d', c_double),
    ('s', dbString),
    ('t', dbDateTime),
]

dbValue = struct__db_value # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 200

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 218
class struct__db_column(Structure):
    pass

struct__db_column.__slots__ = [
    'columnName',
    'description',
    'sqlDataType',
    'hostDataType',
    'value',
    'dataLen',
    'precision',
    'scale',
    'nullAllowed',
    'hasDefaultValue',
    'useDefaultValue',
    'defaultValue',
    'select',
    'update',
]
struct__db_column._fields_ = [
    ('columnName', dbString),
    ('description', dbString),
    ('sqlDataType', c_int),
    ('hostDataType', c_int),
    ('value', dbValue),
    ('dataLen', c_int),
    ('precision', c_int),
    ('scale', c_int),
    ('nullAllowed', c_char),
    ('hasDefaultValue', c_char),
    ('useDefaultValue', c_char),
    ('defaultValue', dbValue),
    ('select', c_int),
    ('update', c_int),
]

dbColumn = struct__db_column # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 218

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 228
class struct__db_table(Structure):
    pass

struct__db_table.__slots__ = [
    'tableName',
    'description',
    'numColumns',
    'columns',
    'priv_insert',
    'priv_delete',
]
struct__db_table._fields_ = [
    ('tableName', dbString),
    ('description', dbString),
    ('numColumns', c_int),
    ('columns', POINTER(dbColumn)),
    ('priv_insert', c_int),
    ('priv_delete', c_int),
]

dbTable = struct__db_table # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 228

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 238
class struct__db_cursor(Structure):
    pass

struct__db_cursor.__slots__ = [
    'token',
    'driver',
    'table',
    'column_flags',
    'type',
    'mode',
]
struct__db_cursor._fields_ = [
    ('token', dbToken),
    ('driver', POINTER(dbDriver)),
    ('table', POINTER(dbTable)),
    ('column_flags', POINTER(c_short)),
    ('type', c_int),
    ('mode', c_int),
]

dbCursor = struct__db_cursor # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 238

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 247
class struct__db_index(Structure):
    pass

struct__db_index.__slots__ = [
    'indexName',
    'tableName',
    'numColumns',
    'columnNames',
    'unique',
]
struct__db_index._fields_ = [
    ('indexName', dbString),
    ('tableName', dbString),
    ('numColumns', c_int),
    ('columnNames', POINTER(dbString)),
    ('unique', c_char),
]

dbIndex = struct__db_index # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 247

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 256
class struct__db_driver_state(Structure):
    pass

struct__db_driver_state.__slots__ = [
    'dbname',
    'dbschema',
    'open',
    'ncursors',
    'cursor_list',
]
struct__db_driver_state._fields_ = [
    ('dbname', String),
    ('dbschema', String),
    ('open', c_int),
    ('ncursors', c_int),
    ('cursor_list', POINTER(POINTER(dbCursor))),
]

dbDriverState = struct__db_driver_state # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 256

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 263
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'cat',
    'val',
]
struct_anon_7._fields_ = [
    ('cat', c_int),
    ('val', c_int),
]

dbCatValI = struct_anon_7 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 263

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 270
class union_anon_8(Union):
    pass

union_anon_8.__slots__ = [
    'i',
    'd',
    's',
    't',
]
union_anon_8._fields_ = [
    ('i', c_int),
    ('d', c_double),
    ('s', POINTER(dbString)),
    ('t', POINTER(dbDateTime)),
]

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 281
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'cat',
    'isNull',
    'val',
]
struct_anon_9._fields_ = [
    ('cat', c_int),
    ('isNull', c_int),
    ('val', union_anon_8),
]

dbCatVal = struct_anon_9 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 281

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 290
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'n_values',
    'alloc',
    'ctype',
    'value',
]
struct_anon_10._fields_ = [
    ('n_values', c_int),
    ('alloc', c_int),
    ('ctype', c_int),
    ('value', POINTER(dbCatVal)),
]

dbCatValArray = struct_anon_10 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 290

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 304
class struct__db_connection(Structure):
    pass

struct__db_connection.__slots__ = [
    'driverName',
    'hostName',
    'databaseName',
    'schemaName',
    'port',
    'user',
    'password',
    'keycol',
    'group',
]
struct__db_connection._fields_ = [
    ('driverName', String),
    ('hostName', String),
    ('databaseName', String),
    ('schemaName', String),
    ('port', String),
    ('user', String),
    ('password', String),
    ('keycol', String),
    ('group', String),
]

dbConnection = struct__db_connection # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 304

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 316
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'count',
    'alloc',
    'table',
    'key',
    'cat',
    'where',
    'label',
]
struct_anon_11._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('table', String),
    ('key', String),
    ('cat', POINTER(c_int)),
    ('where', POINTER(POINTER(c_char))),
    ('label', POINTER(POINTER(c_char))),
]

dbRclsRule = struct_anon_11 # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 316

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 4
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_Cstring_to_lowercase'):
        continue
    db_Cstring_to_lowercase = _lib.db_Cstring_to_lowercase
    db_Cstring_to_lowercase.argtypes = [String]
    db_Cstring_to_lowercase.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_Cstring_to_uppercase'):
        continue
    db_Cstring_to_uppercase = _lib.db_Cstring_to_uppercase
    db_Cstring_to_uppercase.argtypes = [String]
    db_Cstring_to_uppercase.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_add_column'):
        continue
    db_add_column = _lib.db_add_column
    db_add_column.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbColumn)]
    db_add_column.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__add_cursor_to_driver_state'):
        continue
    db__add_cursor_to_driver_state = _lib.db__add_cursor_to_driver_state
    db__add_cursor_to_driver_state.argtypes = [POINTER(dbCursor)]
    db__add_cursor_to_driver_state.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_cursor_column_flags'):
        continue
    db_alloc_cursor_column_flags = _lib.db_alloc_cursor_column_flags
    db_alloc_cursor_column_flags.argtypes = [POINTER(dbCursor)]
    db_alloc_cursor_column_flags.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_cursor_table'):
        continue
    db_alloc_cursor_table = _lib.db_alloc_cursor_table
    db_alloc_cursor_table.argtypes = [POINTER(dbCursor), c_int]
    db_alloc_cursor_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_append_table_column'):
        continue
    db_append_table_column = _lib.db_append_table_column
    db_append_table_column.argtypes = [POINTER(dbTable), POINTER(dbColumn)]
    db_append_table_column.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_dirent_array'):
        continue
    db_alloc_dirent_array = _lib.db_alloc_dirent_array
    db_alloc_dirent_array.argtypes = [c_int]
    db_alloc_dirent_array.restype = POINTER(dbDirent)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_handle_array'):
        continue
    db_alloc_handle_array = _lib.db_alloc_handle_array
    db_alloc_handle_array.argtypes = [c_int]
    db_alloc_handle_array.restype = POINTER(dbHandle)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_index_array'):
        continue
    db_alloc_index_array = _lib.db_alloc_index_array
    db_alloc_index_array.argtypes = [c_int]
    db_alloc_index_array.restype = POINTER(dbIndex)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_index_columns'):
        continue
    db_alloc_index_columns = _lib.db_alloc_index_columns
    db_alloc_index_columns.argtypes = [POINTER(dbIndex), c_int]
    db_alloc_index_columns.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_string_array'):
        continue
    db_alloc_string_array = _lib.db_alloc_string_array
    db_alloc_string_array.argtypes = [c_int]
    db_alloc_string_array.restype = POINTER(dbString)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_alloc_table'):
        continue
    db_alloc_table = _lib.db_alloc_table
    db_alloc_table.argtypes = [c_int]
    db_alloc_table.restype = POINTER(dbTable)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_append_string'):
        continue
    db_append_string = _lib.db_append_string
    db_append_string.argtypes = [POINTER(dbString), String]
    db_append_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_auto_print_errors'):
        continue
    db_auto_print_errors = _lib.db_auto_print_errors
    db_auto_print_errors.argtypes = [c_int]
    db_auto_print_errors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 19
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_auto_print_protocol_errors'):
        continue
    db_auto_print_protocol_errors = _lib.db_auto_print_protocol_errors
    db_auto_print_protocol_errors.argtypes = [c_int]
    db_auto_print_protocol_errors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_bind_update'):
        continue
    db_bind_update = _lib.db_bind_update
    db_bind_update.argtypes = [POINTER(dbCursor)]
    db_bind_update.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_calloc'):
        continue
    db_calloc = _lib.db_calloc
    db_calloc.argtypes = [c_int, c_int]
    db_calloc.restype = POINTER(c_ubyte)
    db_calloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_alloc'):
        continue
    db_CatValArray_alloc = _lib.db_CatValArray_alloc
    db_CatValArray_alloc.argtypes = [POINTER(dbCatValArray), c_int]
    db_CatValArray_alloc.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_realloc'):
        continue
    db_CatValArray_realloc = _lib.db_CatValArray_realloc
    db_CatValArray_realloc.argtypes = [POINTER(dbCatValArray), c_int]
    db_CatValArray_realloc.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_free'):
        continue
    db_CatValArray_free = _lib.db_CatValArray_free
    db_CatValArray_free.argtypes = [POINTER(dbCatValArray)]
    db_CatValArray_free.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_init'):
        continue
    db_CatValArray_init = _lib.db_CatValArray_init
    db_CatValArray_init.argtypes = [POINTER(dbCatValArray)]
    db_CatValArray_init.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 26
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_sort'):
        continue
    db_CatValArray_sort = _lib.db_CatValArray_sort
    db_CatValArray_sort.argtypes = [POINTER(dbCatValArray)]
    db_CatValArray_sort.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 27
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_sort_by_value'):
        continue
    db_CatValArray_sort_by_value = _lib.db_CatValArray_sort_by_value
    db_CatValArray_sort_by_value.argtypes = [POINTER(dbCatValArray)]
    db_CatValArray_sort_by_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 28
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_get_value'):
        continue
    db_CatValArray_get_value = _lib.db_CatValArray_get_value
    db_CatValArray_get_value.argtypes = [POINTER(dbCatValArray), c_int, POINTER(POINTER(dbCatVal))]
    db_CatValArray_get_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_get_value_int'):
        continue
    db_CatValArray_get_value_int = _lib.db_CatValArray_get_value_int
    db_CatValArray_get_value_int.argtypes = [POINTER(dbCatValArray), c_int, POINTER(c_int)]
    db_CatValArray_get_value_int.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_CatValArray_get_value_double'):
        continue
    db_CatValArray_get_value_double = _lib.db_CatValArray_get_value_double
    db_CatValArray_get_value_double.argtypes = [POINTER(dbCatValArray), c_int, POINTER(c_double)]
    db_CatValArray_get_value_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 32
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_char_to_lowercase'):
        continue
    db_char_to_lowercase = _lib.db_char_to_lowercase
    db_char_to_lowercase.argtypes = [String]
    db_char_to_lowercase.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_char_to_uppercase'):
        continue
    db_char_to_uppercase = _lib.db_char_to_uppercase
    db_char_to_uppercase.argtypes = [String]
    db_char_to_uppercase.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_clear_error'):
        continue
    db_clear_error = _lib.db_clear_error
    db_clear_error.argtypes = []
    db_clear_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 35
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_clone_table'):
        continue
    db_clone_table = _lib.db_clone_table
    db_clone_table.argtypes = [POINTER(dbTable)]
    db_clone_table.restype = POINTER(dbTable)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 36
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__close_all_cursors'):
        continue
    db__close_all_cursors = _lib.db__close_all_cursors
    db__close_all_cursors.argtypes = []
    db__close_all_cursors.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 37
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_close_cursor'):
        continue
    db_close_cursor = _lib.db_close_cursor
    db_close_cursor.argtypes = [POINTER(dbCursor)]
    db_close_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 38
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_close_database'):
        continue
    db_close_database = _lib.db_close_database
    db_close_database.argtypes = [POINTER(dbDriver)]
    db_close_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 39
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_close_database_shutdown_driver'):
        continue
    db_close_database_shutdown_driver = _lib.db_close_database_shutdown_driver
    db_close_database_shutdown_driver.argtypes = [POINTER(dbDriver)]
    db_close_database_shutdown_driver.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 40
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_column_sqltype'):
        continue
    db_column_sqltype = _lib.db_column_sqltype
    db_column_sqltype.argtypes = [POINTER(dbDriver), String, String]
    db_column_sqltype.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 41
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_column_Ctype'):
        continue
    db_column_Ctype = _lib.db_column_Ctype
    db_column_Ctype.argtypes = [POINTER(dbDriver), String, String]
    db_column_Ctype.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 42
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_Cstring_to_column_default_value'):
        continue
    db_convert_Cstring_to_column_default_value = _lib.db_convert_Cstring_to_column_default_value
    db_convert_Cstring_to_column_default_value.argtypes = [String, POINTER(dbColumn)]
    db_convert_Cstring_to_column_default_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 44
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_Cstring_to_column_value'):
        continue
    db_convert_Cstring_to_column_value = _lib.db_convert_Cstring_to_column_value
    db_convert_Cstring_to_column_value.argtypes = [String, POINTER(dbColumn)]
    db_convert_Cstring_to_column_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_Cstring_to_value'):
        continue
    db_convert_Cstring_to_value = _lib.db_convert_Cstring_to_value
    db_convert_Cstring_to_value.argtypes = [String, c_int, POINTER(dbValue)]
    db_convert_Cstring_to_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 48
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_Cstring_to_value_datetime'):
        continue
    db_convert_Cstring_to_value_datetime = _lib.db_convert_Cstring_to_value_datetime
    db_convert_Cstring_to_value_datetime.argtypes = [String, c_int, POINTER(dbValue)]
    db_convert_Cstring_to_value_datetime.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 50
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_column_default_value_to_string'):
        continue
    db_convert_column_default_value_to_string = _lib.db_convert_column_default_value_to_string
    db_convert_column_default_value_to_string.argtypes = [POINTER(dbColumn), POINTER(dbString)]
    db_convert_column_default_value_to_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 52
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_column_value_to_string'):
        continue
    db_convert_column_value_to_string = _lib.db_convert_column_value_to_string
    db_convert_column_value_to_string.argtypes = [POINTER(dbColumn), POINTER(dbString)]
    db_convert_column_value_to_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_value_datetime_into_string'):
        continue
    db_convert_value_datetime_into_string = _lib.db_convert_value_datetime_into_string
    db_convert_value_datetime_into_string.argtypes = [POINTER(dbValue), c_int, POINTER(dbString)]
    db_convert_value_datetime_into_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_convert_value_to_string'):
        continue
    db_convert_value_to_string = _lib.db_convert_value_to_string
    db_convert_value_to_string.argtypes = [POINTER(dbValue), c_int, POINTER(dbString)]
    db_convert_value_to_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_column'):
        continue
    db_copy_column = _lib.db_copy_column
    db_copy_column.argtypes = [POINTER(dbColumn), POINTER(dbColumn)]
    db_copy_column.restype = POINTER(dbColumn)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 58
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_dbmscap_entry'):
        continue
    db_copy_dbmscap_entry = _lib.db_copy_dbmscap_entry
    db_copy_dbmscap_entry.argtypes = [POINTER(dbDbmscap), POINTER(dbDbmscap)]
    db_copy_dbmscap_entry.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_string'):
        continue
    db_copy_string = _lib.db_copy_string
    db_copy_string.argtypes = [POINTER(dbString), POINTER(dbString)]
    db_copy_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 60
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_table_to_sql'):
        continue
    db_table_to_sql = _lib.db_table_to_sql
    db_table_to_sql.argtypes = [POINTER(dbTable), POINTER(dbString)]
    db_table_to_sql.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_table'):
        continue
    db_copy_table = _lib.db_copy_table
    db_copy_table.argtypes = [String, String, String, String, String, String]
    db_copy_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_table_where'):
        continue
    db_copy_table_where = _lib.db_copy_table_where
    db_copy_table_where.argtypes = [String, String, String, String, String, String, String]
    db_copy_table_where.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_table_select'):
        continue
    db_copy_table_select = _lib.db_copy_table_select
    db_copy_table_select.argtypes = [String, String, String, String, String, String, String]
    db_copy_table_select.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 69
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_table_by_ints'):
        continue
    db_copy_table_by_ints = _lib.db_copy_table_by_ints
    db_copy_table_by_ints.argtypes = [String, String, String, String, String, String, String, POINTER(c_int), c_int]
    db_copy_table_by_ints.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_copy_value'):
        continue
    db_copy_value = _lib.db_copy_value
    db_copy_value.argtypes = [POINTER(dbValue), POINTER(dbValue)]
    db_copy_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 73
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_create_database'):
        continue
    db_create_database = _lib.db_create_database
    db_create_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle)]
    db_create_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 74
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_create_index'):
        continue
    db_create_index = _lib.db_create_index
    db_create_index.argtypes = [POINTER(dbDriver), POINTER(dbIndex)]
    db_create_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 75
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_create_index2'):
        continue
    db_create_index2 = _lib.db_create_index2
    db_create_index2.argtypes = [POINTER(dbDriver), String, String]
    db_create_index2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 77
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_create_table'):
        continue
    db_create_table = _lib.db_create_table
    db_create_table.argtypes = [POINTER(dbDriver), POINTER(dbTable)]
    db_create_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 78
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_add_column'):
        continue
    db_d_add_column = _lib.db_d_add_column
    db_d_add_column.argtypes = []
    db_d_add_column.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 79
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_bind_update'):
        continue
    db_d_bind_update = _lib.db_d_bind_update
    db_d_bind_update.argtypes = []
    db_d_bind_update.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 80
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_dbmscap_filename'):
        continue
    db_dbmscap_filename = _lib.db_dbmscap_filename
    db_dbmscap_filename.argtypes = []
    db_dbmscap_filename.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_close_cursor'):
        continue
    db_d_close_cursor = _lib.db_d_close_cursor
    db_d_close_cursor.argtypes = []
    db_d_close_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 82
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_close_database'):
        continue
    db_d_close_database = _lib.db_d_close_database
    db_d_close_database.argtypes = []
    db_d_close_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 83
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_create_database'):
        continue
    db_d_create_database = _lib.db_d_create_database
    db_d_create_database.argtypes = []
    db_d_create_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_create_index'):
        continue
    db_d_create_index = _lib.db_d_create_index
    db_d_create_index.argtypes = []
    db_d_create_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_create_table'):
        continue
    db_d_create_table = _lib.db_d_create_table
    db_d_create_table.argtypes = []
    db_d_create_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_delete'):
        continue
    db_d_delete = _lib.db_d_delete
    db_d_delete.argtypes = []
    db_d_delete.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_delete_database'):
        continue
    db_d_delete_database = _lib.db_d_delete_database
    db_d_delete_database.argtypes = []
    db_d_delete_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 88
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_describe_table'):
        continue
    db_d_describe_table = _lib.db_d_describe_table
    db_d_describe_table.argtypes = []
    db_d_describe_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 89
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_drop_column'):
        continue
    db_d_drop_column = _lib.db_d_drop_column
    db_d_drop_column.argtypes = []
    db_d_drop_column.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 90
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_drop_index'):
        continue
    db_d_drop_index = _lib.db_d_drop_index
    db_d_drop_index.argtypes = []
    db_d_drop_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 91
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_drop_table'):
        continue
    db_d_drop_table = _lib.db_d_drop_table
    db_d_drop_table.argtypes = []
    db_d_drop_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 92
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_debug'):
        continue
    db_debug = _lib.db_debug
    db_debug.argtypes = [String]
    db_debug.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 93
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_debug_off'):
        continue
    db_debug_off = _lib.db_debug_off
    db_debug_off.argtypes = []
    db_debug_off.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 94
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_debug_on'):
        continue
    db_debug_on = _lib.db_debug_on
    db_debug_on.argtypes = []
    db_debug_on.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 95
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_delete'):
        continue
    db_delete = _lib.db_delete
    db_delete.argtypes = [POINTER(dbCursor)]
    db_delete.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_delete_database'):
        continue
    db_delete_database = _lib.db_delete_database
    db_delete_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle)]
    db_delete_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 97
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_delete_table'):
        continue
    db_delete_table = _lib.db_delete_table
    db_delete_table.argtypes = [String, String, String]
    db_delete_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 98
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_describe_table'):
        continue
    db_describe_table = _lib.db_describe_table
    db_describe_table.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(POINTER(dbTable))]
    db_describe_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 99
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_execute_immediate'):
        continue
    db_d_execute_immediate = _lib.db_d_execute_immediate
    db_d_execute_immediate.argtypes = []
    db_d_execute_immediate.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 100
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_begin_transaction'):
        continue
    db_d_begin_transaction = _lib.db_d_begin_transaction
    db_d_begin_transaction.argtypes = []
    db_d_begin_transaction.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 101
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_commit_transaction'):
        continue
    db_d_commit_transaction = _lib.db_d_commit_transaction
    db_d_commit_transaction.argtypes = []
    db_d_commit_transaction.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 102
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_fetch'):
        continue
    db_d_fetch = _lib.db_d_fetch
    db_d_fetch.argtypes = []
    db_d_fetch.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_find_database'):
        continue
    db_d_find_database = _lib.db_d_find_database
    db_d_find_database.argtypes = []
    db_d_find_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 104
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_get_num_rows'):
        continue
    db_d_get_num_rows = _lib.db_d_get_num_rows
    db_d_get_num_rows.argtypes = []
    db_d_get_num_rows.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 105
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_grant_on_table'):
        continue
    db_d_grant_on_table = _lib.db_d_grant_on_table
    db_d_grant_on_table.argtypes = []
    db_d_grant_on_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 106
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_insert'):
        continue
    db_d_insert = _lib.db_d_insert
    db_d_insert.argtypes = []
    db_d_insert.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 107
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_init_error'):
        continue
    db_d_init_error = _lib.db_d_init_error
    db_d_init_error.argtypes = [String]
    db_d_init_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 108
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_append_error'):
        _func = _lib.db_d_append_error
        _restype = None
        _errcheck = None
        _argtypes = [String]
        db_d_append_error = _variadic_function(_func,_restype,_argtypes,_errcheck)

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 110
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_report_error'):
        continue
    db_d_report_error = _lib.db_d_report_error
    db_d_report_error.argtypes = []
    db_d_report_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 111
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_dirent'):
        continue
    db_dirent = _lib.db_dirent
    db_dirent.argtypes = [String, POINTER(c_int)]
    db_dirent.restype = POINTER(dbDirent)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 112
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_list_databases'):
        continue
    db_d_list_databases = _lib.db_d_list_databases
    db_d_list_databases.argtypes = []
    db_d_list_databases.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 113
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_list_indexes'):
        continue
    db_d_list_indexes = _lib.db_d_list_indexes
    db_d_list_indexes.argtypes = []
    db_d_list_indexes.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 114
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_list_tables'):
        continue
    db_d_list_tables = _lib.db_d_list_tables
    db_d_list_tables.argtypes = []
    db_d_list_tables.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 115
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_open_database'):
        continue
    db_d_open_database = _lib.db_d_open_database
    db_d_open_database.argtypes = []
    db_d_open_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 116
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_open_insert_cursor'):
        continue
    db_d_open_insert_cursor = _lib.db_d_open_insert_cursor
    db_d_open_insert_cursor.argtypes = []
    db_d_open_insert_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 117
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_open_select_cursor'):
        continue
    db_d_open_select_cursor = _lib.db_d_open_select_cursor
    db_d_open_select_cursor.argtypes = []
    db_d_open_select_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 118
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_open_update_cursor'):
        continue
    db_d_open_update_cursor = _lib.db_d_open_update_cursor
    db_d_open_update_cursor.argtypes = []
    db_d_open_update_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 119
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_double_quote_string'):
        continue
    db_double_quote_string = _lib.db_double_quote_string
    db_double_quote_string.argtypes = [POINTER(dbString)]
    db_double_quote_string.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 120
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_driver'):
        continue
    db_driver = _lib.db_driver
    db_driver.argtypes = [c_int, POINTER(POINTER(c_char))]
    db_driver.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 122
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_driver_mkdir'):
        continue
    db_driver_mkdir = _lib.db_driver_mkdir
    db_driver_mkdir.argtypes = [String, c_int, c_int]
    db_driver_mkdir.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 123
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_drop_column'):
        continue
    db_drop_column = _lib.db_drop_column
    db_drop_column.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbString)]
    db_drop_column.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 125
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__drop_cursor_from_driver_state'):
        continue
    db__drop_cursor_from_driver_state = _lib.db__drop_cursor_from_driver_state
    db__drop_cursor_from_driver_state.argtypes = [POINTER(dbCursor)]
    db__drop_cursor_from_driver_state.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 126
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_drop_index'):
        continue
    db_drop_index = _lib.db_drop_index
    db_drop_index.argtypes = [POINTER(dbDriver), POINTER(dbString)]
    db_drop_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 127
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_drop_table'):
        continue
    db_drop_table = _lib.db_drop_table
    db_drop_table.argtypes = [POINTER(dbDriver), POINTER(dbString)]
    db_drop_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 128
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_drop_token'):
        continue
    db_drop_token = _lib.db_drop_token
    db_drop_token.argtypes = [dbToken]
    db_drop_token.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 129
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_update'):
        continue
    db_d_update = _lib.db_d_update
    db_d_update.argtypes = []
    db_d_update.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 130
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_d_version'):
        continue
    db_d_version = _lib.db_d_version
    db_d_version.argtypes = []
    db_d_version.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 131
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_enlarge_string'):
        continue
    db_enlarge_string = _lib.db_enlarge_string
    db_enlarge_string.argtypes = [POINTER(dbString), c_int]
    db_enlarge_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 132
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_error'):
        continue
    db_error = _lib.db_error
    db_error.argtypes = [String]
    db_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 133
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_execute_immediate'):
        continue
    db_execute_immediate = _lib.db_execute_immediate
    db_execute_immediate.argtypes = [POINTER(dbDriver), POINTER(dbString)]
    db_execute_immediate.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 134
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_begin_transaction'):
        continue
    db_begin_transaction = _lib.db_begin_transaction
    db_begin_transaction.argtypes = [POINTER(dbDriver)]
    db_begin_transaction.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 135
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_commit_transaction'):
        continue
    db_commit_transaction = _lib.db_commit_transaction
    db_commit_transaction.argtypes = [POINTER(dbDriver)]
    db_commit_transaction.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 136
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_fetch'):
        continue
    db_fetch = _lib.db_fetch
    db_fetch.argtypes = [POINTER(dbCursor), c_int, POINTER(c_int)]
    db_fetch.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 137
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_find_database'):
        continue
    db_find_database = _lib.db_find_database
    db_find_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle), POINTER(c_int)]
    db_find_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 138
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_find_token'):
        continue
    db_find_token = _lib.db_find_token
    db_find_token.argtypes = [dbToken]
    db_find_token.restype = dbAddress
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 139
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free'):
        continue
    db_free = _lib.db_free
    db_free.argtypes = [POINTER(None)]
    db_free.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 140
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_column'):
        continue
    db_free_column = _lib.db_free_column
    db_free_column.argtypes = [POINTER(dbColumn)]
    db_free_column.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 141
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_cursor'):
        continue
    db_free_cursor = _lib.db_free_cursor
    db_free_cursor.argtypes = [POINTER(dbCursor)]
    db_free_cursor.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 142
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_cursor_column_flags'):
        continue
    db_free_cursor_column_flags = _lib.db_free_cursor_column_flags
    db_free_cursor_column_flags.argtypes = [POINTER(dbCursor)]
    db_free_cursor_column_flags.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 143
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_dbmscap'):
        continue
    db_free_dbmscap = _lib.db_free_dbmscap
    db_free_dbmscap.argtypes = [POINTER(dbDbmscap)]
    db_free_dbmscap.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 144
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_dirent_array'):
        continue
    db_free_dirent_array = _lib.db_free_dirent_array
    db_free_dirent_array.argtypes = [POINTER(dbDirent), c_int]
    db_free_dirent_array.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 145
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_handle'):
        continue
    db_free_handle = _lib.db_free_handle
    db_free_handle.argtypes = [POINTER(dbHandle)]
    db_free_handle.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 146
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_handle_array'):
        continue
    db_free_handle_array = _lib.db_free_handle_array
    db_free_handle_array.argtypes = [POINTER(dbHandle), c_int]
    db_free_handle_array.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 147
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_index'):
        continue
    db_free_index = _lib.db_free_index
    db_free_index.argtypes = [POINTER(dbIndex)]
    db_free_index.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 148
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_index_array'):
        continue
    db_free_index_array = _lib.db_free_index_array
    db_free_index_array.argtypes = [POINTER(dbIndex), c_int]
    db_free_index_array.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 149
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_string'):
        continue
    db_free_string = _lib.db_free_string
    db_free_string.argtypes = [POINTER(dbString)]
    db_free_string.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 150
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_string_array'):
        continue
    db_free_string_array = _lib.db_free_string_array
    db_free_string_array.argtypes = [POINTER(dbString), c_int]
    db_free_string_array.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 151
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_free_table'):
        continue
    db_free_table = _lib.db_free_table
    db_free_table.argtypes = [POINTER(dbTable)]
    db_free_table.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 152
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column'):
        continue
    db_get_column = _lib.db_get_column
    db_get_column.argtypes = [POINTER(dbDriver), String, String, POINTER(POINTER(dbColumn))]
    db_get_column.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 154
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_default_value'):
        continue
    db_get_column_default_value = _lib.db_get_column_default_value
    db_get_column_default_value.argtypes = [POINTER(dbColumn)]
    db_get_column_default_value.restype = POINTER(dbValue)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 155
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_description'):
        continue
    db_get_column_description = _lib.db_get_column_description
    db_get_column_description.argtypes = [POINTER(dbColumn)]
    db_get_column_description.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 156
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_host_type'):
        continue
    db_get_column_host_type = _lib.db_get_column_host_type
    db_get_column_host_type.argtypes = [POINTER(dbColumn)]
    db_get_column_host_type.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 157
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_length'):
        continue
    db_get_column_length = _lib.db_get_column_length
    db_get_column_length.argtypes = [POINTER(dbColumn)]
    db_get_column_length.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 158
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_name'):
        continue
    db_get_column_name = _lib.db_get_column_name
    db_get_column_name.argtypes = [POINTER(dbColumn)]
    db_get_column_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 159
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_precision'):
        continue
    db_get_column_precision = _lib.db_get_column_precision
    db_get_column_precision.argtypes = [POINTER(dbColumn)]
    db_get_column_precision.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 160
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_scale'):
        continue
    db_get_column_scale = _lib.db_get_column_scale
    db_get_column_scale.argtypes = [POINTER(dbColumn)]
    db_get_column_scale.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 161
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_select_priv'):
        continue
    db_get_column_select_priv = _lib.db_get_column_select_priv
    db_get_column_select_priv.argtypes = [POINTER(dbColumn)]
    db_get_column_select_priv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 162
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_sqltype'):
        continue
    db_get_column_sqltype = _lib.db_get_column_sqltype
    db_get_column_sqltype.argtypes = [POINTER(dbColumn)]
    db_get_column_sqltype.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 163
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_update_priv'):
        continue
    db_get_column_update_priv = _lib.db_get_column_update_priv
    db_get_column_update_priv.argtypes = [POINTER(dbColumn)]
    db_get_column_update_priv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 164
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_column_value'):
        continue
    db_get_column_value = _lib.db_get_column_value
    db_get_column_value.argtypes = [POINTER(dbColumn)]
    db_get_column_value.restype = POINTER(dbValue)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 165
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_connection'):
        continue
    db_get_connection = _lib.db_get_connection
    db_get_connection.argtypes = [POINTER(dbConnection)]
    db_get_connection.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 166
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_cursor_number_of_columns'):
        continue
    db_get_cursor_number_of_columns = _lib.db_get_cursor_number_of_columns
    db_get_cursor_number_of_columns.argtypes = [POINTER(dbCursor)]
    db_get_cursor_number_of_columns.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 167
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_cursor_table'):
        continue
    db_get_cursor_table = _lib.db_get_cursor_table
    db_get_cursor_table.argtypes = [POINTER(dbCursor)]
    db_get_cursor_table.restype = POINTER(dbTable)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 168
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_cursor_token'):
        continue
    db_get_cursor_token = _lib.db_get_cursor_token
    db_get_cursor_token.argtypes = [POINTER(dbCursor)]
    db_get_cursor_token.restype = dbToken
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 169
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_default_driver_name'):
        continue
    db_get_default_driver_name = _lib.db_get_default_driver_name
    db_get_default_driver_name.argtypes = []
    db_get_default_driver_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 170
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_default_database_name'):
        continue
    db_get_default_database_name = _lib.db_get_default_database_name
    db_get_default_database_name.argtypes = []
    db_get_default_database_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 171
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_default_schema_name'):
        continue
    db_get_default_schema_name = _lib.db_get_default_schema_name
    db_get_default_schema_name.argtypes = []
    db_get_default_schema_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 172
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_default_group_name'):
        continue
    db_get_default_group_name = _lib.db_get_default_group_name
    db_get_default_group_name.argtypes = []
    db_get_default_group_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 173
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__get_driver_state'):
        continue
    db__get_driver_state = _lib.db__get_driver_state
    db__get_driver_state.argtypes = []
    db__get_driver_state.restype = POINTER(dbDriverState)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 174
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_error_code'):
        continue
    db_get_error_code = _lib.db_get_error_code
    db_get_error_code.argtypes = []
    db_get_error_code.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 175
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_error_msg'):
        continue
    db_get_error_msg = _lib.db_get_error_msg
    db_get_error_msg.argtypes = []
    db_get_error_msg.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 176
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_error_who'):
        continue
    db_get_error_who = _lib.db_get_error_who
    db_get_error_who.argtypes = []
    db_get_error_who.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 177
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_handle_dbname'):
        continue
    db_get_handle_dbname = _lib.db_get_handle_dbname
    db_get_handle_dbname.argtypes = [POINTER(dbHandle)]
    db_get_handle_dbname.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 178
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_handle_dbschema'):
        continue
    db_get_handle_dbschema = _lib.db_get_handle_dbschema
    db_get_handle_dbschema.argtypes = [POINTER(dbHandle)]
    db_get_handle_dbschema.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 179
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_index_column_name'):
        continue
    db_get_index_column_name = _lib.db_get_index_column_name
    db_get_index_column_name.argtypes = [POINTER(dbIndex), c_int]
    db_get_index_column_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 180
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_index_name'):
        continue
    db_get_index_name = _lib.db_get_index_name
    db_get_index_name.argtypes = [POINTER(dbIndex)]
    db_get_index_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 181
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_index_number_of_columns'):
        continue
    db_get_index_number_of_columns = _lib.db_get_index_number_of_columns
    db_get_index_number_of_columns.argtypes = [POINTER(dbIndex)]
    db_get_index_number_of_columns.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 182
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_index_table_name'):
        continue
    db_get_index_table_name = _lib.db_get_index_table_name
    db_get_index_table_name.argtypes = [POINTER(dbIndex)]
    db_get_index_table_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 183
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_num_rows'):
        continue
    db_get_num_rows = _lib.db_get_num_rows
    db_get_num_rows.argtypes = [POINTER(dbCursor)]
    db_get_num_rows.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 184
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_string'):
        continue
    db_get_string = _lib.db_get_string
    db_get_string.argtypes = [POINTER(dbString)]
    if sizeof(c_int) == sizeof(c_void_p):
        db_get_string.restype = ReturnString
    else:
        db_get_string.restype = String
        db_get_string.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 185
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_column'):
        continue
    db_get_table_column = _lib.db_get_table_column
    db_get_table_column.argtypes = [POINTER(dbTable), c_int]
    db_get_table_column.restype = POINTER(dbColumn)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 186
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_column_by_name'):
        continue
    db_get_table_column_by_name = _lib.db_get_table_column_by_name
    db_get_table_column_by_name.argtypes = [POINTER(dbTable), String]
    db_get_table_column_by_name.restype = POINTER(dbColumn)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 187
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_delete_priv'):
        continue
    db_get_table_delete_priv = _lib.db_get_table_delete_priv
    db_get_table_delete_priv.argtypes = [POINTER(dbTable)]
    db_get_table_delete_priv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 188
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_description'):
        continue
    db_get_table_description = _lib.db_get_table_description
    db_get_table_description.argtypes = [POINTER(dbTable)]
    db_get_table_description.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 189
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_insert_priv'):
        continue
    db_get_table_insert_priv = _lib.db_get_table_insert_priv
    db_get_table_insert_priv.argtypes = [POINTER(dbTable)]
    db_get_table_insert_priv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 190
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_name'):
        continue
    db_get_table_name = _lib.db_get_table_name
    db_get_table_name.argtypes = [POINTER(dbTable)]
    db_get_table_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 191
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_number_of_columns'):
        continue
    db_get_table_number_of_columns = _lib.db_get_table_number_of_columns
    db_get_table_number_of_columns.argtypes = [POINTER(dbTable)]
    db_get_table_number_of_columns.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 192
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_number_of_rows'):
        continue
    db_get_table_number_of_rows = _lib.db_get_table_number_of_rows
    db_get_table_number_of_rows.argtypes = [POINTER(dbDriver), POINTER(dbString)]
    db_get_table_number_of_rows.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 193
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_select_priv'):
        continue
    db_get_table_select_priv = _lib.db_get_table_select_priv
    db_get_table_select_priv.argtypes = [POINTER(dbTable)]
    db_get_table_select_priv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 194
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_table_update_priv'):
        continue
    db_get_table_update_priv = _lib.db_get_table_update_priv
    db_get_table_update_priv.argtypes = [POINTER(dbTable)]
    db_get_table_update_priv.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 195
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_as_double'):
        continue
    db_get_value_as_double = _lib.db_get_value_as_double
    db_get_value_as_double.argtypes = [POINTER(dbValue), c_int]
    db_get_value_as_double.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 196
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_day'):
        continue
    db_get_value_day = _lib.db_get_value_day
    db_get_value_day.argtypes = [POINTER(dbValue)]
    db_get_value_day.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 197
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_double'):
        continue
    db_get_value_double = _lib.db_get_value_double
    db_get_value_double.argtypes = [POINTER(dbValue)]
    db_get_value_double.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 198
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_hour'):
        continue
    db_get_value_hour = _lib.db_get_value_hour
    db_get_value_hour.argtypes = [POINTER(dbValue)]
    db_get_value_hour.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 199
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_int'):
        continue
    db_get_value_int = _lib.db_get_value_int
    db_get_value_int.argtypes = [POINTER(dbValue)]
    db_get_value_int.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 200
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_minute'):
        continue
    db_get_value_minute = _lib.db_get_value_minute
    db_get_value_minute.argtypes = [POINTER(dbValue)]
    db_get_value_minute.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 201
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_month'):
        continue
    db_get_value_month = _lib.db_get_value_month
    db_get_value_month.argtypes = [POINTER(dbValue)]
    db_get_value_month.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 202
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_seconds'):
        continue
    db_get_value_seconds = _lib.db_get_value_seconds
    db_get_value_seconds.argtypes = [POINTER(dbValue)]
    db_get_value_seconds.restype = c_double
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 203
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_string'):
        continue
    db_get_value_string = _lib.db_get_value_string
    db_get_value_string.argtypes = [POINTER(dbValue)]
    db_get_value_string.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 204
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_value_year'):
        continue
    db_get_value_year = _lib.db_get_value_year
    db_get_value_year.argtypes = [POINTER(dbValue)]
    db_get_value_year.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 205
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_grant_on_table'):
        continue
    db_grant_on_table = _lib.db_grant_on_table
    db_grant_on_table.argtypes = [POINTER(dbDriver), String, c_int, c_int]
    db_grant_on_table.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 207
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_has_dbms'):
        continue
    db_has_dbms = _lib.db_has_dbms
    db_has_dbms.argtypes = []
    db_has_dbms.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 208
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_init_column'):
        continue
    db_init_column = _lib.db_init_column
    db_init_column.argtypes = [POINTER(dbColumn)]
    db_init_column.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 209
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_init_cursor'):
        continue
    db_init_cursor = _lib.db_init_cursor
    db_init_cursor.argtypes = [POINTER(dbCursor)]
    db_init_cursor.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 210
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__init_driver_state'):
        continue
    db__init_driver_state = _lib.db__init_driver_state
    db__init_driver_state.argtypes = []
    db__init_driver_state.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 211
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_init_handle'):
        continue
    db_init_handle = _lib.db_init_handle
    db_init_handle.argtypes = [POINTER(dbHandle)]
    db_init_handle.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 212
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_init_index'):
        continue
    db_init_index = _lib.db_init_index
    db_init_index.argtypes = [POINTER(dbIndex)]
    db_init_index.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 213
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_init_string'):
        continue
    db_init_string = _lib.db_init_string
    db_init_string.argtypes = [POINTER(dbString)]
    db_init_string.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 214
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_init_table'):
        continue
    db_init_table = _lib.db_init_table
    db_init_table.argtypes = [POINTER(dbTable)]
    db_init_table.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 215
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_insert'):
        continue
    db_insert = _lib.db_insert
    db_insert.argtypes = [POINTER(dbCursor)]
    db_insert.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 216
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_interval_range'):
        continue
    db_interval_range = _lib.db_interval_range
    db_interval_range.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    db_interval_range.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 217
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_isdir'):
        continue
    db_isdir = _lib.db_isdir
    db_isdir.argtypes = [String]
    db_isdir.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 218
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_legal_tablename'):
        continue
    db_legal_tablename = _lib.db_legal_tablename
    db_legal_tablename.argtypes = [String]
    db_legal_tablename.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 219
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_list_databases'):
        continue
    db_list_databases = _lib.db_list_databases
    db_list_databases.argtypes = [POINTER(dbDriver), POINTER(dbString), c_int, POINTER(POINTER(dbHandle)), POINTER(c_int)]
    db_list_databases.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 221
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_list_drivers'):
        continue
    db_list_drivers = _lib.db_list_drivers
    db_list_drivers.argtypes = []
    db_list_drivers.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 222
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_list_indexes'):
        continue
    db_list_indexes = _lib.db_list_indexes
    db_list_indexes.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(POINTER(dbIndex)), POINTER(c_int)]
    db_list_indexes.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 224
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_list_tables'):
        continue
    db_list_tables = _lib.db_list_tables
    db_list_tables.argtypes = [POINTER(dbDriver), POINTER(POINTER(dbString)), POINTER(c_int), c_int]
    db_list_tables.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 226
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_malloc'):
        continue
    db_malloc = _lib.db_malloc
    db_malloc.argtypes = [c_int]
    db_malloc.restype = POINTER(c_ubyte)
    db_malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 227
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__mark_database_closed'):
        continue
    db__mark_database_closed = _lib.db__mark_database_closed
    db__mark_database_closed.argtypes = []
    db__mark_database_closed.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 228
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__mark_database_open'):
        continue
    db__mark_database_open = _lib.db__mark_database_open
    db__mark_database_open.argtypes = [String, String]
    db__mark_database_open.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 229
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_memory_error'):
        continue
    db_memory_error = _lib.db_memory_error
    db_memory_error.argtypes = []
    db_memory_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 230
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_new_token'):
        continue
    db_new_token = _lib.db_new_token
    db_new_token.argtypes = [dbAddress]
    db_new_token.restype = dbToken
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 231
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_nocase_compare'):
        continue
    db_nocase_compare = _lib.db_nocase_compare
    db_nocase_compare.argtypes = [String, String]
    db_nocase_compare.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 232
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_noproc_error'):
        continue
    db_noproc_error = _lib.db_noproc_error
    db_noproc_error.argtypes = [c_int]
    db_noproc_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 233
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_open_database'):
        continue
    db_open_database = _lib.db_open_database
    db_open_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle)]
    db_open_database.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 234
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_open_insert_cursor'):
        continue
    db_open_insert_cursor = _lib.db_open_insert_cursor
    db_open_insert_cursor.argtypes = [POINTER(dbDriver), POINTER(dbCursor)]
    db_open_insert_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 235
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_open_select_cursor'):
        continue
    db_open_select_cursor = _lib.db_open_select_cursor
    db_open_select_cursor.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbCursor), c_int]
    db_open_select_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 237
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_open_update_cursor'):
        continue
    db_open_update_cursor = _lib.db_open_update_cursor
    db_open_update_cursor.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbString), POINTER(dbCursor), c_int]
    db_open_update_cursor.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 239
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_print_column_definition'):
        continue
    db_print_column_definition = _lib.db_print_column_definition
    db_print_column_definition.argtypes = [POINTER(FILE), POINTER(dbColumn)]
    db_print_column_definition.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 240
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_print_error'):
        continue
    db_print_error = _lib.db_print_error
    db_print_error.argtypes = []
    db_print_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 241
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_print_index'):
        continue
    db_print_index = _lib.db_print_index
    db_print_index.argtypes = [POINTER(FILE), POINTER(dbIndex)]
    db_print_index.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 242
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_print_table_definition'):
        continue
    db_print_table_definition = _lib.db_print_table_definition
    db_print_table_definition.argtypes = [POINTER(FILE), POINTER(dbTable)]
    db_print_table_definition.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 243
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_procedure_not_implemented'):
        continue
    db_procedure_not_implemented = _lib.db_procedure_not_implemented
    db_procedure_not_implemented.argtypes = [String]
    db_procedure_not_implemented.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 244
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_protocol_error'):
        continue
    db_protocol_error = _lib.db_protocol_error
    db_protocol_error.argtypes = []
    db_protocol_error.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 245
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_read_dbmscap'):
        continue
    db_read_dbmscap = _lib.db_read_dbmscap
    db_read_dbmscap.argtypes = []
    db_read_dbmscap.restype = POINTER(dbDbmscap)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 246
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_realloc'):
        continue
    db_realloc = _lib.db_realloc
    db_realloc.argtypes = [POINTER(None), c_int]
    db_realloc.restype = POINTER(c_ubyte)
    db_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 247
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_char'):
        continue
    db__recv_char = _lib.db__recv_char
    db__recv_char.argtypes = [String]
    db__recv_char.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 248
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_column_default_value'):
        continue
    db__recv_column_default_value = _lib.db__recv_column_default_value
    db__recv_column_default_value.argtypes = [POINTER(dbColumn)]
    db__recv_column_default_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 249
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_column_definition'):
        continue
    db__recv_column_definition = _lib.db__recv_column_definition
    db__recv_column_definition.argtypes = [POINTER(dbColumn)]
    db__recv_column_definition.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 250
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_column_value'):
        continue
    db__recv_column_value = _lib.db__recv_column_value
    db__recv_column_value.argtypes = [POINTER(dbColumn)]
    db__recv_column_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 251
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_datetime'):
        continue
    db__recv_datetime = _lib.db__recv_datetime
    db__recv_datetime.argtypes = [POINTER(dbDateTime)]
    db__recv_datetime.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 252
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_double'):
        continue
    db__recv_double = _lib.db__recv_double
    db__recv_double.argtypes = [POINTER(c_double)]
    db__recv_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 253
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_double_array'):
        continue
    db__recv_double_array = _lib.db__recv_double_array
    db__recv_double_array.argtypes = [POINTER(POINTER(c_double)), POINTER(c_int)]
    db__recv_double_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 254
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_float'):
        continue
    db__recv_float = _lib.db__recv_float
    db__recv_float.argtypes = [POINTER(c_float)]
    db__recv_float.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 255
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_float_array'):
        continue
    db__recv_float_array = _lib.db__recv_float_array
    db__recv_float_array.argtypes = [POINTER(POINTER(c_float)), POINTER(c_int)]
    db__recv_float_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 256
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_handle'):
        continue
    db__recv_handle = _lib.db__recv_handle
    db__recv_handle.argtypes = [POINTER(dbHandle)]
    db__recv_handle.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 257
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_index'):
        continue
    db__recv_index = _lib.db__recv_index
    db__recv_index.argtypes = [POINTER(dbIndex)]
    db__recv_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 258
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_index_array'):
        continue
    db__recv_index_array = _lib.db__recv_index_array
    db__recv_index_array.argtypes = [POINTER(POINTER(dbIndex)), POINTER(c_int)]
    db__recv_index_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 259
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_int'):
        continue
    db__recv_int = _lib.db__recv_int
    db__recv_int.argtypes = [POINTER(c_int)]
    db__recv_int.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 260
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_int_array'):
        continue
    db__recv_int_array = _lib.db__recv_int_array
    db__recv_int_array.argtypes = [POINTER(POINTER(c_int)), POINTER(c_int)]
    db__recv_int_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 261
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_procnum'):
        continue
    db__recv_procnum = _lib.db__recv_procnum
    db__recv_procnum.argtypes = [POINTER(c_int)]
    db__recv_procnum.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 262
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_return_code'):
        continue
    db__recv_return_code = _lib.db__recv_return_code
    db__recv_return_code.argtypes = [POINTER(c_int)]
    db__recv_return_code.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 263
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_short'):
        continue
    db__recv_short = _lib.db__recv_short
    db__recv_short.argtypes = [POINTER(c_short)]
    db__recv_short.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 264
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_short_array'):
        continue
    db__recv_short_array = _lib.db__recv_short_array
    db__recv_short_array.argtypes = [POINTER(POINTER(c_short)), POINTER(c_int)]
    db__recv_short_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 265
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_string'):
        continue
    db__recv_string = _lib.db__recv_string
    db__recv_string.argtypes = [POINTER(dbString)]
    db__recv_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 266
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_string_array'):
        continue
    db__recv_string_array = _lib.db__recv_string_array
    db__recv_string_array.argtypes = [POINTER(POINTER(dbString)), POINTER(c_int)]
    db__recv_string_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 267
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_table_data'):
        continue
    db__recv_table_data = _lib.db__recv_table_data
    db__recv_table_data.argtypes = [POINTER(dbTable)]
    db__recv_table_data.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 268
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_table_definition'):
        continue
    db__recv_table_definition = _lib.db__recv_table_definition
    db__recv_table_definition.argtypes = [POINTER(POINTER(dbTable))]
    db__recv_table_definition.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 269
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_token'):
        continue
    db__recv_token = _lib.db__recv_token
    db__recv_token.argtypes = [POINTER(dbToken)]
    db__recv_token.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 270
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__recv_value'):
        continue
    db__recv_value = _lib.db__recv_value
    db__recv_value.argtypes = [POINTER(dbValue), c_int]
    db__recv_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 271
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_Cstring'):
        continue
    db__send_Cstring = _lib.db__send_Cstring
    db__send_Cstring.argtypes = [String]
    db__send_Cstring.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 272
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_char'):
        continue
    db__send_char = _lib.db__send_char
    db__send_char.argtypes = [c_int]
    db__send_char.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 273
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_column_default_value'):
        continue
    db__send_column_default_value = _lib.db__send_column_default_value
    db__send_column_default_value.argtypes = [POINTER(dbColumn)]
    db__send_column_default_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 274
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_column_definition'):
        continue
    db__send_column_definition = _lib.db__send_column_definition
    db__send_column_definition.argtypes = [POINTER(dbColumn)]
    db__send_column_definition.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 275
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_column_value'):
        continue
    db__send_column_value = _lib.db__send_column_value
    db__send_column_value.argtypes = [POINTER(dbColumn)]
    db__send_column_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 276
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_datetime'):
        continue
    db__send_datetime = _lib.db__send_datetime
    db__send_datetime.argtypes = [POINTER(dbDateTime)]
    db__send_datetime.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 277
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_double'):
        continue
    db__send_double = _lib.db__send_double
    db__send_double.argtypes = [c_double]
    db__send_double.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 278
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_double_array'):
        continue
    db__send_double_array = _lib.db__send_double_array
    db__send_double_array.argtypes = [POINTER(c_double), c_int]
    db__send_double_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 279
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_failure'):
        continue
    db__send_failure = _lib.db__send_failure
    db__send_failure.argtypes = []
    db__send_failure.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 280
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_float'):
        continue
    db__send_float = _lib.db__send_float
    db__send_float.argtypes = [c_float]
    db__send_float.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 281
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_float_array'):
        continue
    db__send_float_array = _lib.db__send_float_array
    db__send_float_array.argtypes = [POINTER(c_float), c_int]
    db__send_float_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 282
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_handle'):
        continue
    db__send_handle = _lib.db__send_handle
    db__send_handle.argtypes = [POINTER(dbHandle)]
    db__send_handle.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 283
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_index'):
        continue
    db__send_index = _lib.db__send_index
    db__send_index.argtypes = [POINTER(dbIndex)]
    db__send_index.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 284
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_index_array'):
        continue
    db__send_index_array = _lib.db__send_index_array
    db__send_index_array.argtypes = [POINTER(dbIndex), c_int]
    db__send_index_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 285
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_int'):
        continue
    db__send_int = _lib.db__send_int
    db__send_int.argtypes = [c_int]
    db__send_int.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 286
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_int_array'):
        continue
    db__send_int_array = _lib.db__send_int_array
    db__send_int_array.argtypes = [POINTER(c_int), c_int]
    db__send_int_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 287
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_procedure_not_implemented'):
        continue
    db__send_procedure_not_implemented = _lib.db__send_procedure_not_implemented
    db__send_procedure_not_implemented.argtypes = [c_int]
    db__send_procedure_not_implemented.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 288
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_procedure_ok'):
        continue
    db__send_procedure_ok = _lib.db__send_procedure_ok
    db__send_procedure_ok.argtypes = [c_int]
    db__send_procedure_ok.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 289
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_short'):
        continue
    db__send_short = _lib.db__send_short
    db__send_short.argtypes = [c_int]
    db__send_short.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 290
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_short_array'):
        continue
    db__send_short_array = _lib.db__send_short_array
    db__send_short_array.argtypes = [POINTER(c_short), c_int]
    db__send_short_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 291
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_string'):
        continue
    db__send_string = _lib.db__send_string
    db__send_string.argtypes = [POINTER(dbString)]
    db__send_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 292
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_string_array'):
        continue
    db__send_string_array = _lib.db__send_string_array
    db__send_string_array.argtypes = [POINTER(dbString), c_int]
    db__send_string_array.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 293
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_success'):
        continue
    db__send_success = _lib.db__send_success
    db__send_success.argtypes = []
    db__send_success.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 294
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_table_data'):
        continue
    db__send_table_data = _lib.db__send_table_data
    db__send_table_data.argtypes = [POINTER(dbTable)]
    db__send_table_data.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 295
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_table_definition'):
        continue
    db__send_table_definition = _lib.db__send_table_definition
    db__send_table_definition.argtypes = [POINTER(dbTable)]
    db__send_table_definition.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 296
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_token'):
        continue
    db__send_token = _lib.db__send_token
    db__send_token.argtypes = [POINTER(dbToken)]
    db__send_token.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 297
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__send_value'):
        continue
    db__send_value = _lib.db__send_value
    db__send_value.argtypes = [POINTER(dbValue), c_int]
    db__send_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 298
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_select_CatValArray'):
        continue
    db_select_CatValArray = _lib.db_select_CatValArray
    db_select_CatValArray.argtypes = [POINTER(dbDriver), String, String, String, String, POINTER(dbCatValArray)]
    db_select_CatValArray.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 301
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_select_int'):
        continue
    db_select_int = _lib.db_select_int
    db_select_int.argtypes = [POINTER(dbDriver), String, String, String, POINTER(POINTER(c_int))]
    db_select_int.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 303
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_select_value'):
        continue
    db_select_value = _lib.db_select_value
    db_select_value.argtypes = [POINTER(dbDriver), String, String, c_int, String, POINTER(dbValue)]
    db_select_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 305
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_description'):
        continue
    db_set_column_description = _lib.db_set_column_description
    db_set_column_description.argtypes = [POINTER(dbColumn), String]
    db_set_column_description.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 306
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_has_defined_default_value'):
        continue
    db_set_column_has_defined_default_value = _lib.db_set_column_has_defined_default_value
    db_set_column_has_defined_default_value.argtypes = [POINTER(dbColumn)]
    db_set_column_has_defined_default_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 307
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_has_undefined_default_value'):
        continue
    db_set_column_has_undefined_default_value = _lib.db_set_column_has_undefined_default_value
    db_set_column_has_undefined_default_value.argtypes = [POINTER(dbColumn)]
    db_set_column_has_undefined_default_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 308
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_host_type'):
        continue
    db_set_column_host_type = _lib.db_set_column_host_type
    db_set_column_host_type.argtypes = [POINTER(dbColumn), c_int]
    db_set_column_host_type.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 309
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_length'):
        continue
    db_set_column_length = _lib.db_set_column_length
    db_set_column_length.argtypes = [POINTER(dbColumn), c_int]
    db_set_column_length.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 310
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_name'):
        continue
    db_set_column_name = _lib.db_set_column_name
    db_set_column_name.argtypes = [POINTER(dbColumn), String]
    db_set_column_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 311
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_null_allowed'):
        continue
    db_set_column_null_allowed = _lib.db_set_column_null_allowed
    db_set_column_null_allowed.argtypes = [POINTER(dbColumn)]
    db_set_column_null_allowed.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 312
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_precision'):
        continue
    db_set_column_precision = _lib.db_set_column_precision
    db_set_column_precision.argtypes = [POINTER(dbColumn), c_int]
    db_set_column_precision.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 313
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_scale'):
        continue
    db_set_column_scale = _lib.db_set_column_scale
    db_set_column_scale.argtypes = [POINTER(dbColumn), c_int]
    db_set_column_scale.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 314
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_select_priv_granted'):
        continue
    db_set_column_select_priv_granted = _lib.db_set_column_select_priv_granted
    db_set_column_select_priv_granted.argtypes = [POINTER(dbColumn)]
    db_set_column_select_priv_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 315
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_select_priv_not_granted'):
        continue
    db_set_column_select_priv_not_granted = _lib.db_set_column_select_priv_not_granted
    db_set_column_select_priv_not_granted.argtypes = [POINTER(dbColumn)]
    db_set_column_select_priv_not_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 316
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_sqltype'):
        continue
    db_set_column_sqltype = _lib.db_set_column_sqltype
    db_set_column_sqltype.argtypes = [POINTER(dbColumn), c_int]
    db_set_column_sqltype.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 317
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_update_priv_granted'):
        continue
    db_set_column_update_priv_granted = _lib.db_set_column_update_priv_granted
    db_set_column_update_priv_granted.argtypes = [POINTER(dbColumn)]
    db_set_column_update_priv_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 318
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_update_priv_not_granted'):
        continue
    db_set_column_update_priv_not_granted = _lib.db_set_column_update_priv_not_granted
    db_set_column_update_priv_not_granted.argtypes = [POINTER(dbColumn)]
    db_set_column_update_priv_not_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 319
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_column_use_default_value'):
        continue
    db_set_column_use_default_value = _lib.db_set_column_use_default_value
    db_set_column_use_default_value.argtypes = [POINTER(dbColumn)]
    db_set_column_use_default_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 320
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_connection'):
        continue
    db_set_connection = _lib.db_set_connection
    db_set_connection.argtypes = [POINTER(dbConnection)]
    db_set_connection.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 321
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_column_flag'):
        continue
    db_set_cursor_column_flag = _lib.db_set_cursor_column_flag
    db_set_cursor_column_flag.argtypes = [POINTER(dbCursor), c_int]
    db_set_cursor_column_flag.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 322
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_column_for_update'):
        continue
    db_set_cursor_column_for_update = _lib.db_set_cursor_column_for_update
    db_set_cursor_column_for_update.argtypes = [POINTER(dbCursor), c_int]
    db_set_cursor_column_for_update.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 323
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_mode'):
        continue
    db_set_cursor_mode = _lib.db_set_cursor_mode
    db_set_cursor_mode.argtypes = [POINTER(dbCursor), c_int]
    db_set_cursor_mode.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 324
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_mode_insensitive'):
        continue
    db_set_cursor_mode_insensitive = _lib.db_set_cursor_mode_insensitive
    db_set_cursor_mode_insensitive.argtypes = [POINTER(dbCursor)]
    db_set_cursor_mode_insensitive.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 325
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_mode_scroll'):
        continue
    db_set_cursor_mode_scroll = _lib.db_set_cursor_mode_scroll
    db_set_cursor_mode_scroll.argtypes = [POINTER(dbCursor)]
    db_set_cursor_mode_scroll.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 326
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_table'):
        continue
    db_set_cursor_table = _lib.db_set_cursor_table
    db_set_cursor_table.argtypes = [POINTER(dbCursor), POINTER(dbTable)]
    db_set_cursor_table.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 327
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_token'):
        continue
    db_set_cursor_token = _lib.db_set_cursor_token
    db_set_cursor_token.argtypes = [POINTER(dbCursor), dbToken]
    db_set_cursor_token.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 328
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_type_insert'):
        continue
    db_set_cursor_type_insert = _lib.db_set_cursor_type_insert
    db_set_cursor_type_insert.argtypes = [POINTER(dbCursor)]
    db_set_cursor_type_insert.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 329
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_type_readonly'):
        continue
    db_set_cursor_type_readonly = _lib.db_set_cursor_type_readonly
    db_set_cursor_type_readonly.argtypes = [POINTER(dbCursor)]
    db_set_cursor_type_readonly.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 330
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_cursor_type_update'):
        continue
    db_set_cursor_type_update = _lib.db_set_cursor_type_update
    db_set_cursor_type_update.argtypes = [POINTER(dbCursor)]
    db_set_cursor_type_update.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 331
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_default_connection'):
        continue
    db_set_default_connection = _lib.db_set_default_connection
    db_set_default_connection.argtypes = []
    db_set_default_connection.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 332
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_error_who'):
        continue
    db_set_error_who = _lib.db_set_error_who
    db_set_error_who.argtypes = [String]
    db_set_error_who.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 333
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_handle'):
        continue
    db_set_handle = _lib.db_set_handle
    db_set_handle.argtypes = [POINTER(dbHandle), String, String]
    db_set_handle.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 334
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_error_handler_driver'):
        continue
    db_set_error_handler_driver = _lib.db_set_error_handler_driver
    db_set_error_handler_driver.argtypes = [POINTER(dbDriver)]
    db_set_error_handler_driver.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 335
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_error_handler_driver'):
        continue
    db_unset_error_handler_driver = _lib.db_unset_error_handler_driver
    db_unset_error_handler_driver.argtypes = [POINTER(dbDriver)]
    db_unset_error_handler_driver.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 336
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_index_column_name'):
        continue
    db_set_index_column_name = _lib.db_set_index_column_name
    db_set_index_column_name.argtypes = [POINTER(dbIndex), c_int, String]
    db_set_index_column_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 338
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_index_name'):
        continue
    db_set_index_name = _lib.db_set_index_name
    db_set_index_name.argtypes = [POINTER(dbIndex), String]
    db_set_index_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 339
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_index_table_name'):
        continue
    db_set_index_table_name = _lib.db_set_index_table_name
    db_set_index_table_name.argtypes = [POINTER(dbIndex), String]
    db_set_index_table_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 340
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_index_type_non_unique'):
        continue
    db_set_index_type_non_unique = _lib.db_set_index_type_non_unique
    db_set_index_type_non_unique.argtypes = [POINTER(dbIndex)]
    db_set_index_type_non_unique.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 341
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_index_type_unique'):
        continue
    db_set_index_type_unique = _lib.db_set_index_type_unique
    db_set_index_type_unique.argtypes = [POINTER(dbIndex)]
    db_set_index_type_unique.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 342
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__set_protocol_fds'):
        continue
    db__set_protocol_fds = _lib.db__set_protocol_fds
    db__set_protocol_fds.argtypes = [POINTER(FILE), POINTER(FILE)]
    db__set_protocol_fds.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 343
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_string'):
        continue
    db_set_string = _lib.db_set_string
    db_set_string.argtypes = [POINTER(dbString), String]
    db_set_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 344
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_string_no_copy'):
        continue
    db_set_string_no_copy = _lib.db_set_string_no_copy
    db_set_string_no_copy.argtypes = [POINTER(dbString), String]
    db_set_string_no_copy.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 345
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_column'):
        continue
    db_set_table_column = _lib.db_set_table_column
    db_set_table_column.argtypes = [POINTER(dbTable), c_int, POINTER(dbColumn)]
    db_set_table_column.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 346
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_delete_priv_granted'):
        continue
    db_set_table_delete_priv_granted = _lib.db_set_table_delete_priv_granted
    db_set_table_delete_priv_granted.argtypes = [POINTER(dbTable)]
    db_set_table_delete_priv_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 347
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_delete_priv_not_granted'):
        continue
    db_set_table_delete_priv_not_granted = _lib.db_set_table_delete_priv_not_granted
    db_set_table_delete_priv_not_granted.argtypes = [POINTER(dbTable)]
    db_set_table_delete_priv_not_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 348
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_description'):
        continue
    db_set_table_description = _lib.db_set_table_description
    db_set_table_description.argtypes = [POINTER(dbTable), String]
    db_set_table_description.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 349
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_insert_priv_granted'):
        continue
    db_set_table_insert_priv_granted = _lib.db_set_table_insert_priv_granted
    db_set_table_insert_priv_granted.argtypes = [POINTER(dbTable)]
    db_set_table_insert_priv_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 350
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_insert_priv_not_granted'):
        continue
    db_set_table_insert_priv_not_granted = _lib.db_set_table_insert_priv_not_granted
    db_set_table_insert_priv_not_granted.argtypes = [POINTER(dbTable)]
    db_set_table_insert_priv_not_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 351
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_name'):
        continue
    db_set_table_name = _lib.db_set_table_name
    db_set_table_name.argtypes = [POINTER(dbTable), String]
    db_set_table_name.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 352
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_select_priv_granted'):
        continue
    db_set_table_select_priv_granted = _lib.db_set_table_select_priv_granted
    db_set_table_select_priv_granted.argtypes = [POINTER(dbTable)]
    db_set_table_select_priv_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 353
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_select_priv_not_granted'):
        continue
    db_set_table_select_priv_not_granted = _lib.db_set_table_select_priv_not_granted
    db_set_table_select_priv_not_granted.argtypes = [POINTER(dbTable)]
    db_set_table_select_priv_not_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 354
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_update_priv_granted'):
        continue
    db_set_table_update_priv_granted = _lib.db_set_table_update_priv_granted
    db_set_table_update_priv_granted.argtypes = [POINTER(dbTable)]
    db_set_table_update_priv_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 355
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_table_update_priv_not_granted'):
        continue
    db_set_table_update_priv_not_granted = _lib.db_set_table_update_priv_not_granted
    db_set_table_update_priv_not_granted.argtypes = [POINTER(dbTable)]
    db_set_table_update_priv_not_granted.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 356
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_datetime_current'):
        continue
    db_set_value_datetime_current = _lib.db_set_value_datetime_current
    db_set_value_datetime_current.argtypes = [POINTER(dbValue)]
    db_set_value_datetime_current.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 357
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_datetime_not_current'):
        continue
    db_set_value_datetime_not_current = _lib.db_set_value_datetime_not_current
    db_set_value_datetime_not_current.argtypes = [POINTER(dbValue)]
    db_set_value_datetime_not_current.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 358
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_day'):
        continue
    db_set_value_day = _lib.db_set_value_day
    db_set_value_day.argtypes = [POINTER(dbValue), c_int]
    db_set_value_day.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 359
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_double'):
        continue
    db_set_value_double = _lib.db_set_value_double
    db_set_value_double.argtypes = [POINTER(dbValue), c_double]
    db_set_value_double.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 360
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_hour'):
        continue
    db_set_value_hour = _lib.db_set_value_hour
    db_set_value_hour.argtypes = [POINTER(dbValue), c_int]
    db_set_value_hour.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 361
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_int'):
        continue
    db_set_value_int = _lib.db_set_value_int
    db_set_value_int.argtypes = [POINTER(dbValue), c_int]
    db_set_value_int.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 362
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_minute'):
        continue
    db_set_value_minute = _lib.db_set_value_minute
    db_set_value_minute.argtypes = [POINTER(dbValue), c_int]
    db_set_value_minute.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 363
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_month'):
        continue
    db_set_value_month = _lib.db_set_value_month
    db_set_value_month.argtypes = [POINTER(dbValue), c_int]
    db_set_value_month.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 364
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_not_null'):
        continue
    db_set_value_not_null = _lib.db_set_value_not_null
    db_set_value_not_null.argtypes = [POINTER(dbValue)]
    db_set_value_not_null.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 365
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_null'):
        continue
    db_set_value_null = _lib.db_set_value_null
    db_set_value_null.argtypes = [POINTER(dbValue)]
    db_set_value_null.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 366
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_seconds'):
        continue
    db_set_value_seconds = _lib.db_set_value_seconds
    db_set_value_seconds.argtypes = [POINTER(dbValue), c_double]
    db_set_value_seconds.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 367
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_string'):
        continue
    db_set_value_string = _lib.db_set_value_string
    db_set_value_string.argtypes = [POINTER(dbValue), String]
    db_set_value_string.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 368
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_value_year'):
        continue
    db_set_value_year = _lib.db_set_value_year
    db_set_value_year.argtypes = [POINTER(dbValue), c_int]
    db_set_value_year.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 369
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_shutdown_driver'):
        continue
    db_shutdown_driver = _lib.db_shutdown_driver
    db_shutdown_driver.argtypes = [POINTER(dbDriver)]
    db_shutdown_driver.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 370
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_sqltype_name'):
        continue
    db_sqltype_name = _lib.db_sqltype_name
    db_sqltype_name.argtypes = [c_int]
    db_sqltype_name.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 371
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_sqltype_to_Ctype'):
        continue
    db_sqltype_to_Ctype = _lib.db_sqltype_to_Ctype
    db_sqltype_to_Ctype.argtypes = [c_int]
    db_sqltype_to_Ctype.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 372
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_start_driver'):
        continue
    db_start_driver = _lib.db_start_driver
    db_start_driver.argtypes = [String]
    db_start_driver.restype = POINTER(dbDriver)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 373
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_start_driver_open_database'):
        continue
    db_start_driver_open_database = _lib.db_start_driver_open_database
    db_start_driver_open_database.argtypes = [String, String]
    db_start_driver_open_database.restype = POINTER(dbDriver)
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 374
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__start_procedure_call'):
        continue
    db__start_procedure_call = _lib.db__start_procedure_call
    db__start_procedure_call.argtypes = [c_int]
    db__start_procedure_call.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 375
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_store'):
        continue
    db_store = _lib.db_store
    db_store.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        db_store.restype = ReturnString
    else:
        db_store.restype = String
        db_store.errcheck = ReturnString
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 376
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_strip'):
        continue
    db_strip = _lib.db_strip
    db_strip.argtypes = [String]
    db_strip.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 377
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_syserror'):
        continue
    db_syserror = _lib.db_syserror
    db_syserror.argtypes = [String]
    db_syserror.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 378
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_table_exists'):
        continue
    db_table_exists = _lib.db_table_exists
    db_table_exists.argtypes = [String, String, String]
    db_table_exists.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 380
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_column_has_default_value'):
        continue
    db_test_column_has_default_value = _lib.db_test_column_has_default_value
    db_test_column_has_default_value.argtypes = [POINTER(dbColumn)]
    db_test_column_has_default_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 381
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_column_has_defined_default_value'):
        continue
    db_test_column_has_defined_default_value = _lib.db_test_column_has_defined_default_value
    db_test_column_has_defined_default_value.argtypes = [POINTER(dbColumn)]
    db_test_column_has_defined_default_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 382
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_column_has_undefined_default_value'):
        continue
    db_test_column_has_undefined_default_value = _lib.db_test_column_has_undefined_default_value
    db_test_column_has_undefined_default_value.argtypes = [POINTER(dbColumn)]
    db_test_column_has_undefined_default_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 383
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_column_null_allowed'):
        continue
    db_test_column_null_allowed = _lib.db_test_column_null_allowed
    db_test_column_null_allowed.argtypes = [POINTER(dbColumn)]
    db_test_column_null_allowed.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 384
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_column_use_default_value'):
        continue
    db_test_column_use_default_value = _lib.db_test_column_use_default_value
    db_test_column_use_default_value.argtypes = [POINTER(dbColumn)]
    db_test_column_use_default_value.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 385
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_any_column_flag'):
        continue
    db_test_cursor_any_column_flag = _lib.db_test_cursor_any_column_flag
    db_test_cursor_any_column_flag.argtypes = [POINTER(dbCursor)]
    db_test_cursor_any_column_flag.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 386
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_any_column_for_update'):
        continue
    db_test_cursor_any_column_for_update = _lib.db_test_cursor_any_column_for_update
    db_test_cursor_any_column_for_update.argtypes = [POINTER(dbCursor)]
    db_test_cursor_any_column_for_update.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 387
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_column_flag'):
        continue
    db_test_cursor_column_flag = _lib.db_test_cursor_column_flag
    db_test_cursor_column_flag.argtypes = [POINTER(dbCursor), c_int]
    db_test_cursor_column_flag.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 388
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_column_for_update'):
        continue
    db_test_cursor_column_for_update = _lib.db_test_cursor_column_for_update
    db_test_cursor_column_for_update.argtypes = [POINTER(dbCursor), c_int]
    db_test_cursor_column_for_update.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 389
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_mode_insensitive'):
        continue
    db_test_cursor_mode_insensitive = _lib.db_test_cursor_mode_insensitive
    db_test_cursor_mode_insensitive.argtypes = [POINTER(dbCursor)]
    db_test_cursor_mode_insensitive.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 390
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_mode_scroll'):
        continue
    db_test_cursor_mode_scroll = _lib.db_test_cursor_mode_scroll
    db_test_cursor_mode_scroll.argtypes = [POINTER(dbCursor)]
    db_test_cursor_mode_scroll.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 391
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_type_fetch'):
        continue
    db_test_cursor_type_fetch = _lib.db_test_cursor_type_fetch
    db_test_cursor_type_fetch.argtypes = [POINTER(dbCursor)]
    db_test_cursor_type_fetch.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 392
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_type_insert'):
        continue
    db_test_cursor_type_insert = _lib.db_test_cursor_type_insert
    db_test_cursor_type_insert.argtypes = [POINTER(dbCursor)]
    db_test_cursor_type_insert.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 393
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_cursor_type_update'):
        continue
    db_test_cursor_type_update = _lib.db_test_cursor_type_update
    db_test_cursor_type_update.argtypes = [POINTER(dbCursor)]
    db_test_cursor_type_update.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 394
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db__test_database_open'):
        continue
    db__test_database_open = _lib.db__test_database_open
    db__test_database_open.argtypes = []
    db__test_database_open.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 395
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_index_type_unique'):
        continue
    db_test_index_type_unique = _lib.db_test_index_type_unique
    db_test_index_type_unique.argtypes = [POINTER(dbIndex)]
    db_test_index_type_unique.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 396
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_value_datetime_current'):
        continue
    db_test_value_datetime_current = _lib.db_test_value_datetime_current
    db_test_value_datetime_current.argtypes = [POINTER(dbValue)]
    db_test_value_datetime_current.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 397
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_test_value_isnull'):
        continue
    db_test_value_isnull = _lib.db_test_value_isnull
    db_test_value_isnull.argtypes = [POINTER(dbValue)]
    db_test_value_isnull.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 398
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_column_has_default_value'):
        continue
    db_unset_column_has_default_value = _lib.db_unset_column_has_default_value
    db_unset_column_has_default_value.argtypes = [POINTER(dbColumn)]
    db_unset_column_has_default_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 399
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_column_null_allowed'):
        continue
    db_unset_column_null_allowed = _lib.db_unset_column_null_allowed
    db_unset_column_null_allowed.argtypes = [POINTER(dbColumn)]
    db_unset_column_null_allowed.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 400
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_column_use_default_value'):
        continue
    db_unset_column_use_default_value = _lib.db_unset_column_use_default_value
    db_unset_column_use_default_value.argtypes = [POINTER(dbColumn)]
    db_unset_column_use_default_value.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 401
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_cursor_column_flag'):
        continue
    db_unset_cursor_column_flag = _lib.db_unset_cursor_column_flag
    db_unset_cursor_column_flag.argtypes = [POINTER(dbCursor), c_int]
    db_unset_cursor_column_flag.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 402
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_cursor_column_for_update'):
        continue
    db_unset_cursor_column_for_update = _lib.db_unset_cursor_column_for_update
    db_unset_cursor_column_for_update.argtypes = [POINTER(dbCursor), c_int]
    db_unset_cursor_column_for_update.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 403
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_cursor_mode'):
        continue
    db_unset_cursor_mode = _lib.db_unset_cursor_mode
    db_unset_cursor_mode.argtypes = [POINTER(dbCursor)]
    db_unset_cursor_mode.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 404
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_cursor_mode_insensitive'):
        continue
    db_unset_cursor_mode_insensitive = _lib.db_unset_cursor_mode_insensitive
    db_unset_cursor_mode_insensitive.argtypes = [POINTER(dbCursor)]
    db_unset_cursor_mode_insensitive.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 405
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_unset_cursor_mode_scroll'):
        continue
    db_unset_cursor_mode_scroll = _lib.db_unset_cursor_mode_scroll
    db_unset_cursor_mode_scroll.argtypes = [POINTER(dbCursor)]
    db_unset_cursor_mode_scroll.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 406
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_update'):
        continue
    db_update = _lib.db_update
    db_update.argtypes = [POINTER(dbCursor)]
    db_update.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 407
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_gversion'):
        continue
    db_gversion = _lib.db_gversion
    db_gversion.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbString)]
    db_gversion.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 409
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_whoami'):
        continue
    db_whoami = _lib.db_whoami
    db_whoami.argtypes = []
    db_whoami.restype = c_char_p
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 410
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_zero'):
        continue
    db_zero = _lib.db_zero
    db_zero.argtypes = [POINTER(None), c_int]
    db_zero.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 411
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_zero_string'):
        continue
    db_zero_string = _lib.db_zero_string
    db_zero_string.argtypes = [POINTER(dbString)]
    db_zero_string.restype = None
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 412
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_sizeof_string'):
        continue
    db_sizeof_string = _lib.db_sizeof_string
    db_sizeof_string.argtypes = [POINTER(dbString)]
    db_sizeof_string.restype = c_uint
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 413
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_login'):
        continue
    db_set_login = _lib.db_set_login
    db_set_login.argtypes = [String, String, String, String]
    db_set_login.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 414
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_set_login2'):
        continue
    db_set_login2 = _lib.db_set_login2
    db_set_login2.argtypes = [String, String, String, String, String, String, c_int]
    db_set_login2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 416
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_login'):
        continue
    db_get_login = _lib.db_get_login
    db_get_login.argtypes = [String, String, POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    db_get_login.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 417
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_login2'):
        continue
    db_get_login2 = _lib.db_get_login2
    db_get_login2.argtypes = [String, String, POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    db_get_login2.restype = c_int
    break

# D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32/include/grass/defs/dbmi.h: 419
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'db_get_login_dump'):
        continue
    db_get_login_dump = _lib.db_get_login_dump
    db_get_login_dump.argtypes = [POINTER(FILE)]
    db_get_login_dump.restype = c_int
    break

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 18
try:
    DB_VERSION = '0'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 21
try:
    DB_DEFAULT_DRIVER = 'sqlite'
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 27
try:
    DB_PROC_VERSION = 999
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 29
try:
    DB_PROC_CLOSE_DATABASE = 101
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 30
try:
    DB_PROC_CREATE_DATABASE = 102
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 31
try:
    DB_PROC_DELETE_DATABASE = 103
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 32
try:
    DB_PROC_FIND_DATABASE = 104
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 33
try:
    DB_PROC_LIST_DATABASES = 105
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 34
try:
    DB_PROC_OPEN_DATABASE = 106
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 35
try:
    DB_PROC_SHUTDOWN_DRIVER = 107
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 37
try:
    DB_PROC_CLOSE_CURSOR = 201
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 38
try:
    DB_PROC_DELETE = 202
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 39
try:
    DB_PROC_FETCH = 203
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 40
try:
    DB_PROC_INSERT = 204
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 41
try:
    DB_PROC_OPEN_INSERT_CURSOR = 205
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 42
try:
    DB_PROC_OPEN_SELECT_CURSOR = 206
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 43
try:
    DB_PROC_OPEN_UPDATE_CURSOR = 207
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 44
try:
    DB_PROC_UPDATE = 208
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 45
try:
    DB_PROC_ROWS = 209
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 46
try:
    DB_PROC_BIND_UPDATE = 220
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 47
try:
    DB_PROC_BIND_INSERT = 221
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 49
try:
    DB_PROC_EXECUTE_IMMEDIATE = 301
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 50
try:
    DB_PROC_BEGIN_TRANSACTION = 302
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 51
try:
    DB_PROC_COMMIT_TRANSACTION = 303
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 53
try:
    DB_PROC_CREATE_TABLE = 401
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 54
try:
    DB_PROC_DESCRIBE_TABLE = 402
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 55
try:
    DB_PROC_DROP_TABLE = 403
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 56
try:
    DB_PROC_LIST_TABLES = 404
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 57
try:
    DB_PROC_ADD_COLUMN = 405
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 58
try:
    DB_PROC_DROP_COLUMN = 406
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 59
try:
    DB_PROC_GRANT_ON_TABLE = 407
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 61
try:
    DB_PROC_CREATE_INDEX = 701
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 62
try:
    DB_PROC_LIST_INDEXES = 702
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 63
try:
    DB_PROC_DROP_INDEX = 703
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 66
try:
    DB_PERM_R = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 67
try:
    DB_PERM_W = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 68
try:
    DB_PERM_X = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 71
try:
    DB_OK = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 72
try:
    DB_FAILED = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 73
try:
    DB_NOPROC = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 74
try:
    DB_MEMORY_ERR = (-1)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 75
try:
    DB_PROTOCOL_ERR = (-2)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 76
try:
    DB_EOF = (-1)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 79
try:
    DB_SQL_TYPE_UNKNOWN = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 81
try:
    DB_SQL_TYPE_CHARACTER = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 82
try:
    DB_SQL_TYPE_SMALLINT = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 83
try:
    DB_SQL_TYPE_INTEGER = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 84
try:
    DB_SQL_TYPE_REAL = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 85
try:
    DB_SQL_TYPE_DOUBLE_PRECISION = 6
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 86
try:
    DB_SQL_TYPE_DECIMAL = 7
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 87
try:
    DB_SQL_TYPE_NUMERIC = 8
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 88
try:
    DB_SQL_TYPE_DATE = 9
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 89
try:
    DB_SQL_TYPE_TIME = 10
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 90
try:
    DB_SQL_TYPE_TIMESTAMP = 11
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 91
try:
    DB_SQL_TYPE_INTERVAL = 12
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 92
try:
    DB_SQL_TYPE_TEXT = 13
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 94
try:
    DB_SQL_TYPE_SERIAL = 21
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 97
try:
    DB_YEAR = 16384
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 98
try:
    DB_MONTH = 8192
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 99
try:
    DB_DAY = 4096
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 100
try:
    DB_HOUR = 2048
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 101
try:
    DB_MINUTE = 1024
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 102
try:
    DB_SECOND = 512
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 103
try:
    DB_FRACTION = 256
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 104
try:
    DB_DATETIME_MASK = 65280
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 107
try:
    DB_C_TYPE_STRING = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 108
try:
    DB_C_TYPE_INT = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 109
try:
    DB_C_TYPE_DOUBLE = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 110
try:
    DB_C_TYPE_DATETIME = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 113
try:
    DB_CURRENT = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 114
try:
    DB_NEXT = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 115
try:
    DB_PREVIOUS = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 116
try:
    DB_FIRST = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 117
try:
    DB_LAST = 5
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 120
try:
    DB_READONLY = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 121
try:
    DB_INSERT = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 122
try:
    DB_UPDATE = 3
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 123
try:
    DB_SEQUENTIAL = 0
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 124
try:
    DB_SCROLL = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 125
try:
    DB_INSENSITIVE = 4
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 128
try:
    DB_GRANTED = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 129
try:
    DB_NOT_GRANTED = (-1)
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 132
try:
    DB_PRIV_SELECT = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 134
try:
    DB_GROUP = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 135
try:
    DB_PUBLIC = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 138
try:
    DB_DEFINED = 1
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 139
try:
    DB_UNDEFINED = 2
except:
    pass

# D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 142
try:
    DB_SQL_MAX = 8192
except:
    pass

_db_string = struct__db_string # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 151

_dbmscap = struct__dbmscap # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 153

_db_dirent = struct__db_dirent # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 166

_db_driver = struct__db_driver # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 173

_db_handle = struct__db_handle # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 180

_db_date_time = struct__db_date_time # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 191

_db_value = struct__db_value # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 200

_db_column = struct__db_column # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 218

_db_table = struct__db_table # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 228

_db_cursor = struct__db_cursor # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 238

_db_index = struct__db_index # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 247

_db_driver_state = struct__db_driver_state # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 256

_db_connection = struct__db_connection # D:\\src\\osgeo4w\\src\\grass\\grass-7.8.6RC3\\dist.x86_64-w64-mingw32\\include\\grass\\dbmi.h: 304

# No inserted files

