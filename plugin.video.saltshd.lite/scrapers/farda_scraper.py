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
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
import scraper

BASE_URL = 'http://dl.fardadownload.ir/Serial'

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
        return 'FardaDownload'

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        norm_title = scraper_utils.normalize_title(video.title)
        if source_url and source_url != FORCE_NO_MATCH:
            source_url = urlparse.urljoin(self.base_url, source_url)
            for line in self._get_files(source_url, cache_limit=24):
                if not line['directory']:
                    match = {}
                    if video.video_type == VIDEO_TYPES.MOVIE:
                        match_title, _match_year, height, extra = scraper_utils.parse_movie_link(line['link'])
                        if norm_title in scraper_utils.normalize_title(match_title):
                            match = line
                    else:
                        _show_title, season, episode, height, extra = scraper_utils.parse_episode_link(line['link'])
                        if int(video.season) == int(season) and int(video.episode) == int(episode):
                            match = line
                        
                    if 'dubbed' in extra.lower(): continue
                    if match:
                        stream_url = match['url'] + '|User-Agent=%s' % (scraper_utils.get_ua())
                        stream_url = stream_url.replace(self.base_url, '')
                        hoster = {'multi-part': False, 'host': self._get_direct_hostname(stream_url), 'class': self, 'quality': scraper_utils.height_get_quality(height), 'views': None, 'rating': None, 'url': stream_url, 'direct': True}
                        if 'x265' in extra: hoster['format'] = 'x265'
                        if 'size' in match: hoster['size'] = scraper_utils.format_size(int(match['size']))
                        hosters.append(hoster)
            
        return hosters

    def _get_episode_url(self, show_url, video):
        force_title = scraper_utils.force_title(video)
        if not force_title:
            show_url = self.base_url + show_url
            html = self._http_get(show_url, cache_limit=48)
            match = re.search('href="(S%02d/)"' % (int(video.season)), html)
            if match:
                season_url = urlparse.urljoin(show_url, match.group(1))
            else:
                season_url = show_url

            for item in self._get_files(season_url, cache_limit=8):
                match = re.search('[._ -]S%02d[._ -]?E%02d[._ -]' % (int(video.season), int(video.episode)), item['title'], re.I)
                if match:
                    return scraper_utils.pathify_url(season_url)

    def search(self, video_type, title, year, season=''):
        results = []
        norm_title = scraper_utils.normalize_title(title)
        html = self._http_get(self.base_url, cache_limit=24 * 7)
        for item in self._parse_directory(html):
            if norm_title in scraper_utils.normalize_title(item['title']) and item['directory']:
                result = {'url': scraper_utils.pathify_url(item['link']), 'title': scraper_utils.cleanse_title(item['title']), 'year': ''}
                results.append(result)
        return results
