#!/usr/bin/python
 
"""
	IF you copy/paste 'script.xvbmc.oc' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""
 
import xbmc, xbmcgui
import shutil
import urllib2,urllib
import os
import time

# import xbmcaddon
 
# Set the addon environment
# addon = xbmcaddon.Addon('script.xvbmc.oc')

# Refresh addon environment
# xbmc.executebuiltin("UpdateLocalAddons")
 
 
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create('XvBMC Nederland - OverClock','XvBMC-NL: doing some VOODOO...','')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
  
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print 'Gedownload:'+str(percent)+'%'
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print 'Download Geannuleerd'
        dp.close()
 
 
 
def showMenu():
    '''Set up our XvBMC Main-Menu'''
    
    # Create list of menu items
    userchoice = []
    userchoice.append("XvBMC Overclock Pi - none")
    userchoice.append("XvBMC Overclock Pi - High")
    userchoice.append("XvBMC Overclock Pi - Turbo")
    userchoice.append("XvBMC Overclock Pi - Max")
    userchoice.append("Exit")
    
    # Display the menu
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland #OVERCLOCK# Menu", 
                                           userchoice)
    # Process menu actions
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/data/config-noclock.txt
    if userchoice[inputchoice] == "XvBMC Overclock Pi - none":
        Config0()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/data/config-high.txt
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - High":
        Config1()
	
    #    /storage/.kodi/addons/script.xvbmc.update/resources/data/config-turbo.txt
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - Turbo":
        Config2()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/data/config-x265.txt
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - Max":
        Config3()
 
 
class Config0Class(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','default-clock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/resources/config0.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
 
class Config1Class(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','High-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/resources/config1.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
 
class Config2Class(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','Turbo-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/resources/config2.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
 
class Config3Class(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','Max-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/resources/config3.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
 
def Config0():
    mydisplay = Config0Class()
    del mydisplay
 
def Config1():
    mydisplay = Config1Class()
    del mydisplay
 
def Config2():
    mydisplay = Config2Class()
    del mydisplay
 
def Config3():
    mydisplay = Config3Class()
    del mydisplay
 
 
 
########################################################################
# This is where we start! Copyright (C) XvBMC Nederland (R) Dutch - NL #
########################################################################
 
showMenu()