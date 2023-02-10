@echo off
REM ***************************************************************************

REM Change these paths as needed
set CurrDir=%cd%
set TargetDir=%CurrDir%\Release
set QGIS_Plugin_Dir=%CurrDir%\QGISPlugin
set DLLdir=%QGIS_Plugin_Dir%\win\DLLs
set Installdir=%QGIS_Plugin_Dir%\win\Install\Install_Release

if not exist "%QGIS_Plugin_Dir%" (echo "Could not find QGIS directory %QGIS_Plugin_Dir% set is manually" & goto error)

echo Current directory: %CurrDir%
echo Target directory: %TargetDir%
echo QGIS plugin directory: %QGIS_Plugin_Dir%
   
REM Copy over the dll dependency directory
copy "%DLLdir%" %TargetDir%\ 

if errorlevel 1 (echo "Could not copy DLLs from %DLLdir%" & goto error)

REM Copy over the plugins directory

xcopy "%Installdir%/plugins" "%TargetDir%/plugins" /e /i /h /y

if errorlevel 1 (echo "Could not copy plugins folder" & goto error)

REM Copy over the qgis dlls

copy "%Installdir%/bin" %TargetDir%\ 

if errorlevel 1 (echo "Could not copy qgis dlls from %Installdir%/bin" & goto error)


REM Copy over the i18n directory

xcopy "%Installdir%/i18n" "%TargetDir%/i18n" /e /i /h /y

if errorlevel 1 (echo "Could not copy i18n folder" & goto error)


REM Copy over the resources directory

xcopy "%Installdir%/resources" "%TargetDir%/resources" /e /i /h /y

if errorlevel 1 (echo "Could not copy resources folder" & goto error)

REM Copy over the svg directory

xcopy "%Installdir%/svg" "%TargetDir%/svg" /e /i /h /y

if errorlevel 1 (echo "Could not copy svg folder" & goto error)

goto end


:error
echo ERROR %ERRORLEVEL%: %DATE% %TIME%

exit /b 1

:end
echo FINISHED: %DATE% %TIME%

endlocal
