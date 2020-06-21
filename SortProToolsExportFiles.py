import re
import Helpers
import os


def main():
    CurrentDir = Helpers.askFileDirectory()

    for root, dirs, files in os.walk(CurrentDir):
        for currentfile in files:
            print(currentfile)
            reg = re.search(r"(^[^\.]+)([\._])(.+)(\.\w\w\w)", currentfile)
            name = reg.group(1)
            rubbish  = reg.group(3)
            filetype = reg.group(4)

            if not rubbish.upper().find('L'):
                name += ' L'
            if not rubbish.upper().find('R'):
                name += ' R'


            try:
                os.rename(os.path.join(CurrentDir, currentfile), os.path.join(CurrentDir, name))
            except FileExistsError:
                i = 2
                while True:
                    rename = name + str(i)
                    try:
                        os.rename(os.path.join(CurrentDir, currentfile), os.path.join(CurrentDir, rename))
                    except FileExistsError:
                        pass

            name+=filetype
            print(name)
            print(rubbish)
            print(filetype)

main()
