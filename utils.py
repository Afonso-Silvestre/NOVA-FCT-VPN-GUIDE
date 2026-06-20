from pathlib import Path
import shutil, os, stat, subprocess

def write_to_file(f: Path, text: str) -> None:
    """
    Writes `text` to the file `f`.
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

def move_to_desktop(src: Path) -> None:
    """
    Moves `src` to the Desktop folder.
    """
    desktop = Path(subprocess.run(["xdg-user-dir", "DESKTOP"], capture_output=True, text=True, check=True).stdout.strip())

    shutil.move(src, desktop / src.name)
