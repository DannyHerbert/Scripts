import tkinter as tk
from tkinter import filedialog
import os

def askFileDirectory
    rooot = tk.Tk()
    rooot.withdraw()
    CurrentDir = filedialog.askdirectory()
    return CurrentDir

def getFileExtension(filename):
    return os.path.splitext(filename)[1]
