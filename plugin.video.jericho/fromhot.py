import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon
from datetime import datetime, timedelta
from time import time

import utils

def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)

def Main():
    listhtml = utils.getHtml('http://www.fromhot.com/', 'http://www.fromhot.com/')
    match = re.compile('<li id=".*?">.*?href="(.*?)">(.*?)</a></li>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for menupage, name in match:
        utils.addDir(name, menupage,255,'http://www.u-bet.be/wp-content/uploads/2015/10/FromHot.png','')
    xbmcplugin.endOfDirectory(utils.addon_handle)

#def Main():
#    utils.addDir('Show All','http://www.stream2watch.co/live-now/sport-stream',249,'','')
#    utils.addDir('Soccer','http://www.stream2watch.co/live-now/sport-stream/soccer',249,'http://www.stream2watch.co/logos/Soccer.png','')
#    utils.addDir('Basketball','http://www.stream2watch.co/live-now/sport-stream/basketball',249,'http://www.stream2watch.co/logos/Basketball.png','')
#    utils.addDir('Boxing','http://www.stream2watch.co/live-now/sport-stream/boxing',249,'http://www.stream2watch.co/logos/Boxing.png','')
#    utils.addDir('Darts','http://www.stream2watch.co/live-now/sport-stream/darts',249,'http://www.stream2watch.co/logos/Darts.png','')
#    utils.addDir('Football','http://www.stream2watch.co/live-now/sport-stream/football',249,'http://www.stream2watch.co/logos/Football.png','')
#    utils.addDir('Golf','http://www.stream2watch.co/live-now/sport-stream/golf',249,'http://www.stream2watch.co/logos/Golf.png','')
#    utils.addDir('Hockey','http://www.stream2watch.co/live-now/sport-stream/hockey',249,'http://www.stream2watch.co/logos/Hockey.png','')
#    utils.addDir('Baseball','http://www.stream2watch.co/live-now/sport-stream/baseball',249,'http://www.stream2watch.co/logos/Baseball.png','')
#    utils.addDir('Motor','http://www.stream2watch.co/live-now/sport-stream/motor',249,'http://www.stream2watch.co/logos/Motor.png','')
#    utils.addDir('Tennis','http://www.stream2watch.co/live-now/sport-stream/tennis',249,'http://www.stream2watch.co/logos/Tennis.png','')
#    utils.addDir('Wrestling','http://www.stream2watch.co/live-now/sport-stream/wrestling',249,'http://www.stream2watch.co/logos/Wrestling.png','')
#    xbmcplugin.endOfDirectory(utils.addon_handle)
    


def List(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile('<span class=".*?">(.*?)</span> - <span class=".*?">(.*?)</span>.*?.*?class.*?<td>(.*?)</td>.*?href="(.*?)".*?>(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    #match = re.compile(r">(\d+:\d+)</span> - <.+?class=[\"\']flg.+?[\"\']>.+?<td>([^<]+)</td><td.+?target=[\"\']_blank[\"\'].+?title=[\"\']Open Video[\"\']>([^<]+)<.+?id=.+?a href=[\"\']([^\"\']+)", re.IGNORECASE | re.DOTALL)
    for tijd1, tijd2, competitie, videopage, wedstrijd in match:
        name = tijd1 + ' - ' + tijd2 + ' ' + '(' + competitie + ')' + ' ' + wedstrijd
        if 'Unibet' in name:
            pass
        else:
            videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
            utils.addDir(name,videopage,300,'http://www.u-bet.be/wp-content/uploads/2015/10/FromHot.png','')
    xbmcplugin.endOfDirectory(utils.addon_handle)