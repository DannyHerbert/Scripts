#TODO: pass path on command line to skip pop up for directory
#TODO: allow setting compression settings

import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import py7zr

exclusionType = ("7ZIP", "ZIP")

rooot = tk.Tk()
rooot.withdraw()

CurrentDir = filedialog.askdirectory()

for root, dirs, files in os.walk(CurrentDir):
    for dir in dirs:
        path = os.path.join(CurrentDir, dir);
        print("Zipping: " + path);
        arc = py7zr.SevenZipFile(path + '.7z', 'w')
        arc.writeall(path);
        arc.close()
    break
