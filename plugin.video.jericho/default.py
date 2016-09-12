import urllib
import urllib2
import re
import os
import sys
import base64
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
import plugintools
import urlparse
import httplib
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from time import time
from lib.utils import *
from addon.common.net import Net
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
try:
    import json
except:
    import simplejson as json
import time
import random
import utils, xite, foxsports, ziggosporttotaal, slamfm40, streamhd, Hesgoals, stream2watch, livetvru, fromhot, livefootballvideohighlights, livefootballvideo, sportp2p, showsporttv, hdfree, mamahd, Sportstream365, woopio, footlive

xbmcplugin.setContent(utils.addon_handle, 'movies')
addon = xbmcaddon.Addon(id=utils.__scriptid__)

progress = utils.progress
dialog = utils.dialog

imgDir = utils.imgDir
rootDir = utils.rootDir





net = Net(user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36')
headers = {
    'Accept'    :   'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

resolve_url=['180upload.com', 'allmyvideos.net', 'bestreams.net', 'clicknupload.com', 'cloudzilla.to', 'movshare.net', 'novamov.com', 'nowvideo.sx', 'videoweed.es', 'daclips.in', 'datemule.com', 'fastvideo.in', 'faststream.in', 'filehoot.com', 'filenuke.com', 'sharesix.com', 'docs.google.com', 'plus.google.com', 'picasaweb.google.com', 'gorillavid.com', 'gorillavid.in', 'grifthost.com', 'hugefiles.net', 'ipithos.to', 'ishared.eu', 'kingfiles.net', 'mail.ru', 'my.mail.ru', 'videoapi.my.mail.ru', 'mightyupload.com', 'mooshare.biz', 'movdivx.com', 'movpod.net', 'movpod.in', 'movreel.com', 'mrfile.me', 'nosvideo.com', 'openload.io', 'played.to', 'bitshare.com', 'filefactory.com', 'k2s.cc', 'oboom.com', 'rapidgator.net', 'uploaded.net', 'primeshare.tv', 'bitshare.com', 'filefactory.com', 'k2s.cc', 'oboom.com', 'rapidgator.net', 'uploaded.net', 'sharerepo.com', 'stagevu.com', 'streamcloud.eu', 'streamin.to', 'thefile.me', 'thevideo.me', 'tusfiles.net', 'uploadc.com', 'zalaa.com', 'uploadrocket.net', 'uptobox.com', 'v-vids.com', 'veehd.com', 'vidbull.com', 'videomega.tv', 'vidplay.net', 'vidspot.net', 'vidto.me', 'vidzi.tv', 'vimeo.com', 'vk.com', 'vodlocker.com', 'xfileload.com', 'xvidstage.com', 'zettahost.tv']
g_ignoreSetResolved=['plugin.video.dramasonline','plugin.video.f4mTester','plugin.video.shahidmbcnet','plugin.video.SportsDevil','plugin.stream.vaughnlive.tv','plugin.video.ZemTV-shani']

class NoRedirection(urllib2.HTTPErrorProcessor):
   def http_response(self, request, response):
       return response
   https_response = http_response

JerichoBase2  ='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2plcmljaG8tMjAxNi9KZXJpY2hvL21hc3Rlci9YTUwvaW5kZXgyLnhtbA=='
#BvlsBase  ='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2plcmljaG8tMjAxNi9KZXJpY2hvL21hc3Rlci9YTUwvdm9ldGJhbC54bWw='
MusicBase  ='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2plcmljaG8tMjAxNi9KZXJpY2hvL21hc3Rlci9YTUwvbXV6aWVrLnhtbA=='



#sourceSitebvls = 'http://www.bvls2016.sc/'   

addon = xbmcaddon.Addon('plugin.video.jericho')
addon_version = addon.getAddonInfo('version')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
favorites = os.path.join(profile, 'favorites')
history = os.path.join(profile, 'history')

if not os.path.exists(profile):
    os.makedirs(profile)

REV = os.path.join(profile, 'list_revision')
icon = os.path.join(home, 'icon.png')
FANART = os.path.join(home, 'fanart.jpg')
source_file = os.path.join(profile, 'source_file')
functions_dir = profile

debug = addon.getSetting('debug')
if os.path.exists(favorites):
    FAV = open(favorites).read()
else: FAV = []
if os.path.exists(source_file):
    SOURCES = open(source_file).read()
else: SOURCES = []

###
API_URL = 'http://ida.omroep.nl/aapi/?stream='
BASE_URL = 'http://livestreams.omroep.nl/'
#USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25'
REF_URL = 'http://www.npo.nl'
TOKEN_URL = 'http://ida.omroep.nl/npoplayer/i.js'

def Colored(text = '', colorid = '', isBold = False):
    if colorid == 'ZM':
        color = 'FF11b500'
    elif colorid == 'EB':
        color = 'FFe37101'
    elif colorid == 'bold':
        return '[B]' + text + '[/B]'
    else:
        color = colorid
         
    if isBold:
        text = '[B]' + text + '[/B]'
    return '[COLOR ' + color + ']' + text + '[/COLOR]' 

def AddSports365Channels(url=None):
    errored=True
    import live365
    addDir(Colored("Alle tijden zijn lokaal.",'lime') ,"" ,0 ,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/sport365.png',fanart,"","","","","",isItFolder=False)        #name,url,mode,icon
    videos=live365.getLinks()
    for nm,link,active in videos:
        if active:
           
            addDir(Colored(nm  ,'none') ,link,48 ,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/sport365.png',fanart,"","","","","",isItFolder=False)
        else:
            addDir("[COLOR red][B]X[/B] [/COLOR]"+Colored(nm ,'none') ,"",0 ,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/sport365.png',fanart,"","","","","",isItFolder=False)
        errored=False
    if errored:
       if RefreshResources([('live365.py','https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/live365.py')]):
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('XBMC', 'No Links, so updated files dyamically, try again, just in case!')           
            print 'Updated files'


def playSports365(url):
    #print ('playSports365')
    import live365
    urlToPlay=live365.selectMatch(url)
    if urlToPlay and len(urlToPlay)>0:
        listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
    #    print   "playing stream name: " + str(name) 
        xbmc.Player(  ).play( urlToPlay, listitem)  
    else:
       if RefreshResources([('live365.py','https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/live365.py')]):
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('XBMC', 'No Links, so updated files dyamically, try again, just in case!')           
            print 'Updated files'
    return    
    
def RefreshResources(resources):
#    print Fromurl
    pDialog = xbmcgui.DialogProgress()
    ret = pDialog.create('XBMC', 'checking Updates...')
    totalFile=len(resources)
    fileno=0
    import hashlib
    updated=False
    try:
        for rfile in resources:
            if pDialog.iscanceled(): return
            progr = (fileno*80)/totalFile
            fname = rfile[0]
            fileToDownload = rfile[1]
            fileHash=hashlib.md5(fileToDownload+addon_version).hexdigest()
            lastFileTime=addon.getSetting( "Etagid"+fileHash)  
            if lastFileTime=="": lastFileTime=None
            resCode=200
            #print fileToDownload
            eTag=None        
            try:
                req = urllib2.Request(fileToDownload)
                req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')

                if lastFileTime:
                    req.add_header('If-None-Match',lastFileTime)
                response = urllib2.urlopen(req)
                resCode=response.getcode()
                if resCode<>304:
                    try:
                        eTag=response.info().getheader('Etag')
                    except: pass
                    data=response.read()
            except Exception as e: 
                s = str(e)
                if 'Not Modified'.lower() in s.lower(): resCode=304
                data=''
            if ('Exec format error: exec' in data or 'A file permissions error has occurred' in data) and 'xbmcplugin' not in data:
                data=''

            if len(data)>0:
                with open(os.path.join(home, fname), "wb") as filewriter:
                    filewriter.write(data)
                    updated=True
                    if eTag:
                        addon.setSetting( id="Etagid"+fileHash ,value=eTag)    
                pDialog.update(20+progr, 'imported ...'+fname)
            elif resCode==304:
                pDialog.update(20+progr, 'No Change.. skipping.'+fname)
            else:            
                pDialog.update(20+progr, 'Failed..zero byte.'+fname)
            fileno+=1
    except: pass
    pDialog.close()
    return updated


def collect_token():
    req = urllib2.Request(TOKEN_URL)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    token = re.search(r'npoplayer.token = "(.*?)"',page).group(1)
    #xbmc.log("plugin.video.nederland24:: oldtoken: %s" % token)
    # site change, token invalid, needs to be reordered. Thanks to rieter for figuring this out very quickly.
    first = -1
    last = -1
    for i in range(5, len(token) - 5, 1):
    #xbmc.log("plugin.video.nederland24:: %s" % token[i])
        if token[i].isdigit():
            if first < 0:
                first = i
                #xbmc.log("plugin.video.nederland24:: %s" % token[i])
            elif last < 0:
                last = i
                #xbmc.log("plugin.video.nederland24:: %s" % token[i])
                break

    newtoken = list(token)
    if first < 0 or last < 0:
        first = 12
        last = 13
    newtoken[first] = token[last]
    newtoken[last] = token[first]
    newtoken = ''.join(newtoken)
    #xbmc.log("plugin.video.nederland24:: newtoken: %s" % newtoken)
    return newtoken

def resolve_http_redirect(url, depth=0):
    if depth > 10:
        raise Exception("Redirected "+depth+" times, giving up.")
    o = urlparse.urlparse(url,allow_fragments=True)
    conn = httplib.HTTPConnection(o.netloc)
    path = o.path
    if o.query:
        path +='?'+o.query
    conn.request("HEAD", path)
    res = conn.getresponse()
    headers = dict(res.getheaders())
    if headers.has_key('location') and headers['location'] != url:
        return resolve_http_redirect(headers['location'], depth+1)
    else:
        return url
    
def streamNpo(source):
    URL=API_URL+BASE_URL+source+"&token=%s" % collect_token()
    req = urllib2.Request(URL)
    req.add_header('User-Agent', USER_AGENT)
    req.add_header('Referer', REF_URL)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    videopre=re.search(r'http:(.*?)url',page).group()
    prostream= (videopre.replace('\/', '/'))
    finalUrl = resolve_http_redirect(prostream)
    return finalUrl

#def findStream(page):
 #   frameHtml = bitly.OPEN_URL2(page, sourceSitebvls, bitly.getUserAgent())
  #  if 'window.atob' in frameHtml:
   #     b64coded = bitly.getBaseEncodedString(frameHtml)
    #    streamUrl = bitly.getStreamUrl(b64coded)
    #else:
     #   liveresolvelink = re.compile('player.*?src="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(frameHtml)[0]
     #   import liveresolver
     #   streamUrl = liveresolver.resolve(liveresolvelink)
     #   xbmc.log(streamUrl)
    #return streamUrl

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.jerichor3-%s]: %s" % string)

def makeRequest(url, headers=None):
        try:
            if headers is None:
                headers = {'User-agent' : 'THEHOOD'}
            req = urllib2.Request(url,None,headers)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            addon_log('URL: '+url)
            if hasattr(e, 'code'):
                addon_log('We failed with error code - %s.' % e.code)
                xbmc.executebuiltin("XBMC.Notification(Jericho,We failed with error code - "+str(e.code)+",10000,"+icon+")")
            elif hasattr(e, 'reason'):
                addon_log('We failed to reach a server.')
                addon_log('Reason: %s' %e.reason)
                xbmc.executebuiltin("XBMC.Notification(Jericho,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")


def JerichoIndex():
    addon_log("JerichoIndex")
    addDir('Addon News','News',46,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/nieuws.png',  FANART,'','','','',isItFolder=False)
    addDir('Information','Privacy Policy',45,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/informatie.png',fanart,'','','','',isItFolder=False)    
    addDir('Sports','',70,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/sport.png' ,  fanart,'','','','')
    addDir('Music','',75,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/muziek.png' ,  fanart,'','','','')
    getData(base64.b64decode(JerichoBase2),'')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def indexsport():
    addon_log("indexsport")
    addDir('Live Sport','',72,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/livesport.png',fanart,"","","","","",)
    addDir('FOX Sports Videos *Dutch*','http://www.foxsports.nl/video/',227,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fs.png' ,  fanart,'','','','')
    addDir('Ziggo Sport Totaal Replays and Clips','http://www.ziggosporttotaal.nl/video/',232,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/zst.png' ,  fanart,'','','','')
    addDir('Fullmatchesandshows.com','http://fullmatchesandshows.com/',301,'http://www.fullmatchesandshows.com/wp-content/uploads/2014/12/FMS-logo-n-text-SMALL.png' ,  fanart,'','','','')
    addDir('UFC','http://mmanext.com/',77,'http://mmanext.com/wp-content/uploads/2015/06/mmanext111.png',fanart,"","","","","",)
    addDir('MamaHD','',275,'http://mamahd.com/images/logo.png',fanart,"","","","","",)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def indexlivesport():
    addon_log("indexlivesport")
    addDir('SEBN.SC','',63,'http://sebn.sc/images/logo.png',fanart,"","","","","",)
    addDir('Sport365 - From ZemTV (Geoblocked)','',47,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/sport365.png',fanart,"","","","","",)
    #addDir('Feed2allnow.eu','',104,'http://cdn.cdnco.us/feed2all/logo.png',fanart,"","","","","",)
    addDir('StreamHD.eu/','',242,'http://www.streamhd.eu/images/logo.png',fanart,"","","","","",)
    addDir('Wizhdsports.to','',114,'http://wizhdsports.to/images/wiz.jpg',fanart,"","","","","",)
    addDir('Hesgoals.sc','',244,'https://2.bp.blogspot.com/-nPM2WTm78RY/V0I1k04gNUI/AAAAAAAAA-M/wWeh_Bwn63oW6QRQCJQiWV__IaCDscXXQCLcB/s1600/hesgoal.png',fanart,"","","","","",)
    addDir('Showsport-tv.com','',270,'http://showsport-tv.com/images/logo.png',fanart,"","","","","",)
    addDir('HDFree.Tv','',273,icon,fanart,"","","","","",)
    #addDir('Stream2watch.co','',248,'http://www.stream2watch.co/images/logo.png',fanart,"","","","","",)
    #addDir('LiveTV.sx','',251,'http://cdn.livetvcdn.net/img/oglogo.png',fanart,"","","","","",)
    #addDir('Woop.io','',308,'https://i.imgsafe.org/924ffb8.png',fanart,"","","","","",)
    #addDir('Wiz1.net','',106,'http://i39.tinypic.com/3128vb9.png',fanart,"","","","","",)
    #addDir('Foot-live.info','',115,icon,fanart,"","","","","",)
    addDir('Sportstream365.com','',306,'http://sportstream365.com/img/logo_en.png',fanart,"","","","","",)
    addDir('Tuttosportweb.com','',111,icon,fanart,"","","","","",)
    addDir('Golden Arrows Channel (Darts)','',112,icon,fanart,"","","","","",)
    #addDir('FromHot.com','',254,'http://www.u-bet.be/wp-content/uploads/2015/10/FromHot.png', fanart,"","","","","",)
    #addDir('Goatd.net','',107,icon,fanart,"","","","","",)
    #addDir('SportP2P','',268,'http://www.sportp2p.com/images/logo.png',fanart,"","","","","",)
    #addDir('LiveFootballVideo.com','',264,'http://livefootballvideo.com/images/xlivefootballvideologo.png.pagespeed.ic.3kxaAupa3O.png',fanart,"","","","","",)
    #addDir('Live9.net','',108,icon,fanart,"","","","","",)
    #addDir('Vipbox.nu','',109,'http://cdn.vipboxoc.co//images/vipbox-logo.png',fanart,"","","","","",)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
#def indexbvls():
 #   addon_log("indexbvls")
  #  getData(base64.b64decode(BvlsBase),'')
   # xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def indexmuziek():
    addon_log("indexmuziek")
    getData(base64.b64decode(MusicBase),'')
    addDir('XITE','http://xite.nl/videos/1',221,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/xite.png' ,  fanart,'','','','')
    addDir('Slam FM Top 40','http://www.slam.nl/slam40/',241,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/xite.png' ,  fanart,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))



def playLiveResolver(url, name):
    dp = xbmcgui.DialogProgress()
    dp.create("Jericho","Please wait")  
    import liveresolver
    resolved = liveresolver.resolve(url) 
    if resolved:
        #if 'p2pcast' in resolved:
        #    resolved = 'plugin://plugin.video.f4mTester/?streamtype=HLS&amp;url=' + urllib.quote_plus(resolved)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png",thumbnailImage="DefaultVideo.png")
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        xbmc.Player().play(resolved, liz)  
    else:
        xbmc.executebuiltin("XBMC.Notification(Jericho,No playable link found. - ,5000)")  
    
   
def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)
    
def getbvlsSchedule():
    bvlspage = getHtml('http://sebn.sc/')
    datum = re.compile('<h1>(.*?)</h1>', re.DOTALL | re.IGNORECASE).findall(bvlspage)[0]
    utils.addDir(datum,'',63,'http://sebn.sc/images/logo.png','',fanart)
    utils.addDir('','',63,'http://sebn.sc/images/logo.png','',fanart)
    
    match = re.compile(r'<td class="rt-td"> <p class="sports">(.*?)</p>.*?sports1">(.*?)</p>.*?sports">(.*?)</p>.*?href="(.*?)"', re.DOTALL | re.IGNORECASE).findall(bvlspage)
    for tijd, categorie, name, videopage in match:
        name = tijd + ' - [' + categorie + '] ' + name
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(name,videopage,300,'http://sebn.sc/images/logo.png','',fanart)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def getwizhdSchedule(url):
    bvlspage = getHtml(url)
    match = re.compile(r'<div class="match" id="match.*?">(.*?)\$\("#channel.*?" \)\.slideDown\( 100 \);', re.IGNORECASE | re.DOTALL).findall(bvlspage)
    for wedstrijd in match:
        try:
            eggs = re.compile('<span id="startTime.*?Span">\n\t\t(.*?)</span>.*?<div class="name">(.*?)</div>', re.IGNORECASE | re.DOTALL).findall(wedstrijd)
            for tijd, name in eggs:
                try:
                    dt = datetime.strptime(tijd, "%H:%M")
                    tijd = str(dt.hour+1).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
                except :
                    pass
                utils.addDir(tijd+' - '+name,'',113,'http://wizhdsports.to/images/wiz.jpg', '', fanart)
            try:
                streams = re.compile('<div style="float:left;"><a href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(wedstrijd)
                for videopage, streamname in streams:
                    tekstregel = '             [COLOR yellow]' + streamname + ' [/COLOR] '
                    videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
                    utils.addDir(tekstregel,videopage,300,'http://wizhdsports.to/images/wiz.jpg', '', fanart)
            except: pass
        except:
            addDir('Error with the agenda.','',113,'http://wizhdsports.to/images/wiz.jpg',fanart,"","","","","",)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def getwizhdcats():
    listhtml = utils.getHtml('http://wizhdsports.to/index.html','http://wizhdsports.to/index.html')
    match = re.compile("""<li onclick="location='(.*?)'.*?src="(.*?)".*?<div style="float:left">(.*?)</div>""", re.IGNORECASE | re.DOTALL).findall(listhtml)
    for page, img, name in match:
        if 'P2P' in name:
            pass
        else:
            name = name.replace('Home', 'All')
            utils.addDir(name,page,113,img,'',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def getUFC():
    ufcpage = getHtml('http://mmanext.com/ufc-videos/')
    match = re.compile('story-contain-img.*?src.*?http(.*?).jpg.*?<h2>(.*?)</h2>.*?text-date left">(.*?)</span>.*?href="(.*?)".*?Read More', re.IGNORECASE | re.DOTALL).findall(ufcpage)
    for img, name, datum, videopage in match:
        name = utils.cleantext(name)
        img = img.replace('s://','://')
        img = 'http' + img + '.jpg'
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(datum + ': '+ name,videopage,300,img, '', FANART)
    try:
        nextp = re.compile("""class="current">.*?</span>.*?href='(.*?)'""", re.IGNORECASE | re.DOTALL).findall(ufcpage)[0]
        next = nextp.replace("&amp;","&")
        utils.addDir('Volgende Pagina', next, 79,'', '')
    except: pass
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def getUFCnext(url):
    ufcpage = getHtml(url)
    match = re.compile('story-contain-img.*?src.*?http(.*?).jpg.*?<h2>(.*?)</h2>.*?text-date left">(.*?)</span>.*?href="(.*?)".*?Read More', re.IGNORECASE | re.DOTALL).findall(ufcpage)
    for img, name, datum, videopage in match:
        name = utils.cleantext(name)
        img = img.replace('s://','://')
        img = 'http' + img + '.jpg'
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(datum + ': '+ name,videopage,300,img, '', FANART)
    try:
        nextp = re.compile("""class="current">.*?</span>.*?href='(.*?)'""", re.IGNORECASE | re.DOTALL).findall(ufcpage)[0]
        next = nextp.replace("&amp;","&")
        utils.addDir('Volgende Pagina', next, 79,'', '')
    except: pass
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
def PlayYouTube(url, name):
        dp = xbmcgui.DialogProgress()
        dp.create("Jericho","Please wait")  
        import YDStreamExtractor
        YDStreamExtractor.disableDASHVideo(True)
        vid = YDStreamExtractor.getVideoInfo(url,quality=1)
        stream_url = vid.streamURL()
        print "stream_url =", stream_url
        img = " "
        listitem = xbmcgui.ListItem(name, iconImage=img, thumbnailImage=img)
        playfile = xbmc.Player()
        playfile.play(stream_url, listitem)

def Catfeed2all():
        addDir('Football' ,'football.html',105,icon ,  FANART,'','','','')
        addDir('AM. Football' ,'american-football.html',105,icon ,  FANART,'','','','')
        addDir('Basketball' ,'basketball.html',105,icon ,  FANART,'','','','')
        addDir('Boxing/WWE/UFC' ,'boxing-wwe-ufc.html',105,icon ,  FANART,'','','','')
        addDir('Rugby' ,'rugby.html',105,icon ,  FANART,'','','','')
        addDir('Ice Hockey' ,'ice-hockey.html',105,icon ,  FANART,'','','','')
        addDir('Tennis' ,'tennis.html',105,icon ,  FANART,'','','','')
        addDir('Motorsport' ,'motosport.html',105,icon ,  FANART,'','','','')
        addDir('Golf' ,'golf.html',105,icon ,  FANART,'','','','')
        addDir('Baseball' ,'baseball.html',105,icon ,  FANART,'','','','')
        addDir('Darts' ,'darts.html',105,icon ,  FANART,'','','','')
        addDir('Snooker' ,'snooker.html',105,icon ,  FANART,'','','','')
        addDir('Handball' ,'handball.html',105,icon ,  FANART,'','','','')
        addDir('Cricket' ,'cricket.html',105,icon ,  FANART,'','','','')
        addDir('Aussie Rules' ,'aussie-rules.html',105,icon ,  FANART,'','','','')
        addDir('Others' ,'others.html',105,icon ,  FANART,'','','','')
        return



def Addthefeed2all(url):
    pagecontent=bitly.OPEN_URL2('http://www.nowfeed2all.eu/type/'+url,'http://www.feed2allnow.eu/',bitly.getUserAgent())
    match1=re.compile('<span>\s*([^<]+)</span>\s*([^<]+) </a> </h3>.+?\s*.+?href=\'(.*?)\'',re.DOTALL).findall(pagecontent)
    for tijd,wedstrijd,videopage in match1:
        videopage = 'http://www.feed2allnow.eu' + videopage
        if (bitly.getResponse(videopage)):
        
            videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
            utils.addDir(wedstrijd, videopage, 300, icon, '', FANART)
            #utils.addDir(wedstrijd, videopage, 60, icon, '', FANART)
    #except:
        #pass
    try:
        pagecontent=bitly.OPEN_URL2('http://www.nowfeed2all.eu/type/'+url,'http://www.feed2allnow.eu/',bitly.getUserAgent())
        match1=re.compile('<span class="matchtime">([^<]+)</span> </span>\s*([^<]+)</a> </h3>.+?\s*.+?href=\'([^<]+)\'',re.DOTALL).findall(pagecontent)
        for tijd,wedstrijd,videopage in match1:
            try:
                dt = datetime.strptime(tijd, "%H:%M")
                tijd = str(dt.hour+1).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
            except :
                pass        
            videopage = 'http://www.feed2allnow.eu' + videopage
            if (bitly.getResponse(videopage)):
                videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
                utils.addDir('('+tijd+') '+ wedstrijd, videopage, 300, icon, '', FANART)
                #utils.addDir('('+tijd+') '+ wedstrijd, videopage, 60, icon, '', FANART)
    except:
        pass
    
def Catvipbox():
        addDir('Football' ,'football.html',110,icon ,  FANART,'','','','')
        addDir('AM. Football' ,'american-football.html',110,icon ,  FANART,'','','','')
        addDir('Basketball' ,'basketball.html',110,icon ,  FANART,'','','','')
        addDir('Boxing/WWE/UFC' ,'boxing-wwe-ufc.html',110,icon ,  FANART,'','','','')
        addDir('Rugby' ,'rugby.html',110,icon ,  FANART,'','','','')
        addDir('Ice Hockey' ,'ice-hockey.html',110,icon ,  FANART,'','','','')
        addDir('Tennis' ,'tennis.html',110,icon ,  FANART,'','','','')
        addDir('Motorsport' ,'motosport.html',110,icon ,  FANART,'','','','')
        addDir('Golf' ,'golf.html',110,icon ,  FANART,'','','','')
        addDir('Baseball' ,'baseball.html',110,icon ,  FANART,'','','','')
        addDir('Darts' ,'darts.html',110,icon ,  FANART,'','','','')
        addDir('Snooker' ,'snooker.html',110,icon ,  FANART,'','','','')
        addDir('Handball' ,'handball.html',110,icon ,  FANART,'','','','')
        addDir('Cricket' ,'cricket.html',110,icon ,  FANART,'','','','')
        addDir('Aussie Rules' ,'aussie-rules.html',110,icon ,  FANART,'','','','')
        addDir('Others' ,'others.html',110,icon ,  FANART,'','','','')
        return



def Addvipbox(url):
    pagecontent=bitly.OPEN_URL2('http://nl.vipbox.nu/sports/'+url,'http://nl.vipbox.nu/',bitly.getUserAgent())
    match1 = re.compile("""matchtime">(.*?)</span> (.*?)</a>.*?gameLinks.*?href='(.*?)'>Link 1""", re.IGNORECASE | re.DOTALL).findall(pagecontent)
    for tijd,wedstrijd,videopage in match1:
        try:
            dt = datetime.strptime(tijd, "%H:%M")
            tijd = str(dt.hour+1).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
        except:
            pass    
        tijd = tijd.replace('24','00').replace('25','01').replace('26','02')    
        videopage = 'http://nl.vipbox.nu/' + videopage
        if (bitly.getResponse(videopage)):
            videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
            utils.addDir('('+tijd+') '+ wedstrijd, videopage, 300, icon, '', FANART)
            #addDir('('+tijd+') '+ wedstrijd, videopage, 60, icon, FANART,'','','','')

def Addwiz():
    pagecontent = bitly.OPEN_URL2('http://www.wiz1.net/lag10_home.php','http://www.wiz1.net/',bitly.getUserAgent())
    match = re.compile(r'(\d{2}:\d{2}) <font color="#5185C9"><b>([^<]+)</b></font> ([^<]+)<a href="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(pagecontent)
    for tijd, sport, wedstrijd, videopage in match:
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        try:
            dt = datetime.strptime(tijd, "%H:%M")
            tijd = str(dt.hour+0).rjust(2,'0') + ':' + str(dt.minute).rjust(2,'0')
        except :
            pass
        utils.addDir(sport+': '+ tijd + ' - '+ wedstrijd, videopage, 300, icon, '', FANART)
        #addDir(sport+': '+ tijd + ' - '+ wedstrijd, videopage, 60, icon, FANART,'','','','')
        
def AddDarts():
    pagecontent = bitly.OPEN_URL2('http://goldenarrowschannel.jouwweb.nl/schedule','http://goldenarrowschannel.jouwweb.nl/',bitly.getUserAgent())
    match = re.compile("""<tr style='mso-yfti-irow:.*?'>.*?<td width=56 valign=top style='width:42.15pt;border:solid windowtext 1.5pt;.*?border-top:none;mso-border-top-alt:solid windowtext 1.5pt;padding:0cm 5.4pt 0cm 5.4pt'>(.*?)</p>.*?<td width=66 valign=top style='width:49.6pt;border-top:none;border-left:none;.*?border-bottom:solid windowtext 1.5pt;border-right:solid windowtext 1.5pt;.*?mso-border-top-alt:solid windowtext 1.5pt;mso-border-left-alt:solid windowtext 1.5pt;.*?padding:0cm 5.4pt 0cm 5.4pt'>(.*?)</p>.*?<td width=66 valign=top style='width:49.6pt;border-top:none;border-left:none;.*?border-bottom:solid windowtext 1.5pt;border-right:solid windowtext 1.5pt;.*?mso-border-top-alt:solid windowtext 1.5pt;mso-border-left-alt:solid windowtext 1.5pt;.*?padding:0cm 5.4pt 0cm 5.4pt'>(.*?)</p>.*?<td width=538 valign=top style='width:403.65pt;border-top:none;border-left:.*?none;border-bottom:solid windowtext 1.5pt;border-right:solid windowtext 1.5pt;.*?mso-border-top-alt:solid windowtext 1.5pt;mso-border-left-alt:solid windowtext 1.5pt;.*?padding:0cm 5.4pt 0cm 5.4pt'>(.*?)</p>.*?href="(.*?)">""", re.IGNORECASE | re.DOTALL).findall(pagecontent)
    for datum, UKtijd, EUtijd, name, videopage in match:
        datum = striphtml(datum)
        datum = datum.replace('\n','').replace('\t','').replace(' ','')
        UKtijd = striphtml(UKtijd)
        UKtijd = UKtijd.replace('\n','').replace('\t','').replace(' ','')
        EUtijd = striphtml(EUtijd)
        EUtijd = EUtijd.replace('\n','').replace('\t','').replace(' ','')
        name = striphtml(name)
        name = name.replace('\n','').replace('\t','').replace(' ','')
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(datum + ' - ' + EUtijd + ' - ' + name, videopage, 300, icon, '', FANART)
        #addDir(sport+': '+ tijd + ' - '+ wedstrijd, videopage, 60, icon, FANART,'','','','')

def Addtuttosport():
    pagecontent = bitly.OPEN_URL2('http://tuttoserie.blogspot.nl/p/daily.html','http://tuttoserie.blogspot.nl/p/daily.html',bitly.getUserAgent())
    match = re.compile(r'(\d{2}:\d{2}) (.*?) - <a.*?href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(pagecontent)
    for tijd, name, videopage, title in match:
        wedstrijd = striphtml(name)
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(tijd + ' - ' + name + ' - (' + title + ')', videopage, '', icon, '', FANART)
        #addDir(tijd1 + tijd2 + tijd3 + ' - ' + wedstrijd + '(' + competitie + ')', videopage, 60, icon, FANART,'','','','')
        
def Addgoatd():
    jsport=''
    goatpage = bitly.OPEN_URL2('http://goatd.net/','http://goatd.net/',bitly.getUserAgent())
    match = re.compile(r'<b>ET</b></td>\s+<td[^<]+><img src="([^"]+)".*?href="([^"]+)"[^>]+>([^<]+)<.*?<b>([^<]+)<.*?<b>([^<]+)<', re.DOTALL | re.IGNORECASE).findall(goatpage)
    for img, videopage, wedstrijd, tijd, zone in match:
        try:
            sport = re.compile('http://.*?/.*?/.*?/.*?/.*?/.*?/(.*?).gif', re.DOTALL | re.IGNORECASE).findall(img)
            if sport > 0 :
                for jsport in sport:
                    jsport = re.sub("[^A-Za-z]", "", jsport) 
        except:
            pass
        videopage = 'http://goatd.net/' + videopage
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(jsport + ': ' + tijd + ' - ' + zone +' '+ wedstrijd, videopage, 300, img, '', FANART)
        #addDir(jsport + ': ' + tijd + ' - ' + zone +' '+ wedstrijd, videopage, 60, img, FANART,'','','','')
        
def Addlive9():
    live9page = bitly.OPEN_URL2('http://live9.net/','http://live9.net/',bitly.getUserAgent())
    match = re.compile(r'(\d{2}:\d{2}) <font color="#ffea01"><b>([^<]+)</b></font> ([^<]+)<a href="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(live9page)
    for tijd, sport, wedstrijd, videopage in match:
        name = tijd + ' - ' + sport + ' - ' + wedstrijd
        videopage = videopage.replace("t/live","t/lives")
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(name, videopage, 300,icon , '', FANART)
        #addDir(name, videopage, 60,icon ,  FANART,'','','','')
    
def getHtml(url, referer=None, hdr=None, data=None):
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
    if not hdr:
        req = urllib2.Request(url, data, headers)
    else:
        req = urllib2.Request(url, data, hdr)
    if referer:
        req.add_header('Referer', referer)
    response = urllib2.urlopen(req, timeout=60)
    data = response.read()    
    response.close()
    return data        
    
def News():
    text = ''
    twit = 'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/Nieuws.xml'
    req = urllib2.Request(twit)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re.DOTALL).findall(link)
    for status, dte in match:
        try:
                status = status.decode('ascii', 'ignore')
        except:
                status = status.decode('utf-8','ignore')
        dte = dte[:-15]
        status = status.replace('&amp;','')
        dte = '[COLOR yellow][B]'+dte+'[/B][/COLOR]'
        text = text+dte+'\n'+status+'\n'+'\n'
    showText('[COLOR yellow][B]News[/B][/COLOR]', text)



def Privacy_Policy():
    text = ''
    twit = 'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/informatie.xml'
    req = urllib2.Request(twit)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re.DOTALL).findall(link)
    for status, dte in match:
        try:
                status = status.decode('ascii', 'ignore')
        except:
                status = status.decode('utf-8','ignore')
        dte = dte[:-15]
        status = status.replace('&amp;','')
        dte = '[COLOR yellow][B]'+dte+'[/B][/COLOR]'
        text = text+dte+'\n'+status+'\n'+'\n'
    showText('[COLOR yellow][B]Information[/B][/COLOR]', text)

def showText(heading, text):
    intid = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % intid)
    xbmc.sleep(100)
    win = xbmcgui.Window(intid)
    retry = 50
    while retry > 0:
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass


def getSoup(url,data=None):
        if url.startswith('http://') or url.startswith('https://'):
            data = makeRequest(url)
            if re.search("#EXTM3U",data) or 'm3u' in url: 
                #print 'found m3u data',data
                return data
                
        elif data is not None:
            if xbmcvfs.exists(url):
                if url.startswith("smb://") or url.startswith("nfs://"):
                    copy = xbmcvfs.copy(url, os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    if copy:
                        data = open(os.path.join(profile, 'temp', 'sorce_temp.txt'), "r").read()
                        xbmcvfs.delete(os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    else:
                        addon_log("failed to copy from smb:")
                else:
                    data = open(url, 'r').read()
                    if re.match("#EXTM3U",data)or 'm3u' in url: 
                        #print 'found m3u data',data
                        return data
            else:
                addon_log("Soup Data not found!")
                return
        return BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)


def getData(url,fanart):
    if addon.getSetting('Thumbnail_On') =="true":
        SetViewLayout = "Thumbnail"
    else:
        SetViewLayout = "List"
     
    soup = getSoup(url)
    #print type(soup)
    if isinstance(soup,BeautifulSOAP):
        if len(soup('layoutype')) < 1:
            SetViewLayout = "List"        

        if len(soup('channels')) > 0:
            channels = soup('channel')
            for channel in channels:
#                print channel

                linkedUrl=''
                lcount=0
                try:
                    linkedUrl =  channel('externallink')[0].string
                    lcount=len(channel('externallink'))
                except: pass
                #print 'linkedUrl',linkedUrl,lcount
                if lcount>1: linkedUrl=''

                name = channel('name')[0].string
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    thumbnail = ''

                try:
                    if not channel('fanart'):
                        if addon.getSetting('use_thumb') == "true":
                            fanArt = thumbnail
                        else:
                            fanArt = fanart
                    else:
                        fanArt = channel('fanart')[0].string
                    if fanArt == None:
                        raise
                except:
                    fanArt = fanart

                try:
                    desc = channel('info')[0].string
                    if desc == None:
                        raise
                except:
                    desc = ''

                try:
                    genre = channel('genre')[0].string
                    if genre == None:
                        raise
                except:
                    genre = ''

                try:
                    date = channel('date')[0].string
                    if date == None:
                        raise
                except:
                    date = ''

                try:
                    credits = channel('credits')[0].string
                    if credits == None:
                        raise
                except:
                    credits = ''

                try:
                    if linkedUrl=='':
                        addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),2,thumbnail,fanArt,desc,genre,date,credits,True)
                    else:
                        #print linkedUrl
                        addDir(name.encode('utf-8'),linkedUrl.encode('utf-8'),1,thumbnail,fanArt,desc,genre,date,None,'source')
                except:
                    addon_log('There was a problem adding directory from getData(): '+name.encode('utf-8', 'ignore'))
        else:
            addon_log('No Channels: getItems')
            getItems(soup('item'),fanart)
    else:
        parse_m3u(soup)

    if SetViewLayout == "Thumbnail":
       SetViewThumbnail()


# borrow from https://github.com/enen92/P2P-Streams-XBMC/blob/master/plugin.video.p2p-streams/resources/core/livestreams.py
# This will not go through the getItems functions ( means you must have ready to play url, no regex)
def parse_m3u(data):
    content = data.rstrip()
    match = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)').findall(content)
    total = len(match)
    print 'total m3u links',total
    for other,channel_name,stream_url in match:
        if 'tvg-logo' in other:
            thumbnail = re_me(other,'tvg-logo=[\'"](.*?)[\'"]')
            if thumbnail:
                if thumbnail.startswith('http'):
                    thumbnail = thumbnail
                
                elif not addon.getSetting('logo-folderPath') == "":
                    logo_url = addon.getSetting('logo-folderPath')
                    thumbnail = logo_url + thumbnail

                else:
                    thumbnail = thumbnail
            #else:
            
        else:
            thumbnail = ''
        if 'type' in other:
            mode_type = re_me(other,'type=[\'"](.*?)[\'"]')
            if mode_type == 'yt-dl':
                stream_url = stream_url +"&mode=18"
            elif mode_type == 'regex':
                url = stream_url.split('&regexs=')
                #print url[0] getSoup(url,data=None)
                regexs = parse_regex(getSoup('',data=url[1]))
                
                addLink(url[0], channel_name,thumbnail,'','','','','',None,regexs,total)
                continue
        addLink(stream_url, channel_name,thumbnail,'','','','','',None,'',total)

    xbmc.executebuiltin("Container.SetViewMode(50)")

def getChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('channel', attrs={'name' : name.decode('utf-8')})
        items = channel_list('item')
        try:
            fanart = channel_list('fanart')[0].string
            if fanart is None:
                raise
        except:
            fanart = fanart
        for channel in channel_list('subchannel'):
            name = channel('name')[0].string
            try:
                thumbnail = channel('thumbnail')[0].string
                if thumbnail is None:
                    raise
            except:
                thumbnail = ''
            try:
                if not channel('fanart'):
                    if addon.getSetting('use_thumb') == "true":
                        fanart = thumbnail
                else:
                    fanart = channel('fanart')[0].string
                if fanart is None:
                    raise
            except:
                pass
            try:
                desc = channel('info')[0].string
                if desc is None:
                    raise
            except:
                desc = ''

            try:
                genre = channel('genre')[0].string
                if genre is None:
                    raise
            except:
                genre = ''

            try:
                date = channel('date')[0].string
                if date is None:
                    raise
            except:
                date = ''

            try:
                strcredits = channel('credits')[0].string
                if strcredits is None:
                    raise
            except:
                strcredits = ''

            try:
                addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),3,thumbnail,fanart,desc,genre,strcredits,date)
            except:
                addon_log('There was a problem adding directory - '+name.encode('utf-8', 'ignore'))
        getItems(items,fanart)


def getSubChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('subchannel', attrs={'name' : name.decode('utf-8')})
        items = channel_list('subitem')
        getItems(items,fanart)


def FindFirstPattern(text,pattern):
    result = ""
    try:    
        matches = re.findall(pattern,text, flags=re.DOTALL)
        result = matches[0]
    except:
        result = ""

    return result

def regex_get_all(text, start_with, end_with):
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r                

def regex_from_to(text, from_string, to_string, excluding=True):
    if excluding:
       try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
       except: r = ''
    else:
       try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
       except: r = ''
    return r

def getItems(items,fanart):
        total = len(items)
        #print 'START GET ITEMS *****'
        addon_log('Total Items: %s' %total)
        for item in items:
            isXMLSource=False
            isJsonrpc = False
            try:
                name = item('title')[0].string
                if name is None:
                    name = 'unknown?'
            except:
                addon_log('Name Error')
                name = ''


            try:
                if item('epg'):
                    if item.epg_url:
                        addon_log('Get EPG Regex')
                        epg_url = item.epg_url.string
                        epg_regex = item.epg_regex.string
                        epg_name = get_epg(epg_url, epg_regex)
                        if epg_name:
                            name += ' - ' + epg_name
                    elif item('epg')[0].string > 1:
                        name += getepg(item('epg')[0].string)
                else:
                    pass
            except:
                addon_log('EPG Error')
            try:
                url = []
                if len(item('link')) >0:
#                    print 'item link', item('linkas')
                    for i in item('link'):
                        if not i.string is None:
                            url.append(i.string)
                    
                elif len(item('sportsdevil')) >0:
                    for i in item('sportsdevil'):
                        if not i.string is None:
                            sportsdevil = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +i.string
                            referer = item('referer')[0].string
                            if referer:
                                #print 'referer found'
                                sportsdevil = sportsdevil + '%26referer=' +referer
                            url.append(sportsdevil)

                elif len(item('p2p')) >0:
                    for i in item('p2p'):
                        if not i.string is None:
                            if addon.getSetting('default_player') == 'p2p-streams':
                                if 'sop://' in i:
                                    sop = 'plugin://plugin.video.p2p-streams/?url='+i.string +'&amp;mode=2&amp;' + 'name='+name 
                                    url.append(sop) 
                                else:
                                    p2p='plugin://plugin.video.p2p-streams/?url='+i.string +'&mode=1&name=' +name 
                                url.append(p2p)
                            else:
                                if 'sop://' in i:
                                    sop = 'plugin://program.plexus/?url='+i.string +'&amp;mode=2&amp;' + 'name='+name 
                                    url.append(sop) 
                                else:
                                    p2p='plugin://program.plexus/?url='+i.string +'&mode=1&name=' +name 
                                url.append(p2p)
                                

                elif len(item('vaughn')) >0:
                    for i in item('vaughn'):
                        if not i.string is None:
                            vaughn = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel='+i.string
                            url.append(vaughn)
                elif len(item('veetle')) >0:
                    for i in item('veetle'):
                        if not i.string is None:
                            veetle = 'plugin://plugin.video.veetle/?channel='+i.string
                        url.append(veetle)
                elif len(item('npo')) >0:
                    for i in item('npo'):
                        if not i.string is None:
                            npo = streamNpo(i.string)
                    url.append(npo)    
                elif len(item('bvls')) >0:
                    for i in item('bvls'):
                        if not i.string == None:
                            title = item('title')[0].string
                            color = 'none'
                            titlesup = ''
                            streamUrl = findStream(i.string)
                            if streamUrl.startswith('rtmp'):
                                color = 'orange'
                                titlesup = '(RTMP)'
                            elif (bitly.getResponse(streamUrl)):
                                color = 'lime'
                                titlesup = '(OTHER)'
                                if streamUrl[-4:] == '.flv' :
                                    streamUrl = bitly.VeetleId(streamUrl)
                                    titlesup = '(VEETLE)'
                            name='[COLOR %s]%s %s[/COLOR]' % (color, title, titlesup) 
                            bvls = streamUrl
                            url.append(bvls)
                elif len(item('ytch')) >0:
                    for i in item('ytch'):
                        thumbnail = item('thumbnail')[0].string
                        title = item('title')[0].string
                        plugintools.add_item( 
                        #action="", 
                        title=title,
                        url="plugin://plugin.video.youtube/channel/"+i.string+"/",
                        thumbnail= thumbnail,
                        folder=True )
                elif len(item('ytlist')) >0:
                    for i in item('ytlist'):
                        thumbnail = item('thumbnail')[0].string
                        title = item('title')[0].string
                        plugintools.add_item( 
                        #action="", 
                        title=title,
                        url="plugin://plugin.video.youtube/user/"+i.string+"/",
                        thumbnail= thumbnail,
                        folder=True )
                elif len(item('utube')) >0:
                    for i in item('utube'):
                        if not i.string is None:
                            if len(i.string) == 11:
                                utube = 'plugin://plugin.video.youtube/play/?video_id='+ i.string 
                            elif i.string.startswith('PL') and not '&order=' in i.string :
                                utube = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + i.string
                            else:
                                utube = 'plugin://plugin.video.youtube/play/?playlist_id=' + i.string 
                    url.append(utube)
                elif len(item('imdb')) >0:
                    for i in item('imdb'):
                        if not i.string is None:
                            if addon.getSetting('genesisorpulsar') == '0':
                                imdb = 'plugin://plugin.video.genesis/?action=play&imdb='+i.string
                            else:
                                imdb = 'plugin://plugin.video.pulsar/movie/tt'+i.string+'/play'
                            url.append(imdb)                      
                elif len(item('f4m')) >0:
                        for i in item('f4m'):
                            if not i.string is None:
                                if '.f4m' in i.string:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)+'&amp;name='+name
                                elif '.m3u8' in i.string:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)+'&amp;streamtype=HLS'+'&amp;name='+name
                                    
                                else:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)+'&amp;streamtype=TSDOWNLOADER'+'&amp;name='+name
                        url.append(f4m)
                elif len(item('ftv')) >0:
                    for i in item('ftv'):
                        if not i.string is None:
                            ftv = 'plugin://plugin.video.F.T.V/?name='+urllib.quote(name) +'&url=' +i.string +'&mode=125&ch_fanart=na'
                        url.append(ftv)                        
                if len(url) < 1:
                    raise
            except:
                addon_log('Error <link> element, Passing:'+name.encode('utf-8', 'ignore'))
                continue
                
            isXMLSource=False

            try:
                isXMLSource = item('externallink')[0].string
            except: pass
            
            if isXMLSource:
                ext_url=[isXMLSource]
                isXMLSource=True
            else:
                isXMLSource=False
            try:
                isJsonrpc = item('jsonrpc')[0].string
            except: pass
            if isJsonrpc:
                ext_url=[isJsonrpc]
                isJsonrpc=True
            else:
                isJsonrpc=False            
            try:
                thumbnail = item('thumbnail')[0].string
                if thumbnail is None:
                    raise
            except:
                thumbnail = ''
            try:
                if not item('fanart'):
                    if addon.getSetting('use_thumb') == "true":
                        fanart = thumbnail
                    else:
                        fanart = fanart
                else:
                    fanart = item('fanart')[0].string
                if fanart is None:
                    raise
            except:
                fanart = fanart
            try:
                desc = item('info')[0].string
                if desc is None:
                    raise
            except:
                desc = ''

            try:
                genre = item('genre')[0].string
                if genre is None:
                    raise
            except:
                genre = ''

            try:
                date = item('date')[0].string
                if date is None:
                    raise
            except:
                date = ''

            regexs = None
            if item('regex'):
                try:
                    reg_item = item('regex')
                    regexs = parse_regex(reg_item)
                except:
                    pass            
           
            try:
                if len(url) > 1:
                    
                    alt = 0
                    playlist = []
                    for i in url:
                        if addon.getSetting('ask_playlist_items') == 'true':
                            if regexs:
                                playlist.append(i+'&regexs='+regexs)
                            elif  any(x in i for x in resolve_url) and  i.startswith('http'):
                                playlist.append(i+'&mode=19')
                        else:
                            playlist.append(i)
                    if addon.getSetting('add_playlist') == "false":                    
                            for i in url:
                                alt += 1
                                print 'ADDLINK 1'
                                addLink(i,'%s) %s' %(alt, name.encode('utf-8', 'ignore')),thumbnail,fanart,desc,genre,date,True,playlist,regexs,total)                            
                    else:
                        addLink('', name.encode('utf-8', 'ignore'),thumbnail,fanart,desc,genre,date,True,playlist,regexs,total)
                else:
                    if isXMLSource:
                        addDir(name.encode('utf-8'),ext_url[0].encode('utf-8'),1,thumbnail,fanart,desc,genre,date,None,'source')
                    elif isJsonrpc:
                        addDir(name.encode('utf-8'),ext_url[0],53,thumbnail,fanart,desc,genre,date,None,'source')
                    elif url[0].find('sublink') > 0:
                        addDir(name.encode('utf-8'),url[0],30,thumbnail,fanart,desc,regexs,'','','')
                        addDir(name.encode('utf-8'),url[0],30,thumbnail,fanart,desc,genre,date,'sublink')                
                    else: 
                        addLink(url[0],name.encode('utf-8', 'ignore'),thumbnail,fanart,desc,genre,date,True,None,regexs,total)

                    #print 'success'
            except:
                addon_log('There was a problem adding item - '+name.encode('utf-8', 'ignore'))
        print 'FINISH GET ITEMS *****'      

def parse_regex(reg_item):
                try:
                    regexs = {}
                    for i in reg_item:
                        regexs[i('name')[0].string] = {}
                        #regexs[i('name')[0].string]['expre'] = i('expres')[0].string
                        try:
                            regexs[i('name')[0].string]['expre'] = i('expres')[0].string
                            if not regexs[i('name')[0].string]['expre']:
                                regexs[i('name')[0].string]['expre']=''
                        except:
                            addon_log("Regex: -- No Referer --")
                        regexs[i('name')[0].string]['page'] = i('page')[0].string
                        try:
                            regexs[i('name')[0].string]['refer'] = i('referer')[0].string
                        except:
                            addon_log("Regex: -- No Referer --")
                        try:
                            regexs[i('name')[0].string]['connection'] = i('connection')[0].string
                        except:
                            addon_log("Regex: -- No connection --")

                        try:
                            regexs[i('name')[0].string]['notplayable'] = i('notplayable')[0].string
                        except:
                            addon_log("Regex: -- No notplayable --")
                            
                        try:
                            regexs[i('name')[0].string]['noredirect'] = i('noredirect')[0].string
                        except:
                            addon_log("Regex: -- No noredirect --")
                        try:
                            regexs[i('name')[0].string]['origin'] = i('origin')[0].string
                        except:
                            addon_log("Regex: -- No origin --")
                        try:
                            regexs[i('name')[0].string]['includeheaders'] = i('includeheaders')[0].string
                        except:
                            addon_log("Regex: -- No includeheaders --")                            
                            
                        try:
                            regexs[i('name')[0].string]['x-req'] = i('x-req')[0].string
                        except:
                            addon_log("Regex: -- No x-req --")
                        try:
                            regexs[i('name')[0].string]['x-forward'] = i('x-forward')[0].string
                        except:
                            addon_log("Regex: -- No x-forward --")

                        try:
                            regexs[i('name')[0].string]['agent'] = i('agent')[0].string
                        except:
                            addon_log("Regex: -- No User Agent --")
                        try:
                            regexs[i('name')[0].string]['post'] = i('post')[0].string
                        except:
                            addon_log("Regex: -- Not a post")
                        try:
                            regexs[i('name')[0].string]['rawpost'] = i('rawpost')[0].string
                        except:
                            addon_log("Regex: -- Not a rawpost")
                        try:
                            regexs[i('name')[0].string]['htmlunescape'] = i('htmlunescape')[0].string
                        except:
                            addon_log("Regex: -- Not a htmlunescape")


                        try:
                            regexs[i('name')[0].string]['readcookieonly'] = i('readcookieonly')[0].string
                        except:
                            addon_log("Regex: -- Not a readCookieOnly")
                        #print i
                        try:
                            regexs[i('name')[0].string]['cookiejar'] = i('cookiejar')[0].string
                            if not regexs[i('name')[0].string]['cookiejar']:
                                regexs[i('name')[0].string]['cookiejar']=''
                        except:
                            addon_log("Regex: -- Not a cookieJar")                            
                        try:
                            regexs[i('name')[0].string]['setcookie'] = i('setcookie')[0].string
                        except:
                            addon_log("Regex: -- Not a setcookie")
                        try:
                            regexs[i('name')[0].string]['appendcookie'] = i('appendcookie')[0].string
                        except:
                            addon_log("Regex: -- Not a appendcookie")
                                                    
                        try:
                            regexs[i('name')[0].string]['ignorecache'] = i('ignorecache')[0].string
                        except:
                            addon_log("Regex: -- no ignorecache")
                        #try:
                        #    regexs[i('name')[0].string]['ignorecache'] = i('ignorecache')[0].string
                        #except:
                        #    addon_log("Regex: -- no ignorecache")            

                    regexs = urllib.quote(repr(regexs))
                    return regexs
                    #print regexs
                except:
                    regexs = None
                    addon_log('regex Error: '+name.encode('utf-8', 'ignore'))
#copies from lamda's implementation
def get_ustream(url):
    try:
        for i in range(1, 51):
            result = getUrl(url)
            if "EXT-X-STREAM-INF" in result: return url
            if not "EXTM3U" in result: return
            xbmc.sleep(2000)
        return
    except:
        return
        
 
def getRegexParsed(regexs, url, cookieJar=None, forCookieJarOnly=False, recursiveCall=False, cachedPages=None,
                   rawPost=False, cookie_jar_file=None):#0,1,2 = URL, regexOnly, CookieJarOnly
        if not cachedPages:
            cachedPages = {}
        if not recursiveCall:
            regexs = eval(urllib.unquote(regexs))
        #cachedPages = {}
        #print 'url',url
        doRegexs = re.compile('\$doregex\[([^\]]*)\]').findall(url)
        #print 'doRegexs',doRegexs,regexs
        setresolved=True
              
 


        for k in doRegexs:
            if k in regexs:
                #print 'processing ' ,k
                m = regexs[k]
                #print m
                cookieJarParam=False


                if  'cookiejar' in m: # so either create or reuse existing jar
                    #print 'cookiejar exists',m['cookiejar']
                    cookieJarParam=m['cookiejar']
                    if  '$doregex' in cookieJarParam:
                        cookieJar=getRegexParsed(regexs, m['cookiejar'],cookieJar,True, True,cachedPages)
                        cookieJarParam=True
                    else:
                        cookieJarParam=True
                #print 'm[cookiejar]',m['cookiejar'],cookieJar
                if cookieJarParam:
                    if cookieJar is None:
                        #print 'create cookie jar'
                        cookie_jar_file=None
                        if 'open[' in m['cookiejar']:
                            cookie_jar_file=m['cookiejar'].split('open[')[1].split(']')[0]
                            
                        cookieJar=getCookieJar(cookie_jar_file)
                        if cookie_jar_file:
                            saveCookieJar(cookieJar,cookie_jar_file)
                        #import cookielib
                        #cookieJar = cookielib.LWPCookieJar()
                        #print 'cookieJar new',cookieJar
                    elif 'save[' in m['cookiejar']:
                        cookie_jar_file=m['cookiejar'].split('save[')[1].split(']')[0]
                        complete_path=os.path.join(profile,cookie_jar_file)
                        print 'complete_path',complete_path
                        saveCookieJar(cookieJar,cookie_jar_file)
                        
 
                if  m['page'] and '$doregex' in m['page']:
                    m['page']=getRegexParsed(regexs, m['page'],cookieJar,recursiveCall=True,cachedPages=cachedPages)

                if 'setcookie' in m and m['setcookie'] and '$doregex' in m['setcookie']:
                    m['setcookie']=getRegexParsed(regexs, m['setcookie'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
                if 'appendcookie' in m and m['appendcookie'] and '$doregex' in m['appendcookie']:
                    m['appendcookie']=getRegexParsed(regexs, m['appendcookie'],cookieJar,recursiveCall=True,cachedPages=cachedPages)

                 
                if  'post' in m and '$doregex' in m['post']:
                    m['post']=getRegexParsed(regexs, m['post'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
                    print 'post is now',m['post']

                if  'rawpost' in m and '$doregex' in m['rawpost']:
                    m['rawpost']=getRegexParsed(regexs, m['rawpost'],cookieJar,recursiveCall=True,cachedPages=cachedPages,rawPost=True)
                    #print 'rawpost is now',m['rawpost']
  
                if 'rawpost' in m and '$epoctime$' in m['rawpost']:
                    m['rawpost']=m['rawpost'].replace('$epoctime$',getEpocTime())
  
                if 'rawpost' in m and '$epoctime2$' in m['rawpost']:
                    m['rawpost']=m['rawpost'].replace('$epoctime2$',getEpocTime2())

  
                link=''
                if m['page'] and m['page'] in cachedPages and not 'ignorecache' in m and forCookieJarOnly==False :
                    link = cachedPages[m['page']]
                else:
                    if m['page'] and  not m['page']=='' and  m['page'].startswith('http'):
                        if '$epoctime$' in m['page']:
                            m['page']=m['page'].replace('$epoctime$',getEpocTime())
                        if '$epoctime2$' in m['page']:
                            m['page']=m['page'].replace('$epoctime2$',getEpocTime2())

                        #print 'Ingoring Cache',m['page']
                        page_split=m['page'].split('|')
                        pageUrl=page_split[0]
                        header_in_page=None
                        if len(page_split)>1:
                            header_in_page=page_split[1]
                        req = urllib2.Request(pageUrl)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')
                        if 'refer' in m:
                            req.add_header('Referer', m['refer'])
                        if 'agent' in m:
                            req.add_header('User-agent', m['agent'])
                        if 'x-req' in m:
                            req.add_header('X-Requested-With', m['x-req'])
                        if 'x-forward' in m:
                            req.add_header('X-Forwarded-For', m['x-forward'])
                        if 'setcookie' in m:
                            print 'adding cookie',m['setcookie']
                            req.add_header('Cookie', m['setcookie'])
                        if 'appendcookie' in m:
                            print 'appending cookie to cookiejar',m['appendcookie']
                            cookiestoApend=m['appendcookie']
                            cookiestoApend=cookiestoApend.split(';')
                            for h in cookiestoApend:
                                n,v=h.split('=')
                                w,n= n.split(':')
                                ck = cookielib.Cookie(version=0, name=n, value=v, port=None, port_specified=False, domain=w, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
                                cookieJar.set_cookie(ck)

                                

                            
                        if 'origin' in m:
                            req.add_header('Origin', m['origin'])
                        if header_in_page:
                            header_in_page=header_in_page.split('&')
                            for h in header_in_page:
                                n,v=h.split('=')
                                req.add_header(n,v)


                        if not cookieJar is None:
                            #print 'cookieJarVal',cookieJar
                            cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
                            opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
                            opener = urllib2.install_opener(opener)
                            if 'noredirect' in m:
                                opener2 = urllib2.build_opener(NoRedirection)
                                opener = urllib2.install_opener(opener2)
                                
                        if 'connection' in m:
                            print '..........................connection//////.',m['connection']
                            from keepalive import HTTPHandler
                            keepalive_handler = HTTPHandler()
                            opener = urllib2.build_opener(keepalive_handler)
                            urllib2.install_opener(opener)
                            
                        #print 'after cookie jar'
                        post=None

                        if 'post' in m:
                            postData=m['post']
                            if '$LiveStreamRecaptcha' in postData:
                                (captcha_challenge,catpcha_word)=processRecaptcha(m['page'])
                                if captcha_challenge:
                                    postData+='recaptcha_challenge_field:'+captcha_challenge+',recaptcha_response_field:'+catpcha_word
                            splitpost=postData.split(',')
                            post={}
                            for p in splitpost:
                                n=p.split(':')[0]
                                v=p.split(':')[1]
                                post[n]=v
                            post = urllib.urlencode(post)

                        if 'rawpost' in m:
                            post=m['rawpost']
                            if '$LiveStreamRecaptcha' in post:
                                (captcha_challenge,catpcha_word)=processRecaptcha(m['page'])
                                if captcha_challenge:
                                   post+='&recaptcha_challenge_field='+captcha_challenge+'&recaptcha_response_field='+catpcha_word


                            

                        if post:
                            response = urllib2.urlopen(req,post)
                        else:
                            response = urllib2.urlopen(req)

                        link = response.read()
                        link=javascriptUnEscape(link)
                        #print link This just print whole webpage in LOG
                        if 'includeheaders' in m:
                            link+=str(response.headers.get('Set-Cookie'))

                        response.close()
                        cachedPages[m['page']] = link
                        #print link
                        #print 'store link for',m['page'],forCookieJarOnly
                        
                        if forCookieJarOnly:
                            return cookieJar# do nothing
                    elif m['page'] and  not m['page'].startswith('http'):
                        if m['page'].startswith('$pyFunction:'):
                            val=doEval(m['page'].split('$pyFunction:')[1],'',cookieJar )
                            if forCookieJarOnly:
                                return cookieJar# do nothing
                            link=val
                        else:
                            link=m['page']
                if '$pyFunction:playmedia(' in m['expre'] or 'ActivateWindow'  in m['expre']   or  any(x in url for x in g_ignoreSetResolved):
                    setresolved=False
                if  '$doregex' in m['expre']:
                    m['expre']=getRegexParsed(regexs, m['expre'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
                    
                
                if not m['expre']=='':
                    print 'doing it ',m['expre']
                    if '$LiveStreamCaptcha' in m['expre']:
                        val=askCaptcha(m,link,cookieJar)
                        #print 'url and val',url,val
                        url = url.replace("$doregex[" + k + "]", val)
                    elif m['expre'].startswith('$pyFunction:'):
                        #print 'expeeeeeeeeeeeeeeeeeee',m['expre']
                        val=doEval(m['expre'].split('$pyFunction:')[1],link,cookieJar )
                        if 'ActivateWindow' in m['expre']: return 
                        print 'still hre'
                        print 'url k val',url,k,val

                        url = url.replace("$doregex[" + k + "]", val)
                    else:
                        if not link=='':
                            reg = re.compile(m['expre']).search(link)
                            val=''
                            try:
                                val=reg.group(1).strip()
                            except: traceback.print_exc()
                        else:
                            val=m['expre']
                        if rawPost:
                            print 'rawpost'
                            val=urllib.quote_plus(val)
                        if 'htmlunescape' in m:
                            #val=urllib.unquote_plus(val)
                            import HTMLParser
                            val=HTMLParser.HTMLParser().unescape(val)                     
                        url = url.replace("$doregex[" + k + "]", val)
                        #return val
                else:           
                    url = url.replace("$doregex[" + k + "]",'')
        if '$epoctime$' in url:
            url=url.replace('$epoctime$',getEpocTime())
        if '$epoctime2$' in url:
            url=url.replace('$epoctime2$',getEpocTime2())

        if '$GUID$' in url:
            import uuid
            url=url.replace('$GUID$',str(uuid.uuid1()).upper())
        if '$get_cookies$' in url:
            url=url.replace('$get_cookies$',getCookiesString(cookieJar))   

        if recursiveCall: return url
        print 'final url',url
        if url=="": 
            return
        else:
            return url,setresolved

            
        
def getmd5(t):
    import hashlib
    h=hashlib.md5()
    h.update(t)
    return h.hexdigest()

def decrypt_vaughnlive(encrypted):
    retVal=""
    for val in encrypted.split(':'):
        retVal+=chr(int(val.replace("0m0",""))/84/5)
    return retVal

def playmedia(media_url):
    try:
        import  CustomPlayer
        player = CustomPlayer.MyXBMCPlayer()
        listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=media_url )
        player.play( media_url,listitem)
        xbmc.sleep(1000)
        while player.is_active:
            xbmc.sleep(200)
    except:
        traceback.print_exc()
    return ''
    
        
def get_saw_rtmp(page_value, referer=None):
    if referer:
        referer=[('Referer',referer)]
    if page_value.startswith("http"):
        page_url=page_value
        page_value= getUrl(page_value,headers=referer)

    str_pattern="(eval\(function\(p,a,c,k,e,(?:r|d).*)"

    reg_res=re.compile(str_pattern).findall(page_value)
    r=""
    if reg_res and len(reg_res)>0:
        for v in reg_res:
            r1=get_unpacked(v)
            r2=re_me(r1,'\'(.*?)\'')
            if 'unescape' in r1:
                r1=urllib.unquote(r2)
            r+=r1+'\n'
        print 'final value is ',r
        
        page_url=re_me(r,'src="(.*?)"')
        
        page_value= getUrl(page_url,headers=referer)

    #print page_value

    rtmp=re_me(page_value,'streamer\'.*?\'(.*?)\'\)')
    playpath=re_me(page_value,'file\',\s\'(.*?)\'')

    
    return rtmp+' playpath='+playpath +' pageUrl='+page_url
    
def get_leton_rtmp(page_value, referer=None):
    if referer:
        referer=[('Referer',referer)]
    if page_value.startswith("http"):
        page_value= getUrl(page_value,headers=referer)
    str_pattern="var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
    reg_res=re.compile(str_pattern).findall(page_value)[0] 

    a,b,c,d,f,v= reg_res
    f=int(f)
    a=int(a)/f
    b=int(b)/f
    c=int(c)/f
    d=int(d)/f

    ret= 'rtmp://' + str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d) + v
    return ret

def SaveToFile(file_name,page_data,append=False):
    if append:
        f = open(file_name, 'a')
        f.write(page_data)
        f.close()        
    else:
        f=open(file_name,'wb')
        f.write(page_data)
        f.close()
        return ''
    
def LoadFile(file_name):
    f=open(file_name,'rb')
    d=f.read()
    f.close()
    return d
    
def get_packed_iphonetv_url(page_data):
    import re,base64,urllib

    s=page_data
    while 'geh(' in s:
        if s.startswith('lol('): s=s[5:-1]
#        print 's is ',s
        s=re.compile('"(.*?)"').findall(s)[0]
        s=  base64.b64decode(s)
        s=urllib.unquote(s)
    print s
    return s

def get_ferrari_url(page_data):
    print 'get_dag_url2',page_data
    page_data2=getUrl(page_data)
    patt='(http.*)'
    import uuid
    playback=str(uuid.uuid1()).upper()
    links=re.compile(patt).findall(page_data2)
    headers=[('X-Playback-Session-Id',playback)]
    for l in links:
        try:
                page_datatemp=getUrl(l,headers=headers)

        except: pass
    
    return page_data+'|&X-Playback-Session-Id='+playback

    
def get_dag_url(page_data):
    print 'get_dag_url',page_data
    if page_data.startswith('http://dag.total-stream.net'):
        headers=[('User-Agent','Verismo-BlackUI_(2.4.7.5.8.0.34)')]
        page_data=getUrl(page_data,headers=headers)

    if '127.0.0.1' in page_data:
        return revist_dag(page_data)
    elif re_me(page_data, 'wmsAuthSign%3D([^%&]+)') != '':
        final_url = re_me(page_data, '&ver_t=([^&]+)&') + '?wmsAuthSign=' + re_me(page_data, 'wmsAuthSign%3D([^%&]+)') + '==/mp4:' + re_me(page_data, '\\?y=([^&]+)&')
    else:
        final_url = re_me(page_data, 'href="([^"]+)"[^"]+$')
        if len(final_url)==0:
            final_url=page_data
    final_url = final_url.replace(' ', '%20')
    return final_url

def re_me(data, re_patten):
    match = ''
    m = re.search(re_patten, data)
    if m is not None:
        match = m.group(1)
    else:
        match = ''
    return match

def revist_dag(page_data):
    final_url = ''
    if '127.0.0.1' in page_data:
        final_url = re_me(page_data, '&ver_t=([^&]+)&') + ' live=true timeout=15 playpath=' + re_me(page_data, '\\?y=([a-zA-Z0-9-_\\.@]+)')
        
    if re_me(page_data, 'token=([^&]+)&') != '':
        final_url = final_url + '?token=' + re_me(page_data, 'token=([^&]+)&')
    elif re_me(page_data, 'wmsAuthSign%3D([^%&]+)') != '':
        final_url = re_me(page_data, '&ver_t=([^&]+)&') + '?wmsAuthSign=' + re_me(page_data, 'wmsAuthSign%3D([^%&]+)') + '==/mp4:' + re_me(page_data, '\\?y=([^&]+)&')
    else:
        final_url = re_me(page_data, 'HREF="([^"]+)"')

    if 'dag1.asx' in final_url:
        return get_dag_url(final_url)

    if 'devinlivefs.fplive.net' not in final_url:
        final_url = final_url.replace('devinlive', 'flive')
    if 'permlivefs.fplive.net' not in final_url:
        final_url = final_url.replace('permlive', 'flive')
    return final_url


def get_unwise( str_eval):
    page_value=""
    try:        
        ss="w,i,s,e=("+str_eval+')' 
        exec ss
        page_value=unwise_func(w,i,s,e)
    except: traceback.print_exc(file=sys.stdout)
    #print 'unpacked',page_value
    return page_value
    
def unwise_func( w, i, s, e):
    lIll = 0
    ll1I = 0
    Il1l = 0
    ll1l = []
    l1lI = []
    while True:
        if lIll < 5:
            l1lI.append(w[lIll])
        elif lIll < len(w):
            ll1l.append(w[lIll])
        lIll+=1
        if ll1I < 5:
            l1lI.append(i[ll1I])
        elif ll1I < len(i):
            ll1l.append(i[ll1I])
        ll1I+=1
        if Il1l < 5:
            l1lI.append(s[Il1l])
        elif Il1l < len(s):
            ll1l.append(s[Il1l])
        Il1l+=1
        if len(w) + len(i) + len(s) + len(e) == len(ll1l) + len(l1lI) + len(e):
            break

    lI1l = ''.join(ll1l)#.join('');
    I1lI = ''.join(l1lI)#.join('');
    ll1I = 0
    l1ll = []
    for lIll in range(0,len(ll1l),2):
        #print 'array i',lIll,len(ll1l)
        ll11 = -1
        if ord(I1lI[ll1I]) % 2:
            ll11 = 1
        #print 'val is ', lI1l[lIll: lIll+2]
        l1ll.append(chr(    int(lI1l[lIll: lIll+2], 36) - ll11))
        ll1I+=1
        if ll1I >= len(l1lI):
            ll1I = 0
    ret=''.join(l1ll)
    if 'eval(function(w,i,s,e)' in ret:
        print 'STILL GOing'
        ret=re.compile('eval\(function\(w,i,s,e\).*}\((.*?)\)').findall(ret)[0] 
        return get_unwise(ret)
    else:
        print 'FINISHED'
        return ret
    
def get_unpacked( page_value, regex_for_text='', iterations=1, total_iteration=1):
    try:        
        reg_data=None
        if page_value.startswith("http"):
            page_value= getUrl(page_value)
        print 'page_value',page_value
        if regex_for_text and len(regex_for_text)>0:
            page_value=re.compile(regex_for_text).findall(page_value)[0] #get the js variable
        
        page_value=unpack(page_value,iterations,total_iteration)
    except: traceback.print_exc(file=sys.stdout)
    print 'unpacked',page_value
    if 'sav1live.tv' in page_value:
        page_value=page_value.replace('sav1live.tv','sawlive.tv') #quick fix some bug somewhere
        print 'sav1 unpacked',page_value
    return page_value

def unpack(sJavascript,iteration=1, totaliterations=2  ):
    print 'iteration',iteration
    if sJavascript.startswith('var _0xcb8a='):
        aSplit=sJavascript.split('var _0xcb8a=')
        ss="myarray="+aSplit[1].split("eval(")[0]
        exec ss
        a1=62
        c1=int(aSplit[1].split(",62,")[1].split(',')[0])
        p1=myarray[0]
        k1=myarray[3]
        with open('temp file'+str(iteration)+'.js', "wb") as filewriter:
            filewriter.write(str(k1))
        #aa=1/0
    else:

        aSplit = sJavascript.split("rn p}('")
        print aSplit
        
        p1,a1,c1,k1=('','0','0','')
     
        ss="p1,a1,c1,k1=('"+aSplit[1].split(".spli")[0]+')' 
        exec ss
    k1=k1.split('|')
    aSplit = aSplit[1].split("))'")
#    print ' p array is ',len(aSplit)
#   print len(aSplit )

    #p=str(aSplit[0]+'))')#.replace("\\","")#.replace('\\\\','\\')

    #print aSplit[1]
    #aSplit = aSplit[1].split(",")
    #print aSplit[0] 
    #a = int(aSplit[1])
    #c = int(aSplit[2])
    #k = aSplit[3].split(".")[0].replace("'", '').split('|')
    #a=int(a)
    #c=int(c)
    
    #p=p.replace('\\', '')
#    print 'p val is ',p[0:100],'............',p[-100:],len(p)
#    print 'p1 val is ',p1[0:100],'............',p1[-100:],len(p1)
    
    #print a,a1
    #print c,a1
    #print 'k val is ',k[-10:],len(k)
#    print 'k1 val is ',k1[-10:],len(k1)
    e = ''
    d = ''#32823

    #sUnpacked = str(__unpack(p, a, c, k, e, d))
    sUnpacked1 = str(__unpack(p1, a1, c1, k1, e, d,iteration))
    
    #print sUnpacked[:200]+'....'+sUnpacked[-100:], len(sUnpacked)
#    print sUnpacked1[:200]+'....'+sUnpacked1[-100:], len(sUnpacked1)
    
    #exec('sUnpacked1="'+sUnpacked1+'"')
    if iteration>=totaliterations:
#        print 'final res',sUnpacked1[:200]+'....'+sUnpacked1[-100:], len(sUnpacked1)
        return sUnpacked1#.replace('\\\\', '\\')
    else:
#        print 'final res for this iteration is',iteration
        return unpack(sUnpacked1,iteration+1)#.replace('\\', ''),iteration)#.replace('\\', '');#unpack(sUnpacked.replace('\\', ''))

def __unpack(p, a, c, k, e, d, iteration,v=1):

    #with open('before file'+str(iteration)+'.js', "wb") as filewriter:
    #    filewriter.write(str(p))
    while c >= 1:
        c = c -1
        if k[c]:
            aa=str(__itoaNew(c, a))
            if v==1:
                p=re.sub('\\b' + aa +'\\b', k[c], p)# THIS IS Bloody slow!
            else:
                p=findAndReplaceWord(p,aa,k[c])

            #p=findAndReplaceWord(p,aa,k[c])

            
    #with open('after file'+str(iteration)+'.js', "wb") as filewriter:
    #    filewriter.write(str(p))
    return p

#
#function equalavent to re.sub('\\b' + aa +'\\b', k[c], p)
def findAndReplaceWord(source_str, word_to_find,replace_with):
    splits=None
    splits=source_str.split(word_to_find)
    if len(splits)>1:
        new_string=[]
        current_index=0
        for current_split in splits:
            #print 'here',i
            new_string.append(current_split)
            val=word_to_find#by default assume it was wrong to split

            #if its first one and item is blank then check next item is valid or not
            if current_index==len(splits)-1:
                val='' # last one nothing to append normally
            else:
                if len(current_split)==0: #if blank check next one with current split value
                    if ( len(splits[current_index+1])==0 and word_to_find[0].lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890_') or (len(splits[current_index+1])>0  and splits[current_index+1][0].lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890_'):# first just just check next
                        val=replace_with
                #not blank, then check current endvalue and next first value
                else:
                    if (splits[current_index][-1].lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890_') and (( len(splits[current_index+1])==0 and word_to_find[0].lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890_') or (len(splits[current_index+1])>0  and splits[current_index+1][0].lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890_')):# first just just check next
                        val=replace_with
                        
            new_string.append(val)
            current_index+=1
        #aaaa=1/0
        source_str=''.join(new_string)
    return source_str        

def __itoa(num, radix):
#    print 'num red',num, radix
    result = ""
    if num==0: return '0'
    while num > 0:
        result = "0123456789abcdefghijklmnopqrstuvwxyz"[num % radix] + result
        num /= radix
    return result

def __itoaNew(cc, a):
    aa="" if cc < a else __itoaNew(int(cc / a),a) 
    cc = (cc % a)
    bb=chr(cc + 29) if cc> 35 else str(__itoa(cc,36))
    return aa+bb


def getCookiesString(cookieJar):
    try:
        cookieString=""
        for index, cookie in enumerate(cookieJar):
            cookieString+=cookie.name + "=" + cookie.value +";"
    except: pass
    #print 'cookieString',cookieString
    return cookieString


def saveCookieJar(cookieJar,COOKIEFILE):
    try:
        complete_path=os.path.join(profile,COOKIEFILE)
        cookieJar.save(complete_path,ignore_discard=True)
    except: pass

def getCookieJar(COOKIEFILE):

    cookieJar=None
    if COOKIEFILE:
        try:
            complete_path=os.path.join(profile,COOKIEFILE)
            cookieJar = cookielib.LWPCookieJar()
            cookieJar.load(complete_path,ignore_discard=True)
        except:
            cookieJar=None

    if not cookieJar:
        cookieJar = cookielib.LWPCookieJar()

    return cookieJar
    
def doEval(fun_call,page_data,Cookie_Jar):
    ret_val=''
    if functions_dir not in sys.path:
        sys.path.append(functions_dir)
    
    print fun_call
    try:
        py_file='import '+fun_call.split('.')[0]
        print py_file,sys.path
        exec py_file
        print 'done'
    except:
        print 'error in import'
        traceback.print_exc(file=sys.stdout)
    print 'ret_val='+fun_call
    exec ('ret_val='+fun_call)
    print ret_val
    #exec('ret_val=1+1')
    return str(ret_val)
    
def processRecaptcha(url):
    html_text=getUrl(url)
    recapChallenge=""
    solution=""
    cap_reg="<script.*?src=\"(.*?recap.*?)\""
    match =re.findall(cap_reg, html_text)
    captcha=False
    captcha_reload_response_chall=None
    solution=None

    if match and len(match)>0: #new shiny captcha!
        captcha_url=match[0]
        captcha=True

        cap_chall_reg='challenge.*?\'(.*?)\''
        cap_image_reg='\'(.*?)\''
        captcha_script=getUrl(captcha_url)
        recapChallenge=re.findall(cap_chall_reg, captcha_script)[0]
        captcha_reload='http://www.google.com/recaptcha/api/reload?c='
        captcha_k=captcha_url.split('k=')[1]
        captcha_reload+=recapChallenge+'&k='+captcha_k+'&captcha_k=1&type=image&lang=en-GB'
        captcha_reload_js=getUrl(captcha_reload)
        captcha_reload_response_chall=re.findall(cap_image_reg, captcha_reload_js)[0]
        captcha_image_url='http://www.google.com/recaptcha/api/image?c='+captcha_reload_response_chall
        if not captcha_image_url.startswith("http"):
            captcha_image_url='http://www.google.com/recaptcha/api/'+captcha_image_url
        import random
        n=random.randrange(100,1000,5)
        local_captcha = os.path.join(profile,str(n) +"captcha.img" )
        localFile = open(local_captcha, "wb")
        localFile.write(getUrl(captcha_image_url))
        localFile.close()
        solver = InputWindow(captcha=local_captcha)
        solution = solver.get()
        os.remove(local_captcha)
    return captcha_reload_response_chall ,solution

def getUrl(url, cookieJar=None,post=None, timeout=20, headers=None):


    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link


def get_decode(strtext,reg=None):
    if reg:
        strtext=re.findall(reg, strtext)[0]
    s1 = urllib.unquote(strtext[0: len(strtext)-1])
    t = ''
    for i in range( len(s1)):
        t += chr(ord(s1[i]) - s1[len(s1)-1])
    t=urllib.unquote(t)
    print t
    return t

def javascriptUnEscape(strtext):
    js=re.findall('unescape\(\'(.*?)\'',strtext)
    print 'js',js
    if (not js is None) and len(js)>0:
        for j in js:
            #print urllib.unquote(j)
            strtext=strtext.replace(j ,urllib.unquote(j))
    return strtext

iid=0
def askCaptcha(m,html_page, cookieJar):
    global iid
    iid+=1
    expre= m['expre']
    page_url = m['page']
    captcha_regex=re.compile('\$LiveStreamCaptcha\[([^\]]*)\]').findall(expre)[0]

    captcha_url=re.compile(captcha_regex).findall(html_page)[0]
    print expre,captcha_regex,captcha_url
    if not captcha_url.startswith("http"):
        page_='http://'+"".join(page_url.split('/')[2:3])
        if captcha_url.startswith("/"):
            captcha_url=page_+captcha_url
        else:
            captcha_url=page_+'/'+captcha_url
    
    local_captcha = os.path.join(profile, str(iid)+"captcha.jpg" )
    localFile = open(local_captcha, "wb")
    print ' c capurl',captcha_url
    req = urllib2.Request(captcha_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')
    if 'refer' in m:
        req.add_header('Referer', m['refer'])
    if 'agent' in m:
        req.add_header('User-agent', m['agent'])
    if 'setcookie' in m:
        print 'adding cookie',m['setcookie']
        req.add_header('Cookie', m['setcookie'])
        
    #cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    #opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    urllib2.urlopen(req)
    response = urllib2.urlopen(req)

    localFile.write(response.read())
    response.close()
    localFile.close()
    solver = InputWindow(captcha=local_captcha)
    solution = solver.get()
    return solution
    
class InputWindow(xbmcgui.WindowDialog):
    def __init__(self, *args, **kwargs):
        self.cptloc = kwargs.get('captcha')
        self.img = xbmcgui.ControlImage(335,30,624,60,self.cptloc)
        self.addControl(self.img)
        self.kbd = xbmc.Keyboard()

    def get(self):
        self.show()
        time.sleep(2)        
        self.kbd.doModal()
        if self.kbd.isConfirmed():
            text = self.kbd.getText()
            self.close()
            return text
        self.close()
        return False
    
def getEpocTime():
    import time
    return str(int(time.time()*1000))

def getEpocTime2():
    import time
    return str(int(time.time()))

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if params[len(params)-1]=='/':
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]
        return param


def getFavorites():
        items = json.loads(open(favorites).read())
        total = len(items)
        for i in items:
            name = i[0]
            url = i[1]
            iconimage = i[2]
            try:
                fanArt = i[3]
                if fanArt is None:
                    raise
            except:
                if addon.getSetting('use_thumb') == "true":
                    fanArt = iconimage
                else:
                    fanArt = fanart
            try: playlist = i[5]
            except: playlist = None
            try: regexs = i[6]
            except: regexs = None

            if i[4] == 0:
                addLink(url,name,iconimage,fanArt,'','','','fav',playlist,regexs,total)
            else:
                addDir(name,url,i[4],iconimage,fanart,'','','','','fav')


def addFavorite(name,url,iconimage,fanart,mode,playlist=None,regexs=None):
        favList = []
        try:
            # seems that after 
            name = name.encode('utf-8', 'ignore')
        except:
            pass
        if not os.path.exists(favorites):
            addon_log('Making Favorites File')
            favList.append((name,url,iconimage,fanart,mode,playlist,regexs))
            a = open(favorites, "w")
            a.write(json.dumps(favList))
            a.close()
        else:
            addon_log('Appending Favorites')
            a = open(favorites).read()
            data = json.loads(a)
            data.append((name,url,iconimage,fanart,mode))
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()


def rmFavorite(name):
        data = json.loads(open(favorites).read())
        for index in range(len(data)):
            if data[index][0]==name:
                del data[index]
                b = open(favorites, "w")
                b.write(json.dumps(data))
                b.close()
                break
        xbmc.executebuiltin("XBMC.Container.Refresh")


def play_playlist(name, mu_playlist):
        import urlparse
        if addon.getSetting('ask_playlist_items') == 'true':
            names = []
            for i in mu_playlist:
                d_name=urlparse.urlparse(i).netloc
                if d_name == '':
                    names.append(name)
                else:
                    names.append(d_name)
            dialog = xbmcgui.Dialog()
            index = dialog.select('Choose a video source', names)
            if index >= 0:
                if "&mode=19" in mu_playlist[index]:
                    xbmc.Player().play(urlsolver(mu_playlist[index].replace('&mode=19','')))
                elif "$doregex" in mu_playlist[index] :

                    sepate = mu_playlist[index].split('&regexs=')

                    url,setresolved = getRegexParsed(sepate[1], sepate[0])
                    xbmc.Player().play(url)
                else:
                    url = mu_playlist[index]
                    xbmc.Player().play(url)
        else:
            playlist = xbmc.PlayList(1) # 1 means video
            playlist.clear()
            item = 0
            for i in mu_playlist:
                item += 1
                info = xbmcgui.ListItem('%s) %s' %(str(item),name))
                playlist.add(i, info)
                xbmc.executebuiltin('playlist.playoffset(video,0)')


def addDir(name,url,mode,iconimage,fanart,description,genre,date,credits,showcontext=False,isItFolder=True):
        
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        liz.setProperty("Fanart_Image", fanart)
        if showcontext:
            contextMenu = []
            if showcontext == 'source':
                if name in str(SOURCES):
                    contextMenu.append(('Remove from Sources','XBMC.RunPlugin(%s?mode=8&name=%s)' %(sys.argv[0], urllib.quote_plus(name))))
            elif showcontext == 'download':
                contextMenu.append(('Download','XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            elif showcontext == 'fav':
                contextMenu.append(('Remove from Jericho Favorites','XBMC.RunPlugin(%s?mode=6&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isItFolder)

        return ok

def ytdl_download(url,title,media_type='video'):
    # play in xbmc while playing go back to contextMenu(c) to "!!Download!!"
    # Trial yasceen: seperate |User-Agent=
    import youtubedl
    if not url == '':
        if media_type== 'audio':
            youtubedl.single_YD(url,download=True,audio=True)
        else:
            youtubedl.single_YD(url,download=True)   
    elif xbmc.Player().isPlaying():
        import YDStreamExtractor
        if YDStreamExtractor.isDownloading():

            YDStreamExtractor.manageDownloads()
        else:
            xbmc_url = xbmc.Player().getPlayingFile()

            xbmc_url = xbmc_url.split('|User-Agent=')[0]
            info = {'url':xbmc_url,'title':title,'media_type':media_type}
            youtubedl.single_YD('',download=True,dl_info=info)    
    else:
        xbmc.executebuiltin("XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)")
 
## Lunatixz PseudoTV feature
def ascii(string):
    if isinstance(string, basestring):
        if isinstance(string, unicode):
           string = string.encode('ascii', 'ignore')
    return string
def uni(string, encoding = 'utf-8'):
    if isinstance(string, basestring):
        if not isinstance(string, unicode):
            string = unicode(string, encoding, 'ignore')
    return string
def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))

def sendJSON( command):
    data = ''
    try:
        data = xbmc.executeJSONRPC(uni(command))
    except UnicodeEncodeError:
        data = xbmc.executeJSONRPC(ascii(command))

    return uni(data)

#hakamac thanks Roman_V_M
def SetViewThumbnail():
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.confluence':
        xbmc.executebuiltin('Container.SetViewMode(500)')
    elif skin_used == 'skin.aeon.nox':
        xbmc.executebuiltin('Container.SetViewMode(511)') 
    else:
        xbmc.executebuiltin('Container.SetViewMode(500)')


def pluginquerybyJSON(url):
    json_query = uni('{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":["thumbnail","title","year","dateadded","fanart","rating","season","episode","studio"]},"id":1}') %url

    json_folder_detail = json.loads(sendJSON(json_query))
    for i in json_folder_detail['result']['files'] :
        url = i['file']
        name = removeNonAscii(i['label'])
        thumbnail = removeNonAscii(i['thumbnail'])
        try:
            fanart = removeNonAscii(i['fanart'])
        except Exception:
            fanart = ''
        try:
            date = i['year']
        except Exception:
            date = ''
        try:
            episode = i['episode']
            season = i['season']
            if episode == -1 or season == -1:
                description = ''
            else:
                description = '[COLOR yellow] S' + str(season)+'[/COLOR][COLOR lime] E' + str(episode) +'[/COLOR]'
        except Exception:
            description = ''
        try:
            studio = i['studio']
            if studio:
                description += '\n Studio:[COLOR steelblue] ' + studio[0] + '[/COLOR]'
        except Exception:
            studio = ''

        if i['filetype'] == 'file':
            addLink(url,name,thumbnail,fanart,description,'',date,'',None,'',total=len(json_folder_detail['result']['files']))
            #xbmc.executebuiltin("Container.SetViewMode(500)")

        else:
            addDir(name,url,53,thumbnail,fanart,description,'',date,'')
            #xbmc.executebuiltin("Container.SetViewMode(500)")

def addLink(url,name,iconimage,fanart,description,genre,date,showcontext,playlist,regexs,total,setCookie=""):
        #print 'url,name',url,name
        contextMenu =[]
        try:
            name = name.encode('utf-8')
        except: pass
        ok = True
       
        if regexs: 
            mode = '17'
           
            contextMenu.append(('[COLOR white]!!Download Currently Playing!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))           
        elif  any(x in url for x in resolve_url) and  url.startswith('http'):
            mode = '19'
          
            contextMenu.append(('[COLOR white]!!Download Currently Playing!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))           
        elif url.endswith('&mode=18'):
            url=url.replace('&mode=18','')
            mode = '18' 
          
            contextMenu.append(('[COLOR white]!!Download!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name)))) 
            if addon.getSetting('dlaudioonly') == 'true':
                contextMenu.append(('!!Download [COLOR seablue]Audio!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
                                        %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))                                     
        elif url.startswith('magnet:?xt=') or '.torrent' in url:
          
            if '&' in url and not '&amp;' in url :
                url = url.replace('&','&amp;')
            url = 'plugin://plugin.video.pulsar/play?uri=' + url
            mode = '12'
                     
        else: 
            mode = '12'
      
            contextMenu.append(('[COLOR white]!!Download Currently Playing!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))           
        u=sys.argv[0]+"?"
        play_list = False
      
        if playlist:
            if addon.getSetting('add_playlist') == "false":
                u += "url="+urllib.quote_plus(url)+"&mode="+mode
            else:
                u += "mode=13&name=%s&playlist=%s" %(urllib.quote_plus(name), urllib.quote_plus(str(playlist).replace(',','||')))
                name = name + '[COLOR lime] (' + str(len(playlist)) + ' items )[/COLOR]'
                play_list = True
        else:
            u += "url="+urllib.quote_plus(url)+"&mode="+mode
        if regexs:
            u += "&regexs="+regexs
        if not setCookie == '':
            u += "&setCookie="+urllib.quote_plus(setCookie)
  
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date })
        liz.setProperty("Fanart_Image", fanart)
        
        if (not play_list) and not any(x in url for x in g_ignoreSetResolved):#  (not url.startswith('plugin://plugin.video.f4mTester')):
            if regexs:
                if '$pyFunction:playmedia(' not in urllib.unquote_plus(regexs) and 'notplayable' not in urllib.unquote_plus(regexs)  :
                    #print 'setting isplayable',url, urllib.unquote_plus(regexs),url
                    liz.setProperty('IsPlayable', 'true')
            else:
                liz.setProperty('IsPlayable', 'true')
        else:
            addon_log( 'NOT setting isplayable'+url)
       
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(
                    ('Remove from Jericho Favorites','XBMC.RunPlugin(%s?mode=6&name=%s)'
                     %(sys.argv[0], urllib.quote_plus(name)))
                     )
            elif not name in FAV:
                fav_params = (
                    '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
                    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart))
                    )
                if playlist:
                    fav_params += 'playlist='+urllib.quote_plus(str(playlist).replace(',','||'))
                if regexs:
                    fav_params += "&regexs="+regexs
                contextMenu.append(('Add to Jericho Favorites','XBMC.RunPlugin(%s)' %fav_params))
            liz.addContextMenuItems(contextMenu)
       
        if not playlist is None:
            if addon.getSetting('add_playlist') == "false":
                playlist_name = name.split(') ')[1]
                contextMenu_ = [
                    ('Play '+playlist_name+' PlayList','XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
                     %(sys.argv[0], urllib.quote_plus(playlist_name), urllib.quote_plus(str(playlist).replace(',','||'))))
                     ]
                liz.addContextMenuItems(contextMenu_)
        #print 'adding',name
 #       print url,totalitems
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,totalItems=total)
        #print 'added',name
        return ok

def playsetresolved(url,name,iconimage,setresolved=True):
    if setresolved:
        liz = xbmcgui.ListItem(name, iconImage=iconimage)
        liz.setInfo(type='Video', infoLabels={'Title':name})
        liz.setProperty("IsPlayable","true")
        liz.setPath(str(url))
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    else:
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')      


## Thanks to daschacka, an epg scraper for http://i.teleboy.ch/programm/station_select.php
##  http://forum.xbmc.org/post.php?p=936228&postcount=1076
def getepg(link):
        url=urllib.urlopen(link)
        source=url.read()
        url.close()
        source2 = source.split("Jetzt")
        source3 = source2[1].split('programm/detail.php?const_id=')
        sourceuhrzeit = source3[1].split('<br /><a href="/')
        nowtime = sourceuhrzeit[0][40:len(sourceuhrzeit[0])]
        sourcetitle = source3[2].split("</a></p></div>")
        nowtitle = sourcetitle[0][17:len(sourcetitle[0])]
        nowtitle = nowtitle.encode('utf-8')
        return "  - "+nowtitle+" - "+nowtime


def get_epg(url, regex):
        data = makeRequest(url)
        try:
            item = re.findall(regex, data)[0]
            return item
        except:
            addon_log('regex failed')
            addon_log(regex)
            return


xbmcplugin.setContent(int(sys.argv[1]), 'movies')

try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_GENRE)
except:
    pass

params=get_params()

url=None
name=None
mode=None
page=None
iconimage=None
fanart=FANART
playlist=None
fav_mode=None
regexs=None

try:
    url=urllib.unquote_plus(params["url"]).decode('utf-8')
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    fanart=urllib.unquote_plus(params["fanart"])
except:
    pass
try:
    page=int(params["page"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass
try:
    playlist=eval(urllib.unquote_plus(params["playlist"]).replace('||',','))
except:
    pass
try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    regexs=params["regexs"]
except:
    pass

addon_log("Mode: "+str(mode))
if not url is None:
    addon_log("URL: "+str(url.encode('utf-8')))
addon_log("Name: "+str(name))

if mode is None:
    addon_log("Index")
    if not addon.getSetting('policy1.0.5') == 'true':
        Privacy_Policy()
        addon.setSetting('policy1.0.5','true')
    JerichoIndex()

elif mode==1:
    addon_log("getData")
    getData(url,fanart)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==2:
    addon_log("getChannelItems")
    getChannelItems(name,url,fanart)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==3:
    addon_log("getSubChannelItems")
    getSubChannelItems(name,url,fanart)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==4:
    addon_log("getFavorites")
    getFavorites()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==5:
    addon_log("addFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,iconimage,fanart,fav_mode)

elif mode==6:
    addon_log("rmFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)

elif mode==12:
    addon_log("setResolvedUrl")
    if not url.startswith("plugin://plugin") or not any(x in url for x in g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
        print 'Not setting setResolvedUrl'
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')


elif mode==13:
    addon_log("play_playlist")
    play_playlist(name, playlist)

elif mode==17:
    addon_log("getRegexParsed")
    url,setresolved = getRegexParsed(regexs, url)
    if url:
        playsetresolved(url,name,iconimage,setresolved)
    else:
        xbmc.executebuiltin("XBMC.Notification(Jericho,Failed to extract regex. - "+"this"+",4000,"+icon+")")
elif mode==18:
    addon_log("youtubedl")
    try:
        import youtubedl
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(Jericho,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000,"")")
    stream_url=youtubedl.single_YD(url)
    playsetresolved(stream_url,name,iconimage)


elif mode==21:
    addon_log("download current file using youtube-dl service")
    ytdl_download('',name,'video')
elif mode==23:
    addon_log("get info then download")
    ytdl_download(url,name,'video') 
elif mode==24:
    addon_log("Audio only youtube download")
    ytdl_download(url,name,'audio')

elif mode==45:
    Privacy_Policy()

elif mode==46:
    News()

elif mode==47 :
    AddSports365Channels(url)
    
elif mode==48:
    url=base64.b64decode(url)
    playSports365(url.split('Sports365:')[1])

elif mode==53:
    addon_log("Requesting JSON-RPC Items")
    pluginquerybyJSON(url)
    
elif mode==60:
    playLiveResolver(url, name)
    
elif mode==61:
    livestreamer(url,filter)

elif mode==63:
    getbvlsSchedule()

if mode==70:
    addon_log("indexsport")
    indexsport()

if mode==71:
    JerichoIndex()
    
if mode==72:
    addon_log("indexlivesport")
    indexlivesport()
    
#if mode==74:
 #   addon_log("indexbvls")
  #  indexbvls()
    
if mode==75:
    addon_log("indexmuziek")
    indexmuziek()

elif mode==77:
    getUFC()

elif mode==78:
    PlayYouTube(url, name)

elif mode==79:
    getUFCnext(url)
    
elif mode==104:
    Catfeed2all()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode==105:
    Addthefeed2all(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode==106:
    Addwiz()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode==107:
    Addgoatd()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode==108:
    Addlive9()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==109:
    Catvipbox()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode==110:
    Addvipbox(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode==111:
    Addtuttosport()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode==112:
    AddDarts()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode == 113:
    getwizhdSchedule(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
elif mode == 114:
    getwizhdcats()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode == 115: footlive.Main()
elif mode == 116: footlive.List(url)
elif mode == 117: footlive.Liststreams(url)
    
elif mode == 220: xite.Main()
elif mode == 221: xite.List(url)
elif mode == 222: xite.Playvid(url, name)
elif mode == 227: foxsports.Main()
elif mode == 228: foxsports.List(url, page)
elif mode == 229: foxsports.SearchList(url)
elif mode == 230: foxsports.Search(url)
elif mode == 231: foxsports.Playvid(url, name)
elif mode == 232: ziggosporttotaal.Main()
elif mode == 233: ziggosporttotaal.List(url)
elif mode == 234: ziggosporttotaal.SearchList(url)
elif mode == 235: ziggosporttotaal.Search(url)
elif mode == 236: ziggosporttotaal.Playvid(url, name)
elif mode == 237: foxsports.MainSamenvattingen()
elif mode == 238: foxsports.MainDoelpunten()
elif mode == 239: foxsports.MainInterviews()
elif mode == 240: slamfm40.Main()
elif mode == 241: slamfm40.List(url)
elif mode == 242: streamhd.List()
elif mode == 243: streamhd.Playvid(url, name)
elif mode == 244: Hesgoals.Main()
elif mode == 245: Hesgoals.ListRacing(url)
elif mode == 246: Hesgoals.ListFootball(url)
elif mode == 247: Hesgoals.Playvid(url, name)
elif mode == 248: stream2watch.Main()
elif mode == 249: stream2watch.List(url)
elif mode == 250: stream2watch.ListStream(url)
elif mode == 251: livetvru.Main()
elif mode == 252: livetvru.List(url)
elif mode == 253: livetvru.ListStream(url)
elif mode == 254: fromhot.Main()
elif mode == 255: fromhot.List(url)
elif mode == 264: livefootballvideo.Main()
elif mode == 265: livefootballvideo.List(url)
elif mode == 266: livefootballvideo.ListTeams(url)
elif mode == 267: livefootballvideo.ListStreams(url)
elif mode == 268: sportp2p.List(url)
elif mode == 269: sportp2p.ListStreams(url)
elif mode == 270: showsporttv.Main()
elif mode == 271: showsporttv.List(url)
elif mode == 272: showsporttv.ListStream(url)
elif mode == 273: hdfree.Main()
elif mode == 274: hdfree.List(url)
elif mode == 275: mamahd.Main()
elif mode == 300: utils.playyt(url, name)
elif mode == 301: livefootballvideohighlights.ListHighlights(url)
elif mode == 302: livefootballvideohighlights.ListLatest(url)
elif mode == 303: livefootballvideohighlights.ListLElse(url)
elif mode == 304: livefootballvideohighlights.ListStream(url)
elif mode == 305: livefootballvideohighlights.get_PLAYlink(url)
elif mode == 306: Sportstream365.Main()
elif mode == 307: Sportstream365.List(url)
elif mode == 308: woopio.Main()
elif mode == 309: woopio.Competitions()
elif mode == 310: woopio.List(url)
elif mode == 311: woopio.Liststreams(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))