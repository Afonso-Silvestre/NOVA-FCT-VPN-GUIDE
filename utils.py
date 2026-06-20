from pathlib import Path
import shutil, os, stat

def write_to_file(f: Path, text: str):
    with open(f, "w", encoding="utf-8") as file:
        file.write(text)

def make_executable(f: Path):
    os.chmod(f, os.stat(f).st_mode | stat.S_IEXEC)

def move_to_desktop(src: Path) -> None:
    shutil.move(src, Path.home() / "Desktop" / src.name)
