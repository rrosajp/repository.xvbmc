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
    utils.addDir('All Matches','http://livefootballvideo.com/streaming',265,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Competitions','http://livefootballvideo.com/competitions',266,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg') 
    utils.addDir('Teams','http://livefootballvideo.com/teams',266,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg') 
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
    match = re.compile('<div class="leaguelogo column">.*?src="(.*?)" alt.*?title="(.*?)">.*?rel=".*?">(.*?)</span>.*?alt="(.*?)".*?versus.*?">(.*?)</div>.*?alt="(.*?)".*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    #match = re.compile(r">(\d+:\d+)</span> - <.+?class=[\"\']flg.+?[\"\']>.+?<td>([^<]+)</td><td.+?target=[\"\']_blank[\"\'].+?title=[\"\']Open Video[\"\']>([^<]+)<.+?id=.+?a href=[\"\']([^\"\']+)", re.IGNORECASE | re.DOTALL)
    for img, competitie, tijd, hometeam, vs, awayteam, videopage in match:
        name = tijd + ' - (' + competitie + ') ' + hometeam + ' ' + vs + ' ' + awayteam
        utils.addDir(name,videopage,267,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListTeams(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('src="(.*?)".*?href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for img, videopage, name in match:
        name = striphtml(name)
        img = "http://livefootballvideo.com" + img
        videopage = "http://livefootballvideo.com" + videopage
        utils.addDownLink(name, videopage, 265, img, '', fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListStreams(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile("</tr>.*?src='(.*?)'.*?left'>(.*?)</td>.*?td>(.*?)</td><td>(.*?)</td>.*?href='(.*?)'", re.IGNORECASE | re.DOTALL).findall(listhtml)
    #match = re.compile(r">(\d+:\d+)</span> - <.+?class=[\"\']flg.+?[\"\']>.+?<td>([^<]+)</td><td.+?target=[\"\']_blank[\"\'].+?title=[\"\']Open Video[\"\']>([^<]+)<.+?id=.+?a href=[\"\']([^\"\']+)", re.IGNORECASE | re.DOTALL)
    for img, name, taal, bitrate, videopage in match:
        name = name + ' - ' + taal + ' (' + bitrate + ')'
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        img = "http://livefootballvideo.com" + img
        utils.addDir(name,videopage,300,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)