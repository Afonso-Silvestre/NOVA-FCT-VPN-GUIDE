import subprocess, shutil, getpass, os, stat
from pathlib import Path

def moveToDesktop(src: Path) -> None:
    username = getpass.getuser()
    shutil.move(src, f"/home/{username}/Desktop/{src.name}")

BASH_SCRIPT: str = "#!/bin/bash\necho \"RUNNING NOVA FCT VPN\"\nsudo snx-rs -s vpn.fct.unl.pt -u CLIP_USERNAME -o vpn_Username_Password -X true -T tcpt"
BASH_FILE: str = "vpn.sh"
BASH_PATH = Path(BASH_FILE).resolve()

SHORTCUT_SCRIPT: str = "[Desktop Entry]\nType=Application\nName=VPN\nExec=PATH\nTerminal=true"
SHORTCUT_FILE: str = "VPN.desktop"
SHORTCUT_PATH = Path(SHORTCUT_FILE).resolve()

username = input("What is your clip username?\n")

with open(BASH_FILE, "w", encoding="utf-8") as file: # opens file, if it doesnt exist creates it and wipes it clean (w mode)
    file.write(BASH_SCRIPT.replace("CLIP_USERNAME", username, 1))

with open(SHORTCUT_FILE, "w", encoding="utf-8") as file:
    file.write(SHORTCUT_SCRIPT.replace("PATH", str(BASH_PATH), 1))

os.chmod(BASH_PATH, os.stat(BASH_PATH).st_mode | stat.S_IEXEC) # make vpn.sh executable

os.chmod(SHORTCUT_PATH, os.stat(SHORTCUT_PATH).st_mode | stat.S_IEXEC) # make the shorcut executable

moveToDesktop(SHORTCUT_PATH)