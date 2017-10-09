#!/usr/bin/python
""#line:6
import re as O00O00O0OOOO0OO00 ,base64 as O0000O000OOOOOOOO ,urllib as OOO00OO0O0000OO00 ,urllib2 as O00OOOO0OOO0000OO ,sys as O0O00O00O00OOO00O ,xbmcvfs as OO0O0OOO0O00O0000 #line:25
import xbmc as O0O0O00O00000OOOO ,xbmcaddon as OO0OO00O0OOO0O00O ,xbmcgui as OOO00OOOO00OO0OO0 ,xbmcplugin as OO0O00O0000OOOOO0 #line:26
import os as OO0OO0O00O0O0OO00 ,shutil as O000000000OO000OO ,time as O00OOO0OO0O0000OO #line:27
import sqlite3 as O00O0OO00O0OOO00O #line:28
import utils as OOO000OO00OO0O0OO #line:29
from resources .lib import addon_able as O00OOOOOOO0OOOOO0 #line:32
from resources .lib import downloader as OO000O0O00O0O0OO0 ,extract as O0O0OOOOOO0O0OO0O #line:33
from resources .lib import common as O0OO0OOO00OOOO0O0 #line:34
from resources .lib .common import platform as OO000OO0O0OO00O00 ,subtitleNope as O00OOO00OOO0OOOO0 ,nonlinux as O00OO0O00000OOO00 ,nonelecNL as O0O000OO00OO000OO #line:35
from resources .lib .common import base as OOOOOOOO0OO000000 ,basewiz as OOO000OO00000OOOO ,currentbldtxt as O0O0O0OOOOOOO0O0O ,currentsptxt as OO000O000OOOOO000 ,currentbldtxtwiz as O000O0OO00O00O00O ,currentsptxtwiz as OO000O0O00OOO00OO ,currentsptxtrpi as OO0OOO0OOO000O000 #line:36
from resources .lib import flush as O0O0OO000OO0OO0OO #line:38
from resources .lib import huisvrouw as OOO00O000OO0O0OOO #line:39
from resources .lib import purge as OO000OOOO0OO000OO #line:40
from resources .lib import rpioc as OO0OO00OOO00O000O #line:41
from resources .lib import rpidev as OO00O0OOO00OOO00O #line:42
ADDON =OOO000OO00OO0O0OO .ADDON #line:44
ADDON_ID =OO0OO00O0OOO0O00O .Addon ().getAddonInfo ('id')#line:46
AddonID ='script.xvbmc.updatertools'#line:47
AddonTitle ='XvBMC Nederland'#line:48
addonPath =OO0OO0O00O0O0OO00 .path .join (OO0OO0O00O0O0OO00 .path .join (O0O0O00O00000OOOO .translatePath ('special://home'),'addons'),'script.xvbmc.updatertools')#line:49
ART =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/addons/'+AddonID +'/resources/media/'))#line:50
artwork =O0000O000OOOOOOOO .b64decode ('c2tpbi5hZW9uLm5veC5zcGlu')#line:51
FANART =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/addons/'+AddonID ,'fanart.jpg'))#line:52
FANARTsub =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/addons/'+AddonID +'/resources/media/','art.jpg'))#line:53
ICON =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/addons/'+AddonID ,'icon.png'))#line:54
MainTitle ="XvBMC Nederland"#line:55
mediaPath =OO0OO0O00O0O0OO00 .path .join (addonPath ,'resources/media')#line:56
U =ADDON .getSetting ('User')#line:57
USER_AGENT ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'#line:58
About ='[COLOR dimgray][B]X[/B]v[B]BMC[/B] disclaimer & usage policy[/COLOR]'#line:60
Terug ='[COLOR dimgray]<<<back[/COLOR]'#line:61
dialog =OOO00OOOO00OO0OO0 .Dialog ()#line:63
dp =OOO00OOOO00OO0OO0 .DialogProgress ()#line:64
BASEURL ="https://bit.ly/XvBMC-Pi"#line:65
buildinfotxt ='[COLOR gray][B] - [/B]your XvBMC build: [I]unknown[/I] [/COLOR]'#line:66
serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: [I]unknown[/I] [/COLOR]'#line:67
xbmcver =O0O0O00O00000OOOO .getInfoLabel ("System.BuildVersion")[:4 ]#line:68
EXCLUDES =[ADDON_ID ,'plugin.program.xvbmcinstaller.nl','repository.xvbmc']#line:70
HOME =O0O0O00O00000OOOO .translatePath ('special://home/')#line:71
skin =O0O0O00O00000OOOO .getSkinDir ()#line:72
USERDATA =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/userdata',''))#line:73
USERADDONDATA =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/userdata/addon_data',''))#line:74
def resolver_settings ():#line:78
    import urlresolver as O0OOO00OO000O0O0O #line:79
    O0OOO00OO000O0O0O .display_settings ()#line:80
def mainMenu ():#line:83
    O00O000O0O0O00OO0 ,OOO00O0O00O0OOOOO =OOO000OO00OO0O0OO .checkUpdate ()#line:85
    if O00O000O0O0O00OO0 =="update":#line:87
       OOOO0OOO00OOOO0O0 ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(OOO00O0O00O0OOOOO )+'[COLOR orange] (fork)[/COLOR]'#line:88
       O00OO0OOOOOO00OOO =O0000O000OOOOOOOO .b64decode (OOOOOOOO0OO000000 )+'update/sp/servicepack.zip'#line:89
       addDir ('%s'%OOOO0OOO00OOOO0O0 ,O00OO0OOOOOO00OOO ,1 ,ART +'xvbmc.png',FANART ,'')#line:91
    elif O00O000O0O0O00OO0 =="wizupdate":#line:92
       OOOO0OOO00OOOO0O0 ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(OOO00O0O00O0OOOOO )+'[COLOR orange] (wizard)[/COLOR]'#line:93
       O00OO0OOOOOO00OOO =O0000O000OOOOOOOO .b64decode (OOO000OO00000OOOO )+'wizardsp.zip'#line:94
       addDir ('%s'%OOOO0OOO00OOOO0O0 ,O00OO0OOOOOO00OOO ,1 ,ART +'xvbmc.png',FANART ,'')#line:96
    elif O00O000O0O0O00OO0 =="rpiupdate":#line:97
       OOOO0OOO00OOOO0O0 ="[COLOR orange]XvBMC RPi update available[B]: %s[/B][/COLOR]"%(OOO00O0O00O0OOOOO )+'[COLOR orange] (forced)[/COLOR]'#line:98
       O0O0OO0000OOOOO00 =O0000O000OOOOOOOO .b64decode (OOOOOOOO0OO000000 )+'update/sp/'#line:99
       addDir ('%s'%OOOO0OOO00OOOO0O0 ,O0O0OO0000OOOOO00 ,69 ,ART +'xvbmc.png',FANART ,'')#line:101
    elif O00O000O0O0O00OO0 =="notinstalled":#line:105
       if O0O0O00O00000OOOO .getCondVisibility ('System.HasAddon(%s)'%(artwork )):#line:106
          if OO0OO0O00O0O0OO00 .path .isfile (O0OO0OOO00OOOO0O0 .bldversietxt ):#line:107
             OOOO0OOO00OOOO0O0 ="[COLOR orange]Sorry (portable) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:108
             O00OO0OOOOOO00OOO =O0000O000OOOOOOOO .b64decode (OOOOOOOO0OO000000 )+'update/sp/servicepack.zip'#line:109
             addDir ('%s'%OOOO0OOO00OOOO0O0 ,O00OO0OOOOOO00OOO ,1 ,ART +'xvbmc.png',FANART ,'')#line:111
          elif OO0OO0O00O0O0OO00 .path .isfile (O0OO0OOO00OOOO0O0 .bldversietxtwiz ):#line:112
               OOOO0OOO00OOOO0O0 ="[COLOR orange]Sorry (wizard) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:113
               O00OO0OOOOOO00OOO =O0000O000OOOOOOOO .b64decode (OOO000OO00000OOOO )+'wizardsp.zip'#line:114
               addDir ('%s'%OOOO0OOO00OOOO0O0 ,O00OO0OOOOOO00OOO ,1 ,ART +'xvbmc.png',FANART ,'')#line:116
          elif O0O0O00O00000OOOO .getCondVisibility ('System.HasAddon("service.openelec.settings")')+O0O0O00O00000OOOO .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:118
               OOOO0OOO00OOOO0O0 ="[COLOR orange]unknown [B]RPi[/B] version; force update[B]?[/B][/COLOR] [COLOR lime] (continue?)[/COLOR]"#line:119
               O0O0OO0000OOOOO00 =O0000O000OOOOOOOO .b64decode (OOOOOOOO0OO000000 )+'update/sp/'#line:120
               addDir ('%s'%OOOO0OOO00OOOO0O0 ,O0O0OO0000OOOOO00 ,69 ,ART +'xvbmc.png',FANART ,'')#line:122
          else :#line:123
               OOOO0OOO00OOOO0O0 ="[COLOR orange]unknown build status; force update?[/COLOR] [COLOR red][B](continue at your own risk)[/B][/COLOR]"#line:124
               O0O0O0OOO00O000O0 =O0000O000OOOOOOOO .b64decode (OOOOOOOO0OO000000 )+'update/sp/servicepack.zip'#line:125
               addDir ('%s'%OOOO0OOO00OOOO0O0 ,O0O0O0OOO00O000O0 ,1 ,ART +'xvbmc.png',FANART ,'')#line:127
       else :#line:128
          OOOO0OOO00OOOO0O0 ="[COLOR orange]Sorry, [B]unknown[/B] build/servicepack/update status [B] :[/B]\'-([/COLOR]"#line:129
          addItem ('%s'%OOOO0OOO00OOOO0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:130
    elif O00O000O0O0O00OO0 =="noupdaterpi":#line:131
         if O0O0O00O00000OOOO .getCondVisibility ('System.HasAddon("service.openelec.settings")')+O0O0O00O00000OOOO .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:133
            OOOO0OOO00OOOO0O0 ="[COLOR orange]You have the [B]latest[/B] [COLOR red]XvBMC[/COLOR] [COLOR lime][B]RPi[/B][/COLOR] forced updates [B] 3:[/B]-)[/COLOR]"#line:134
            addItem ('%s'%OOOO0OOO00OOOO0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:135
         else :#line:136
            OOOO0OOO00OOOO0O0 ="[COLOR orange]You [B]somehow[/B] have the latest [COLOR lime]XvBMC[/COLOR] [COLOR red][B]RPi[/B][/COLOR] forced updates [B]???[/B][/COLOR]"#line:137
            addItem ('%s'%OOOO0OOO00OOOO0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:138
    else :#line:139
       OOOO0OOO00OOOO0O0 ="[COLOR orange]You have the [B]latest[/B] XvBMC updates [B] :[/B]-)[/COLOR]"#line:140
       addItem ('%s'%OOOO0OOO00OOOO0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:141
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:143
    addDir ('[COLOR red]XvBMC Tools[/COLOR]',BASEURL ,10 ,ART +'tools.png',OO0OO0O00O0O0OO00 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:144
    addDir ('[COLOR white]XvBMC Maintenance[/COLOR]',BASEURL ,20 ,ART +'maint.png',OO0OO0O00O0O0OO00 .path .join (mediaPath ,"onderhoud.jpg"),'')#line:145
    addDir ('[COLOR dodgerblue]XvBMC About[/COLOR]',BASEURL ,2 ,ART +'wtf.png',OO0OO0O00O0O0OO00 .path .join (mediaPath ,"over.jpg"),'')#line:146
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:147
    addItem ('[COLOR gray]system information (kodi %s):[/COLOR]'%xbmcver ,BASEURL ,16 ,ART +'xvbmc.png')#line:148
    global serviceinfotxt #line:149
    OO0O0000OOO0OO0OO ,OOOOOOO0OO00000OO =O0OO0OOO00OOOO0O0 .checkSPversie ()#line:150
    if OO0O0000OOO0OO0OO =="uwspversietxt":#line:151
       OO0O0O0O0OO000O0O =OOO000OO00OO0O0OO .getHtml2 (OO000O000OOOOO000 )#line:152
       serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OOOOOOO0OO00000OO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OO0O0O0O0OO000O0O )#line:153
    elif OO0O0000OOO0OO0OO =="uwspversietxtwiz":#line:154
         OO0O0O0O0OO000O0O =OOO000OO00OO0O0OO .getHtml2 (OO000O0O00OOO00OO )#line:155
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OOOOOOO0OO00000OO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OO0O0O0O0OO000O0O )#line:156
    elif OO0O0000OOO0OO0OO =="uwspversietxtrpi":#line:157
         OO0O0O0O0OO000O0O =OOO000OO00OO0O0OO .getHtml2 (OO0OOO0OOO000O000 )#line:158
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OOOOOOO0OO00000OO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OO0O0O0O0OO000O0O )#line:159
    addItem ('%s'%serviceinfotxt ,BASEURL ,'',OO0OO0O00O0O0OO00 .path .join (mediaPath ,"wtf.png"))#line:160
    global buildinfotxt #line:161
    OOOO0OOOO000O000O ,O0O0OOOOO00OO0OOO =O0OO0OOO00OOOO0O0 .checkXvbmcversie ()#line:162
    if OOOO0OOOO000O000O =="bldversietxt":#line:163
       OO0O000O0OOO0O0OO =OOO000OO00OO0O0OO .getHtml2 (O0O0O0OOOOOOO0O0O )#line:164
       buildinfotxt ='[COLOR gray][B] - [/B]your system build: %s [/COLOR]'%(O0O0OOOOO00OO0OOO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OO0O000O0OOO0O0OO )#line:165
    elif OOOO0OOOO000O000O =="bldversietxtwiz":#line:166
         OO0O000O0OOO0O0OO =OOO000OO00OO0O0OO .getHtml2 (O000O0OO00O00O00O )#line:167
         buildinfotxt ='[COLOR gray][B] - [/B]your wizard build: %s [/COLOR]'%(O0O0OOOOO00OO0OOO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%OO0O000O0OOO0O0OO )#line:168
    addItem ('%s'%buildinfotxt ,BASEURL ,'',OO0OO0O00O0O0OO00 .path .join (mediaPath ,"wtf.png"))#line:169
    if O0O0O00O00000OOOO .getCondVisibility ('System.HasAddon("service.openelec.settings")')+O0O0O00O00000OOOO .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:171
       addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:172
       addDir ('[COLOR orange]XvBMC Raspberry Pi [B] -[/B] Tools, DEV. & Maintenance[/COLOR]',BASEURL ,30 ,ART +'RPi.png',FANARTsub ,'')#line:173
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:175
    addItem (Terug ,BASEURL ,3 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:176
    O0OO0OOO00OOOO0O0 .setView ('movies','EPiC')#line:177
def XvBMCmaint ():#line:179
    addItem ('[B]B[/B]uild [COLOR red]purge[/COLOR] [COLOR dimgray](build [B]c[/B]rap[B]c[/B]leaner & fix evil addons/repos)[/COLOR]',BASEURL ,21 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:180
    addItem ('[B]C[/B]lear cache',BASEURL ,22 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:181
    addItem ('[B]D[/B]elete thumbnails',BASEURL ,23 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:182
    addItem ('[B]F[/B]lush add-ons [COLOR dimgray](salts HD/RD lite & Exodus \'cache+temp\' files)[/COLOR]',BASEURL ,24 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:183
    addItem ('[B]F[/B]ull \"auto\" clean [COLOR dimgray](cache, crashlogs, packages & thumbnails)[/COLOR]',BASEURL ,25 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:184
    addItem ('[B]P[/B]urge packages',BASEURL ,26 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:185
    addItem ('[B]R[/B]efresh addons[COLOR white]+[/COLOR]repos',BASEURL ,27 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:186
    if int (OOO000OO00OO0O0OO .kodiver )<=16.7 :#line:187
       addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s remove addons.db',BASEURL ,28 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:188
    elif int (OOO000OO00OO0O0OO .kodiver )>16.7 :#line:189
         addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s enable all add-ons [COLOR dimgray](Kodi 17+ Krypton)[/COLOR]',BASEURL ,29 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:190
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:192
    addItem (About ,BASEURL ,2 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"wtf.png"))#line:193
    addItem (Terug ,BASEURL ,3 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:194
    O0OO0OOO00OOOO0O0 .setView ('movies','EPiC')#line:195
def XvBMCtools1 ():#line:197
    addItem ('[B]C[/B]onvert physical paths (\'home\') to \'special\'',BASEURL ,11 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:198
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]most[/COLOR] add-ons)[/COLOR]',BASEURL ,12 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:199
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]all[/COLOR] add-ons)[/COLOR]',BASEURL ,13 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:200
    addItem ('[B]E[/B]nable Kodi Live Streams [COLOR dimgray](17+ Krypton; [COLOR white]RTMP[/COLOR])[/COLOR]',BASEURL ,14 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:201
    addItem ('[B]F[/B]orce close Kodi  [COLOR dimgray](Kill Kodi)[/COLOR]',BASEURL ,15 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:202
    addItem ('[B]L[/B]og viewer [COLOR dimgray](show \'kodi.log\')[/COLOR]',BASEURL ,17 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:204
    addItem ('[B]U[/B]RLResolver -> settings',BASEURL ,18 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:205
    addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s Advancedsettings unlocker [COLOR dimgray](reset)[/COLOR]',BASEURL ,19 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:206
    addDir ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s [COLOR white][B]H[/B]idden [B]g[/B]ems[B] & [/B][B]M[/B]ore [B]t[/B]ools[/COLOR] [COLOR dimgray](TiP[B]!![/B])[/COLOR]',BASEURL ,40 ,ART +'xvbmc.png',OO0OO0O00O0O0OO00 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:207
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:209
    addItem (About ,BASEURL ,2 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"wtf.png"))#line:210
    addItem (Terug ,BASEURL ,3 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:211
    O0OO0OOO00OOOO0O0 .setView ('movies','EPiC')#line:212
def XvBMCrpi ():#line:214
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] extreme crapcleaner [COLOR dimgray]([B]no[/B] factory reset)[/COLOR]',BASEURL ,31 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"tools.png"))#line:215
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] overclock [COLOR dimgray](raspberry Pi ***only***)[/COLOR]',BASEURL ,32 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"overclock.png"))#line:216
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] #dev# corner [COLOR dimgray](firmware, OS, etc.)[/COLOR]',BASEURL ,33 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"firmware.png"))#line:217
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:219
    addItem (About ,BASEURL ,2 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"wtf.png"))#line:220
    addItem (Terug ,BASEURL ,3 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:221
    O0OO0OOO00OOOO0O0 .setView ('movies','EPiC')#line:222
def XvBMCtools2 ():#line:224
    addItem ('[B]K[/B]odi Quick Reset [COLOR dimgray](\"rejuvenate\" XvBMC-NL build)[/COLOR]',BASEURL ,41 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:226
    addItem ('[B]K[/B]odi Factory Reset [COLOR dimgray](complete Kodi Krypton wipe)[/COLOR]',BASEURL ,42 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:227
    addItem ('[B]K[/B]odi Fresh Start [COLOR dimgray](remove older Kodi\'s)[/COLOR]',BASEURL ,43 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:228
    addItem ('[B]P[/B]ush Fixes [COLOR dimgray](for XvBMC builds)[/COLOR]',BASEURL ,44 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:229
    addItem ('[B]P[/B]ush XvBMC REPOsitory [COLOR dimgray](install or fix repo)[/COLOR]',BASEURL ,45 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:231
    addItem ('[B]P[/B]ush x[B]X[/B]x [COLOR dimgray](\"dirty\"-up your box with some 69 and mo\')[/COLOR]',BASEURL ,46 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"maint.png"))#line:232
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:234
    addItem (About ,BASEURL ,2 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"wtf.png"))#line:235
    addItem (Terug ,BASEURL ,3 ,OO0OO0O00O0O0OO00 .path .join (mediaPath ,"xvbmc.png"))#line:236
    O0OO0OOO00OOOO0O0 .setView ('movies','EPiC')#line:237
def wizard (name ,url ):#line:241
    O0O0O00O00O0O0000 =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/addons','packages'))#line:242
    if not OO0OO0O00O0O0OO00 .path .exists (O0O0O00O00O0O0000 ):#line:243
        OO0OO0O00O0O0OO00 .makedirs (O0O0O00O00O0O0000 )#line:244
    O0O0OOOO0O0O0OOO0 =OO0OO0O00O0O0OO00 .path .join (O0O0O00O00O0O0000 ,'default.zip')#line:245
    try :#line:246
       OO0OO0O00O0O0OO00 .remove (O0O0OOOO0O0O0OOO0 )#line:247
    except :#line:248
       pass #line:249
    OO000O0O00O0O0OO0 .download (url ,O0O0OOOO0O0O0OOO0 )#line:250
    if OO0OO0O00O0O0OO00 .path .exists (O0O0OOOO0O0O0OOO0 ):#line:252
        OO00O0O0O00O00O0O =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://','home'))#line:253
        O00OOO0OO0O0000OO .sleep (2 )#line:254
        dp .create (MainTitle ,'XvBMC-NL: pull update VoOdOo...','','Please Wait')#line:256
        dp .update (0 ,"","***Extract ZIP - Please Wait")#line:257
        O0OO0OOO00OOOO0O0 .log ("==========================================================")#line:258
        O0OO0OOO00OOOO0O0 .log (OO00O0O0O00O00O0O )#line:259
        O0OO0OOO00OOOO0O0 .log ("==========================================================")#line:260
        O0O0OOOOOO0O0OO0O .all (O0O0OOOO0O0O0OOO0 ,OO00O0O0O00O00O0O ,dp )#line:261
        dp .close ()#line:262
        try :OO0OO0O00O0O0OO00 .remove (O0O0OOOO0O0O0OOO0 )#line:263
        except :pass #line:264
    if int (OOO000OO00OO0O0OO .kodiver )<=16.7 :#line:265
       dialog .ok (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  HINT  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:266
       O0OO0OOO00OOOO0O0 .forceRefresh (melding =False )#line:267
    elif int (OOO000OO00OO0O0OO .kodiver )>16.7 :#line:268
         OOO000OO00OO0O0OO .enableAddons (melding =False )#line:269
         O00OOO0OO0O0000OO .sleep (0.5 )#line:270
         OOO00O0O0000OO000 =OOO00OOOO00OO0OO0 .Dialog ().yesno (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  SUCCESS  !!![/B][/COLOR]','[B]IF[/B] add-ons do NOT work you probably should reboot.','(een REBOOT van uw systeem is VEELAL wenselijk)',yeslabel ='[COLOR lime]Reboot[/COLOR]',nolabel ='[COLOR red]Continue[/COLOR]')#line:271
         if OOO00O0O0000OO000 ==1 :#line:272
            O00OOO0OO0O0000OO .sleep (1 )#line:273
            O0OO0OOO00OOOO0O0 .killKodi ()#line:274
         elif OOO00O0O0000OO000 ==0 :#line:275
              if int (OOO000OO00OO0O0OO .kodiver )>16.7 :#line:276
                 OOO000OO00OO0O0OO .enableAddons (melding =False )#line:277
                 O00OOO0OO0O0000OO .sleep (0.5 )#line:278
                 dialog .ok (MainTitle +" : [COLOR red]add-ons[/COLOR] [COLOR green][B]enabled[/B][/COLOR]",'[COLOR orange][B]!!!  TIP  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:279
                 O0O0O00O00000OOOO .executebuiltin ('ReloadSkin()')#line:280
    O0O0O00O00000OOOO .executebuiltin ("Container.Refresh")#line:281
    O0O0O00O00000OOOO .sleep (5000 )#line:282
def fileexchange (url ,name ,locatie ):#line:288
    dp .create (MainTitle ,'XvBMC-NL: RPi update VoOdOo...','','Please Wait')#line:289
    if not OO0OO0O00O0O0OO00 .path .exists (locatie ):OO0OO0O00O0O0OO00 .makedirs (locatie )#line:290
    O0OOO0OOO00O0O000 =OO0OO0O00O0O0OO00 .path .join (locatie ,name )#line:291
    dp .update (0 ,'','.file.VoOdOo.')#line:292
    try :OO0OO0O00O0O0OO00 .remove (O0OOO0OOO00O0O000 )#line:293
    except :pass #line:294
    OO000O0O00O0O0OO0 .download (url +name ,O0OOO0OOO00O0O000 )#line:295
    O00OOO0OO0O0000OO .sleep (1 )#line:296
    dp .close ()#line:297
    O0O0O00O00000OOOO .executebuiltin ("Container.Refresh")#line:299
    O0O0O00O00000OOOO .sleep (1000 )#line:300
def unlocker ():#line:303
    dialog .ok (MainTitle +" - unlocker",' ','unlock advancedsettings for this build','[COLOR dimgray](+reset \'advancedsettings.xml\' -use at your own risk)[/COLOR]')#line:305
    O000O0000O00000OO =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/userdata/'))#line:306
    OO00O0O0OOOO0O0OO =O0000O000OOOOOOOO .b64decode ('YWR2YW5jZWRzZXR0aW5ncy54bWw=')#line:307
    O0OO0OOOOO0O0OO0O =True #line:308
    try :#line:309
        OO0OO0O00O0O0OO00 .unlink (O000O0000O00000OO +OO00O0O0OOOO0O0OO )#line:310
    except :#line:311
        O0OO0OOOOO0O0OO0O =False #line:312
    if O0OO0OOOOO0O0OO0O :#line:314
        dialog .ok (MainTitle +" - [B]UNLOCKED[/B]",'[COLOR green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Herstart[/B] Kodi ter afronding \'unlocker\' (force close)','[B]Reboot[/B] Kodi to complete \'unlocker\' (force close)')#line:315
        OO0OO0O00O0O0OO00 ._exit (1 )#line:316
    else :#line:317
        dialog .ok (MainTitle +" - [B]OOOOOOPS[/B]",'[COLOR red][B]!!!  Failed  !!![/B][/COLOR]','[B]Nope![/B] helaas geen succes (niks te \'unlocken\')','[B]Nope![/B] close but no cigar  (nothing to \'unlock\')')#line:318
def XvbmcOc ():#line:321
    O00OOO0O00O0O0O00 =OO000OO0O0OO00O00 ()#line:322
    O0OO0OOO00OOOO0O0 .log ("Platform: "+str (O00OOO0O00O0O0O00 ))#line:323
    if not O00OOO0O00O0O0O00 =='linux':#line:324
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] OverClock!",O00OOO00OOO0OOOO0 ,O00OO0O00000OOO00 ,O0O000OO00OO000OO )#line:325
       O0OO0OOO00OOOO0O0 .log ("none Linux OS ie. Open-/LibreELEC")#line:326
    else :#line:327
        O0OO0OOO00OOOO0O0 .log ("linux os")#line:328
        OO0OO00OOO00O000O .ocMenu ()#line:329
def XvbmcDev ():#line:332
    O00O000OOOOO00O00 =OO000OO0O0OO00O00 ()#line:333
    O0OO0OOO00OOOO0O0 .log ("Platform: "+str (O00O000OOOOO00O00 ))#line:334
    if not O00O000OOOOO00O00 =='linux':#line:335
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] #dev#",O00OOO00OOO0OOOO0 ,O00OO0O00000OOO00 ,O0O000OO00OO000OO )#line:336
       O0OO0OOO00OOOO0O0 .log ("none Linux OS ie. Open-/LibreELEC")#line:337
    else :#line:338
        O0OO0OOO00OOOO0O0 .log ("linux os")#line:339
        OO00O0OOO00OOO00O .devMenu ()#line:340
def disabled ():#line:343
    O0OO0OOO00OOOO0O0 .okDialog ('[COLOR red][B]Sorry, disabled! [/B](for now)[/COLOR]','','[COLOR lime]goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')#line:344
def rejuvXvbmc ():#line:347
    OOOO000OO000O0OOO =O0OO0OOO00OOOO0O0 .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Wilt u uw XvBMC \'build\' volledig opschonen (wipe) en Kodi Krypton [B]leeg[/B] her-configureren?','[COLOR dimgray]Please confirm that you wish you wipe clean your current configuration and reconfigure Kodi.[/COLOR]')#line:348
    if OOOO000OO000O0OOO :#line:349
        OOOO0O0O0OO0O0OO0 =OO0OO00O0OOO0O00O .Addon (id =AddonID ).getAddonInfo ('path');OOOO0O0O0OO0O0OO0 =O0O0O00O00000OOOO .translatePath (OOOO0O0O0OO0O0OO0 );#line:350
        OOO0O0O000OO00O0O =OO0OO0O00O0O0OO00 .path .join (OOOO0O0O0OO0O0OO0 ,"..","..");OOO0O0O000OO00O0O =OO0OO0O00O0O0OO00 .path .abspath (OOO0O0O000OO00O0O );O0OO0OOO00OOOO0O0 .log ("rejuvXvbmc.main_XvBMC: xbmcPath="+OOO0O0O000OO00O0O );#line:351
        OOO0OO0O00OOO00OO =('addons','Database','packages','userdata')#line:353
        OO0OOO000OO0O0OO0 =('metadata.album.universal','metadata.artists.universal','metadata.common.imdb.com','metadata.common.musicbrainz.org','metadata.common.theaudiodb.com','metadata.common.themoviedb.org','metadata.themoviedb.org','metadata.tvdb.com','plugin.program.super.favourites','plugin.program.xvbmcinstaller.nl','repository.xvbmc','resource.language.nl_nl','script.xvbmc.updatertools','service.xbmc.versioncheck','skin.aeon.nox.spin','script.grab.fanart','service.library.data.provider','resource.images.recordlabels.white','resource.images.studios.coloured','resource.images.studios.white','xbmc.gui','script.skinshortcuts','script.module.simplejson','script.module.unidecode')#line:359
        O0000OOOOO00OOO0O =('Addons26.db','Addons27.db','guisettings.xml','kodi.log','Textures13.db')#line:361
        O0OOO000O0O0000OO =O0OO0OOO00OOOO0O0 .message_yes_no ("[COLOR white][B]"+AddonTitle +"[/B][/COLOR]",'Wilt u het XvBMC-NL basis \'framework\' handhaven na reset? Verwijderd alles behalve XvBMC (aanbeveling).','[COLOR dimgray](do you wish to keep XvBMC\'s default framework?)[/COLOR]')#line:362
        if O0OOO000O0O0000OO :#line:363
            OOO0OO0O00OOO00OO =OOO0OO0O00OOO00OO +('addon_data','keymaps','media',)#line:364
            OO0OOO000OO0O0OO0 =OO0OOO000OO0O0OO0 +('inputstream.rtmp','keymaps','media','service.subtitles.addic7ed','service.subtitles.opensubtitles_by_opensubtitles','service.subtitles.opensubtitlesBeta','service.subtitles.podnapisi','service.subtitles.subscene',)#line:365
            O0000OOOOO00OOO0O =O0000OOOOO00OOO0O +('advancedsettings.xml','favourites.xml','profiles.xml','RssFeeds.xml','sources.xml','versiebld.txt','versiesp.txt','wizbld.txt','wizsp.txt',)#line:366
        else :#line:367
            OOO0OO0O00OOO00OO =OOO0OO0O00OOO00OO +('addon_data',)#line:368
            OO0OOO000OO0O0OO0 =OO0OOO000OO0O0OO0 +('inputstream.rtmp',)#line:369
            O0000OOOOO00OOO0O =O0000OOOOO00OOO0O +('advancedsettings.xml','RssFeeds.xml',)#line:370
            O0OO00000O0O00OOO =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join (USERADDONDATA ,'plugin.program.super.favourites','Super Favourites'))#line:371
            OOOO00OO0OO0O0000 =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join (USERDATA ,'addon_data','script.skinshortcuts'))#line:372
            try :#line:373
                O000000000OO000OO .rmtree (O0OO00000O0O00OOO )#line:374
            except Exception as OO000O0O0OOOOO00O :O0OO0OOO00OOOO0O0 .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (OO000O0O0OOOOO00O ))#line:375
            try :#line:376
                O000000000OO000OO .rmtree (OOOO00OO0OO0O0000 )#line:377
            except Exception as OO000O0O0OOOOO00O :O0OO0OOO00OOOO0O0 .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (OO000O0O0OOOOO00O ))#line:378
        dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Snelle XvBMC Krypton reset, even geduld...','','[COLOR dimgray](Quick XvBMC Krypton reset, please wait...)[/COLOR]')#line:379
        try :#line:380
            for O00O0O0000OO0OO00 ,O00OO0O0000OO0O0O ,O00OO0OOOOO00OOO0 in OO0OO0O00O0O0OO00 .walk (OOO0O0O000OO00O0O ,topdown =True ):#line:381
                O00OO0O0000OO0O0O [:]=[O00OOO0OO0OO0OO00 for O00OOO0OO0OO0OO00 in O00OO0O0000OO0O0O if O00OOO0OO0OO0OO00 not in OO0OOO000OO0O0OO0 ]#line:382
                O00OO0OOOOO00OOO0 [:]=[O0O0OO0O00OOO0O00 for O0O0OO0O00OOO0O00 in O00OO0OOOOO00OOO0 if O0O0OO0O00OOO0O00 not in O0000OOOOO00OOO0O ]#line:383
                for OOOO0O00OOOO0O0OO in O00OO0OOOOO00OOO0 :#line:384
                    try :#line:385
                        dp .update (11 ,'','***Cleaning files...')#line:386
                        OO0OO0O00O0O0OO00 .remove (OO0OO0O00O0O0OO00 .path .join (O00O0O0000OO0OO00 ,OOOO0O00OOOO0O0OO ))#line:387
                    except Exception as OO000O0O0OOOOO00O :O0OO0OOO00OOOO0O0 .log ("rejuvXvbmc.file_name: User files partially removed - "+str (OO000O0O0OOOOO00O ))#line:389
                for O0O00OOO0OO00O000 in O00OO0O0000OO0O0O :#line:390
                    if O0O00OOO0OO00O000 not in OOO0OO0O00OOO00OO :#line:391
                        try :#line:392
                            dp .update (33 ,'','***Cleaning folders...')#line:393
                            O000000000OO000OO .rmtree (OO0OO0O00O0O0OO00 .path .join (O00O0O0000OO0OO00 ,O0O00OOO0OO00O000 ))#line:394
                        except Exception as OO000O0O0OOOOO00O :O0OO0OOO00OOOO0O0 .log ("rejuvXvbmc.folder: User folders partially removed - "+str (OO000O0O0OOOOO00O ))#line:396
            dp .update (66 ,'','***Crap Cleaning...')#line:397
            O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ()#line:398
        except Exception as OO000O0O0OOOOO00O :#line:399
            O0OO0OOO00OOOO0O0 .log ("rejuvXvbmc: User stuff partially removed - "+str (OO000O0O0OOOOO00O ))#line:400
            O0OO0OOO00OOOO0O0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Error![/B][/COLOR]",'...DAT ging niet helemaal goed, controleer uw log...','[COLOR dimgray](XvBMC user files partially removed, please check log)[/COLOR]')#line:401
            O0O00O00O00OOO00O .exit ()#line:402
        dp .update (99 ,'','***Cleaning Crap...')#line:403
        O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:404
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:405
        OO0OO0O00O0O0OO00 ._exit (1 )#line:406
    else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:407
def WipeXBMC ():#line:410
    if skin !="skin.estuary":#line:411
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'selecteer eerst de standaard (Estuary) skin alvorens een volledige [B]\'wipe\'[/B] van uw Kodi uit te voeren.','','[COLOR dimgray](before Kodi wipe, select Estuary skin first)[/COLOR]')#line:412
        O0O0O00O00000OOOO .executebuiltin ("ActivateWindow(InterfaceSettings)")#line:413
        return #line:414
    else :#line:415
        O0OO0OOOO00O0OOO0 =OOO00OOOO00OO0OO0 .Dialog ().yesno ("[COLOR lime][B]BELANGRIJK / IMPORTANT / HINT[/B][/COLOR]",'[B]let op: [/B]dit zal alles verwijderen van uw huidige Kodi installatie, weet u zeker dat u wilt doorgaan[B]?[/B]','','[COLOR dimgray](this will remove your current Kodi build, continue?)[/COLOR]',yeslabel ='[COLOR lime][B]JA/YES[/B][/COLOR]',nolabel ='[COLOR red]nee/nope[/COLOR]')#line:416
        if O0OO0OOOO00O0OOO0 ==1 :#line:417
           dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'verwijder alles, even geduld...','','[COLOR dimgray](remove everything, please wait...)[/COLOR]')#line:418
           try :#line:419
               for OO0O0000OOOOOOOOO ,O000000O0O000O0O0 ,OO0000O0000OO0OO0 in OO0OO0O00O0O0OO00 .walk (HOME ,topdown =True ):#line:420
                    O000000O0O000O0O0 [:]=[O00O00OOOO00O000O for O00O00OOOO00O000O in O000000O0O000O0O0 if O00O00OOOO00O000O not in EXCLUDES ]#line:421
                    for O0OO0OOOOOO0000O0 in OO0000O0000OO0OO0 :#line:422
                        try :dp .update (11 ,'','***Cleaning files...');OO0OO0O00O0O0OO00 .remove (OO0OO0O00O0O0OO00 .path .join (OO0O0000OOOOOOOOO ,O0OO0OOOOOO0000O0 ));OO0OO0O00O0O0OO00 .rmdir (OO0OO0O00O0O0OO00 .path .join (OO0O0000OOOOOOOOO ,O0OO0OOOOOO0000O0 ))#line:423
                        except :pass #line:424
                    for O0OO0OOOOOO0000O0 in O000000O0O000O0O0 :#line:425
                        try :dp .update (33 ,'','***Cleaning folders...');OO0OO0O00O0O0OO00 .rmdir (OO0OO0O00O0O0OO00 .path .join (OO0O0000OOOOOOOOO ,O0OO0OOOOOO0000O0 ));OO0OO0O00O0O0OO00 .rmdir (OO0O0000OOOOOOOOO )#line:426
                        except :pass #line:427
               dp .update (66 ,'','***Crap Cleaning...')#line:428
               O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ()#line:429
           except :pass #line:430
           dp .update (99 ,'','***Cleaning Crap...')#line:431
           O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:432
           dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'Kodi zal nu afsluiten...','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:433
           OO0OO0O00O0O0OO00 ._exit (1 )#line:434
        elif O0OO0OOOO00O0OOO0 ==0 :#line:435
             dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen Kodi Krypton \'wipe\' uitgevoerd...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:436
def FRESHSTART (params ):#line:439
    if int (OOO000OO00OO0O0OO .kodiver )>16.7 :#line:440
       dialog .ok ("[COLOR lime]"+MainTitle +"[/COLOR] [COLOR red][B]- NOPE![/B][/COLOR]",'[COLOR orange][B]NOTE:[/B][/COLOR]','[COLOR white]alleen voor oudere Kodi\'s dan Krypton (>17.0)[/COLOR]','[COLOR dimgray](for use with older Kodi\'s only (>17.0)[/COLOR]')#line:441
    else :#line:442
        O0OO0OOO00OOOO0O0 .log ("freshstart.main_XvBMC: "+repr (params ));OO0O000O0O0OOO000 =O0OO0OOO00OOOO0O0 .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Remove[/B][/COLOR]",'Kodi terugzetten naar de standaard fabrieksinstellingen?','[COLOR dimgray](reset Kodi to factory defaults)[/COLOR]')#line:443
        if OO0O000O0O0OOO000 :#line:444
            OO00O0OO0OO00O000 =OO0OO00O0OOO0O00O .Addon (id =AddonID ).getAddonInfo ('path');OO00O0OO0OO00O000 =O0O0O00O00000OOOO .translatePath (OO00O0OO0OO00O000 );#line:445
            O00000OOO0OO000O0 =OO0OO0O00O0O0OO00 .path .join (OO00O0OO0OO00O000 ,"..","..");O00000OOO0OO000O0 =OO0OO0O00O0O0OO00 .path .abspath (O00000OOO0OO000O0 );O0OO0OOO00OOOO0O0 .log ("freshstart.main_XvBMC: xbmcPath="+O00000OOO0OO000O0 );O0O00OO00OO00OOOO =False #line:446
            dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- FreshStart![/B][/COLOR]",'terug naar fabrieksinstellingen, even geduld...','','[COLOR dimgray](factory reset Kodi, please wait...)[/COLOR]')#line:447
            try :#line:448
                for OO00OO00OO0O0O000 ,O0O000000OO0OOO0O ,O0OO0OOOO00OO000O in OO0OO0O00O0O0OO00 .walk (O00000OOO0OO000O0 ,topdown =True ):#line:449
                    O0O000000OO0OOO0O [:]=[O00OOOOOOOOOOOOO0 for O00OOOOOOOOOOOOO0 in O0O000000OO0OOO0O if O00OOOOOOOOOOOOO0 not in EXCLUDES ]#line:450
                    dp .update (33 ,'','***Cleaning files+folders...')#line:451
                    for O0000OOO000O0OO00 in O0OO0OOOO00OO000O :#line:452
                        try :OO0OO0O00O0O0OO00 .remove (OO0OO0O00O0O0OO00 .path .join (OO00OO00OO0O0O000 ,O0000OOO000O0OO00 ))#line:453
                        except :#line:454
                            if O0000OOO000O0OO00 not in ["Addons1.db","MyMusic7","MyVideos37.db","Textures1.db","xbmc.log"]:O0O00OO00OO00OOOO =True #line:455
                            O0OO0OOO00OOOO0O0 .log ("XvBMC-Error removing file: "+OO00OO00OO0O0O000 +" "+O0000OOO000O0OO00 )#line:456
                    for O0000OOO000O0OO00 in O0O000000OO0OOO0O :#line:457
                        try :OO0OO0O00O0O0OO00 .rmdir (OO0OO0O00O0O0OO00 .path .join (OO00OO00OO0O0O000 ,O0000OOO000O0OO00 ))#line:458
                        except :#line:459
                            if O0000OOO000O0OO00 not in ["Database","userdata"]:O0O00OO00OO00OOOO =True #line:460
                            O0OO0OOO00OOOO0O0 .log ("XvBMC-Error removing folder: "+OO00OO00OO0O0O000 +" "+O0000OOO000O0OO00 )#line:461
                dp .update (66 ,'','***Crap Cleaning...')#line:462
                O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ()#line:463
                if not O0O00OO00OO00OOOO :O0OO0OOO00OOOO0O0 .log ("freshstart.main_XvBMC: All user files removed, you now have a CLEAN install");O0OO0OOO00OOOO0O0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:464
                else :O0OO0OOO00OOOO0O0 .log ("freshstart.main_XvBMC: User files partially removed");O0OO0OOO00OOOO0O0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:465
            except :O0OO0OOO00OOOO0O0 .message ("[COLOR red][B]"+AddonTitle +"[/B][/COLOR]",'Problem found','Your settings have [B]not[/B] been changed');import traceback as OOO00000OOO0O00OO ;O0OO0OOO00OOOO0O0 .log (OOO00000OOO0O00OO .format_exc ());O0OO0OOO00OOOO0O0 .log ("freshstart.main_XvBMC: NOTHING removed");O0O00O00O00OOO00O .exit ()#line:466
            dp .update (99 ,'','***Cleaning Crap...')#line:467
            O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();O0OO0OOO00OOOO0O0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:468
            dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:469
            OO0OO0O00O0O0OO00 ._exit (1 )#line:470
        else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:471
def repository (name ,url ,locatie ):#line:474
    O00000OO000OOOO00 =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home/addons','packages'))#line:475
    if not OO0OO0O00O0O0OO00 .path .exists (O00000OO000OOOO00 ):OO0OO0O00O0O0OO00 .makedirs (O00000OO000OOOO00 )#line:476
    O000OO000O0OOO0O0 =OO0OO0O00O0O0OO00 .path .join (O00000OO000OOOO00 ,name )#line:477
    try :OO0OO0O00O0O0OO00 .remove (O000OO000O0OOO0O0 )#line:478
    except :pass #line:479
    OO000O0O00O0O0OO0 .download (url ,O000OO000O0OOO0O0 )#line:480
    if OO0OO0O00O0O0OO00 .path .exists (O000OO000O0OOO0O0 ):#line:481
        O00OOO0OO0O0000OO .sleep (2 )#line:482
        dp .create (MainTitle ,'XvBMC-NL: Repository VoOdOo...','','Please Wait')#line:483
        dp .update (0 ,'','***Mo\' XvBMC Repo vOoDoO')#line:484
        O0OO0OOO00OOOO0O0 .log ('REPO@'+locatie )#line:485
        O0O0OOOOOO0O0OO0O .all (O000OO000O0OOO0O0 ,locatie ,dp )#line:486
        dp .close ()#line:487
        try :OO0OO0O00O0O0OO00 .remove (O000OO000O0OOO0O0 )#line:488
        except :pass #line:489
    if int (OOO000OO00OO0O0OO .kodiver )<=16.7 :#line:490
       dialog .ok (MainTitle +"[COLOR green][B] - finished[/B][/COLOR]",' ','[COLOR orange][B]!!!  DONE  !!![/B][/COLOR]')#line:491
       O0OO0OOO00OOOO0O0 .forceRefresh (melding =False )#line:492
    elif int (OOO000OO00OO0O0OO .kodiver )>16.7 :#line:493
         OOO000OO00OO0O0OO .enableAddons (melding =False )#line:494
         O00OOO0OO0O0000OO .sleep (0.5 )#line:495
         dialog .ok (MainTitle +"[COLOR green][B] - finished[/B][/COLOR]",' ','[COLOR orange][B]!!!  DONE  !!![/B][/COLOR]')#line:496
         O0O0O00O00000OOOO .executebuiltin ('ReloadSkin()')#line:497
    O0O0O00O00000OOOO .executebuiltin ("Container.Refresh")#line:498
    O0O0O00O00000OOOO .sleep (5000 )#line:499
def addItem (name ,url ,mode ,iconimage ):#line:502
    OO0OOO00O0OO0OO0O =O0O00O00O00OOO00O .argv [0 ]+"?url="+OOO00OO0O0000OO00 .quote_plus (url )+"&mode="+str (mode )+"&name="+OOO00OO0O0000OO00 .quote_plus (name )#line:503
    O00O0000OOO0OOOO0 =True #line:504
    OOO000OO00O0OO00O =OOO00OOOO00OO0OO0 .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:505
    OOO000OO00O0OO00O .setInfo (type ="Video",infoLabels ={"Title":name })#line:506
    OOO000OO00O0OO00O .setArt ({'fanart':FANART })#line:507
    O00O0000OOO0OOOO0 =OO0O00O0000OOOOO0 .addDirectoryItem (handle =int (O0O00O00O00OOO00O .argv [1 ]),url =OO0OOO00O0OO0OO0O ,listitem =OOO000OO00O0OO00O ,isFolder =False )#line:508
    return O00O0000OOO0OOOO0 #line:509
def get_params ():#line:512
        OO00OO000O000OOO0 =[]#line:513
        O0OOOO00OO0OO0O00 =O0O00O00O00OOO00O .argv [2 ]#line:514
        if len (O0OOOO00OO0OO0O00 )>=2 :#line:515
                O0O00OOO0O00OO0O0 =O0O00O00O00OOO00O .argv [2 ]#line:516
                OOO0OOO00O0OOO00O =O0O00OOO0O00OO0O0 .replace ('?','')#line:517
                if (O0O00OOO0O00OO0O0 [len (O0O00OOO0O00OO0O0 )-1 ]=='/'):#line:518
                        O0O00OOO0O00OO0O0 =O0O00OOO0O00OO0O0 [0 :len (O0O00OOO0O00OO0O0 )-2 ]#line:519
                O00000OOO000O0OOO =OOO0OOO00O0OOO00O .split ('&')#line:520
                OO00OO000O000OOO0 ={}#line:521
                for OOOOO0O0OOOO0O0O0 in range (len (O00000OOO000O0OOO )):#line:522
                        OOOOO0OOO0O000O00 ={}#line:523
                        OOOOO0OOO0O000O00 =O00000OOO000O0OOO [OOOOO0O0OOOO0O0O0 ].split ('=')#line:524
                        if (len (OOOOO0OOO0O000O00 ))==2 :#line:525
                                OO00OO000O000OOO0 [OOOOO0OOO0O000O00 [0 ]]=OOOOO0OOO0O000O00 [1 ]#line:526
        return OO00OO000O000OOO0 #line:527
def addDir (name ,url ,mode ,iconimage ,fanart ,description ):#line:530
        O0OOOOOO0OO000OO0 =O0O00O00O00OOO00O .argv [0 ]+"?url="+OOO00OO0O0000OO00 .quote_plus (url )+"&mode="+str (mode )+"&name="+OOO00OO0O0000OO00 .quote_plus (name )+"&iconimage="+OOO00OO0O0000OO00 .quote_plus (iconimage )+"&fanart="+OOO00OO0O0000OO00 .quote_plus (fanart )+"&description="+OOO00OO0O0000OO00 .quote_plus (description )#line:531
        O0OOOOOOOO0OOOOO0 =True #line:532
        O0OOO00O0O00OO000 =OOO00OOOO00OO0OO0 .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:533
        O0OOO00O0O00OO000 .setInfo (type ="Video",infoLabels ={"Title":name ,"Plot":description })#line:534
        O0OOO00O0O00OO000 .setProperty ("Fanart_Image",fanart )#line:535
        if mode ==1 :#line:536
            O0OOOOOOOO0OOOOO0 =OO0O00O0000OOOOO0 .addDirectoryItem (handle =int (O0O00O00O00OOO00O .argv [1 ]),url =O0OOOOOO0OO000OO0 ,listitem =O0OOO00O0O00OO000 ,isFolder =False )#line:537
        elif mode ==2 :#line:538
            O0OOOOOOOO0OOOOO0 =OO0O00O0000OOOOO0 .addDirectoryItem (handle =int (O0O00O00O00OOO00O .argv [1 ]),url =O0OOOOOO0OO000OO0 ,listitem =O0OOO00O0O00OO000 ,isFolder =False )#line:539
        elif mode ==69 :#line:540
            O0OOOOOOOO0OOOOO0 =OO0O00O0000OOOOO0 .addDirectoryItem (handle =int (O0O00O00O00OOO00O .argv [1 ]),url =O0OOOOOO0OO000OO0 ,listitem =O0OOO00O0O00OO000 ,isFolder =False )#line:541
        else :#line:542
            O0OOOOOOOO0OOOOO0 =OO0O00O0000OOOOO0 .addDirectoryItem (handle =int (O0O00O00O00OOO00O .argv [1 ]),url =O0OOOOOO0OO000OO0 ,listitem =O0OOO00O0O00OO000 ,isFolder =True )#line:543
        return O0OOOOOOOO0OOOOO0 #line:544
params =get_params ()#line:547
url =None #line:548
name =None #line:549
mode =None #line:550
iconimage =None #line:551
fanart =None #line:552
description =None #line:553
try :#line:556
        url =OOO00OO0O0000OO00 .unquote_plus (params ["url"])#line:557
except :#line:558
        pass #line:559
try :#line:560
        name =OOO00OO0O0000OO00 .unquote_plus (params ["name"])#line:561
except :#line:562
        pass #line:563
try :#line:564
        iconimage =OOO00OO0O0000OO00 .unquote_plus (params ["iconimage"])#line:565
except :#line:566
        pass #line:567
try :#line:568
        mode =int (params ["mode"])#line:569
except :#line:570
        pass #line:571
try :#line:572
        fanart =OOO00OO0O0000OO00 .unquote_plus (params ["fanart"])#line:573
except :#line:574
        pass #line:575
try :#line:576
        description =OOO00OO0O0000OO00 .unquote_plus (params ["description"])#line:577
except :#line:578
        pass #line:579
O0OO0OOO00OOOO0O0 .log ("EPiC "+str (AddonTitle ))#line:583
if mode ==None or url ==None or len (url )<1 :#line:591
   mainMenu ()#line:592
elif mode ==1 :#line:594
     wizard (name ,url )#line:596
elif mode ==10 :#line:598
     XvBMCtools1 ()#line:599
elif mode ==20 :#line:601
     XvBMCmaint ()#line:602
elif mode ==30 :#line:604
     XvBMCrpi ()#line:605
elif mode ==2 :#line:607
     O0OO0OOO00OOOO0O0 .AboutXvBMC ()#line:608
elif mode ==3 :#line:610
     O0OO0OOO00OOOO0O0 .closeandexit ()#line:611
elif mode ==4 :#line:613
     O0OO0OOO00OOOO0O0 .okDialog (O00OOO00OOO0OOOO0 ,'sorry, nothing todo...','with kind regards, team [COLOR green]XvBMC Nederland[/COLOR]')#line:614
elif mode ==11 :#line:616
     OOO00O000OO0O0OOO .Fix_Special (url )#line:617
elif mode ==12 :#line:619
     OOO00O000OO0O0OOO .AddonsEnable ()#line:620
elif mode ==13 :#line:622
     O00OOOOOOO0OOOOO0 .setall_enable ()#line:623
elif mode ==14 :#line:625
     OOO00O000OO0O0OOO .EnableRTMP ()#line:626
elif mode ==15 :#line:628
     O0OO0OOO00OOOO0O0 .killKodi ()#line:629
elif mode ==16 :#line:631
     O0OO0OOO00OOOO0O0 .KODIVERSION (url )#line:632
elif mode ==17 :#line:634
     OOO00O000OO0O0OOO .xvbmcLog ()#line:635
elif mode ==18 :#line:637
     resolver_settings ()#line:638
elif mode ==19 :#line:640
     unlocker ()#line:641
elif mode ==21 :#line:643
     OO000OOOO0OO000OO .purgeOLD ()#line:644
elif mode ==22 :#line:646
     OOO00O000OO0O0OOO .clearCache ()#line:647
elif mode ==23 :#line:649
     OOO00O000OO0O0OOO .deleteThumbnails ()#line:650
elif mode ==24 :#line:652
     O0O0OO000OO0OO0OO .flushMenu ()#line:653
elif mode ==25 :#line:655
     OOO00O000OO0O0OOO .autocleanask ()#line:656
elif mode ==26 :#line:658
     OOO00O000OO0O0OOO .purgePackages ()#line:659
elif mode ==27 :#line:661
     O0OO0OOO00OOOO0O0 .forceRefresh (melding =True )#line:662
elif mode ==28 :#line:664
     OOO00O000OO0O0OOO .AddonsDatabaseRemoval ()#line:665
elif mode ==29 :#line:667
     OOO000OO00OO0O0OO .enableAddons (melding =True )#line:668
elif mode ==31 :#line:670
     OOO00O000OO0O0OOO .PiCCleaner ()#line:671
elif mode ==32 :#line:673
     XvbmcOc ()#line:674
elif mode ==33 :#line:676
     XvbmcDev ()#line:677
elif mode ==40 :#line:679
     XvBMCtools2 ()#line:680
elif mode ==41 :#line:682
     rejuvXvbmc ()#line:683
elif mode ==42 :#line:685
     WipeXBMC ()#line:686
elif mode ==43 :#line:688
     FRESHSTART (params )#line:689
elif mode ==44 :#line:691
     disabled ()#line:692
elif mode ==45 :#line:694
     locatie =O0O0O00O00000OOOO .translatePath (OO0OO0O00O0O0OO00 .path .join ('special://home','addons'))#line:695
     name ='repository.xvbmc-4.1.0.zip'#line:696
     url =O0000O000OOOOOOOO .b64decode ('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL1JFUE9zaXRvcnkvemlwcy9yZXBvc2l0b3J5Lnh2Ym1jLw==')+name #line:697
     repository (name ,url ,locatie )#line:699
elif mode ==46 :#line:701
     url =O0000O000OOOOOOOO .b64decode (OOOOOOOO0OO000000 )+'triple-x/xXxvbmc.zip'#line:702
     wizard (name ,url )#line:704
elif mode ==69 :#line:706
     locatie =USERDATA #line:707
     name ='rpi-service'#line:708
     fileexchange (url ,name +'.txt',locatie )#line:710
     wizard (name ,url +name +'.zip')#line:712
"""
    IF you copy/paste XvBMC's -default.py- please keep the credits -2- XvBMC-NL, Thx.
"""#line:716
OO0O00O0000OOOOO0 .endOfDirectory (int (O0O00O00O00OOO00O .argv [1 ]))
