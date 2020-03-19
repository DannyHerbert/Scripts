#TODO: pass path on command line to skip pop up for directory

import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import zipfile
from tqdm import tqdm

exclusionType = ("7ZIP", "ZIP")

rooot = tk.Tk()
rooot.withdraw()

CurrentDir = filedialog.askdirectory()

for root, dirs, files in os.walk(CurrentDir):
    for dir in dirs:
        path = os.path.join(CurrentDir, dir)

        print("Zipping: " + path)

        zipper = zipfile.ZipFile(path + ".zip", 'w', compression = zipfile.ZIP_LZMA)
        for subRoot, subDir, subFiles in os.walk(path):
            for subfile in tqdm(subFiles):
                zipper.write(os.path.join(path, subfile), subfile)
        zipper.close()
    break
