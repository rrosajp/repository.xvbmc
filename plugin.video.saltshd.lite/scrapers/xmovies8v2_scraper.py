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
import dom_parser
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
from salts_lib.constants import QUALITIES
from salts_lib.constants import Q_ORDER
from salts_lib.constants import XHR
import scraper

BASE_URL = 'http://xmovies8.tv'
PLAYER_URL = '/ajax/movie/load_player'
EPISODES_URL = '/ajax/movie/load_episodes'

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
        return 'xmovies8.v2'

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        sources = {}
        if source_url and source_url != FORCE_NO_MATCH:
            page_url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(page_url, cache_limit=.5)
            html = self.__get_players(html, page_url)
            players = list(set(re.findall("load_player\(\s*'([^']+)'\s*,\s*'?(\d+)\s*'?", html)))
            player_url = urlparse.urljoin(self.base_url, PLAYER_URL)
            for link_id, height in players:
                headers = {'Referer': page_url, 'Accept-Formating': 'application/json, text/javascript', 'Server': 'cloudflare-nginx'}
                headers.update(XHR)
                data = {'id': link_id, 'quality': height, 'from': 'v3'}
                html = self._http_get(player_url, data=data, headers=headers, cache_limit=.5)
                iframe_url = dom_parser.parse_dom(html, 'iframe', {'class': 'frame-player\d*'}, ret='src')
                if iframe_url:
                    iframe_url = iframe_url[0]
                    if 'player.php' in iframe_url:
                        iframe_url = urlparse.urljoin(self.base_url, iframe_url)
                        video_url = dom_parser.parse_dom(html, 'input', {'type': 'hidden'}, ret='value')
                        if video_url:
                            headers = {'Referer': page_url}
                            html = self._http_get(video_url[0], headers=headers, allow_redirect=False, method='HEAD', cache_limit=.25)
                            if html.startswith('http'):
                                if self._get_direct_hostname(html) == 'gvideo':
                                    quality = scraper_utils.gv_get_quality(html)
                                else:
                                    quality = scraper_utils.height_get_quality(height)
                                sources[html] = {'quality': quality, 'direct': True}
                                if not kodi.get_setting('scraper_url') and Q_ORDER[quality] >= Q_ORDER[QUALITIES.HD720]: break
                                
                    else:
                        sources[iframe_url] = {'quality': QUALITIES.HIGH, 'direct': False}
                    
            for source in sources:
                direct = sources[source]['direct']
                quality = sources[source]['quality']
                if direct:
                    host = self._get_direct_hostname(source)
                else:
                    host = urlparse.urlparse(source).hostname
                stream_url = source + '|User-Agent=%s' % (scraper_utils.get_ua())
                hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': stream_url, 'direct': direct}
                hosters.append(hoster)
            
        return hosters

    def __get_players(self, html, page_url):
        url = urlparse.urljoin(self.base_url, EPISODES_URL)
        match = re.search("data\s*:\s*{\s*id:\s*(\d+),\s*episode_id:\s*(\d+),\s*link_id:\s*(\d+),\s*from:\s*'([^']+)", html)
        if match:
            show_id, ep_id, link_id, from_id = match.groups()
            data = {'id': show_id, 'episode_id': ep_id, 'link_id': link_id, 'from': from_id}
            headers = {'Referer': page_url, 'Accept-Formating': 'application/json, text/javascript', 'Server': 'cloudflare-nginx'}
            headers.update(XHR)
            html = self._http_get(url, data=data, headers=headers, cache_limit=1)
        return html
    
    def _get_episode_url(self, season_url, video):
        episode_pattern = 'href="([^"]+)[^>]+class="[^"]*btn-episode[^>]*>%s<' % (video.episode)
        return self._default_get_episode_url(season_url, video, episode_pattern)

    def search(self, video_type, title, year, season=''):
        results = []
        search_url = urlparse.urljoin(self.base_url, '/movies/search?s=%s' % urllib.quote_plus(title))
        html = self._http_get(search_url, cache_limit=8)
        for item in dom_parser.parse_dom(html, 'div', {'class': '[^"]*c-content-product-2[^"]*'}):
            match_title_year = dom_parser.parse_dom(item, 'p', {'class': '[^"]*c-title[^"]*'})
            match_url = dom_parser.parse_dom(item, 'a', ret='href')
            is_season = dom_parser.parse_dom(item, 'div', {'class': '[^"]*c-bg-red[^'"]*"})
            if match_title_year and match_url:
                match_title_year = match_title_year[0]
                match_url = match_url[0]
                if (video_type == VIDEO_TYPES.MOVIE and not is_season) or (video_type == VIDEO_TYPES.SEASON and is_season):
                    match_year = ''
                    if video_type == VIDEO_TYPES.SEASON:
                        match_title = match_title_year
                        if season and not re.search('Season\s+(%s)\s+' % (season), match_title_year, re.I):
                            continue
                    else:
                        match = re.search('(.*?)\s+(\d{4})$', match_title_year)
                        if match:
                            match_title, match_year = match.groups()
                        else:
                            match_title = match_title_year
                            match_year = ''
        
                    match_url = urlparse.urljoin(match_url, 'watching.html')
                    if not year or not match_year or year == match_year:
                        result = {'url': scraper_utils.pathify_url(match_url), 'title': scraper_utils.cleanse_title(match_title), 'year': match_year}
                        results.append(result)
        return results
