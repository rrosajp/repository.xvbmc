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
    utils.addDir('Schedule','http://hdfree.tv/live-sports-streaming.php',274,'http://showsport-tv.com/images/logo.png','')
    
    listhtml = utils.getHtml('http://hdfree.tv/tvlogos.html', 'http://hdfree.tv/tvlogos.html')
    match = re.compile(r'<a href="(http://hdfree.tv/[^"#]+)".*?<img\s*src="([^"#]+)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, img in match:
        name = videopage.replace('http://hdfree.tv/watch/','').replace('-live-stream.html','').replace('-',' ')
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(name, videopage,300,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    


def List(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile(r"""(\d\d:\d\d)\s*-\s*(\d\d:\d\d)</span><h3 class="panel-title">\s*([^<]+).*?href='([^'"]+)""", re.IGNORECASE | re.DOTALL).findall(listhtml)
    for tijd1, tijd2, wedstrijd, videopage in match:
        try:
            dt = datetime.strptime(tijd1, "%H:%M")
            tijd = str(dt.hour+1).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
        except :
            pass  
        try:
            dt = datetime.strptime(tijd2, "%H:%M")
            tijd = str(dt.hour+1).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
        except :
            pass  
        name = '[' + tijd1 + ' - ' + tijd2 + '] ' + wedstrijd
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDownLink(name, videopage, 300, '', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    