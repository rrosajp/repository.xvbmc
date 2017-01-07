import sys
import os
import urllib
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import base64


from metahandler import metahandlers

addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))
ddicon = xbmc.translatePath(os.path.join(home, 'icon.png'))
dialog = xbmcgui.Dialog()
addon_handle = int(sys.argv[1])
filminfo = addon.getSetting('enable_meta')


def show_tags():
  xbmcplugin.setContent(addon_handle, 'movies')

  for tag in tags:
    if not tag['icon'].startswith('http'):
        iconPath = os.path.join(home, 'logos', tag['icon'])
    try:
        fanart = tag['fanart']
        if not fanart.startswith('http'):
            fanart = os.path.join(home, 'logos', fanart)
    except: fanart = None        
    li = xbmcgui.ListItem(tag['name'], iconImage=iconPath)
    if fanart: li.setArt({'fanart': fanart})
    url = sys.argv[0] + '?tag=' + str(tag['id'])
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

  xbmcplugin.endOfDirectory(addon_handle)


def show_streams(tag):
  xbmcplugin.setContent(addon_handle, 'movies')
  for stream in streams[str(tag)]:
    iconPath = stream['icon']
    videourl = stream['url']
    if videourl.startswith('aHR'):
        try: videourl = base64.b64decode(videourl)
        except: pass
    name = stream['name']
    year = stream['year']
    blnresolve = stream['resolve']
    try: imdb = stream['imdb']
    except: imdb = ''
    try: tags = stream['tag']
    except: tags = None
    contextMenuItems = []
    backdrop = ''
    folder = False
    if tags:
        videourl = sys.argv[0] + '?tag=' + str(tags)
        folder = True
    elif blnresolve:
        videourl = (sys.argv[0] +
         "?url=" + urllib.quote_plus(videourl) +
         "&tag=resolve" + 
         "&name=" + urllib.quote_plus(name))
    if filminfo == 'true':
        mg = metahandlers.MetaData(tmdb_api_key='f7f51775877e0bb6703520952b3c7840')
        meta = mg.get_meta('movie', name=name, year=year, imdb_id=imdb)
        iconPath = meta['cover_url']
        if iconPath == '':
            iconPath = stream['icon']
            if not iconPath.startswith('http'):
                iconPath = os.path.join(home, 'logos', stream['icon'])          
        filmmeta = meta
        imdbid = meta['imdb_id']
        backdrop = meta['backdrop_url']
        if not imdbid == '' and backdrop == '': backdrop = 'http://films4u.org/imdb/bgs/'+imdbid+'.jpg'
    else:
        name = "%s (%s)" % (name, year)
        filmmeta = { "Title": name }
        backdrop = ''
        if not iconPath.startswith('http'):
            iconPath = os.path.join(home, 'logos', stream['icon'])
    li = xbmcgui.ListItem(name, thumbnailImage=iconPath, iconImage=iconPath)
    li.setInfo(type="Video", infoLabels= filmmeta)
    contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
    li.addContextMenuItems(contextMenuItems, replaceItems=False)
    if not backdrop == '': li.setArt({'fanart': backdrop})
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=videourl, listitem=li, totalItems=len(streams[str(tag)]), isFolder=folder)

  xbmcplugin.endOfDirectory(addon_handle)


def resolve_play(url, name):
    if 'plugin.video.hipevolution' in xbmc.getInfoLabel('Container.PluginName'):
        videourl = None
        if 'youtube' in url:
            ytid = url.split("?v=")[-1].split("/")[-1].split("?")[0].split("&")[0]
            videourl = 'plugin://plugin.video.youtube/play/?video_id=%s' % ytid
        else:
            import urlresolver
            try: videourl = urlresolver.resolve(url)
            except: pass
        if videourl:
            iconimage = xbmc.getInfoImage("ListItem.Thumb")
            listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
            listitem.setInfo('video', {'Title': name})
            xbmc.Player().play(videourl, listitem)
        else:
            notify('Hip-Hop-Evolution','Link is offline')


def notify(header=None, msg='', duration=5000):
    if header is None: header = 'Hip-Hop-Evolution'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, ddicon)
    xbmc.executebuiltin(builtin)


def get_params():
  """
  Retrieves the current existing parameters from XBMC.
  """
  param = []
  paramstring = sys.argv[2]
  if len(paramstring) >= 2:
    params = sys.argv[2]
    cleanedparams = params.replace('?', '')
    if params[len(params) - 1] == '/':
      params = params[0:len(params) - 2]
    pairsofparams = cleanedparams.split('&')
    param = {}
    for i in range(len(pairsofparams)):
      splitparams = {}
      splitparams = pairsofparams[i].split('=')
      if (len(splitparams)) == 2:
        param[splitparams[0]] = splitparams[1]
  return param


def lower_getter(field):
  def _getter(obj):
    return obj[field].lower()

  return _getter


tags = [
  {
    'name': 'Hip Hop Evolution',
    'id': 'LiveTV',
    'icon': 'kidsi.png',
	'fanart': 'fanart.png'
  }
]


LiveTV = [{
   'name': 'Hip Hop Evolution - Trailer',
  'year': '2016',
  'url': 'http://allvid.ch/ldxrrurtxj4y',
  'icon': '',
  'resolve': True,
  'disabled': False
}, {
  'name': 'Hip Hop Evolution - S01E01 The Foundation',
  'year': '2016',
  'url': 'http://allvid.ch/8wazlsl3yok0',
  'icon': '',
  'resolve': True,
  'disabled': False
}, {
  'name': 'Hip Hop Evolution - S01E02 The Underground to the Mainstream',
  'year': '2016',
  'url': 'http://allvid.ch/yip76esb1cgf',
  'icon': '',
  'resolve': True,
  'disabled': False
}, {
  'name': 'Hip Hop Evolution - S01E03 The New Guard',
  'year': '2006',
  'url': 'http://allvid.ch/63vrqui2i2dg',
  'icon': '',
  'resolve': True,
  'disabled': False
}, {
  'name': 'Hip Hop Evolution - S01E04 The Birth of Gangsta Rap',
  'year': '2016',
  'url': 'http://allvid.ch/09ci3nkwwlv4',
  'icon': '',
  'resolve': True,
  'disabled': False
}]









streams = {
  'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  
  
  # 'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  # 'Movies': sorted(Movies, key=lower_getter('name')),
}


PARAMS = get_params()
TAG = None
NAME = None
URL = None


try:
  TAG = PARAMS['tag']
except:
  pass
try: URL = urllib.unquote_plus(PARAMS["url"])
except: pass
try: NAME = urllib.unquote_plus(PARAMS["name"])
except: pass


if TAG == None:
  if xbmc.getCondVisibility('System.HasAddon(script.module.urlresolver)'):
    show_tags()
elif TAG == 'resolve':
  resolve_play(URL, NAME)
else:
  show_streams(TAG)

