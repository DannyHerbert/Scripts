
import os
import tkinter
from tkinter import filedialog
import zipfile
import sys
from tqdm import tqdm

rooot = tkinter.Tk()
rooot.withdraw()

CurrentDir = ''
if (len(sys.argv) <= 1):
    CurrentDir = filedialog.askdirectory()
else:
    CurrentDir = sys.argv[1];
    CurrentDir = CurrentDir.replace(os.sep, '/')
    CurrentDir = CurrentDir[:-1]


print(CurrentDir)
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
