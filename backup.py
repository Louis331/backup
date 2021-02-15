import datetime
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import getpass
import os
import shutil
import time

PATH = os.path.join('C:/Users/{}/AppData/LocalLow/IronGate/Valheim/worlds'.format(getpass.getuser()))
TMP_PATH = os.path.join(os.getcwd(), 'tmp')
running = True
TIME = 600 #In seconds

file_list = []

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

while True:
    now = datetime.datetime.now().strftime("%m-%d-%Y %H %M %S")
    backup_path = os.path.join(TMP_PATH, now)

    shutil.make_archive(backup_path, 'zip', PATH)

    print('\nCreated zipfile')
    
    backup_path += '.zip'

    zipfile = drive.CreateFile({'title': now + '.zip'})
    zipfile.SetContentFile(backup_path)
    zipfile.Upload()
    print('File uploaded')
    zipfile.content.close()

    os.remove(backup_path)
    print('Local zip deleted file deleted')

    file_list.append(zipfile)

    if len(file_list) > 6:
        zipfile = file_list.pop(0)
        zipfile.Delete()
        print('Removed file from drive that\'s {} seconds old'.format(TIME * 7))

    print('Waiting \n')
    time.sleep(TIME)