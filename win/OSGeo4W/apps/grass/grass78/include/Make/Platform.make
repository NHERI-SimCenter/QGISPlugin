#############################################################################
#
# MODULE:   	Grass Compilation
# AUTHOR(S):	Original author unknown - probably CERL
#		Markus Neteler - Germany/Italy - neteler@itc.it
#   	    	Justin Hickey - Thailand - jhickey@hpcc.nectec.or.th
#   	    	Huidae Cho - Korea - grass4u@gmail.com
#   	    	Eric G. Miller - egm2@jps.net
# PURPOSE:  	The source file for this Makefile is in src/CMD/head/head.in.
#		It is the top part of a file called make.rules which is used
#		for compiling all GRASS modules. This part of the file provides
#		make variables that are dependent on the results of the
#		configure script.
# COPYRIGHT:    (C) 2000 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#   	    	License (>=v2). Read the file COPYING that comes with GRASS
#   	    	for details.
#
#############################################################################

############################## Make Variables ###############################

CC                  = x86_64-w64-mingw32-gcc
CXX                 = x86_64-w64-mingw32-g++
LEX                 = flex
YACC                = bison -y
PERL                = /usr/bin/perl
AR                  = ar
RANLIB              = ranlib
MKDIR               = mkdir -p
CHMOD               = chmod
INSTALL             = /usr/bin/install -c 
INSTALL_DATA        = ${INSTALL} -m 644

prefix              = /D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/apps/grass
exec_prefix         = ${prefix}
ARCH                = x86_64-w64-mingw32
UNIX_BIN            = /D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/bin
INST_DIR            = ${prefix}/grass78

GRASS_HOME          = /D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/apps/grass/grass78
RUN_GISBASE         = D:/src/osgeo4w/src/grass/grass-7.8.6RC3/dist.x86_64-w64-mingw32

GRASS_VERSION_MAJOR = 7
GRASS_VERSION_MINOR = 8
GRASS_VERSION_RELEASE = 6RC3
GRASS_VERSION_DATE  = 2021
GRASS_VERSION_GIT   = exported

STRIPFLAG           = 
LD_SEARCH_FLAGS     = 
LD_LIBRARY_PATH_VAR = PATH

#generate static (ST) or shared (SH)
GRASS_LIBRARY_TYPE  = shlib

#static libs:
STLIB_LD            = ${AR} cr
STLIB_PREFIX        = lib
STLIB_SUFFIX        = .a

#shared libs
SHLIB_PREFIX        = lib
SHLIB_LD            = x86_64-w64-mingw32-gcc -shared
SHLIB_LDFLAGS       = 
SHLIB_CFLAGS        = 
SHLIB_SUFFIX        = .dll
EXE                 = .exe

DEFAULT_DATABASE    =
DEFAULT_LOCATION    =

CPPFLAGS            =   -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
CFLAGS              = -g -O2 
CXXFLAGS            = -g -O2
INCLUDE_DIRS        =  -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
LINK_FLAGS          =   -Wl,--export-dynamic,--enable-runtime-pseudo-reloc  -L/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/lib

DLLIB               = 
XCFLAGS             = 
XLIBPATH            = 
XLIB                =  
XEXTRALIBS          = 
USE_X11             = 

MATHLIB             =  
ICONVLIB            = -liconv
INTLLIB             = -lintl
SOCKLIB             = 

#ZLIB:
ZLIB                =  -lz 
ZLIBINCPATH         = 
ZLIBLIBPATH         = 

#BZIP2:
BZIP2LIB            =  -lbz2 
BZIP2INCPATH        = 
BZIP2LIBPATH        = 

#ZSTD:
ZSTDLIB             =  -lzstd 
ZSTDINCPATH         = 
ZSTDLIBPATH         = 

DBMIEXTRALIB        = 

#readline
READLINEINCPATH     = 
READLINELIBPATH     = 
READLINELIB         = 
HISTORYLIB          = 

#PostgreSQL:
PQINCPATH           =  -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
PQLIBPATH           =  -L/d/src/osgeo4w/src/grass/grass-7.8.6RC3/mswindows/osgeo4w/lib
PQLIB               =  -lpq 
USE_POSTGRES        = 1

#MySQL:
MYSQLINCPATH        = 
MYSQLLIBPATH        = 
MYSQLLIB            = 
MYSQLDLIB           = 

#SQLite:
SQLITEINCPATH       =  -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
SQLITELIBPATH       =  -L/d/src/osgeo4w/src/grass/grass-7.8.6RC3/mswindows/osgeo4w/lib
SQLITELIB           =  -lsqlite3 

#ODBC:
ODBCINC             = 
ODBCLIB             =  -lodbc32 

#Image formats:
PNGINC              = 
PNGLIB              =  -lpng  -lz  
USE_PNG             = 1

TIFFINCPATH         = 
TIFFLIBPATH         = 
TIFFLIB             =  -ltiff 

#openGL files for NVIZ/r3.showdspf
OPENGLINC           = 
OPENGLLIB           =   -lopengl32 
OPENGLULIB          =   -lglu32 
OPENGL_X11          = 
OPENGL_AQUA         = 
OPENGL_WINDOWS      = 1
USE_OPENGL          = 1

#FFTW:
FFTWINC             = 
FFTWLIB             =  -lfftw3 

#LAPACK/BLAS stuff for gmath lib:
BLASLIB             = 
BLASINC             = 
LAPACKLIB           = 
LAPACKINC           = 

#GDAL/OGR
GDALLIBS            = /D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/lib/gdal_i.lib
GDALCFLAGS          = -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
USE_GDAL            = 1
USE_OGR             = 1

#NetCDF
NETCDFLIBS          = 
NETCDFCFLAGS        =     
USE_NETCDF          = 

#LAS LiDAR through libLAS
LASLIBS             = /D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/lib/liblas_c.lib
LASCFLAGS           = 
LASINC              = -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
USE_LIBLAS          = 1

#LAS LiDAR through PDAL
PDALLIBS             = 
PDALCPPFLAGS         = 
PDALINC              = 
USE_PDAL             = 

#GEOS
GEOSLIBS            = /D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/lib/geos_c.lib -lgeos_c 
GEOSCFLAGS          = -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
USE_GEOS            = 1

#FreeType:
FTINC               =  -I/mingw64/include/freetype2
FTLIB               =  -lfreetype 

#PROJ.4:
PROJINC             =  -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
PROJLIB             =  -L/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/lib -lproj 
PROJSHARE           = /D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/share/proj

#OPENDWG:
OPENDWGINCPATH      = 
OPENDWGLIBPATH      = 
OPENDWGLIB          = 
USE_OPENDWG         = 

#cairo
CAIROINC                  = -mms-bitfields -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/cairo -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/lzo -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/pixman-1 -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/freetype2 -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/libpng16 -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/harfbuzz -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include/glib-2.0 -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/lib/glib-2.0/include -ID:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/include -I/D/src/osgeo4w/src/grass/osgeo4w/osgeo4w/include
CAIROLIB                  = -LD:/src/osgeo4w/src/grass/osgeo4w/msys64/mingw64/lib -lcairo -lpng16 -lz -lfontconfig -lfreetype -L/d/src/osgeo4w/src/grass/grass-7.8.6RC3/mswindows/osgeo4w/lib -lcairo -lfontconfig 
USE_CAIRO                 = 1
CAIRO_HAS_XRENDER         = 
CAIRO_HAS_XRENDER_SURFACE = 

#Python
PYTHON              = python3

#regex
REGEXINCPATH        = 
REGEXLIBPATH        = 
REGEXLIB            =  -lregex 
USE_REGEX           = 1

#pthreads
PTHREADINCPATH      = 
PTHREADLIBPATH      = 
PTHREADLIB          = 
USE_PTHREAD         = 

#OpenMP
OMPINCPATH          = 
OMPLIBPATH          = 
OMPLIB              = 
OMPCFLAGS           = 
USE_OPENMP          = 

#OpenCL
OCLINCPATH          = 
OCLLIBPATH          = 
OCLLIB              = 
USE_OPENCL          = 

#i18N
HAVE_NLS            = 1

#Large File Support (LFS)
USE_LARGEFILES      = 1
LFS_CFLAGS          = -D_FILE_OFFSET_BITS=64

#BSD sockets
HAVE_SOCKET         = 

MINGW		    = yes
MACOSX_APP	    = 
MACOSX_ARCHS        = 
MACOSX_SDK          = 

# Cross compilation
CROSS_COMPILING     =  
