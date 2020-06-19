import os
import shutil
import datetime
import subprocess
import Helpers


filetypes = ('WAV', 'MP3')
FullReelFolder = "FullReel"
IndividualFilesFolder = "IndividualFiles"
initials = "??"

CurrentDir = Helpers.askFileDirectory()

for filetype in filetypes:
    os.makedirs(os.path.join(CurrentDir, filetype, FullReelFolder))
    os.makedirs(os.path.join(CurrentDir, filetype, IndividualFilesFolder))

for root, dirs, files in os.walk(CurrentDir):
    for file in files:
        if initials == "??":
            initials = " " + file.split()[0][:1] + file.split()[1][:1]

        fileextension = Helpers.getFileExtension(file)[1:].upper()
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

