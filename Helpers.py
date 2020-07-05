import tkinter as tk
from tkinter import filedialog
import os


def getFileExtension(filename):
    return os.path.splitext(filename)[1]
