![Discord](https://img.shields.io/discord/337666388527153163?label=discord&logo=discord&style=flat-square)

This is the repository for *Darkest Hour: Europe '44-'45*. For more information, visit the [Steam Store](https://store.steampowered.com/app/1280/).

## Prerequisites
Before cloning this repository, all of the following requirements must be satisfied.

### System
* You must be using a Windows OS.
* You must have the [RODIR environment variable](https://github.com/DarklightGames/DarkestHour/wiki/RODIR-Environment-Variable) defined on your machine.

### Dependencies & Tools
* [Git for Windows](https://git-scm.com/downloads)
* [Python ≥3.5.4](https://www.python.org/downloads/) (we use Python to supplement our various build processes)

### Base game & SDK
This game is a modification for *Red Orchestra: Ostfront 41-45* and requires you to own the base game. You'll need to have the following apps installed:
* [Steam](http://store.steampowered.com)
* [Red Orchestra: Ostfront 41-45](http://store.steampowered.com/app/1200/)
* [Red Orchestra SDK Beta](https://github.com/DarklightGames/DarkestHour/wiki/SDK-Installation)

## Cloning the repository
Apart from the code files, the repository also contains asset packages (maps, textures, meshes, etc.), which are stored using Git Large File Storage. To clone it, you'll have to perform a few extra steps.

Before you continue, make sure you have at least **11GB** of free disk space on the drive where *Red Orchestra* is installed on, as asset files are quite hefty.

### Option 1: Using Command Prompt
1. Open a Command Prompt window in Administrator mode by pressing <kbd>Win</kbd>, typing `cmd`, then pressing <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd>.
2. Enter the following commands, hitting <kbd>Enter</kbd> after each line:
```batch
cd /d "%RODIR%"
git lfs install --skip-smudge
git clone https://github.com/DarklightGames/DarkestHour.git tmp
xcopy tmp . /e /h /y
rmdir /s /q tmp
git lfs pull
git lfs install --force
```

### Option 2: Using Git Bash
```bash
$ cd "$RODIR"
$ git lfs install --skip-smudge
$ git clone https://github.com/DarklightGames/DarkestHour.git tmp
$ cp -rf tmp/. .
$ rm -rf tmp
$ git lfs pull
$ git lfs install --force
```

## Running the application
After completing the steps above and successfully cloning the repository, you can:
* Run the development version of the game via `%RODIR%/System/DarkestHourDev.bat`. 
* Run the development version of the SDK via `%RODIR%/System/DHEd.bat`.

Be aware that these batch files will compile the game's code files if necessary. Compilation can fail if there are errors in your code.
