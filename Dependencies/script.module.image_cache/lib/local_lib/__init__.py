"""
    Image Cache Module
    Copyright (C) 2016 tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import zipfile
import xbmcvfs
import db_utils
import kodi

DB_NAME = 'tmdb_cache.db'
DB_FOLDER = kodi.translate_path(kodi.get_profile())
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)

def _update_db():
    db_ver = None
    if xbmcvfs.exists(DB_PATH):
        db_connection = db_utils.DBCache(DB_PATH)
        db_ver = db_connection.get_setting('db_version')
        db_connection.close()
    
    if db_ver != kodi.get_version():
        try:
            zip_path = os.path.join(kodi.translate_path(kodi.get_path()), 'tmdb_cache.zip')
            zip_file = zipfile.ZipFile(zip_path, 'r')
            zip_file.extract(DB_NAME, DB_FOLDER)
            db_connection = db_utils.DBCache(DB_PATH)
            db_connection.set_setting('db_version', kodi.get_version())
        finally:
            try: zip_file.close()
            except UnboundLocalError: pass
