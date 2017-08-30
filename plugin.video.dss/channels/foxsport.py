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
CHANNELNAME = "foxsport"

fox_cat = 'http://mapi.foxsports.nl/api/mobile/v1/articles/category/'

def isGeneric():
    return True

# Entry point
def mainlist(item):
    logger.info("foxsport.main_list")
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Uitzending Gemist[/COLOR][/B]" , action="Uitzending_Gemist" , url="",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Video\'s[/COLOR][/B]" , action="Video_s" , url="",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Kompetitie[/COLOR][/B]" , action="Competition_Main" , url="",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Voetbal[/COLOR][/B]" , action="foxmore" , url="http://mapi.foxsports.nl/api/mobile/v2/soccer/articles",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Tennis[/COLOR][/B]" , action="foxmore" , url="http://mapi.foxsports.nl/api/mobile/v1/tennis/articles",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Meer Sports[/COLOR][/B]" , action="foxmore" , url="http://mapi.foxsports.nl/api/mobile/v1/articles/moresports",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Fox Sports Youtube[/COLOR][/B]" , action="youtube_playlists" , url="EredivisieLive",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Zoeken[/COLOR][/B]" , action="search_fox" , url="",thumbnail="",folder=True) )
    return itemlist

def Uitzending_Gemist(item):
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Fox Sports DOC[/COLOR][/B]" , action="foxread" , url="115",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Club TV[/COLOR][/B]" , action="foxread" , url="116",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]De Tafel Van Kees[/COLOR][/B]" , action="foxread" , url="117",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Fox Sports Vandaag[/COLOR][/B]" , action="foxread" , url="118",thumbnail="",folder=True) )
    return itemlist

def Video_s(item):
    itemlist=[]
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Samenvattingen[/COLOR][/B]" , action="foxread" , url="1",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Doelpunten[/COLOR][/B]" , action="foxread" , url="2",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Interviews[/COLOR][/B]" , action="foxread" , url="3",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Aanbevolen[/COLOR][/B]" , action="foxread" , url="4",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Meest Bekeken[/COLOR][/B]" , action="foxread" , url="5",thumbnail="",folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="[B][COLOR white]Meer Video[/COLOR][/B]" , action="foxread" , url="6",thumbnail="",folder=True) )
    return itemlist


def Competition_Main(item):
    itemlist=[]
    livejson = scrapertools.cachePage('http://mapi.foxsports.nl/api/mobile/v1/soccer/competitions')
    livejson = json.loads(livejson)
    for items in livejson["national"]:
	ID = items["id"]
	url = 'http://mapi.foxsports.nl/api/mobile/v2/soccer/articles/'+str(ID)
	title = items["name"]
	title = title.encode('utf-8')
	title = removeNonAscii(title)
	icon = items["icon"]
	itemlist.append( Item(channel=CHANNELNAME, title='[B][COLOR white]'+title+'[/COLOR][/B]' , action="foxmore" , url=url,thumbnail=icon,folder=True) )
    for items in livejson["international"]:
	ID = items["id"]
	url = 'http://mapi.foxsports.nl/api/mobile/v2/soccer/articles/'+str(ID)
	title = items["name"]
	title = title.encode('utf-8')
	title = removeNonAscii(title)
	icon = items["icon"]
	itemlist.append( Item(channel=CHANNELNAME, title='[B][COLOR white]'+title+'[/COLOR][/B]' , action="foxmore" , url=url,thumbnail=icon,folder=True) )
    return itemlist


def foxmore(item):
    itemlist=[]
    livejson = scrapertools.cachePage(item.url)
    livejson = json.loads(livejson, encoding='utf-8')
    for items in livejson["other_articles"]:
	title = items["title"]
	title = title.encode('utf-8')
	title = removeNonAscii(title)
	image = items["image"]
	image = image.replace('{size}','300x184')
	last_modified = items["last_modified"][0:10]
	if "video" in items:
	    video_id = items["video"]["diva_settings"]["video_id"]
	    url = get_video(video_id)
	    if url is not None :
		itemlist.append( Item(channel=CHANNELNAME, title='[B][COLOR white]'+title+'[/COLOR][/B]  [COLOR darkorange]('+last_modified+')[/COLOR]' , action="play" , url=url,thumbnail=image,folder=True) )

    for items in livejson["hero_image_articles"]:
	title = items["title"]
	title = title.encode('utf-8')
	title = removeNonAscii(title)
	image = items["image"]
	image = image.replace('{size}','300x184')
	last_modified = items["last_modified"][0:10]
	if "video" in items:
	    video_id = items["video"]["diva_settings"]["video_id"]
	    url = get_video(video_id)
	    if url is not None :
                itemlist.append( Item(channel=CHANNELNAME, title='[B][COLOR white]'+title+'[/COLOR][/B]  [COLOR darkorange]('+last_modified+')[/COLOR]' , action="play" , url=url,thumbnail=image,folder=True) )
    return itemlist



def foxread(item):
    itemlist=[]
    livejson = scrapertools.cachePage(fox_cat+item.url)
    livejson = json.loads(livejson)
    for items in livejson:
	title = items["title"]
	title = title.encode('utf-8')
	title = removeNonAscii(title)
	image = items["image"]
	last_modified = items["last_modified"][0:10]
	video_id = items["video"]["diva_settings"]["video_id"]
	image = image.replace('{size}','300x184')
	url = get_video(video_id)
	if url is not None:   
            itemlist.append( Item(channel=CHANNELNAME, title='[B][COLOR white]'+title+'[/COLOR] [/B] ('+last_modified+')' , action="play" , url=url,thumbnail=image,folder=True) )
    return itemlist


def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))


def get_video(id):
	try:
		xmlLocation = 'http://www.foxsports.nl/divadata/Output/VideoData/'+id+'.xml'
		xml_regex = '<videoSource format="HLS" offset=".*?">\s*<DVRType>.*?</DVRType>\s*<uri>(.*?)</uri>'
		content = scrapertools.cachePage(xmlLocation)
		url = re.compile(xml_regex, re.DOTALL).findall(content)
		for video in url:
			return video
	except:
		url = None
		return url

def search_fox(item):
    itemlist=[]
    query = dialog_input()
    query = query.encode('utf-8')
    query = removeNonAscii(query)
    livejson = scrapertools.cachePage('http://mapi.foxsports.nl/api/mobile/v1/search/'+query)
    livejson = json.loads(livejson)
    for items in livejson:
	items = items["object"]
	title = items["title"]
	title = title.encode('utf-8')
	title = removeNonAscii(title)
	image = items["image"]
	image = image.replace('{size}','Editorial')
	imported = items["date"]
	imported = str(datetime.fromtimestamp(imported))
	imported = imported[0:10]
	if "video" in items:
	    video_id = items["video"]["diva_settings"]["video_id"]
	    url = get_video(video_id)
	    if url is not None :
		itemlist.append( Item(channel=CHANNELNAME, title='[B][COLOR white]'+title+'[/COLOR] [/B] ('+imported+')' , action="play" , url=url,thumbnail=image) )
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


# Show all YouTube playlists for the selected channel
def youtube_playlists(item):
    return youtube_channel.playlists(item,item.url)



def play(item):
    itemlist = []
    itemlist.append([item.title, item.url])
    return itemlist
