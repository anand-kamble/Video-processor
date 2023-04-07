import subprocess
import os
import platform
from Constants import LOG_FILE_NAME


def OpenFile(filepath: str):
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def openLogs():
    OpenFile(os.getcwd()+"/"+LOG_FILE_NAME)
    return None
