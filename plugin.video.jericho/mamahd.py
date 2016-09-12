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
    listhtml = utils.getHtml('http://mamahd.com/live/', 'http://mamahd.com/live/')
    match = re.compile(r'href="([^"]+)">[\s\t]*<img\s*src="([^"]+)"\s*/*><br\s*/*>[\s\t]*<span>([^<]+)', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, img, name in match:
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(name, videopage,300,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)