#!/usr/bin/python
""#line:5
import xbmc as O00000O0O0OOO00O0 ,xbmcaddon as O0O0O0OOO0O000O0O ,xbmcgui as O00O0OO00O00O00O0 ,xbmcplugin as OOO0OOO0OO0O000O0 #line:25
import os as O000O0O00OO0OOOOO ,shutil as O0O000000OO00OO00 ,time as O00O0O000O000OOO0 #line:26
import urllib2 as OO0O0OOO0O0OO0000 ,urllib as O0OO00O00OO0O000O #line:27
AddonID ='script.xvbmc.updatertools'#line:36
ADDON =O0O0O0OOO0O000O0O .Addon (id =AddonID )#line:37
dialog =O00O0OO00O00O00O0 .Dialog ()#line:39
MainTitle ="XvBMC Nederland"#line:40
piOC ='XvBMC overclock [COLOR white]RPi[/COLOR]'#line:41
SubTitle =" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] #OverClock#"#line:42
def ocMenu ():#line:45
    ""#line:46
    O0OOO0O0O0O00O00O =[]#line:49
    O0OOO0O0O0O00O00O .append (piOC +' [B]-[/B]None')#line:50
    O0OOO0O0O0O00O00O .append (piOC +' [B]-[/B]High')#line:51
    O0OOO0O0O0O00O00O .append (piOC +' [B]-[/B]Turbo')#line:52
    O0OOO0O0O0O00O00O .append (piOC +' [B]-[/B]Max')#line:53
    O0OOO0O0O0O00O00O .append ("[B][COLOR white]Exit[/COLOR][/B]")#line:54
    O0OO0OO000OOO00OO =O00O0OO00O00O00O0 .Dialog ().select (MainTitle +SubTitle ,O0OOO0O0O0O00O00O )#line:58
    if O0OOO0O0O0O00O00O [O0OO0OO000OOO00OO ]==piOC +' [B]-[/B]None':#line:62
       Config0 ()#line:63
    elif O0OOO0O0O0O00O00O [O0OO0OO000OOO00OO ]==piOC +' [B]-[/B]High':#line:66
         Config1 ()#line:67
    elif O0OOO0O0O0O00O00O [O0OO0OO000OOO00OO ]==piOC +' [B]-[/B]Turbo':#line:70
         Config2 ()#line:71
    elif O0OOO0O0O0O00O00O [O0OO0OO000OOO00OO ]==piOC +' [B]-[/B]Max':#line:74
         Config3 ()#line:75
class Config0Class (O00O0OO00O00O00O0 .Window ):#line:78
  def __init__ (self ):#line:79
    if dialog .yesno (MainTitle ,'default-clock Raspberry RPi?'):#line:80
       O0O000OO0000000O0 ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/oc/config0.sh"#line:81
       O000O0O00OO0OOOOO .system (O0O000OO0000000O0 )#line:82
       dialog .ok (MainTitle ,'XvBMC Pi NOT overclocked','','Press OK to reboot...')#line:83
       O00000O0O0OOO00O0 .sleep (1000 )#line:84
       O00000O0O0OOO00O0 .executebuiltin ("Reboot")#line:85
class Config1Class (O00O0OO00O00O00O0 .Window ):#line:87
  def __init__ (self ):#line:88
    if dialog .yesno (MainTitle ,'High-overclock Raspberry Pi?'):#line:89
       O0000O0O0000O000O ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/oc/config1.sh"#line:90
       O000O0O00OO0OOOOO .system (O0000O0O0000O000O )#line:91
       dialog .ok (MainTitle ,'XvBMC High-overclocked Pi','','Press OK to reboot...')#line:92
       O00000O0O0OOO00O0 .sleep (1000 )#line:93
       O00000O0O0OOO00O0 .executebuiltin ("Reboot")#line:94
class Config2Class (O00O0OO00O00O00O0 .Window ):#line:96
  def __init__ (self ):#line:97
    if dialog .yesno (MainTitle ,'Turbo-overclock Raspberry Pi?'):#line:98
       OOOOO0000O00OOOO0 ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/oc/config2.sh"#line:99
       O000O0O00OO0OOOOO .system (OOOOO0000O00OOOO0 )#line:100
       dialog .ok (MainTitle ,'XvBMC Turbo-overclocked Pi','','Press OK to reboot...')#line:101
       O00000O0O0OOO00O0 .sleep (1000 )#line:102
       O00000O0O0OOO00O0 .executebuiltin ("Reboot")#line:103
class Config3Class (O00O0OO00O00O00O0 .Window ):#line:105
  def __init__ (self ):#line:106
    if dialog .yesno (MainTitle ,'Max-overclock Raspberry Pi?'):#line:107
       OO000OOOO00O000O0 ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/oc/config3.sh"#line:108
       O000O0O00OO0OOOOO .system (OO000OOOO00O000O0 )#line:109
       dialog .ok (MainTitle ,'XvBMC x265-overclock Pi','','Press OK to reboot...')#line:110
       O00000O0O0OOO00O0 .sleep (1000 )#line:111
       O00000O0O0OOO00O0 .executebuiltin ("Reboot")#line:112
def Config0 ():#line:115
    OO000O00O0O0000OO =Config0Class ()#line:116
    del OO000O00O0O0000OO #line:117
def Config1 ():#line:119
    OO000OO0OO0OOO0OO =Config1Class ()#line:120
    del OO000OO0OO0OOO0OO #line:121
def Config2 ():#line:123
    OO0OOOOO00000000O =Config2Class ()#line:124
    del OO0OOOOO00000000O #line:125
def Config3 ():#line:127
    O0000OOO0OOOO0000 =Config3Class ()#line:128
    del O0000OOO0OOOO0000 #line:129
"""
    IF you copy/paste XvBMC's 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
