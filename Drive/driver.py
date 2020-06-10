from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


def main():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    SEARCH = "Nicola Van Dyke"

    #List out all files
    fileList = drive.ListFile({'q': "'1-EczUSGU3lpjaSYhaoTj9Q3yfETJ0NXx' in parents and trashed=false"}).GetList()
    print('Files Found: {}'.format(len(fileList)))
    clientID = 0
    for file in fileList:
        print('Title: {}, ID: {}'.format(file['title'], file['id']))
        if file['title'] == SEARCH:
            clientID = file['id']

    getfileidfrompath(os.getcwd())


def getfileidfrompath(filepath):
    path = os.path.normpath(filepath)
    path.split(os.sep)
    print (path)


main()


