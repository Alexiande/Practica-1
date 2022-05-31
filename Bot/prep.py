import os
import sys
import glob
import shutil

import src.cfgs.sysconfig as scfg
from src.database import *

if __name__ == '__main__':
    app_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Папка, откуда запускаемся
    data_path = os.path.join(app_path, scfg.DATA_DIR[:-1])
    os.makedirs(data_path, exist_ok=True)
    open(scfg.DATA_DIR + scfg.DATABASE_FILENAME, 'w').close()
    open(scfg.DATA_DIR + scfg.LOG_FILENAME, 'w').close()
    db = Database()
    db.create_table(scfg.TABLE_NAME, [['user_id', 'INTEGER'], ['group_slug', 'VARCHAR(30)']])
    del db