#!/bin/bash 

# Written by Dr. Stevan Gavrilovic, University of California, Berkeley

# This script replaces the absolute path in libraries with the relative @loader_path 

# ********* THINGS TO CHANGE START *********

# Set the path where the bundled libs are
pathToInstall="/Users/steve/Desktop/SimCenter/QGISPlugin/mac/Install"

pathToReplace="/opt/QGIS/qgis-deps-0.8.0/stage/lib"

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
			toRep=$pathToReplace
			
			result="${firstString/$toRep/$secondString}" 
			
			echo "Changing path for: " "$firstString $result $f"
						
			install_name_tool -id $result $f
			install_name_tool -change $firstString $result $f
			
		    if [ $? != "0" ]; then
		    echo "Error in install name tool: "$f
		    exit
		    fi
		fi
	done
    
done

