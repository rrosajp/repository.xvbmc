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
import urllib
from salts_lib import dom_parser
from salts_lib import kodi
from salts_lib import log_utils
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import QUALITIES
from salts_lib.constants import VIDEO_TYPES
import scraper

BASE_URL = 'http://yshow.me'
XHR = {'X-Requested-With': 'XMLHttpRequest'}

class YShows_Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.TVSHOW, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'yshows'

    def resolve_link(self, link):
        link_url = urlparse.urljoin(self.base_url, link)
        html = self._http_get(link_url, cache_limit=.25)
        match = re.search('<iframe[^>]+src="([^"]+)', html, re.I)
        if match:
            return match.group(1)

    def format_source_label(self, item):
        label = '[%s] %s' % (item['quality'], item['host'])
        return label

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            page_url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(page_url, cache_limit=.25)
            for td in dom_parser.parse_dom(html, 'td', {'class': '[^"]*text-xs-left[^"]*'}):
                link = dom_parser.parse_dom(td, 'a', ret='href')
                host = dom_parser.parse_dom(td, 'img', ret='alt')
                if link and host:
                    host = host[0]
                    link = link[0]
                    quality = scraper_utils.get_quality(video, host, QUALITIES.HIGH)
                    hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': link, 'direct': False}
                    hosters.append(hoster)
        return hosters

    def _get_episode_url(self, show_url, video):
        episode_pattern = 'href="([^"]+-[sS]%s[Ee]%s[^"]+)' % (video.season, video.episode)
        title_pattern = 'href="(?P<url>[^"]+[Ss]\d+-?[Ee]\d+[^"]+).*?Episode\s+\d+\s*:\s*(?P<title>[^<]+)'
        return self._default_get_episode_url(show_url, video, episode_pattern, title_pattern)

    def search(self, video_type, title, year, season=''):
        results = []
        search_url = urlparse.urljoin(self.base_url, '/search?q=%s')
        search_url = search_url % (urllib.quote_plus(title))
        html = self._http_get(search_url, cache_limit=8)
        fragment = dom_parser.parse_dom(html, 'div', {'class': 'col-md-9'})
        if fragment:
            for match in re.finditer('href="([^"]+)[^>]+>([^<]+)', fragment[0]):
                url, match_title = match.groups()
                result = {'url': scraper_utils.pathify_url(url), 'title': scraper_utils.cleanse_title(match_title), 'year': ''}
                results.append(result)
        return results
