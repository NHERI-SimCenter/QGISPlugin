QT += svg printsupport

#Change these to the appropriate folders
mac {

DEFINES += Q_WS_MAC HAVE_STATIC_PROVIDERS #WITH_QTWEBKIT

PATH_TO_QGIS_DEPS=/opt/QGIS/qgis-deps-0.8.0/stage

PATH_TO_QGIS_SRC=$$PWD/mac/src
PATH_TO_INSTALL=$$PWD/mac/Install


} else {

DEFINES += Q_WS_WIN APP_STATIC_DEFINE HAVE_STATIC_PROVIDERS QTSIGNAL_STATIC_DEFINE QWT_DLL # CORE_STATIC_DEFINE  GUI_STATIC_DEFINE ANALYSIS_STATIC_DEFINE NATIVE_STATIC_DEFINE _3D_STATIC_DEFINE

# Defines needed to compile with MSVS
DEFINES += NOMINMAX _IMAGEHLP_SOURCE_ _USE_MATH_DEFINES

PATH_TO_QGIS_DEPS=$$PWD\win\OSGeo4W
PATH_TO_QGIS_SRC=$$PWD\win\src
PATH_TO_INSTALL=$$PWD\win\Install

}


# Do not change
PATH_TO_QGIS_EXT=$$PWD/external

# Need this to prevent a compile error
DEFINES += TEST_DATA_DIR=\\\"$$PWD/tests/testdata\\\"

INCLUDEPATH += \
            $$PWD \

include(QGISSrc.pri)

SOURCES += \
        $$PWD/QgisApp.cpp \

HEADERS += \
        $$PWD/QgisApp.h \

