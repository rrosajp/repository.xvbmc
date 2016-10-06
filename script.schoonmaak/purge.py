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


#        ProgTitle ="XvBMC-NL-Maintenance"          #
dialog = xbmcgui.Dialog()
#        ProgTitle ="XvBMC-NL-Maintenance"          #


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

exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("M2IgMjIgKCk6IzcwOjEKCTQyID0xNSAoKSM3MDoxNgoJMTMgYiAxYiA0MiA6IzcwOjE4CgkJNTkgPTE3IC4xYyAoYiAuMTAgKSM3MDoxOQoJCTViIDZkIC4xMCAuNGMgKDU5ICk9PWMgOiM3MDoyMAoJCQkxMyA0MyAsMyAsNSAxYiA2ZCAuNWEgKDU5ICk6IzcwOjIxCgkJCQk1YiAxZCAoMyApPjAgMjYgMWQgKDUgKT4wIDojNzA6MjcKCQkJCQkxMyA3IDFiIDUgOiM3MDoyOAoJCQkJCQkxYSA6IzcwOjI5CgkJCQkJCQk2ZCAuMWUgKDZkIC4xMCAuNmMgKDQzICw3ICkpIzcwOjMwCgkJCQkJCWUgOjEyICM3MDozMQoJCQkJCTEzIDYgMWIgMyA6IzcwOjMyCgkJCQkJCTFhIDojNzA6MzMKCQkJCQkJCTkgLjggKDZkIC4xMCAuNmMgKDQzICw2ICkpIzcwOjM0CgkJCQkJCWUgMTEgOiM3MDozNQoJCQkJCQkJOSAuOCAoNTkgLDZmID1jICkjNzA6MzYKCQkJCQkJMWYgOiM3MDozNwoJCQkJCQkJOSAuOCAoNTkgLDZmID1jICkjNzA6MzgKCQkJCQkJCTEyICM3MDozOQoJCQkJNWUgMWQgKDMgKT09MCAyNiAxZCAoNSApPT0wIDojNzA6NDEKCQkJCQkxMyA3IDFiIDUgOiM3MDo0NQoJCQkJCQkxYSA6IzcwOjQ2CgkJCQkJCQk2ZCAuMWUgKDZkIC4xMCAuNmMgKDQzICw3ICkpIzcwOjQ3CgkJCQkJCWUgOjEyICM3MDo0OAoJCQkJCTEzIDYgMWIgMyA6IzcwOjQ5CgkJCQkJCTFhIDojNzA6NTAKCQkJCQkJCTkgLjggKDZkIC4xMCAuNmMgKDQzICw2ICkpIzcwOjUxCgkJCQkJCWUgMTEgOiM3MDo1MgoJCQkJCQkJOSAuOCAoNTkgLDZmID1jICkjNzA6NTMKCQkJCQkJMWYgOiM3MDo1NAoJCQkJCQkJOSAuOCAoNTkgLDZmID1jICkjNzA6NTUKCQkJCQkJCTEyICM3MDo1NgoJCTFhIDojNzA6NTgKCQkJMTcgLjNlICgzYyAoNTkgKSkjNzA6NjEKCQkJOSAuOCAoNTkgLDZmID1jICkjNzA6NjIKCQllIDExIDojNzA6NjMKCQkJOSAuOCAoNTkgLDZmID1jICkjNzA6NjQKCQkxZiA6IzcwOjY1CgkJCTkgLjggKDU5ICw2ZiA9YyApIzcwOjY2CgkJCTEyICM3MDo2NwoJNGQgLjY4ICgiLT0gM2YgMmYgPS0gIiwnNjAgNGUgNWMgMWIgNWYgNTcnLCcnLCcoNGYgNWMgNmUgMmIgNmUgYSAyNCknKSM3MDo2OQoJMTcgLmYgKCIxNCIpIzcwOjcxCgkxNyAuZiAoIjZhIikjNzA6NzIKIiIiCgk0NCA0MCA1ZC8yZSAnMjUuMmQnIDJhIDNhIDRhIDIzIC0yLSA2YiAtNC0gMmMtNGIsIDNkLgoiIiIKI2Q=")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|O0OOOOOO0OOOO0OO0|4|OOOO0OOOO0O0OO0O0|O00OOO0OO0O00O0OO|O0OOOOO00O0OO00O0|rmtree|shutil|a|O0O0OOOO000O00O00|True|e9015584e6a44b14988f13e2298bcbf9|except|executebuiltin|path|OSError|pass|for|UpdateLocalAddons|setupXvbmcEntries|16|xbmc|18|19|try|in|translatePath|len|unlink|else|20|21|purgeOLD|credits|whistle|script|and|27|28|29|please|clean|XvBMC|purge|paste|DONE|30|31|32|33|34|35|36|37|38|39|keep|def|str|Thx|log|ALL|you|41|O00000OOO00OO0O0O|OOO0O0OO000OO0000|IF|45|46|47|48|49|the|NL|exists|dialog|system|everything|50|51|52|53|54|55|56|condition|58|OO000OOOO000OOOOO|walk|if|is|copy|elif|good|your|61|62|63|64|65|66|67|ok|69|UpdateAddonRepos|EPiC|join|os|as|ignore_errors|line|71|72".split("|")))


#######################################################################
#						do some VooDoo
#######################################################################

purgeOLD()
