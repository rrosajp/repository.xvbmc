#!/usr/bin/python
 
"""
	IF you copy/paste 'script.schoonmaak' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""

#   script.Schoonmaak (EPiC Kodi Schoonmaak XvBMC Nederland)
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
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
import os,shutil,time
import downloader, extract
import sqlite3
import common as Common

# import xbmcaddon
# Set the addon environment                  #
# addon = xbmcaddon.Addon('script.schoonmaak')


#               ProgTitle ="XvBMC-NL-Maintenance"                     #
thumbnailPath = xbmc.translatePath('special://thumbnails');
cachePath     = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath      = xbmc.translatePath('special://temp')
addonPath     = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'script.schoonmaak')
mediaPath     = os.path.join(addonPath, 'media')
xvbmcfanart   = os.path.join(addonPath, 'fanart.jpg')
databasePath  = xbmc.translatePath('special://database')
dialog        = xbmcgui.Dialog()
base          = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'
MainTitle     = "XvBMC-NL-Maintenance"
Windows       = xbmc.translatePath('special://home')
WindowsCache  = xbmc.translatePath('special://home')
OtherCache    = xbmc.translatePath('special://home/temp')
#               ProgTitle ="XvBMC-NL-Maintenance"                     #


#######################################################################
#                          CLASSES
#######################################################################

class cacheEntry:
    def __init__(self, namei, pathi):
        self.name = namei
        self.path = pathi


#######################################################################
#						Define Menus
#######################################################################

def mainMenu():
	xbmc.executebuiltin("Container.SetViewMode(51)")
	addItem('[B]A[/B]uto Clean (cache, crashlogs, packages & thumbnails)','url', 1,os.path.join(mediaPath, "cache.png"))
	addItem('[B]C[/B]lear Cache','url', 2,os.path.join(mediaPath, "cache.png"))
	addItem('[B]D[/B]elete Thumbnails', 'url', 3,os.path.join(mediaPath, "thumbs.png"))
	addItem('[B]F[/B]lush Add-ons (Salts HD/RD lite, Exodus, etc.)', 'url', 4,os.path.join(mediaPath, "packages.png"))
	addItem('[B]P[/B]urge Packages', 'url', 5,os.path.join(mediaPath, "packages.png"))
	addItem('[B]R[/B]aspberry [COLOR white]Pi[/COLOR] Extreme [B]C[/B]rap[B]C[/B]leaner [COLOR dimgray](it\'s not a fresh restart)[/COLOR]', 'url', 6,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[B]R[/B]efresh [B]A[/B]ddons[COLOR white]+[/COLOR][B]R[/B]epos', 'url', 7,os.path.join(mediaPath, "kmbroom.png"))
	addItem('[B]R[/B]emove addons.db', 'url', 8,os.path.join(mediaPath, "thumbs.png"))
	addItem('[B][COLOR lime]X[/COLOR][/B]vBMC About (over & [COLOR dodgerblue][B]i[/B][/COLOR]nfo)', 'url', 9,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[B][COLOR lime]X[/COLOR][/B]vBMC Build [COLOR red]Purge[/COLOR] (image crap cleaner)', 'url', 10,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[B][COLOR lime]X[/COLOR][/B]vBMC UPDATER(r) [B]&[/B] Development [COLOR darkgreen][I](kodi dev.tools)[/I][/COLOR]', 'url', 11,os.path.join(mediaPath, "xvbmc.png"))
	addItem('[B]K[/B]ill kodi  (force close)', 'url', 12,os.path.join(mediaPath, "kmbroom.png"))
	addItem('[B]K[/B]odi versie (WhoAm[B]i[/B])', 'url', 13,os.path.join(mediaPath, "kmbroom.png"))
	addItem('[COLOR white][B]Back[/B][/COLOR]', 'url', 14,os.path.join(mediaPath, "kmbroom.png"))


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

def setupCacheEntries():
    entries = 8 #make sure this reflects the amount of entries you have
    dialogName = ["MP3 Streams", "Quasar", "SportsDevil", "SportsDevilNL", "Simple Downloader", "Spotitube", "Kmediatorrent", "SkinHelperService"]
    pathName = ["special://profile/addon_data/plugin.audio.mp3streams/temp_dl",
				"special://profile/addon_data/plugin.video.quasar/cache",
				"special://profile/addon_data/plugin.video.SportsDevil/cache",
				"special://profile/addon_data/plugin.video.SportsDevilNL/cache",
				"special://profile/addon_data/script.module.simple.downloader",
				"special://profile/addon_data/plugin.video.spotitube/cache",
				"special://profile/addon_data/plugin.video.kmediatorrent/cache",
				"special://profile/addon_data/script.skin.helper.service/musicartcache"]
                    
    cacheEntries = []
    
    for x in range(entries):
        cacheEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return cacheEntries


#######################################################################
#						CACHE
#######################################################################

def clearCache():
    if os.path.exists(cachePath)==True:    
        for root, dirs, files in os.walk(cachePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:

                #  dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if os.path.exists(tempPath)==True:    
        for root, dirs, files in os.walk(tempPath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                #  dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Temp Files", str(file_count) + " files found", "Do you want to delete them?"):
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                #  dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                #  dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass    
                
    cacheEntries = setupCacheEntries()
                                         
    for entry in cacheEntries:
        clear_cache_path = xbmc.translatePath(entry.path)
        if os.path.exists(clear_cache_path)==True:    
            for root, dirs, files in os.walk(clear_cache_path):
                file_count = 0
                file_count += len(files)
                if file_count > 0:

                   #   dialog = xbmcgui.Dialog()
                   #if dialog.yesno(MainTitle,str(file_count) + "%s cache files found"%(entry.name), "Do you want to delete them?"):
                    if dialog.yesno(MainTitle,"%s cache files found"%(entry.name), "Do you want to delete them?"):
                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            shutil.rmtree(os.path.join(root, d))
                            
                else:
                    pass
                

    
    dialog.ok(MainTitle, "Done Clearing Cache files")


#######################################################################
#						THUMBS
#######################################################################

def deleteThumbnails():
    if os.path.exists(thumbnailPath)==True:  
            #  dialog = xbmcgui.Dialog()
            if dialog.yesno("Delete Thumbnails", "This option deletes all thumbnails", "Are you sure you want to do this?"):
                for root, dirs, files in os.walk(thumbnailPath):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            try:
                                os.unlink(os.path.join(root, f))
                            except:
                                pass                
    else:
        pass
    
    text13 = os.path.join(databasePath,"Textures13.db")
    try:
        os.unlink(text13)
    except OSError: #DOES THIS WORK WITH KRYPTO?
        try:
            dbcon = sqlite3.connect(text13)
            dbcur = dbcon.cursor()
            dbcur.execute('DROP TABLE IF EXISTS path')
            dbcur.execute('VACUUM')
            dbcon.commit()
            dbcur.execute('DROP TABLE IF EXISTS sizes')
            dbcur.execute('VACUUM')
            dbcon.commit()
            dbcur.execute('DROP TABLE IF EXISTS texture')
            dbcur.execute('VACUUM')
            dbcon.commit()
            dbcur.execute("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))"""
                          )
            dbcon.commit()
            dbcur.execute("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)"""
                          )
            dbcon.commit()
            dbcur.execute("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))"""
                          )
            dbcon.commit()
        except:
            pass

    dialog.ok(MainTitle, "Please reboot your system to rebuild thumbnail folder...")


#######################################################################
#						REFRESHLOACALADDONS&REPOS
#######################################################################

def forceRefresh():
	xbmc.executebuiltin('UpdateLocalAddons')
	dialog.ok(MainTitle, "Force Refresh Repos and Update LocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
	xbmc.executebuiltin("ReloadSkin()")


#######################################################################
#						Pi CrapCleaner Extreme
#######################################################################

def PiCCleaner():
    myplatform = Common.platform()
    print "Platform: " + str(myplatform)
    if not myplatform == 'linux': #Open-/LibreELEC OS *check failed*
        dialog.ok('XvBMC-Pi-Maintenance', '[COLOR=red][B]!!!  NOPE  !!![/B][/COLOR]','[US] you\'re running a \'none linux os\' ie. Open-/LibreELEC','[NL] dit is geen Raspberry Pi met Open-/LibreELEC OS...')
        print "none Linux OS ie. Open-/LibreELEC" # ie. Windows/Mac/Atv
    else: #Open-/LibreELEC OS *check succes*
        print "linux os" # ie. Open-/LibreELEC
        if dialog.yesno('XvBMC-Pi-Maintenance','about to do some extreme CrapCleaner voodoo...','[I]this will take a few seconds to complete, be patient![/I]', '[B]are you sure[COLOR white]?[/COLOR][/B]'):
            bashCommand = "/bin/bash /storage/.kodi/addons/script.schoonmaak/xvbmc-piecc.sh"
	    os.system(bashCommand)
	    dialog.ok(MainTitle, '[B]Pi[/B] CrapCleaner finished!','', 'Press OK to reboot...')
	    xbmc.executebuiltin("Reboot")

	
#######################################################################
#						PACKAGES
#######################################################################

def purgePackages():
    purgePath = xbmc.translatePath('special://home/addons/packages')
    #  dialog = xbmcgui.Dialog()
    for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
    if dialog.yesno("Delete Package Cache Files", "%d packages found."%file_count, "Delete Them?"):  
        for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:            
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
                
                dialog.ok(MainTitle, "Deleting Packages all done")
            else:
                dialog.ok(MainTitle, "No Packages to Purge")

#######################################################################
#						WHOAMI/WHOIS
#######################################################################

def KODIVERSION(url): xbmc_version=xbmc.getInfoLabel("System.BuildVersion"); version=xbmc_version[:4]; print version; dialog.ok(MainTitle, "Your Kodi Version : [COLOR lime][B]%s[/B][/COLOR]" % version)


#######################################################################
#						ADDONS??.dB
#######################################################################

def AddonsDatabaseRemoval():
    dbList = os.listdir(databasePath)
    dbAddons = []
    removed = True

    xbmc_version=xbmc.getInfoLabel("System.BuildVersion")
    version=float(xbmc_version[:4])

    if version >= 17.0 and version <= 17.9:
        codename = 'Krypton'
    else:
        codename = 'Pass'

    if codename == "Pass":
        try:
            for file in dbList:
                if re.findall('Addons(\d+)\.db', file):
                    dbAddons.append(file)
            for file in dbAddons:
                dbFile = os.path.join(databasePath, file)
                fo = open(dbFile, 'ab+')
                try:
                   #os.unlink(dbFile)
                    fo.close()
                    os.remove(fo.name)
                except:
                    removed = False
            if removed:
                dialog.ok(MainTitle, "Please reboot your system to rebuild addons database...")
            else:
                dialog.ok(MainTitle, "Removal failed!", "try manual remove, see: http://kodi.wiki/view/Database_version")
        except:
            pass
    else:
        dialog.ok(MainTitle,'This feature is not available in Kodi 17 Krypton','','[COLOR yellow]Thank you for using XvBMC Maintenance[/COLOR]')


#######################################################################
#						UPDATER
#######################################################################

def xvbmcupdater(url):
#	xbmc.executebuiltin('UpdateLocalAddons')
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','script.xvbmc.update')))
    if pluginpath: xbmc.executebuiltin("RunAddon(script.xvbmc.update)")
    else:
        url=base64.b64decode(base)+'script.xvbmc.update/script.xvbmc.update-4.0.2.zip'
        path = xbmc.translatePath(os.path.join('special://home','addons','packages'))
        if not os.path.exists(path):
            os.makedirs(path)
        lib=os.path.join(path, 'script.xvbmc.update-4.0.2.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib)
        if os.path.exists(lib):
            addonfolder = xbmc.translatePath(os.path.join('special://','home','addons',''))
            time.sleep(2)
            dp = xbmcgui.DialogProgress()
            dp.create("XvBMC Nederland - Maintenance","XvBMC-NL: doing some extracting VOODOO...",'', 'Please Wait')
            dp.update(0,"", "*Extracting ZiP Please Wait*")
            extract.all(lib,addonfolder,dp)
            dp.close()
            try: os.remove(lib)
            except: pass
            print '=== Kodi.#Updater XvBMC Nederland ==='
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("RunAddon(script.xvbmc.update)")


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


#######################################################################
#						Auto.Clean(er)
#######################################################################

def autocleanask():
    
	choice = xbmcgui.Dialog().yesno(MainTitle, 'Select [COLOR green]YES[/COLOR] to delete your:','cache, crashlogs, packages & thumbnails all at once.','[I][COLOR white]Do you wish to continue?[/I][/COLOR]', yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR red]NO[/COLOR][/B]')
	if choice == 1:
		autocleannow()
	
def autocleannow():
    AutoClean = True

    if os.path.exists(cachePath)==True:    
        for root, dirs, files in os.walk(cachePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                    for f in files:
                        try:
							if (f.endswith(".log")): continue
							os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
				
    if os.path.exists(tempPath)==True:    
        for root, dirs, files in os.walk(tempPath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                    for f in files:
                        try:
                            if (f.endswith(".log")): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass    
                
    cacheEntries = setupCacheEntries()
                                         
    for entry in cacheEntries:
        clear_cache_path = xbmc.translatePath(entry.path)
        if os.path.exists(clear_cache_path)==True:    
            for root, dirs, files in os.walk(clear_cache_path):
                file_count = 0
                file_count += len(files)
                if file_count > 0:
                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            shutil.rmtree(os.path.join(root, d))
                            
                else:
                    pass
        
    if os.path.exists(thumbnailPath)==True:  
                for root, dirs, files in os.walk(thumbnailPath):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            try:
                                os.unlink(os.path.join(root, f))
                            except:
								pass
    else:
        pass
    
    text13 = os.path.join(databasePath,"Textures13.db")
    try:
		os.unlink(text13)
    except OSError:
        pass
		
    purgePath = xbmc.translatePath('special://home/addons/packages')
    dialog = xbmcgui.Dialog()
    for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
    for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:            
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))

    if AutoClean==True:
        #dialog.ok(MainTitle, "Auto Remove Crash Log Files...")
        AutoCrash()
    else:
        #dialog.ok(MainTitle, "Skip auto remove crash log files...")
        xbmc.log(str(AutoClean))

    choice = xbmcgui.Dialog().yesno(MainTitle,"[COLOR white][B]A[/B]uto [B]C[/B]lean finished:[/COLOR]","[I]cache, crashlogs, packages & thumbnails are removed.[/I]","Reboot your device now to finish the process?", yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR red]NO[/COLOR][/B]')
    if choice == 1:
         Common.killKodi()

def AutoCrash():  

	HomeDir = xbmc.translatePath('special://home')
	WindowsCache = os.path.join(xbmc.translatePath('special://home'), 'cache')
	OtherCache = xbmc.translatePath('special://temp')
	
	if os.path.exists(HomeDir)==True:   
		path=Windows
		import glob
		for infile in glob.glob(os.path.join(path, '*.dmp')):
			File=infile
			print infile
			os.remove(infile)
				
		for infile in glob.glob(os.path.join(path, '*.txt')):
			File=infile
			print infile
			os.remove(infile)
				
	if os.path.exists(WindowsCache)==True:   
		path=WindowsCache
		import glob
		for infile in glob.glob(os.path.join(path, '*.dmp')):
			File=infile
			print infile
			os.remove(infile)
				
		for infile in glob.glob(os.path.join(path, '*.txt')):
			File=infile
			print infile
			os.remove(infile)

	if os.path.exists(OtherCache)==True:   
		path=OtherCache
		import glob
		for infile in glob.glob(os.path.join(path, '*.dmp')):
			File=infile
			print infile
			os.remove(infile)
				
		for infile in glob.glob(os.path.join(path, '*.txt')):
			File=infile
			print infile
			os.remove(infile)


#######################################################################
#						GOBACK
#######################################################################

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
	autocleanask()

elif mode==2:
	clearCache()

elif mode==3:
	deleteThumbnails()

elif mode==4:
    xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/xvbmc-flush.py)')

elif mode==5:
	purgePackages()

elif mode==6:
	PiCCleaner()

elif mode==7:
    forceRefresh()

elif mode==8:
    AddonsDatabaseRemoval()

elif mode==9:	
	AboutXvBMC()

elif mode==10:
	xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.schoonmaak/purge.py)')

elif mode==11:
    xvbmcupdater(url)

elif mode==12:
	Common.killKodi()

elif mode==13:
	KODIVERSION(url)

elif mode==14:
	closeandexit()


xbmcplugin.endOfDirectory(int(sys.argv[1]))

