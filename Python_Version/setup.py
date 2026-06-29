"""
SETUP.PY

Author: Afonso Silvestre
Date: 20-06-2026
Description:
    This script creates a bash file that initializes
    the vpn in the home folder, and creates a desktop
    shortcut for the file as well.
    We first create the files, write their scripts 
    and then make them executable.

Usage:
    python setup.py    

"""

from pathlib import Path
from utils import get_desktop_path, make_executable, write_to_file

BASH_PATH = Path.home() / "vpn.sh"
BASH_SCRIPT: str = "#!/bin/bash\necho \"RUNNING NOVA FCT VPN\"\nsudo snx-rs -s vpn.fct.unl.pt -u CLIP_USERNAME -o vpn_Username_Password -X true -T tcpt"

SHORTCUT_PATH = get_desktop_path() / "VPN.desktop"
print(SHORTCUT_PATH)
SHORTCUT_SCRIPT: str = "[Desktop Entry]\nType=Application\nName=VPN\nExec=PATH\nTerminal=true"

username = input("What is your CLIP username?\n")

write_to_file(BASH_PATH, BASH_SCRIPT.replace("CLIP_USERNAME", username, 1))
make_executable(BASH_PATH)

write_to_file(SHORTCUT_PATH, SHORTCUT_SCRIPT.replace("PATH", str(BASH_PATH.resolve()), 1))
make_executable(SHORTCUT_PATH)