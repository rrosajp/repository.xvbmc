#!/usr/bin/python

"""
	IF you copy/paste 'script.xvbmc.oc' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""

import xbmc,xbmcaddon,xbmcgui,xbmcplugin
import os,shutil,time
import urllib2,urllib
#import downloader
#import extract


################ ProgTitle = "XvBMC OC"   ######################
AddonID        = 'script.xvbmc.oc'
addon_id       = 'script.xvbmc.oc'
ADDON          = xbmcaddon.Addon(id=addon_id)
dialog         = xbmcgui.Dialog()
piOC           = 'XvBMC overclock [COLOR white]Pi[/COLOR]'
################ ProgTitle = "XvBMC OC"   ######################


def showMenu():
    '''Set up our XvBMC-OC Menu'''
    
    # Create list of menu items
    userchoice = []
    userchoice.append(piOC+' -None')
    userchoice.append(piOC+' -High')
    userchoice.append(piOC+' -Turbo')
    userchoice.append(piOC+' -Max')
    userchoice.append("[B][COLOR white]Exit[/COLOR][/B]")
    
    # Display the menu
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland [B]-[/B] #OVERCLOCK# [COLOR red]\'RPi\'[/COLOR]", 
                                           userchoice)
    # Process menu actions
    
    #	/resources/data/config-noclock.txt
    if userchoice[inputchoice] == piOC+' -None':
        Config0()
    
    #	/resources/data/config-high.txt
    elif userchoice[inputchoice] == piOC+' -High':
        Config1()
	
    #	/resources/data/config-turbo.txt
    elif userchoice[inputchoice] == piOC+' -Turbo':
        Config2()
    
    #	/resources/data/config-x265.txt
    elif userchoice[inputchoice] == piOC+' -Max':
        Config3()


class Config0Class(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','default-clock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.oc/resources/config0.sh"
	os.system(bashCommand)
	dialog.ok("XvBMC Nederland", 'XvBMC Pi NOT overclocked','', 'Press OK to reboot...')
	xbmc.executebuiltin("Reboot")

class Config1Class(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','High-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.oc/resources/config1.sh"
	os.system(bashCommand)
	dialog.ok("XvBMC Nederland", 'XvBMC High-overclocked Pi','', 'Press OK to reboot...')
	xbmc.executebuiltin("Reboot")

class Config2Class(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','Turbo-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.oc/resources/config2.sh"
	os.system(bashCommand)
	dialog.ok("XvBMC Nederland", 'XvBMC Turbo-overclocked Pi','', 'Press OK to reboot...')
	xbmc.executebuiltin("Reboot")

class Config3Class(xbmcgui.Window):
  def __init__(self):
    #  dialog = xbmcgui.Dialog()
    if dialog.yesno('XvBMC NL Raspberry Pi instellen','Max-overclock Raspberry Pi?'):
        bashCommand = "/bin/bash /storage/.kodi/addons/script.xvbmc.oc/resources/config3.sh"
	os.system(bashCommand)
	dialog.ok("XvBMC Nederland", 'XvBMC x265-overclock Pi','', 'Press OK to reboot...')
	xbmc.executebuiltin("Reboot")


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

