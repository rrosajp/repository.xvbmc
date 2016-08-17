#!/usr/bin/python
 
"""
	IF you copy/paste 'script.xvbmc.update' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""

#   script.xvbmc.update (XvBMC Update & Development 'Nederland')
#
#   Copyright (C) 2016
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


import re,base64,urllib,urllib2,uuid
import xbmc,xbmcgui,xbmcplugin
import os,shutil,time
import downloader
import extract

# import xbmcaddon
# Set the addon environment                    #
# addon = xbmcaddon.Addon('script.xvbmc.update')


#                  ProgTitle="XvBMC Update+Development"               #
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'script.xvbmc.update')
mediaPath = os.path.join(addonPath, 'media')
xvbmcfanart = os.path.join(addonPath, 'fanart.jpg')
dialog = xbmcgui.Dialog()
base='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'
#                  ProgTitle="XvBMC Update+Development"               #


#######################################################################
#						Define Menus
#######################################################################

def mainMenu():
	xbmc.executebuiltin("Container.SetViewMode(51)")
	addItem('[COLOR lime]XvBMC [B]S[/B]ervice[B]P[/B]ack 03 (25-06-2016)[/COLOR]', 'url', 1,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[COLOR red]XvBMC [B]S[/B]ervice[B]P[/B]ack (00 t/m 03) bulk pack[/COLOR]','url', 2,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]R[/B]efresh [B]A[/B]ddons[COLOR white]+[/COLOR][B]R[/B]epos', 'url', 3,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]O[/B]ver[B]C[/B]lock (Raspberry [COLOR white]Pi[/COLOR] **[B]only[/B]**)', 'url', 4,os.path.join(mediaPath, "dev.png"))	
	addItem('XvBMC [B]#DEV#[/B] Corner (Firmware-OS-etc)', 'url', 5,os.path.join(mediaPath, "dev.png"))
	addItem('[COLOR white]X[/COLOR]vBMC About (over & [COLOR dodgerblue][B]i[/B][/COLOR]nfo)', 'url', 6,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]S[/B]choonmaak/[B]M[/B]aintenance (v[COLOR white][B]3[/B][/COLOR])', 'url', 7,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[COLOR dimgray]XvBMC [B]T[/B]weaking[/COLOR]', 'url', 8,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[COLOR white][B]Back[/B][/COLOR]', 'url', 9,os.path.join(mediaPath, "dev.png"))


#######################################################################
#						Add to menus
#######################################################################

def addItem(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setArt({'fanart': xvbmcfanart})
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

#######################################################################
#						Parses Choice
#######################################################################
      
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

#######################################################################
#						Work Functions
#######################################################################

def ServicePack(url):
    verifyplatform()
#	\update\sp\03-servicepack.zip
    if dialog.yesno('XvBMC NL most recent ServicePacks','Download de laatste XvBMC ServicePack?',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(base)+'update/sp/03-servicepack.zip'
        path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, 'update.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            addonfolder = xbmc.translatePath(os.path.join('special://','home'))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - Updater","XvBMC-NL: doing some extracting VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            dialog.ok("XvBMC-NL ServicePack - Update finished", 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-ons do NOT work you probably should reboot first)')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/purge.py)')

def UpdateRollup(url):
    verifyplatform()
#	\update\sp\03-sp-rollup.zip
    if dialog.yesno('XvBMC NL ServicePack Update Rollup','Download ALLE XvBMC SP-updates (all-in-1)?',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(base)+'update/sp/03-sp-rollup.zip'
        path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, 'update.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            addonfolder = xbmc.translatePath(os.path.join('special://','home'))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - Updater","XvBMC-NL: doing some extracting VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            dialog.ok("XvBMC-NL ServicePack - RollUp finished", 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-ons do NOT work you probably should reboot first)')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/purge.py)')


def forceRefresh():
#	http://kodi.wiki/view/List_of_built-in_functions
	xbmc.executebuiltin('UpdateLocalAddons')
	dialog.ok("XvBMC Nederland", "Force Refresh Repos and Update LocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	xbmc.executebuiltin("ReloadSkin()")


def xvbmcOverclock(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.xvbmc.oc')))
    if pluginpath: xbmc.executebuiltin("XBMC.RunAddon(script.xvbmc.oc)")
    else:
        url=base64.b64decode(base)+'script.xvbmc.oc/script.xvbmc.oc-3.03.zip'
        path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, 'script.xvbmc.oc-3.03.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            addonfolder = xbmc.translatePath(os.path.join('special://','home','addons',''))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - Updater","XvBMC-#OC: doing some extracting VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            print '=== Kodi.#OC XvBMC Nederland ==='
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("RunAddon(script.xvbmc.oc)")


def subDEVmenu(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.xvbmc.dev')))
    if pluginpath: xbmc.executebuiltin("XBMC.RunAddon(script.xvbmc.dev)")
    else:
        url=base64.b64decode(base)+'script.xvbmc.dev/script.xvbmc.dev-3.04.zip'
        path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, 'script.xvbmc.dev-3.04.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            addonfolder = xbmc.translatePath(os.path.join('special://','home','addons',''))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - Updater","XvBMC-#DEV: doing some extracting VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            print '=== Kodi.#DEV XvBMC Nederland ==='
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("RunAddon(script.xvbmc.dev)")


def xvbmcTweak():
#	EPiC XvBMC user preferences and tweaking
	dialog.ok("XvBMC NL Tweaks", "EPiC XvBMC Tweaking bitches...", "Coming soon to a theater near you ;-P")


def xvbmcMaintenance(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.schoonmaak')))
    if pluginpath: xbmc.executebuiltin("RunAddon(script.schoonmaak)")
    else:
        url=base64.b64decode(base)+'script.schoonmaak/script.schoonmaak-1.10.10.zip'
        path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, 'script.schoonmaak-1.10.10.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            addonfolder = xbmc.translatePath(os.path.join('special://','home','addons',''))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - Updater","XvBMC-#Maintenance: doing some extracting VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            print '=== Kodi.#CrapClean XvBMC Nederland ==='
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("RunAddon(script.schoonmaak)")


def closeandexit():
#	http://kodi.wiki/view/Keyboard.xml
	xbmc.executebuiltin('Action(back)')


#######################################################################
#						ABOUT
#######################################################################
def AboutXvBMC():
	text = ''
	twit = 'https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/readme.xml'
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
	    dte = '[COLOR lime][B]'+dte+'[/B][/COLOR]'
	    text = text+dte+'\n'+status+'\n'+'\n'
	infoTXT('[COLOR lime]Over XvBMC Nederland[/COLOR]', text)	

def infoTXT(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
	try:
	    xbmc.sleep(10)
	    retry -= 1
	    win.getControl(1).setLabel(heading)
	    win.getControl(5).setText(text)
	    return
	except:
	    pass


def verifyplatform():
#   choice = dialog.yesno('XvBMC Nederland (Dutch)', '*verify platform*', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
#   if choice == 0:
#       return
#   elif choice == 1:
#       pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message read this first.", "[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, but...","No guarantees for OSX [B];-p[/B]")
    elif myplatform == 'linux': #Linux
        #dialog.ok("XvBMC NL most recent ServicePacks", "Download de laatste XvBMC (Open-/LibreELEC) ServicePack?",'','')
        print '=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ==='	
    elif myplatform == 'android': # Android  
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message read this first.", "There\'s also a specific [COLOR=white]XvBMC[/COLOR]\'s Android add-on update(r)","(enkel en alleen voor specifieke bonus Android add-on updates)")
    elif myplatform == 'windows': # Windows
        #dialog.ok("XvBMC NL most recent ServicePacks", "Download de laatste XvBMC (Windows) ServicePack?",'','')
        print '=== Download de laatste XvBMC (Windows) ServicePack ==='		
    else: #ATV
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message read this first.", "[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, but...","No guarantees for ATV [B];-p[/B]")    

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'


#######################################################################
#						START MAIN
#######################################################################              

params=get_params()
url=None
name=None
mode=None
fanart=None
iconimage=None

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
try:    
		fanart=urllib.unquote_plus(params["fanart"])
except: 
		pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass

print "Base: "+str(base)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Fanart: "+str(fanart)
print "IconImage: "+str(iconimage)

if mode==None or url==None or len(url)<1:
	mainMenu()

elif mode==1:
#	ServicePack(url)
#	dialog.ok("XvBMC NL most recent ServicePacks", 'Disabled: download laatste XvBMC ServicePack','', 'Download onze nieuwe (Pi) V3-image dd. 09-08-2016 !!!')
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'linux': # Open-/LibreELEC
        dialog.ok("XvBMC NL most recent ServicePacks", 'Disabled: download laatste XvBMC ServicePack','', 'Download onze nieuwe (Pi) V3-image dd. 09-08-2016 !!!')
    else: #rest
        ServicePack(url)

elif mode==2:
#	UpdateRollup(url)
#	dialog.ok("XvBMC NL ServicePack Update Rollup", 'Disabled: download alle XvBMC SP-updates (all-in-1)','', 'Download onze nieuwe (Pi) V3-image dd. 09-08-2016 !!!')
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'linux': # Open-/LibreELEC
        dialog.ok("XvBMC NL ServicePack Update Rollup", 'Disabled: download alle XvBMC SP-updates (all-in-1)','', 'Download onze nieuwe (Pi) V3-image dd. 09-08-2016 !!!')
    else: #rest
        UpdateRollup(url)

elif mode==3:
	forceRefresh()

elif mode==4:
	xvbmcOverclock(url)

elif mode==5:
    subDEVmenu(url)

elif mode==6:	
	AboutXvBMC()

elif mode==7:
	xvbmcMaintenance(url)

elif mode==8:
    xvbmcTweak()

elif mode==9:
	closeandexit()


xbmcplugin.endOfDirectory(int(sys.argv[1]))

