# Middle-Tier

## Description 

The main interface of the program's components. Used to communicate between our AI and bizhawk. 

## Dependencies
Python >=3.9

Bizhawk

## Usage

### Setup

#### Windows

##### Install

To initialize all dependencies run `setup_windows.ps1` from inside the root of the repo.

Then open and run hook.lua in Bizhawk's lua console. The socket ip and port should display in Bizhawks's OCD.

#### Resetting

If something something seems to be acting up, you can reset installed dependencies with `reset_project.ps1`. Run it in powershell inside the root of the repo. Do this before running the setup again.

### Running

#### Enviroment

Make sure you are inside the virtual enviroment when running the program. To access it after the initial setup run `\env\Scripts\activate`. 
If you don't see a (env) in your terminal session you are not in the virtual enviroment.

#### Excecution

When inside the virtual enviroment, run `python.exe middle-tier/middle-tier.py`. You typically shouldn't ever be running any of the other files. 
This will probably be updated to use a new structure.

#### Args
```
usage: middle-tier [-h] [-c] [-d] [-g GAME] [-l] [-m] [-p] [-r ROM] [-q] [-v] [-vv]

options:
  -h, --help            show this help message and exit
  -c, --config          Force running of first-time config setup
  -d, --demo            Test demo using the sample config
  -g GAME, --game GAME  Select a specific game config file to use
  -l, --loop            Continously display the state of all addresses in console
  -m, --manual          Don't automatically start bizhawk, let the user start it manually instead
  -p, --play            (Warning: Buggy) Play the game yourself!
  -r ROM, --rom ROM     Specify the path to the file you'll be opening
  -q, --quiet           Only log errors to stdout
  -v, --verbose         Log extra info to stdout
  -vv, --very_verbose   Log all debug info to stdout
```

#### Examples

##### Continously poll for memory output
```
python.exe .\middle-tier\middle-tier.py --game ".\game-data\NES\Excitebike.json" --rom "[YOUR PATH TO ROMS GOES HERE]\Excitebike (JU) [!].nes" --loop
```

##### Play the game via CLI
```
python.exe .\middle-tier\middle-tier.py --game ".\game-data\NES\Excitebike.json" --rom "[YOUR PATH TO ROMS GOES HERE]\Excitebike (JU) [!].nes" --loop --play
```