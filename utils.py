from pathlib import Path
import shutil, os, stat

def writeToFile(f: Path, text: str):
    with open(f, "w", encoding="utf-8") as file:
        file.write(text)

def makeExec(f: Path):
    os.chmod(f, os.stat(f).st_mode | stat.S_IEXEC)

def moveToDesktop(src: Path) -> None:
    shutil.move(src, Path.home() / "Desktop" / src.name)
