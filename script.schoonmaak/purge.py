#!/usr/bin/python
 
"""
	IF you copy/paste 'script.purge' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""

#   script.Purge (Kodi Purge + Schoonmaak XvBMC)
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


import os, xbmc, xbmcgui, shutil


#		 ProgTitle="XvBMC Raw Maintenance" 		#
dialog = xbmcgui.Dialog()
#		 ProgTitle="XvBMC Raw Maintenance" 		#


#######################################################################
#                          CLASSES
#######################################################################


class cacheEntry:
    def __init__(self, namei, pathi):
        self.name = namei
        self.path = pathi


#######################################################################
#						Work Functions
#######################################################################


def setupXvbmcEntries():
    entries = 9 #make sure this reflects the amount of entries you have
    dialogName = ["DutchNubes", "NLVIEW", "nl-viewer", "nl-viewer2", "nlv3", "SportCenterHD", "SportsDevil", "NLviewRepo", "TVaddons.nl"]
    pathName = ["special://home/addons/plugin.video.cloudtv",
				"special://home/addons/plugin.video.NLVIEW",
				"special://home/addons/plugin.video.nl-viewer",
				"special://home/addons/plugin.video.nl-viewer2",
				"special://home/addons/plugin.video.nlv3",
				"special://home/addons/plugin.video.sportcenterhd",
				"special://home/addons/plugin.video.SportsDevil",
				"special://home/addons/repository.NLVIEW",
				"special://home/addons/repository.tvaddons.nl"]
                    
    XvbmcEntries = []
    
    for x in range(entries):
        XvbmcEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return XvbmcEntries


#######################################################################
#						CRAPCLEANER
#######################################################################
def purgeOLD():
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
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d), ignore_errors=True)
                        except:
                            pass

                else:
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.cloudtv')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.NLVIEW')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.nl-viewer')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.nl-viewer2')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.nlv3')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.sportcenterhd')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','plugin.video.SportsDevil')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','repository.NLVIEW')), ignore_errors=True)
                    shutil.rmtree(xbmc.translatePath(os.path.join('special://home/addons/','repository.tvaddons.nl')), ignore_errors=True)
                    dialog.ok("XvBMC Nederland", 'we found some orphaned dependencies...','', 'NOTE: a REBOOT is highly recommended!')
                    xbmc.executebuiltin("UpdateLocalAddons")
                    pass

        else:
          # dialog.ok("XvBMC-NL Purge", "Crap cleaner all done...")
            pass

    dialog.ok("-= ALL DONE =- ", 'your system seems in good condition','', '(everything is as clean as a whistle)')
#	return


#######################################################################
#						do some VooDoo
#######################################################################


purgeOLD()

