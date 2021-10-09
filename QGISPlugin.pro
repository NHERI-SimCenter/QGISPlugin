
QT += core widgets gui xml network sql concurrent webengine webenginewidgets

CONFIG += c++17



# Do not change. Keep the folder format where there is a QGIS root folder and in it there is a build, source, and install folder
PATH_TO_QGIS=$$PATH_TO_QGIS_ROOT/QGIS
PATH_TO_QGIS_SRC=$$PATH_TO_QGIS/src
PATH_TO_QGIS_DEPS_INC=$$PATH_TO_QGIS_DEPS/include
PATH_TO_QGIS_BUILD=$$PATH_TO_QGIS_ROOT/build

PATH_TO_QGIS_PLUGIN=$$PWD

include(./QGIS.pri)




