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
    utils.addDir('Show All', 'http://livetv.sx/en/allupcomingsports/',252,'http://cdn.livetvcdn.net/img/oglogo.png','')
    
    listhtml = utils.getHtml('http://livetv.sx/en/allupcomingsports/', 'http://livetv.sx/en/allupcomingsports/')
    match = re.compile('width=27><a class="main" href="(.*?)">.*?src="(.*?)".*?<b>(.*?)</b>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for menupage, img, name in match:
        menupage = 'http://livetv.sx' + menupage
        utils.addDir(name, menupage,252,img,'')
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
    timezone = re.compile('&nbsp;&nbsp;&nbsp;<span class="date">(.*?)<.*?">(.*?)<', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name, tijdzone in timezone:
        name = name + tijdzone + ')'
        utils.addDir(name,'',252,'','')
    
    listmenu = re.compile('<table align="center" width="90%"></tr><tr><td colspan=4 height=48><br><b>.*?</b>(.*?)<table width="100%" cellpadding=0 cellspacing=0>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile(r'<img width=27.*?src="(.*?)".*?<a class="live" href="(.*?)">(.*?)</a>.*?evdesc">.*?at (.*?)\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s<br>.*?(\(.*?)</span>', re.IGNORECASE | re.DOTALL).findall(listmenu)
    for img, videopage, wedstrijd, tijd, competitie in match:  
        wedstrijd = striphtml(wedstrijd)
        wedstrijd = utils.cleantext(wedstrijd)
        name = tijd + ' - ' + wedstrijd + ' ' + competitie
        videopage = 'http://livetv.sx' + videopage
        utils.addDir(name,videopage,253,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
    
def ListStream(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile(r'show_webplayer\(\'(\w+)\',\s*\'(\w+)\',\s*(\w+),\s*(\w+),\s*(\w+),\s*(\w+),\s*\'(\w+)\'\).+?href="(.+?)">', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for streamer_tmp,video,eid,lid,ci,si,jj,url in match:        
        xbmc.log(url)
        name = streamer_tmp + ' - ' + video
        url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + url
        utils.addDownLink(name, url, 300, 'http://cdn.livetvcdn.net/img/oglogo.png', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)