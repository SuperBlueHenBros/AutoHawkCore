<# 
    FIRST TIME SETUP ONLY
    Do not run if you already have a venv folder
#>

# make sure pip is up to date and has dependencies for setup
python.exe -m pip install --upgrade pip
python.exe -m pip install --user virtualenv

# setup venv
python.exe -m venv env
.\env\Scripts\activate
.\env\Scripts\python.exe -m pip install --upgrade pip

# get bizhook's latest version from repo
mkdir lib\bizhook
git clone https://github.com/SuperBlueHenBros/Bizhook.git lib\bizhook
python.exe -m pip install -e lib\bizhook
