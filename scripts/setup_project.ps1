Write-Host -ForegroundColor Yellow "Checking and updating your dependencies"
# make sure pip is up to date and has dependencies for setup
python.exe -m pip install --upgrade pip
python.exe -m pip install --user virtualenv

Write-Host -ForegroundColor Yellow "Setting up a virtual enviroment to use modified bizhook version"
# setup venv
python.exe -m venv env
.\env\Scripts\activate
.\env\Scripts\python.exe -m pip install --upgrade pip

Write-Host -ForegroundColor Yellow "Cloning and installing API client library"
# get bizhook's latest version from repo
mkdir lib\bizhook
git clone https://github.com/SuperBlueHenBros/AutoHawkAPI-Client.git lib\bizhook
python.exe -m pip install -e lib\bizhook

Write-Host -ForegroundColor Yellow "Cloning the lua API server hook for bizhawk"
# get the latest lua-components
git clone https://github.com/SuperBlueHenBros/AutoHawkAPI-Server.git lib\lua-components

Write-Host -ForegroundColor Yellow "Installing any dependencies"
# install pynput for using keyboard input
python.exe -m pip install pynput

Write-Host -ForegroundColor Yellow "Installing middletier as a module with pip"
# install middle-tier with pip
python.exe -m pip install -e .