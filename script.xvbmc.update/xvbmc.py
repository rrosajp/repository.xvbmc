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
addonPath      = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'script.xvbmc.update')
mediaPath      = os.path.join(addonPath, 'media')
xvbmcfanart    = os.path.join(addonPath, 'fanart.jpg')
dialog         = xbmcgui.Dialog()
base           = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'
locate         = 'aHR0cHM6Ly9lcGljYXBvYy5zdGFja3N0b3JhZ2UuY29tL2luZGV4LnBocC8='
bestand        = '20160828232103'
waarschuwing   = '[COLOR=red][B]!!!  WARNING  !!![/B][/COLOR]'
readme         = 'if you\'re seeing this message read this first[B]:[/B]'
noservicepack  = 'Sorry the [B]S[/B]ervice[B]P[/B]ack update is [COLOR=red]outdated[/COLOR] at this moment'
notforked      = '[COLOR dimgray](the newest XvBMC\'s [B]Pi[/B]-image is not forked, [B]yet[/B]...)[/COLOR]'
upgrade40      = 'XvBMC upgrade v4 beta'
upgrade40dl    = 'Download XvBMC v4 beta upgrade -4-'
upgrade31      = 'XvBMC v3.1 *[B]final[/B]* Jarvis'
upgrade31dl    = 'Download XvBMC\'s [COLOR=lime](Pi) v3.1 *final* 26-08-\'16[/COLOR]'
resetos        = 'XvBMC Reset Kodi'
resetosdl      = 'import XvBMC\'s [COLOR=lime]Kodi defaults[/COLOR]'
resetinfo      = '[COLOR dimgray]S[COLOR dimgray]tandalone \'default\' [COLOR white]+[/COLOR] [/COLOR]R[COLOR dimgray]aspberry[/COLOR] Pi \'Jarvis\' 16.1[/COLOR]'
comingsoon     = '[B]Coming soon:[/B] onze nieuwste [COLOR=lime]v4 *beta*[/COLOR]'
uitgeschakeld  = '[COLOR=red]Disabled: [/COLOR]'
herstart       = 'PRESS OK TO FORCECLOSE AND REBOOT!'
forceersluiten = '[COLOR dimgray]indien forceclose niet werkt, herstart uw systeem handmatig, [/COLOR]if forceclose does not work shutdown manually'
#                  ProgTitle="XvBMC Update+Development"               #


#######################################################################
#						Define Menus
#######################################################################

def mainMenu():
	xbmc.executebuiltin("Container.SetViewMode(51)")
	addItem('[COLOR red]XvBMC [B]U[/B]pgrade v[B]4[/B].0 beta[/COLOR] [COLOR dimgray]([/COLOR]R[COLOR dimgray]aspberry[/COLOR] Pi [COLOR white]+[/COLOR] S[COLOR dimgray]tandalone)[/COLOR]', 'url', 1,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[COLOR lime]XvBMC v3.1 *final* Jarvis[/COLOR] [COLOR dimgray]([/COLOR]R[COLOR dimgray]aspberry[/COLOR] Pi [COLOR white]+[/COLOR] S[COLOR dimgray]tandalone)[/COLOR]', 'url', 2,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]R[/B]eset Kodi ' +'[COLOR dimgray]([/COLOR]' +resetinfo +'[COLOR dimgray])[/COLOR]', 'url', 3,os.path.join(mediaPath, "dev.png"))
	addItem('[COLOR dimgray]XvBMC [B]S[/B]ervice[B]P[/B]ack (v3.1)[/COLOR]', 'url', 4,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[COLOR dimgray]XvBMC [B]S[/B]ervice[B]P[/B]ack bulk pack (v3.1)[/COLOR]','url', 5,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]R[/B]efresh [B]A[/B]ddons[COLOR white]+[/COLOR][B]R[/B]epos', 'url', 6,os.path.join(mediaPath, "dev.png"))
	addItem('XvBMC [B]O[/B]ver[B]C[/B]lock (Raspberry [COLOR white]Pi[/COLOR] **[B]only[/B]**)', 'url', 7,os.path.join(mediaPath, "dev.png"))	
	addItem('XvBMC [B]#DEV#[/B] Corner (Firmware-OS-etc)', 'url', 8,os.path.join(mediaPath, "dev.png"))
	addItem('[COLOR white]X[/COLOR]vBMC About (over & [COLOR dodgerblue][B]i[/B][/COLOR]nfo)', 'url', 9,os.path.join(mediaPath, "xvbmc.png"))
	addItem('XvBMC [B]S[/B]choonmaak/[B]M[/B]aintenance (v[COLOR white][B]3[/B][/COLOR])', 'url', 10,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[COLOR dimgray]XvBMC [B]T[/B]weaking[/COLOR]', 'url', 11,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[COLOR white][B]Back[/B][/COLOR]', 'url', 12,os.path.join(mediaPath, "dev.png"))


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

def XvbmcPiUpgrade(url):
    if dialog.yesno(upgrade40 +' [B]- Pi[/B] image', upgrade40dl +' [B]Raspberry [COLOR=white]Pi[/COLOR][/B]?',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(locate)+'s/***************/download' #MdZoWzbgwXQfwIB=XvBMC31final // #GRc7wabLgVRdMDF =LibreELEC702
        path = xbmc.translatePath(os.path.join('/storage/.restore/',''))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, bestand+'.tar')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        time.sleep(2)
        dialog.ok('XvBMC Nederland [B]- Pi[/B]', upgrade40 +' done.', herstart,  forceersluiten)
        killKodi()

def XvbmcUpgrade(url):
    if dialog.yesno(upgrade40 +' - Portable build', upgrade40dl +' [COLOR=white]Portable[/COLOR]?','','(...enig [B]geduld[/B] is vereist, please be patient...)',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(locate)+'s/***************/download' #KhEZaBn8fLbDo5Q =xvbmcresettest
        path = xbmc.translatePath(os.path.join('special://home/','temp'))
        addonpath = xbmc.translatePath(os.path.join('special://home/','addons'))
        userpath = xbmc.translatePath(os.path.join('special://home/','userdata'))
        mediapath = xbmc.translatePath(os.path.join('special://home/','media'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, bestand+'.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland (dutch)","XvBMC-NL: doing some crazy ass VOODOO...",'', '[COLOR dimgray](format C:[B] ;-p [/B]*please wait*)[/COLOR]')
            removefolder(addonpath, 'script.xvbmc.update')
            removefolder(userpath, 'script.xvbmc.update')
            removefolder(mediapath, 'script.xvbmc.update')
            dp.update(0,"", "now really going medieval on your ass")
            addonfolder = xbmc.translatePath(os.path.join('special://','home'))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - UGRADER","XvBMC-NL: doing some upgrading VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            for root, dirs, files in os.walk(xbmc.translatePath('special://thumbnails')):
                file_count = 0
                file_count += len(files)
                if file_count > 0:                
                    for f in files:
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
            dialog.ok('XvBMC Nederland - Portable', upgrade40 +' done.', herstart,  forceersluiten)
            killKodi()


def XvbmcPi31(url):
    if dialog.yesno(upgrade31 +' [B]- Pi[/B] image', upgrade31dl +' [COLOR=white]image[/COLOR]?',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(locate)+'s/MdZoWzbgwXQfwIB/download' #MdZoWzbgwXQfwIB=XvBMC31final // #GRc7wabLgVRdMDF =LibreELEC702
        path = xbmc.translatePath(os.path.join('/storage/.restore/',''))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, bestand+'.tar')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        time.sleep(2)
        dialog.ok('XvBMC Nederland [B]- Pi[/B]', upgrade31 +' done.', herstart,  forceersluiten)
        killKodi()

def XvbmcStandalone31(url):
    if dialog.yesno(upgrade31 +' - Portable', upgrade31dl +' [COLOR=white]build[/COLOR]?','','(...enig [B]geduld[/B] is vereist, please be patient...)',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(locate)+'s/***************/download' #KhEZaBn8fLbDo5Q =xvbmcresettest
        path = xbmc.translatePath(os.path.join('special://home/','temp'))
        addonpath = xbmc.translatePath(os.path.join('special://home/','addons'))
        userpath = xbmc.translatePath(os.path.join('special://home/','userdata'))
        mediapath = xbmc.translatePath(os.path.join('special://home/','media'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, bestand+'.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland (dutch)","XvBMC-NL: doing some crazy ass VOODOO...",'', '[COLOR dimgray](format C:[B] ;-p [/B]*please wait*)[/COLOR]')
            removefolder(addonpath, 'script.xvbmc.update')
            removefolder(userpath, 'script.xvbmc.update')
            removefolder(mediapath, 'script.xvbmc.update')
            dp.update(0,"", "now really going medieval on your ass")
            addonfolder = xbmc.translatePath(os.path.join('special://','home'))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - UGRADER","XvBMC-NL: doing some upgrading VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            for root, dirs, files in os.walk(xbmc.translatePath('special://thumbnails')):
                file_count = 0
                file_count += len(files)
                if file_count > 0:                
                    for f in files:
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
            dialog.ok('XvBMC Nederland - Portable', upgrade31 +' done.', herstart,  forceersluiten)
            killKodi()


def XvbmcPiReset(url):
    if dialog.yesno(resetos +' [B]- Pi[/B] image', resetosdl +'; reset to Jarvis v[B]16.1[/B]?','','(...enig [B]geduld[/B] is vereist, please be patient...)',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(locate)+'s/GRc7wabLgVRdMDF/download' #MdZoWzbgwXQfwIB=XvBMC31final // #GRc7wabLgVRdMDF =LibreELEC702
        path = xbmc.translatePath(os.path.join('/storage/.restore/',''))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, bestand+'.tar')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        time.sleep(2)
        dialog.ok('XvBMC Nederland [B]- Pi[/B]', resetos +' done.', herstart,  forceersluiten)
        killKodi()

def XvbmcPcReset(url):
    if dialog.yesno(resetos +' - Portable', resetosdl +'; reset to default?','','(...enig [B]geduld[/B] is vereist, please be patient...)',nolabel='Nee, No',yeslabel='Ja, Yes'):
        url=base64.b64decode(locate)+'s/KhEZaBn8fLbDo5Q/download' #KhEZaBn8fLbDo5Q =xvbmcresettest
        path = xbmc.translatePath(os.path.join('special://home/','temp'))
        addonpath = xbmc.translatePath(os.path.join('special://home/','addons'))
        userpath = xbmc.translatePath(os.path.join('special://home/','userdata'))
        mediapath = xbmc.translatePath(os.path.join('special://home/','media'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, bestand+'.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland (dutch)","XvBMC-NL: doing some crazy ass VOODOO...",'', '[COLOR dimgray](format C:[B] ;-p [/B]*please wait*)[/COLOR]')
            removefolder(addonpath, 'script.xvbmc.update')
            removefolder(userpath, 'script.xvbmc.update')
            removefolder(mediapath, 'script.xvbmc.update')
            dp.update(0,"", "now really going medieval on your ass")
            addonfolder = xbmc.translatePath(os.path.join('special://','home'))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - UGRADER","XvBMC-NL: doing some upgrading VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            for root, dirs, files in os.walk(xbmc.translatePath('special://thumbnails')):
                file_count = 0
                file_count += len(files)
                if file_count > 0:                
                    for f in files:
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
            dialog.ok('XvBMC Nederland - Portable', resetos +' done.', herstart,  forceersluiten)
            killKodi()


def ServicePack(url):
    verifyplatform()
#	\update\sp\03-servicepack.zip
    if dialog.yesno('XvBMC NL most recent ServicePack','Download de laatste XvBMC [COLOR=white][B]S[/B]ervice[B]P[/B]ack[/COLOR]?',nolabel='Nee, No',yeslabel='Ja, Yes'):
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
            dp.create("XvBMC Nederland - Updater","XvBMC-NL: doing some updating VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            dialog.ok('XvBMC-NL ServicePack - Update finished', 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-ons do NOT work you probably should reboot first)')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/purge.py)')

def UpdateRollup(url):
    verifyplatform()
#	\update\sp\03-sp-rollup.zip
    if dialog.yesno('XvBMC NL ServicePack Update Rollup','Download ALLE XvBMC [COLOR=white][B]SP[/B][/COLOR]-updates [COLOR=white]([B]all-in-1[/B])[/COLOR]?',nolabel='Nee, No',yeslabel='Ja, Yes'):
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
            dp.create("XvBMC Nederland - Updater","XvBMC-NL: doing some updating VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            dialog.ok('XvBMC-NL ServicePack - RollUp finished', 'een REBOOT van uw systeem is SOMS wenselijk...','', '(if add-ons do NOT work you probably should reboot first)')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/purge.py)')


def forceRefresh():
#	http://kodi.wiki/view/List_of_built-in_functions
	xbmc.executebuiltin('UpdateLocalAddons')
	dialog.ok('XvBMC Nederland', 'Force Refresh Repos and Update LocalAddons')
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
            dp.create("XvBMC Nederland - Updater","XvBMC-#OC: doing some VOODOO...",'', 'Please Wait')
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
            dp.create("XvBMC Nederland - Updater","XvBMC-#DEV: doing some VOODOO...",'', 'Please Wait')
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
	dialog.ok('XvBMC NL Tweaks', 'EPiC XvBMC Tweaking bitches...', 'Coming soon to a theater near you [B];-p[/B]')


def xvbmcMaintenance(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.schoonmaak')))
    if pluginpath: xbmc.executebuiltin("RunAddon(script.schoonmaak)")
    else:
        url=base64.b64decode(base)+'script.schoonmaak/script.schoonmaak-1.10.12.zip'
        path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, 'script.schoonmaak-1.10.12.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            addonfolder = xbmc.translatePath(os.path.join('special://','home','addons',''))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - Updater","XvBMC-#Maintenance: doing some of our VOODOO...",'', 'Please Wait')
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
        dialog.ok(waarschuwing, readme, '[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO guarantees for OSX [B];-p[/B]')
    elif myplatform == 'linux': #Linux
        #dialog.ok('XvBMC NL most recent ServicePack', 'Download de laatste XvBMC (Open-/LibreELEC) ServicePack?','','') # N.V.T. als er een actuele SP is dan willen we die natuurlijk ook lol ;-p #
        print '=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ==='	
    elif myplatform == 'android': # Android # inclusief bonus melding Android-Updater #
        dialog.ok('[COLOR=red][B]!!!  IMPORTANT  !!![/COLOR][/B]', '[COLOR=lime]There\'s also a specific XvBMC\'s Android add-on update(r)[/COLOR]', '...enkel voor specifieke bonus Android add-on updates...', noservicepack +' ' +notforked) # , 'NOTE: ' +noservicepack +notforked +'(let op)'
    elif myplatform == 'windows': # Windows
        #dialog.ok(waarschuwing,  readme, noservicepack, notforked)  # N.V.T. als er een actuele SP is dan willen we die natuurlijk ook lol ;-p #
        print '=== Download de laatste XvBMC (Windows) ServicePack ==='		
    else: #ATV
        dialog.ok(waarschuwing, readme, '[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO guarantees for ATV [B];-p[/B]')    

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


def removefolder(map, exclude=None):
    for root, dirs, files in os.walk(map, topdown=False):
        for name in files:
            if(root.find(exclude) > 0):
                continue
            try: os.remove(os.path.join(root, name))
            except: pass
        for name in dirs:
            if(name == exclude):
                continue
            try: os.rmdir(os.path.join(root, name))
            except: pass

def killKodi():
    choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok(waarschuwing, 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: xbmc.executebuiltin("Reboot")
        except: pass
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok(waarschuwing, 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok(waarschuwing, 'Your system has been detected as Android, you ', '[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Either close using Task Manager (If unsure pull the plug).')
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok(waarschuwing, 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Use task manager and NOT ALT F4')
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok(waarschuwing, 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.','Your platform could not be detected so just pull the power cable.')


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
#	Upgrade(v40)
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'linux': # Open-/LibreELEC
        dialog.ok(upgrade40 +' [B]- Pi[/B]', uitgeschakeld +upgrade40 +' \'Raspberry Pi\'','', comingsoon +' image [COLOR dimgray] [B]([/B]Pi 2+3[B])[/B][/COLOR]') # DiSABLE indien v4.0 *online* #
        #XvbmcPiUpgrade(url) # BLOCKED-4-NOW (v4.0) # 
    else: #rest
        print "none linux os"
        dialog.ok(upgrade40 +' - Portable', uitgeschakeld +upgrade40 +' \'Standalone\'','', comingsoon +' build [COLOR dimgray] [B]([/B]Pi fork[B])[/B][/COLOR]') # DiSABLE indien v4.0 *online* #
        #XvbmcUpgrade(url) # BLOCKED-4-NOW (v4.0) # 

elif mode==2:
#	Upgrade(v31)
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'linux': # Open-/LibreELEC
        dialog.ok(upgrade31 +' [B]- Pi[/B]', '[COLOR red]INSTALL: [/COLOR]' +upgrade31 +' \'Raspberry Pi\'?','', comingsoon +' image [COLOR dimgray] [B]([/B]Pi 2+3[B])[/B][/COLOR]') # AANPASSEN in Tip! indien v4.0 *online* #
        XvbmcPi31(url)
    else: #rest
        print "none linux os"
        dialog.ok(upgrade31 +' - Portable', uitgeschakeld +upgrade31 +' \'Standalone\'','', comingsoon +' build [COLOR dimgray] [B]([/B]Pi fork[B])[/B][/COLOR]') # AANPASSEN in Tip! indien v4.0 *online* #
        #XvbmcStandalone31(url) # ENABLE indien v3.1 *online* #

elif mode==3:
#	Upgrade(null)
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'linux': # Open-/LibreELEC
        dialog.ok(resetos +' [B]- Pi[/B]', '[COLOR red]WARNING: [/COLOR]' +resetos +' \'Raspberry Pi\' -2- [B]Jarvis[/B]','', '[COLOR dimgray][B]NOTE: [/B][/COLOR]' +resetinfo +'!')
        XvbmcPiReset(url)
    else: #rest
        print "none linux os"
        dialog.ok(resetos +' - Portable', '[COLOR red]WARNING: [/COLOR]' +resetos +' \'Standalone\' -2- default','', '[COLOR dimgray][B]NOTE: [/B][/COLOR]' +resetinfo +'!')
        XvbmcPcReset(url)

elif mode==4:
#	ServicePack(url)
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'linux': # Open-/LibreELEC
        dialog.ok('XvBMC NL most recent ServicePack', uitgeschakeld +' download laatste XvBMC [COLOR=white]ServicePack[/COLOR]','', upgrade31dl +' image') # DiSABLE indien SP *online* #
        #ServicePack(url) # BLOCKED-4-NOW (v4.0) # 
    else: #rest
        print "none linux os"
        dialog.ok(waarschuwing,  readme, noservicepack, notforked) # DiSABLE indien SP *online* #
        #ServicePack(url) # BLOCKED-4-NOW (v4.0) # 

elif mode==5:
#	UpdateRollup(url)
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'linux': # Open-/LibreELEC
        dialog.ok('XvBMC NL ServicePack Update Rollup', uitgeschakeld +' download alle XvBMC SP-updates [COLOR=white](all-in-1)[/COLOR]','', upgrade31dl +' image') # DiSABLE indien SP *online* #
        #ServicePack(url) # BLOCKED-4-NOW (v4.0) # 
    else: #rest
        print "none linux os"
        dialog.ok(waarschuwing,  readme, noservicepack, notforked) # DiSABLE indien SP *online* #
        #UpdateRollup(url) # BLOCKED-4-NOW (v4.0) # 

elif mode==6:
	forceRefresh()

elif mode==7:
	xvbmcOverclock(url)

elif mode==8:
    subDEVmenu(url)

elif mode==9:	
	AboutXvBMC()

elif mode==10:
	xvbmcMaintenance(url)

elif mode==11:
    xvbmcTweak()

elif mode==12:
	closeandexit()


xbmcplugin.endOfDirectory(int(sys.argv[1]))

