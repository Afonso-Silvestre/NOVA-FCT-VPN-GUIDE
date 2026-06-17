import shutil, os, stat
from pathlib import Path


def moveToDesktop(src: Path) -> None:
    shutil.move(src, Path.home() / "Desktop" / src.name)

BASH_PATH = Path("vpn.sh")
BASH_SCRIPT: str = "#!/bin/bash\necho \"RUNNING NOVA FCT VPN\"\nsudo snx-rs -s vpn.fct.unl.pt -u CLIP_USERNAME -o vpn_Username_Password -X true -T tcpt"

SHORTCUT_PATH = Path("VPN.desktop")
SHORTCUT_SCRIPT: str = "[Desktop Entry]\nType=Application\nName=VPN\nExec=PATH\nTerminal=true"

username = input("What is your CLIP username?\n")

with open(BASH_PATH, "w", encoding="utf-8") as file:
    file.write(BASH_SCRIPT.replace("CLIP_USERNAME", username, 1))

with open(SHORTCUT_PATH, "w", encoding="utf-8") as file:
    file.write(SHORTCUT_SCRIPT.replace("PATH", str(BASH_PATH), 1))

os.chmod(BASH_PATH, os.stat(BASH_PATH).st_mode | stat.S_IEXEC)

os.chmod(SHORTCUT_PATH, os.stat(SHORTCUT_PATH).st_mode | stat.S_IEXEC)

moveToDesktop(SHORTCUT_PATH)