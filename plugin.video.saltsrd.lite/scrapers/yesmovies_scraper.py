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
from salts_lib import dom_parser
from salts_lib import kodi
from salts_lib import log_utils
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import QUALITIES
from salts_lib.constants import VIDEO_TYPES
import scraper
import xml.etree.ElementTree as ET


BASE_URL = 'http://yesmovies.to'
QP_URL = '/ajax/movie_quick_play/%s.html'
SL_URL = '/ajax/movie_servers_list/%s/%s/%s.html'
PLAYLIST_URL1 = '/ajax/movie_load_embed/%s.html'
PLAYLIST_URL2 = '/ajax/movie_load_episode_rss/%s.html'
XHR = {'X-Requested-With': 'XMLHttpRequest'}

class YesMovies_Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.MOVIE, VIDEO_TYPES.SEASON, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'YesMovies'

    def resolve_link(self, link):
        return link

    def format_source_label(self, item):
        label = '[%s] %s' % (item['quality'], item['host'])
        return label

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            links = []
            page_url = urlparse.urljoin(self.base_url, source_url)
            if video.video_type == VIDEO_TYPES.MOVIE:
                _, html = self.__get_source_page(source_url)
                for match in re.finditer('''load_episode\(\s*(\d+)\s*,\s*(\d+)''', html, re.DOTALL):
                    links.append(match.groups())
            else:
                html = self._http_get(page_url, cache_limit=1)
                match1 = re.search('default_server\s*:\s*"([^"]+)', html)
                match2 = re.search('episode_id\s*:\s*"([^"]+)', html)
                if match1 and match2:
                    links.append((match1.group(1), match2.group(1)))
            
            for link_type, link_id in links:
                if link_type in ['12', '13', '14', '15']:
                    url = urlparse.urljoin(self.base_url, PLAYLIST_URL1 % (link_id))
                    sources = self.__get_link_from_json(url)
                else:
                    url = urlparse.urljoin(self.base_url, PLAYLIST_URL2 % (link_id))
                    sources = self.__get_links_from_xml(url, video, page_url)
            
                for source in sources:
                    if not source.lower().startswith('http'): continue
                    if sources[source]['direct']:
                        host = self._get_direct_hostname(source)
                        if host != 'gvideo':
                            stream_url = source + '|User-Agent=%s&Referer=%s' % (scraper_utils.get_ua(), page_url)
                        else:
                            stream_url = source
                    else:
                        host = urlparse.urlparse(source).hostname
                        stream_url = source
                    hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': sources[source]['quality'], 'views': None, 'rating': None, 'url': stream_url, 'direct': sources[source]['direct']}
                    hosters.append(hoster)
        return hosters

    def __get_source_page(self, page_url):
        html = ''
        sl_url = ''
        match = re.search('(\d+)\.html', page_url)
        if match:
            qp_url = QP_URL % (match.group(1))
            qp_url = urlparse.urljoin(self.base_url, qp_url)
            headers = XHR
            headers['Referer'] = urlparse.urljoin(self.base_url, page_url)
            html = self._http_get(qp_url, headers=headers, cache_limit=24)
            source_url = dom_parser.parse_dom(html, 'a', {'title': 'View all episodes'}, ret='href')
            if source_url:
                match = re.search('-(\d+)/(\d+)-(\d+)/', source_url[0])
                if match:
                    show_id, episode_id, server_id = match.groups()
                    sl_url = SL_URL % (show_id, episode_id, server_id)
                    sl_url = urlparse.urljoin(self.base_url, sl_url)
                    html = self._http_get(sl_url, headers=headers, cache_limit=8)
        return sl_url, html
        
    def __get_link_from_json(self, url):
        sources = {}
        html = self._http_get(url, cache_limit=.5)
        js_result = scraper_utils.parse_json(html, url)
        if 'embed_url' in js_result:
            sources[js_result['embed_url']] = {'quality': QUALITIES.HIGH, 'direct': False}
        return sources
    
    def __get_links_from_xml(self, url, video, page_url):
        sources = {}
        try:
            headers = {'Referer': page_url}
            xml = self._http_get(url, headers=headers, cache_limit=.5)
            root = ET.fromstring(xml)
            for item in root.findall('.//item'):
                title = item.find('title').text
                for source in item.findall('{http://rss.jwpcdn.com/}source'):
                    stream_url = source.get('file')
                    label = source.get('label')
                    if self._get_direct_hostname(stream_url) == 'gvideo':
                        quality = scraper_utils.gv_get_quality(stream_url)
                    elif label:
                        quality = scraper_utils.height_get_quality(label)
                    elif title:
                        quality = scraper_utils.blog_get_quality(video, title, '')
                    else:
                        quality = scraper_utils.blog_get_quality(video, stream_url, '')
                    sources[stream_url] = {'quality': quality, 'direct': True}
                    log_utils.log('Adding stream: %s Quality: %s' % (stream_url, quality), log_utils.LOGDEBUG)
        except Exception as e:
            log_utils.log('Exception during YesMovies XML Parse: %s' % (e), log_utils.LOGWARNING)
            raise

        return sources
    
    def _get_episode_url(self, season_url, video):
        sl_url, _ = self.__get_source_page(season_url)
        episode_pattern = '''onclick="[^"]*(http://[^']+)[^>]+Episode\s+0*%s''' % (video.episode)
        title_pattern = '''onclick="[^"]*(?P<url>http://[^']+)[^>]+Episode\s+\d+:\s*(?P<title>[^"]+)'''
        headers = XHR
        headers['Referer'] = urlparse.urljoin(self.base_url, season_url)
        return self._default_get_episode_url(sl_url, video, episode_pattern=episode_pattern, title_pattern=title_pattern, headers=headers)
    
    def search(self, video_type, title, year, season=''):
        results = []
        search_url = urlparse.urljoin(self.base_url, '/ajax/movie_suggest_search.html')
        title = re.sub('[^A-Za-z0-9 ]', '', title)
        data = {'keyword': title}
        headers = XHR
        headers['Referer'] = self.base_url
        html = self._http_get(search_url, data=data, headers=headers, cache_limit=8)
        js_data = scraper_utils.parse_json(html, search_url)
        html = js_data.get('content', '')
        html = html.replace('\"', '"')
        log_utils.log(html)
        titles = dom_parser.parse_dom(html, 'a', {'class': 'ss-title'})
        urls = dom_parser.parse_dom(html, 'a', {'class': 'ss-title'}, ret='href')
        match_year = ''
        for match_title, match_url in zip(titles, urls):
            is_season = re.search('Season\s+(\d+)', match_title, re.I)
            if (video_type == VIDEO_TYPES.MOVIE and not is_season) or (video_type == VIDEO_TYPES.SEASON and is_season):
                if video_type == VIDEO_TYPES.SEASON:
                    if season and int(season) != int(is_season.group(1)): continue
                    
                if not year or not match_year or year == match_year:
                    result = {'title': scraper_utils.cleanse_title(match_title), 'year': match_year, 'url': scraper_utils.pathify_url(match_url)}
                    results.append(result)
    
            return results
