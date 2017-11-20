# -*- coding: utf-8 -*-
#------------------------------------------------------------
# channels eredivisieclubs
#---------------------------------------------------------------------------
import os
import sys

import urlparse,re,urllib2
import urllib
import datetime
import xbmc, xbmcgui,xbmcplugin
import base64

from core import logger
from core import config
from core import scrapertools
from core import httptools
from core.item import Item

try:
    import json
except:
    import simplejson as json

DEBUG = True
CHANNELNAME = "sebn"

def isGeneric():
    return True

# Entry point
def mainlist(item):
    logger.info("sebn.main_list")
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 1" , action="play" , url="http://trgoalstv.com/se1.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 2" , action="play" , url="http://trgoalstv.com/se2.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 3" , action="play" , url="http://trgoalstv.com/se3.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 4" , action="play" , url="http://trgoalstv.com/se4.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 5" , action="play" , url="http://trgoalstv.com/se5.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 6" , action="play" , url="http://trgoalstv.com/se6.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 7" , action="play" , url="http://trgoalstv.com/se7.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 8" , action="play" , url="http://trgoalstv.com/se8.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 9" , action="play" , url="http://trgoalstv.com/se9.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 10" , action="play" , url="http://trgoalstv.com/se10.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 11" , action="play" , url="http://trgoalstv.com/se11.html",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 12" , action="play" , url="http://trgoalstv.com/se12.html",thumbnail="http://sebn.sc/images/logo.png") )
  

    return itemlist



def getNowLive(item):
    try:
        # Get the ID
        data = httptools.downloadpage(item.url).data
        videoContentId = scrapertools.find_single_match(data, 'id=\'([^"]+)\'')
        referUrl =item.url   
        USER_AGENT = "Mozilla/5.0 (X11 Linux i686 rv:41.0) Gecko/20100101 Firefox/41.0 Iceweasel/41.0.2"
        
        # Get the decodeURL
        html = getRequestP2pcast("http://nowlive.club/stream.php?id=" + videoContentId + "&width=680&height=380&stretching=uniform&p=1", urllib.unquote(referUrl), USER_AGENT)
        m = re.compile('curl = "(.*?)"').search(html)
        decodedURL = base64.b64decode(m.group(1))

                        
        # Get the token
        html = getRequestP2pcast("http://nowlive.club/getToken.php", "http://nowlive.pw/stream.php?id=" + videoContentId, USER_AGENT, "XMLHttpRequest")
        m = re.compile('"token":"(.*?)"').search(html)
        token = m.group(1)


        # Parse the final URL
        u = decodedURL + token + "|Referer=http://nowlive.club/stream.php?id=" + videoContentId + "&width=680&height=380&stretching=uniform&p=1&User-Agent=" + USER_AGENT
        print ("Final URL: " + u)
        return u
    except:
        u = ''
        return u
  

def getRequestP2pcast (url, referUrl, userAgent, xRequestedWith=""):
        UTF8 = 'utf-8'
        headers = {'User-Agent':userAgent, 'Referer':referUrl, 'X-Requested-With': xRequestedWith, 'Accept':"text/html", 'Accept-Encoding':'gzip,deflate,sdch', 'Accept-Language':'en-US,en;q=0.8'} 
        request = urllib2.Request(url.encode(UTF8), None, headers)

        try:
            response = urllib2.urlopen(request)
            
            if response.info().getheader('Content-Encoding') == 'gzip':
                buf = StringIO( response.read() )
                f = gzip.GzipFile(fileobj=buf)
                link1 = f.read()
            else:
                link1=response.read()
        except:
            link1 = ""
        
        link1 = str(link1).replace('\n','')
        return(link1)


def play(item):
    try:
        item.url = getNowLive(item)
        itemlist = []
        itemlist.append([item.title, item.url])
        return itemlist
    except:
        pass
    
