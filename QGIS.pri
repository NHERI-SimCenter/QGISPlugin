QT += svg printsupport

#Change these to the appropriate folders
mac {

DEFINES += Q_WS_MAC HAVE_STATIC_PROVIDERS #WITH_QTWEBKIT

PATH_TO_QGIS_DEPS=/opt/QGIS/qgis-deps-0.8.0/stage

PATH_TO_QGIS_SRC=$$PWD/mac/src
PATH_TO_QGIS_EXT=$$PWD/mac/external
#PATH_TO_INSTALL=/Users/steve/Desktop/SimCenter/QGIS/Install
PATH_TO_INSTALL=$$PWD/mac/Install


} else {

}


# Do not change
PATH_TO_QGIS_DEPS_INC=$$PATH_TO_QGIS_DEPS/include

# Need this to prevent a compile error
DEFINES += TEST_DATA_DIR=\\\"$$PWD/tests/testdata\\\"

INCLUDEPATH += \
            $$PWD \

include(QGISSrc.pri)

SOURCES += \
        $$PWD/QgisApp.cpp \

HEADERS += \
        $$PWD/QgisApp.h \

