#!/usr/bin/python
""#line:6
import xbmc as OOOOO00OOO00OO00O ,xbmcaddon as O0OO000000OOOO00O ,xbmcgui as O000OOOO0O000OOOO ,xbmcplugin as O00O0O0000O0OOO0O #line:25
import os as O00O000O0OOO000OO ,shutil as OO00000000O000000 ,time as OO0OO0OO0OO00OO00 #line:26
import urllib2 as O0O000O0000O0O0OO ,urllib as O0000OOOO00O000O0 #line:27
import downloader as O0OO0OO0O0O0O0OO0 #line:28
from common import platform as OO0O00O0000OO0O0O ,subtitleNope as OOO0OO0OO0O0OOOO0 ,nonlinux as O000O00000O0OOOOO ,nonelecNL as OO0O0O000O00OOOOO #line:30
from common import log as O00OO0OO00OOO000O #line:31
AddonID ='script.xvbmc.updatertools'#line:34
ADDON =O0OO000000OOOO00O .Addon (id =AddonID )#line:35
dialog =O000OOOO0O000OOOO .Dialog ()#line:37
MainTitle ="XvBMC Nederland"#line:38
reset =' [COLOR orange]*reset*[/COLOR]'#line:39
New =' [COLOR lime][B]*[/B]NEW[B]*[/B][/COLOR]'#line:40
OLD =' [COLOR red][B]*[/B]OLD[B]*[/B][/COLOR]'#line:41
piOS =' [COLOR red][B]*[/B]RPi[B]*[/B][/COLOR]'#line:42
SubTitle =" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] #DEV#"#line:43
def devMenu ():#line:46
    ""#line:47
    OOO000O0O0OO0OOOO =[]#line:50
    OOO000O0O0OO0OOOO .append ('XvBMC #DEV# [B]-[/B] [COLOR white]Pi[/COLOR] Firmware [B]-[/B] Cutting Edge'+New )#line:51
    OOO000O0O0OO0OOOO .append ('XvBMC #DEV# [B]-[/B] [COLOR white]Pi[/COLOR] Firmware [B]-[/B] XvBMC Fallback'+reset )#line:52
    OOO000O0O0OO0OOOO .append ('XvBMC #DEV# [B]-[/B] [COLOR white]Libre[/COLOR]ELEC_arm-8.0.2'+piOS )#line:53
    OOO000O0O0OO0OOOO .append ('XvBMC #DEV# [B]-[/B] [COLOR white]Open[/COLOR]ELEC_arm-8.0.4'+piOS )#line:54
    OOO000O0O0OO0OOOO .append ('[B][COLOR white]Exit[/COLOR][/B]')#line:55
    OOO0000OOOOOOOO00 =O000OOOO0O000OOOO .Dialog ().select (MainTitle +SubTitle ,OOO000O0O0OO0OOOO )#line:59
    if OOO000O0O0OO0OOOO [OOO0000OOOOOOOO00 ]=='XvBMC #DEV# [B]-[/B] [COLOR white]Pi[/COLOR] Firmware [B]-[/B] Cutting Edge'+New :#line:63
        FirmwareRecent ()#line:64
    elif OOO000O0O0OO0OOOO [OOO0000OOOOOOOO00 ]=='XvBMC #DEV# [B]-[/B] [COLOR white]Pi[/COLOR] Firmware [B]-[/B] XvBMC Fallback'+reset :#line:67
        FirmwareXvbmc ()#line:68
    elif OOO000O0O0OO0OOOO [OOO0000OOOOOOOO00 ]=='XvBMC #DEV# [B]-[/B] [COLOR white]Libre[/COLOR]ELEC_arm-8.0.2'+piOS :#line:71
        SystemOS ()#line:72
    elif OOO000O0O0OO0OOOO [OOO0000OOOOOOOO00 ]=='XvBMC #DEV# [B]-[/B] [COLOR white]Open[/COLOR]ELEC_arm-8.0.4'+piOS :#line:75
        OpenElecTV ()#line:76
class FirmwareRecentClass (O000OOOO0O000OOOO .Window ):#line:79
  def __init__ (self ):#line:80
    OOO0OOO00O000OOO0 =OO0O00O0000OO0O0O ()#line:81
    O00OO0OO00OOO000O ("XvBMC_Platform: "+str (OOO0OOO00O000OOO0 ))#line:82
    if not OOO0OOO00O000OOO0 =='linux':#line:83
       dialog .ok (MainTitle +SubTitle ,OOO0OO0OO0O0OOOO0 ,O000O00000O0OOOOO ,OO0O0O000O00OOOOO )#line:84
       O00OO0OO00OOO000O ("none Linux OS ie. Open-/LibreELEC")#line:85
    else :#line:86
        O00OO0OO00OOO000O ("linux os")#line:87
        if dialog .yesno ("XvBMC-NL Raspberry latest firmware",'Update [COLOR white]most recent[/COLOR] PI2+3 firmware?'):#line:88
           OOOO0O0000OOOOOO0 ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/dev/firmwarerecent.sh"#line:89
           O00O000O0OOO000OO .system (OOOO0O0000OOOOOO0 )#line:90
           dialog .ok (MainTitle ,'XvBMC [COLOR white]most recent[/COLOR] firmware flashed','','Press OK to reboot...')#line:91
           OO0OO0OO0OO00OO00 .sleep (0.5 )#line:92
           OOOOO00OOO00OO00O .executebuiltin ("Reboot")#line:93
class FirmwareXvbmcClass (O000OOOO0O000OOOO .Window ):#line:95
  def __init__ (self ):#line:96
    OO00O0OOO0O00000O =OO0O00O0000OO0O0O ()#line:97
    O00OO0OO00OOO000O ("XvBMC_Platform: "+str (OO00O0OOO0O00000O ))#line:98
    if not OO00O0OOO0O00000O =='linux':#line:99
       dialog .ok (MainTitle +SubTitle ,OOO0OO0OO0O0OOOO0 ,O000O00000O0OOOOO ,OO0O0O000O00OOOOO )#line:100
       O00OO0OO00OOO000O ("none Linux OS ie. Open-/LibreELEC")#line:101
    else :#line:102
        O00OO0OO00OOO000O ("linux os")#line:103
        if dialog .yesno ("XvBMC-NL Raspberry firmware reset",'RE-Flash XvBMC [COLOR white]\"default\"[/COLOR] firmware?'):#line:104
           OO0O00OOO0OOOO00O ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/dev/firmwarexvbmc.sh"#line:105
           O00O000O0OOO000OO .system (OO0O00OOO0OOOO00O )#line:106
           dialog .ok (MainTitle ,'XvBMC [COLOR white]\"default\"[/COLOR] firmware re-flashed','','Press OK to reboot...')#line:107
           OO0OO0OO0OO00OO00 .sleep (0.5 )#line:108
           OOOOO00OOO00OO00O .executebuiltin ("Reboot")#line:109
class SystemOSClass (O000OOOO0O000OOOO .Window ):#line:112
  def __init__ (self ):#line:113
    O0O0O00000OO0OOO0 =OO0O00O0000OO0O0O ()#line:114
    O00OO0OO00OOO000O ("XvBMC_Platform: "+str (O0O0O00000OO0OOO0 ))#line:115
    if not O0O0O00000OO0OOO0 =='linux':#line:116
       dialog .ok (MainTitle +SubTitle ,OOO0OO0OO0O0OOOO0 ,O000O00000O0OOOOO ,OO0O0O000O00OOOOO )#line:117
       O00OO0OO00OOO000O ("none Linux OS ie. Open-/LibreELEC")#line:118
    else :#line:119
        O00OO0OO00OOO000O ("linux os")#line:120
        if dialog .yesno ("XvBMC-NL LibreELEC \'[COLOR white]OS[/COLOR]-update\'",'Preparing LE[COLOR white]8.0.2[/COLOR] and reboot when done...'):#line:121
           OO00OOOOOO0O00OO0 ='http://releases.libreelec.tv/LibreELEC-RPi2.arm-8.0.2.tar'#line:122
           O00OOO0O000000O0O =OOOOO00OOO00OO00O .translatePath (O00O000O0OOO000OO .path .join ('/storage/.update/',''))#line:123
           O0OO00OOOO00O00OO =O000OOOO0O000OOOO .DialogProgress ()#line:124
           O0OO00OOOO00O00OO .create ("XvBMC Nederland","XvBMC-DEV: doing some VoOdOo...",'','Please Wait')#line:125
           O000OOOO0OO00O0OO =O00O000O0OOO000OO .path .join (O00OOO0O000000O0O ,'libreelec802.tar')#line:126
           try :#line:127
               O00O000O0OOO000OO .remove (O000OOOO0OO00O0OO )#line:128
           except :#line:129
               pass #line:130
           O0OO0OO0O0O0O0OO0 .download (OO00OOOOOO0O00OO0 ,O000OOOO0OO00O0OO ,O0OO00OOOO00O00OO )#line:131
           OO0OO0OO0OO00OO00 .sleep (3 )#line:133
           dialog .ok (MainTitle ,'LibreELEC SYSTEM update finished!','','Press OK to reboot...')#line:138
           OOOOO00OOO00OO00O .sleep (1000 )#line:139
           OOOOO00OOO00OO00O .executebuiltin ("Reboot")#line:140
class OpenElecTVClass (O000OOOO0O000OOOO .Window ):#line:142
  def __init__ (self ):#line:143
    O00000OOOOOOO000O =OO0O00O0000OO0O0O ()#line:144
    O00OO0OO00OOO000O ("XvBMC_Platform: "+str (O00000OOOOOOO000O ))#line:145
    if not O00000OOOOOOO000O =='linux':#line:146
       dialog .ok (MainTitle +SubTitle ,OOO0OO0OO0O0OOOO0 ,O000O00000O0OOOOO ,OO0O0O000O00OOOOO )#line:147
       O00OO0OO00OOO000O ("none Linux OS ie. Open-/LibreELEC")#line:148
    else :#line:149
        O00OO0OO00OOO000O ("linux os")#line:150
        if dialog .yesno ("XvBMC-NL LibreELEC \'[COLOR white]OS[/COLOR]-update\'",'Preparing OE[COLOR white]8.0.4[/COLOR] and reboot when done...'):#line:151
           OOOOOOO00OO000000 ='http://openelec.mirror.triple-it.nl/OpenELEC-RPi2.arm-8.0.4.tar'#line:152
           O000O00OOOO0000OO =OOOOO00OOO00OO00O .translatePath (O00O000O0OOO000OO .path .join ('/storage/.update/',''))#line:153
           OO00O0OOO000O0000 =O000OOOO0O000OOOO .DialogProgress ()#line:154
           OO00O0OOO000O0000 .create ("XvBMC Nederland","XvBMC-DEV: doing some VoOdOo...",'','Please Wait')#line:155
           O000000O000O0O0OO =O00O000O0OOO000OO .path .join (O000O00OOOO0000OO ,'openelec804.tar')#line:156
           try :#line:157
               O00O000O0OOO000OO .remove (O000000O000O0O0OO )#line:158
           except :#line:159
               pass #line:160
           O0OO0OO0O0O0O0OO0 .download (OOOOOOO00OO000000 ,O000000O000O0O0OO ,OO00O0OOO000O0000 )#line:161
           OO0OO0OO0OO00OO00 .sleep (3 )#line:163
           dialog .ok (MainTitle ,'OpenELEC SYSTEM update finished!','','Press OK to reboot...')#line:168
           OOOOO00OOO00OO00O .sleep (1000 )#line:169
           OOOOO00OOO00OO00O .executebuiltin ("Reboot")#line:170
def FirmwareRecent ():#line:173
    OOO0O000O0OO0OOO0 =FirmwareRecentClass ()#line:174
    del OOO0O000O0OO0OOO0 #line:175
def FirmwareXvbmc ():#line:177
    O0O0O00O0O0OO00O0 =FirmwareXvbmcClass ()#line:178
    del O0O0O00O0O0OO00O0 #line:179
def SystemOS ():#line:181
    OOO0O00000O0OO0O0 =SystemOSClass ()#line:182
    del OOO0O00000O0OO0O0 #line:183
def OpenElecTV ():#line:185
    OO00O0OO0OOOOO0O0 =OpenElecTVClass ()#line:186
    del OO00O0OO0OOOOO0O0 #line:187
"""
    IF you copy/paste XvBMC's 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
