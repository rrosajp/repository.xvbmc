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

from salts_lib import dom_parser
from salts_lib import kodi
from salts_lib import scraper_utils
from salts_lib import log_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
import scraper

XHR = {'X-Requested-With': 'XMLHttpRequest'}
BASE_URL = 'http://vidnow4k.com'

class VidNow4K_Scraper(scraper.Scraper):
    base_url = BASE_URL
    
    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.MOVIE, VIDEO_TYPES.TVSHOW, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'VidNow4K'

    def resolve_link(self, link):
        return link

    def format_source_label(self, item):
        return '[%s] %s' % (item['quality'], item['host'])

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            page_url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(page_url, cache_limit=.5)
            fragment = dom_parser.parse_dom(html, 'table', {'class': '[^"]*links-table[^"]*'})
            if fragment:
                for row in dom_parser.parse_dom(fragment[0], 'tr'):
                    match = re.search("bind\(.*?'([^']+).*?<td>(.*?)</td>", row, re.DOTALL)
                    if match:
                        stream_url, q_str = match.groups()
                        if self._get_direct_hostname(stream_url) == 'gvideo':
                            sources = self._parse_google(stream_url)
                        else:
                            sources = [stream_url]
                        
                        for source in sources:
                            host = self._get_direct_hostname(source)
                            if host == 'gvideo':
                                quality = scraper_utils.gv_get_quality(source)
                                direct = True
                            else:
                                host = urlparse.urlparse(source).hostname
                                quality = scraper_utils.blog_get_quality(video, q_str, host)
                                direct = False
                            hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': source, 'direct': direct}
                            hosters.append(hoster)
            
        return hosters

    def _get_episode_url(self, show_url, video):
        show_url = urlparse.urljoin(self.base_url, show_url)
        html = self._http_get(show_url, cache_limit=8)
        fragment = dom_parser.parse_dom(html, 'div', {'class': '[^"]*seasons[^"]*'})
        if fragment:
            match = re.search('href="([^"]+)[^>]*>%s<' % (video.season), html)
            if match:
                season_url = scraper_utils.pathify_url(match.group(1))
                episode_pattern = 'href="([^"]*/seasons/%s/episodes/%s(?!\d)[^"]*)' % (video.season, video.episode)
                title_pattern = 'href="(?P<url>[^"]+)[^>]*>Episode\s+\d+\s+-\s+(<?P<title>[^<]+)'
                return self._default_get_episode_url(season_url, video, episode_pattern, title_pattern)

    def search(self, video_type, title, year, season=''):
        results = []
        search_url = urlparse.urljoin(self.base_url, '/titles/paginate')
        if video_type == VIDEO_TYPES.TVSHOW:
            media_type = 'series'
            url_type = 'series'
            landing_url = urlparse.urljoin(self.base_url, '/series')
        else:
            media_type = 'movie'
            url_type = 'movies'
            landing_url = urlparse.urljoin(self.base_url, '/movies')
            
        token = self.__get_token()
        if token:
            params = {'_token': token, 'perPage': 18, 'page': 1, 'order': 'release_dateDesc', 'query': title, 'type': media_type, 'minRating': '', 'maxRating': ''}
            search_url = search_url + '?' + urllib.urlencode(params)
            headers = XHR
            headers['Referer'] = landing_url
            html = self._http_get(search_url, headers=headers, cache_limit=0)
            js_data = scraper_utils.parse_json(html, search_url)
            if 'items' in js_data:
                for item in js_data['items']:
                    match_year = item.get('year', '')
                    if 'type' in item and 'title' in item and 'id' in item:
                        slug = re.sub('\s+', '-', item['title'].lower())
                        match_url = '/%s/%s-%s' % (url_type, item['id'], slug)
                        if not year or not match_year or year == match_year:
                            result = {'title': scraper_utils.cleanse_title(item['title']), 'year': match_year, 'url': scraper_utils.pathify_url(match_url)}
                            results.append(result)
        return results

    def __get_token(self):
        html = self._http_get(self.base_url, cache_limit=48)
        match = re.search("\s*token\s*:\s*'([^']+)", html)
        if match:
            return match.group(1)
        
        