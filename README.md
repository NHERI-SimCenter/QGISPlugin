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
1) Copy the folder QGISPlugin/mac/Install/share to the folder Contents/MacOS
2) Copy the folder QGISPlugin/mac/Install/qgis to the folder Contents/MacOS/lib


### How to compile R2D with QGIS

1) Clone the QGISPlugin repo: https://github.com/sgavrilovic/QGISPlugin.git
2) In R2D.pro change the PATH_TO_QGIS_PLUGIN variable to point to the repo where you cloned the QGISPlugin code, e.g., PATH_TO_QGIS_PLUGIN=../../QGISPlugin

FOR MAC ONLY: 
3) You need to set the DYLD_FRAMEWORK_PATH and DYLD_LIBRARY_PATH variables to point to the plugin libs folder. To do this in Qt Creator click on Projects->Run->Environment
	Add to DYLD_FRAMEWORK_PATH the following paths: /Users/steve/Desktop/SimCenter/QGISPlugin/mac/Install/lib:/Users/steve/Desktop/SimCenter/QGISPlugin/mac/qgis-deps-0.8.0/stage/lib
	Add to DYLD_LIBRARY_PATH the following paths: /Users/steve/Desktop/SimCenter/QGISPlugin/mac/Install/lib:/Users/steve/Desktop/SimCenter/QGISPlugin/mac/qgis-deps-0.8.0/stage
4) Under Projects->Run->you have to uncheck the "Add build library search path to DYLD_LIBRARY_PATH and DYLD_FRAMEWORK_PATH" option

### Contact

Dr. Stevan Gavrilovic

gavrilovic@berkeley.edu

