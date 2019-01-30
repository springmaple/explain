@ECHO OFF
SET CWD=%cd%
CD /D %~dp0\scripts
python explain.py %1
CD /D %CWD%
