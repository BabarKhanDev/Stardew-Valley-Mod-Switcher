@echo off

rem Call the Python script

set modpacks_dir="modpacks/"
set mods_dir="R:/Games/Steam/steamapps/common/Stardew Valley/Mods/"

python "nogui.py" %modpacks_dir% %mods_dir%

set steam="C:/Games/Steam/steam.exe"

%steam% "steam://rungameid/413150"