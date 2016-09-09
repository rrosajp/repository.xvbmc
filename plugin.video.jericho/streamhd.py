import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon
from datetime import datetime, timedelta
from time import time

import utils

def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)

def List():
    listhtml = utils.getHtml2('http://www.streamhd.eu/')
    match = re.compile('eventsmall"> (.*?) </span>.*?alt=".*?"> (.*?)</a>.*?">.*?hidden-xs hidden-sm.*?> (.*?) </a>.*?href="(.*?)"> (.*?) </a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for tijd, sport, competitie, videopage, wedstrijd in match:
        competitie = striphtml(competitie)
        try:
            dt = datetime.strptime(tijd, "%H:%M")
            tijd = str(dt.hour+1).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
        except :
            pass        
        name = tijd + ' - ' + sport + ': ' + competitie + ' - ' + wedstrijd
        videopage = "http://www.streamhd.eu" + videopage
        utils.addDownLink(name, videopage, 243, '', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml(url,'')
    iframe = re.compile('name="videoiframe" src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    iframe2 = utils.getHtml(iframe,'')
    video = re.compile('iframe src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(iframe2)[0]
    videocontent = utils.getHtml(video, '')
    match = re.compile('file: "(.*?)"', re.IGNORECASE | re.DOTALL).findall(videocontent)[0]
    if match:
        videourl = match
        videourl = videourl.replace("&amp;","&")
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Music'})
        listitem.setProperty("IsPlayable","true")
        if int(sys.argv[1]) == -1:
            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            pl.clear()
            pl.add(videourl, listitem)
            xbmc.Player().play(pl)
        else:
            listitem.setPath(str(videourl))
            xbmcplugin.setResolvedUrl(utils.addon_handle, True, listitem)
    else:
        utils.notify('','Couldn\'t find a playable video link')