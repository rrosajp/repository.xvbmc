import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3
import yt

def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)

def Resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 

def Main():
    utils.addDir('Highlights & Full Matches','http://www.fullmatchesandshows.com/',302,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg') 
    #utils.addDir('Fixtures','http://liveonsat.com/quickindex.html',302,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg') 
    #utils.addDir('League Tables','http://www.sportinglife.com/football/tables',302,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def ListHighlights(url):
    utils.addDir('Latest','http://www.fullmatchesandshows.com/',302,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Shows','http://www.fullmatchesandshows.com/category/show/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    #utils.addDir('Search','http://www.fullmatchesandshows.com/?s=',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Premier League','http://www.fullmatchesandshows.com/category/premier-league/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('La Liga','http://www.fullmatchesandshows.com/category/la-liga/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Bundesliga','http://www.fullmatchesandshows.com/category/bundesliga/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Champions League','http://www.fullmatchesandshows.com/category/champions-league/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Europa League','http://www.fullmatchesandshows.com/category/europa-league/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Serie A','http://www.fullmatchesandshows.com/category/serie-a/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Eredivisie','http://www.fullmatchesandshows.com/category/eredivisie/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Ligue 1','http://www.fullmatchesandshows.com/category/ligue-1/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('MLS','http://www.fullmatchesandshows.com/category/mls/',303,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/icon.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListLatest(url):
    listhtml = utils.getHtml(url,url)
    match = re.compile('<div class="td-block-span4">.*?href="(.*?)" rel="bookmark" title="(.*?)".*?src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, name, img in match:
        name = utils.cleantext(name)
        utils.addDir(name, videopage, 304, img, '', fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListLElse(url):
    listhtml = utils.getHtml(url,url)
    pageview = re.compile('<!doctype html >(.*?)<span class="current">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"', re.IGNORECASE | re.DOTALL).findall(pageview)
    for videopage, name, img in match:
        name = utils.cleantext(name)
        utils.addDir(name, videopage, 304, img, '', fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    try:
        next = re.compile('<span class="current">.</span><a href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        utils.addDir('Volgende Pagina', next, 303,'', '')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListStream(url):
    utils.addDownLink('Extended Highlights',url,305,'','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    listhtml = utils.getHtml(url,url)
    match = re.compile('<link href=".+?" rel="stylesheet" type="text/css"><li tabindex="0" class="button_style" id=".+?"><a href="(.+?)"><div class="acp_title">(.+?)</div></a></li>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for url2,name in match:
        name = (name).replace('HL English','English Highlights')
        utils.addDownLink(name, url2, 305, '', '', fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    

def get_PLAYlink(url):
    listhtml = utils.getHtml(url,url)
    match_youtube = re.compile('<iframe width="560" height="315" src="https://www.youtube.com/embed/(.+?)" frameborder="0" allowfullscreen>').findall(listhtml)
    for url in match_youtube:
        yt.PlayVideo(url)
    match = re.compile('<script data-config="(.+?)" data-height').findall(listhtml)
    for playlink in match:
        if 'div' in playlink:
            pass
        else:
            Playlink = (playlink).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
            Resolve('http:'+Playlink)