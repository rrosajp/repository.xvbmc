#!/usr/bin/python

"""
	IF you copy/paste 'script.xvbmc-flush' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""

import xbmc, xbmcgui
import shutil
import urllib2,urllib
import os
import time


# import xbmcaddon
# Set the addon environment
# addon = xbmcaddon.Addon('script.xvbmc-flush')


# ProgTitle="XvBMC Flush Toilet" #
dialog = xbmcgui.Dialog()
# ProgTitle="XvBMC Flush Toilet" #


def showMenu():
    '''Set up our XvBMC-OC Menu'''
    
    # Create list of menu items
    userchoice = []
    userchoice.append("Salts [B]HD[/B] Lite - flush cache")
    userchoice.append("Salts [B]HD[/B] Lite - reset db")
    userchoice.append("Salts [B]RD[/B] Lite - flush cache")
    userchoice.append("Salts [B]RD[/B] Lite - reset db")
    userchoice.append("Exodus - flush cache")
    userchoice.append("Exodus - flush sources")
    userchoice.append("[COLOR red]Remove[/COLOR] [COLOR lime]ALL[/COLOR] [COLOR red]these DataBases (Pi optimized)[/COLOR] [COLOR dimgray][I][B]\'[/B]alpha phase[B]\'[/B][/I][/COLOR]")
    userchoice.append("[B][COLOR white]Exit[/COLOR][/B]")
    
    # Display the menu
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland Flush Addon cache/database", 
                                           userchoice)
    # Process menu actions
    
    if userchoice[inputchoice] == "Salts [B]HD[/B] Lite - flush cache":
        HDflush()
    
    elif userchoice[inputchoice] == "Salts [B]HD[/B] Lite - reset db":
        HDreset()
	
    elif userchoice[inputchoice] == "Salts [B]RD[/B] Lite - flush cache":
        RDflush()
    
    elif userchoice[inputchoice] == "Salts [B]RD[/B] Lite - reset db":
        RDreset()
	
    elif userchoice[inputchoice] == "Exodus - flush cache":
        ExodusCache()
    
    elif userchoice[inputchoice] == "Exodus - flush sources":
        ExodusSources()
	
    elif userchoice[inputchoice] == "[COLOR red]Remove[/COLOR] [COLOR lime]ALL[/COLOR] [COLOR red]these DataBases (Pi optimized)[/COLOR] [COLOR dimgray][I][B]\'[/B]alpha phase[B]\'[/B][/I][/COLOR]":
        RemoveAllDB()


class HDflushClass(xbmcgui.Window):
  def __init__(self):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.video.saltshd.lite')))
    if pluginpath: xbmc.executebuiltin("RunPlugin(plugin://plugin.video.saltshd.lite/?mode=flush_cache)")
    else:
		dialog.ok("XvBMC Nederland", 'Salts HD Lite bevindt zich niet op uw systeem','', '(...Salts HD Lite not found...)')

class HDresetClass(xbmcgui.Window):
  def __init__(self):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.video.saltshd.lite')))
    if pluginpath: xbmc.executebuiltin("RunPlugin(plugin://plugin.video.saltshd.lite/?mode=reset_db)")
    else:
		dialog.ok("XvBMC Nederland", 'Salts HD Lite bevindt zich niet op uw systeem','', '(...Salts HD Lite not found...)')

class RDflushClass(xbmcgui.Window):
  def __init__(self):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.video.saltsrd.lite')))
    if pluginpath: xbmc.executebuiltin("RunPlugin(plugin://plugin.video.saltsrd.lite/?mode=flush_cache)")
    else:
		dialog.ok("XvBMC Nederland", 'Salts RD Lite bevindt zich niet op uw systeem','', '(...Salts RD Lite not found...)')

class RDresetClass(xbmcgui.Window):
  def __init__(self):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.video.saltsrd.lite')))
    if pluginpath: xbmc.executebuiltin("RunPlugin(plugin://plugin.video.saltsrd.lite/?mode=reset_db)")
    else:
		dialog.ok("XvBMC Nederland", 'Salts RD Lite bevindt zich niet op uw systeem','', '(...Salts RD Lite not found...)')

class ExodusCacheClass(xbmcgui.Window):
  def __init__(self):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.video.exodus')))
    if pluginpath: xbmc.executebuiltin("RunPlugin(plugin://plugin.video.exodus/?action=clearCache)")
    else:
		dialog.ok("XvBMC Nederland", 'Exodus bevindt zich niet op uw systeem','', '(...Exodus not found...)')

class ExodusSourcesClass(xbmcgui.Window):
  def __init__(self):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.video.exodus')))
    if pluginpath: xbmc.executebuiltin("RunPlugin(plugin://plugin.video.exodus/?action=clearSources)")
    else:
		dialog.ok("XvBMC Nederland", 'Exodus bevindt zich niet op uw systeem','', '(...Exodus not found...)')

class RemoveAllDbClass(xbmcgui.Window):
  def __init__(self):
    dialog.ok("XvBMC Nederland", '[COLOR white][B]*[/B]DataBase CrapCleaner extreme[B]*[/B][/COLOR]','', '(Raspberry Pi optimized, [B]can[/B] work cross-platform)')
    import os,xbmc,shutil
#   bruteforce removal  #
    XvBMC    = os.listdir(xbmc.translatePath(os.path.join('special://home/userdata/Database/')))
    DBfolder = xbmc.translatePath(os.path.join('special://home/userdata/Database/'))
    exodus   = os.listdir(xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.exodus/')))
    EXfolder = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.exodus/'))
    for item in XvBMC:
        if ('saltsrd.lite') in item:
            print str(XvBMC)+str(item)
            #xbmc.log(str(DBfolder+item))
            dbFile = os.path.join(DBfolder, item)
            try:
                xbmc.log(str(dbFile))
                os.unlink(dbFile)
            except: pass
        elif ('saltshd.lite') in item:
            print str(XvBMC)+str(item)
            #xbmc.log(str(DBfolder+item))
            dbFile = os.path.join(DBfolder, item)
            try:
                xbmc.log(str(dbFile))
                os.remove(dbFile)
            except: pass
        else:
            pass

    for item in exodus:
        if ('cache') in item:
            print str(exodus)+str(item)
            #xbmc.log(str(EXfolder+item))
            dbFile = os.path.join(EXfolder, item)
            try:
                xbmc.log(str(dbFile))
                os.remove(dbFile)
            except: pass
        elif ('providers.8') in item:
            print str(exodus)+str(item)
            #xbmc.log(str(EXfolder+item))
            dbFile = os.path.join(EXfolder, item)
            try:
                xbmc.log(str(dbFile))
                os.remove(dbFile)
            except: pass
        else:
            pass


def HDflush():
    mydisplay = HDflushClass()
    del mydisplay

def HDreset():
    mydisplay = HDresetClass()
    del mydisplay

def RDflush():
    mydisplay = RDflushClass()
    del mydisplay

def RDreset():
    mydisplay = RDresetClass()
    del mydisplay

def ExodusCache():
    mydisplay = ExodusCacheClass()
    del mydisplay

def ExodusSources():
    mydisplay = ExodusSourcesClass()
    del mydisplay

def RemoveAllDB():
    mydisplay = RemoveAllDbClass()
    del mydisplay

 
########################################################################
# This is where we start! Copyright (C) XvBMC Nederland (R) Dutch - NL #
########################################################################


showMenu()

