@echo off

rem Call the Python script

set modpacks_dir="modpacks/"
set mods_dir="R:/Games/Steam/steamapps/common/Stardew Valley/Mods/"

python "nogui.py" %modpacks_dir% %mods_dir%

rem Pause at the end of the script (optional)