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


DEBUG = True
CHANNELNAME = "fhe"

def isGeneric():
    return True

# Entry point
def mainlist(item):
    logger.info("fhe.main_list")
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 1" , action="play" , url="http://fhe.sc/popup/popup-1.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 2" , action="play" , url="http://fhe.sc/popup/popup-2.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 3" , action="play" , url="http://fhe.sc/popup/popup-3.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="FHE 4" , action="play" , url="http://fhe.sc/popup/popup-4.php",thumbnail="https://www.fhe.sc/wp-content/uploads/2017/04/cropped-logo-1.png") )
    return itemlist



def play(item):
    logger.info("dss.channels.fhe play")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    data_url = re.compile('file: \'(.*?)\'', re.DOTALL | re.IGNORECASE).findall(data)
    for url in data_url:
        itemlist.append([item.title, url])
    return itemlist



def dialog_notification(heading, message, icon=0, time=5000, sound=True):
    import xbmcgui
    dialog = xbmcgui.Dialog()
    l_icono=(xbmcgui.NOTIFICATION_INFO , xbmcgui.NOTIFICATION_WARNING, xbmcgui.NOTIFICATION_ERROR)
    dialog.notification (heading, message, l_icono[icon], time, sound)
