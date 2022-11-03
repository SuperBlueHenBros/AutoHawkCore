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

#### Demo

Run `python.exe demo.py -d` inside the virtual enviroment you set up. 

