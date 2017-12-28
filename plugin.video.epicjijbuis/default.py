# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Credits to Coldkeys for the basics (sourcecode), Thx Bro...
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------
import base64,os,re,sys,time,xbmc,xbmcaddon,xbmcgui,xbmcplugin
import plugintools
import urllib,urllib2
addonID   = 'plugin.video.epicjijbuis'
ADDON     = xbmcaddon.Addon(id=addonID)
addon_id  = 'plugin.video.epicjijbuis'
addonInfo = xbmcaddon.Addon().getAddonInfo
AddonTitle= 'XvBMC Nederland'
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'plugin.video.epicjijbuis')
base      = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'
BASEURL   = "https://bit.ly/XvBMC-Pi"
dialog    = xbmcgui.Dialog()
local     = xbmcaddon.Addon(id=addonID)
icon      = local.getAddonInfo('icon')
icondir   = local.getAddonInfo('icon')
fanart    = local.getAddonInfo('fanart')
fanartdir = local.getAddonInfo('fanart')
artwork   = xbmc.translatePath(os.path.join('special://home', 'addons', addonID, '/'))
epicartwrk= base64.b64decode(base)+'plugin.video.epicjijbuis/ART/'
noxartwork= base64.b64decode(base)+'plugin.video.noxmusic/'
redartwork= base64.b64decode(base)+'plugin.video.redmusic/'
Terug     = "[COLOR dimgray]<<<back[/COLOR]"
whoami    = "[COLOR dimgray]\[B],,[/B]/ (^_^) \[B],,[/B]/[/COLOR]    [COLOR white]EPiC[/COLOR] JijBuis [COLOR white][B]C[/B][/COLOR]an't [COLOR white][B]B[/B][/COLOR]e [COLOR white][B]S[/B][/COLOR]topped    [COLOR dimgray]\[B],,[/B]/ (^_^) \[B],,[/B]/[/COLOR]"
def addonIcon():
    return artwork + 'icon.png'
YOUTUBE_CHANNEL_ID_1 = "UCeR1Vv0VULfsNDIk0-lO4pA/playlists"
YOUTUBE_CHANNEL_ID_2 = "UCVX6eEeIIScwApzNs7Uuvug/playlists"
YOUTUBE_CHANNEL_ID_3 = "DanceTrippinOfficial"
YOUTUBE_CHANNEL_ID_4 = "UCw39ZmFGboKvrHv4n6LviCA"
YOUTUBE_CHANNEL_ID_5 = "PLZ1f3amS4y1ffYEhGZDtawaEyRQQu69Bw"
YOUTUBE_CHANNEL_ID_6 = "detop40"
YOUTUBE_CHANNEL_ID_7 = "PLFgquLnL59alDqvbikpe5jUhFa_lLl8_H"
def infoDialog(message, heading=addonInfo('name'), icon=addonIcon(), time=3000):
    try:
        dialog.notification(heading, message, icon, time, sound=False)
    except:
        execute("Notification(%s,%s, %s, %s)" % (heading, message, time, icon))
def okDialog(line1, line2, line3, heading=addonInfo('name')):
    return dialog.ok(heading, line1, line2, line3)
def yesnoDialog(line1, line2, line3, heading=addonInfo('name'), nolabel='', yeslabel=''):
    return dialog.yesno(heading, line1, line2, line3, nolabel, yeslabel)
noxmusicchannellist=[
        ("Armin van Buuren", "user/arminvanbuuren", 'https://yt3.ggpht.com/-bp-G-1ubrMA/AAAAAAAAAAI/AAAAAAAAAAA/lysFIFc6AaQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DJ Kensel Official", "channel/UCSP9jzPSR8n4_BD15PJIyEA", 'https://yt3.ggpht.com/-6kRR5mlPbf4/AAAAAAAAAAI/AAAAAAAAAAA/tbEH9cBPh7c/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Hardwell", "user/robberthardwell", 'https://yt3.ggpht.com/-1T1SCHCg1FQ/AAAAAAAAAAI/AAAAAAAAAAA/8FY0PMmPr3I/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Martin Garrix", "user/MartinGarrix", 'https://yt3.ggpht.com/-KRv6BJdFwk8/AAAAAAAAAAI/AAAAAAAAAAA/pQpuy_-RPhE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Tiesto", "user/officialtiesto", 'https://yt3.ggpht.com/-IKUxTd9MtfU/AAAAAAAAAAI/AAAAAAAAAAA/b26T9-6Y2qU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Venus Music", "channel/UCwfMdhb-f02OsYR8T78aKeQ", 'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("W&W", "user/WandWmusic", 'https://yt3.ggpht.com/-XUlyqOk4meY/AAAAAAAAAAI/AAAAAAAAAAA/5I2gEh7OJ2Y/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DeepSense", "user/MrDeepSense", 'https://yt3.ggpht.com/-U15Ut65AO3I/AAAAAAAAAAI/AAAAAAAAAAA/wG_JGLcud7U/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Keep It Underground", "user/aliasmike2002", 'https://yt3.ggpht.com/--SezWJJO8q0/AAAAAAAAAAI/AAAAAAAAAAA/5SzkvVF1gZ8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Spectrum Music", "user/SpectrumRecordings", 'https://yt3.ggpht.com/-vzLxO7i5Qgk/AAAAAAAAAAI/AAAAAAAAAAA/NvJaOyJCRGE/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep Space House", "user/DeepSpaceHouse", 'https://yt3.ggpht.com/-YFwLXVl_Vqc/AAAAAAAAAAI/AAAAAAAAAAA/XjzlD4yTbNk/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep House Amsterdam", "user/DeepHouseAmsterdam", 'https://yt3.ggpht.com/-INq4Js7Kn4c/AAAAAAAAAAI/AAAAAAAAAAA/E1hfqVmqVu8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Indefinitely", "channel/UC3xS7KD-nL8dpireWEUIxNA", 'https://yt3.ggpht.com/-v-1eCp72Tfo/AAAAAAAAAAI/AAAAAAAAAAA/Ms6e0w5cEb8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Viet Melodic", "channel/UCqaay_q0YERQBEg4o5EjvZw", 'https://yt3.ggpht.com/-U9lOTob88oI/AAAAAAAAAAI/AAAAAAAAAAA/s-MRRhKbRxA/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep Territory", "channel/UCnfmB-zAnhvM13i8CczCA6g/featured", 'https://yt3.ggpht.com/-QTChEDkSUEk/AAAAAAAAAAI/AAAAAAAAAAA/EGo9VWg3jJk/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("XDeep Music", "channel/UCSSEXzYHBijpCPJdiZbS7mw", 'https://yt3.ggpht.com/-kS8xy0vSVDU/AAAAAAAAAAI/AAAAAAAAAAA/bggfl99bU7o/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Best Car Music Mixes", "channel/UC830NkyfSaql_EFNkmtSXxQ", 'https://yt3.ggpht.com/-yzl2Jg0nISI/AAAAAAAAAAI/AAAAAAAAAAA/Vy0ZnBcpNF4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DjRegard", "channel/UCw39ZmFGboKvrHv4n6LviCA", 'https://yt3.ggpht.com/-Z6Mnb8qdA7A/AAAAAAAAAAI/AAAAAAAAAAA/CeU6rdpFLHI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Dj Drop G", "channel/UCPg3xfvygstC-AkG2Fg3ZXw", 'https://yt3.ggpht.com/-0cirbz4I_PU/AAAAAAAAAAI/AAAAAAAAAAA/7nigAQzB9Tc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DJ ekki Music", "user/DJEkkiMusic", 'https://yt3.ggpht.com/-q2uL4uvohU8/AAAAAAAAAAI/AAAAAAAAAAA/dz13xu82IaA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep Mix Nation", "user/DeepMixNation", 'https://yt3.ggpht.com/-BA3TEtJOooQ/AAAAAAAAAAI/AAAAAAAAAAA/Jg3jjzr73Ec/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep House Nation", "channel/UCwfMdhb-f02OsYR8T78aKeQ", 'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("The Deep Sky", "channel/UCiwb-9kJYSsfLU23u6-67mw", 'https://yt3.ggpht.com/-OpItHD85Yek/AAAAAAAAAAI/AAAAAAAAAAA/Dxtacpi3R3U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Miss Deep Mix", "channel/UCT_v9nbT8As4mclOg_WK1-w", 'https://yt3.ggpht.com/-F6jOzGq1tlU/AAAAAAAAAAI/AAAAAAAAAAA/kTdpRJWn6bw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Maximise Deep", "channel/UC3oQei6hjfNt9PF3B0PnwAQ", 'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Major Deep", "channel/UCuyc9llVi6_49OF_yx4NtZw", 'https://yt3.ggpht.com/-B3-wWU7pbaQ/AAAAAAAAAAI/AAAAAAAAAAA/_oXKAnEwopU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep House Club", "channel/UCDS_jKale8ThWLwGRB15oow", 'https://yt3.ggpht.com/-xnkcEn0aKIc/AAAAAAAAAAI/AAAAAAAAAAA/B_SyhGZZxak/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Pulse Musification", "user/PulseMusicification", 'https://yt3.ggpht.com/-OJ6LMm0FIPk/AAAAAAAAAAI/AAAAAAAAAAA/dw61QOyY8RA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Club House Music", "user/DJGosha4TdiRadio", 'https://yt3.ggpht.com/-6Y_rcQ4QotA/AAAAAAAAAAI/AAAAAAAAAAA/iHSKU-T1usg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),    
        ("Best Music", "channel/UComEqi_pJLNcJzgxk4pPz_A", 'https://yt3.ggpht.com/-xIs9J9XA4hQ/AAAAAAAAAAI/AAAAAAAAAAA/4ktYY9TcTb0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Electro Dance Mixes", "user/Spart2", 'https://yt3.ggpht.com/-nevFJT9TzUk/AAAAAAAAAAI/AAAAAAAAAAA/w8nCecBOHy0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Only Music Hits TV", "user/OnlyMusicHitsTV11", 'https://yt3.ggpht.com/-D_Dt4745g04/AAAAAAAAAAI/AAAAAAAAAAA/WDvmapj0Lic/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Dj Daniel Sky", "channel/UC7Jr5B5todkiLE-1l32JYDQ", 'https://yt3.ggpht.com/-cZo2zaoXK2w/AAAAAAAAAAI/AAAAAAAAAAA/iPXcyvOAXnc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Eric Clapman", "user/ericclapman", 'https://yt3.ggpht.com/-HIVzO-P_Rk4/AAAAAAAAAAI/AAAAAAAAAAA/XPzAMMq2EpY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Electro Dance Movement", "user/ElectroDanceMovement", 'https://yt3.ggpht.com/-rnymhxYBlaU/AAAAAAAAAAI/AAAAAAAAAAA/ECz2jWvUodA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Crunkz", "user/TheCrunkiiyz", 'https://yt3.ggpht.com/-Se6L7HBPnLU/AAAAAAAAAAI/AAAAAAAAAAA/aE3VbVfFvqc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("The Deep Sky", "channel/UCiwb-9kJYSsfLU23u6-67mw", 'https://yt3.ggpht.com/-OpItHD85Yek/AAAAAAAAAAI/AAAAAAAAAAA/Dxtacpi3R3U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Base Deep", "channel/UC6LRklglaoc2ywIwmcv21qQ", 'https://yt3.ggpht.com/-RzQd-nnVVHI/AAAAAAAAAAI/AAAAAAAAAAA/Iz9UCjJlcD4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DEEP ZONE", "channel/UCfNwCpAb1ZH4rpKMyUsvRIg", 'https://yt3.ggpht.com/-FIpPIRSkYm8/AAAAAAAAAAI/AAAAAAAAAAA/_Wq0iMcwEbQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Feel The Sound", "channel/UCg5XZgxVytarljBn4ueKqkg", 'https://yt3.ggpht.com/-WNYR4e_2O9Y/AAAAAAAAAAI/AAAAAAAAAAA/5lnXVY-n_Bk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Ahmet KILIC", "user/djahmet008", 'https://yt3.ggpht.com/-c_Yi_sSVLDw/AAAAAAAAAAI/AAAAAAAAAAA/4jj4Z4_7Dbo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')]    
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==1 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        elif mode==2 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        elif mode==69 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def disabled():
    okDialog('[COLOR orange]add-on by [B]X[/B]v[B]BMC Nederland[/B]:[/COLOR]','','[COLOR lime]goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')
def epicxvbmcnl():
    plugintools.log("XvBMC.epicxvbmcnl")
    params = plugintools.get_params()
    url=None
    name=None
    mode=None
    iconimage=None
    fanart=None
    description=None
    try: url=urllib.unquote_plus(params["url"])
    except: pass
    try: name=urllib.unquote_plus(params["name"])
    except: pass
    try: iconimage=urllib.unquote_plus(params["iconimage"])
    except: pass
    try: mode=int(params["mode"])
    except: pass
    try: fanart=urllib.unquote_plus(params["fanart"])
    except: pass
    try: description=urllib.unquote_plus(params["description"])
    except: pass
    plugintools.log("EPiC "+str(AddonTitle))
    if mode==None or url==None or len(url)<1: main_list(params)
    elif mode==1: xbmc.executebuiltin('Action(back)')
    elif mode==2: disabled()
    elif mode==3: NoxMusic()
    elif mode==4: randomizer(params)
    else:
        pass
    plugintools.close_item_list()
def main_list(params):
    setView('movies', 'EPiC')
    plugintools.log("XvBMC.main_list "+repr(params))
    addDir(whoami,BASEURL,2,icondir,fanartdir,'')
    addDir('',BASEURL,2,icondir,fanartdir,'')
    plugintools.add_item( 
        title="[B][COLOR purple]EP[/B][COLOR dodgerblue]i[/COLOR][B]C[/B][/COLOR] [COLOR dimgray][B][COLOR darkmagenta]M[/COLOR][/B]usic [B][COLOR darkmagenta]V[/COLOR][/B]ideo [B][COLOR darkmagenta]C[/COLOR][/B]hannel (...it\'s like [COLOR mediumvioletred]MTV[/COLOR], [B]but[/B] bettâh...)[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail=icon,
        fanart=epicartwrk+'hooligan.jpg',
        folder=True )
    plugintools.add_item( 
        title="  [COLOR dimgray]-[/COLOR] Rockabilly/Psychobilly [COLOR dimgray](allesin1nl)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/PLPXmmKS-D--bd_OBbxpqVAQPiCXnFacx7/",
        thumbnail=epicartwrk+'rockabella.png',
        fanart=epicartwrk+'rockabilly.jpg',
        folder=True )
    plugintools.add_item( 
        title="  [COLOR dimgray]-[/COLOR] Rock AM Ring [COLOR dimgray](allesin1nl)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/PLPXmmKS-D--aRKdAID0t_7t6hP_FLncPj/",
        thumbnail=epicartwrk+'rockAMring.png',
        fanart=epicartwrk+'RaR.jpg',
        folder=True )
    addDir('',BASEURL,2,icondir,fanartdir,'')
    addDir('TOP[COLOR white]40[/COLOR] | [B]R[/B][COLOR white]&[/COLOR][B]B[/B] | miscellaneous | various | mo[COLOR white]\'[/COLOR] full-concerts | etc[COLOR white]...[/COLOR]',BASEURL,4,epicartwrk+'cbs.png',epicartwrk+'CBS.jpg','')
    addDir('',BASEURL,2,icondir,fanartdir,'')
    plugintools.add_item( 
        title="[COLOR red][8bit][/COLOR] RetroBit Music [COLOR dimgray](.:C.T.R.L:.)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/PLxQ6orh4rPn6F2ZkpEYlZ6VyopXNuGmQT/",
        thumbnail=epicartwrk+'8bit.png',
        fanart=epicartwrk+'RetroBits.jpg',
        folder=True )
    addDir('[COLOR dimgray][B]\'[/B][/COLOR][COLOR white]N[/COLOR]ox [COLOR white]M[/COLOR]usic[COLOR dimgray][B]\'[/B][/COLOR][B]  - [/B]Deep House, trance, electro... [COLOR dimgray](XvBMC-NL)[/COLOR]',BASEURL,3,noxartwork+'icon.png',noxartwork+'fanart.jpg','')
    plugintools.add_item( 
        title="Alles in [COLOR orange] [B]1 [/B][/COLOR]NL[B] - [/B]Live Music [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://archive.org/download/fanart_20170116/Live%20Music%20icon.png",
        fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        title="Alles in [COLOR orange] [B]1 [/B][/COLOR]NL[B] - [/B]DanceTrippin TV [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://archive.org/download/fanart_20170116/DanceIcon.png",
        fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        title="Carpool Karaoke by James Corden & guests [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://i4.mirror.co.uk/incoming/article4843959.ece/ALTERNATES/s615b/James-Corden.jpg",
        fanart=base64.b64decode(base)+'plugin.video.carpool-karaoke/'+'fanart.jpg',
        folder=True )
    plugintools.add_item( 
        title="DjRegard Official [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-Z6Mnb8qdA7A/AAAAAAAAAAI/AAAAAAAAAAA/CeU6rdpFLHI/s900-c-k-no-rj-c0xffffff/photo.jpg",
        fanart=base64.b64decode(base)+'plugin.video.djRegard/'+'fanart.jpg',
        folder=True )
    addDir('',BASEURL,2,icondir,fanartdir,'')
    addDir(Terug,BASEURL,1,icondir,fanartdir,'')
    addDir('',BASEURL,69,icondir,fanartdir,'')
def NoxMusic():
    setView('movies', 'EPiC')
    plugintools.log("XvBMC.Nox_list")
    addDir(whoami,BASEURL,2,icondir,fanartdir,'')
    addDir('',BASEURL,2,icondir,fanartdir,'')
    for name, id, icon in noxmusicchannellist:
        plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,fanart=icon,folder=True)
    addDir('',BASEURL,2,icondir,fanartdir,'')
    addDir(Terug,BASEURL,1,icondir,fanartdir,'')
    addDir('',BASEURL,69,icondir,fanartdir,'')
def randomizer(params):
    setView('movies', 'EPiC')
    plugintools.log("XvBMC.Random_list "+repr(params))
    addDir(whoami,BASEURL,2,icondir,fanartdir,'')
    addDir('',BASEURL,2,icondir,fanartdir,'')
    plugintools.add_item( 
        title="Miscellaneous \'[B]F[/B]ull [B]C[/B]oncerts\' [COLOR dimgray](\'ik doe een gok\' [COLOR white];-p[/COLOR])[/COLOR]",
        url='plugin://plugin.video.youtube/search/?q=full+concert&sp=CAMSBhABGAIgAQ%253D%253D',
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    plugintools.add_item( 
        title="[COLOR white]NL[/COLOR][B] - [/B]Top [B]40[/B] [COLOR dimgray](\'playlist\\afspeellijst\' is het complete overzicht)[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail=epicartwrk+'top40.png',
        fanart=epicartwrk+'LP40.jpg',
        folder=True )
    plugintools.add_item( 
        title="[COLOR white]NL[/COLOR][B] - [/B]Populairste [B]\"[/B]random[B]\"[/B] [B]Y[/B]ou[B]T[/B]ube tracks [COLOR dimgray] (popular music)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail=epicartwrk+'topNL.png',
        fanart=epicartwrk+'headphones40.jpg',
        folder=True )
    addDir('',BASEURL,2,icondir,fanartdir,'')
    plugintools.add_item( 
        title="[COLOR red][B]R[/B][/COLOR]ed[COLOR red] [B]M[/B][/COLOR]usic -MusicHits[B]\'[/B]17- Best Songs Playlist [COLOR dimgray](OneLoveCunt)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/PLw-VjHDlEOgvtnnnqWlTqByAtC7tXBg6D/",
        thumbnail=redartwork+'icon.png',
        fanart=redartwork+'fanart.jpg',
        folder=True )
    addDir('',BASEURL,2,icondir,fanartdir,'')
    plugintools.add_item( 
        title="Top [B]R[COLOR white]&[/COLOR]B[/B] Clips [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/PLPXmmKS-D--am3Ai7GjiyhrXk18worMAH/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    addDir('',BASEURL,2,icondir,fanartdir,'')
    addDir(Terug,BASEURL,1,icondir,fanartdir,'')
    addDir('',BASEURL,69,icondir,fanartdir,'')
def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if local.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % local.getSetting(viewType) )
epicxvbmcnl()

"""
    IF you copy/paste this please keep the credits -2- XvBMC-NL (and Coldkeys), Thx.
"""