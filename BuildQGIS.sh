#!/bin/bash 

# Written by Dr. Stevan Gavrilovic, University of California, Berkeley

# \!/ Note: some changes were made to this script and it is not tested

# Usage: 
# Need to install pyQt5 and sip on system python: python3 -m pip install sip pyqt5
# First you need to install the dependencies. Go to this guide: <https://github.com/qgis/QGIS/blob/master/INSTALL.md#5-building-on-macos-x> to do that. Qt and dependencies will be installed in opt/ folder 
# Change the deps version and qt version below when upgrading. Again, note where the deps folder and Qt are installed
# Also, change the install prefix so it installs everything in the QGIS plugin folder

# Issues:
# - If you have problems with DWITH_QTWEBKIT off, you need to ifdef some statements out in the file where the error occurs.
# - When you add the QCA framework, errors may throw as system libs will conflict with the libs in deps. Delete the libs in deps that cause this to occur, i.e., libjpeg, libpng, etc.
# - You will need to copy over the header and source files from the QGISApp as listed in your projects pro file

PATH_TO_INSTALL=/Users/steve/Desktop/SimCenter/QGIS/Install
PATH_TO_DEPS=/opt/QGIS

_qt5Core_install_prefix=/opt/Qt/5.15.2/clang_64

QGIS_DEPS_VERSION=0.8.0;\
QT_VERSION=5.15.2;\
PATH=$PATH_TO_DEPS/qgis-deps-${QGIS_DEPS_VERSION}/stage/bin:$PATH;\

cmake \
  -D CMAKE_INSTALL_PREFIX=$PATH_TO_INSTALL \
  -D CMAKE_BUILD_TYPE=Release \
  -D ENABLE_TESTS=0 \
  -D QGIS_MACAPP_BUNDLE=3 \
  -D QGIS_MACAPP_FRAMEWORK= 0 \
  -D WITH_BINDINGS=0 \
  -D WITH_QTWEBKIT=0 \
  -D WITH_3D=1 \
  -D WITH_GUI=1 \
  -D QGIS_MACAPP_INSTALL_DEV=1 \
  -D WITH_DESKTOP=0 \
  -D WITH_SPATIALITE=0 \
  -D LIBRARY_TYPE=SHARED \
  -D WITH_CORE=1 \
  -D WITH_SERVER=0 \
  -D QGIS_MAC_DEPS_DIR=$PATH_TO_DEPS/qgis-deps-${QGIS_DEPS_VERSION}/stage \
  -D CMAKE_PREFIX_PATH=/opt/Qt/${QT_VERSION}/clang_64 \
  ../QGIS

