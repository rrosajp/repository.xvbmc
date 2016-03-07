import sys, urllib2, urllib
import xbmcgui
import xbmcplugin, xbmcaddon
import urlparse
import paths, tvguide

import socket, sys, os

from lib.streams import *
from lib.utils import *

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

pDialog = xbmcgui.DialogProgress()
_PERCENT_ = 0
progIncrease = 19

xbmcplugin.setContent(addon_handle, 'movies')

addon = xbmcaddon.Addon('plugin.video.nlsports')
newFeatures = addon.getSetting('newFeatures')

def addSubMenu(internal, readable):
    print 'adding ' + internal
    url = build_url({'site': internal})
    icon = xbmcutil.getIcon(internal)
    li = xbmcgui.ListItem(label=readable, iconImage=icon, thumbnailImage=icon)
    fanart = xbmcutil.getFanart(internal)
    li.setProperty('fanart_image',fanart)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

def mainMenu():
    addSubMenu('bvls','BVLS Streams')
    #xbmcutil.addMenuItem('Sport1 Voetbal SD','http://ziggo.cdn.sport1.triple-it.nl/sport1voetbalhd.isml/QualityLevels(696000)/manifest(format=m3u8-aapl).m3u8','true','http://www.lyngsat-logo.com/hires/ss/sport1_nl_voetbal_hd.png','http://www.voetbal-gokken.nl/wp-content/uploads/2013/01/allianz-arena.jpg')
    #xbmcutil.addMenuItem('Sport1 Voetbal HD','http://ziggo.cdn.sport1.triple-it.nl/sport1voetbalhd.isml/QualityLevels(2896000)/manifest(format=m3u8-aapl).m3u8','true','http://www.lyngsat-logo.com/hires/ss/sport1_nl_voetbal_hd.png','http://www.voetbal-gokken.nl/wp-content/uploads/2013/01/allianz-arena.jpg')
    if geo.returnCountyCode() == "NL":
        addSubMenu('sport365','Sport365')
    
    addSubMenu('iptv','[COLOR gold]IP TV[/COLOR]')
    #addDummyItem('--- UNSUPPORTED ---')
    #addSubMenu('janlul', '[COLOR grey]JanLul Streams[/COLOR]')
    #addSubMenu('daz','[COLOR grey]DazSports Streams[/COLOR]')
    #addSubMenu('13stream', '[COLOR grey]13th Stream[/COLOR]')
    #addSubMenu('lmmg','[COLOR grey]LMMG Streams[/COLOR]')
    #addSubMenu('mdhzk','[COLOR grey]MDHZK Streams[/COLOR]')
    #addSubMenu('spst','[COLOR grey]Sports-streams[/COLOR]')
    #addSubMenu('sotd','[COLOR grey]Stream of the Day[/COLOR]')
#    addSubMenu('pole','Poleposition')
    #if newFeatures == "true":
    #    addSubMenu('sotd','Stream of the Day - [COLOR red]Unsupported[/COLOR]')
#    addSubMenu('tvguide', 'TV Gids')
    addDummyItem('')
    #addDummyItem('[COLOR yellow]Bedank de streamers, SMS: \'DONATE STREAM\' naar 7733 (E 3,00 p/b)[/COLOR]')
    addDummyItem('[COLOR green]Stream online[/COLOR]')
    addDummyItem('[COLOR red]Stream offline[/COLOR]')
    xbmcplugin.endOfDirectory(addon_handle)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)
    
def addDummyItem(labelString, icon=False, iconName = '', fanart=False, fanartName=''):
    if icon:
        iconimg = xbmcutil.getIcon(iconName)
        li = xbmcgui.ListItem(label=labelString, iconImage=iconimg, thumbnailImage=iconimg)
    else:
        li = xbmcgui.ListItem(label=labelString)

    li.setProperty('IsPlayable','false')
    if fanart:
        fanartimg = xbmcutil.getFanart(fanartName)
        li.setProperty('fanart_image',fanartimg)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url='plugin://plugin.video.nlsports/none', listitem=li)

argSite = args.get('site', None)
playUrl = args.get('play', None)
p2pMode = args.get('mode', None)
streamName = args.get('streamName', None)

if argSite is None:
    if playUrl is None :
        mainMenu()
    else :
        playUrl[0] = playUrl[0].decode("base64")
        if p2pMode is not None :
            playUrl[0] = str(playUrl[0]) + "&mode=" + str(p2pMode[0])
        while xbmc.Player().isPlaying():
            xbmc.Player().stop()
            xbmc.sleep(5)
        pl=xbmc.PlayList(1)
        pl.clear()
        iconimg = os.path.join(paths.rootDir, 'icon.png')
        print str(streamName[0])
        li = xbmcgui.ListItem('NL Sports - '+str(streamName[0]), iconImage=iconimg, thumbnailImage=iconimg)
        li.setProperty('IsPlayable', 'true')
        li.setProperty('fanart_image', os.path.join(paths.rootDir, 'fanart.jpg'))
        xbmc.PlayList(1).add(str(playUrl[0]), li)
        xbmc.Player().play(pl)
else:
    site = argSite[0]
    pDialog.create('NL Sports', 'Laden van streams...')
    if site == 'bvls': #bvls2016.sc
        bvls.addStreams()
    elif site == 'iptv':
        iptv.addStreams()
    elif site == 'sport365':
        sport365.addStreams()
    else:
        mainMenu()

    xbmcplugin.endOfDirectory(addon_handle)
