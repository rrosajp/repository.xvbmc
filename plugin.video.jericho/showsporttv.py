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
    utils.addDir('Schedule','http://showsport-tv.com/',271,'http://showsport-tv.com/images/logo.png','')
    
    listhtml = utils.getHtml('http://showsport-tv.com/', 'http://showsport-tv.com/')
    match = re.compile(r'<a\s*href="([^"]+)"\s*title="([^"]+) live stream"><img\ssrc="([^"]+)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, name, img in match:
        img = 'http://showsport-tv.com' + img
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://showsport-tv.com' + videopage
        utils.addDir(name, videopage,300,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    


def List(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile(r'src="(.*?)".*?(?:rel="(\d*)"></span>|src="/images/(live).gif">)</div><div[^>]*><img[^>]*><span>([^<]*)</span></div>\s*(?:<div[^>]*><img[^>]*></div>\s*<div[^>]*><span[^>]*>([^<]*)</span><img[^>]*></div>)?<div[^>]*>\s*<a class="online" href="([^"]*)">', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for img, time, live, p1, p2, url in match:
    #if time in match:
        try:
            print(datetime.datetime.fromtimestamp(int(time)).strftime('%d %B %H:%M'))
        except :
            pass
        name = p1 + ' - ' + p2
        img = 'http://showsport-tv.com' + img
        url = 'http://showsport-tv.com' + url
        utils.addDir(name,url,272,img,'')         
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
    
def ListStream(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile(r""""setURL\('([^"]+)'\)">([^<]+)</button>""", re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, name in match:  
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://showsport-tv.com' + videopage
        utils.addDownLink(name, videopage, 300, '', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)