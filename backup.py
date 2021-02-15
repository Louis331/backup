import datetime
import getpass
import os
import shutil

PATH = os.path.join('C:/Users/{}/AppData/LocalLow/IronGate/Valheim/worlds'.format(getpass.getuser()))

now = datetime.datetime.now().strftime("%m-%d-%Y %H %M %S")
shutil.make_archive('tmp/backup ' + now, 'zip', PATH)