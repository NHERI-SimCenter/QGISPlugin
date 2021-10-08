QT += svg printsupport

DEFINES += Q_WS_MAC HAVE_STATIC_PROVIDERS #WITH_QTWEBKIT

DEFINES += TEST_DATA_DIR=\\\"$$PWD/tests/testdata\\\"

INCLUDEPATH += $$PATH_TO_QGIS_PLUGIN

include($$PATH_TO_QGIS_PLUGIN/QGISSrc.pri)

SOURCES += \
        $$PATH_TO_QGIS_PLUGIN/QGISVisualizationWidget.cpp \
        $$PATH_TO_QGIS_PLUGIN/QgisApp.cpp \

HEADERS += \
        $$PATH_TO_QGIS_PLUGIN/QGISVisualizationWidget.h \
        $$PATH_TO_QGIS_PLUGIN/QgisApp.h \

