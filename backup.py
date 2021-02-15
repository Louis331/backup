import datetime
import getpass
import os
import shutil
import time

PATH = os.path.join('C:/Users/{}/AppData/LocalLow/IronGate/Valheim/worlds'.format(getpass.getuser()))
running = True

while running:
    now = datetime.datetime.now().strftime("%m-%d-%Y %H %M %S")
    backup_path = os.path.join(os.getcwd(), 'tmp', now)

    shutil.make_archive(backup_path, 'zip', PATH)
    # os.remove(backup_path + '.zip')

    time.sleep(600)
