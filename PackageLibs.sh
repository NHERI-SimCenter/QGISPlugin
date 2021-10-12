#!/bin/bash 

# Written by Stevan Gavrilovic, University of California, Berkeley
# Usage: 
# 	1) cd the folder one directory above the OpenSeesPyMac folder containing setup.py and version.py
# 	2) Copy this script file over to that folder
#   3) Change the version number in the version.py file
#   4) Check if testing or release, and uncomment the appropriate line 96-99
# 	5) Run: bash PackageApp.sh
#   6) Twine username: steva44

# ********* THINGS TO CHANGE START *********
# Set the path to the where the QGIS libs are located
pathlibs="/Users/steve/Desktop/SimCenter/QGIS/Install/lib"

# Set the path where you want the bundled libs to go
pathToInstall="/Users/steve/Desktop/SimCenter/QGISPlugin/QGISPlugin/mac/Install"

# Set the path to dylibbundler on your computer
pathBundler="/usr/local/Cellar/dylibbundler/1.0.0/bin/dylibbundler"

# ********* THINGS TO CHANGE END *********


# Check to see if the dylibbundler exists at the given location
if [ ! -f "$pathBundler" ]; then
    
    echo "Could not find dylibbundler at $pathBundler. Exiting"
    exit
fi

# The name of the libs folder
libsdir=$pathToInstall/lib

# Remove the libs dir if it exists, dylib bundler will make one
if [ -d "$libsdir" ]; then
echo "Lib directory " $libsdir " exists, removing"
rm -dr $libsdir
fi

mkdir $libsdir

libsdirTemp=$pathToInstall/Temp

# Remove the libs dir if it exists, dylib bundler will make one
if [ -d "$libsdirTemp" ]; then
echo "Lib directory " $libsdirTemp " exists, removing"
rm -dr $libsdirTemp
fi

mkdir $libsdirTemp

# Copy over all of the items from the libs folder in the folder containing
cp –R $pathlibs/* $libsdirTemp/

# Export the DYLD_LIBRARY_PATH path for dylibbundler
export DYLD_LIBRARY_PATH=/opt/QGIS/qgis-deps-0.8.0/stage/lib

# Call dylib bundler to bundle the core lib
$pathBundler -of -b -p "@loader_path/" -x $libsdirTemp/libqgis_core.dylib -d $libsdir

if [ $? != "0" ]; then
echo "Error. Exiting at core lib"
exit
fi

# Call dylib bundler to bundle the gui lib
$pathBundler -of -b -p "@loader_path/" -x $libsdirTemp/libqgis_gui.dylib -d $libsdir

if [ $? != "0" ]; then
echo "Error. Exiting at gui lib"
exit
fi

# Call dylib bundler to bundle the analysis lib
$pathBundler -of -b -p "@loader_path/" -x $libsdirTemp/libqgis_analysis.dylib -d $libsdir

if [ $? != "0" ]; then
echo "Error. Exiting at analysis lib"
exit
fi

# Call dylib bundler to bundle the native lib
$pathBundler -of -b -p "@loader_path/" -x $libsdirTemp/libqgis_native.dylib -d $libsdir

if [ $? != "0" ]; then
echo "Error. Exiting at native lib"
exit
fi

# Call dylib bundler to bundle the grass lib
$pathBundler -of -b -p "@loader_path/" -x $libsdirTemp/libqgisgrass7.dylib -d $libsdir

if [ $? != "0" ]; then
echo "Error. Exiting at grass lib"
exit
fi

# Call dylib bundler to bundle the 3d lib
$pathBundler -of -b -p "@loader_path/" -x $libsdirTemp/libqgis_3d.dylib -d $libsdir

if [ $? != "0" ]; then
echo "Error. Exiting at 3d lib"
exit
fi

# Copy over all of the items from the temp folder into the libs folder
cp –R $libsdirTemp/* $libsdir/
