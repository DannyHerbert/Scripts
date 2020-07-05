import re
import Helpers
import os
import tkinter as tk



def main():
    gui = Gui()
    
    print(gui.deleteUnsortableFiles.get())
    print(gui.keepLeftRight.get())
    print(gui.fileBrowser.currentDirectory)

    deleteUnsortableFiles = gui.deleteUnsortableFiles.get()
    keepLeftRight = gui.keepLeftRight.get()
    CurrentDir = gui.fileBrowser.currentDirectory


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
                if deleteUnsortableFiles:
                    print("Deleting File..")
                    print("")
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
            if rubbish is not None and keepLeftRight:
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
    # Bit hard to parse. Goes back to rename first file '1' if there are multiple of the same name
    # gives "file 1, file 2, file 3" rather than "file, file 2, file 3"
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

class Gui:
    root = None
    deleteUnsortableFiles = None
    keepLeftRight = None
    fileBrowser = None

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rename Pro Tools Files")
        self.root.geometry("300x150")


        self.deleteUnsortableFiles = tk.IntVar()
        self.keepLeftRight = tk.IntVar()
        self.currentDirectory = tk.StringVar()

        self.createCheckBox("Delete hidden/unused Files?", self.deleteUnsortableFiles)
        self.createCheckBox("Keep L and R?", self.keepLeftRight)
        self.fileBrowser = self.createFileBrowser()
        self.createButton("Done" , self.onExit)

        self.root.mainloop()
        self.root.withdraw()

    def createFileBrowser(self):
        fileBrowser = self.FileBrowser(self.root)
        return fileBrowser

    def createCheckBox(self, name, var):
        check = tk.Checkbutton(self.root, text = name, variable = var)
        check.pack()
        return check 

    def createButton(self, name, callback):
        button = tk.Button(self.root, text = name, command = callback)
        button.pack()

    def onExit(self):
        self.root.quit()

    class FileBrowser:
        frame = None
        labelText = None
        label = None
        button = None
        currentDirectory = "None"
        root = None

        def __init__(self, root):
            self.root = root
            self.labelText = tk.StringVar()
            self.labelText.set("None")
            self.frame = tk.LabelFrame(root, text = "Directory to Sort:")
            self.label  = tk.Label (self.frame, textvariable = self.labelText, bg = "white")
            self.label.config(width = 20)
            self.button = tk.Button(self.frame, text = "Browse", command = self.buttonCallback)
            self.label.grid(row = 0, column = 0)
            self.button.grid(row = 0, column = 1)
            self.frame.pack()

        def buttonCallback(self):
            self.currentDirectory = tk.filedialog.askdirectory()
            self.labelText.set(self.currentDirectory)


main()
