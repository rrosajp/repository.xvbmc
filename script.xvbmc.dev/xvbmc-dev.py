#!/usr/bin/python
 
"""
	IF you copy/paste 'script.xvbmc.dev' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""
 
import xbmc, xbmcgui
import shutil
import urllib2,urllib
import os
import time

# import xbmcaddon
# Set the addon environment
# addon = xbmcaddon.Addon('script.xvbmc.dev')

# Refresh addon environment
# xbmc.executebuiltin("UpdateLocalAddons")
 
 
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create('XvBMC Nederland - #DEV# Corner','XvBMC-NL: doing some VOODOO...','')
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
    userchoice.append("XvBMC #DEV# Corner (Pi Firmware -Cutting Edge)")
    userchoice.append("XvBMC #DEV# Corner (Pi Firmware -20 may 2016)")
    userchoice.append("XvBMC #DEV# Corner (Pi Firmware -Current v3 image)")
    userchoice.append("XvBMC #DEV# Corner (LibreELEC_arm-7.0.1)")
    userchoice.append("XvBMC #DEV# Corner (OpenELEC_arm-6.95.3)")
    userchoice.append("Exit")
    
    # Display the menu
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland #DEV# Menu", 
                                           userchoice)
    # Process menu actions
    
    #  /storage/.kodi/addons/script.xvbmc.update/resources/firmwarerecent.sh
    if userchoice[inputchoice] == "XvBMC #DEV# Corner (Pi Firmware -Cutting Edge)":
        FirmwareRecent()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/firmwaretested.sh
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (Pi Firmware -20 may 2016)":
        FirmwareTested()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/firmwareimage.sh
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (Pi Firmware -Current v3 image)":
        FirmwareImage()
    
	#    http://releases.libreelec.tv/LibreELEC-RPi2.arm-7.0.1.tar
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (LibreELEC_arm-7.0.1)":
        SystemOS()
    
    #    http://openelec.mirror.triple-it.nl/OpenELEC-RPi2.arm-6.95.3.tar
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (OpenELEC_arm-6.95.3)":
        OpenElecTV()
 
 
class FirmwareRecentClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry current firmware','Update -2- Most Recent PI firmware?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/resources/firmwarerecent.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
 
class FirmwareTestedClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry advised Firmware','Flash 20 may 2016 PI firmware?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/resources/firmwaretested.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
 
class FirmwareImageClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Firmware Reset','RE-Flash XvBMC most recent v3 PI firmware?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/resources/firmwareimage.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
 
class SystemOSClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL LibreELEC OS update','Preparing v7.0.1 and Reboot when done...'):

        url = 'http://releases.libreelec.tv/LibreELEC-RPi2.arm-7.0.1.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/',''))
        lib=os.path.join(path, 'libreelec701.tar')
        DownloaderClass(url,lib)

	time.sleep(1)
   	xbmc.executebuiltin("Notification(XvBMC SYSTEM update done,Reboot in 9 seconds...,9000,special://home/addons/script.xvbmc.update/icon.png)")
	xbmc.executebuiltin("Reboot")
 
class OpenElecTVClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL OpenELEC OS update','Preparing arm-6.95.3 and Reboot when done...'):

        url = 'http://openelec.mirror.triple-it.nl/OpenELEC-RPi2.arm-6.95.3.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/',''))
        lib=os.path.join(path, 'openelec6953.tar')
        DownloaderClass(url,lib)

	time.sleep(1)		
   	xbmc.executebuiltin("Notification(XvBMC SYSTEM update done,Reboot in 9 seconds...,9000,special://home/addons/script.xvbmc.update/icon.png)")
	xbmc.executebuiltin("Reboot")
 
def FirmwareRecent():
    mydisplay = FirmwareRecentClass()
    del mydisplay
 
def FirmwareTested():
    mydisplay = FirmwareTestedClass()
    del mydisplay
 
def FirmwareImage():
    mydisplay = FirmwareImageClass()
    del mydisplay
 
def SystemOS():
    mydisplay = SystemOSClass()
    del mydisplay
 
def OpenElecTV():
    mydisplay = OpenElecTVClass()
    del mydisplay
 
 
 
########################################################################
# This is where we start! Copyright (C) XvBMC Nederland (R) Dutch - NL #
########################################################################
 
showMenu()