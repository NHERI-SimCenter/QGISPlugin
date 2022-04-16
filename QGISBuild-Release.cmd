@echo off
REM ***************************************************************************
REM First need to follow instructions online on QGIS  github page to install dependencies using OSgeo4W and cygwin
REM Check the paths below to make sure they are still valid
REM Then Run this config script and if successful, a new VS window will open
REM Find the .sln file in this instance of MSVC (CMAKE generated this file in the build folder) and build the solution
REM It NEEDS to be in that instance of MSVC... or else it will not pick up the necessary Env vars
REM Otherwise need to run call "C:\OSGeo4W\etc\ini\qt5.bat" then "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2019.lnk" to open MSVC then go find the generated .sln file in the build folder

REM If you get an error MSB4035	The required attribute "Include" is empty or missing from the element <CustomBuild>, put a space between the quotes so that <CustomBuild Include="">=<CustomBuild Include=" ">

REM ***************************************************************************


REM Change these paths as needed
set O4W_ROOT=C:\OSGeo4W
set BUILDDIR=C:\Users\Office\Desktop\SimCenter\QGIS\Build_Release
set QTROOTDIR=C:\Qt\5.15.2\msvc2019_64

REM config without a build
set CONFIGONLY=1

setlocal enabledelayedexpansion

set VERSION=2.11.0
set PACKAGE=38
set PACKAGENAME=qgis-steve
set ARCH=x86_64
set SHA=Steve
set SITE=qgis.org

if not exist "%BUILDDIR%" mkdir %BUILDDIR%
if not exist "%BUILDDIR%" (echo could not create build directory %BUILDDIR% & goto error)

cd %BUILDDIR%

call %O4W_ROOT%\bin\o4w_env.bat
call %O4W_ROOT%\usr\src\osgeo4w\msvc-env.bat %ARCH%
:: call gdal-dev-env.bat


set LIB_DIR=%O4W_ROOT%

if "%ARCH%"=="x86" (
	set CMAKE_OPT=^
		-D SPATIALINDEX_LIBRARY=%O4W_ROOT%/lib/spatialindex-32.lib
) else (
	set CMAKE_OPT=^
		-D SPATIALINDEX_LIBRARY=%O4W_ROOT%/lib/spatialindex-64.lib ^
		-D CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_NO_WARNINGS=TRUE
)

for %%i in ("%GRASS_PREFIX%") do set GRASS7_VERSION=%%~nxi
set GRASS_VERSIONS=%GRASS7_VERSION%

set TAR=tar.exe
if exist "c:\cygwin\bin\tar.exe" set TAR=c:\cygwin\bin\tar.exe
if exist "c:\cygwin64\bin\tar.exe" set TAR=c:\cygwin64\bin\tar.exe

set BUILDCONF=Release


cd ..\QGIS
set SRCDIR=%CD%

if "%BUILDDIR:~1,1%"==":" %BUILDDIR:~0,2%
cd %BUILDDIR%

set PKGDIR=%OSGEO4W_ROOT%\apps\%PACKAGENAME%

if exist repackage goto package

if not exist build.log goto build

REM
REM try renaming the logfile to see if it's locked
REM

if exist build.tmp del build.tmp
if exist build.tmp (echo could not remove build.tmp & goto error)

ren build.log build.tmp
if exist build.log goto locked
if not exist build.tmp goto locked

ren build.tmp build.log
if exist build.tmp goto locked
if not exist build.log goto locked

goto build

:locked
echo Logfile locked
if exist build.tmp del build.tmp
goto error

:build
echo BEGIN: %DATE% %TIME%

set >buildenv.log

if exist qgsversion.h del qgsversion.h

rem if exist CMakeCache.txt if exist skipcmake goto skipcmake

touch %SRCDIR%\CMakeLists.txt

echo CMAKE: %DATE% %TIME%

if "%CMAKEGEN%"=="" set CMAKEGEN=Visual Studio 16 2019
if "%OSGEO4W_CXXFLAGS%"=="" set OSGEO4W_CXXFLAGS=/MD /Z7 /MP /Od /D NDEBUG

for %%i in (%PYTHONHOME%) do set PYVER=%%~ni


cmake -G "%CMAKEGEN%" ^
	-D CMAKE_BUILD_TYPE=Release ^
	-D CMAKE_CXX_COMPILER="%CXX:\=/%" ^
	-D PKG_CONFIG_EXECUTABLE=C:\Users\Office\Desktop\C++Libraries\pkgconfig\pkg-config.exe ^
	-D CMAKE_INSTALL_PREFIX=C:\Users\Office\Desktop\QGIS\Install_Release ^
	-D Python_EXECUTABLE=C:\OSGeo4W\bin\python.exe ^
	-D CMAKE_C_COMPILER="%CC:\=/%" ^
	-D CMAKE_LINKER="%CMAKE_COMPILER_PATH:\=/%/link.exe" ^
	-D CMAKE_CXX_FLAGS_RELWITHDEBINFO="%OSGEO4W_CXXFLAGS%" ^
	-D CMAKE_PDB_OUTPUT_DIRECTORY_RELWITHDEBINFO=%BUILDDIR%\apps\%PACKAGENAME%\pdb ^
	-D SUBMIT_URL="https://cdash.orfeo-toolbox.org/submit.php?project=QGIS" ^
	-D BUILDNAME="%BUILDNAME%" ^
	-D SITE="%SITE%" ^
	-D PEDANTIC=TRUE ^
	-D ENABLE_TESTS=0 ^
	-D LIBRARY_TYPE=SHARED ^
	-D WITH_BINDINGS=0 ^
	-D WITH_QTWEBKIT=0 ^
	-D WITH_GUI=1 ^
	-D WITH_DESKTOP=0 ^
	-D WITH_SPATIALITE=0 ^
	-D WITH_CORE=1 ^
	-D WITH_SERVER=0 ^
	-D WITH_QSPATIALITE=0 ^
	-D WITH_HANA=0 ^
	-D WITH_3D=1 ^
	-D WITH_ORACLE=0 ^
	-D WITH_CUSTOM_WIDGETS=0 ^
	-D WITH_GRASS=TRUE ^
	-D WITH_GRASS7=TRUE ^
	-D GRASS_PREFIX7=%GRASS_PREFIX:\=/% ^
	-D CMAKE_BUILD_TYPE=%BUILDCONF% ^
	-D CMAKE_CONFIGURATION_TYPES=%BUILDCONF% ^
	-D SETUPAPI_LIBRARY="%SETUPAPI_LIBRARY%" ^
	-D PROJ_LIBRARY=%O4W_ROOT%/lib/proj.lib ^
	-D PROJ_INCLUDE_DIR=%O4W_ROOT%/include ^
	-D GDAL_LIBRARY=%O4W_ROOT%/lib/gdal_i.lib ^
	-D GDAL_INCLUDE_DIR=%O4W_ROOT%/include ^
	-D GEOS_LIBRARY=%O4W_ROOT%/lib/geos_c.lib ^
	-D SQLITE3_LIBRARY=%O4W_ROOT%/lib/sqlite3_i.lib ^
	-D SPATIALITE_LIBRARY=%O4W_ROOT%/lib/spatialite_i.lib ^
	-D PYTHON_EXECUTABLE=%O4W_ROOT%/bin/python3.exe ^
	-D SIP_BINARY_PATH=%PYTHONHOME:\=/%/sip.exe ^
	-D PYTHON_INCLUDE_DIR=%PYTHONHOME:\=/%/include ^
	-D PYTHON_LIBRARY=%PYTHONHOME:\=/%/libs/%PYVER%.lib ^
	-D QT_LIBRARY_DIR=%QTROOTDIR%/lib ^
	-D QT_HEADERS_DIR=%QTROOTDIR%/include ^
	-D FCGI_INCLUDE_DIR=%O4W_ROOT%/include ^
	-D FCGI_LIBRARY=%O4W_ROOT%/lib/libfcgi.lib ^
	-D QCA_INCLUDE_DIR=%OSGEO4W_ROOT%\apps\Qt5\include\QtCrypto ^
	-D QCA_LIBRARY=%OSGEO4W_ROOT%\apps\Qt5\lib\qca-qt5.lib ^
	-D QSCINTILLA_LIBRARY=%OSGEO4W_ROOT%\apps\Qt5\lib\qscintilla2_qt5.lib ^
	-D DART_TESTING_TIMEOUT=60 ^
	-D PUSH_TO_CDASH=TRUE ^
	-D CMAKE_PREFIX_PATH=%QTROOTDIR% ^
	%CMAKE_OPT% ^
	%SRCDIR:\=/%
if errorlevel 1 (echo cmake failed & goto error)

if "%CONFIGONLY%"=="1" (

"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2019.lnk"

echo Exiting after configuring build directory: %CD% & goto end
)


:skipcmake
if exist ..\noclean (echo skip clean & goto skipclean)
echo CLEAN: %DATE% %TIME%
cmake --build %BUILDDIR% --target clean --config %BUILDCONF%
if errorlevel 1 (echo clean failed & goto error)

:skipclean
if exist ..\skipbuild (echo skip build & goto skipbuild)
echo ALL_BUILD: %DATE% %TIME%
cmake --build %BUILDDIR% --target %TARGET%Build --config %BUILDCONF%
set /P tag=<%BUILDDIR%\Testing\TAG
findstr "<Error>" %BUILDDIR%\Testing\%tag%\Build.xml >nul
if not errorlevel 1 (
	cmake --build %BUILDDIR% --target %TARGET%Submit --config %BUILDCONF%
	if errorlevel 1 echo SUBMITTING BUILD ERRORS WAS NOT SUCCESSFUL.
	echo build failed
	goto error
)

:skipbuild
if exist ..\skiptests goto skiptests

echo RUN_TESTS: %DATE% %TIME%

reg add "HKCU\Software\Microsoft\Windows\Windows Error Reporting" /v DontShow /t REG_DWORD /d 1 /f

set oldtemp=%TEMP%
set oldtmp=%TMP%
set oldpath=%PATH%

set TEMP=%TEMP%\%PACKAGENAME%-%ARCH%
set TMP=%TEMP%
if exist "%TEMP%" rmdir /s /q "%TEMP%"
mkdir "%TEMP%"

for %%g IN (%GRASS_VERSIONS%) do (
	set path=!path!;%OSGEO4W_ROOT%\apps\grass\%%g\lib
	set GISBASE=%OSGEO4W_ROOT%\apps\grass\%%g
)
PATH %path%;%BUILDDIR%\output\plugins
set QT_PLUGIN_PATH=%BUILDDIR%\output\plugins;%OSGEO4W_ROOT%\apps\qt5\plugins

cmake --build %BUILDDIR% --target %TARGET%Test --config %BUILDCONF%
if errorlevel 1 echo TESTS WERE NOT SUCCESSFUL.

set TEMP=%oldtemp%
set TMP=%oldtmp%
PATH %oldpath%

cmake --build %BUILDDIR% --target %TARGET%Submit --config %BUILDCONF%
if errorlevel 1 echo TEST SUBMISSION WAS NOT SUCCESSFUL.

:skiptests
if exist ..\skippackage goto end

if exist "%PKGDIR%" (
	echo REMOVE: %DATE% %TIME%
	rmdir /s /q "%PKGDIR%"
)

echo INSTALL: %DATE% %TIME%
cmake --build %BUILDDIR% --target install --config %BUILDCONF%
if errorlevel 1 (echo INSTALL failed & goto error)

:package
echo PACKAGE: %DATE% %TIME%

cd ..

sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' -e 's/@grassversions@/%GRASS_VERSIONS%/g' postinstall-dev.bat >%OSGEO4W_ROOT%\etc\postinstall\%PACKAGENAME%.bat
if errorlevel 1 (echo creation of desktop postinstall failed & goto error)

sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' -e 's/@grassversions@/%GRASS_VERSIONS%/g' preremove-dev.bat >%OSGEO4W_ROOT%\etc\preremove\%PACKAGENAME%.bat
if errorlevel 1 (echo creation of desktop preremove failed & goto error)

sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' -e 's/^call py3_env.bat/call gdal-dev-py3-env.bat/' designer.bat.tmpl >%OSGEO4W_ROOT%\bin\%PACKAGENAME%-designer.bat.tmpl
if errorlevel 1 (echo creation of designer template failed & goto error)
sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' qgis.reg.tmpl >%PKGDIR%\bin\qgis.reg.tmpl
if errorlevel 1 (echo creation of registry template & goto error)

sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' -e 's/^call py3_env.bat/call gdal-dev-py3-env.bat/' qgis.bat.tmpl >%OSGEO4W_ROOT%\bin\%PACKAGENAME%.bat.tmpl
if errorlevel 1 (echo creation of desktop template failed & goto error)

set batches=bin/%PACKAGENAME%.bat.tmpl
for %%g IN (%GRASS_VERSIONS%) do (
	for /f "usebackq tokens=1" %%a in (`%%g --config version`) do set gv=%%a
	for /F "delims=." %%i in ("!gv!") do set v=%%i

	sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' -e 's/@grasspath@/%%g/g' -e 's/@grassversion@/!gv!/g' -e 's/^call py3_env.bat/call gdal-dev-py3-env.bat/' qgis-grass.bat.tmpl >%OSGEO4W_ROOT%\bin\%PACKAGENAME%-g!v!.bat.tmpl
	if errorlevel 1 (echo creation of desktop template failed & goto error)
	set batches=!batches! bin/%PACKAGENAME%-g!v!.bat.tmpl
)

sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' -e 's/^call py3_env.bat/call gdal-dev-py3-env.bat/' python.bat.tmpl >%OSGEO4W_ROOT%\bin\python-%PACKAGENAME%.bat.tmpl
if errorlevel 1 (echo creation of python wrapper template failed & goto error)

sed -e 's/@package@/%PACKAGENAME%/g' -e 's/@version@/%VERSION%/g' -e 's/^call py3_env.bat/call gdal-dev-py3-env.bat/' process.bat.tmpl >%OSGEO4W_ROOT%\bin\qgis_process-%PACKAGENAME%.bat.tmpl
if errorlevel 1 (echo creation of qgis process wrapper template failed & goto error)

touch exclude
if exist ..\skipbuild (echo skip build & goto skipbuild)

move %PKGDIR%\bin\qgis.exe %OSGEO4W_ROOT%\bin\%PACKAGENAME%-bin.exe
if errorlevel 1 (echo move of desktop executable failed & goto error)
copy qgis.vars %OSGEO4W_ROOT%\bin\%PACKAGENAME%-bin.vars
if errorlevel 1 (echo copy of desktop executable vars failed & goto error)

if not exist %PKGDIR%\qtplugins\sqldrivers mkdir %PKGDIR%\qtplugins\sqldrivers
move %OSGEO4W_ROOT%\apps\qt5\plugins\sqldrivers\qsqlocispatial.dll %PKGDIR%\qtplugins\sqldrivers
if errorlevel 1 (echo move of oci sqldriver failed & goto error)
move %OSGEO4W_ROOT%\apps\qt5\plugins\sqldrivers\qsqlspatialite.dll %PKGDIR%\qtplugins\sqldrivers
if errorlevel 1 (echo move of spatialite sqldriver failed & goto error)

if not exist %PKGDIR%\qtplugins\designer mkdir %PKGDIR%\qtplugins\designer
move %OSGEO4W_ROOT%\apps\qt5\plugins\designer\qgis_customwidgets.dll %PKGDIR%\qtplugins\designer
if errorlevel 1 (echo move of customwidgets failed & goto error)

if not exist %PKGDIR%\python\PyQt5\uic\widget-plugins mkdir %PKGDIR%\python\PyQt5\uic\widget-plugins
move %PYTHONHOME%\Lib\site-packages\PyQt5\uic\widget-plugins\qgis_customwidgets.py %PKGDIR%\python\PyQt5\uic\widget-plugins
if errorlevel 1 (echo move of customwidgets binding failed & goto error)

for %%i in (dbghelp.dll symsrv.dll) do (
	copy "%DBGHLP_PATH%\%%i" %OSGEO4W_ROOT%\apps\%PACKAGENAME%
	if errorlevel 1 (echo %%i not found & goto error)
)

if not exist %ARCH%\release\qgis\%PACKAGENAME% mkdir %ARCH%\release\qgis\%PACKAGENAME%
%TAR% -C %OSGEO4W_ROOT% -cjf %ARCH%/release/qgis/%PACKAGENAME%/%PACKAGENAME%-%VERSION%-%PACKAGE%.tar.bz2 ^
	--exclude-from exclude ^
	--exclude "*.pyc" ^
	apps/%PACKAGENAME% ^
	bin/%PACKAGENAME%-bin.exe ^
	bin/%PACKAGENAME%-bin.vars ^
	%batches% ^
	bin/%PACKAGENAME%-designer.bat.tmpl ^
	bin/python-%PACKAGENAME%.bat.tmpl ^
	bin/qgis_process-%PACKAGENAME%.bat.tmpl ^
	etc/postinstall/%PACKAGENAME%.bat ^
	etc/preremove/%PACKAGENAME%.bat
if errorlevel 1 (echo tar failed & goto error)

if not exist %ARCH%\release\qgis\%PACKAGENAME%-pdb mkdir %ARCH%\release\qgis\%PACKAGENAME%-pdb
%TAR% -C %BUILDDIR% -cjf %ARCH%/release/qgis/%PACKAGENAME%-pdb/%PACKAGENAME%-pdb-%VERSION%-%PACKAGE%.tar.bz2 ^
	apps/%PACKAGENAME%/pdb
if errorlevel 1 (echo tar failed & goto error)

goto end

:usage
echo usage: %0 version package packagename arch [sha [site]]
echo sample: %0 2.11.0 38 qgis-dev x86_64 339dbf1 qgis.org
exit /b 1

:error
echo BUILD ERROR %ERRORLEVEL%: %DATE% %TIME%
if exist %PACKAGENAME%-%VERSION%-%PACKAGE%.tar.bz2 del %PACKAGENAME%-%VERSION%-%PACKAGE%.tar.bz2
exit /b 1

:end
echo FINISHED: %DATE% %TIME%

endlocal
