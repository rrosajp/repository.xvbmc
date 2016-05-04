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

# Refresh addon environment
# xbmc.executebuiltin("UpdateLocalAddons")
 
 
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
    '''Set up our XvBMC Main-Menu'''
    
    # Create list of menu items                                                       #
    userchoice = []
    userchoice.append("XvBMC ServicePack 01 (01-05-2016)")
    userchoice.append("XvBMC ServicePack (00 t/m 01) bulk pack")
    userchoice.append("XvBMC Refresh UpdateAddonRepos")
    userchoice.append("XvBMC OverClock (raspberry Pi)")
    userchoice.append("XvBMC #DEV# Corner (Firmware-OS-etc)")
    userchoice.append("XvBMC Tweaking")
    userchoice.append("Exit")
    
    # Display the menu                                                                #
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland Maintenance", 
                                           userchoice)
    # Process menu actions
    
    #  https://archive.org/download/XvBMC/servicepack.zip                             #
    if userchoice[inputchoice] == "XvBMC ServicePack 01 (01-05-2016)":
        ServicePack()
    
    #    https://archive.org/download/XvBMC/updaterollup.zip                          #
    elif userchoice[inputchoice] == "XvBMC ServicePack (00 t/m 01) bulk pack":
        UpdateRollup()
    
    #    http://kodi.wiki/view/List_of_built-in_functions                             #
    elif userchoice[inputchoice] == "XvBMC Refresh UpdateAddonRepos":
        forceRefresh()
    
    #    OCmenu  XvBMC Nederland                                                      #
    elif userchoice[inputchoice] == "XvBMC OverClock (raspberry Pi)":
        subOCmenu()
    
    #    DEVmenu XvBMC Nederland                                                      #
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (Firmware-OS-etc)":
        subDEVmenu()
    
    #    edit EPiC user preferences                                                   #
    elif userchoice[inputchoice] == "XvBMC Tweaking":
        xbmcgui.Dialog().ok("XvBMC NL Tweaks", "EPiC XvBMC Tweaking bitches...", "Coming soon to a theater near you ;-P")
 
 
class ServicePackClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL most recent ServicePacks','Download de laatste XvBMC ServicePack?'):
        url = 'https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/sp/01-servicepack.zip'
        path = xbmc.translatePath(os.path.join('special://home/addons/','packages')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
        lib=os.path.join(path, 'update.zip')
        DownloaderClass(url,lib)
        addonfolder = xbmc.translatePath(os.path.join('special://home',''))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,addonfolder))
 
	time.sleep(1)
	xbmc.executebuiltin("Notification(XvBMC Nederland last servicepack,ServicePack update finished!,6000,special://home/addons/script.xvbmc.update/icon.png)")
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
#	xbmc.executebuiltin("ReloadSkin()")
#	xbmc.executebuiltin("LoadProfile(Master user,)")
#	time.sleep(1)
#	xbmc.executebuiltin("Reboot")
 
class UpdateRollupClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL ServicePack Update Rollup','Download ALLE XvBMC SP-updates (all-in-1)?'):
	xbmc.executebuiltin("UpdateLocalAddons")
        url = 'https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/sp/01-sp-rollup.zip'
        path = xbmc.translatePath(os.path.join('special://home/addons/','packages')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
        lib=os.path.join(path, 'update.zip')
        DownloaderClass(url,lib)
        addonfolder = xbmc.translatePath(os.path.join('special://home',''))
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,addonfolder))

 	time.sleep(1)
	xbmc.executebuiltin("Notification(XvBMC Nederland servicepack rollup,ServicePack bulk update finished!,7000,special://home/addons/script.xvbmc.update/icon.png)")
	xbmc.executebuiltin("UpdateLocalAddons")
	xbmc.executebuiltin("UpdateAddonRepos")
#	xbmc.executebuiltin("ReloadSkin()")
#	xbmc.executebuiltin("LoadProfile(Master user,)")
#	time.sleep(1)
#	xbmc.executebuiltin("Reboot")
 
class forceRefreshClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    xbmc.executebuiltin("UpdateLocalAddons")
    dialog.ok('XvBMC Nederland Maintenance', 'De addons worden vernieuwd...')
    xbmc.executebuiltin("UpdateAddonRepos")
    time.sleep(1)
    xbmc.executebuiltin("ReloadSkin()")
 
def ServicePack():
    mydisplay = ServicePackClass()
    del mydisplay
 
def UpdateRollup():
    mydisplay = UpdateRollupClass()
    del mydisplay
 
def forceRefresh():
    mydisplay = forceRefreshClass()
    del mydisplay
 
 
 
def subOCmenu():
    '''Set up our XvBMC OC-Menu'''
    
    # Create list of menu items                                                        #
    userchoice = []
    userchoice.append("XvBMC Overclock Pi - none")
    userchoice.append("XvBMC Overclock Pi - High")
    userchoice.append("XvBMC Overclock Pi - Turbo")
    userchoice.append("XvBMC Overclock Pi - Max")
    userchoice.append("Exit")
    
    # Display the menu                                                                 #
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland #OVERCLOCK# Menu", 
                                           userchoice)
    # Process menu actions
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/bin/config-noclock.txt    #
    if userchoice[inputchoice] == "XvBMC Overclock Pi - none":
        Config0()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/bin/config-high.txt       #
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - High":
        Config1()
	
    #    /storage/.kodi/addons/script.xvbmc.update/resources/bin/config-turbo.txt      #
    elif userchoice[inputchoice] == "XvBMC Overclock Pi - Turbo":
        Config2()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/bin/config-x265.txt       #
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
 
 
 
def subDEVmenu():
    '''Set up our XvBMC DEV-Menu'''
    
    # Create list of menu items                                                   #
    userchoice = []
    userchoice.append("XvBMC #DEV# Corner (Firmware - Cutting Edge)")
    userchoice.append("XvBMC #DEV# Corner (Firmware - 12 april 2016)")
    userchoice.append("XvBMC #DEV# Corner (Firmware - Current v3 image)")
    userchoice.append("XvBMC #DEV# Corner (LibreELEC_arm-7.0.0)")
    userchoice.append("XvBMC #DEV# Corner (OpenELEC_arm-6.95.2)")
    userchoice.append("Exit")
    
    # Display the menu                                                            #
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland #DEV# Menu", 
                                           userchoice)
    # Process menu actions
    
    #  /storage/.kodi/addons/script.xvbmc.update/resources/firmwarerecent.sh      #
    if userchoice[inputchoice] == "XvBMC #DEV# Corner (Firmware - Cutting Edge)":
        FirmwareRecent()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/firmwaretested.sh    #
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (Firmware - 12 april 2016)":
        FirmwareTested()
    
    #    /storage/.kodi/addons/script.xvbmc.update/resources/firmwareimage.sh     #
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (Firmware - Current v3 image)":
        FirmwareImage()
    
	#    http://releases.libreelec.tv/LibreELEC-RPi2.arm-7.0.0.tar                 #
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (LibreELEC_arm-7.0.0)":
        SystemOS()
    
    #    http://openelec.mirror.triple-it.nl/OpenELEC-RPi2.arm-6.95.2.tar         #
    elif userchoice[inputchoice] == "XvBMC #DEV# Corner (OpenELEC_arm-6.95.2)":
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
    if dialog.yesno('XvBMC NL Raspberry advised Firmware','Flash 12 april 2016 PI firmware?'):
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
    if dialog.yesno('XvBMC NL LibreELEC OS update','Preparing v7.0.0 and Reboot when done...'):
        url = 'http://releases.libreelec.tv/LibreELEC-RPi2.arm-7.0.0.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/','')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
#       path = xbmc.translatePath(os.path.join('special://home',''))    # Standalone # (XvBMC Nederland : https://www.fb.com/groups/XvBMCnederland/)               #
        lib=os.path.join(path, 'libreelec700.tar')
        DownloaderClass(url,lib)
 
   	xbmc.executebuiltin("Notification(XvBMC SYSTEM update done,Reboot in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)")
	time.sleep(1)
	xbmc.executebuiltin("Reboot")
 
class OpenElecTVClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL OpenELEC OS update','Preparing arm-6.95.2 and Reboot when done...'):
        url = 'http://openelec.mirror.triple-it.nl/OpenELEC-RPi2.arm-6.95.2.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/','')) # Raspberry  # (XvBMC Nederland : https://www.fb.com/groups/XbmcVoorBeginnersRaspberryPi/) #
#       path = xbmc.translatePath(os.path.join('special://home',''))    # Standalone # (XvBMC Nederland : https://www.fb.com/groups/XvBMCnederland/)               #
        lib=os.path.join(path, 'openelec6952.tar')
        DownloaderClass(url,lib)
 
   	xbmc.executebuiltin("Notification(XvBMC SYSTEM update done,Reboot in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)")
	time.sleep(1)
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