@echo off
IF ["%1"]==[""] GOTO ERROR

:CREATE
MKDIR day%1
COPY "templates\template2.py" "day%1\day%1.py"
echo Successfully created Day %1
GOTO END

:ERROR
echo "No day was specified"

:END