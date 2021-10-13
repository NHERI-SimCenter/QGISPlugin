#!/bin/bash 

# Written by Stevan Gavrilovic, University of California, Berkeley

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


# For each file in the temp folder
for f in $pathToInstall/lib/*.dylib; do
	
	otool -L $f | sed 1d | \
	while read i
	do
		if [[ $i == *"/opt/QGIS"* ]]; then
			
			IFS=' '     # space is set as delimiter
			read -ra ADDR <<< "$i"   # str is read into an array as tokens separated by IF
			firstString="${ADDR[0]}"
			
			[ firstString == "" ] && continue
			
			secondString="@loader_path"
			toRep="/opt/QGIS/qgis-deps-0.8.0/stage/lib"
			
			result="${firstString/$toRep/$secondString}" 
			
			echo "Changing" "$firstString $result $f"
						
			install_name_tool -id $result $f
			install_name_tool -change $firstString $result $f
			
		    if [ $? != "0" ]; then
		    echo "Error in install name tool: "$f
		    exit
		    fi
		fi
	done
    
done

