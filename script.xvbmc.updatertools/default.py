#!/usr/bin/python
""#line:6
import re as O0O00OOOO00OOOOO0 ,base64 as OO000OO0O0O000O0O ,urllib as OO0O0O0O00OO00O0O ,urllib2 as OOOOO00O00000O000 ,sys as O0O0OOO00O0OOOOO0 ,xbmcvfs as OOO0OOO0000000000 #line:25
import xbmc as O0O00O00OOOO0OO00 ,xbmcaddon as O0O00O0000OO0O0OO ,xbmcgui as OOOO0OOO000O000OO ,xbmcplugin as OOOO0OOO00000O00O #line:26
import os as OOOO00O000OOO0OO0 ,shutil as OO00OOOO0OO0OO00O ,time as O00OO0OO00O0O00O0 #line:27
import sqlite3 as OOO0O0O00O00OO0OO #line:28
import utils as OOOOOOOO00OOOO000 #line:29
from resources .lib import addon_able as OO0OO0000O0O000O0 #line:32
from resources .lib import downloader as O000OOOOOOO00OO0O ,extract as O000OOO000O00O0OO #line:33
from resources .lib import common as O0O0O0O0O00OO00O0 #line:34
from resources .lib .common import platform as O000OO00O00O00O00 ,subtitleNope as O00O000OOO0O0O0O0 ,nonlinux as OOOOOOOOO0O0O0000 ,nonelecNL as O00O00OO000OO00O0 #line:35
from resources .lib .common import base as OO00O0OO00OOO0OOO ,basewiz as OO0O0O0OO00OO0000 ,currentbldtxt as O0O0OOO0000O0O00O ,currentsptxt as O000O00O000OOOOOO ,currentbldtxtwiz as O00000O000O0O0O0O ,currentsptxtwiz as OO00O000000OO0OOO ,currentsptxtrpi as O00O0OOOOO00O0OOO ,repos as OO00O00O000OOOO00 #line:36
from resources .lib import flush as OOO0O00O0OOO0O00O #line:38
from resources .lib import huisvrouw as OO0OO00O00O000OOO #line:39
from resources .lib import purge as O00OO0OOOO0OOO0OO #line:40
from resources .lib import rpioc as OOO000O00OO00OO0O #line:41
from resources .lib import rpidev as OO000O00OO00OOO00 #line:42
ADDON =OOOOOOOO00OOOO000 .ADDON #line:44
ADDON_ID =O0O00O0000OO0O0OO .Addon ().getAddonInfo ('id')#line:46
AddonID ='script.xvbmc.updatertools'#line:47
AddonTitle ='XvBMC Nederland'#line:48
addonPath =OOOO00O000OOO0OO0 .path .join (OOOO00O000OOO0OO0 .path .join (O0O00O00OOOO0OO00 .translatePath ('special://home'),'addons'),'script.xvbmc.updatertools')#line:49
ART =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/addons/'+AddonID +'/resources/media/'))#line:50
artwork =OO000OO0O0O000O0O .b64decode ('c2tpbi5hZW9uLm5veC5zcGlu')#line:51
FANART =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/addons/'+AddonID ,'fanart.jpg'))#line:52
FANARTsub =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/addons/'+AddonID +'/resources/media/','art.jpg'))#line:53
ICON =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/addons/'+AddonID ,'icon.png'))#line:54
MainTitle ="XvBMC Nederland"#line:55
mediaPath =OOOO00O000OOO0OO0 .path .join (addonPath ,'resources/media')#line:56
U =ADDON .getSetting ('User')#line:57
USER_AGENT ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'#line:58
About ='[COLOR dimgray][B]X[/B]v[B]BMC[/B] disclaimer & usage policy[/COLOR]'#line:60
Terug ='[COLOR dimgray]<<<back[/COLOR]'#line:61
dialog =OOOO0OOO000O000OO .Dialog ()#line:63
dp =OOOO0OOO000O000OO .DialogProgress ()#line:64
BASEURL ="https://bit.ly/XvBMC-Pi"#line:65
buildinfotxt ='[COLOR gray][B] - [/B]your XvBMC build: [I]unknown[/I] [/COLOR]'#line:66
serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: [I]unknown[/I] [/COLOR]'#line:67
xbmcver =O0O00O00OOOO0OO00 .getInfoLabel ("System.BuildVersion")[:4 ]#line:68
EXCLUDES =[ADDON_ID ,'plugin.program.xvbmcinstaller.nl','repository.xvbmc']#line:70
HOME =O0O00O00OOOO0OO00 .translatePath ('special://home/')#line:71
skin =O0O00O00OOOO0OO00 .getSkinDir ()#line:72
USERDATA =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/userdata',''))#line:73
USERADDONDATA =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/userdata/addon_data',''))#line:74
xxxCheck =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join (USERADDONDATA ,'plugin.program.super.favourites','Super Favourites','xXx','favourites.xml'))#line:75
xxxIcon =OO000OO0O0O000O0O .b64decode ('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMvdHJpcGxlLXgvYWR1bHQucG5n')#line:76
def resolver_settings ():#line:80
    import urlresolver as O0OO0O0000OOOOO00 #line:81
    O0OO0O0000OOOOO00 .display_settings ()#line:82
def mainMenu ():#line:85
    O0O0O0OOO0OO00OOO ,OO0000OO00O0OO0O0 =OOOOOOOO00OOOO000 .checkUpdate ()#line:87
    if O0O0O0OOO0OO00OOO =="update":#line:89
       OO0O0O0OOO0OO0O0O ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(OO0000OO00O0OO0O0 )+'[COLOR orange] (fork)[/COLOR]'#line:90
       OO00O0O0O0O0O0O00 =OO000OO0O0O000O0O .b64decode (OO00O0OO00OOO0OOO )+'update/sp/servicepack.zip'#line:91
       addDir ('%s'%OO0O0O0OOO0OO0O0O ,OO00O0O0O0O0O0O00 ,1 ,ART +'xvbmc.png',FANART ,'')#line:93
    elif O0O0O0OOO0OO00OOO =="wizupdate":#line:94
       OO0O0O0OOO0OO0O0O ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(OO0000OO00O0OO0O0 )+'[COLOR orange] (wizard)[/COLOR]'#line:95
       OO00O0O0O0O0O0O00 =OO000OO0O0O000O0O .b64decode (OO0O0O0OO00OO0000 )+'wizardsp.zip'#line:96
       addDir ('%s'%OO0O0O0OOO0OO0O0O ,OO00O0O0O0O0O0O00 ,1 ,ART +'xvbmc.png',FANART ,'')#line:98
    elif O0O0O0OOO0OO00OOO =="rpiupdate":#line:99
       OO0O0O0OOO0OO0O0O ="[COLOR orange]XvBMC RPi update available[B]: %s[/B][/COLOR]"%(OO0000OO00O0OO0O0 )+'[COLOR orange] (forced)[/COLOR]'#line:100
       OOO0O0000OOOOO00O =OO000OO0O0O000O0O .b64decode (OO00O0OO00OOO0OOO )+'update/sp/'#line:101
       addDir ('%s'%OO0O0O0OOO0OO0O0O ,OOO0O0000OOOOO00O ,100 ,ART +'xvbmc.png',FANART ,'')#line:103
    elif O0O0O0OOO0OO00OOO =="notinstalled":#line:107
       if O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon(%s)'%(artwork )):#line:108
          if OOOO00O000OOO0OO0 .path .isfile (O0O0O0O0O00OO00O0 .bldversietxt ):#line:109
             OO0O0O0OOO0OO0O0O ="[COLOR orange]Sorry (portable) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:110
             OO00O0O0O0O0O0O00 =OO000OO0O0O000O0O .b64decode (OO00O0OO00OOO0OOO )+'update/sp/servicepack.zip'#line:111
             addDir ('%s'%OO0O0O0OOO0OO0O0O ,OO00O0O0O0O0O0O00 ,1 ,ART +'xvbmc.png',FANART ,'')#line:113
          elif OOOO00O000OOO0OO0 .path .isfile (O0O0O0O0O00OO00O0 .bldversietxtwiz ):#line:114
               OO0O0O0OOO0OO0O0O ="[COLOR orange]Sorry (wizard) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:115
               OO00O0O0O0O0O0O00 =OO000OO0O0O000O0O .b64decode (OO0O0O0OO00OO0000 )+'wizardsp.zip'#line:116
               addDir ('%s'%OO0O0O0OOO0OO0O0O ,OO00O0O0O0O0O0O00 ,1 ,ART +'xvbmc.png',FANART ,'')#line:118
          elif O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon("service.openelec.settings")')+O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:120
               OO0O0O0OOO0OO0O0O ="[COLOR orange]unknown [B]RPi[/B] version; force update[B]?[/B][/COLOR] [COLOR lime] (continue?)[/COLOR]"#line:121
               OOO0O0000OOOOO00O =OO000OO0O0O000O0O .b64decode (OO00O0OO00OOO0OOO )+'update/sp/'#line:122
               addDir ('%s'%OO0O0O0OOO0OO0O0O ,OOO0O0000OOOOO00O ,100 ,ART +'xvbmc.png',FANART ,'')#line:124
          else :#line:125
               OO0O0O0OOO0OO0O0O ="[COLOR orange]unknown build status; force update?[/COLOR] [COLOR red][B](continue at your own risk)[/B][/COLOR]"#line:126
               OO0000OOO0O0O0000 =OO000OO0O0O000O0O .b64decode (OO00O0OO00OOO0OOO )+'update/sp/servicepack.zip'#line:127
               addDir ('%s'%OO0O0O0OOO0OO0O0O ,OO0000OOO0O0O0000 ,1 ,ART +'xvbmc.png',FANART ,'')#line:129
       else :#line:130
          OO0O0O0OOO0OO0O0O ="[COLOR orange]Sorry, [B]unknown[/B] build/servicepack/update status [B] :[/B]\'-([/COLOR]"#line:131
          addItem ('%s'%OO0O0O0OOO0OO0O0O ,BASEURL ,4 ,ART +'xvbmc.png')#line:132
    elif O0O0O0OOO0OO00OOO =="noupdaterpi":#line:133
         if O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon("service.openelec.settings")')+O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:135
            OO0O0O0OOO0OO0O0O ="[COLOR orange]You have the [B]latest[/B] [COLOR red]XvBMC[/COLOR] [COLOR lime][B]RPi[/B][/COLOR] forced updates [B] 3:[/B]-)[/COLOR]"#line:136
            addItem ('%s'%OO0O0O0OOO0OO0O0O ,BASEURL ,4 ,ART +'xvbmc.png')#line:137
         else :#line:138
            OO0O0O0OOO0OO0O0O ="[COLOR orange]You [B]somehow[/B] have the latest [COLOR lime]XvBMC[/COLOR] [COLOR red][B]RPi[/B][/COLOR] forced updates [B]???[/B][/COLOR]"#line:139
            addItem ('%s'%OO0O0O0OOO0OO0O0O ,BASEURL ,4 ,ART +'xvbmc.png')#line:140
    else :#line:141
       OO0O0O0OOO0OO0O0O ="[COLOR orange]You have the [B]latest[/B] XvBMC updates [B] :[/B]-)[/COLOR]"#line:142
       addItem ('%s'%OO0O0O0OOO0OO0O0O ,BASEURL ,4 ,ART +'xvbmc.png')#line:143
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:145
    addDir ('[COLOR red]XvBMC Tools[/COLOR]',BASEURL ,10 ,ART +'tools.png',OOOO00O000OOO0OO0 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:146
    addDir ('[COLOR white]XvBMC Maintenance[/COLOR]',BASEURL ,20 ,ART +'maint.png',OOOO00O000OOO0OO0 .path .join (mediaPath ,"onderhoud.jpg"),'')#line:147
    addDir ('[COLOR dodgerblue]XvBMC About[/COLOR]',BASEURL ,2 ,ART +'wtf.png',OOOO00O000OOO0OO0 .path .join (mediaPath ,"over.jpg"),'')#line:148
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:149
    addItem ('[COLOR gray]system information (kodi %s):[/COLOR]'%xbmcver ,BASEURL ,16 ,ART +'xvbmc.png')#line:150
    global serviceinfotxt #line:151
    OO0O0000O0000O0OO ,OOO00O00OO00O0OOO =O0O0O0O0O00OO00O0 .checkSPversie ()#line:152
    if OO0O0000O0000O0OO =="uwspversietxt":#line:153
       O000OOO00O0OO000O =OOOOOOOO00OOOO000 .getHtml2 (O000O00O000OOOOOO )#line:154
       serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OOO00O00OO00O0OOO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O000OOO00O0OO000O )#line:155
    elif OO0O0000O0000O0OO =="uwspversietxtwiz":#line:156
         O000OOO00O0OO000O =OOOOOOOO00OOOO000 .getHtml2 (OO00O000000OO0OOO )#line:157
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OOO00O00OO00O0OOO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O000OOO00O0OO000O )#line:158
    elif OO0O0000O0000O0OO =="uwspversietxtrpi":#line:159
         O000OOO00O0OO000O =OOOOOOOO00OOOO000 .getHtml2 (O00O0OOOOO00O0OOO )#line:160
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OOO00O00OO00O0OOO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O000OOO00O0OO000O )#line:161
    addItem ('%s'%serviceinfotxt ,BASEURL ,'',OOOO00O000OOO0OO0 .path .join (mediaPath ,"wtf.png"))#line:162
    global buildinfotxt #line:163
    O000O0OO0O0000000 ,O00O000OOOO0OOO0O =O0O0O0O0O00OO00O0 .checkXvbmcversie ()#line:164
    if O000O0OO0O0000000 =="bldversietxt":#line:165
       O0000OO0OOOOO00OO =OOOOOOOO00OOOO000 .getHtml2 (O0O0OOO0000O0O00O )#line:166
       buildinfotxt ='[COLOR gray][B] - [/B]your system build: %s [/COLOR]'%(O00O000OOOO0OOO0O +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0000OO0OOOOO00OO )#line:167
    elif O000O0OO0O0000000 =="bldversietxtwiz":#line:168
         O0000OO0OOOOO00OO =OOOOOOOO00OOOO000 .getHtml2 (O00000O000O0O0O0O )#line:169
         buildinfotxt ='[COLOR gray][B] - [/B]your wizard build: %s [/COLOR]'%(O00O000OOOO0OOO0O +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0000OO0OOOOO00OO )#line:170
    addItem ('%s'%buildinfotxt ,BASEURL ,'',OOOO00O000OOO0OO0 .path .join (mediaPath ,"wtf.png"))#line:171
    if O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon("service.openelec.settings")')+O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:173
       addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:174
       addDir ('[COLOR orange]XvBMC Raspberry Pi [B] -[/B] Tools, DEV. & Maintenance[/COLOR]',BASEURL ,30 ,ART +'RPi.png',FANARTsub ,'')#line:175
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:177
    addItem (Terug ,BASEURL ,3 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:178
    O0O0O0O0O00OO00O0 .setView ('movies','EPiC')#line:179
def XvBMCmaint ():#line:181
    addItem ('[B]B[/B]uild [COLOR red]purge[/COLOR] [COLOR dimgray](build [B]c[/B]rap[B]c[/B]leaner & fix evil addons/repos)[/COLOR]',BASEURL ,21 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:182
    addItem ('[B]C[/B]lear cache',BASEURL ,22 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:183
    addItem ('[B]D[/B]elete thumbnails',BASEURL ,23 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:184
    addItem ('[B]F[/B]lush add-ons [COLOR dimgray](salts HD/RD lite & Exodus \'cache+temp\' files)[/COLOR]',BASEURL ,24 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:185
    addItem ('[B]F[/B]ull \"auto\" clean [COLOR dimgray](cache, crashlogs, packages & thumbnails)[/COLOR]',BASEURL ,25 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:186
    addItem ('[B]P[/B]urge packages',BASEURL ,26 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:187
    addItem ('[B]R[/B]efresh addons[COLOR white]+[/COLOR]repos',BASEURL ,27 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:188
    if int (OOOOOOOO00OOOO000 .kodiver )<=16.7 :#line:189
       addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s remove addons.db',BASEURL ,28 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:190
    elif int (OOOOOOOO00OOOO000 .kodiver )>16.7 :#line:191
         addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s enable all add-ons [COLOR dimgray](Kodi 17+ Krypton)[/COLOR]',BASEURL ,29 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:192
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:194
    addItem (About ,BASEURL ,2 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"wtf.png"))#line:195
    addItem (Terug ,BASEURL ,3 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:196
    O0O0O0O0O00OO00O0 .setView ('movies','EPiC')#line:197
def XvBMCtools1 ():#line:199
    addItem ('[B]C[/B]onvert physical paths (\'home\') to \'special\'',BASEURL ,11 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:200
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]most[/COLOR] add-ons)[/COLOR]',BASEURL ,12 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:201
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]all[/COLOR] add-ons)[/COLOR]',BASEURL ,13 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:202
    addItem ('[B]E[/B]nable Kodi Live Streams [COLOR dimgray](17+ Krypton; [COLOR white]RTMP[/COLOR])[/COLOR]',BASEURL ,14 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:203
    addItem ('[B]F[/B]orce close Kodi  [COLOR dimgray](Kill Kodi)[/COLOR]',BASEURL ,15 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:204
    addItem ('[B]L[/B]og viewer [COLOR dimgray](show \'kodi.log\')[/COLOR]',BASEURL ,17 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:206
    addItem ('[B]U[/B]RLResolver -> settings',BASEURL ,18 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:207
    addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s Advancedsettings unlocker [COLOR dimgray](reset)[/COLOR]',BASEURL ,19 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:208
    addDir ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s [COLOR white][B]H[/B]idden [B]g[/B]ems[B] & [/B][B]M[/B]ore [B]t[/B]ools[/COLOR] [COLOR dimgray](TiP[B]!![/B])[/COLOR]',BASEURL ,40 ,ART +'xvbmc.png',OOOO00O000OOO0OO0 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:209
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:211
    addItem (About ,BASEURL ,2 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"wtf.png"))#line:212
    addItem (Terug ,BASEURL ,3 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:213
    O0O0O0O0O00OO00O0 .setView ('movies','EPiC')#line:214
def XvBMCrpi ():#line:216
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] extreme crapcleaner [COLOR dimgray]([B]no[/B] factory reset)[/COLOR]',BASEURL ,31 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"tools.png"))#line:217
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] overclock [COLOR dimgray](raspberry Pi ***only***)[/COLOR]',BASEURL ,32 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"overclock.png"))#line:218
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] #dev# corner [COLOR dimgray](firmware, OS, etc.)[/COLOR]',BASEURL ,33 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"firmware.png"))#line:219
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:221
    addItem (About ,BASEURL ,2 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"wtf.png"))#line:222
    addItem (Terug ,BASEURL ,3 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:223
    O0O0O0O0O00OO00O0 .setView ('movies','EPiC')#line:224
def XvBMCtools2 ():#line:226
    addItem ('[B]K[/B]odi Quick Reset [COLOR dimgray](\"rejuvenate\" XvBMC-NL build)[/COLOR]',BASEURL ,41 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:228
    addItem ('[B]K[/B]odi Factory Reset [COLOR dimgray](complete Kodi Krypton wipe)[/COLOR]',BASEURL ,42 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:229
    addItem ('[B]K[/B]odi Fresh Start [COLOR dimgray](remove older Kodi\'s)[/COLOR]',BASEURL ,43 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:230
    addItem ('[B]P[/B]ush Fixes [COLOR dimgray](for XvBMC builds)[/COLOR]',BASEURL ,44 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:231
    addItem ('[B]P[/B]ush XvBMC REPOsitory [COLOR dimgray](install or fix repo)[/COLOR]',BASEURL ,45 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"maint.png"))#line:232
    if OOOO00O000OOO0OO0 .path .isfile (xxxCheck ):#line:233
       if O0O00O00OOOO0OO00 .getCondVisibility ('System.HasAddon("plugin.program.super.favourites")'):#line:234
          addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:235
          addItem ('[COLOR hotpink]activated: [/COLOR][COLOR pink]XvBMC\'s [B] [COLOR hotpink]x[COLOR deeppink]X[/COLOR]x[/COLOR] [/B] section ([COLOR hotpink]18[/COLOR][COLOR deeppink][B]+[/B][/COLOR])[/COLOR]',BASEURL ,69 ,xxxIcon )#line:236
       else :#line:237
           addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:238
           addItem ('[COLOR red]\'Super Favourites\' is missing, [COLOR lime][I]click here [/I][/COLOR] to (re-)install & enable [B]18+[/B][/COLOR]',BASEURL ,70 ,xxxIcon )#line:239
    else :#line:240
        addItem ('[B]P[/B]ush x[B]X[/B]x [COLOR dimgray](\"dirty\"-up your box with some 69 and mo\')[/COLOR]',BASEURL ,46 ,xxxIcon )#line:241
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:243
    addItem (About ,BASEURL ,2 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"wtf.png"))#line:244
    addItem (Terug ,BASEURL ,3 ,OOOO00O000OOO0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:245
    O0O0O0O0O00OO00O0 .setView ('movies','EPiC')#line:246
def wizard (name ,url ):#line:250
    O0O0O00OOO0OO0O00 =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/addons','packages'))#line:251
    if not OOOO00O000OOO0OO0 .path .exists (O0O0O00OOO0OO0O00 ):#line:252
        OOOO00O000OOO0OO0 .makedirs (O0O0O00OOO0OO0O00 )#line:253
    O0OO00OOO0OO000O0 =OOOO00O000OOO0OO0 .path .join (O0O0O00OOO0OO0O00 ,'default.zip')#line:254
    try :#line:255
       OOOO00O000OOO0OO0 .remove (O0OO00OOO0OO000O0 )#line:256
    except :#line:257
       pass #line:258
    O000OOOOOOO00OO0O .download (url ,O0OO00OOO0OO000O0 )#line:259
    if OOOO00O000OOO0OO0 .path .exists (O0OO00OOO0OO000O0 ):#line:261
        O00000OOO0O0OO0O0 =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://','home'))#line:262
        O00OO0OO00O0O00O0 .sleep (2 )#line:263
        dp .create (MainTitle ,'XvBMC-NL: pull update VoOdOo...','','Please Wait')#line:265
        dp .update (0 ,"","***Extract ZIP - Please Wait")#line:266
        O0O0O0O0O00OO00O0 .log ("==========================================================")#line:267
        O0O0O0O0O00OO00O0 .log (O00000OOO0O0OO0O0 )#line:268
        O0O0O0O0O00OO00O0 .log ("==========================================================")#line:269
        O000OOO000O00O0OO .all (O0OO00OOO0OO000O0 ,O00000OOO0O0OO0O0 ,dp )#line:270
        dp .close ()#line:271
        try :OOOO00O000OOO0OO0 .remove (O0OO00OOO0OO000O0 )#line:272
        except :pass #line:273
    if int (OOOOOOOO00OOOO000 .kodiver )<=16.7 :#line:274
       dialog .ok (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  HINT  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:275
       O0O0O0O0O00OO00O0 .forceRefresh (melding =False )#line:276
    elif int (OOOOOOOO00OOOO000 .kodiver )>16.7 :#line:277
         OOOOOOOO00OOOO000 .enableAddons (melding =False )#line:278
         O00OO0OO00O0O00O0 .sleep (0.5 )#line:279
         O0OO000O0000OO0OO =OOOO0OOO000O000OO .Dialog ().yesno (MainTitle +"[COLOR green][B] - success[/B][/COLOR]",' ','[B]IF[/B] add-ons do NOT work, you need to [B]reboot 1st[/B].','(een REBOOT van uw systeem is VEELAL wenselijk)',yeslabel ='[COLOR lime]Reboot[/COLOR]',nolabel ='[COLOR red]Continue[/COLOR]')#line:280
         if O0OO000O0000OO0OO ==1 :#line:281
            O00OO0OO00O0O00O0 .sleep (1 )#line:282
            O0O0O0O0O00OO00O0 .killKodi ()#line:283
         elif O0OO000O0000OO0OO ==0 :#line:284
              if int (OOOOOOOO00OOOO000 .kodiver )>16.7 :#line:285
                 OOOOOOOO00OOOO000 .enableAddons (melding =False )#line:286
                 O00OO0OO00O0O00O0 .sleep (0.5 )#line:287
                 dialog .ok (MainTitle +" : [COLOR red]add-ons[/COLOR] [COLOR green][B]enabled[/B][/COLOR]",'[COLOR orange][B]!!!  TIP  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:288
                 O0O00O00OOOO0OO00 .executebuiltin ('ReloadSkin()')#line:289
    O0O00O00OOOO0OO00 .executebuiltin ("Container.Refresh")#line:290
    O0O00O00OOOO0OO00 .sleep (5000 )#line:291
def fileexchange (url ,name ,locatie ):#line:295
    dp .create (MainTitle ,'XvBMC-NL: RPi update VoOdOo...','','Please Wait')#line:296
    if not OOOO00O000OOO0OO0 .path .exists (locatie ):OOOO00O000OOO0OO0 .makedirs (locatie )#line:297
    OO00OOO0OOOOOOOOO =OOOO00O000OOO0OO0 .path .join (locatie ,name )#line:298
    dp .update (0 ,'','.file.VoOdOo.')#line:299
    try :OOOO00O000OOO0OO0 .remove (OO00OOO0OOOOOOOOO )#line:300
    except :pass #line:301
    O000OOOOOOO00OO0O .download (url +name ,OO00OOO0OOOOOOOOO )#line:302
    O00OO0OO00O0O00O0 .sleep (1 )#line:303
    dp .close ()#line:304
    O0O00O00OOOO0OO00 .executebuiltin ("Container.Refresh")#line:306
    O0O00O00OOOO0OO00 .sleep (1000 )#line:307
def customwizard (name ,url ,storeLoc ,unzipLoc ):#line:309
    if not OOOO00O000OOO0OO0 .path .exists (storeLoc ):OOOO00O000OOO0OO0 .makedirs (storeLoc )#line:311
    O00O0O00OOO0OO00O =OOOO00O000OOO0OO0 .path .join (storeLoc ,name )#line:312
    try :OOOO00O000OOO0OO0 .remove (O00O0O00OOO0OO00O )#line:313
    except :pass #line:314
    O000OOOOOOO00OO0O .download (url +name ,O00O0O00OOO0OO00O )#line:315
    if OOOO00O000OOO0OO0 .path .exists (O00O0O00OOO0OO00O ):#line:317
       O00OO0OO00O0O00O0 .sleep (2 )#line:319
       dp .create (MainTitle ,'XvBMC-NL: just doing our VoOdOo...','','Please Wait')#line:320
       dp .update (0 ,'','***Mo\' XvBMC magic...')#line:321
       O0O0O0O0O00OO00O0 .log (str ('UNWiZ@'+unzipLoc ))#line:322
       O000OOO000O00O0OO .all (O00O0O00OOO0OO00O ,unzipLoc ,dp )#line:323
       dp .close ()#line:324
       try :OOOO00O000OOO0OO0 .remove (O00O0O00OOO0OO00O )#line:325
       except :pass #line:326
    if int (OOOOOOOO00OOOO000 .kodiver )<=16.7 :#line:327
       dialog .ok (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  HINT  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:328
       O0O0O0O0O00OO00O0 .forceRefresh (melding =False )#line:329
    elif int (OOOOOOOO00OOOO000 .kodiver )>16.7 :#line:330
         OOOOOOOO00OOOO000 .enableAddons (melding =False )#line:331
         O00OO0OO00O0O00O0 .sleep (0.5 )#line:332
         O00OO000OO0000O00 =OOOO0OOO000O000OO .Dialog ().yesno (MainTitle +"[COLOR green][B] - success[/B][/COLOR]",' ','[B]IF[/B] add-ons do NOT work, you need to [B]reboot 1st[/B].','(een REBOOT van uw systeem is VEELAL wenselijk)',yeslabel ='[COLOR lime]Reboot[/COLOR]',nolabel ='[COLOR red]Continue[/COLOR]')#line:333
         if O00OO000OO0000O00 ==1 :#line:334
            O00OO0OO00O0O00O0 .sleep (1 )#line:335
            O0O0O0O0O00OO00O0 .killKodi ()#line:336
         elif O00OO000OO0000O00 ==0 :#line:337
              if int (OOOOOOOO00OOOO000 .kodiver )>16.7 :#line:338
                 OOOOOOOO00OOOO000 .enableAddons (melding =False )#line:339
                 O00OO0OO00O0O00O0 .sleep (0.5 )#line:340
                 dialog .ok (MainTitle +" : [COLOR red]add-ons[/COLOR] [COLOR green][B]enabled[/B][/COLOR]",'[COLOR orange][B]!!!  TIP  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:341
                 O0O00O00OOOO0OO00 .executebuiltin ('ReloadSkin()')#line:342
    O0O00O00OOOO0OO00 .executebuiltin ("Container.Refresh")#line:343
    O0O00O00OOOO0OO00 .sleep (5000 )#line:344
def unlocker ():#line:347
    dialog .ok (MainTitle +" - unlocker",' ','unlock advancedsettings for this build','[COLOR dimgray](+reset \'advancedsettings.xml\' -use at your own risk)[/COLOR]')#line:349
    O00OO0O000O00O000 =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/userdata/'))#line:350
    OO000O000O000OO0O =OO000OO0O0O000O0O .b64decode ('YWR2YW5jZWRzZXR0aW5ncy54bWw=')#line:351
    O0OOOOOO0O000OO0O =True #line:352
    try :#line:353
        OOOO00O000OOO0OO0 .unlink (O00OO0O000O00O000 +OO000O000O000OO0O )#line:354
    except :#line:355
        O0OOOOOO0O000OO0O =False #line:356
    if O0OOOOOO0O000OO0O :#line:358
        dialog .ok (MainTitle +" - [B]UNLOCKED[/B]",'[COLOR green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Herstart[/B] Kodi ter afronding \'unlocker\' (force close)','[B]Reboot[/B] Kodi to complete \'unlocker\' (force close)')#line:359
        OOOO00O000OOO0OO0 ._exit (1 )#line:360
    else :#line:361
        dialog .ok (MainTitle +" - [B]OOOOOOPS[/B]",'[COLOR red][B]!!!  Failed  !!![/B][/COLOR]','[B]Nope![/B] helaas geen succes (niks te \'unlocken\')','[B]Nope![/B] close but no cigar  (nothing to \'unlock\')')#line:362
def XvbmcOc ():#line:365
    OOOO0OO0O0OOOO00O =O000OO00O00O00O00 ()#line:366
    O0O0O0O0O00OO00O0 .log ("Platform: "+str (OOOO0OO0O0OOOO00O ))#line:367
    if not OOOO0OO0O0OOOO00O =='linux':#line:368
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] OverClock!",O00O000OOO0O0O0O0 ,OOOOOOOOO0O0O0000 ,O00O00OO000OO00O0 )#line:369
       O0O0O0O0O00OO00O0 .log ("none Linux OS ie. Open-/LibreELEC")#line:370
    else :#line:371
        O0O0O0O0O00OO00O0 .log ("linux os")#line:372
        OOO000O00OO00OO0O .ocMenu ()#line:373
def XvbmcDev ():#line:376
    OO0O0O0OOOOOOOO00 =O000OO00O00O00O00 ()#line:377
    O0O0O0O0O00OO00O0 .log ("Platform: "+str (OO0O0O0OOOOOOOO00 ))#line:378
    if not OO0O0O0OOOOOOOO00 =='linux':#line:379
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] #dev#",O00O000OOO0O0O0O0 ,OOOOOOOOO0O0O0000 ,O00O00OO000OO00O0 )#line:380
       O0O0O0O0O00OO00O0 .log ("none Linux OS ie. Open-/LibreELEC")#line:381
    else :#line:382
        O0O0O0O0O00OO00O0 .log ("linux os")#line:383
        OO000O00OO00OOO00 .devMenu ()#line:384
def disabled ():#line:387
    O0O0O0O0O00OO00O0 .okDialog ('[COLOR red][B]Sorry, disabled! [/B](for now)[/COLOR]','','[COLOR lime]goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')#line:388
def rejuvXvbmc ():#line:391
    OO0OOOOOO0OOOOOOO =O0O0O0O0O00OO00O0 .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Wilt u uw XvBMC \'build\' volledig opschonen (wipe) en Kodi Krypton [B]leeg[/B] her-configureren?','[COLOR dimgray]Please confirm that you wish you wipe clean your current configuration and reconfigure Kodi.[/COLOR]')#line:392
    if OO0OOOOOO0OOOOOOO :#line:393
        O0O00000000O0O0OO =O0O00O0000OO0O0OO .Addon (id =AddonID ).getAddonInfo ('path');O0O00000000O0O0OO =O0O00O00OOOO0OO00 .translatePath (O0O00000000O0O0OO );#line:394
        OO0O00O00O000OO0O =OOOO00O000OOO0OO0 .path .join (O0O00000000O0O0OO ,"..","..");OO0O00O00O000OO0O =OOOO00O000OOO0OO0 .path .abspath (OO0O00O00O000OO0O );O0O0O0O0O00OO00O0 .log ("rejuvXvbmc.main_XvBMC: xbmcPath="+OO0O00O00O000OO0O );#line:395
        OOOO000O00O0OO0OO =('addons','Database','packages','userdata')#line:397
        OO0O000O000OO0O0O =('metadata.album.universal','metadata.artists.universal','metadata.common.imdb.com','metadata.common.musicbrainz.org','metadata.common.theaudiodb.com','metadata.common.themoviedb.org','metadata.themoviedb.org','metadata.tvdb.com','plugin.program.super.favourites','plugin.program.xvbmcinstaller.nl','repository.xvbmc','resource.language.nl_nl','script.xvbmc.updatertools','service.xbmc.versioncheck','skin.aeon.nox.spin','script.grab.fanart','service.library.data.provider','resource.images.recordlabels.white','resource.images.studios.coloured','resource.images.studios.white','xbmc.gui','script.skinshortcuts','script.module.simplejson','script.module.unidecode')#line:403
        OOOOO00O0OO0O0OOO =('Addons26.db','Addons27.db','guisettings.xml','kodi.log','Textures13.db')#line:405
        OO000O0OO0000O0OO =O0O0O0O0O00OO00O0 .message_yes_no ("[COLOR white][B]"+AddonTitle +"[/B][/COLOR]",'Wilt u het XvBMC-NL basis \'framework\' handhaven na reset? Verwijderd alles behalve XvBMC (aanbeveling).','[COLOR dimgray](do you wish to keep XvBMC\'s default framework?)[/COLOR]')#line:406
        if OO000O0OO0000O0OO :#line:407
            OOOO000O00O0OO0OO =OOOO000O00O0OO0OO +('addon_data','keymaps','media',)#line:408
            OO0O000O000OO0O0O =OO0O000O000OO0O0O +('inputstream.rtmp','keymaps','media','service.subtitles.addic7ed','service.subtitles.opensubtitles_by_opensubtitles','service.subtitles.opensubtitlesBeta','service.subtitles.podnapisi','service.subtitles.subscene',)#line:409
            OOOOO00O0OO0O0OOO =OOOOO00O0OO0O0OOO +('advancedsettings.xml','favourites.xml','profiles.xml','RssFeeds.xml','sources.xml','versiebld.txt','versiesp.txt','wizbld.txt','wizsp.txt',)#line:410
        else :#line:411
            OOOO000O00O0OO0OO =OOOO000O00O0OO0OO +('addon_data',)#line:412
            OO0O000O000OO0O0O =OO0O000O000OO0O0O +('inputstream.rtmp',)#line:413
            OOOOO00O0OO0O0OOO =OOOOO00O0OO0O0OOO +('advancedsettings.xml','RssFeeds.xml',)#line:414
            O00OO0OO0O0000OO0 =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join (USERADDONDATA ,'plugin.program.super.favourites','Super Favourites'))#line:415
            O00OOOOOO0O0000OO =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join (USERDATA ,'addon_data','script.skinshortcuts'))#line:416
            try :#line:417
                OO00OOOO0OO0OO00O .rmtree (O00OO0OO0O0000OO0 )#line:418
            except Exception as OOOOO00OO00O00O00 :O0O0O0O0O00OO00O0 .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (OOOOO00OO00O00O00 ))#line:419
            try :#line:420
                OO00OOOO0OO0OO00O .rmtree (O00OOOOOO0O0000OO )#line:421
            except Exception as OOOOO00OO00O00O00 :O0O0O0O0O00OO00O0 .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (OOOOO00OO00O00O00 ))#line:422
        dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Snelle XvBMC Krypton reset, even geduld...','','[COLOR dimgray](Quick XvBMC Krypton reset, please wait...)[/COLOR]')#line:423
        try :#line:424
            for O0O00OO00OO0O0000 ,OOO0O0000O0000O00 ,OOOOO00OOO0OO0OOO in OOOO00O000OOO0OO0 .walk (OO0O00O00O000OO0O ,topdown =True ):#line:425
                OOO0O0000O0000O00 [:]=[OOO00OOO0OOO000O0 for OOO00OOO0OOO000O0 in OOO0O0000O0000O00 if OOO00OOO0OOO000O0 not in OO0O000O000OO0O0O ]#line:426
                OOOOO00OOO0OO0OOO [:]=[O00OO00O000O000O0 for O00OO00O000O000O0 in OOOOO00OOO0OO0OOO if O00OO00O000O000O0 not in OOOOO00O0OO0O0OOO ]#line:427
                for OO000OO00OO0OO00O in OOOOO00OOO0OO0OOO :#line:428
                    try :#line:429
                        dp .update (11 ,'','***Cleaning files...')#line:430
                        OOOO00O000OOO0OO0 .remove (OOOO00O000OOO0OO0 .path .join (O0O00OO00OO0O0000 ,OO000OO00OO0OO00O ))#line:431
                    except Exception as OOOOO00OO00O00O00 :O0O0O0O0O00OO00O0 .log ("rejuvXvbmc.file_name: User files partially removed - "+str (OOOOO00OO00O00O00 ))#line:433
                for O0000000OO000O00O in OOO0O0000O0000O00 :#line:434
                    if O0000000OO000O00O not in OOOO000O00O0OO0OO :#line:435
                        try :#line:436
                            dp .update (33 ,'','***Cleaning folders...')#line:437
                            OO00OOOO0OO0OO00O .rmtree (OOOO00O000OOO0OO0 .path .join (O0O00OO00OO0O0000 ,O0000000OO000O00O ))#line:438
                        except Exception as OOOOO00OO00O00O00 :O0O0O0O0O00OO00O0 .log ("rejuvXvbmc.folder: User folders partially removed - "+str (OOOOO00OO00O00O00 ))#line:440
            dp .update (66 ,'','***Crap Cleaning...')#line:441
            O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ()#line:442
        except Exception as OOOOO00OO00O00O00 :#line:443
            O0O0O0O0O00OO00O0 .log ("rejuvXvbmc: User stuff partially removed - "+str (OOOOO00OO00O00O00 ))#line:444
            O0O0O0O0O00OO00O0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Error![/B][/COLOR]",'...DAT ging niet helemaal goed, controleer uw log...','[COLOR dimgray](XvBMC user files partially removed, please check log)[/COLOR]')#line:445
            O0O0OOO00O0OOOOO0 .exit ()#line:446
        dp .update (99 ,'','***Cleaning Crap...')#line:447
        O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:448
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:449
        OOOO00O000OOO0OO0 ._exit (1 )#line:450
    else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:451
def WipeXBMC ():#line:454
    if skin !="skin.estuary":#line:455
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'selecteer eerst de standaard (Estuary) skin alvorens een volledige [B]\'wipe\'[/B] van uw Kodi uit te voeren.','','[COLOR dimgray](before Kodi wipe, select Estuary skin first)[/COLOR]')#line:456
        O0O00O00OOOO0OO00 .executebuiltin ("ActivateWindow(InterfaceSettings)")#line:457
        return #line:458
    else :#line:459
        O00OO0OOO00O0O0O0 =OOOO0OOO000O000OO .Dialog ().yesno ("[COLOR lime][B]BELANGRIJK / IMPORTANT / HINT[/B][/COLOR]",'[B]let op: [/B]dit zal alles verwijderen van uw huidige Kodi installatie, weet u zeker dat u wilt doorgaan[B]?[/B]','','[COLOR dimgray](this will remove your current Kodi build, continue?)[/COLOR]',yeslabel ='[COLOR lime][B]JA/YES[/B][/COLOR]',nolabel ='[COLOR red]nee/nope[/COLOR]')#line:460
        if O00OO0OOO00O0O0O0 ==1 :#line:461
           dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'verwijder alles, even geduld...','','[COLOR dimgray](remove everything, please wait...)[/COLOR]')#line:462
           try :#line:463
               for O0000OOO0O00OOO0O ,OO0O0O0OO000O00O0 ,OOO00000O0OOO0O0O in OOOO00O000OOO0OO0 .walk (HOME ,topdown =True ):#line:464
                    OO0O0O0OO000O00O0 [:]=[O000O0OO000O0O0O0 for O000O0OO000O0O0O0 in OO0O0O0OO000O00O0 if O000O0OO000O0O0O0 not in EXCLUDES ]#line:465
                    for OOOO00OO00O0O0O00 in OOO00000O0OOO0O0O :#line:466
                        try :dp .update (11 ,'','***Cleaning files...');OOOO00O000OOO0OO0 .remove (OOOO00O000OOO0OO0 .path .join (O0000OOO0O00OOO0O ,OOOO00OO00O0O0O00 ));OOOO00O000OOO0OO0 .rmdir (OOOO00O000OOO0OO0 .path .join (O0000OOO0O00OOO0O ,OOOO00OO00O0O0O00 ))#line:467
                        except :pass #line:468
                    for OOOO00OO00O0O0O00 in OO0O0O0OO000O00O0 :#line:469
                        try :dp .update (33 ,'','***Cleaning folders...');OOOO00O000OOO0OO0 .rmdir (OOOO00O000OOO0OO0 .path .join (O0000OOO0O00OOO0O ,OOOO00OO00O0O0O00 ));OOOO00O000OOO0OO0 .rmdir (O0000OOO0O00OOO0O )#line:470
                        except :pass #line:471
               dp .update (66 ,'','***Crap Cleaning...')#line:472
               O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ()#line:473
           except :pass #line:474
           dp .update (99 ,'','***Cleaning Crap...')#line:475
           O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:476
           dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'Kodi zal nu afsluiten...','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:477
           OOOO00O000OOO0OO0 ._exit (1 )#line:478
        elif O00OO0OOO00O0O0O0 ==0 :#line:479
             dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen Kodi Krypton \'wipe\' uitgevoerd...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:480
def FRESHSTART (params ):#line:483
    if int (OOOOOOOO00OOOO000 .kodiver )>16.7 :#line:484
       dialog .ok ("[COLOR lime]"+MainTitle +"[/COLOR] [COLOR red][B]- NOPE![/B][/COLOR]",'[COLOR orange][B]NOTE:[/B][/COLOR]','[COLOR white]alleen voor oudere Kodi\'s dan Krypton (>17.0)[/COLOR]','[COLOR dimgray](for use with older Kodi\'s only (>17.0)[/COLOR]')#line:485
    else :#line:486
        O0O0O0O0O00OO00O0 .log ("freshstart.main_XvBMC: "+repr (params ));O00O0000OOOO0OOOO =O0O0O0O0O00OO00O0 .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Remove[/B][/COLOR]",'Kodi terugzetten naar de standaard fabrieksinstellingen?','[COLOR dimgray](reset Kodi to factory defaults)[/COLOR]')#line:487
        if O00O0000OOOO0OOOO :#line:488
            O0O0OOOOO0O0OO0O0 =O0O00O0000OO0O0OO .Addon (id =AddonID ).getAddonInfo ('path');O0O0OOOOO0O0OO0O0 =O0O00O00OOOO0OO00 .translatePath (O0O0OOOOO0O0OO0O0 );#line:489
            O00OO0000O0O0OO0O =OOOO00O000OOO0OO0 .path .join (O0O0OOOOO0O0OO0O0 ,"..","..");O00OO0000O0O0OO0O =OOOO00O000OOO0OO0 .path .abspath (O00OO0000O0O0OO0O );O0O0O0O0O00OO00O0 .log ("freshstart.main_XvBMC: xbmcPath="+O00OO0000O0O0OO0O );OO0O0O000O0OO00O0 =False #line:490
            dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- FreshStart![/B][/COLOR]",'terug naar fabrieksinstellingen, even geduld...','','[COLOR dimgray](factory reset Kodi, please wait...)[/COLOR]')#line:491
            try :#line:492
                for OOOOOOOO00O000OOO ,O0O0O0OOO00OOOO0O ,OO0000OOOOOO0O00O in OOOO00O000OOO0OO0 .walk (O00OO0000O0O0OO0O ,topdown =True ):#line:493
                    O0O0O0OOO00OOOO0O [:]=[OO00O0000OO000O00 for OO00O0000OO000O00 in O0O0O0OOO00OOOO0O if OO00O0000OO000O00 not in EXCLUDES ]#line:494
                    dp .update (33 ,'','***Cleaning files+folders...')#line:495
                    for OOOOO000O00OO00OO in OO0000OOOOOO0O00O :#line:496
                        try :OOOO00O000OOO0OO0 .remove (OOOO00O000OOO0OO0 .path .join (OOOOOOOO00O000OOO ,OOOOO000O00OO00OO ))#line:497
                        except :#line:498
                            if OOOOO000O00OO00OO not in ["Addons1.db","MyMusic7","MyVideos37.db","Textures1.db","xbmc.log"]:OO0O0O000O0OO00O0 =True #line:499
                            O0O0O0O0O00OO00O0 .log ("XvBMC-Error removing file: "+OOOOOOOO00O000OOO +" "+OOOOO000O00OO00OO )#line:500
                    for OOOOO000O00OO00OO in O0O0O0OOO00OOOO0O :#line:501
                        try :OOOO00O000OOO0OO0 .rmdir (OOOO00O000OOO0OO0 .path .join (OOOOOOOO00O000OOO ,OOOOO000O00OO00OO ))#line:502
                        except :#line:503
                            if OOOOO000O00OO00OO not in ["Database","userdata"]:OO0O0O000O0OO00O0 =True #line:504
                            O0O0O0O0O00OO00O0 .log ("XvBMC-Error removing folder: "+OOOOOOOO00O000OOO +" "+OOOOO000O00OO00OO )#line:505
                dp .update (66 ,'','***Crap Cleaning...')#line:506
                O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ()#line:507
                if not OO0O0O000O0OO00O0 :O0O0O0O0O00OO00O0 .log ("freshstart.main_XvBMC: All user files removed, you now have a CLEAN install");O0O0O0O0O00OO00O0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:508
                else :O0O0O0O0O00OO00O0 .log ("freshstart.main_XvBMC: User files partially removed");O0O0O0O0O00OO00O0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:509
            except :O0O0O0O0O00OO00O0 .message ("[COLOR red][B]"+AddonTitle +"[/B][/COLOR]",'Problem found','Your settings have [B]not[/B] been changed');import traceback as OO00OOO0O0OOO00O0 ;O0O0O0O0O00OO00O0 .log (OO00OOO0O0OOO00O0 .format_exc ());O0O0O0O0O00OO00O0 .log ("freshstart.main_XvBMC: NOTHING removed");O0O0OOO00O0OOOOO0 .exit ()#line:510
            dp .update (99 ,'','***Cleaning Crap...')#line:511
            O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();O0O0O0O0O00OO00O0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:512
            dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:513
            OOOO00O000OOO0OO0 ._exit (1 )#line:514
        else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:515
def addItem (name ,url ,mode ,iconimage ):#line:519
    O000O00000O00OO00 =O0O0OOO00O0OOOOO0 .argv [0 ]+"?url="+OO0O0O0O00OO00O0O .quote_plus (url )+"&mode="+str (mode )+"&name="+OO0O0O0O00OO00O0O .quote_plus (name )#line:520
    O0OOO0O0000000OO0 =True #line:521
    OOOOOOO000OOOO0OO =OOOO0OOO000O000OO .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:522
    OOOOOOO000OOOO0OO .setInfo (type ="Video",infoLabels ={"Title":name })#line:523
    OOOOOOO000OOOO0OO .setArt ({'fanart':FANART })#line:524
    O0OOO0O0000000OO0 =OOOO0OOO00000O00O .addDirectoryItem (handle =int (O0O0OOO00O0OOOOO0 .argv [1 ]),url =O000O00000O00OO00 ,listitem =OOOOOOO000OOOO0OO ,isFolder =False )#line:525
    return O0OOO0O0000000OO0 #line:526
def get_params ():#line:529
        OO0OOOOO00O000000 =[]#line:530
        OO00000O000O00OOO =O0O0OOO00O0OOOOO0 .argv [2 ]#line:531
        if len (OO00000O000O00OOO )>=2 :#line:532
                OO0000O000O000000 =O0O0OOO00O0OOOOO0 .argv [2 ]#line:533
                O0OO0OOOOO000000O =OO0000O000O000000 .replace ('?','')#line:534
                if (OO0000O000O000000 [len (OO0000O000O000000 )-1 ]=='/'):#line:535
                        OO0000O000O000000 =OO0000O000O000000 [0 :len (OO0000O000O000000 )-2 ]#line:536
                O0000000O0OO0OOOO =O0OO0OOOOO000000O .split ('&')#line:537
                OO0OOOOO00O000000 ={}#line:538
                for O0O0O00000000000O in range (len (O0000000O0OO0OOOO )):#line:539
                        O00O0OO0OO00OO0O0 ={}#line:540
                        O00O0OO0OO00OO0O0 =O0000000O0OO0OOOO [O0O0O00000000000O ].split ('=')#line:541
                        if (len (O00O0OO0OO00OO0O0 ))==2 :#line:542
                                OO0OOOOO00O000000 [O00O0OO0OO00OO0O0 [0 ]]=O00O0OO0OO00OO0O0 [1 ]#line:543
        return OO0OOOOO00O000000 #line:544
def addDir (name ,url ,mode ,iconimage ,fanart ,description ):#line:547
        O0O000OOOO00OO0OO =O0O0OOO00O0OOOOO0 .argv [0 ]+"?url="+OO0O0O0O00OO00O0O .quote_plus (url )+"&mode="+str (mode )+"&name="+OO0O0O0O00OO00O0O .quote_plus (name )+"&iconimage="+OO0O0O0O00OO00O0O .quote_plus (iconimage )+"&fanart="+OO0O0O0O00OO00O0O .quote_plus (fanart )+"&description="+OO0O0O0O00OO00O0O .quote_plus (description )#line:548
        O00OO0O000O00O0O0 =True #line:549
        O0O0OO00OO00OOO0O =OOOO0OOO000O000OO .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:550
        O0O0OO00OO00OOO0O .setInfo (type ="Video",infoLabels ={"Title":name ,"Plot":description })#line:551
        O0O0OO00OO00OOO0O .setProperty ("Fanart_Image",fanart )#line:552
        if mode ==1 :#line:553
            O00OO0O000O00O0O0 =OOOO0OOO00000O00O .addDirectoryItem (handle =int (O0O0OOO00O0OOOOO0 .argv [1 ]),url =O0O000OOOO00OO0OO ,listitem =O0O0OO00OO00OOO0O ,isFolder =False )#line:554
        elif mode ==2 :#line:555
            O00OO0O000O00O0O0 =OOOO0OOO00000O00O .addDirectoryItem (handle =int (O0O0OOO00O0OOOOO0 .argv [1 ]),url =O0O000OOOO00OO0OO ,listitem =O0O0OO00OO00OOO0O ,isFolder =False )#line:556
        elif mode ==100 :#line:557
            O00OO0O000O00O0O0 =OOOO0OOO00000O00O .addDirectoryItem (handle =int (O0O0OOO00O0OOOOO0 .argv [1 ]),url =O0O000OOOO00OO0OO ,listitem =O0O0OO00OO00OOO0O ,isFolder =False )#line:558
        else :#line:559
            O00OO0O000O00O0O0 =OOOO0OOO00000O00O .addDirectoryItem (handle =int (O0O0OOO00O0OOOOO0 .argv [1 ]),url =O0O000OOOO00OO0OO ,listitem =O0O0OO00OO00OOO0O ,isFolder =True )#line:560
        return O00OO0O000O00O0O0 #line:561
params =get_params ()#line:564
url =None #line:565
name =None #line:566
mode =None #line:567
iconimage =None #line:568
fanart =None #line:569
description =None #line:570
try :#line:573
        url =OO0O0O0O00OO00O0O .unquote_plus (params ["url"])#line:574
except :#line:575
        pass #line:576
try :#line:577
        name =OO0O0O0O00OO00O0O .unquote_plus (params ["name"])#line:578
except :#line:579
        pass #line:580
try :#line:581
        iconimage =OO0O0O0O00OO00O0O .unquote_plus (params ["iconimage"])#line:582
except :#line:583
        pass #line:584
try :#line:585
        mode =int (params ["mode"])#line:586
except :#line:587
        pass #line:588
try :#line:589
        fanart =OO0O0O0O00OO00O0O .unquote_plus (params ["fanart"])#line:590
except :#line:591
        pass #line:592
try :#line:593
        description =OO0O0O0O00OO00O0O .unquote_plus (params ["description"])#line:594
except :#line:595
        pass #line:596
O0O0O0O0O00OO00O0 .log ("EPiC "+str (AddonTitle ))#line:600
if mode ==None or url ==None or len (url )<1 :#line:608
   mainMenu ()#line:609
elif mode ==1 :#line:611
     wizard (name ,url )#line:613
elif mode ==10 :#line:615
     XvBMCtools1 ()#line:616
elif mode ==20 :#line:618
     XvBMCmaint ()#line:619
elif mode ==30 :#line:621
     XvBMCrpi ()#line:622
elif mode ==2 :#line:624
     O0O0O0O0O00OO00O0 .AboutXvBMC ()#line:625
elif mode ==3 :#line:627
     O0O0O0O0O00OO00O0 .closeandexit ()#line:628
elif mode ==4 :#line:630
     O0O0O0O0O00OO00O0 .okDialog (O00O000OOO0O0O0O0 ,'sorry, nothing todo...','with kind regards, team [COLOR green]XvBMC Nederland[/COLOR]')#line:631
elif mode ==11 :#line:633
     OO0OO00O00O000OOO .Fix_Special (url )#line:634
elif mode ==12 :#line:636
     OO0OO00O00O000OOO .AddonsEnable ()#line:637
elif mode ==13 :#line:639
     OO0OO0000O0O000O0 .setall_enable ()#line:640
elif mode ==14 :#line:642
     OO0OO00O00O000OOO .EnableRTMP ()#line:643
elif mode ==15 :#line:645
     O0O0O0O0O00OO00O0 .killKodi ()#line:646
elif mode ==16 :#line:648
     O0O0O0O0O00OO00O0 .KODIVERSION (url )#line:649
elif mode ==17 :#line:651
     OO0OO00O00O000OOO .xvbmcLog ()#line:652
elif mode ==18 :#line:654
     resolver_settings ()#line:655
elif mode ==19 :#line:657
     unlocker ()#line:658
elif mode ==21 :#line:660
     O00OO0OOOO0OOO0OO .purgeOLD ()#line:661
elif mode ==22 :#line:663
     OO0OO00O00O000OOO .clearCache ()#line:664
elif mode ==23 :#line:666
     OO0OO00O00O000OOO .deleteThumbnails ()#line:667
elif mode ==24 :#line:669
     OOO0O00O0OOO0O00O .flushMenu ()#line:670
elif mode ==25 :#line:672
     OO0OO00O00O000OOO .autocleanask ()#line:673
elif mode ==26 :#line:675
     OO0OO00O00O000OOO .purgePackages ()#line:676
elif mode ==27 :#line:678
     O0O0O0O0O00OO00O0 .forceRefresh (melding =True )#line:679
elif mode ==28 :#line:681
     OO0OO00O00O000OOO .AddonsDatabaseRemoval ()#line:682
elif mode ==29 :#line:684
     OOOOOOOO00OOOO000 .enableAddons (melding =True )#line:685
elif mode ==31 :#line:687
     OO0OO00O00O000OOO .PiCCleaner ()#line:688
elif mode ==32 :#line:690
     XvbmcOc ()#line:691
elif mode ==33 :#line:693
     XvbmcDev ()#line:694
elif mode ==40 :#line:696
     XvBMCtools2 ()#line:697
elif mode ==41 :#line:699
     rejuvXvbmc ()#line:700
elif mode ==42 :#line:702
     WipeXBMC ()#line:703
elif mode ==43 :#line:705
     FRESHSTART (params )#line:706
elif mode ==44 :#line:708
     disabled ()#line:709
elif mode ==45 :#line:711
     name ='repository.xvbmc-4.1.0.zip'#line:712
     url =OO000OO0O0O000O0O .b64decode (OO00O00O000OOOO00 )#line:713
     storeLoc =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/addons','packages'))#line:714
     unzipLoc =OOOO00O000OOO0OO0 .path .join (HOME ,'addons')#line:715
     customwizard (name ,url ,storeLoc ,unzipLoc )#line:717
elif mode ==46 :#line:719
     url =OO000OO0O0O000O0O .b64decode (OO00O0OO00OOO0OOO )+'triple-x/xXxvbmc.zip'#line:720
     wizard (name ,url )#line:722
elif mode ==69 :#line:723
     O0O00O00OOOO0OO00 .executebuiltin ('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?folder=xXx",return)')#line:724
elif mode ==70 :#line:725
     name ='plugin.program.super.favourites-1.0.59.zip'#line:726
     url =OO000OO0O0O000O0O .b64decode (OO00O0OO00OOO0OOO )+'plugin.program.super.favourites/'#line:727
     storeLoc =O0O00O00OOOO0OO00 .translatePath (OOOO00O000OOO0OO0 .path .join ('special://home/addons','packages'))#line:728
     unzipLoc =OOOO00O000OOO0OO0 .path .join (HOME ,'addons')#line:729
     customwizard (name ,url ,storeLoc ,unzipLoc )#line:731
elif mode ==100 :#line:733
     locatie =USERDATA #line:734
     name ='rpi-service'#line:735
     fileexchange (url ,name +'.txt',locatie )#line:737
     wizard (name ,url +name +'.zip')#line:739
"""
    IF you copy/paste XvBMC's -default.py- please keep the credits -2- XvBMC-NL, Thx.
"""#line:743
OOOO0OOO00000O00O .endOfDirectory (int (O0O0OOO00O0OOOOO0 .argv [1 ]))
