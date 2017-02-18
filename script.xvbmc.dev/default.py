#!/usr/bin/python
 
"""
	IF you copy/paste 'script.xvbmc.dev' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""
 
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
import os,shutil,time
import urllib2,urllib
import downloader
#import extract


################ ProgTitle = "XvBMC DEV"  ######################
AddonID        = 'script.xvbmc.dev'
addon_id       = 'script.xvbmc.dev'
ADDON          = xbmcaddon.Addon(id=addon_id)
dialog         = xbmcgui.Dialog()
piOS           = '[COLOR red]\'RPi\'[/COLOR]'
testedfirmware = '-29dec_2016 -LE703'     # knownworkingfirmware
xvbmcbuildfirm = '-20jan_2017 -v31_image' # currentxvbmcfirmware 
################ ProgTitle = "XvBMC DEV"  ######################


def showMenu():
    '''Set up our XvBMC-DEV Menu'''
    
    # Create list of menu items
    userchoice = []
    userchoice.append('XvBMC #DEV# Corner ([COLOR white]Pi[/COLOR] Firmware -Cutting Edge)')
    userchoice.append('XvBMC #DEV# Corner ([COLOR white]Pi[/COLOR] Firmware '+testedfirmware +')')
    userchoice.append('XvBMC #DEV# Corner ([COLOR white]Pi[/COLOR] Firmware '+xvbmcbuildfirm +')')
    userchoice.append('XvBMC #DEV# Corner ([COLOR white]Libre[/COLOR]ELEC_arm-7.0.3) '+piOS)
    userchoice.append('XvBMC #DEV# Corner ([COLOR white]Open[/COLOR]ELEC_arm-7.0.1) '+piOS)
    userchoice.append('[B][COLOR white]Exit[/COLOR][/B]')
    
    # Display the menu
    inputchoice = xbmcgui.Dialog().select('XvBMC Nederland '+piOS+'[B]-[/B]#DEV#[B]-[/B]Menu ', 
                                           userchoice)
    # Process menu actions
    
    #  /storage/.kodi/addons/script.xvbmc.dev/resources/firmwarerecent.sh
    if userchoice[inputchoice] == 'XvBMC #DEV# Corner ([COLOR white]Pi[/COLOR] Firmware -Cutting Edge)':
        FirmwareRecent()
    
    #    /storage/.kodi/addons/script.xvbmc.dev/resources/firmwaretested.sh
    elif userchoice[inputchoice] == 'XvBMC #DEV# Corner ([COLOR white]Pi[/COLOR] Firmware '+testedfirmware +')':
        FirmwareTested()
    
    #    /storage/.kodi/addons/script.xvbmc.dev/resources/firmwareimage.sh
    elif userchoice[inputchoice] == 'XvBMC #DEV# Corner ([COLOR white]Pi[/COLOR] Firmware '+xvbmcbuildfirm +')':
        FirmwareImage()
    
	#    /releases.libreelec.tv/LibreELEC-RPi2.arm-etceteraetceteraetcetera
    elif userchoice[inputchoice] == 'XvBMC #DEV# Corner ([COLOR white]Libre[/COLOR]ELEC_arm-7.0.3) '+piOS:
        SystemOS()
    
    #    /openelec.mirror.triple-it.nl/OpenELEC-RPi2.arm-etceteraetceteraetcetera
    elif userchoice[inputchoice] == 'XvBMC #DEV# Corner ([COLOR white]Open[/COLOR]ELEC_arm-7.0.1) '+piOS:
        OpenElecTV()


class FirmwareRecentClass(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC-NL Raspberry current firmware','Update most recent PI2+3 firmware?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.dev/resources/firmwarerecent.sh"
	os.system(bashCommand)
	dialog.ok("XvBMC Nederland", 'XvBMC most recent Firmware flashed','', 'Press OK to reboot...')
	xbmc.executebuiltin("Reboot")

class FirmwareTestedClass(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC-NL Raspberry advised firmware','Flash recent/verified firmware: '+testedfirmware +' ?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.dev/resources/firmwaretested.sh"
	os.system(bashCommand)
	dialog.ok("XvBMC Nederland", 'XvBMC advised Firmware flashed','', 'Press OK to reboot...')
	xbmc.executebuiltin("Reboot")

class FirmwareImageClass(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC-NL Raspberry firmware reset','RE-Flash current XvBMC-image firmware: '+xvbmcbuildfirm +' ?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.dev/resources/firmwareimage.sh"
	os.system(bashCommand)
	dialog.ok("XvBMC Nederland", 'XvBMC default Firmware re-flashed','', 'Press OK to reboot...')
	xbmc.executebuiltin("Reboot")

class SystemOSClass(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC-NL LibreELEC OS update','Preparing v7.0.3 and Reboot when done...'):
		url='http://releases.libreelec.tv/LibreELEC-RPi2.arm-7.0.3.tar'
		path = xbmc.translatePath(os.path.join('/storage/.update/',''))
		dp = xbmcgui.DialogProgress()
		dp.create("XvBMC Nederland","XvBMC-DEV: doing some VOODOO...",'', 'Please Wait')
		lib=os.path.join(path, 'libreelec703.tar')
		try:
			os.remove(lib)
		except:
			pass
		downloader.download(url, lib, dp)
	#	addonfolder = xbmc.translatePath(os.path.join('/storage/.update/',''))
		time.sleep(3)
	#	dp.update(0,"", "Extracting ZiP Please Wait...")
	#	print '=== EXCTRACTING LibreELEC ==='
	#	extract.all(lib,addonfolder,dp)
		dialog.ok("XvBMC Nederland", 'LibreELEC SYSTEM update finished!','', 'Press OK to reboot...')
		xbmc.executebuiltin("Reboot")

class OpenElecTVClass(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC-NL OpenELEC OS update','Preparing arm-7.0.1 and Reboot when done...'):
		url='http://openelec.mirror.triple-it.nl/OpenELEC-RPi2.arm-7.0.1.tar'
		path = xbmc.translatePath(os.path.join('/storage/.update/',''))
		dp = xbmcgui.DialogProgress()
		dp.create("XvBMC Nederland","XvBMC-DEV: doing some VOODOO...",'', 'Please Wait')
		lib=os.path.join(path, 'openelec701.tar')
		try:
			os.remove(lib)
		except:
			pass
		downloader.download(url, lib, dp)
	#	addonfolder = xbmc.translatePath(os.path.join('/storage/.update/',''))
		time.sleep(3)
	#	dp.update(0,"", "Extracting ZiP Please Wait...")
	#	print '=== EXCTRACTING OpenELEC ==='
	#	extract.all(lib,addonfolder,dp)
		dialog.ok("XvBMC Nederland", 'OpenELEC SYSTEM update finished!','', 'Press OK to reboot...')
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

