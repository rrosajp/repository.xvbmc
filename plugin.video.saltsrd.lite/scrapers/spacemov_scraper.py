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
import scraper
import urlparse
import re
import urllib
import kodi
import log_utils
import dom_parser
from salts_lib import scraper_utils
from salts_lib.constants import VIDEO_TYPES
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import QUALITIES

BASE_URL = 'http://www.spacemov.net'
XHR = {'X-Requested-With': 'XMLHttpRequest'}

class Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.MOVIE])

    @classmethod
    def get_name(cls):
        return 'SpaceMov'

    def get_sources(self, video):
        source_url = self.get_url(video)
        sources = []
        if source_url and source_url != FORCE_NO_MATCH:
            page_url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(page_url, cache_limit=8)
            for fragment in dom_parser.parse_dom(html, 'div', {'class': 'video'}):
                for source in dom_parser.parse_dom(fragment, 'iframe', ret='src') + dom_parser.parse_dom(fragment, 'script', ret='src'):
                    if 'validateemb' in source: continue
                    host = urlparse.urlparse(source).hostname
                    source = {'multi-part': False, 'url': source, 'host': host, 'class': self, 'quality': QUALITIES.HD720, 'views': None, 'rating': None, 'direct': False}
                    sources.append(source)

        return sources

    def search(self, video_type, title, year, season=''):
        results = []
        search_url = urlparse.urljoin(self.base_url, '/wp-admin/admin-ajax.php')
        referer = self.base_url + '/?' + urllib.urlencode({'s': title, 'submit': 'Search'})
        headers = {'Referer': referer}
        headers.update(XHR)
        params = {'s': title, 'action': 'dwls_search'}
        html = self._http_get(search_url, params=params, headers=headers, cache_limit=8)
        js_data = scraper_utils.parse_json(html, search_url)
        for match in js_data.get('results', []):
            match_title_year = match.get('post_title')
            match_url = match.get('permalink')
            if match_url and match_title_year:
                match_title, match_year = scraper_utils.extra_year(match_title_year)
                if not year or not match_year or year == match_year:
                    result = {'title': scraper_utils.cleanse_title(match_title), 'year': match_year, 'url': scraper_utils.pathify_url(match_url)}
                    results.append(result)

        return results
