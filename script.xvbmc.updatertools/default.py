#!/usr/bin/python
""#line:6
import re as OOOO0OOO00O0O00O0 ,base64 as O0O0O00OO0O00O000 ,urllib as O0OO000OOOO0OO0OO ,urllib2 as OOOO0OOO0O000O00O ,sys as O0OOOOO0O000OO00O ,xbmcvfs as O0O00O000OO0O0O0O #line:25
import xbmc as OO0O0000OO00O0O00 ,xbmcaddon as O00OO0OOOOO0OO0OO ,xbmcgui as OO0O0OO000O0OO00O ,xbmcplugin as OOO00OOOO000OOOOO #line:26
import os as O000OOOO0OO00O0OO ,shutil as OOOOOOOO0O0O00O0O ,time as O0000OOOO00O00O0O #line:27
import sqlite3 as O0O0OO00O00OOOOOO #line:28
import utils as O0O0O000O0O00O000 #line:29
from resources .lib import addon_able as O0O0OOO0O0O0O0000 #line:32
from resources .lib import downloader as O0O0OO0O0O000OOOO ,extract as OOO000OOOO0O000O0 #line:33
from resources .lib import common as OOO000OO00OO000OO #line:34
from resources .lib .common import platform as OOO00OOO0O00O000O ,subtitleNope as O0000OOO0O0OO000O ,nonlinux as OO0OOOO00OOO000O0 ,nonelecNL as OO00OOO0O00O000O0 #line:35
from resources .lib .common import base as O0O0OO0O00OOOO000 ,basewiz as O00OO0OO0O00O0O0O ,currentbldtxt as OO0OO0O00O00OOO0O ,currentsptxt as OOOO0O00OO0O00O0O ,currentbldtxtwiz as O00OO0OO000O00O00 ,currentsptxtwiz as O00O00O0OOOOO00OO ,currentsptxtrpi as OOO00OOOOOOOO0O0O #line:36
from resources .lib import flush as O000OOOOOO0000O0O #line:38
from resources .lib import huisvrouw as OO00OOOO00OOO0000 #line:39
from resources .lib import purge as O0O0OOOO00O000O0O #line:40
from resources .lib import rpioc as O00O00O0OOO0OOO0O #line:41
from resources .lib import rpidev as OOOO00OO000000O0O #line:42
ADDON =O0O0O000O0O00O000 .ADDON #line:44
ADDON_ID =O00OO0OOOOO0OO0OO .Addon ().getAddonInfo ('id')#line:46
AddonID ='script.xvbmc.updatertools'#line:47
AddonTitle ='XvBMC Nederland'#line:48
addonPath =O000OOOO0OO00O0OO .path .join (O000OOOO0OO00O0OO .path .join (OO0O0000OO00O0O00 .translatePath ('special://home'),'addons'),'script.xvbmc.updatertools')#line:49
ART =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/addons/'+AddonID +'/resources/media/'))#line:50
artwork =O0O0O00OO0O00O000 .b64decode ('c2tpbi5hZW9uLm5veC5zcGlu')#line:51
FANART =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/addons/'+AddonID ,'fanart.jpg'))#line:52
FANARTsub =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/addons/'+AddonID +'/resources/media/','art.jpg'))#line:53
ICON =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/addons/'+AddonID ,'icon.png'))#line:54
MainTitle ="XvBMC Nederland"#line:55
mediaPath =O000OOOO0OO00O0OO .path .join (addonPath ,'resources/media')#line:56
U =ADDON .getSetting ('User')#line:57
USER_AGENT ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'#line:58
About ='[COLOR dimgray][B]X[/B]v[B]BMC[/B] disclaimer & usage policy[/COLOR]'#line:60
Terug ='[COLOR dimgray]<<<back[/COLOR]'#line:61
dialog =OO0O0OO000O0OO00O .Dialog ()#line:63
dp =OO0O0OO000O0OO00O .DialogProgress ()#line:64
BASEURL ="https://bit.ly/XvBMC-Pi"#line:65
buildinfotxt ='[COLOR gray][B] - [/B]your wizard build: [I]unknown[/I] [/COLOR]'#line:66
serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: [I]unknown[/I] [/COLOR]'#line:67
xbmcver =OO0O0000OO00O0O00 .getInfoLabel ("System.BuildVersion")[:4 ]#line:68
EXCLUDES =[ADDON_ID ,'plugin.program.xvbmcinstaller.nl','repository.xvbmc']#line:70
HOME =OO0O0000OO00O0O00 .translatePath ('special://home/')#line:71
skin =OO0O0000OO00O0O00 .getSkinDir ()#line:72
USERDATA =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/userdata',''))#line:73
USERADDONDATA =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/userdata/addon_data',''))#line:74
def resolver_settings ():#line:78
    import urlresolver as O00000OO000OOOOOO #line:79
    O00000OO000OOOOOO .display_settings ()#line:80
def mainMenu ():#line:83
    OOOO0O00OOO000O0O ,O0O00OOO0O0O00O0O =O0O0O000O0O00O000 .checkUpdate ()#line:85
    if OOOO0O00OOO000O0O =="update":#line:87
       OO0OOO0O0O00OOO00 ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(O0O00OOO0O0O00O0O )+'[COLOR orange] (fork)[/COLOR]'#line:88
       O0OOO0OOO0OOOO0OO =O0O0O00OO0O00O000 .b64decode (O0O0OO0O00OOOO000 )+'update/sp/servicepack.zip'#line:89
       addDir ('%s'%OO0OOO0O0O00OOO00 ,O0OOO0OOO0OOOO0OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:91
    elif OOOO0O00OOO000O0O =="wizupdate":#line:92
       OO0OOO0O0O00OOO00 ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(O0O00OOO0O0O00O0O )+'[COLOR orange] (wizard)[/COLOR]'#line:93
       O0OOO0OOO0OOOO0OO =O0O0O00OO0O00O000 .b64decode (O00OO0OO0O00O0O0O )+'wizardsp.zip'#line:94
       addDir ('%s'%OO0OOO0O0O00OOO00 ,O0OOO0OOO0OOOO0OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:96
    elif OOOO0O00OOO000O0O =="rpiupdate":#line:97
       OO0OOO0O0O00OOO00 ="[COLOR orange]XvBMC RPi update available[B]: %s[/B][/COLOR]"%(O0O00OOO0O0O00O0O )+'[COLOR orange] (forced)[/COLOR]'#line:98
       O0OO0O000O0OO0OOO =O0O0O00OO0O00O000 .b64decode (O0O0OO0O00OOOO000 )+'update/sp/'#line:99
       addDir ('%s'%OO0OOO0O0O00OOO00 ,O0OO0O000O0OO0OOO ,69 ,ART +'xvbmc.png',FANART ,'')#line:101
    elif OOOO0O00OOO000O0O =="notinstalled":#line:105
       if OO0O0000OO00O0O00 .getCondVisibility ('System.HasAddon(%s)'%(artwork )):#line:106
          if O000OOOO0OO00O0OO .path .isfile (OOO000OO00OO000OO .bldversietxt ):#line:107
             OO0OOO0O0O00OOO00 ="[COLOR orange]Sorry (portable) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:108
             O0OOO0OOO0OOOO0OO =O0O0O00OO0O00O000 .b64decode (O0O0OO0O00OOOO000 )+'update/sp/servicepack.zip'#line:109
             addDir ('%s'%OO0OOO0O0O00OOO00 ,O0OOO0OOO0OOOO0OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:111
          elif O000OOOO0OO00O0OO .path .isfile (OOO000OO00OO000OO .bldversietxtwiz ):#line:112
               OO0OOO0O0O00OOO00 ="[COLOR orange]Sorry (wizard) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:113
               O0OOO0OOO0OOOO0OO =O0O0O00OO0O00O000 .b64decode (O00OO0OO0O00O0O0O )+'wizardsp.zip'#line:114
               addDir ('%s'%OO0OOO0O0O00OOO00 ,O0OOO0OOO0OOOO0OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:116
          elif OO0O0000OO00O0O00 .getCondVisibility ('System.HasAddon("service.openelec.settings")')+OO0O0000OO00O0O00 .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:118
               OO0OOO0O0O00OOO00 ="[COLOR orange]unknown [B]RPi[/B] version; force update[B]?[/B][/COLOR] [COLOR lime] (continue?)[/COLOR]"#line:119
               O0OO0O000O0OO0OOO =O0O0O00OO0O00O000 .b64decode (O0O0OO0O00OOOO000 )+'update/sp/'#line:120
               addDir ('%s'%OO0OOO0O0O00OOO00 ,O0OO0O000O0OO0OOO ,69 ,ART +'xvbmc.png',FANART ,'')#line:122
          else :#line:123
               OO0OOO0O0O00OOO00 ="[COLOR orange]unknown build status; force update?[/COLOR] [COLOR red][B](continue at your own risk)[/B][/COLOR]"#line:124
               O000OOO0OOOO0OO0O =O0O0O00OO0O00O000 .b64decode (O0O0OO0O00OOOO000 )+'update/sp/servicepack.zip'#line:125
               addDir ('%s'%OO0OOO0O0O00OOO00 ,O000OOO0OOOO0OO0O ,1 ,ART +'xvbmc.png',FANART ,'')#line:127
       else :#line:128
          OO0OOO0O0O00OOO00 ="[COLOR orange]Sorry, [B]unknown[/B] build/servicepack/update status [B] :[/B]\'-([/COLOR]"#line:129
          addItem ('%s'%OO0OOO0O0O00OOO00 ,BASEURL ,4 ,ART +'xvbmc.png')#line:130
    elif OOOO0O00OOO000O0O =="noupdaterpi":#line:131
         if OO0O0000OO00O0O00 .getCondVisibility ('System.HasAddon("service.openelec.settings")')+OO0O0000OO00O0O00 .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:133
            OO0OOO0O0O00OOO00 ="[COLOR orange]You have the [B]latest[/B] [COLOR red]XvBMC[/COLOR] [COLOR lime][B]RPi[/B][/COLOR] forced updates [B] 3:[/B]-)[/COLOR]"#line:134
            addItem ('%s'%OO0OOO0O0O00OOO00 ,BASEURL ,4 ,ART +'xvbmc.png')#line:135
         else :#line:136
            OO0OOO0O0O00OOO00 ="[COLOR orange]You [B]somehow[/B] have the latest [COLOR lime]XvBMC[/COLOR] [COLOR red][B]RPi[/B][/COLOR] forced updates [B]???[/B][/COLOR]"#line:137
            addItem ('%s'%OO0OOO0O0O00OOO00 ,BASEURL ,4 ,ART +'xvbmc.png')#line:138
    else :#line:139
       OO0OOO0O0O00OOO00 ="[COLOR orange]You have the [B]latest[/B] XvBMC updates [B] :[/B]-)[/COLOR]"#line:140
       addItem ('%s'%OO0OOO0O0O00OOO00 ,BASEURL ,4 ,ART +'xvbmc.png')#line:141
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:143
    addDir ('[COLOR red]XvBMC Tools[/COLOR]',BASEURL ,10 ,ART +'tools.png',O000OOOO0OO00O0OO .path .join (mediaPath ,"gereedschap.jpg"),'')#line:144
    addDir ('[COLOR white]XvBMC Maintenance[/COLOR]',BASEURL ,20 ,ART +'maint.png',O000OOOO0OO00O0OO .path .join (mediaPath ,"onderhoud.jpg"),'')#line:145
    addDir ('[COLOR dodgerblue]XvBMC About[/COLOR]',BASEURL ,2 ,ART +'wtf.png',O000OOOO0OO00O0OO .path .join (mediaPath ,"over.jpg"),'')#line:146
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:147
    addItem ('[COLOR gray]system information (kodi %s):[/COLOR]'%xbmcver ,BASEURL ,16 ,ART +'xvbmc.png')#line:148
    global serviceinfotxt #line:149
    O0O0OO00OO0O0O0OO ,O000O0OOOO00OO000 =OOO000OO00OO000OO .checkSPversie ()#line:150
    if O0O0OO00OO0O0O0OO =="uwspversietxt":#line:151
       OOOOOO00O0O00000O =O0O0O000O0O00O000 .getHtml2 (OOOO0O00OO0O00O0O )#line:152
       serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(O000O0OOOO00OO000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OOOOOO00O0O00000O )#line:153
    elif O0O0OO00OO0O0O0OO =="uwspversietxtwiz":#line:154
         OOOOOO00O0O00000O =O0O0O000O0O00O000 .getHtml2 (O00O00O0OOOOO00OO )#line:155
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(O000O0OOOO00OO000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OOOOOO00O0O00000O )#line:156
    elif O0O0OO00OO0O0O0OO =="uwspversietxtrpi":#line:157
         OOOOOO00O0O00000O =O0O0O000O0O00O000 .getHtml2 (OOO00OOOOOOOO0O0O )#line:158
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(O000O0OOOO00OO000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OOOOOO00O0O00000O )#line:159
    addItem ('%s'%serviceinfotxt ,BASEURL ,'',O000OOOO0OO00O0OO .path .join (mediaPath ,"wtf.png"))#line:160
    global buildinfotxt #line:161
    O0OOO0OOO00OO0000 ,OOOO00OOO0O0OO000 =OOO000OO00OO000OO .checkXvbmcversie ()#line:162
    if O0OOO0OOO00OO0000 =="bldversietxt":#line:163
       O0O00OO0OOOO0OO0O =O0O0O000O0O00O000 .getHtml2 (OO0OO0O00O00OOO0O )#line:164
       buildinfotxt ='[COLOR gray][B] - [/B]your system build: %s [/COLOR]'%(OOOO00OOO0O0OO000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0O00OO0OOOO0OO0O )#line:165
    elif O0OOO0OOO00OO0000 =="bldversietxtwiz":#line:166
         O0O00OO0OOOO0OO0O =O0O0O000O0O00O000 .getHtml2 (O00OO0OO000O00O00 )#line:167
         buildinfotxt ='[COLOR gray][B] - [/B]your wizard build: %s [/COLOR]'%(OOOO00OOO0O0OO000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0O00OO0OOOO0OO0O )#line:168
    addItem ('%s'%buildinfotxt ,BASEURL ,'',O000OOOO0OO00O0OO .path .join (mediaPath ,"wtf.png"))#line:169
    if OO0O0000OO00O0O00 .getCondVisibility ('System.HasAddon("service.openelec.settings")')+OO0O0000OO00O0O00 .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:171
       addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:172
       addDir ('[COLOR orange]XvBMC Raspberry Pi [B] -[/B] Tools, DEV. & Maintenance[/COLOR]',BASEURL ,30 ,ART +'RPi.png',FANARTsub ,'')#line:173
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:175
    addItem (Terug ,BASEURL ,3 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:176
    OOO000OO00OO000OO .setView ('movies','EPiC')#line:177
def XvBMCmaint ():#line:179
    addItem ('[B]B[/B]uild [COLOR red]purge[/COLOR] [COLOR dimgray](build [B]c[/B]rap[B]c[/B]leaner & fix evil addons/repos)[/COLOR]',BASEURL ,21 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:180
    addItem ('[B]C[/B]lear cache',BASEURL ,22 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:181
    addItem ('[B]D[/B]elete thumbnails',BASEURL ,23 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:182
    addItem ('[B]F[/B]lush add-ons [COLOR dimgray](salts HD/RD lite & Exodus \'cache+temp\' files)[/COLOR]',BASEURL ,24 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:183
    addItem ('[B]F[/B]ull \"auto\" clean [COLOR dimgray](cache, crashlogs, packages & thumbnails)[/COLOR]',BASEURL ,25 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:184
    addItem ('[B]P[/B]urge packages',BASEURL ,26 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:185
    addItem ('[B]R[/B]efresh addons[COLOR white]+[/COLOR]repos',BASEURL ,27 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:186
    if int (O0O0O000O0O00O000 .kodiver )<=16.7 :#line:187
       addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s remove addons.db',BASEURL ,28 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:188
    elif int (O0O0O000O0O00O000 .kodiver )>16.7 :#line:189
         addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s enable all add-ons [COLOR dimgray](Kodi 17+ Krypton)[/COLOR]',BASEURL ,29 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:190
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:192
    addItem (About ,BASEURL ,2 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"wtf.png"))#line:193
    addItem (Terug ,BASEURL ,3 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:194
    OOO000OO00OO000OO .setView ('movies','EPiC')#line:195
def XvBMCtools1 ():#line:197
    addItem ('[B]C[/B]onvert physical paths (\'home\') to \'special\'',BASEURL ,11 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:198
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]most[/COLOR] add-ons)[/COLOR]',BASEURL ,12 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:199
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]all[/COLOR] add-ons)[/COLOR]',BASEURL ,13 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:200
    addItem ('[B]E[/B]nable Kodi Live Streams [COLOR dimgray](17+ Krypton; [COLOR white]RTMP[/COLOR])[/COLOR]',BASEURL ,14 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:201
    addItem ('[B]F[/B]orce close Kodi  [COLOR dimgray](Kill Kodi)[/COLOR]',BASEURL ,15 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:202
    addItem ('[B]L[/B]og viewer [COLOR dimgray](show \'kodi.log\')[/COLOR]',BASEURL ,17 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:204
    addItem ('[B]U[/B]RLResolver -> settings',BASEURL ,18 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:205
    addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s Advancedsettings unlocker [COLOR dimgray](reset)[/COLOR]',BASEURL ,19 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:206
    addDir ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s [COLOR white][B]H[/B]idden [B]g[/B]ems[B] & [/B][B]M[/B]ore [B]t[/B]ools[/COLOR] [COLOR dimgray](TiP[B]!![/B])[/COLOR]',BASEURL ,40 ,ART +'xvbmc.png',O000OOOO0OO00O0OO .path .join (mediaPath ,"gereedschap.jpg"),'')#line:207
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:209
    addItem (About ,BASEURL ,2 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"wtf.png"))#line:210
    addItem (Terug ,BASEURL ,3 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:211
    OOO000OO00OO000OO .setView ('movies','EPiC')#line:212
def XvBMCrpi ():#line:214
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] extreme crapcleaner [COLOR dimgray]([B]no[/B] factory reset)[/COLOR]',BASEURL ,31 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"tools.png"))#line:215
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] overclock [COLOR dimgray](raspberry Pi ***only***)[/COLOR]',BASEURL ,32 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"overclock.png"))#line:216
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] #dev# corner [COLOR dimgray](firmware, OS, etc.)[/COLOR]',BASEURL ,33 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"firmware.png"))#line:217
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:219
    addItem (About ,BASEURL ,2 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"wtf.png"))#line:220
    addItem (Terug ,BASEURL ,3 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:221
    OOO000OO00OO000OO .setView ('movies','EPiC')#line:222
def XvBMCtools2 ():#line:224
    addItem ('[B]K[/B]odi Quick Reset [COLOR dimgray](\"rejuvenate\" XvBMC-NL build)[/COLOR]',BASEURL ,41 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:226
    addItem ('[B]K[/B]odi Factory Reset [COLOR dimgray](complete Kodi Krypton wipe)[/COLOR]',BASEURL ,42 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:227
    addItem ('[B]K[/B]odi Fresh Start [COLOR dimgray](remove older Kodi\'s)[/COLOR]',BASEURL ,43 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:228
    addItem ('[B]P[/B]ush Fixes [COLOR dimgray](for XvBMC builds)[/COLOR]',BASEURL ,44 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"maint.png"))#line:229
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:231
    addItem (About ,BASEURL ,2 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"wtf.png"))#line:232
    addItem (Terug ,BASEURL ,3 ,O000OOOO0OO00O0OO .path .join (mediaPath ,"xvbmc.png"))#line:233
    OOO000OO00OO000OO .setView ('movies','EPiC')#line:234
def wizard (name ,url ):#line:238
    O000O0OOO0OOO000O =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/addons','packages'))#line:239
    if not O000OOOO0OO00O0OO .path .exists (O000O0OOO0OOO000O ):#line:240
        O000OOOO0OO00O0OO .makedirs (O000O0OOO0OOO000O )#line:241
    OOO0OOOOO00O00OOO =O000OOOO0OO00O0OO .path .join (O000O0OOO0OOO000O ,'default.zip')#line:242
    try :#line:243
       O000OOOO0OO00O0OO .remove (OOO0OOOOO00O00OOO )#line:244
    except :#line:245
       pass #line:246
    O0O0OO0O0O000OOOO .download (url ,OOO0OOOOO00O00OOO )#line:247
    if O000OOOO0OO00O0OO .path .exists (OOO0OOOOO00O00OOO ):#line:249
        O00O00OO0O0OO00O0 =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://','home'))#line:250
        O0000OOOO00O00O0O .sleep (2 )#line:251
        dp .create (MainTitle ,'XvBMC-NL: pull update VoOdOo...','','Please Wait')#line:253
        dp .update (0 ,"","***Extract ZIP - Please Wait")#line:254
        OOO000OO00OO000OO .log ("==========================================================")#line:255
        OOO000OO00OO000OO .log (O00O00OO0O0OO00O0 )#line:256
        OOO000OO00OO000OO .log ("==========================================================")#line:257
        OOO000OOOO0O000O0 .all (OOO0OOOOO00O00OOO ,O00O00OO0O0OO00O0 ,dp )#line:258
        dp .close ()#line:259
        try :O000OOOO0OO00O0OO .remove (OOO0OOOOO00O00OOO )#line:260
        except :pass #line:261
    if int (O0O0O000O0O00O000 .kodiver )<=16.7 :#line:262
       dialog .ok (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  HINT  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:263
       OOO000OO00OO000OO .forceRefresh (melding =False )#line:264
    elif int (O0O0O000O0O00O000 .kodiver )>16.7 :#line:265
         O0O0O000O0O00O000 .enableAddons (melding =False )#line:266
         O0000OOOO00O00O0O .sleep (0.5 )#line:267
         OOO00O0O000OOOOO0 =OO0O0OO000O0OO00O .Dialog ().yesno (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  SUCCESS  !!![/B][/COLOR]','[B]IF[/B] add-ons do NOT work you probably should reboot.','(een REBOOT van uw systeem is VEELAL wenselijk)',yeslabel ='[COLOR lime]Reboot[/COLOR]',nolabel ='[COLOR red]Continue[/COLOR]')#line:268
         if OOO00O0O000OOOOO0 ==1 :#line:269
            O0000OOOO00O00O0O .sleep (1 )#line:270
            OOO000OO00OO000OO .killKodi ()#line:271
         elif OOO00O0O000OOOOO0 ==0 :#line:272
              if int (O0O0O000O0O00O000 .kodiver )>16.7 :#line:273
                 O0O0O000O0O00O000 .enableAddons (melding =False )#line:274
                 O0000OOOO00O00O0O .sleep (0.5 )#line:275
                 dialog .ok (MainTitle +" : [COLOR red]add-ons[/COLOR] [COLOR green][B]enabled[/B][/COLOR]",'[COLOR orange][B]!!!  TIP  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:276
                 OO0O0000OO00O0O00 .executebuiltin ('ReloadSkin()')#line:277
    OO0O0000OO00O0O00 .executebuiltin ("Container.Refresh")#line:278
    OO0O0000OO00O0O00 .sleep (5000 )#line:279
def fileexchange (url ):#line:285
    dp .create (MainTitle ,'XvBMC-NL: RPi update VoOdOo...','','Please Wait')#line:286
    if not O000OOOO0OO00O0OO .path .exists (USERDATA ):#line:287
        O000OOOO0OO00O0OO .makedirs (USERDATA )#line:288
    OO000OO00O0O0OO00 =O000OOOO0OO00O0OO .path .join (USERDATA ,'rpi-service.txt')#line:289
    dp .update (50 ,'','vOoDoO')#line:290
    try :#line:291
        O000OOOO0OO00O0OO .remove (OO000OO00O0O0OO00 )#line:292
    except :#line:293
        pass #line:294
    O0O0OO0O0O000OOOO .download (url +'rpi-service.txt',OO000OO00O0O0OO00 )#line:295
    dp .update (75 ,'','VoOdOo')#line:296
    O0000OOOO00O00O0O .sleep (1 )#line:297
    dp .close ()#line:298
    OO0O0000OO00O0O00 .executebuiltin ("Container.Refresh")#line:300
    OO0O0000OO00O0O00 .sleep (1000 )#line:301
def unlocker ():#line:304
    dialog .ok (MainTitle +" - unlocker",' ','unlock advancedsettings for this build','[COLOR dimgray](+reset \'advancedsettings.xml\' -use at your own risk)[/COLOR]')#line:306
    OOOOOOO0OO00O0OOO =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join ('special://home/userdata/'))#line:307
    OO0O0000O0OO00000 =O0O0O00OO0O00O000 .b64decode ('YWR2YW5jZWRzZXR0aW5ncy54bWw=')#line:308
    OOOOO0O0O0O0000O0 =True #line:309
    try :#line:310
        O000OOOO0OO00O0OO .unlink (OOOOOOO0OO00O0OOO +OO0O0000O0OO00000 )#line:311
    except :#line:312
        OOOOO0O0O0O0000O0 =False #line:313
    if OOOOO0O0O0O0000O0 :#line:315
        dialog .ok (MainTitle +" - [B]UNLOCKED[/B]",'[COLOR green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Herstart[/B] Kodi ter afronding \'unlocker\' (force close)','[B]Reboot[/B] Kodi to complete \'unlocker\' (force close)')#line:316
        O000OOOO0OO00O0OO ._exit (1 )#line:317
    else :#line:318
        dialog .ok (MainTitle +" - [B]OOOOOOPS[/B]",'[COLOR red][B]!!!  Failed  !!![/B][/COLOR]','[B]Nope![/B] helaas geen succes (niks te \'unlocken\')','[B]Nope![/B] close but no cigar  (nothing to \'unlock\')')#line:319
def XvbmcOc ():#line:322
    O00OOO00000OO00OO =OOO00OOO0O00O000O ()#line:323
    OOO000OO00OO000OO .log ("Platform: "+str (O00OOO00000OO00OO ))#line:324
    if not O00OOO00000OO00OO =='linux':#line:325
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] OverClock!",O0000OOO0O0OO000O ,OO0OOOO00OOO000O0 ,OO00OOO0O00O000O0 )#line:326
       OOO000OO00OO000OO .log ("none Linux OS ie. Open-/LibreELEC")#line:327
    else :#line:328
        OOO000OO00OO000OO .log ("linux os")#line:329
        O00O00O0OOO0OOO0O .ocMenu ()#line:330
def XvbmcDev ():#line:333
    OOOOO0O0O00000000 =OOO00OOO0O00O000O ()#line:334
    OOO000OO00OO000OO .log ("Platform: "+str (OOOOO0O0O00000000 ))#line:335
    if not OOOOO0O0O00000000 =='linux':#line:336
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] #dev#",O0000OOO0O0OO000O ,OO0OOOO00OOO000O0 ,OO00OOO0O00O000O0 )#line:337
       OOO000OO00OO000OO .log ("none Linux OS ie. Open-/LibreELEC")#line:338
    else :#line:339
        OOO000OO00OO000OO .log ("linux os")#line:340
        OOOO00OO000000O0O .devMenu ()#line:341
def disabled ():#line:344
    OOO000OO00OO000OO .okDialog ('[COLOR red][B]Sorry, disabled! [/B](for now)[/COLOR]','','[COLOR lime]goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')#line:345
def rejuvXvbmc ():#line:348
    O000OO0O0O00O0O00 =OOO000OO00OO000OO .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Wilt u uw XvBMC \'build\' volledig opschonen (wipe) en Kodi Krypton [B]leeg[/B] her-configureren?','[COLOR dimgray]Please confirm that you wish you wipe clean your current configuration and reconfigure Kodi.[/COLOR]')#line:349
    if O000OO0O0O00O0O00 :#line:350
        O0OOO00OO0O000O0O =O00OO0OOOOO0OO0OO .Addon (id =AddonID ).getAddonInfo ('path');O0OOO00OO0O000O0O =OO0O0000OO00O0O00 .translatePath (O0OOO00OO0O000O0O );#line:351
        OO0O0O0OOOO0O000O =O000OOOO0OO00O0OO .path .join (O0OOO00OO0O000O0O ,"..","..");OO0O0O0OOOO0O000O =O000OOOO0OO00O0OO .path .abspath (OO0O0O0OOOO0O000O );OOO000OO00OO000OO .log ("rejuvXvbmc.main_XvBMC: xbmcPath="+OO0O0O0OOOO0O000O );#line:352
        O0O0O0OO00O000O00 =('addons','Database','packages','userdata')#line:354
        OOOO0O00O000000OO =('metadata.album.universal','metadata.artists.universal','metadata.common.imdb.com','metadata.common.musicbrainz.org','metadata.common.theaudiodb.com','metadata.common.themoviedb.org','metadata.themoviedb.org','metadata.tvdb.com','plugin.program.super.favourites','plugin.program.xvbmcinstaller.nl','repository.xvbmc','resource.language.nl_nl','script.xvbmc.updatertools','service.xbmc.versioncheck','skin.aeon.nox.spin','script.grab.fanart','service.library.data.provider','resource.images.recordlabels.white','resource.images.studios.coloured','resource.images.studios.white','xbmc.gui','script.skinshortcuts','script.module.simplejson','script.module.unidecode')#line:360
        O0O0OOOO0OO000O00 =('Addons26.db','Addons27.db','guisettings.xml','kodi.log','Textures13.db')#line:362
        O00OOO0O0O0O0OO0O =OOO000OO00OO000OO .message_yes_no ("[COLOR white][B]"+AddonTitle +"[/B][/COLOR]",'Wilt u het XvBMC-NL basis \'framework\' handhaven na reset? Verwijderd alles behalve XvBMC (aanbeveling).','[COLOR dimgray](do you wish to keep XvBMC\'s default framework?)[/COLOR]')#line:363
        if O00OOO0O0O0O0OO0O :#line:364
            O0O0O0OO00O000O00 =O0O0O0OO00O000O00 +('addon_data','keymaps','media',)#line:365
            OOOO0O00O000000OO =OOOO0O00O000000OO +('inputstream.rtmp','keymaps','media','service.subtitles.addic7ed','service.subtitles.opensubtitles_by_opensubtitles','service.subtitles.opensubtitlesBeta','service.subtitles.podnapisi','service.subtitles.subscene',)#line:366
            O0O0OOOO0OO000O00 =O0O0OOOO0OO000O00 +('advancedsettings.xml','favourites.xml','profiles.xml','RssFeeds.xml','sources.xml','versiebld.txt','versiesp.txt','wizbld.txt','wizsp.txt',)#line:367
        else :#line:368
            O0O0O0OO00O000O00 =O0O0O0OO00O000O00 +('addon_data',)#line:369
            OOOO0O00O000000OO =OOOO0O00O000000OO +('inputstream.rtmp',)#line:370
            O0O0OOOO0OO000O00 =O0O0OOOO0OO000O00 +('advancedsettings.xml','RssFeeds.xml',)#line:371
            O0OOOO0O0O000OO0O =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join (USERADDONDATA ,'plugin.program.super.favourites','Super Favourites'))#line:372
            OOO000O00OOOOO0OO =OO0O0000OO00O0O00 .translatePath (O000OOOO0OO00O0OO .path .join (USERDATA ,'addon_data','script.skinshortcuts'))#line:373
            try :#line:374
                OOOOOOOO0O0O00O0O .rmtree (O0OOOO0O0O000OO0O )#line:375
            except Exception as OO00O00OO0OOOO00O :OOO000OO00OO000OO .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (OO00O00OO0OOOO00O ))#line:376
            try :#line:377
                OOOOOOOO0O0O00O0O .rmtree (OOO000O00OOOOO0OO )#line:378
            except Exception as OO00O00OO0OOOO00O :OOO000OO00OO000OO .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (OO00O00OO0OOOO00O ))#line:379
        dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Snelle XvBMC Krypton reset, even geduld...','','[COLOR dimgray](Quick XvBMC Krypton reset, please wait...)[/COLOR]')#line:380
        try :#line:381
            for OO0O000O0OO0OO0OO ,OOO000000O0O000OO ,O00000OO00OOO0OO0 in O000OOOO0OO00O0OO .walk (OO0O0O0OOOO0O000O ,topdown =True ):#line:382
                OOO000000O0O000OO [:]=[OO000OO00O000O0O0 for OO000OO00O000O0O0 in OOO000000O0O000OO if OO000OO00O000O0O0 not in OOOO0O00O000000OO ]#line:383
                O00000OO00OOO0OO0 [:]=[O0OO0O0000OO000O0 for O0OO0O0000OO000O0 in O00000OO00OOO0OO0 if O0OO0O0000OO000O0 not in O0O0OOOO0OO000O00 ]#line:384
                for O00O0OO0O0O0O00OO in O00000OO00OOO0OO0 :#line:385
                    try :#line:386
                        dp .update (11 ,'','***Cleaning files...')#line:387
                        O000OOOO0OO00O0OO .remove (O000OOOO0OO00O0OO .path .join (OO0O000O0OO0OO0OO ,O00O0OO0O0O0O00OO ))#line:388
                    except Exception as OO00O00OO0OOOO00O :OOO000OO00OO000OO .log ("rejuvXvbmc.file_name: User files partially removed - "+str (OO00O00OO0OOOO00O ))#line:390
                for O0O00000OO0OO0000 in OOO000000O0O000OO :#line:391
                    if O0O00000OO0OO0000 not in O0O0O0OO00O000O00 :#line:392
                        try :#line:393
                            dp .update (33 ,'','***Cleaning folders...')#line:394
                            OOOOOOOO0O0O00O0O .rmtree (O000OOOO0OO00O0OO .path .join (OO0O000O0OO0OO0OO ,O0O00000OO0OO0000 ))#line:395
                        except Exception as OO00O00OO0OOOO00O :OOO000OO00OO000OO .log ("rejuvXvbmc.folder: User folders partially removed - "+str (OO00O00OO0OOOO00O ))#line:397
            dp .update (66 ,'','***Crap Cleaning...')#line:398
            OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ()#line:399
        except Exception as OO00O00OO0OOOO00O :#line:400
            OOO000OO00OO000OO .log ("rejuvXvbmc: User stuff partially removed - "+str (OO00O00OO0OOOO00O ))#line:401
            OOO000OO00OO000OO .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Error![/B][/COLOR]",'...DAT ging niet helemaal goed, controleer uw log...','[COLOR dimgray](XvBMC user files partially removed, please check log)[/COLOR]')#line:402
            O0OOOOO0O000OO00O .exit ()#line:403
        dp .update (99 ,'','***Cleaning Crap...')#line:404
        OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:405
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:406
        O000OOOO0OO00O0OO ._exit (1 )#line:407
    else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:408
def WipeXBMC ():#line:411
    if skin !="skin.estuary":#line:412
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'selecteer eerst de standaard (Estuary) skin alvorens een volledige [B]\'wipe\'[/B] van uw Kodi uit te voeren.','','[COLOR dimgray](before Kodi wipe, select Estuary skin first)[/COLOR]')#line:413
        OO0O0000OO00O0O00 .executebuiltin ("ActivateWindow(InterfaceSettings)")#line:414
        return #line:415
    else :#line:416
        OOO0OOOO0OOO0O000 =OO0O0OO000O0OO00O .Dialog ().yesno ("[COLOR lime][B]BELANGRIJK / IMPORTANT / HINT[/B][/COLOR]",'[B]let op: [/B]dit zal alles verwijderen van uw huidige Kodi installatie, weet u zeker dat u wilt doorgaan[B]?[/B]','','[COLOR dimgray](this will remove your current Kodi build, continue?)[/COLOR]',yeslabel ='[COLOR lime][B]JA/YES[/B][/COLOR]',nolabel ='[COLOR red]nee/nope[/COLOR]')#line:417
        if OOO0OOOO0OOO0O000 ==1 :#line:418
           dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'verwijder alles, even geduld...','','[COLOR dimgray](remove everything, please wait...)[/COLOR]')#line:419
           try :#line:420
               for OOO000O000O000O00 ,O0O00O00000O000OO ,OO000000OOOOO0O0O in O000OOOO0OO00O0OO .walk (HOME ,topdown =True ):#line:421
                    O0O00O00000O000OO [:]=[OOO0O00OO0OO0OO0O for OOO0O00OO0OO0OO0O in O0O00O00000O000OO if OOO0O00OO0OO0OO0O not in EXCLUDES ]#line:422
                    for O0OOOO0O0O000OOOO in OO000000OOOOO0O0O :#line:423
                        try :dp .update (11 ,'','***Cleaning files...');O000OOOO0OO00O0OO .remove (O000OOOO0OO00O0OO .path .join (OOO000O000O000O00 ,O0OOOO0O0O000OOOO ));O000OOOO0OO00O0OO .rmdir (O000OOOO0OO00O0OO .path .join (OOO000O000O000O00 ,O0OOOO0O0O000OOOO ))#line:424
                        except :pass #line:425
                    for O0OOOO0O0O000OOOO in O0O00O00000O000OO :#line:426
                        try :dp .update (33 ,'','***Cleaning folders...');O000OOOO0OO00O0OO .rmdir (O000OOOO0OO00O0OO .path .join (OOO000O000O000O00 ,O0OOOO0O0O000OOOO ));O000OOOO0OO00O0OO .rmdir (OOO000O000O000O00 )#line:427
                        except :pass #line:428
               dp .update (66 ,'','***Crap Cleaning...')#line:429
               OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ()#line:430
           except :pass #line:431
           dp .update (99 ,'','***Cleaning Crap...')#line:432
           OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:433
           dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'Kodi zal nu afsluiten...','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:434
           O000OOOO0OO00O0OO ._exit (1 )#line:435
        elif OOO0OOOO0OOO0O000 ==0 :#line:436
             dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen Kodi Krypton \'wipe\' uitgevoerd...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:437
def FRESHSTART (params ):#line:440
    if int (O0O0O000O0O00O000 .kodiver )>16.7 :#line:441
       dialog .ok ("[COLOR lime]"+MainTitle +"[/COLOR] [COLOR red][B]- NOPE![/B][/COLOR]",'[COLOR orange][B]NOTE:[/B][/COLOR]','[COLOR white]alleen voor oudere Kodi\'s dan Krypton (>17.0)[/COLOR]','[COLOR dimgray](for use with older Kodi\'s only (>17.0)[/COLOR]')#line:442
    else :#line:443
        OOO000OO00OO000OO .log ("freshstart.main_XvBMC: "+repr (params ));O00O0OO0OOO0O0O0O =OOO000OO00OO000OO .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Remove[/B][/COLOR]",'Kodi terugzetten naar de standaard fabrieksinstellingen?','[COLOR dimgray](reset Kodi to factory defaults)[/COLOR]')#line:444
        if O00O0OO0OOO0O0O0O :#line:445
            O0OO0OOOOO0OO00OO =O00OO0OOOOO0OO0OO .Addon (id =AddonID ).getAddonInfo ('path');O0OO0OOOOO0OO00OO =OO0O0000OO00O0O00 .translatePath (O0OO0OOOOO0OO00OO );#line:446
            O0OO00OO0O0O0OO0O =O000OOOO0OO00O0OO .path .join (O0OO0OOOOO0OO00OO ,"..","..");O0OO00OO0O0O0OO0O =O000OOOO0OO00O0OO .path .abspath (O0OO00OO0O0O0OO0O );OOO000OO00OO000OO .log ("freshstart.main_XvBMC: xbmcPath="+O0OO00OO0O0O0OO0O );OO0O0O0OO000O0OO0 =False #line:447
            dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- FreshStart![/B][/COLOR]",'terug naar fabrieksinstellingen, even geduld...','','[COLOR dimgray](factory reset Kodi, please wait...)[/COLOR]')#line:448
            try :#line:449
                for O00000O0OO00O000O ,O00OO00OOOO0OO000 ,OOO0O00OO0O000O0O in O000OOOO0OO00O0OO .walk (O0OO00OO0O0O0OO0O ,topdown =True ):#line:450
                    O00OO00OOOO0OO000 [:]=[O0O00O000O0OO000O for O0O00O000O0OO000O in O00OO00OOOO0OO000 if O0O00O000O0OO000O not in EXCLUDES ]#line:451
                    dp .update (33 ,'','***Cleaning files+folders...')#line:452
                    for O00O0O0OOO0OOOO0O in OOO0O00OO0O000O0O :#line:453
                        try :O000OOOO0OO00O0OO .remove (O000OOOO0OO00O0OO .path .join (O00000O0OO00O000O ,O00O0O0OOO0OOOO0O ))#line:454
                        except :#line:455
                            if O00O0O0OOO0OOOO0O not in ["Addons1.db","MyMusic7","MyVideos37.db","Textures1.db","xbmc.log"]:OO0O0O0OO000O0OO0 =True #line:456
                            OOO000OO00OO000OO .log ("XvBMC-Error removing file: "+O00000O0OO00O000O +" "+O00O0O0OOO0OOOO0O )#line:457
                    for O00O0O0OOO0OOOO0O in O00OO00OOOO0OO000 :#line:458
                        try :O000OOOO0OO00O0OO .rmdir (O000OOOO0OO00O0OO .path .join (O00000O0OO00O000O ,O00O0O0OOO0OOOO0O ))#line:459
                        except :#line:460
                            if O00O0O0OOO0OOOO0O not in ["Database","userdata"]:OO0O0O0OO000O0OO0 =True #line:461
                            OOO000OO00OO000OO .log ("XvBMC-Error removing folder: "+O00000O0OO00O000O +" "+O00O0O0OOO0OOOO0O )#line:462
                dp .update (66 ,'','***Crap Cleaning...')#line:463
                OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ()#line:464
                if not OO0O0O0OO000O0OO0 :OOO000OO00OO000OO .log ("freshstart.main_XvBMC: All user files removed, you now have a CLEAN install");OOO000OO00OO000OO .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:465
                else :OOO000OO00OO000OO .log ("freshstart.main_XvBMC: User files partially removed");OOO000OO00OO000OO .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:466
            except :OOO000OO00OO000OO .message ("[COLOR red][B]"+AddonTitle +"[/B][/COLOR]",'Problem found','Your settings have [B]not[/B] been changed');import traceback as O00000OOO0OOOO0O0 ;OOO000OO00OO000OO .log (O00000OOO0OOOO0O0 .format_exc ());OOO000OO00OO000OO .log ("freshstart.main_XvBMC: NOTHING removed");O0OOOOO0O000OO00O .exit ()#line:467
            dp .update (99 ,'','***Cleaning Crap...')#line:468
            OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();OOO000OO00OO000OO .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:469
            dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:470
            O000OOOO0OO00O0OO ._exit (1 )#line:471
        else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:472
def addItem (name ,url ,mode ,iconimage ):#line:476
    O0OO00OOO00O0OOO0 =O0OOOOO0O000OO00O .argv [0 ]+"?url="+O0OO000OOOO0OO0OO .quote_plus (url )+"&mode="+str (mode )+"&name="+O0OO000OOOO0OO0OO .quote_plus (name )#line:477
    OO000OO0OO0O0OOO0 =True #line:478
    O0OO0O0O00O0OO0O0 =OO0O0OO000O0OO00O .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:479
    O0OO0O0O00O0OO0O0 .setInfo (type ="Video",infoLabels ={"Title":name })#line:480
    O0OO0O0O00O0OO0O0 .setArt ({'fanart':FANART })#line:481
    OO000OO0OO0O0OOO0 =OOO00OOOO000OOOOO .addDirectoryItem (handle =int (O0OOOOO0O000OO00O .argv [1 ]),url =O0OO00OOO00O0OOO0 ,listitem =O0OO0O0O00O0OO0O0 ,isFolder =False )#line:482
    return OO000OO0OO0O0OOO0 #line:483
def get_params ():#line:486
        OO00OO0000000OO00 =[]#line:487
        OO0OO0OO0O00000OO =O0OOOOO0O000OO00O .argv [2 ]#line:488
        if len (OO0OO0OO0O00000OO )>=2 :#line:489
                OO0OOOOOO00O00OOO =O0OOOOO0O000OO00O .argv [2 ]#line:490
                OO000O0O00000OO0O =OO0OOOOOO00O00OOO .replace ('?','')#line:491
                if (OO0OOOOOO00O00OOO [len (OO0OOOOOO00O00OOO )-1 ]=='/'):#line:492
                        OO0OOOOOO00O00OOO =OO0OOOOOO00O00OOO [0 :len (OO0OOOOOO00O00OOO )-2 ]#line:493
                OOOOOOOO00OOOOOOO =OO000O0O00000OO0O .split ('&')#line:494
                OO00OO0000000OO00 ={}#line:495
                for OOO0000OOO0000O00 in range (len (OOOOOOOO00OOOOOOO )):#line:496
                        OOOOO0OO0OOO00O0O ={}#line:497
                        OOOOO0OO0OOO00O0O =OOOOOOOO00OOOOOOO [OOO0000OOO0000O00 ].split ('=')#line:498
                        if (len (OOOOO0OO0OOO00O0O ))==2 :#line:499
                                OO00OO0000000OO00 [OOOOO0OO0OOO00O0O [0 ]]=OOOOO0OO0OOO00O0O [1 ]#line:500
        return OO00OO0000000OO00 #line:501
def addDir (name ,url ,mode ,iconimage ,fanart ,description ):#line:504
        OO00OOO00O0OOOO0O =O0OOOOO0O000OO00O .argv [0 ]+"?url="+O0OO000OOOO0OO0OO .quote_plus (url )+"&mode="+str (mode )+"&name="+O0OO000OOOO0OO0OO .quote_plus (name )+"&iconimage="+O0OO000OOOO0OO0OO .quote_plus (iconimage )+"&fanart="+O0OO000OOOO0OO0OO .quote_plus (fanart )+"&description="+O0OO000OOOO0OO0OO .quote_plus (description )#line:505
        O00000OOOOOO0O0OO =True #line:506
        OOO00OO0000OOO0O0 =OO0O0OO000O0OO00O .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:507
        OOO00OO0000OOO0O0 .setInfo (type ="Video",infoLabels ={"Title":name ,"Plot":description })#line:508
        OOO00OO0000OOO0O0 .setProperty ("Fanart_Image",fanart )#line:509
        if mode ==1 :#line:510
            O00000OOOOOO0O0OO =OOO00OOOO000OOOOO .addDirectoryItem (handle =int (O0OOOOO0O000OO00O .argv [1 ]),url =OO00OOO00O0OOOO0O ,listitem =OOO00OO0000OOO0O0 ,isFolder =False )#line:511
        elif mode ==2 :#line:512
            O00000OOOOOO0O0OO =OOO00OOOO000OOOOO .addDirectoryItem (handle =int (O0OOOOO0O000OO00O .argv [1 ]),url =OO00OOO00O0OOOO0O ,listitem =OOO00OO0000OOO0O0 ,isFolder =False )#line:513
        elif mode ==69 :#line:514
            O00000OOOOOO0O0OO =OOO00OOOO000OOOOO .addDirectoryItem (handle =int (O0OOOOO0O000OO00O .argv [1 ]),url =OO00OOO00O0OOOO0O ,listitem =OOO00OO0000OOO0O0 ,isFolder =False )#line:515
        else :#line:516
            O00000OOOOOO0O0OO =OOO00OOOO000OOOOO .addDirectoryItem (handle =int (O0OOOOO0O000OO00O .argv [1 ]),url =OO00OOO00O0OOOO0O ,listitem =OOO00OO0000OOO0O0 ,isFolder =True )#line:517
        return O00000OOOOOO0O0OO #line:518
params =get_params ()#line:521
url =None #line:522
name =None #line:523
mode =None #line:524
iconimage =None #line:525
fanart =None #line:526
description =None #line:527
try :#line:530
        url =O0OO000OOOO0OO0OO .unquote_plus (params ["url"])#line:531
except :#line:532
        pass #line:533
try :#line:534
        name =O0OO000OOOO0OO0OO .unquote_plus (params ["name"])#line:535
except :#line:536
        pass #line:537
try :#line:538
        iconimage =O0OO000OOOO0OO0OO .unquote_plus (params ["iconimage"])#line:539
except :#line:540
        pass #line:541
try :#line:542
        mode =int (params ["mode"])#line:543
except :#line:544
        pass #line:545
try :#line:546
        fanart =O0OO000OOOO0OO0OO .unquote_plus (params ["fanart"])#line:547
except :#line:548
        pass #line:549
try :#line:550
        description =O0OO000OOOO0OO0OO .unquote_plus (params ["description"])#line:551
except :#line:552
        pass #line:553
OOO000OO00OO000OO .log ("EPiC "+str (AddonTitle ))#line:557
if mode ==None or url ==None or len (url )<1 :#line:565
   mainMenu ()#line:566
elif mode ==1 :#line:568
     wizard (name ,url )#line:570
elif mode ==10 :#line:572
     XvBMCtools1 ()#line:573
elif mode ==20 :#line:575
     XvBMCmaint ()#line:576
elif mode ==30 :#line:578
     XvBMCrpi ()#line:579
elif mode ==2 :#line:581
     OOO000OO00OO000OO .AboutXvBMC ()#line:582
elif mode ==3 :#line:584
     OOO000OO00OO000OO .closeandexit ()#line:585
elif mode ==4 :#line:587
     OOO000OO00OO000OO .okDialog (O0000OOO0O0OO000O ,'sorry, nothing todo...','with kind regards, team [COLOR green]XvBMC Nederland[/COLOR]')#line:588
elif mode ==11 :#line:590
     OO00OOOO00OOO0000 .Fix_Special (url )#line:591
elif mode ==12 :#line:593
     OO00OOOO00OOO0000 .AddonsEnable ()#line:594
elif mode ==13 :#line:596
     O0O0OOO0O0O0O0000 .setall_enable ()#line:597
elif mode ==14 :#line:599
     OO00OOOO00OOO0000 .EnableRTMP ()#line:600
elif mode ==15 :#line:602
     OOO000OO00OO000OO .killKodi ()#line:603
elif mode ==16 :#line:605
     OOO000OO00OO000OO .KODIVERSION (url )#line:606
elif mode ==17 :#line:608
     OO00OOOO00OOO0000 .xvbmcLog ()#line:609
elif mode ==18 :#line:611
     resolver_settings ()#line:612
elif mode ==19 :#line:614
     unlocker ()#line:615
elif mode ==21 :#line:617
     O0O0OOOO00O000O0O .purgeOLD ()#line:618
elif mode ==22 :#line:620
     OO00OOOO00OOO0000 .clearCache ()#line:621
elif mode ==23 :#line:623
     OO00OOOO00OOO0000 .deleteThumbnails ()#line:624
elif mode ==24 :#line:626
     O000OOOOOO0000O0O .flushMenu ()#line:627
elif mode ==25 :#line:629
     OO00OOOO00OOO0000 .autocleanask ()#line:630
elif mode ==26 :#line:632
     OO00OOOO00OOO0000 .purgePackages ()#line:633
elif mode ==27 :#line:635
     OOO000OO00OO000OO .forceRefresh (melding =True )#line:636
elif mode ==28 :#line:638
     OO00OOOO00OOO0000 .AddonsDatabaseRemoval ()#line:639
elif mode ==29 :#line:641
     O0O0O000O0O00O000 .enableAddons (melding =True )#line:642
elif mode ==31 :#line:644
     OO00OOOO00OOO0000 .PiCCleaner ()#line:645
elif mode ==32 :#line:647
     XvbmcOc ()#line:648
elif mode ==33 :#line:650
     XvbmcDev ()#line:651
elif mode ==40 :#line:653
     XvBMCtools2 ()#line:654
elif mode ==41 :#line:656
     rejuvXvbmc ()#line:657
elif mode ==42 :#line:659
     WipeXBMC ()#line:660
elif mode ==43 :#line:662
     FRESHSTART (params )#line:663
elif mode ==44 :#line:665
     disabled ()#line:666
elif mode ==69 :#line:668
     fileexchange (url )#line:670
     wizard (name ,url +'rpi-service.zip')#line:672
"""
    IF you copy/paste XvBMC's -default.py- please keep the credits -2- XvBMC-NL, Thx.
"""#line:676
OOO00OOOO000OOOOO .endOfDirectory (int (O0OOOOO0O000OO00O .argv [1 ]))
