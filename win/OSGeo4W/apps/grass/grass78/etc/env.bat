REM
REM Environmental variables for GRASS OSGeo4W installer
REM

set GISBASE=%OSGEO4W_ROOT%\apps\grass\grass78

REM Uncomment if you want to use Bash instead of Cmd
REM Note that msys package must be also installed
REM set GRASS_SH=%OSGEO4W_ROOT%\apps\msys\bin\sh.exe

set GRASS_PYTHON=%OSGEO4W_ROOT%\bin\python3.exe
set GRASS_PROJSHARE=%OSGEO4W_ROOT%\share\proj

set FONTCONFIG_FILE=%GISBASE%\etc\fonts.conf
