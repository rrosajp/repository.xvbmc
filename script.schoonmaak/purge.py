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


import re,base64,os
import xbmc,xbmcgui,shutil


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

exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MjAgZSAoKTojYToxCgk3ID05ICNhOjIKCTI2ID1bImQiLCIxMy0yMiIsIjEzLWYiLCIyMyIsIjEwIiwiYiIsIjFjLTI1IiwiMTUiLCIxOS4xMyJdI2E6MwoJOCA9WyIwOi8vNS8yOC80LjYuZCIsIjA6Ly81LzI4LzQuNi4xMy0yMiIsIjA6Ly81LzI4LzQuNi4xMy1mIiwiMDovLzUvMjgvNC42LjIzIiwiMDovLzUvMjgvNC42LjExIiwiMDovLzUvMjgvNC42LmIiLCIwOi8vNS8yOC80LjYuMWUiLCIwOi8vNS8yOC9jLmQiLCIwOi8vNS8yOC9jLjE4LjEzIl0jYToxMgoJMjcgPVtdI2E6MTQKCTFmIDI5IDI0IDFkICg3ICk6I2E6MTYKCQkyNyAuMWEgKDIxICgyNiBbMjkgXSw4IFsyOSBdKSkjYToxNwoJMWIgMjc=")))(lambda a,b:b[int("0x"+a.group(1),16)],"special|1|2|3|plugin|home|video|OO00000000O00OO0O|O0O0O0OO000000O0O|9|line|SportsDevil|repository|NLVIEW|setupXvbmcEntries|viewer2|SportCenterHD|sportcenterhd|12|nl|14|NLviewRepo|16|17|tvaddons|TVaddons|append|return|Troma|range|troma|for|def|cacheEntry|viewer|nlv3|in|copypaste|O0OOO0OO0O0O0OOOO|O0O0O0O0000O000OO|addons|O0OOO00OO000O0000".split("|")))


#######################################################################
#						CRAPCLEANER
#######################################################################

exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("M2UgMjIgKCk6IzNkOjEKCWMgPTE0ICgpIzNkOjE2CgkxYSBiIDFkIGMgOiMzZDoxOAoJCTNhID1lIC41NyAoYiAuZCApIzNkOjE5CgkJNGIgMTAgLmQgLjExICgzYSApPT00YyA6IzNkOjIwCgkJCTFhIDIgLDVhICw3IDFkIDEwIC4yYSAoM2EgKTojM2Q6MjEKCQkJCTQgPTAgIzNkOjI0CgkJCQk0ICs9MzcgKDcgKSMzZDoyNQoJCQkJNGIgNCA+MCA6IzNkOjI2CgkJCQkJMWEgNSAxZCA3IDojM2Q6MjcKCQkJCQkJMWIgOiMzZDoyOAoJCQkJCQkJMTAgLjRkICgxMCAuZCAuMTUgKDIgLDUgKSkjM2Q6MjkKCQkJCQkJZiA1OCA6IzNkOjMwCgkJCQkJCQkxMCAuM2YgKDEwIC5kIC4xNSAoMiAsNSApKSMzZDozMQoJCQkJCTFhIDggMWQgNWEgOiMzZDozMgoJCQkJCQkxYiA6IzNkOjMzCgkJCQkJCQkxMyAuMTIgKDEwIC5kIC4xNSAoMiAsOCApLDkgPTRjICkjM2Q6MzQKCQkJCQkJZiA1OCA6IzNkOjM1CgkJCQkJCQkxMCAuNGYgKDEwIC5kIC4xNSAoMiAsOCApKSMzZDozNgoJCQkJNTAgOiMzZDozOAoJCQkJCTRiIDEwIC5kIC4xMSAoM2EgKTojM2Q6NDIKCQkJCQkJMWIgOiMzZDo0MwoJCQkJCQkJMTMgLjEyICgzYSAsOSA9NGMgKSMzZDo0NgoJCQkJCQkJZSAuMyAoIjYiKSMzZDo0NwoJCQkJCQlmIDoxYyAjM2Q6NDgKCQkJCQk1MCA6IzNkOjQ5CgkJCQkJCWUgLjQwICgzYyAoM2EgKSkjM2Q6NTEKCQkJCQkJZSAuMyAoIjYiKSMzZDo1MgoJCQkJCQkxYyAjM2Q6NTMKCQk0YiAxMCAuZCAuMTEgKDNhICk6IzNkOjU1CgkJCTFiIDojM2Q6NTYKCQkJCTEzIC4xMiAoM2EgLDkgPTRjICkjM2Q6NTkKCQkJCWUgLjMgKCI2IikjM2Q6NDUKCQkJZiA6MWMgIzNkOjM5Cgk1NCAuM2IgKCItPSA0MSAyYiA9LSAiLCcyZSA0YSAyYyAxZCAyZiAxZicsJycsJygxZSAyYyAyZCA0ZSAyZCBhIDIzKScpIzNkOjQ0CgllIC4zICgiMTciKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|OO00O0O0O00OO0OO0|executebuiltin|O00OO0OO00O0O0000|O00O000OO0O0O0OO0|UpdateLocalAddons|OO0O000OOOOOOOO0O|O0O00O0000000OO00|ignore_errors|a|O0O0O000OO00O0OOO|OOO0000O000O00000|path|xbmc|except|os|exists|rmtree|shutil|setupXvbmcEntries|join|16|UpdateAddonRepos|18|19|for|try|pass|in|everything|condition|20|21|purgeOLD|whistle|24|25|26|27|28|29|walk|DONE|is|as|your|good|30|31|32|33|34|35|36|len|38|61|OO00O00OOOO0000OO|ok|str|line|def|remove|log|ALL|42|43|63|60|46|47|48|49|system|if|True|unlink|clean|rmdir|else|51|52|53|dialog|55|56|translatePath|OSError|59|OO0O0O00OOO00000O".split("|")))


#######################################################################
#						do some VooDoo
#######################################################################

purgeOLD()
