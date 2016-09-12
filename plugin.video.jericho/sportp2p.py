import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon
from datetime import datetime, timedelta
from time import time

import utils

def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)

 
def List(url):
    listhtml = utils.getHtml('http://www.sportp2p.com/online/','http://www.sportp2p.com/online/')
    match = re.compile('class="contact.*?src="(.*?)".*?timeh">(.*?)</div>.*?href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    #match = re.compile(r">(\d+:\d+)</span> - <.+?class=[\"\']flg.+?[\"\']>.+?<td>([^<]+)</td><td.+?target=[\"\']_blank[\"\'].+?title=[\"\']Open Video[\"\']>([^<]+)<.+?id=.+?a href=[\"\']([^\"\']+)", re.IGNORECASE | re.DOTALL)
    for img, tijd, videopage, wedstrijd in match:
        name = tijd + ' - ' + wedstrijd
        img = 'http://www.sportp2p.com' + img
        videopage = 'http://www.sportp2p.com' + videopage
        utils.addDir(name,videopage,269,img,'')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListStreams(url):
    listhtml = utils.getHtml(url, url)
    match1 = re.compile('/redirect_bet.php.link=4.*?<td class="ratetd" width="100px">100</td>(.*?)Enjoy your favorite sporting events with us!', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile("""title=".*?>...(.*?)</td>.*?open.'(.*?)'.*?b>(.*?)</b>""", re.IGNORECASE | re.DOTALL).findall(match1)
    #match = re.compile(r">(\d+:\d+)</span> - <.+?class=[\"\']flg.+?[\"\']>.+?<td>([^<]+)</td><td.+?target=[\"\']_blank[\"\'].+?title=[\"\']Open Video[\"\']>([^<]+)<.+?id=.+?a href=[\"\']([^\"\']+)", re.IGNORECASE | re.DOTALL)
    for soort, videopage, name in match:
        if 'opcast' in soort:
            pass
        elif 'ceStream' in soort:
            pass
        else:
            name = name + ' (' + soort + ')'
            videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
            utils.addDir(name,videopage,300,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)