# -*- coding: utf-8 -*-
#------------------------------------------------------------
# channels foxsport
#---------------------------------------------------------------------------
import os
import sys

import urlparse,re
import urllib
import datetime


from core import logger
from core import config
from core import scrapertools
from core.item import Item

import time, datetime
from datetime import date, datetime, timedelta

import youtube_channel

try:
	import json
except:
	import simplejson as json



DEBUG = True
CHANNELNAME = "telesport"

telesport='https://www.telesport.nl/overzicht/video'

def isGeneric():
    return True



# Entry point
def mainlist(item):
    logger.info("telesport.main_list")
    dialog_notification("Telesport", "Playlist is loading")
    itemlist=[]
    data_1 = scrapertools.cachePage(telesport)
    a_regex = 'href=\"/video(.*?)\"'
    video_url = re.compile(a_regex, re.DOTALL).findall(data_1)
    for items in video_url:
        url= 'https://www.telesport.nl/video'+items
        json_url = get_api(url)
        data = scrapertools.cachePage(json_url)
        json_data = json.loads(data)
        for items in json_data["items"]:
            title= items["title"]
            poster= "http:"+items["poster"]
            prov= items["locations"]["adaptive"][1]["src"]
            itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]"+title+"[/COLOR][/B]" , action="play" , url=prov,thumbnail=poster,folder=True) )
    
    return itemlist



def get_api(url):
    #print url
    data= scrapertools.cachePage(url)
    a_regex = '<iframe src=\"//content.tmgvideo.nl(.*?)\"'
    frame_url = re.compile(a_regex, re.DOTALL).findall(data)
    for url1 in frame_url:
        #print url1
        url_b = "http://content.tmgvideo.nl"+url1
        data_b = scrapertools.cachePage(url_b)
        #print data_b
        b_regex='playlist: \"(.*?)\"'
        playlists = re.compile(b_regex, re.DOTALL).findall(data_b)
        for playlist in playlists:
            return playlist




def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))





def dialog_input(default="", heading="", hidden=False):
    import xbmc
    keyboard = xbmc.Keyboard(default, heading, hidden)
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        return keyboard.getText()
    else:
        return ""

def dialog_notification(heading, message, icon=0, time=5000, sound=True):
    import xbmcgui
    dialog = xbmcgui.Dialog()
    l_icono=(xbmcgui.NOTIFICATION_INFO , xbmcgui.NOTIFICATION_WARNING, xbmcgui.NOTIFICATION_ERROR)
    dialog.notification (heading, message, l_icono[icon], time, sound)


# Show all YouTube playlists for the selected channel
def youtube_playlists(item):
    return youtube_channel.playlists(item,item.url)



def play(item):
    itemlist = []
    itemlist.append([item.title, item.url])
    return itemlist
