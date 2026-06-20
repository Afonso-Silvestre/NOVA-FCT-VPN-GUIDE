from pathlib import Path
from utils import move_to_desktop, make_executable, write_to_file

BASH_PATH = Path("vpn.sh")
BASH_SCRIPT: str = "#!/bin/bash\necho \"RUNNING NOVA FCT VPN\"\nsudo snx-rs -s vpn.fct.unl.pt -u CLIP_USERNAME -o vpn_Username_Password -X true -T tcpt"

SHORTCUT_PATH = Path("VPN.desktop")
SHORTCUT_SCRIPT: str = "[Desktop Entry]\nType=Application\nName=VPN\nExec=PATH\nTerminal=true"

username = input("What is your CLIP username?\n")

write_to_file(BASH_PATH, BASH_SCRIPT.replace("CLIP_USERNAME", username, 1))
write_to_file(SHORTCUT_PATH, SHORTCUT_SCRIPT.replace("PATH", str(BASH_PATH.resolve()), 1))

make_executable(BASH_PATH)
make_executable(SHORTCUT_PATH)

move_to_desktop(SHORTCUT_PATH)