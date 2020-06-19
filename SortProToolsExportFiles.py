
import Helpers
import os


def main():
    CurrentDir = Helpers.askFileDirectory()

    for root, dirs, files in os.walk(CurrentDir):
        for file in files:
            #rename sort

