@echo off
REM ***************************************************************************

REM Change these paths as needed
set CurrDir=%cd%
set QGIS_Plugin_Dir=%cd%/../QGISPlugin
set DLLdir=%QGIS_Plugin_Dir%/win/DLLs
set Installdir=%QGIS_Plugin_Dir%/win/Install/Install_Debug

if not exist "%QGIS_Plugin_Dir%" (echo "Could not find QGIS directory %QGIS_Plugin_Dir% set is manually" & goto error)

echo Current directory: %CurrDir%
   
REM Copy over the dll dependency directory
copy "%DLLdir%" %CurrDir%\ 

if errorlevel 1 (echo "Could not copy DLLs from %DLLdir%" & goto error)

REM Copy over the plugins directory

xcopy "%DLLdir%/plugins" "%CurrDir%/plugins" /e /i /h /y

if errorlevel 1 (echo "Could not copy plugins folder" & goto error)

REM Copy over the qgis dlls

copy "%Installdir%/bin" %CurrDir%\ 

if errorlevel 1 (echo "Could not copy qgis dlls from %Installdir%/bin" & goto error)


REM Copy over the i18n directory

xcopy "%Installdir%/i18n" "%CurrDir%/i18n" /e /i /h /y

if errorlevel 1 (echo "Could not copy i18n folder" & goto error)


REM Copy over the resources directory

xcopy "%Installdir%/resources" "%CurrDir%/resources" /e /i /h /y

if errorlevel 1 (echo "Could not copy resources folder" & goto error)

REM Copy over the svg directory

xcopy "%Installdir%/svg" "%CurrDir%/svg" /e /i /h /y

if errorlevel 1 (echo "Could not copy svg folder" & goto error)

goto end


:error
echo ERROR %ERRORLEVEL%: %DATE% %TIME%

exit /b 1

:end
echo FINISHED: %DATE% %TIME%

endlocal
