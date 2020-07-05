import re
import Helpers
import os



def main():
    CurrentDir = Helpers.askFileDirectory()
    
    deleteOtherFiles = Helpers.createCheckBox("Delete Other Files?")


    for root, dirs, files in os.walk(CurrentDir):
        for currentFile in files:
            print("File Name:  " + currentFile)

            # (first group of characters up that are not a -, _ , or . character. This is the actual name)
            # (and -, ., or _ character. Thrown away)
            # (any characters. this is all the 'dup2', '_01' nonsense)
            # (filetype)

            reg = re.search(r"(^[^.^\-^_?]+)([._-])?(.+)?(\.\w{3})", currentFile)

            # Name of file
            try:
                name = reg.group(1)
            except AttributeError:
                if deleteOtherFiles:
                    os.remove(os.path.join(root, currentFile))
                    continue
                else:
                    continue

            # Seperator (- , . etc)
            seperator = reg.group(2)

            # All the dup2 bits
            rubbish  = reg.group(3)

            # Filetype
            filetype = reg.group(4)

            if seperator is None:
                print("File name is already fine...")
                print("")
                continue

            suffix = ''
            if rubbish is not None:
                # find any l or r character thats not in a word of word a-z characters
                panning = re.search(r"(^|[^a-z^A-Z])([lLrR])([^a-z^A-Z]|$)", rubbish)
                if panning is not None:
                    suffix += " " + panning.group(2)

            name = os.path.split(renameFileAndIterateForDuplicates(os.path.join(root, currentFile),os.path.join(root, name + suffix + filetype)))[1]

            print("New Name:  " + name)
            print("Discared:  " + rubbish)
            print("File type: " + filetype)
            print(" ")

def renameFileAndIterateForDuplicates(currentPathName, newPathName):
    multiFileCheck = newPathName[:-4] + " 1" + newPathName[-4:]
    if(not os.path.isfile(newPathName) and not os.path.isfile(multiFileCheck)):
        os.rename(currentPathName, newPathName)
        return newPathName
    else:
        if(os.path.isfile(newPathName)):
            os.rename(newPathName, multiFileCheck)
        i = 2
        rename = newPathName[:-4] + " " + str(i) + newPathName[-4:]
        while os.path.isfile(rename):
            i += 1
            rename = newPathName[:-4] + " " + str(i) + newPathName[-4:]
        os.rename(currentPathName, rename)
        return rename
main()
