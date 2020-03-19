import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog
import subprocess


rooot = tk.Tk()
rooot.withdraw()

CurrentDir = filedialog.askdirectory()

filetypes = ('WAV', 'MP3')
FullReelFolder = "FullReel"
IndividualFilesFolder = "IndividualFiles"
initials = "??"

for filetype in filetypes:
    os.makedirs(os.path.join(CurrentDir, filetype, FullReelFolder))
    os.makedirs(os.path.join(CurrentDir, filetype, IndividualFilesFolder))

def getExtension(filename):
    return os.path.splitext(filename)[1]

for root, dirs, files in os.walk(CurrentDir):
    for file in files:
        if initials == "??":
            initials = " " + file.split()[0][:1] + file.split()[1][:1]

        fileextension = getExtension(file)[1:].upper()
        if (fileextension not in filetypes): continue

        fileFolder = IndividualFilesFolder if "Reel" not in file else FullReelFolder

        source = os.path.join(root, file)
        destination = os.path.join(root, fileextension, fileFolder)

        shutil.copy(source, destination)
        os.remove(source)
    break

dateFormated = datetime.datetime.now().strftime(" %d%m%Y")
os.rename(CurrentDir, CurrentDir + initials + dateFormated )
CurrentDir = CurrentDir + initials + dateFormated

path = os.path.realpath(CurrentDir)
os.startfile(path)

