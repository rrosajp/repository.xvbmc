#!/usr/bin/python
 
"""
	IF you copy/paste 'script.schoonmaak' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""

#   script.schoonmaak (EPiC Kodi Schoonmaak XvBMC Nederland)
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


import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os, sys, time

#addon_id = 'script.schoonmaak'
#ADDON    = xbmcaddon.Addon(id=addon_id)
#AddonID  = 'script.schoonmaak'
HOME      = xbmc.translatePath('special://home/')
dialog    = xbmcgui.Dialog()

waarschuwing   = '[COLOR=red][B]!!!  WARNING  !!![/B][/COLOR]'
readme         = 'if you\'re seeing this message read this first[B]:[/B]'
noservicepack  = 'Sorry the [B]S[/B]ervice[B]P[/B]ack update is [COLOR=red]outdated[/COLOR] at this moment'
notforked      = '[COLOR dimgray](the newest XvBMC\'s [B]Pi[/B]-image is not forked, [B]yet[/B]...)[/COLOR]'


###############################################################
###FORCE CLOSE KODI - ANDROID ONLY WORKS IF ROOTED#############
###############################################################

def killKodi():
    choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok('[COLOR=red][B]WARNING  !!![/COLOR][/B]', 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: xbmc.executebuiltin("Reboot")
        except: pass
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok('[COLOR=red][B]WARNING  !!![/COLOR][/B]', 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass
        try : os . system ( 'Process.killProcess(android.os.Process.org.fire.guru());' )
        except : pass
        try : os . system ( 'Process.killProcess(android.os.Process.org.fire.guruv());' )
        except : pass
        try : os . system ( 'Process.killProcess(android.os.Process.com.semperpax.spmc16());' )
        except : pass
        try : os . system ( 'Process.killProcess(android.os.Process.org.fire());' )
        except : pass
        try : os . system ( 'Process.killProcess(android.os.Process.org.fire,guru());' )
        except : pass
        dialog.ok('[COLOR=red][B]WARNING  !!![/COLOR][/B]', 'Your system has been detected as Android, you ', '[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Either close using Task Manager (If unsure pull the plug).')
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok('[COLOR=red][B]WARNING  !!![/COLOR][/B]', 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Use task manager and NOT ALT F4')
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok('[COLOR=red][B]WARNING  !!![/COLOR][/B]', 'If you\'re seeing this message it means the force close', 'was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.','Your platform could not be detected so just pull the power cable.')    

		
##########################
###DETERMINE PLATFORM#####
##########################

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

def verifyplatform():
#   choice = dialog.yesno('XvBMC Nederland (Dutch)', '*verify platform*', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
#   if choice == 0:
#       return
#   elif choice == 1:
#       pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        dialog.ok(waarschuwing, readme, '[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO guarantees for OSX [B];-p[/B]')
    elif myplatform == 'linux': #Linux
        #dialog.ok('XvBMC NL most recent ServicePack', 'Download de laatste XvBMC (Open-/LibreELEC) ServicePack?','','') # N.V.T. als er een actuele SP is dan willen we die natuurlijk ook lol ;-p #
        print '=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ==='	
    elif myplatform == 'android': # Android # inclusief bonus melding Android-Updater #
        dialog.ok('[COLOR=red][B]!!!  IMPORTANT  !!![/COLOR][/B]', '[COLOR=lime]There\'s also a specific XvBMC\'s Android add-on update(r)[/COLOR]', '...enkel voor specifieke bonus Android add-on updates...', noservicepack +' ' +notforked) # , 'NOTE: ' +noservicepack +notforked +'(let op)'
    elif myplatform == 'windows': # Windows
        #dialog.ok(waarschuwing,  readme, noservicepack, notforked)  # N.V.T. als er een actuele SP is dan willen we die natuurlijk ook lol ;-p #
        print '=== Download de laatste XvBMC (Windows) ServicePack ==='		
    else: #ATV
        dialog.ok(waarschuwing, readme, '[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO guarantees for ATV [B];-p[/B]')


##########################
###CrapCleaner############
##########################

def removefolder(map, exclude=None):
    for root, dirs, files in os.walk(map, topdown=False):
        for name in files:
            if(root.find(exclude) > 0):
                continue
            try: os.remove(os.path.join(root, name))
            except: pass
        for name in dirs:
            if(name == exclude):
                continue
            try: os.rmdir(os.path.join(root, name))
            except: pass

def REMOVE_EMPTY_FOLDERS():
#initialize the counters
    print"########### Start Removing Empty Folders #########"
    empty_count = 0
    used_count = 0
    for curdir, subdirs, files in os.walk(HOME):
        if len(subdirs) == 0 and len(files) == 0: #check for empty directories. len(files) == 0 may be overkill
            empty_count += 1 #increment empty_count
            os.rmdir(curdir) #delete the directory
            print "successfully removed: "+curdir
        elif len(subdirs) > 0 and len(files) > 0: #check for used directories
            used_count += 1 #increment 


##########################
###TextBox Viewer(s)######
##########################

def TextBoxes(announce):
	class TextBox():
		WINDOW=10147
		CONTROL_LABEL=1
		CONTROL_TEXTBOX=5
		def __init__(self,*args,**kwargs):
			xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
			self.win=xbmcgui.Window(self.WINDOW) # get window
			xbmc.sleep(500) # give window time to initialize
			self.setControls()
		def setControls(self):
			self.win.getControl(self.CONTROL_LABEL).setLabel('XvBMC - View Log[B]:[/B]') # set heading
			try: f=open(announce); text=f.read()
			except: text=announce
			self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
			return
	TextBox()
	while xbmc.getCondVisibility('Window.IsVisible(10147)'):
		time.sleep(.5)

def TextBoxesPlain(announce):
	class TextBox():
		WINDOW=10147
		CONTROL_LABEL=1
		CONTROL_TEXTBOX=5
		def __init__(self,*args,**kwargs):
			xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
			self.win=xbmcgui.Window(self.WINDOW) # get window
			xbmc.sleep(500) # give window time to initialize
			self.setControls()
		def setControls(self):
			self.win.getControl(self.CONTROL_LABEL).setLabel('[B]X[/B]v[B]BMC N[/B]ederland') # set heading
			try: f=open(announce); text=f.read()
			except: text=announce
			self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
			return
	TextBox()
	while xbmc.getCondVisibility('Window.IsVisible(10147)'):
		time.sleep(.5)

"""
	IF you copy/paste 'common.py' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""