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
pathQGISlibs="/Users/steve/Desktop/SimCenter/QGIS/Install/lib"
pathDeplibs="/opt/QGIS/qgis-deps-0.8.0/stage/lib"

# Set the path where you want the bundled libs to go
pathToInstall="/Users/steve/Desktop/SimCenter/QGISPlugin/mac/Install"

# Set the path to dylibbundler on your computer
pathBundler="/usr/local/Cellar/dylibbundler/1.0.0/bin/dylibbundler"

# Export the DYLD_LIBRARY_PATH path for dylibbundler
export DYLD_LIBRARY_PATH=/opt/QGIS/qgis-deps-0.8.0/stage/lib

QGISVersion="3.21.0"

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

# Copy over the items from the QGIS Install libs folder into the temp folder
cp –R $pathQGISlibs/* $libsdirTemp/

#cp $pathQGISlibs/libqgis_3d.$QGISVersion.dylib $libsdirTemp/
#cp $pathQGISlibs/libqgis_analysis.$QGISVersion.dylib $libsdirTemp/
#cp $pathQGISlibs/libqgis_core.$QGISVersion.dylib $libsdirTemp/
#cp $pathQGISlibs/libqgis_gui.$QGISVersion.dylib $libsdirTemp/
#cp $pathQGISlibs/libqgis_native.$QGISVersion.dylib $libsdirTemp/
#cp $pathQGISlibs/libqgisgrass7.$QGISVersion.dylib $libsdirTemp/

# Copy the required dependency libs into the temp folder
cp $pathDeplibs/libgdal.28.dylib $libsdirTemp/
cp $pathDeplibs/libproj.18.2.3.dylib $libsdirTemp/
cp $pathDeplibs/libqscintilla2_qt5.15.0.0.dylib $libsdirTemp/
cp $pathDeplibs/libqt5keychain.0.12.0.dylib $libsdirTemp/

# For each file in the temp folder
for f in $libsdirTemp/*.dylib; do

    echo "Now bundling: "$f
    
    # Handle the QCA framework
    install_name_tool -change "$pathDeplibs/qca-qt5.framework/Versions/2.3.0/qca-qt5" "@rpath/qca-qt5.framework/Versions/2.3.0/qca-qt5" $f
    
    # Call dylib bundler to bundle the libs
    $pathBundler -of -b -p "@loader_path/" -x $f -d $libsdir
    
    if [ $? != "0" ]; then
    echo "Error in bundling: "$f
    exit
    fi
    
done

# Copy over all of the items from the temp folder into the libs folder
cp –R $libsdirTemp/* $libsdir/

## Remove the temporary lib directory
#echo "Removing temp lib directory "$libsdirTemp
#rm -dr $libsdirTemp

echo "Success in bundling all libraries"
