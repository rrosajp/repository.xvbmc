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
import urlparse
import kodi
import log_utils
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
import scraper

USER_AGENT = 'Python-urllib/1.17'
VERSION = '2.3.1'

BASE_URL = 'http://pro.apollogroup.tv'
MOVIE_URL = '/movietv.meta/movie/movie.all.json'
TV_URL = '/movietv.meta/tv/tv.all.json'
MOV_SRC_URL = '/movietv.get.link.php?type=movie&imdb={imdb}&ver={ver}'
TV_SRC_URL = '/movietv.get.link.php?type=tv&imdb={imdb}&ver={ver}'
EP_SRC_URL = '&season={season}&episode={episode}'

class Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.TVSHOW, VIDEO_TYPES.EPISODE, VIDEO_TYPES.MOVIE])

    @classmethod
    def get_name(cls):
        return 'Apollo'

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            url = urlparse.urljoin(self.base_url, source_url)
            headers = {'User-Agent': USER_AGENT}
            html = self._http_get(url, headers=headers, cache_limit=.5)
            stream_url = scraper_utils.parse_json(html, url)
            if stream_url:
                host = self._get_direct_hostname(stream_url)
                if video.video_type == VIDEO_TYPES.MOVIE:
                    result = scraper_utils.parse_movie_link(stream_url)
                else:
                    result = scraper_utils.parse_episode_link(stream_url)
                quality = scraper_utils.height_get_quality(result['height'])
                hoster = {'multi-part': False, 'host': host, 'class': self, 'views': None, 'url': stream_url, 'rating': None, 'quality': quality, 'direct': True}
                hosters.append(hoster)
                
        return hosters

    def _get_episode_url(self, show_url, video):
        return show_url + EP_SRC_URL.format(**{'season': video.season, 'episode': video.episode})
    
    def search(self, video_type, title, year, season=''):
        results = []
        if video_type == VIDEO_TYPES.MOVIE:
            url = urlparse.urljoin(self.base_url, MOVIE_URL)
            src_url = MOV_SRC_URL
        else:
            url = urlparse.urljoin(self.base_url, TV_URL)
            src_url = TV_SRC_URL

        headers = {'User-Agent': USER_AGENT}
        html = self._http_get(url, headers=headers, cache_limit=48)
        norm_title = scraper_utils.normalize_title(title)
        for item in scraper_utils.parse_json(html, url):
            match_year = item.get('year', '')
            if norm_title in scraper_utils.normalize_title(item['title']) and (not year or not match_year or year == match_year):
                imdb_id = item.get('imdb')
                if imdb_id:
                    match_url = src_url.format(**{'imdb': imdb_id, 'ver': VERSION})
                    result = {'url': scraper_utils.pathify_url(match_url), 'title': scraper_utils.cleanse_title(item['title']), 'year': match_year}
                    results.append(result)
            
        return results

    @classmethod
    def has_proxy(cls):
        return True
