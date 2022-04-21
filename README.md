# QGIS plugin for SimCenter tools

This package provides the libraries and source code for implementing a QGIS-based widget within a SimCenter tool. 

First clone this repo and in the .pro file of your project add the following variable:

    PATH_TO_QGIS_PLUGIN=../../QGISPlugin

where **../../QGISPlugin** should be the path to this repo. Include the repo into your build tree by including the **QGIS.pri** file as below:

    include($$PATH_TO_QGIS_PLUGIN/QGIS.pri)

To add the visualization widget in your code create an instance of the **QGISVisualizationWidget** class

    QGISVisualizationWidget

Once compiled, to get full QGIS functionality, the following folders need to be copied into the built package:

For Mac
1) Copy the folder **../QGISPlugin/mac/Install/share** to the folder **R2D.app/Contents/MacOS**
2) Copy the folder **../QGISPlugin/mac/Install/qgis** to the folder **R2D.app/Contents/MacOS/lib**


### How to compile R2D with QGIS

1) Clone the QGISPlugin repo: https://github.com/sgavrilovic/QGISPlugin.git
2) In R2D.pro change the PATH_TO_QGIS_PLUGIN variable to point to the repo where you cloned the QGISPlugin code, e.g., PATH_TO_QGIS_PLUGIN=../../QGISPlugin

FOR MAC ONLY: 

During runtime the executable needs to find the QGIS library and its dependencies. Otherwise you will get a *.dylib not found error when you try to run the application. Two options are: 

1) Copy everything from the **../QGISPlugin/mac/Install/lib** folder into the **R2D.app/Contents/Frameworks** folder. Copy everything from **../QGISPlugin/mac/qgis-deps-0.8.0/stage/lib** folder into the same **R2D.app/Contents/Frameworks** folder. 

2) Set the DYLD_FRAMEWORK_PATH and DYLD_LIBRARY_PATH variables to point to the folders where the QGIS libraries are located. To do this in Qt Creator click on Projects->Run->Environment and under the **Build Environment** change the following:
	
	Add to **DYLD_FRAMEWORK_PATH** the following paths (changing the paths in bold to reflect folder locations on your computer): **/Users/steve/Desktop/SimCenter**/QGISPlugin/mac/Install/lib:**/Users/steve/Desktop/SimCenter**/QGISPlugin/mac/qgis-deps-0.8.0/stage/lib

	Add to **DYLD_LIBRARY_PATH** the following paths (changing the paths in bold to reflect folder locations on your computer): **/Users/steve/Desktop/SimCenter**/QGISPlugin/mac/Install/lib:**/Users/steve/Desktop/SimCenter**/QGISPlugin/mac/qgis-deps-0.8.0/stage


Note: If you get an error during compilation, you may have to uncheck the "Add build library search path to DYLD_LIBRARY_PATH and DYLD_FRAMEWORK_PATH" option Under **Projects->Run**

### Contact

Dr. Stevan Gavrilovic

gavrilovic@berkeley.edu

