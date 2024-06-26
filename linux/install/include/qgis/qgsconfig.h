
// QGSCONFIG.H

#ifndef QGSCONFIG_H
#define QGSCONFIG_H

// Version must be specified according to
// <int>.<int>.<int>-<any text>.
// or else upgrading old project file will not work
// reliably.
// TODO QGIS 4: remove in favor of _QGIS_VERSION
#define VERSION "3.25.0-Master"
#define _QGIS_VERSION "3.25.0-Master"

//used in vim src/core/qgis.cpp
//The way below should work but it resolves to a number like 0110 which the compiler treats as octal I think
//because debuggin it out shows the decimal number 72 which results in incorrect version status.
//As a short term fix I (Tim) am defining the version in top level cmake. It would be good to
//reinstate this more generic approach below at some point though
//#define VERSION_INT 3250
// TODO QGIS 4: Remove in favor of _QGIS_VERSION_INT
#define VERSION_INT 32500
#define _QGIS_VERSION_INT 32500
#define ABISYM(x) x ## 32500
//used in main.cpp and anywhere else where the release name is needed
#define RELEASE_NAME "Master"

#define QGIS_PLUGIN_SUBDIR "lib/qgis/plugins"
#define QGIS_DATA_SUBDIR "share/qgis"
#define QGIS_LIBEXEC_SUBDIR "lib/qgis"
#define QGIS_LIB_SUBDIR "lib"
#define QGIS_QML_SUBDIR "qml"
#define CMAKE_INSTALL_PREFIX "/home/satishr/simcenter/install"
#define CMAKE_SOURCE_DIR "/home/satishr/dev/cpp/QGIS"

#define QGIS_SERVER_MODULE_SUBDIR "lib/qgis/server"

#if !defined(QSCINTILLA_VERSION_STR)
#define QSCINTILLA_VERSION_STR "2.13.2"
#endif

#if defined( __APPLE__ )
//used by Mac to find system or bundle resources relative to amount of bundling
#define QGIS_MACAPP_BUNDLE 3
#endif

#define QT_PLUGINS_DIR "/usr/lib/qt/plugins"

#define PYTHON_VERSION "3.10.4"
#define PYTHON_VERSION_MAJOR "3"
#define PYTHON_VERSION_MINOR "10"
#define PYTHON_VERSION_PATCH "4"

#define PROJ_VERSION_MAJOR 8
#define PROJ_VERSION_MINOR 2
#define PROJ_VERSION_PATCH 0

/* #undef USING_NMAKE */

/* #undef USING_NINJA */

#define HAVE_GUI

/* #undef HAVE_SPATIALITE */

#define HAVE_POSTGRESQL

/* #undef HAVE_ORACLE */

/* #undef HAVE_HANA */

/* #undef SERVER_SKIP_ECW */

/* #undef HAVE_SERVER_PYTHON_PLUGINS */

#define HAVE_OAUTH2_PLUGIN

#define HAVE_OPENCL
/* #undef OPENCL_USE_NEW_HEADER */

/* #undef ENABLE_MODELTEST */

#define HAVE_3D

#define HAVE_GSL

#define HAVE_GEOREFERENCER

#define USE_THREAD_LOCAL

/* #undef QGISDEBUG */

/* #undef HAVE_QUICK */

#define HAVE_QT5SERIALPORT

/* #undef HAVE_STATIC_PROVIDERS */

#define HAVE_EPT

#define HAVE_COPC

/* #undef HAVE_PDAL_QGIS */
#define PDAL_VERSION ""
#define PDAL_VERSION_MAJOR_INT 
#define PDAL_VERSION_MINOR_INT 
#define PDAL_VERSION_MAJOR ""
#define PDAL_VERSION_MINOR ""
#define PDAL_VERSION_MICRO ""

/* #undef ENABLE_TESTS */

/* #undef HAS_KDE_QT5_PDF_TRANSFORM_FIX */
/* #undef HAS_KDE_QT5_SMALL_CAPS_FIX */
/* #undef HAS_KDE_QT5_FONT_STRETCH_FIX */

/* #undef HAVE_CRASH_HANDLER */

#endif

