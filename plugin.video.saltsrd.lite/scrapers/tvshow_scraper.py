"""
    SALTS XBMC Addon
    Copyright (C) 2014 tknorris

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
import re
import urllib
import urlparse
import kodi
import datetime
import log_utils
import dom_parser
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
from salts_lib.constants import XHR
from salts_lib.constants import QUALITIES
from salts_lib.constants import Q_ORDER
from salts_lib.utils2 import i18n
import scraper


BASE_URL = 'http://www.tvshow.me'

class Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'TVShow.me'

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(url, require_debrid=True, cache_limit=.5)
            title = dom_parser.parse_dom(html, 'title')
            if title:
                title = re.sub('^\[ST\]\s*&#8211;\s*', '', title[0])
                meta = scraper_utils.parse_episode_link(title)
                page_quality = scraper_utils.height_get_quality(meta['height'])
            else:
                page_quality = QUALITIES.HIGH
                
            fragment = dom_parser.parse_dom(html, 'section', {'class': '[^"]*entry-content[^"]*'})
            if fragment:
                for section in dom_parser.parse_dom(fragment[0], 'p'):
                    match = re.search('([^<]*)', section)
                    meta = scraper_utils.parse_episode_link(match.group(1))
                    if meta['episode'] != '-1' or meta['airdate']:
                        section_quality = scraper_utils.height_get_quality(meta['height'])
                    else:
                        section_quality = page_quality
                        
                    if Q_ORDER[section_quality] < Q_ORDER[page_quality]:
                        quality = section_quality
                    else:
                        quality = page_quality
                        
                    for stream_url in dom_parser.parse_dom(section, 'a', ret='href'):
                        host = urlparse.urlparse(stream_url).hostname
                        hoster = {'multi-part': False, 'host': host, 'class': self, 'views': None, 'url': stream_url, 'rating': None, 'quality': quality, 'direct': False}
                        hosters.append(hoster)
        return hosters

    def get_url(self, video):
        return self._blog_get_url(video, delim=' ')

    @classmethod
    def get_settings(cls):
        settings = super(cls, cls).get_settings()
        settings = scraper_utils.disable_sub_check(settings)
        name = cls.get_name()
        settings.append('         <setting id="%s-filter" type="slider" range="0,180" option="int" label="     %s" default="60" visible="eq(-4,true)"/>' % (name, i18n('filter_results_days')))
        settings.append('         <setting id="%s-select" type="enum" label="     %s" lvalues="30636|30637" default="0" visible="eq(-5,true)"/>' % (name, i18n('auto_select')))
        settings.append('         <setting id="%s-include_comments" type="bool" label="     %s" default="false" visible="eq(-6,true)"/>' % (name, i18n('include_comments')))
        return settings

    def search(self, video_type, title, year, season=''):
        results = []
        search_url = urlparse.urljoin(self.base_url, '/wp-admin/admin-ajax.php')
        data = {'action': 'ajaxy_sf', 'search': 'false', 'show_category': 0, 'show_post_category': 0, 'post_types': '', 'sf_value': title}
        referer = urlparse.urljoin(self.base_url, '/?s=%s' % (urllib.quote_plus(title)))
        headers = {'Referer': referer}
        headers.update(XHR)
        html = self._http_get(search_url, data=data, headers=headers, require_debrid=True, cache_limit=1)
        js_data = scraper_utils.parse_json(html, search_url)
        try: posts = js_data['post'][0]['all']
        except: posts = []
        for post in posts:
            if self.__too_old(post): continue
            post_title = re.sub('^\[ST\]\s*&#8211;\s*', '', post.get('post_title', ''))
            result = self._blog_proc_results(post_title, '(?P<post_title>.+)(?P<url>.*?)', '', video_type, title, year)
            if result:
                result[0]['url'] = scraper_utils.pathify_url(post['post_link'])
                results.append(result[0])
        return results
    
    def __too_old(self, post):
        filter_days = datetime.timedelta(days=int(kodi.get_setting('%s-filter' % (self.get_name()))))
        match = re.search('(/\d{4}/\d{2}/\d{2}/)', post['post_link'])
        if match:
            post_date = match.group(1)
            date_format = '/%Y/%m/%d/'
        else:
            post_date = post['post_date_formatted']
            date_format = '%B %d, %Y'
            
        if filter_days and post_date:
            try:
                today = datetime.date.today()
                post_date = scraper_utils.to_datetime(post_date, date_format).date()
                if today - post_date > filter_days:
                    return True
            except ValueError:
                return False
        return False
