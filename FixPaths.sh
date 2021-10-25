#!/bin/bash 

# Written by Dr. Stevan Gavrilovic, University of California, Berkeley

# This script replaces the absolute path in libraries with the relative @loader_path or @rpath

# ********* THINGS TO CHANGE START *********

# Set the path where the bundled libs are
pathToInstall="/Users/steve/Desktop/SimCenter/QGISPlugin/mac/Install"

# ********* THINGS TO CHANGE END *********


# For each file in the install folder
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

			result=$secondString/"${firstString##*/}"

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

install_name_tool -id @rpath/libgdal.28.dylib $pathToInstall/lib/libgdal.28.dylib
install_name_tool -id @rpath/libproj.18.dylib $pathToInstall/lib/libproj.18.dylib
install_name_tool -id @rpath/libqscintilla2_qt5.15.0.0.dylib $pathToInstall/lib/libqscintilla2_qt5.15.0.0.dylib
install_name_tool -id @rpath/libsqlite3.0.dylib $pathToInstall/lib/libsqlite3.0.dylib
install_name_tool -id @rpath/libqt5keychain.1.dylib $pathToInstall/lib/libqt5keychain.1.dylib

# Now change the paths on the plugins
for f in $pathToInstall/qgis/plugins/*.so; do

    otool -L $f | sed 1d | \
    while read i
    do
        if [[ $i == *"/opt/QGIS"* ]]; then

            IFS=' '     # space is set as delimiter
            read -ra ADDR <<< "$i"   # str is read into an array as tokens separated by IF
            firstString="${ADDR[0]}"

            [ firstString == "" ] && continue

            secondString="@rpath"

            result=$secondString/"${firstString##*/}"

            # echo $result

            echo "Changing path for: " "$firstString $result $f"

            eval "install_name_tool -change $firstString $result $f" | xargs echo -n

            if [ $? != "0" ]; then
            echo "Error in install name tool: "$f
            exit
            fi
        fi
    done
done
