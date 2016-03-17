@echo off

set PATH=c:\Python27\;c:\Program Files (x86)\Java\jre1.8.0_73\bin\

call java -jar "%~dp0FitSDK\java\FitCSVTool.jar" -b "%~f1" "%~dp0tmp\tmp.csv"
call python "%~dp0clean.py" "%~dp0tmp\tmp.csv" "%~dp0tmp\tmp-fix.csv" 50
call java -jar "%~dp0FitSDK\java\FitCSVTool.jar" -c "%~dp0tmp\tmp-fix.csv" "%~dpn1-fix%~x1"

pause
