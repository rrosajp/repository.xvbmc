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
    listhtml = utils.getHtml('http://woop.io/','http://woop.io/')
    match1 = re.compile('<li> <i class=""><img src="(.*?)".*?href="(.*?)"> (.*?) </a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for img, listpage, name in match1:
        listpage = 'http://woop.io' + listpage
        utils.addDir(name,listpage,310,img,'')
    utils.addDir('Competitions','',309,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Competitions():
    listhtml = utils.getHtml('http://woop.io/','http://woop.io/')
    match = re.compile("""primary'>(.*?)</span><a target=".*?" href="(.*?)"> (.*?)</a>""", re.IGNORECASE | re.DOTALL).findall(listhtml)
    for sport, listpage, name in match:
        listpage = 'http://woop.io' + listpage
        utils.addDir('['+sport+'] ' + name,listpage,310,'','')
        #utils.addDir('[soccer] Dutch Eerste Divisie', 'http://woop.io/competition/Dutch-Eerste-Divisie-stream-soccer-36.html', 310,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def List(url):
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    listhtml = utils.getHtml(url, url)
    match = re.compile(r'moment\("(.*?):00\+.*?href="\.\./\.\.(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for tijd, videopage, wedstrijd in match:
        wedstrijd = striphtml(wedstrijd)      
        name = tijd + ' - ' + wedstrijd
        videopage = 'http://woop.io' + videopage
        utils.addDir(name, videopage, 311, '', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Liststreams(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile('<div class="add-image">.*?src="(.*?)".*?"">(.*?)</a>.*?Provider..(.*?).</s.*?">(.*?)</', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for img, name, provider, videopage in match:
        if 'livetv' in provider:
            pass
        else:
            name = name + ' [' + provider + ']'
            videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://' + videopage
            utils.addDownLink(name, videopage, 300, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)