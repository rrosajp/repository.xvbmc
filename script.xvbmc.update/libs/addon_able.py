from sqlite3 import dbapi2 as db_lib

import os
import xbmc
import xbmcaddon
#from libs import kodi
from libs import common as Common

addon_id = Common.addon_id
db_dir = xbmc.translatePath("special://profile/Database")

db_path = os.path.join(db_dir, 'Addons27.db')

conn = db_lib.connect(db_path)
conn.text_factory = str

ADDON = xbmcaddon.Addon(id=Common.addon_id)


def set_enabled(newaddon, data=None):
    if Common.get_kversion() > 16.5:
        Common.log("Enabling " + newaddon)
        setit = 1
        if data is None: data = ''
        sql = 'REPLACE INTO installed (addonID,enabled) VALUES(?,?)'

        conn.execute(sql, (newaddon, setit,))
        conn.commit()
    else:
        pass


def setall_enable():
    if Common.get_kversion() > 16.5:
        addonfolder = xbmc.translatePath(os.path.join('special://home', 'addons'))
        contents = os.listdir(addonfolder)
        Common.log(contents)
        conn.executemany('update installed set enabled=1 WHERE addonID = (?)', ((val,) for val in contents))
        conn.commit()

    else:
        pass
