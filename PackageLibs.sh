#!/bin/bash 

# Written by Stevan Gavrilovic, University of California, Berkeley

# Go through the paths below in the file to ensure that the version numbers match in your pathDeplibs folder

# ********* THINGS TO CHANGE START *********
# Set the path to the where the QGIS libs are located
pathQGISlibs="/Users/steve/Desktop/SimCenter/QGIS/Install/lib"
pathDeplibs="/opt/QGIS/qgis-deps-0.9/stage/lib"

# Set the path where you want the bundled libs to go
pathToInstall="/Users/steve/Desktop/SimCenter/QGISPlugin/mac/Install"


# Set the path to dylibbundler on your computer
pathBundler="/usr/local/Cellar/dylibbundler/1.0.0/bin/dylibbundler"

# Export the DYLD_LIBRARY_PATH path for dylibbundler
export DYLD_LIBRARY_PATH=/opt/QGIS/qgis-deps-0.9/stage/lib

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

# use -R to do a recursive copy, will copy symlinks by default
# Copy over the items from the QGIS Install libs folder into the temp folder
cp –R $pathQGISlibs/*.dylib $libsdirTemp/

# Copy the required dependency libs into the temp folder
cp -R $pathDeplibs/libgdal.29.dylib $libsdirTemp/

cp -R $pathDeplibs/libproj.22.1.1.dylib $libsdirTemp/
cp -R $pathDeplibs/libproj.22.dylib $libsdirTemp/

cp -R $pathDeplibs/libqscintilla2_qt5.15.0.0.dylib $libsdirTemp/
cp -R $pathDeplibs/libqscintilla2_qt5.15.dylib $libsdirTemp/

cp -R $pathDeplibs/libqt5keychain.0.12.0.dylib $libsdirTemp/
cp -R $pathDeplibs/libqt5keychain.1.dylib $libsdirTemp/


# For each file in the temp folder
for f in $libsdirTemp/*.dylib; do

    echo "Now bundling: "$f
    
    # Handle the QCA framework
    install_name_tool -change "$pathDeplibs/qca-qt5.framework/Versions/2.3.1/qca-qt5" "@rpath/qca-qt5.framework/Versions/2.3.1/qca-qt5" $f
    
    # Call dylib bundler to bundle the libs
    $pathBundler -of -b -p "@loader_path/" -x $f -d $libsdir
    
    if [ $? != "0" ]; then
    echo "Error in bundling: "$f
    exit
    fi
    
done

sudo chmod -R 755 $libsdirTemp


# Copy over all of the items from the temp folder into the libs folder
echo "Copying over files from the temp dir: "$libsdirTemp" into the lib folder: "$libsdir

cp -R $libsdirTemp/* $libsdir

if [ $? != "0" ]; then
echo "Error in copying over files from the temp dir into the lib folder"
exit
fi

# Copy over the qgis folder into the libs folder
echo "Copying over the qgis folder: "$pathQGISlibs/qgis" into the lib folder: "$libsdir

cp -r $pathQGISlibs/qgis $pathToInstall/

if [ $? != "0" ]; then
echo "Error in copying over the qgis dir into the lib dir"
exit
fi

## Remove the temporary lib directory
#echo "Removing temp lib directory "$libsdirTemp
#rm -dr $libsdirTemp

echo "Success in bundling all libraries"
