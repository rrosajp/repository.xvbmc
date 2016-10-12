"""
    SALTS XBMC Addon
    Copyright (C) 2016 tknorris

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
import urllib
import urllib2
import os
import ssl
import socket
import json
import utils
import log_utils
import kodi
import utils2
from db_utils import DB_Connection
from constants import VIDEO_TYPES

_db_connection = None
_tmdb_scraper = None
_tvdb_scraper = None
PLACE_POSTER = os.path.join(kodi.get_path(), 'resources', 'place_poster.png')

# delay db_connection until needed to force db errors during recovery try: block
def _get_db_connection():
    global _tmdb_scraper
    if _tmdb_scraper is None:
        _tmdb_scraper = DB_Connection()
    return _tmdb_scraper
    
def _get_tmdb_scraper():
    global _tvdb_scraper
    if _tvdb_scraper is None:
        _tvdb_scraper = TMDBScraper()
    return _tvdb_scraper
    
def _get_tvdb_scraper():
    global _tvdb_scraper
    if _tvdb_scraper is None:
        _tvdb_scraper = TVDBScraper()
    return _tvdb_scraper
    
class Scraper(object):
    protocol = 'http://'
    
    def _clean_art(self, art_dict):
        new_dict = {}
        for key in art_dict:
            if art_dict[key]:
                new_dict[key] = art_dict[key]
        return new_dict
    
    def _get_url(self, url, params=None, data=None, headers=None):
        if headers is None: headers = {}
        if data is not None:
            if isinstance(data, basestring):
                data = data
            else:
                data = urllib.urlencode(data, True)
        
        url = '%s%s%s' % (self.protocol, self.BASE_URL, url)
        if params: url = url + '?' + urllib.urlencode(params)
        log_utils.log('Calling: %s' % (url))
        db_connection = _get_db_connection()
        _created, _res_header, html = db_connection.get_cached_url(url, data, cache_limit=1)
        if html:
            log_utils.log('Using Cached result for: %s' % (url))
            result = html
        else:
            try:
                request = urllib2.Request(url, data=data, headers=headers)
                response = urllib2.urlopen(request)
                result = ''
                while True:
                    data = response.read()
                    if not data: break
                    result += data
                db_connection.cache_url(url, result, data)
            except (ssl.SSLError, socket.timeout) as e:
                log_utils.log('Image Scraper Timeout: %s' % (url))
                return {}
            except urllib2.HTTPError as e:
                if e.code != 404:
                    log_utils.log('HTTP Error (%s) during image scraper http get: %s' % (e, url))
                return {}
            except Exception as e:
                log_utils.log('Error (%s) during image scraper http get: %s' % (str(e), url), log_utils.LOGWARNING)
                return {}

        try:
            js_data = utils.json_loads_as_str(result)
        except ValueError:
            js_data = ''
            if result:
                log_utils.log('Invalid JSON API Response: %s - |%s|' % (url, js_data), log_utils.LOGERROR)

        return js_data
        
class FanartTVScraper(Scraper):
    API_KEY = kodi.get_setting('fanart_key')
    BASE_URL = 'webservice.fanart.tv/v3'

    def get_movie_images(self, ids):
        art_dict = {}
        video_id = ids.get('tmdb') or ids.get('imdb')
        if self.API_KEY and video_id:
            url = '/movies/%s' % (video_id)
            params = {'api_key': self.API_KEY}
            images = self._get_url(url, params)
            art_dict['banner'] = self.__get_best_image(images.get('moviebanner', []))
            art_dict['fanart'] = self.__get_best_image(images.get('moviebackground', []))
            if not art_dict['fanart']: art_dict['fanart'] = self.__get_best_image(images.get('moviethumb', []))
            art_dict['poster'] = self.__get_best_image(images.get('movieposter', []))
            art_dict['clearlogo'] = self.__get_best_image(images.get('hdmovielogo', []))
            if not art_dict['clearlogo']: art_dict['clearlogo'] = self.__get_best_image(images.get('movielogo', []))
            art_dict['clearart'] = self.__get_best_image(images.get('hdmovieclearart', []))
        
        return self._clean_art(art_dict)
    
    def get_tvshow_images(self, ids):
        art_dict = {}
        if self.API_KEY and 'tvdb' in ids and ids['tvdb']:
            url = '/tv/%s' % (ids['tvdb'])
            params = {'api_key': self.API_KEY}
            images = self._get_url(url, params)
            art_dict['banner'] = self.__get_best_image(images.get('tvbanner', []))
            art_dict['fanart'] = self.__get_best_image(images.get('showbackground', []))
            if not art_dict['fanart']: art_dict['fanart'] = self.__get_best_image(images.get('tvthumb', []))
            art_dict['poster'] = self.__get_best_image(images.get('tvposter', []))
            art_dict['clearlogo'] = self.__get_best_image(images.get('hdtvlogo', []))
            if not art_dict['clearlogo']: art_dict['clearlogo'] = self.__get_best_image(images.get('clearlogo', []))
            art_dict['clearart'] = self.__get_best_image(images.get('hdclearart', []))
            if not art_dict['clearart']: art_dict['clearart'] = self.__get_best_image(images.get('clearart', []))
        
        return self._clean_art(art_dict)
    
    def get_season_images(self, ids):
        season_art = {}
        if 'tvdb' in ids and ids['tvdb']:
            url = '/tv/%s' % (ids['tvdb'])
            params = {'api_key': self.API_KEY}
            images = self._get_url(url, params)
            seasons = set()
            for name in ['seasonposter', 'seasonthumb', 'seasonbanner']:
                seasons |= set([i['season'] for i in images.get(name, [])])
            
            for season in seasons:
                art_dict = {}
                art_dict['poster'] = self.__get_best_image(images.get('seasonposter', []), season)
                art_dict['banner'] = self.__get_best_image(images.get('seasonbanner', []), season)
                art_dict['thumb'] = self.__get_best_image(images.get('seasonthumb', []), season)
                season_art[season] = self._clean_art(art_dict)
                
        return season_art
    
    def __get_best_image(self, images, season=None):
        best = ''
        images = [image for image in images if image.get('lang') == 'en']
        if season is not None:
            images = [image for image in images if image.get('season') == season]
            
        images.sort(key=lambda x: int(x['likes']), reverse=True)
        if images:
            best = images[0]['url']
        return best

class TMDBScraper(Scraper):
    API_KEY = kodi.get_setting('tmdb_key')
    protocol = 'https://'
    BASE_URL = 'api.themoviedb.org/3'
    headers = {'Content-Type': 'application/json'}
    size = 'original'
    
    def __init__(self):
        if self.API_KEY:
            url = '/configuration'
            params = {'api_key': self.API_KEY}
            js_data = self._get_url(url, params, headers=self.headers)
            self.image_base = '%s/%s/' % (js_data['images']['base_url'], self.size)
        else:
            self.image_base = None
        
    def get_movie_images(self, ids):
        art_dict = {}
        if self.image_base and 'tmdb' in ids and ids['tmdb']:
            url = '/movie/%s/images' % (ids['tmdb'])
            params = {'api_key': self.API_KEY, 'include_image_language': 'en,null'}
            images = self._get_url(url, params, headers=self.headers)
            art_dict['fanart'] = self.__get_best_image(images.get('backdrops', []))
            art_dict['poster'] = self.__get_best_image(images.get('posters', []))
        return self._clean_art(art_dict)
    
    def __get_best_image(self, images):
        best = ''
        if images:
            images.sort(key=lambda x: x['width'], reverse=True)
            best = images[0]['file_path']
        
        if best:
            best = self.image_base + best
            
        return best
    
class TVDBScraper(Scraper):
    API_KEY = kodi.get_setting('tvdb_key')
    protocol = 'https://'
    BASE_URL = 'api.thetvdb.com'
    headers = {'Content-Type': 'application/json'}
    image_base = 'http://thetvdb.com/banners/'
    
    def __init__(self):
        if self.API_KEY:
            url = '/login'
            data = {'apikey': self.API_KEY}
            js_data = self._get_url(url, data=json.dumps(data), headers=self.headers)
            self.token = js_data.get('token')
            self.headers.update({'Authorization': 'Bearer %s' % (self.token)})
        else:
            self.token = None
    
    def get_tvshow_images(self, ids, need=None):
        if need is None: need = ['fanart', 'poster', 'banner']
        art_dict = {}
        if 'tvdb' in ids and ids['tvdb'] and self.token is not None:
            url = '/series/%s/images/query' % (ids['tvdb'])
            if 'fanart' in need:
                params = {'keyType': 'fanart'}
                images = self._get_url(url, params, headers=self.headers)
                art_dict['fanart'] = self.__get_best_image(images.get('data', []))
            
            if 'poster' in need:
                params = {'keyType': 'poster'}
                images = self._get_url(url, params, headers=self.headers)
                art_dict['poster'] = self.__get_best_image(images.get('data', []))
            
            if 'banner' in need:
                params = {'keyType': 'series'}
                images = self._get_url(url, params, headers=self.headers)
                art_dict['banner'] = self.__get_best_image(images.get('data', []))
            
        return self._clean_art(art_dict)
    
    def get_season_images(self, ids, need=None):
        season_art = {}
        if need is None: need = ['poster', 'banner']
        if 'tvdb' in ids and ids['tvdb'] and self.token is not None:
            url = '/series/%s/images/query' % (ids['tvdb'])
            images = {}
            seasons = set()
            if 'poster' in need:
                params = {'keyType': 'season'}
                images['season'] = self._get_url(url, params, headers=self.headers).get('data', [])
                seasons |= set([i['subKey'] for i in images.get('season', [])])
            
            if 'banner' in need:
                params = {'keyType': 'seasonwide'}
                images['seasonwide'] = self._get_url(url, params, headers=self.headers).get('data', [])
                seasons |= set([i['subKey'] for i in images.get('seasonwide', [])])
                
            for season in seasons:
                art_dict = {}
                art_dict['poster'] = self.__get_best_image(images.get('season', []), season)
                art_dict['banner'] = self.__get_best_image(images.get('seasonwide', []), season)
                season_art[season] = self._clean_art(art_dict)
                
        return season_art
    
    def __get_best_image(self, images, season=None):
        best = ''
        if season is not None:
            images = [image for image in images if image['subKey'] == season]
                
        if images:
            images.sort(key=lambda x: (x['resolution'], x['ratingsInfo']['average'], x['ratingsInfo']['count']), reverse=True)
            best = images[0]['fileName']
            
        if best:
            best = self.image_base + best
            
        return best

class OMDBScraper(Scraper):
    BASE_URL = 'www.omdbapi.com/'
    
    def get_images(self, ids):
        art_dict = {}
        if 'imdb' in ids and ids['imdb']:
            url = ''
            params = {'i': ids['imdb'], 'plot': 'short', 'r': 'json'}
            images = self._get_url(url, params)
            if 'Poster' in images and images['Poster'].startswith('http'): art_dict['poster'] = images['Poster']
        return self._clean_art(art_dict)

def get_images(video_type, video_ids, season='', episode=''):
    trakt_id = video_ids['trakt']
    art_dict = {'banner': '', 'fanart': utils2.art('fanart.jpg'), 'thumb': '', 'poster': PLACE_POSTER, 'clearart': '', 'clearlogo': ''}
    db_connection = _get_db_connection()
    cached_art = db_connection.get_cached_images(trakt_id, season, episode)
    if cached_art:
        art_dict.update(cached_art)
    else:
        fanart_scraper = FanartTVScraper()
        omdb_scraper = OMDBScraper()
        if video_type == VIDEO_TYPES.MOVIE:
            art_dict.update(fanart_scraper.get_movie_images(video_ids))
            
            if art_dict['fanart'] == utils2.art('fanart.jpg') or art_dict['poster'] == PLACE_POSTER:
                tmdb_scraper = _get_tmdb_scraper()
                art_dict.update(tmdb_scraper.get_movie_images(video_ids))
                
            if art_dict['poster'] == PLACE_POSTER:
                art_dict.update(omdb_scraper.get_images(video_ids))
        elif video_type == VIDEO_TYPES.TVSHOW:
            art_dict.update(fanart_scraper.get_tvshow_images(video_ids))
            
            need = []
            if art_dict['fanart'] == utils2.art('fanart.jpg'): need.append('fanart')
            if art_dict['poster'] == PLACE_POSTER: need.append('poster')
            if not art_dict['banner']: need.append('banner')
            if need:
                tvdb_scraper = _get_tvdb_scraper()
                art_dict.update(tvdb_scraper.get_tvshow_images(video_ids, need))
            
            if art_dict['poster'] == PLACE_POSTER:
                art_dict.update(omdb_scraper.get_images(video_ids))
        elif video_type == VIDEO_TYPES.SEASON:
            art_dict = get_images(VIDEO_TYPES.TVSHOW, video_ids)
            season_art = fanart_scraper.get_season_images(video_ids)

            need = []
            if not all([season_art[key].get('poster', False) for key in season_art]): need.append('poster')
            if not all([season_art[key].get('banner', False) for key in season_art]): need.append('banner')
            if need:
                tvdb_scraper = _get_tvdb_scraper()
                season_art2 = tvdb_scraper.get_season_images(video_ids, need)
                for key in season_art2:
                    season_art.get(key, {}).update(season_art2[key])
            
            for key in season_art:
                temp_dict = art_dict.copy()
                temp_dict.update(season_art[key])
                db_connection.cache_images(trakt_id, temp_dict, key)
                
            art_dict.update(season_art.get(str(season), {}))
        elif video_type == VIDEO_TYPES.EPISODE:
            art_dict = get_images(VIDEO_TYPES.TVSHOW, video_ids)
                
        if not art_dict['thumb']:
            if art_dict['poster']: art_dict['thumb'] = art_dict['poster']
            elif art_dict['fanart']: art_dict['thumb'] = art_dict['fanart']
            
        db_connection.cache_images(trakt_id, art_dict, season, episode)
    
    return art_dict
