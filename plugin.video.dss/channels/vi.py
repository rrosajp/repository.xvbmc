# -*- coding: utf-8 -*-
#------------------------------------------------------------
# channels vi
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
CHANNELNAME = "vi"

vi_home = 'http://apiv2.voetbalinside.livewallcampaigns.com/home/?page=1'
vi_day ='http://apiv2.voetbalinside.livewallcampaigns.com/top?page=1&type=day'
vi_week ='http://apiv2.voetbalinside.livewallcampaigns.com/top?page=1&type=week'
vi_month ='http://apiv2.voetbalinside.livewallcampaigns.com/top?page=1&type=month'
vi_classics ='http://apiv2.voetbalinside.livewallcampaigns.com/top?page=1&type=classics'
vi_search ='http://apiv2.voetbalinside.livewallcampaigns.com/search/?page=1&searchTerm='
vi_video = 'http://www.rtl.nl/system/s4m/vfd/version=2/d=iphone/fmt=adaptive/fun=abstract/'

def isGeneric():
    return True

# Entry point
def mainlist(item):
    
    logger.info("ziggosport.main_list")
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Day[/COLOR][/B]" , action="vi_read" , url='&type=day',channels='top',page=1,thumbnail="http://i.imgur.com/qsveenv.jpgg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Week[/COLOR][/B]" , action="vi_read" , url='&type=week',channels='top',page=1,thumbnail="http://i.imgur.com/qsveenv.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Month[/COLOR][/B]" , action="vi_read" , url='&type=month',channels='top',page=1,thumbnail="http://i.imgur.com/qsveenv.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Classics[/COLOR][/B]" , action="vi_read" , url='&type=classics',channels='top',page=1,thumbnail="http://i.imgur.com/qsveenv.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]VI Youtube[/COLOR][/B]" , action="youtube_playlists" , url="VITVRTL",thumbnail="http://i.imgur.com/qsveenv.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Zoeken[/COLOR][/B]" , action="vi_search" ,query=None, url='&searchTerm=',channels='search',page=1,thumbnail="http://i.imgur.com/qsveenv.jpg",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR red]---- UITGELICHT ----[/COLOR][/B]" ) )
    #vi_read(Item(url='&type=',page=1,channels='home'))
    try:
	livejson = scrapertools.cachePage('http://apiv2.voetbalinside.livewallcampaigns.com/home/?page=1')
	livejson = json.loads(livejson, encoding='utf-8')
	for items in livejson:
	    name = str(items)
	    for items in livejson[name]["items"]:
		title = items["title"]
		title = title.encode('utf-8')
		title = removeNonAscii(title)
		timeDisplay = items["timeDisplay"]
		timeDisplay =	timeDisplay.rstrip(timeDisplay[-6:])
		if "videoUuid" in items:
		    videoUuid = items["videoUuid"]
		    image = items["image"]
		    image = 'http://rtl.lwcdn.nl/imageScaled/?site=voetbalinside&file='+image+'&w=500.0&h=500.0&cropped=1'
		    url = get_video('http://www.rtl.nl/system/s4m/vfd/version=2/d=iphone/fmt=adaptive/fun=abstract/uuid='+videoUuid)
		    if url is not None :
                        itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR blue]"+title+"[/COLOR][/B]" , action="play" , url=url,thumbnail=image,folder=True) )
    except:
        pass
    return itemlist
    

def vi_search(item):
    page = item.page
    itemlist=[]
    if item.query:
        query=item.query
    else:
        query = dialog_input()
    query = query.encode('utf-8')
    query = removeNonAscii(query)
    try:
	livejson = scrapertools.cachePage('http://apiv2.voetbalinside.livewallcampaigns.com/search/?page='+str(page)+'&searchTerm='+query)
	livejson = json.loads(livejson, encoding='utf-8')
	for items in livejson:
	    name = str(items)
	    for items in livejson[name]["items"]:
		title = items["title"]
		title = title.encode('utf-8')
		title = removeNonAscii(title)
		timeDisplay = items["timeDisplay"]
		timeDisplay =	timeDisplay.rstrip(timeDisplay[-6:])
		if "videoUuid" in items:
		    videoUuid = items["videoUuid"]
		    image = items["image"]
		    image = 'http://rtl.lwcdn.nl/imageScaled/?site=voetbalinside&file='+image+'&w=500.0&h=500.0&cropped=1'
		    url = get_video('http://www.rtl.nl/system/s4m/vfd/version=2/d=iphone/fmt=adaptive/fun=abstract/uuid='+videoUuid)
		    if url is not None :
                        itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR blue]"+title+"[/COLOR][/B]" , action="play" , url=url,thumbnail=image,folder=True) )
    except:
        pass
    
    try:
	page =page+1
	livejson = scrapertools.cachePage('http://apiv2.voetbalinside.livewallcampaigns.com/search/?page='+str(page)+'&searchTerm='+query)
	if not '"items":false' in livejson:
	    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Previous Page[/COLOR][/B]" ,query=query, action="vi_search" ,page=page,folder=True) )

    except:
	pass
    return itemlist
        
def vi_read(item):
    url = item.url
    channel = item.channels
    page = item.page
    itemlist=[]
    try:
	urldir=url
	livejson = scrapertools.cachePage('http://apiv2.voetbalinside.livewallcampaigns.com/'+str(channel)+'?page='+str(page)+url)
	livejson = json.loads(livejson, encoding='utf-8')
	for items in livejson:
	    name = str(items)
	    for items in livejson[name]["items"]:
		title = items["title"]
		title = title.encode('utf-8')
		title = removeNonAscii(title)
		timeDisplay = items["timeDisplay"]
		timeDisplay =	timeDisplay.rstrip(timeDisplay[-6:])
		if "videoUuid" in items:
		    videoUuid = items["videoUuid"]
		    image = items["image"]
		    image = 'http://rtl.lwcdn.nl/imageScaled/?site=voetbalinside&file='+image+'&w=500.0&h=500.0&cropped=1'
		    url = get_video('http://www.rtl.nl/system/s4m/vfd/version=2/d=iphone/fmt=adaptive/fun=abstract/uuid='+videoUuid)
		    if url is not None :
                        itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]"+title+"[/COLOR][/B]" , action="play" , url=url,thumbnail=image,folder=True) )
    except:
	pass
    if not "home" in channel:
	try:
	    page =page+1
	    livejson = scrapertools.cachePage('http://apiv2.voetbalinside.livewallcampaigns.com/'+str(channel)+'?page='+str(page)+urldir)
	    if not '"items":false' in livejson:
		itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Previous Page[/COLOR][/B]" , action="vi_read" , url=urldir,page=page,channels='top',thumbnail="https://yt3.ggpht.com/-u4FRgUny9UU/AAAAAAAAAAI/AAAAAAAAAAA/Pi2IJs99mpA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",folder=True) )
	except:
            pass
    return itemlist

def get_video(url):
	try:
		livejson = scrapertools.cachePage(url)
		livejson = json.loads(livejson, encoding='utf-8')
		videohost = livejson["meta"]["videohost"]
		material = livejson["material"]
		for items in material:
			videopath = items["videopath"]
			url = videohost+videopath
			return url
	except:
		url = None
		return url




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
