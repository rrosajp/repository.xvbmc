# coding: utf-8
__author__ = 'mancuniancol'

from quasar import provider

import common
from bs4 import BeautifulSoup

# this read the settings
settings = common.Settings()
# define the browser
browser = common.Browser()
# create the filters
filters = common.Filtering()


def extract_torrents(data):
    filters.information()  # print filters settings
    sint = common.ignore_exception(ValueError)(int)
    results = []
    cont = 0
    if data is not None:
        soup = BeautifulSoup(data, 'html5lib')
        links = soup.select("div.browse-movie-bottom")
        for div in links:
            baseTitle = div.a.text  # title
            aList = div.select("div a")
            for a in aList:
                name = baseTitle + ' ' + a.text
                urlSource = a["href"]
                infoHash = urlSource[urlSource.rfind("/") + 1:-8]
                magnet = 'magnet:?xt=urn:btih:%s' % infoHash
                if filters.verify(name, None):
                    cont += 1
                    results.append({"name": name.strip(),
                                    "uri": magnet,
                                    "language": settings.value.get("language", "en"),
                                    "provider": settings.name,
                                    "icon": settings.icon,
                                    })  # return the torrent
                    if cont >= int(settings.value.get("max_magnets", 10)):  # limit magnets
                        break
                else:
                    provider.log.warning(filters.reason)
    provider.log.info('>>>>>>' + str(cont) + ' torrents sent to Quasar<<<<<<<')
    return results


def search(query):
    return []


def search_general(info):
    info["extra"] = settings.value.get("extra", '')  # add the extra information
    query = filters.type_filtering(info, '%20')  # check type filter and set-up filters.title
    url_search = settings.value["url_address"]
    provider.log.info(url_search)
    # new code
    browser.open(url_search)
    soup = BeautifulSoup(browser.content, 'html5lib')
    item_token = soup.select("div#mobile-search-input input")
    token = item_token[0]["value"]  # hidden token

    # Read
    provider.log.info(url_search)
    payload = {
        "keyword": query,
        "_token": token,
        "quality": "all",
        "genre": "all",
        "rating": "0",
        "order_by": "seeds",
    }
    provider.log.info(payload)
    browser.open(url_search + "/search-movies", payload=payload)
    return extract_torrents(browser.content)


def search_movie(info):
    info["type"] = "movie"
    if settings.value.get("language", "en") == "en":  # Title in english
        query = info['title'].encode('utf-8')  # convert from unicode
        if len(info['title']) != len(query):  # it is a english title
            query = common.IMDB_title(info['imdb_id'])  # Title + year
    else:  # Title en foreign language
        query = common.translator(info['imdb_id'], settings.value["language"])  # Just title
    info["query"] = query
    return search_general(info)


def search_episode(info):
    return []


def search_season(info):
    return []


# This registers your module for use
provider.register(search, search_movie, search_episode, search_season)

del settings
del browser
del filters

