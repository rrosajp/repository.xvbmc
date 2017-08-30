# -*- coding: utf-8 -*-
#------------------------------------------------------------
# channels ziggosport
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



try:
	import json
except:
	import simplejson as json



DEBUG = True
CHANNELNAME = "ziggosport"

ziggosearch = 'http://go.ziggosporttotaal.nl/apiv2/video?appVersion=2.2.0&device=iphone&search='
autosport ='http://go.ziggosporttotaal.nl/apiv2/video?appVersion=2.2.0&category=autosport&device=iphone&order=recent'
golf ='http://go.ziggosporttotaal.nl/apiv2/video?appVersion=2.2.0&category=golf&device=iphone&order=recent'
other ='http://go.ziggosporttotaal.nl/apiv2/video?appVersion=2.2.0&category=other&device=iphone&order=recent'
soccer ='http://go.ziggosporttotaal.nl/apiv2/video?appVersion=2.2.0&category=soccer&device=iphone&order=recent'
tennis ='http://go.ziggosporttotaal.nl/apiv2/video?appVersion=2.2.0&category=tennis&device=iphone&order=recent'

def isGeneric():
    return True

# Entry point
def mainlist(item):
    logger.info("ziggosport.main_list")
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Voetbal[/COLOR][/B]" , action="ziggoread" , url=soccer,thumbnail="https://yt3.ggpht.com/-u4FRgUny9UU/AAAAAAAAAAI/AAAAAAAAAAA/Pi2IJs99mpA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Racing[/COLOR][/B]" , action="ziggoread" , url=autosport,thumbnail="https://yt3.ggpht.com/-u4FRgUny9UU/AAAAAAAAAAI/AAAAAAAAAAA/Pi2IJs99mpA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Golf[/COLOR][/B]" , action="ziggoread" , url=golf,thumbnail="https://yt3.ggpht.com/-u4FRgUny9UU/AAAAAAAAAAI/AAAAAAAAAAA/Pi2IJs99mpA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Tennis[/COLOR][/B]" , action="ziggoread" , url=tennis,thumbnail="https://yt3.ggpht.com/-u4FRgUny9UU/AAAAAAAAAAI/AAAAAAAAAAA/Pi2IJs99mpA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Meer Sport[/COLOR][/B]" , action="ziggoread" , url=other,thumbnail="https://yt3.ggpht.com/-u4FRgUny9UU/AAAAAAAAAAI/AAAAAAAAAAA/Pi2IJs99mpA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Zoeken[/COLOR][/B]" , action="ziggo_search" , url="",thumbnail="https://yt3.ggpht.com/-u4FRgUny9UU/AAAAAAAAAAI/AAAAAAAAAAA/Pi2IJs99mpA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",folder=True) )
    return itemlist


def ziggoread(item):
    itemlist=[]
    livejson = scrapertools.cachePage(item.url)
    livejson = json.loads(livejson, encoding='utf-8')
    for items in livejson["responseObject"]["mediaItems"]:
	imported = items["imported"]
	imported = str(datetime.fromtimestamp(imported))[0:10]
	title = items["title"]
	title = title.encode('utf-8')
	title = removeNonAscii(title)
	image = items["imageUrl"]
	url = items["ipadHigh"]
	if url == None:
	    url = items["iphoneHigh"]
            if url == None:
                url = items["iphoneLow"]
	duration = items["duration"]
	duration = str(timedelta(seconds=duration))
	if duration.startswith("0:"):
	    duration =  duration[2:10]
        duration=  '['+duration+']'
	if url is not None :
            itemlist.append( Item(channel=CHANNELNAME, title='[COLOR darkorange]'+duration+'[/COLOR][B][COLOR white]'+title+'[/COLOR][/B] ('+imported+')', action="play" , url=url,thumbnail=image,folder=True) )
    return itemlist


def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))


def ziggo_search(item):
    itemlist=[]
    query = dialog_input()
    query = query.encode('utf-8')
    query = removeNonAscii(query)
    url = ziggosearch+query
    try:
        livejson = scrapertools.cachePage(url)
        livejson = json.loads(livejson, encoding='utf-8')
        for items in livejson["responseObject"]["mediaItems"]:
            imported = items["imported"]
            imported = str(datetime.fromtimestamp(imported))[0:10]
            title = items["title"]
            title = title.encode('utf-8')
            title = removeNonAscii(title)
            image = items["imageUrl"]
            url = items["ipadHigh"]
            if url == None:
                url = items["iphoneHigh"]
                if url == None:
                    url = items["iphoneLow"]
            duration = items["duration"]
            duration = str(timedelta(seconds=duration))
            if duration.startswith("0:"):
                duration =  duration[2:10]
            duration=  '['+duration+']'
            if url is not None :
                itemlist.append( Item(channel=CHANNELNAME, title='[COLOR darkorange]'+duration+'[/COLOR][B][COLOR white]'+title+'[/COLOR][/B] ('+imported+')', action="play" , url=url,thumbnail=image,folder=True) )
    except:
        pass
    return itemlist



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


def play(item):
    itemlist = []
    itemlist.append([item.title, item.url])
    return itemlist
