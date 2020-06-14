import gMail 
import gDrive
import sys

try:
    PATH = sys.argv[1]
except IndexError:
    raise Exception("You need to provide the path to the files to be sent, fanny")

def main():
    print('Authorising Google Drive...')
    drive = gDrive.authoriseGDrive()
    print('Authorising Google Mail...')
    mail = gMail.authoriseGmail()

    folderToShare = drive.CreateFile({'id' : gDrive.getFileIDFromPath(PATH, drive)})
    folderToShare.FetchMetadata()

    gDrive.enableSharing(folderToShare)
    link = gDrive.getShareableLink(folderToShare)

    gMail.createDraftEmail(mail, "danny", link)

main()


