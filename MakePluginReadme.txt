

Mac OS
-------

Step 1) Compile the QGIS source

cd the QGIS plugin dir containing the file 'BuildQGIS.sh' and run the 'BuildQGIS.sh' file in sudo. The QGIS source (https://github.com/sgavrilovic/qgis) must be one dir down from the QGISPlugin dir. First go into 'BuildQGIS.sh' and change the paths at the top of the file to match your system.

Step 2) Run the 'PackageLibs.sh' script to bundle the libs. It will use dylib_bundler: brew install dylibbundler

If dylib_bundler throws an error, cannot find lib, pass it the path to /opt/QGIS/qgis-deps-0.9/stage/lib, or wherever the QGIS deps are


Step 3) Run the 'FixPaths.sh' script to make the dylib. dependency paths rpaths in the install folder. You may have to run this script more than once, until it no longer says "changing path for ... "


Note: had to build QCA on system, did not use the QCA that came bundled with QGIS deps

Build QCA

cmake .. -DCMAKE_PREFIX_PATH=/Users/steve/Qt/5.15.2/clang_64 -D CMAKE_OSX_DEPLOYMENT_TARGET=10.13 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/Users/steve/Desktop/C++Libraries/qca/QCAInstall


Step 4) Copy over the include, share, etc. folders from the QGIS/Install 

Issues: 

If the plugins will not load, check the plugins output text in the visualization widget by clicking on the message icon in the bottom right corner. It will usually complain about missing simlinks that dylib bundler does not pick up. 

Windows
-------

Need to compile plugin both in release and debug. 

First need to download the dependencies using OSGeo4W and "qgis-rel-dev-deps" branch for the current release

Run the QGISBuild-Debug.cmd and QGISBuild-Release.cmd to build.  Note: make sure to set the paths on your system and your version of Qt that you will be building your app with. This needs to match. For example, if you are using Qt5.15.2 in your app, the QGIS plugin needs to be compiled with the same version.

After the plugin is built, need to copy the files from the "install" folder over to the QGIS plugin folder for the particular OS, e.g., QGISPlugin\win\Install

Then, from the "build" folder need copy over the ui_* files from \QGIS\Build\src\ui to QGISPlugin\win\Install\include

Next, you will need to copy the app source folder. We are going to build the app, but as a plugin, and not a standalone widget as QGIS is built.  To facilitate this, copy the folder \QGIS\src\app into QGISPlugin\win\src

We will need some other source files as well: 

Copy over the 'ogr' folder from \QGIS\src\gui to QGISPlugin\win\src\app

Copy over the 'processing' folder from \QGIS\src\analysis to QGISPlugin\win\src\app

Copy over the 'processing' folder from \QGIS\src\core to QGISPlugin\win\src\app\processing

Copy over the 'scalebar' folder from \QGIS\src\core to QGISPlugin\win\src\app

Copy over the 'raster' folder from  \QGIS\src\gui to QGISPlugin\win\src\app

Copy over the 'layout' folder from  \QGIS\src\gui to QGISPlugin\win\src\app

Copy over the 'effects' folder from  \QGIS\src\gui to QGISPlugin\win\src\app

Copy over the 'diagram' folder from  \QGIS\src\core to QGISPlugin\win\src\app

Copy over the 'auth' folder from  \QGIS\src\gui to QGISPlugin\win\src\app

Copy over the 'attributetable' folder from  \QGIS\src\gui to QGISPlugin\win\src\app

Copy over the 'geometry' folder from  \QGIS\src\core to QGISPlugin\win\src\app

Copy over the 'mesh' folder from  \QGIS\src\core to QGISPlugin\win\src\app

Copy over the 'mesh' folder from  \QGIS\src\gui to QGISPlugin\win\src\app

Copy over the contents of the 'mesh' folder from  \QGIS\src\gui\mesh to QGISPlugin\win\src\app\mesh

Copy over the 'plugins' folder from  \QGIS\src to QGISPlugin\win\src\app

Copy over the '3d' folder from \QGIS\src\3d to QGISPlugin\win\src\app\3d


ISSUES: In debug config, I needed to compile protobuf myself and upload it to the OSGeo4W lib/bin/include folders; due to a symbol mismatch error that is thrown

Need to build qt5keychain
cmake C:\Users\Office\Desktop\C++Libraries\qtkeychain-master\qtkeychain-master -DCMAKE_PREFIX_PATH=C:\Qt\5.15.2\msvc2019_64 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=C:\Users\Office\Desktop\C++Libraries\qtkeychain-master\install
Build qt5keychain with MSVC (debug/release)

Need to build qca
cmake C:\Users\Office\Desktop\C++Libraries\qca-master\qca-master -DCMAKE_PREFIX_PATH=C:\Qt\5.15.2\msvc2019_64 -DPKG_CONFIG_EXECUTABLE=C:\Users\Office\Desktop\C++Libraries\pkgconfig\pkg-config.exe -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=C:\Users\Office\Desktop\C++Libraries\qca-master\install
Build qca with MSVC (debug/release)

Need to build qwt(download source and build with .pro file) After build, cd build folder and run 'nmake install' to install dlls (will install in root c:\\ dir)

Finally, need to build scintilla (download source and run pro file) After build, cd build folder and run 'nmake install' to install dlls (will install in Qt dirs)

Curl

cmake C:\Users\Office\Desktop\C++Libraries\curl-7.63.0\curl-7.63.0 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=C:\Users\Office\Desktop\C++Libraries\curl-7.63.0\Install

Tiff

cmake C:\Users\Office\Desktop\C++Libraries\tiff-4.3.0rc1\tiff-4.3.0 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=C:\Users\Office\Desktop\C++Libraries\tiff-4.3.0rc1\install

Proj

cmake C:\Users\Office\Desktop\proj-9.0.0\proj-9.0.0 ^
-DCMAKE_PREFIX_PATH=C:\OSGeo4W ^
-DCMAKE_BUILD_TYPE=Release ^
-DCMAKE_INSTALL_PREFIX=C:\Users\Office\Desktop\proj-9.0.0\install ^
-DTIFF_LIBRARY=C:\Users\Office\Desktop\C++Libraries\tiff-4.3.0rc1\install\lib\tiff.lib ^
-DTIFF_INCLUDE_DIR=C:\Users\Office\Desktop\C++Libraries\tiff-4.3.0rc1\install\include ^
-DCURL_LIBRARY=C:\Users\Office\Desktop\C++Libraries\curl-7.63.0\Install\lib\libcurl_imp.lib ^
-DCURL_INCLUDE_DIR=C:\Users\Office\Desktop\C++Libraries\curl-7.63.0\Install\include

