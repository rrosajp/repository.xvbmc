# -*- coding: utf-8 -*-
#------------------------------------------------------------
# channels eredivisieclubs
#---------------------------------------------------------------------------
import os
import sys

import urlparse,re
import urllib
import datetime
import xbmc, xbmcgui

from core import logger
from core import config
from core import scrapertools
from core.item import Item



DEBUG = True
CHANNELNAME = "sebn"

def isGeneric():
    return True

# Entry point
def mainlist(item):
    logger.info("sebn.main_list")
    itemlist=[]
    


    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 1" , action="PlaySEBN" , url="http://sebn.sc/sebn-1.php",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 2" , action="PlaySEBN" , url="http://sebn.sc/sebn-2.php",thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 3" , action="PlaySEBN" , url="http://sebn.sc/sebn-3.php", ithumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 4" , action="PlaySEBN" , url="http://sebn.sc/sebn-4.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 5" , action="PlaySEBN" , url="http://sebn.sc/sebn-5.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 6" , action="PlaySEBN" , url="http://sebn.sc/sebn-6.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 7" , action="PlaySEBN" , url="http://sebn.sc/sebn-7.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 8" , action="PlaySEBN" , url="http://sebn.sc/sebn-8.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 9" , action="PlaySEBN" , url="http://sebn.sc/sebn-9.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 10" , action="PlaySEBN" , url="http://sebn.sc/sebn-10.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 11" , action="PlaySEBN" , url="http://sebn.sc/sebn-11.php", thumbnail="http://sebn.sc/images/logo.png") )
    itemlist.append( Item(channel=CHANNELNAME, title="SEBN 12" , action="PlaySEBN" , url="http://sebn.sc/sebn-12.php", thumbnail="http://sebn.sc/images/logo.png") )
    

    return itemlist



def PlaySEBN(item):
    
    url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+item.url
    name = item.title
    iconimage = xbmc.getInfoImage("ListItem.Thumb")
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    dp = xbmcgui.DialogProgress()
    dp.create("DutchSportStreams","Please wait")  
    xbmc.Player().play(url, liz, False)
