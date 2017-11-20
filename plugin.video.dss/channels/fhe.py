# -*- coding: utf-8 -*-
#------------------------------------------------------------
# channels fhe
#---------------------------------------------------------------------------
import os
import sys

import urlparse,re
import datetime
import urllib2,urllib


from core import logger
from core import config
from core import scrapertools
from core import httptools
from core.item import Item
from platformcode import platformtools


DEBUG = True
CHANNELNAME = "fhe"

def isGeneric():
    return True

# Entry point
def mainlist(item):
    logger.info("fhe.main_list")
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 1" , action="play" , url="http://www.fhe.sc/player/streams/stream-1.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 2" , action="play" , url="http://www.fhe.sc/player/streams/stream-2.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 3" , action="play" , url="http://www.fhe.sc/player/streams/stream-3.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 4" , action="play" , url="http://www.fhe.sc/player/streams/stream-4.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 5" , action="play" , url="http://www.fhe.sc/player/streams/stream-5.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 6" , action="play" , url="http://www.fhe.sc/player/streams/stream-6.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    return itemlist





def play(item):
    logger.info("dss.channels.fhe play")
    itemlist = []
    data = httptools.downloadpage(item.url).data
    url = scrapertools.find_single_match(data, '<source.*?src="([^"]+)"')
    itemlist.append([item.title, url])
    return itemlist





def dialog_notification(heading, message, icon=0, time=5000, sound=True):
    import xbmcgui
    dialog = xbmcgui.Dialog()
    l_icono=(xbmcgui.NOTIFICATION_INFO , xbmcgui.NOTIFICATION_WARNING, xbmcgui.NOTIFICATION_ERROR)
    dialog.notification (heading, message, l_icono[icon], time, sound)
