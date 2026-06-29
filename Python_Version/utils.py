"""
UTILS.PY

Author: Afonso Silvestre
Date: 20-06-2026
Description:
    This script simply has auxiliary functions used in setup.py
    It should not be ran individually nor changed.

"""

from pathlib import Path
import os, stat, subprocess

def write_to_file(f: Path, text: str) -> None:
    """
    Writes `text` to file `f`.
    """
    with open(f, "w", encoding="utf-8") as file:
        file.write(text)

def make_executable(f: Path) -> None:
    """
    Equivalent to doing `chmod +x` on your terminal.
    Here "+x" is done by individually setting executable permissions for
    User, Group, and Others individually onto the already set permissions
    for the file.
    """
    os.chmod(f, os.stat(f).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

def get_desktop_path() -> Path:
    return Path(subprocess.run(["xdg-user-dir", "DESKTOP"], capture_output=True, text=True, check=True).stdout.strip())
