#!/bin/bash 

# Put this file in the folder where your app executable is and run it to install the libs in their proper place

# ********* THINGS TO CHANGE START *********

pathToQGIS=/Users/steve/Desktop/SimCenter/QGISPlugin

# ********* THINGS TO CHANGE END *********

currDir=$PWD

cd .. 

mkdir Frameworks

cp -R $pathToQGIS/mac/Install/lib/*.dylib ./Frameworks/
cp -a $pathToQGIS/mac/qgis-deps-0.9/stage/lib/* ./Frameworks/

cd $currDir

mkdir lib

cp -R $pathToQGIS/mac/Install/qgis ./lib/


cp -R $pathToQGIS/mac/Install/share .