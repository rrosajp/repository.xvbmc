import datetime
import os
import re
import time

from salts_lib import kodi
from salts_lib import log_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES

__all__ = ['scraper', 'local_scraper', 'yifystreaming_scraper', 'torbase_scraper', 'pubfilm_scraper', 'hdmovie14_scraper', '123movies_scraper', 'xmovies8v2_scraper', 
'xmovies8_scraper', 'nitertv_scraper', 'movietv_scraper', '9movies_scraper', 'watchhd_scraper', 'pw_scraper', 'clickplay_scraper', 'firemovies_scraper', 'dizigold_scraper', 'moviesub_scraper', 'dayt_scraper', 'tvwtvs_scraper', 'movietv_scraper', 'mwm_scraper', 'dizilab_scraper', 'dizimag_scraper', 'sezonlukdizi_scraper', 'diziay_scraper', 'dizipas_scraper', 'farda_scraper', 'santaseries_scraper']

from . import *
    
class ScraperVideo:
    def __init__(self, video_type, title, year, trakt_id, season='', episode='', ep_title='', ep_airdate=''):
        assert(video_type in (VIDEO_TYPES.__dict__[k] for k in VIDEO_TYPES.__dict__ if not k.startswith('__')))
        self.video_type = video_type
        if isinstance(title, unicode): self.title = title.encode('utf-8')
        else: self.title = title
        self.year = str(year)
        self.season = season
        self.episode = episode
        if isinstance(ep_title, unicode): self.ep_title = ep_title.encode('utf-8')
        else: self.ep_title = ep_title
        self.trakt_id = trakt_id
        self.ep_airdate = None
        if ep_airdate:
            try: self.ep_airdate = datetime.datetime.strptime(ep_airdate, "%Y-%m-%d").date()
            except (TypeError, ImportError): self.ep_airdate = datetime.date(*(time.strptime(ep_airdate, '%Y-%m-%d')[0:3]))

    def __str__(self):
        return '|%s|%s|%s|%s|%s|%s|%s|' % (self.video_type, self.title, self.year, self.season, self.episode, self.ep_title, self.ep_airdate)

def update_xml(xml, new_settings, cat_count):
    new_settings.insert(0, '<category label="Scrapers %s">' % (cat_count))
    new_settings.append('    </category>')
    new_settings = '\n'.join(new_settings)
    match = re.search('(<category label="Scrapers %s">.*?</category>)' % (cat_count), xml, re.DOTALL | re.I)
    if match:
        old_settings = match.group(1)
        if old_settings != new_settings:
            xml = xml.replace(old_settings, new_settings)
    else:
        log_utils.log('Unable to match category: %s' % (cat_count), log_utils.LOGWARNING)
    return xml

def update_settings():
    full_path = os.path.join(kodi.get_path(), 'resources', 'settings.xml')
    
    try:
        # open for append; skip update if it fails
        with open(full_path, 'a') as f:
            pass
    except Exception as e:
        log_utils.log('Dynamic settings update skipped: %s' % (e), log_utils.LOGWARNING)
    else:
        with open(full_path, 'r') as f:
            xml = f.read()

        new_settings = []
        cat_count = 1
        old_xml = xml
        classes = scraper.Scraper.__class__.__subclasses__(scraper.Scraper)  # @UndefinedVariable
        for cls in sorted(classes, key=lambda x: x.get_name().upper()):
            if cls.has_proxy(): continue
            new_settings += cls.get_settings()
            if len(new_settings) > 90:
                xml = update_xml(xml, new_settings, cat_count)
                new_settings = []
                cat_count += 1
    
        if new_settings:
            xml = update_xml(xml, new_settings, cat_count)
    
        if xml != old_xml:
            with open(full_path, 'w') as f:
                f.write(xml)
        else:
            log_utils.log('No Settings Update Needed', log_utils.LOGDEBUG)

update_settings()
