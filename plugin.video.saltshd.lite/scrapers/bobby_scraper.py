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
import log_utils
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
from salts_lib.constants import QUALITIES
import scraper

BASE_URL = 'https://bobby.kohimovie.com'
API_BASE = '/jp/2.1.0'
SEARCH_URL = API_BASE + '/search?q=%s&page=1'
SERVER_URL = API_BASE + '/getServer?serialAlias=%s&osType=iOS'
SOURCE_URL = API_BASE + '/getMovieBySource?serialAlias=%s&source=%s&osType=iOS'
HEADERS = {'User-Agent': 'BobbyMovie/1 (iPhone; iOS 9.3.2; Scale/2.00)'}

class Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.MOVIE, VIDEO_TYPES.SEASON, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'Bobby'

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            query = urlparse.parse_qs(urlparse.urlparse(source_url).query)
            if 'alias' in query:
                alias = query['alias'][0]
                server_url = SERVER_URL % (alias)
                url = urlparse.urljoin(self.base_url, server_url)
                html = self._http_get(url, headers=HEADERS, cache_limit=2)
                js_data = scraper_utils.parse_json(html, url)
                for item in js_data.get('data', []):
                    server_name = item.get('serverName', '')
                    if server_name:
                        source_url = SOURCE_URL % (alias, server_name)
                        url = urlparse.urljoin(self.base_url, source_url)
                        html = self._http_get(url, headers=HEADERS, cache_limit=2)
                        source_data = scraper_utils.parse_json(html, url)
                        for item2 in source_data.get('data', []):
                            if video.video_type == VIDEO_TYPES.EPISODE and int(video.episode) != item2['episode']: continue
                            stream_url = item2.get('streaming', '')
                            if stream_url:
                                host = self._get_direct_hostname(stream_url)
                                if host == 'gvideo':
                                    direct = True
                                    quality = scraper_utils.gv_get_quality(stream_url)
                                    stream_url += '|User-Agent=%s' % (scraper_utils.get_ua())
                                else:
                                    if stream_url.startswith('http://webapp'):
                                        stream_url = stream_url.split('embed=')[-1]
                                    direct = False
                                    host = urlparse.urlparse(stream_url).hostname
                                    quality = scraper_utils.get_quality(video, host, QUALITIES.HIGH)
                                    
                                hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': stream_url, 'direct': direct}
                                hosters.append(hoster)

        return hosters

    def _get_episode_url(self, season_url, video):
        return season_url
    
    def search(self, video_type, title, year, season=''):
        results = []
        search_url = urlparse.urljoin(self.base_url, SEARCH_URL)
        search_url = search_url % (urllib.quote(title))
        html = self._http_get(search_url, headers=HEADERS, cache_limit=24)
        js_data = scraper_utils.parse_json(html, search_url)
        norm_title = scraper_utils.normalize_title(title)
        for item in js_data.get('data', []):
            is_show = item.get('tvshow', False)
            is_season = re.search('Season\s+(\d+)', item['name'], re.I)
            if (video_type == VIDEO_TYPES.MOVIE and not is_show) or (video_type == VIDEO_TYPES.SEASON and is_show):
                if video_type == VIDEO_TYPES.SEASON:
                    if norm_title not in scraper_utils.normalize_title(item['name']): continue
                    if season and is_season and int(season) != int(is_season.group(1)): continue
                        
                match_url = '/?alias=%s' % (item['alias'])
                result = {'title': scraper_utils.cleanse_title(item['name']), 'year': '', 'url': scraper_utils.pathify_url(match_url), 'is_season': is_season}
                results.append(result)

        if video_type == VIDEO_TYPES.SEASON:
            results.sort(key=lambda x: x['is_season'], reverse=True)
            
        return results
