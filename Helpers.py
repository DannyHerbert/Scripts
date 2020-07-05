import tkinter as tk
from tkinter import filedialog
import os

def askFileDirectory():
    root = tk.Tk()
    root.withdraw()
    CurrentDir = filedialog.askdirectory()
    return CurrentDir

def createCheckBox(name):
    root = tk.Tk()
    root.withdraw()
    buttonOn = tk.IntVar()
    c = tk.Checkbutton(root,text = name, variable = buttonOn)
    c.pack()
    return buttonOn


def getFileExtension(filename):
    return os.path.splitext(filename)[1]
