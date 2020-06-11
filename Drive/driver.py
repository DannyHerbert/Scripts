from gDrive import *
from gMail import *

PATH = os.path.normpath(r"G:\My Drive\VOICE OVER\Sessions\Nicola Van Dyke\Session 20052020\Export")

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


