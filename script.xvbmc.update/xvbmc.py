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


import re,urllib,urllib2,uuid
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
dialog = xbmcgui.Dialog()
base='https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/'
#                  ProgTitle="XvBMC Update+Development"               #


#######################################################################
#						Define Menus
#######################################################################

def mainMenu():
	xbmc.executebuiltin("Container.SetViewMode(51)")
	addItem('XvBMC [B]S[/B]ervice[B]P[/B]ack 03 (25-06-2016)', 'url', 1,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]S[/B]ervice[B]P[/B]ack (00 t/m 03) bulk pack','url', 2,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]R[/B]efresh [B]A[/B]ddons[COLOR white]+[/COLOR][B]R[/B]epos', 'url', 3,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]O[/B]ver[B]C[/B]lock (Raspberry [B]Pi[/B] **only**)', 'url', 4,os.path.join(mediaPath, "dev.png"))	
	addItem('XvBMC [B]#DEV#[/B] Corner (Firmware-OS-etc)', 'url', 5,os.path.join(mediaPath, "dev.png"))
	addItem('XvBMC [B]T[/B]weaking', 'url', 6,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]S[/B]choonmaak/[B]M[/B]aintenance (v[COLOR white]3[/COLOR])', 'url', 7,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[B][COLOR white]Back[/COLOR][/B]', 'url', 8,os.path.join(mediaPath, "dev.png"))


#######################################################################
#						Add to menus
#######################################################################

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
	
def addItem(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
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
#	\update\sp\03-servicepack.zip
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL most recent ServicePacks','Download de laatste XvBMC ServicePack?'):
		url=base+'update/sp/03-servicepack.zip'
		path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
		dp = xbmcgui.DialogProgress()
		dp.create("XvBMC Nederland","Updater: doing some VOODOO...",'', 'Please Wait')
		lib=os.path.join(path, 'update.zip')
		try:
			os.remove(lib)
		except:
			pass
		downloader.download(url, lib, dp)
		addonfolder = xbmc.translatePath(os.path.join('special://','home'))
		time.sleep(3)
		dp.update(0,"", "*Extracting ZiP Please Wait*")
		print '=== EXCTRACTING ServicePack ==='
		extract.all(lib,addonfolder,dp)
		dialog.ok("XvBMC-NL ServicePack-update finished", 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-ons do NOT work you probably should reboot first)')
		xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/purge.py)')
		xbmc.executebuiltin("UpdateLocalAddons")
		xbmc.executebuiltin("UpdateAddonRepos")

def UpdateRollup(url):
#	\update\sp\03-sp-rollup.zip
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL ServicePack Update Rollup','Download ALLE XvBMC SP-updates (all-in-1)?'):
		url=base+'update/sp/03-sp-rollup.zip'
		path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
		dp = xbmcgui.DialogProgress()
		dp.create("XvBMC Nederland","Updater: doing some VOODOO...",'', 'Please Wait')
		lib=os.path.join(path, 'update.zip')
		try:
			os.remove(lib)
		except:
			pass
		downloader.download(url, lib, dp)
		addonfolder = xbmc.translatePath(os.path.join('special://','home'))
		time.sleep(3)
		dp.update(0,"", "*Extracting ZiP Please Wait*")
		print '=== EXCTRACTING Roll-Up ==='
		extract.all(lib,addonfolder,dp)
		dialog.ok("XvBMC-NL ServicePack-rollup finished", 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-ons do NOT work you probably should reboot first)')
		xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/purge.py)')
		xbmc.executebuiltin("UpdateLocalAddons")
		xbmc.executebuiltin("UpdateAddonRepos")


def forceRefresh():
#	http://kodi.wiki/view/List_of_built-in_functions
	xbmc.executebuiltin('UpdateLocalAddons')
	dialog.ok("XvBMC Nederland", "Force Refresh Repos and Update LocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
#	xbmc.executebuiltin("ReloadSkin()")


def xvbmcOverclock(url):
#	OCmenu  XvBMC Nederland
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.xvbmc.oc')))
    if pluginpath: xbmc.executebuiltin("XBMC.RunAddon(script.xvbmc.oc)")
    else:
		url=base+'script.xvbmc.oc/script.xvbmc.oc-3.03.zip'
		path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
		dp = xbmcgui.DialogProgress()
		dp.create("XvBMC Nederland","Updater: doing some VOODOO...",'', 'Please Wait')
		lib=os.path.join(path, 'script.xvbmc.oc-3.03.zip')
		try:
			os.remove(lib)
		except:
			pass
		downloader.download(url, lib, dp)
		addonfolder = xbmc.translatePath(os.path.join('special://home','addons',''))
		time.sleep(3)
		dp.update(0,"", "Extracting ZiP Please Wait...")
		print '=== EXCTRACTING Kodi.OC ==='
		extract.all(lib,addonfolder,dp)
	#	dialog.ok("Install Complete", 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-on does NOT work you probably should reboot first)')
		xbmc.executebuiltin("UpdateLocalAddons")
	#	xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.xvbmc.oc/xvbmc-oc.py)')
		xbmc.executebuiltin("RunAddon(script.xvbmc.oc)")


def subDEVmenu(url):
#	DEVmenu XvBMC Nederland
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.xvbmc.dev')))
    if pluginpath: xbmc.executebuiltin("XBMC.RunAddon(script.xvbmc.dev)")
    else:
		url=base+'script.xvbmc.dev/script.xvbmc.dev-3.03.zip'
		path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
		dp = xbmcgui.DialogProgress()
		dp.create("XvBMC Nederland","Updater: doing some VOODOO...",'', 'Please Wait')
		lib=os.path.join(path, 'script.xvbmc.dev-3.03.zip')
		try:
			os.remove(lib)
		except:
			pass
		downloader.download(url, lib, dp)
		addonfolder = xbmc.translatePath(os.path.join('special://home','addons',''))
		time.sleep(3)
		dp.update(0,"", "Extracting ZiP Please Wait...")
		print '=== EXCTRACTING Kodi.DEV ==='
		extract.all(lib,addonfolder,dp)
	#	dialog.ok("Install Complete", 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-on does NOT work you probably should reboot first)')
		xbmc.executebuiltin("UpdateLocalAddons")
	#	xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.xvbmc.dev/xvbmc-dev.py)')
		xbmc.executebuiltin("RunAddon(script.xvbmc.dev)")


def xvbmcTweak():
#	EPiC XvBMC user preferences and tweaking
	dialog.ok("XvBMC NL Tweaks", "EPiC XvBMC Tweaking bitches...", "Coming soon to a theater near you ;-P")


def xvbmcMaintenance(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.schoonmaak')))
    if pluginpath: xbmc.executebuiltin("RunAddon(script.schoonmaak)")
    else:
		url=base+'script.schoonmaak/script.schoonmaak-1.10.08.zip'
		path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
		dp = xbmcgui.DialogProgress()
		dp.create("XvBMC Nederland","Updater: doing some VOODOO...",'', 'Please Wait')
		lib=os.path.join(path, 'script.schoonmaak-1.10.08.zip')
		try:
			os.remove(lib)
		except:
			pass
		downloader.download(url, lib, dp)
		addonfolder = xbmc.translatePath(os.path.join('special://home','addons',''))
		time.sleep(3)
		dp.update(0,"", "Extracting ZiP Please Wait...")
		print '=== EXCTRACTING Kodi.Schoonmaak ==='
		extract.all(lib,addonfolder,dp)
	#	dialog.ok("Install Complete", 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-on does NOT work you probably should reboot first)')
		xbmc.executebuiltin("UpdateLocalAddons")
	#   xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/default.py)')
		xbmc.executebuiltin("RunAddon(script.schoonmaak)")


def closeandexit():
#	http://kodi.wiki/view/Keyboard.xml
	xbmc.executebuiltin('Action(back)')


#######################################################################
#						START MAIN
#######################################################################              

params=get_params()
url=None
name=None
mode=None
fanart=None

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

if mode==None or url==None or len(url)<1:
	mainMenu()

elif mode==1:
	ServicePack(url)

elif mode==2:
	UpdateRollup(url)

elif mode==3:
	forceRefresh()

elif mode==4:
	xvbmcOverclock(url)

elif mode==5:
    subDEVmenu(url)

elif mode==6:
    xvbmcTweak()

elif mode==7:
	xvbmcMaintenance(url)

elif mode==8:
	closeandexit()


xbmcplugin.endOfDirectory(int(sys.argv[1]))

