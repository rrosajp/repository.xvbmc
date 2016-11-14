# -*- coding: utf-8 -*-
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
import urlparse
import kodi
import log_utils
import dom_parser
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
from salts_lib.constants import QUALITIES
from salts_lib.constants import XHR
import scraper

BASE_URL = 'http://www.maksidizi.com'
PHP_URL = '/sw-islem.php?Islem=get_v&url=%s'
ALLOWED_LABELS = {u'maks': True, u'julie': True, u'play': True, u'odnok': True, u'altyazısız': False}

class Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.TVSHOW, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'MaksiDizi'

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        sources = {}
        if source_url and source_url != FORCE_NO_MATCH:
            page_url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(page_url, cache_limit=.5)
            fragment = dom_parser.parse_dom(html, 'div', {'class': 'videos'})
            if fragment:
                for match in re.finditer('href="([^"]+)[^>]*>([^<]+)', fragment[0]):
                    page_url, page_label = match.groups()
                    page_label = page_label.lower()
                    if page_label not in ALLOWED_LABELS: continue
                    sources = self.__get_sources(page_url, ALLOWED_LABELS[page_label])
                    for source in sources:
                        host = self._get_direct_hostname(source)
                        if host == 'gvideo':
                            quality = scraper_utils.gv_get_quality(source)
                            direct = True
                            stream_url = source + '|User-Agent=%s' % (scraper_utils.get_ua())
                        elif sources[source]['direct']:
                            quality = sources[source]['quality']
                            direct = True
                            stream_url = source + '|User-Agent=%s' % (scraper_utils.get_ua())
                        else:
                            quality = sources[source]['quality']
                            direct = False
                            host = urlparse.urlparse(source).hostname
                            stream_url = source
                        
                        hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': stream_url, 'direct': direct}
                        if sources[source]['subs']: hoster['subs'] = 'Turkish Subtitles'
                        hosters.append(hoster)
                
        return hosters

    def __get_sources(self, page_url, subs):
        sources = {}
        php_url = urlparse.urljoin(self.base_url, PHP_URL)
        params = {'Islem': 'get_v', 'url': page_url + '?p=1'}
        headers = {'Referer': page_url}
        headers.update(XHR)
        html = self._http_get(php_url, params=params, headers=headers, cache_limit=.5)
        stream_url = dom_parser.parse_dom(html, 'source', ret='src')
        direct = True
        if not stream_url:
            stream_url = dom_parser.parse_dom(html, 'iframe', ret='src')
            direct = False
            
        if stream_url:
            stream_url = stream_url[0]
            if self._get_direct_hostname(stream_url) == 'gvideo':
                direct = True
            
            if stream_url.startswith('//'):
                stream_url = 'http:' + stream_url
            sources[stream_url] = {'direct': direct, 'subs': subs, 'quality': QUALITIES.HD720}
            
        return sources
    
    def _get_episode_url(self, show_url, video):
        episode_pattern = 'href="([^"]+-%s-sezon-%s-bolum[^"]*)"' % (video.season, video.episode)
        return self._default_get_episode_url(show_url, video, episode_pattern)

    def search(self, video_type, title, year, season=''):
        results = []
        html = self._http_get(self.base_url, cache_limit=48)
        norm_title = scraper_utils.normalize_title(title)
        for show_list in dom_parser.parse_dom(html, 'ul', {'class': 'list'}):
            for item in dom_parser.parse_dom(show_list, 'li'):
                match = re.search('href="([^"]+)[^>]+>([^<]+)', item)
                if match:
                    match_url, match_title = match.groups()
                    match_year = ''
                    if norm_title in scraper_utils.normalize_title(match_title):
                        result = {'url': scraper_utils.pathify_url(match_url), 'title': scraper_utils.cleanse_title(match_title), 'year': match_year}
                        results.append(result)

        return results
