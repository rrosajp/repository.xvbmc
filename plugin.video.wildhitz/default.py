import urllib2,urllib,cgi, re, os
import urlparse
import HTMLParser
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import xml.etree.ElementTree as ET
import random



          

    
addon = xbmcaddon.Addon('plugin.video.wildhitz')
addonname = addon.getAddonInfo('name')
#icon = addon.getAddonInfo('icon')
addon_id = 'plugin.video.wildhitz'
selfAddon = xbmcaddon.Addon(id=addon_id)
profile_path =  xbmc.translatePath(selfAddon.getAddonInfo('profile'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8')) 
icon = os.path.join(home, 'icon.png')
FANART = os.path.join(home, 'fanart.jpg')

addonDir = addon.getAddonInfo('path').decode("utf-8")
libDir = os.path.join(addonDir, 'resources', 'lib')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
favorites = os.path.join(profile, 'favorites')
history = os.path.join(profile, 'history')
 


addon_handle = int(sys.argv[1])
pluginhandle = int(sys.argv[1])





class NoRedirection(urllib2.HTTPErrorProcessor):
   def http_response(self, request, response):
       return response
   https_response = http_response


playlist = 'http://wildhitz.nl/jw/playlist.src.rss.php?plc=&q=jw5&autostart=true&repeat=list'

top3= 'http://wildhitz.nl/jw/playlist.src.rss.php?plc=22465216597e2084839ce5f58681264b&q=jw5&autostart=true&repeat=list'

xml_regex = '<title>(.*?)</title>\s*<jwplayer:file>(.*?)</jwplayer:file>'

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
		link = 'index.html'
		return link


def addLink(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=5"
    ok = True
    liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
    return ok

def addDir(name,url,mode,iconimage,fanart,description,genre,date,credits,isItFolder=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        liz.setProperty("Fanart_Image", fanart)

        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isItFolder)
        return ok







def GetHTML(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link




def Addtypes():
   addDir('Playlist' ,'playlist',2,icon ,  FANART,'','','','')
   addDir('Weekendmix' ,'weekendmix',3,icon ,  FANART,'','','','')
   addDir('Top 3' ,'top3',4,icon ,  FANART,'','','','')


def Wildhitz_playlist():
   pl=xbmc.PlayList(1)
   pl.clear()
   xml = make_request(playlist)
   #xml = filter(lambda x: not x.isspace(), xml)
   xml = re.compile(xml_regex, re.DOTALL).findall(xml)
   for title, url in xml:
      #if title != "  -  ":
      listitem = xbmcgui.ListItem('WildHitz - '+title,thumbnailImage=icon)
      xbmc.PlayList(1).add(url, listitem)
   xbmc.Player().play(pl)


def Wildhitz_top3():
   pl=xbmc.PlayList(1)
   pl.clear()
   xml = make_request(top3)
   #xml = filter(lambda x: not x.isspace(), xml)
   xml = re.compile(xml_regex, re.DOTALL).findall(xml)
   for title, url in xml:
      #if title != "  -  ":
      listitem = xbmcgui.ListItem('WildHitz - '+title,thumbnailImage=icon)
      xbmc.PlayList(1).add(url, listitem)
   xbmc.Player().play(pl)




def Weekendmix():
   url = 'http://pastebin.com/raw/C0H0i8f9'
   content = make_request(url)
   root = ET.fromstring(content)
   items = root.findall('item')
   for item in items:
      title = item.find('title').text
      link = item.find('link').text
      addDir(title ,link,10,icon ,  FANART,'','','','')


def playmix(name,url):
   
   listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )

   xbmc.Player( xbmc.PLAYER_CORE_AUTO ).play( url, listitem)


def keyboard(url=None):
    keyboard = xbmc.Keyboard('', 'Search Artist:', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        if query == '' :
           return False
        else:
           Playlist(query)
           



def PutRequest(url):
    req_regex = '<title>(.*?)</title>'
    url = 'http://www.paradiseradio.org/sam/web/request.php?songID='+url
    request = GetHTML(url)
    match = re.compile(req_regex).findall(request)
    for dialogtext in match:
        if 'error' in request :
            match = re.compile('<h2 class=\"error\">(.*?)</h2>').findall(request)
            for status in match:
                dialog = xbmcgui.Dialog()
                dialog.ok(dialogtext, status, "Paradise Radio")
        if 'success' in request :
            match = re.compile('<h2 class=\"success\">(.*?)</h2>').findall(request)
            for status in match:
                dialog = xbmcgui.Dialog()
                dialog.ok(dialogtext, status, "Paradise Radio")

                





def Playlist(url):
   xml = '<?xml version="1.0"?>\n'+make_request(playlist)
   #xml = filter(lambda x: not x.isspace(), xml)
   xml = re.compile(xml_regex, re.DOTALL).findall(xml)
   for title, url in xml:
      if title is not "-":
         print title
         print url
         addDir(title ,url,5,icon ,  FANART,'','','','')
    



def getResponse(url):
    try:
        response = urllib2.urlopen(url, timeout=200)
        if response and response.getcode() == 200:
            return response
        else :
            return False
    except:
        return False
    









    
        





def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
				
	return param



params=get_params()
url=None
name=None
mode=None
linkType=None

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass


args = cgi.parse_qs(sys.argv[2][1:])
linkType=''
try:
	linkType=args.get('linkType', '')[0]
except:
	pass


print 	mode,url,linkType

try:
	if mode==None or url==None or len(url)<1:
		print "InAddTypes"
		Addtypes()
        elif mode==2 :
		Wildhitz_playlist()
        elif mode==3 :
		Weekendmix()
        elif mode==4 :
		Wildhitz_top3()

	elif mode==6 :
		keyboard(url)
	elif mode==10 :
		playmix(name,url)  		
		

      

    
	

except:
	print 'somethingwrong'
	traceback.print_exc(file=sys.stdout)
	

		
if not ( (mode==2 or mode==4 or mode==9 or mode==10 or mode==15 or mode==21 or mode==22 or mode==27 or mode==33 or mode==35 or mode==37 or mode==40 or mode==42 or mode==0)  )  :
	if mode==144:
		xbmcplugin.endOfDirectory(int(sys.argv[1]),updateListing=True)
	else:
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
