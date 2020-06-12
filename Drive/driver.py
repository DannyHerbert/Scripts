from gDrive import *
from gMail import *
import sys

try:
    PATH = sys.argv[1]
except IndexError:
    raise Exception("You need to provide the path to the files to be sent, fanny")

def main():
    print('Authorising Google Drive...')
    drive = authoriseGDrive()
    print('Authorising Google Mail...')
    mail = authoriseGmail()

    folderToShare = drive.CreateFile({'id' : getFileIDFromPath(PATH, drive)})
    folderToShare.FetchMetadata()

    enableSharing(folderToShare)
    link = getShareableLink(folderToShare)

    createDraftEmail(mail, "danny", link)

main()


