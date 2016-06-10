#   script.Schoonmaak (Kodi Schoonmaak XvBMC / Raw Maintenance No-Issue)
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


import urllib,urllib2,re,uuid, time
import xbmcgui,xbmcplugin
import os,xbmc,shutil
import sqlite3


#                  ProgTitle="XvBMC Raw Maintenance"                  #
thumbnailPath = xbmc.translatePath('special://thumbnails');
cachePath = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath = xbmc.translatePath('special://temp')
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'script.schoonmaak')
mediaPath = os.path.join(addonPath, 'media')
databasePath = xbmc.translatePath('special://database')
dialog = xbmcgui.Dialog()
#                  ProgTitle="XvBMC Raw Maintenance"                  #


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
	xbmc.executebuiltin("Container.SetViewMode(500)")
	addItem('[B][COLOR lime]XvBMC-NL[/COLOR][/B] Build Purge', 'url', 1,os.path.join(mediaPath, "packages.png"))
	addItem('[B]C[/B]lear Cache','url', 2,os.path.join(mediaPath, "cache.png"))
	addItem('[B]D[/B]elete Thumbnails', 'url', 3,os.path.join(mediaPath, "thumbs.png"))
	addItem('[B]P[/B]urge Packages', 'url', 4,os.path.join(mediaPath, "packages.png"))
	addItem('[B]R[/B]emove addons.db', 'url', 5,os.path.join(mediaPath, "thumbs.png"))
	addItem('[COLOR red]Refresh[/COLOR] [B]A[/B]ddons+[B]R[/B]epos', 'url', 6,os.path.join(mediaPath, "kmbroom.png"))
	addItem('Kodi [B]Versie[/B]', 'url', 7,os.path.join(mediaPath, "kmbroom.png"))	


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
def setupCacheEntries():
    entries = 7 #make sure this refelcts the amount of entries you have
    dialogName = ["MP3 Streams", "Quasar", "SportsDevil", "SportsDevilNL", "Simple Downloader", "Spotitube", "Kmediatorrent"]
    pathName = ["special://profile/addon_data/plugin.audio.mp3streams/temp_dl",
				"special://profile/addon_data/plugin.video.quasar/cache",
				"special://profile/addon_data/plugin.video.SportsDevil/cache",
				"special://profile/addon_data/plugin.video.SportsDevilNL/cache",
				"special://profile/addon_data/script.module.simple.downloader",
				"special://profile/addon_data/plugin.video.spotitube/cache",
				"special://profile/addon_data/plugin.video.kmediatorrent/cache"]
                    
    cacheEntries = []
    
    for x in range(entries):
        cacheEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return cacheEntries

def setupXvbmcEntries():
    entries = 4 #make sure this refelcts the amount of entries you have
    dialogName = ["NLview", "SportsDevil", "NLviewRepo", "TVaddons.nl"]
    pathName = ["special://home/addons/plugin.video.NLVIEW",
				"special://home/addons/plugin.video.SportsDevil",
				"special://home/addons/repository.NLVIEW",
				"special://home/addons/repository.tvaddons.nl"]
                    
    XvbmcEntries = []
    
    for x in range(entries):
        XvbmcEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return XvbmcEntries


def clearCache():
    
    if os.path.exists(cachePath)==True:    
        for root, dirs, files in os.walk(cachePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:

                
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

                    
                   #if dialog.yesno("Raw Manager",str(file_count) + "%s cache files found"%(entry.name), "Do you want to delete them?"):
                    if dialog.yesno("XvBMC Raw Manager","%s cache files found"%(entry.name), "Do you want to delete them?"):
                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            shutil.rmtree(os.path.join(root, d))
                            
                else:
                    pass
                

    
    dialog.ok("XvBMC Raw Maintenance", "Done Clearing Cache files")
    
    
def deleteThumbnails():
    
    if os.path.exists(thumbnailPath)==True:  
            
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
    except:
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

    dialog.ok("XvBMC Raw Maintenance", "Please reboot your system to rebuild thumbnail folder...")


def forceRefresh():
	xbmc.executebuiltin('UpdateLocalAddons')
	dialog.ok("XvBMC Raw Maintenance", "Force Refresh Repos and Update LocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
#   xbmc.executebuiltin("ReloadSkin()")


def purgePackages():
    
    purgePath = xbmc.translatePath('special://home/addons/packages')
    
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
                
                dialog.ok("XvBMC Raw Maintenance", "Deleting Packages all done")
            else:
                dialog.ok("XvBMC Raw Maintenance", "No Packages to Purge")


def purgeOld():
#   import os,xbmc,shutil
#   bruteforce removal  #
#   xvbmc = os.listdir(xbmc.translatePath(os.path.join('special://home/addons/')))
#   addonfolder = xbmc.translatePath(os.path.join('special://home/addons/'))
#   for item in xvbmc:
#       if ('repository.tvaddons.nl') in item:
#           print str(xvbmc)+str(item)
#           try:
#               shutil.rmtree(addonfolder+item, ignore_errors=True)
#           except:
#               pass
#       else:
#           pass

    XvbmcEntries = setupXvbmcEntries()

    for entry in XvbmcEntries:
        xvbmcaddons = xbmc.translatePath(entry.path)
        if os.path.exists(xvbmcaddons)==True:    
            for root, dirs, files in os.walk(xvbmcaddons):
                file_count = 0
                file_count += len(files)
                if file_count > 0:

                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            shutil.rmtree(os.path.join(root, d), ignore_errors=True)
                try:
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.NLVIEW')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.SportsDevil')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','repository.NLVIEW')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','repository.tvaddons.nl')), ignore_errors=True)

                    dialog.ok("XvBMC-NL Purge", "Crap Purge all done...")
                except:
                #   dialog.ok("XvBMC-NL Purge", "Done Purging all your CRAP...")					
                    pass
	else:
		dialog.ok("XvBMC-NL Purge", "PLEASE MOVE ALONG....NOTHING TO SEE HERE")
		pass

	return


def KODIVERSION(url): xbmc_version=xbmc.getInfoLabel("System.BuildVersion"); version=xbmc_version[:4]; print version; dialog.ok("XvBMC Raw Maintenance", "Your Kodi Version : [COLOR lime][B]%s[/B][/COLOR]" % version)


def AddonsDatabaseRemoval():
    dbList = os.listdir(databasePath)
    dbAddons = []
    removed = True
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
        dialog.ok("XvBMC Raw Maintenance", "Please reboot your system to rebuild addons database...")
    else:
        dialog.ok("XvBMC Raw Maintenance", "Removal failed!", "try manual remove, see http://kodi.wiki/view/Database_version")
	

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
		purgeOld()

elif mode==2:
		clearCache()

elif mode==3:
        deleteThumbnails()

elif mode==4:
		purgePackages()

elif mode==5:
    AddonsDatabaseRemoval()

elif mode==6:
    forceRefresh()

elif mode==7:
		KODIVERSION(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))

