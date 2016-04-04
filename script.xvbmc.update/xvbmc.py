#!/usr/bin/python
 
'''
    IF you copy/paste 'script.xvbmc.update' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
'''
 
import xbmc, xbmcgui
import shutil
import urllib2,urllib
import os
import xbmcaddon
import time
 
# Set the addon environment
addon = xbmcaddon.Addon('script.xvbmc.update')
 
 
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create('XvBMC Nederland - Maintenance','XvBMC-NL: doing some VooDoo...','')
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
        print 'Download Geannuleerd' # does it break, or does it not break, that is the question :-P
        dp.close()
 
 
def showMenu():
    '''Set up our main menu.'''
    
    # Create list of menu items
    userchoice = []
    userchoice.append("XvBMC ServicePack (2 april)")
    userchoice.append("XvBMC ServicePack (1 t/m ..) bulk pack")
    userchoice.append("XvBMC System/OS LibreELEC_v6.90.004")
    userchoice.append("XvBMC Overclock Pi - none")
    userchoice.append("XvBMC Overclock Pi - turbo")
    userchoice.append("XvBMC Overclock Pi - x265")
    userchoice.append("XvBMC #DEV# Corner (Firmware)")
    userchoice.append("XvBMC #DEV# Corner (OpenELEC_arm-6.95.1)")
    userchoice.append("XvBMC Tweaking")
    userchoice.append("Exit")
    
    # Display the menu  
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland Maintenance", 
                                           userchoice)
    # Process menu actions
    
    #  https://archive.org/download/XvBMC/servicepack.zip                   #
    if userchoice[inputchoice] == "XvBMC ServicePack (2 april)":
        ServicePack()

    #    https://archive.org/download/XvBMC/updaterollup.zip                #
    elif userchoice[inputchoice] == "XvBMC ServicePack (1 t/m ..) bulk pack":
        UpdateRollup()
	
	#    http://releases.libreelec.tv/LibreELEC-RPi2.arm-6.90.004.tar       #
    elif userchoice[inputchoice] == "XvBMC System/OS LibreELEC_v6.90.004":
        SystemOS()
    
    #    /storage/.kodi/addons/script.xvbmc.update/config-noclock.txt       #
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - none":
        Config0()
 
    #    /storage/.kodi/addons/script.xvbmc.update/config-turbo.txt         #
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - turbo":
        Config1()
 
    #    /storage/.kodi/addons/script.xvbmc.update/config-x265.txt          #
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - x265":
        Config2()
 
    #    /storage/.kodi/addons/script.xvbmc.update/firmware.sh                                                                         #
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (Firmware)":
        Firmware()
 
    #    http://openelec.tv/get-openelec/category/57-raspberry-pi2-builds?download=19:raspberry-pi-2-and-pi3-model-b-512mb-update-file #
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (OpenELEC_arm-6.95.1)":
        OpenElecTV()
 
    #    Edit user preferences                                              #
    elif userchoice[inputchoice] == "XvBMC Tweaking":
        xbmcgui.Dialog().ok("XvBMC Tweaks", "EPiC Tweaking @XvBMC bitches", "Coming soon to a theater near you ;-P")
 
 
class ServicePackClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL most recent ServicePacks','Download de laatste XvBMC ServicePack?'):
        url = 'https://github.com/XvBMC/repository.xvbmc/blob/master/zips/update/servicepack.zip?raw=true'
        path = xbmc.translatePath(os.path.join('special://home/addons/','packages')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
#       path = xbmc.translatePath(os.path.join('special://home',''))                 # Standalone # (XvBMC Nederland : https://www.fb.com/groups/XvBMCnederland/)               #
        lib=os.path.join(path, 'update.zip')
        DownloaderClass(url,lib)
        addonfolder = xbmc.translatePath(os.path.join('special://home',''))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,addonfolder))
    
#  	xbmc.executebuiltin("ReloadKeymaps")
   	xbmc.executebuiltin("ReloadSkin()")
	time.sleep(1)
   	xbmc.executebuiltin("Notification(XvBMC Nederland last servicepack,XvBMC updates geslaagd...,5000,special://home/addons/script.xvbmc.update/icon.png)")
 
class UpdateRollupClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL ServicePack Update Rollup','Download ALLE XvBMC SP-updates (all-in-1)?'):
        url = 'https://github.com/XvBMC/repository.xvbmc/blob/master/zips/update/updaterollup.zip?raw=true'
        path = xbmc.translatePath(os.path.join('special://home/addons/','packages')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
#       path = xbmc.translatePath(os.path.join('special://home',''))                 # Standalone # (XvBMC Nederland : https://www.fb.com/groups/XvBMCnederland/)               #
        lib=os.path.join(path, 'update.zip')
        DownloaderClass(url,lib)
        addonfolder = xbmc.translatePath(os.path.join('special://home',''))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,addonfolder))
    
#  	xbmc.executebuiltin("ReloadKeymaps")
   	xbmc.executebuiltin("ReloadSkin()")
	time.sleep(1)
   	xbmc.executebuiltin("Notification(XvBMC Nederland servicepack rollup,XvBMC updates rollup geslaagd...,5000,special://home/addons/script.xvbmc.update/icon.png)")
 
class SystemOSClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC LibreELEC OS update','Preparing v6.90.004 and Reboot when done...'):
        url = 'http://releases.libreelec.tv/LibreELEC-RPi2.arm-6.90.004.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/','')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
#       path = xbmc.translatePath(os.path.join('special://home',''))    # Standalone # (XvBMC Nederland : https://www.fb.com/groups/XvBMCnederland/)               #
        lib=os.path.join(path, 'libreelec690004.tar')
        DownloaderClass(url,lib)
    
#   time.sleep(1)
#  	xbmc.executebuiltin("ReloadKeymaps")
#  	xbmc.executebuiltin("ReloadSkin()")
   	xbmc.executebuiltin("Notification(XvBMC SYSTEM update done,Reboot in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)")
	time.sleep(1)
	xbmc.executebuiltin("Reboot")
 
class Config0Class(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','default-clock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/config0.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
    
#   time.sleep(1)
#  	xbmc.executebuiltin("ReloadKeymaps")
#  	xbmc.executebuiltin("ReloadSkin()")
#  	xbmc.executebuiltin("Notification(XvBMC Nederland Pi default,REBOOT for no-overclock,5000,special://home/addons/script.xvbmc.update/icon.png)")
 
class Config1Class(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','Turbo-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/config1.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
    
#   time.sleep(1)
#  	xbmc.executebuiltin("ReloadKeymaps")
#  	xbmc.executebuiltin("ReloadSkin()")
#   xbmc.executebuiltin("Notification(XvBMC Nederland Pi turbo,REBOOT for turbo-overclock,5000,special://home/addons/script.xvbmc.update/icon.png)")
 
class Config2Class(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','x265-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/config2.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
    
#   time.sleep(1)
#  	xbmc.executebuiltin("ReloadKeymaps")
#  	xbmc.executebuiltin("ReloadSkin()")
#  	xbmc.executebuiltin("Notification(XvBMC Nederland Pi x265,REBOOT for x265-overclock,5000,special://home/addons/script.xvbmc.update/icon.png)")
 
class FirmwareClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Firmware','Update -2- recent Pi firmware?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.update/firmware.sh"
	os.system(bashCommand)
	#~ xbmc.executebuiltin('ReloadSkin()')
    
#   time.sleep(1)
#  	xbmc.executebuiltin("ReloadKeymaps")
#  	xbmc.executebuiltin("ReloadSkin()")
#  	xbmc.executebuiltin("Notification(XvBMC Firmware Update,FINISHED! PLEASE REBOOT...,5000,special://home/addons/script.xvbmc.update/icon.png)")
 
class OpenElecTVClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC OpenELEC OS update','Preparing arm-6.95.1 and Reboot when done...'):
        url = 'http://openelec.tv/get-openelec/category/57-raspberry-pi2-builds?download=19:raspberry-pi-2-and-pi3-model-b-512mb-update-file'
        path = xbmc.translatePath(os.path.join('/storage/.update/','')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
#       path = xbmc.translatePath(os.path.join('special://home',''))    # Standalone # (XvBMC Nederland : https://www.fb.com/groups/XvBMCnederland/)               #
        lib=os.path.join(path, 'openelec6951.tar')
        DownloaderClass(url,lib)
    
#   time.sleep(1)
#  	xbmc.executebuiltin("ReloadKeymaps")
#  	xbmc.executebuiltin("ReloadSkin()")
   	xbmc.executebuiltin("Notification(XvBMC SYSTEM update done,Reboot in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)")
	time.sleep(1)
	xbmc.executebuiltin("Reboot")
 
 
def ServicePack():
    mydisplay = ServicePackClass()
    del mydisplay
 
def UpdateRollup():
    mydisplay = UpdateRollupClass()
    del mydisplay
 
def SystemOS():
    mydisplay = SystemOSClass()
    del mydisplay
 
def Config0():
    mydisplay = Config0Class()
    del mydisplay
 
def Config1():
    mydisplay = Config1Class()
    del mydisplay
 
def Config2():
    mydisplay = Config2Class()
    del mydisplay
 
def Firmware():
    mydisplay = FirmwareClass()
    del mydisplay
 
def OpenElecTV():
    mydisplay = OpenElecTVClass()
    del mydisplay
 
 
########################################################################
# This is where we start!
########################################################################
 
showMenu()