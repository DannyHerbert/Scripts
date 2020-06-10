from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

SEARCH = "Nicola Van Dyke"
PATH = os.path.normpath(r"G:\My Drive\VOICE OVER\Sessions\Nicola Van Dyke\Session 20052020")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def main():

    #List out all files
    fileList = drive.ListFile({'q': "'1-EczUSGU3lpjaSYhaoTj9Q3yfETJ0NXx' in parents and trashed=false"}).GetList()
    print('Files Found: {}'.format(len(fileList)))
    clientID = 0
    for file in fileList:
        print('Title: {}, ID: {}'.format(file['title'], file['id']))
        if file['title'] == SEARCH:
            clientID = file['id']

    getfileidfrompath(PATH)


def getfileidfrompath(filePath):
    pathList = filePath.split(os.sep)
    pathList.pop(0)
    pathList.pop(0)
    print(pathList)

    fileID = 'root'
    for dirName in pathList:
        fileList = drive.ListFile({'q': "'{}' in parents and trashed=false".format(fileID)}).GetList()
        for file in fileList:
            if file['title'] == dirName:
                fileID = file['id']

    print(fileID)


main()


