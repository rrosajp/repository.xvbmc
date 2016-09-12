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
    utils.addDir('Show All','http://www.stream2watch.cc/live-sports',249,'','')
    listhtml = utils.getHtml('http://www.stream2watch.cc/live-sports','http://www.stream2watch.cc/live-sports')
    match = re.compile('<a title="(.*?)" href="(.*?)" class=.*?src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for title, pageurl, img in match:
        utils.addDir(title,pageurl,249,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    


def List(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile('img alt="(.*?)" src="(.*?)".*?<a class="title-t-a" href="(.*?)" title="(.*?)".*?stream-live" title="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for sport, img, videopage, wedstrijd, tijd in match:
        try:
            dt = datetime.strptime(tijd, "%H:%M")
            tijd = str(dt.hour+2).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
        except :
            pass  
        wedstrijd = striphtml(wedstrijd)      
        tijd = tijd.replace('24','00').replace('25','01').replace('26','02')
        name = tijd + ' - ' + sport + ': ' + wedstrijd
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDownLink(name, videopage, 300, '', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)