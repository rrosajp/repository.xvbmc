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


# ProgTitle="XvBMC OverClock" #
dialog = xbmcgui.Dialog()
# ProgTitle="XvBMC OverClock" #


def showMenu():
    '''Set up our XvBMC-OC Menu'''
    
    # Create list of menu items
    userchoice = []
    userchoice.append("XvBMC overclock [COLOR white]Pi[/COLOR] -None")
    userchoice.append("XvBMC overclock [COLOR white]Pi[/COLOR] -High")
    userchoice.append("XvBMC overclock [COLOR white]Pi[/COLOR] -Turbo")
    userchoice.append("XvBMC overclock [COLOR white]Pi[/COLOR] -Max")
    userchoice.append("[B][COLOR white]Exit[/COLOR][/B]")
    
    # Display the menu
    inputchoice = xbmcgui.Dialog().select("XvBMC Nederland #OVERCLOCK# Menu", 
                                           userchoice)
    # Process menu actions
    
    #	/resources/data/config-noclock.txt
    if userchoice[inputchoice] == "XvBMC overclock [COLOR white]Pi[/COLOR] -None":
        Config0()
    
    #	/resources/data/config-high.txt
    elif userchoice[inputchoice] == "XvBMC overclock [COLOR white]Pi[/COLOR] -High":
        Config1()
	
    #	/resources/data/config-turbo.txt
    elif userchoice[inputchoice] == "XvBMC overclock [COLOR white]Pi[/COLOR] -Turbo":
        Config2()
    
    #	/resources/data/config-x265.txt
    elif userchoice[inputchoice] == "XvBMC overclock [COLOR white]Pi[/COLOR] -Max":
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

