#!/usr/bin/python
""#line:6
import re as OOO0OO00OOOO0O000 ,base64 as OO0O0OO00OOO0OOOO ,urllib as O0000OO00OOOOOOO0 ,urllib2 as OOO0O0OOOOO00OOOO ,sys as O0O0000OO0O000OOO ,xbmcvfs as OOO0OO0OO0O000OOO #line:25
import xbmc as OOO00O0O00000O0OO ,xbmcaddon as O0OOOOO000O00000O ,xbmcgui as O00O0O00OO0OO0O0O ,xbmcplugin as O0O0O0000000OOOOO #line:26
import os as OO0OO0000O000O000 ,shutil as OO0OO0000OOO0O0OO ,time as OOOO00OO0OO0OOOO0 #line:27
import sqlite3 as O0O000000OOO00OOO #line:28
import utils as O0000OO0O0O0OOOOO #line:29
from resources .lib import addon_able as O0O0O0O0000OO00OO #line:32
from resources .lib import downloader as OO0OO000OO00OOO00 ,extract as OO000OOOO0OO0OO00 #line:33
from resources .lib import common as O0OO00O0O00OOOOO0 #line:34
from resources .lib .common import platform as O0000O0O000OO0000 ,subtitleNope as O000O0O0OO0O000O0 ,nonlinux as O0000O0000OO00OO0 ,nonelecNL as OOO0O000OO000OOOO #line:35
from resources .lib .common import base as OOOO0OO0OOO0OO0OO ,basewiz as OO00OO0OOOO000O0O ,currentbldtxt as OOOO0OO0OO0OOOOOO ,currentsptxt as O0OO0OOOOO00000O0 ,currentbldtxtwiz as OOO00O0OOO0OO0O0O ,currentsptxtwiz as O0OOO0O0O0O000OOO ,currentsptxtrpi as O0000O00O00OOO0OO ,repos as O0OO000000OOOO0OO #line:36
from resources .lib import flush as OO0O0O00O0OOOOO00 #line:38
from resources .lib import huisvrouw as O00OO0O00OOOOOO0O #line:39
from resources .lib import purge as OO0OOO00000OOOOO0 #line:40
from resources .lib import rpioc as O00OOO0OO0OO0O000 #line:41
from resources .lib import rpidev as OO000O00OO00OOOOO #line:42
ADDON =O0000OO0O0O0OOOOO .ADDON #line:44
ADDON_ID =O0OOOOO000O00000O .Addon ().getAddonInfo ('id')#line:46
AddonID ='script.xvbmc.updatertools'#line:47
AddonTitle ='XvBMC Nederland'#line:48
addonPath =OO0OO0000O000O000 .path .join (OO0OO0000O000O000 .path .join (OOO00O0O00000O0OO .translatePath ('special://home'),'addons'),'script.xvbmc.updatertools')#line:49
ART =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/addons/'+AddonID +'/resources/media/'))#line:50
artwork =OO0O0OO00OOO0OOOO .b64decode ('c2tpbi5hZW9uLm5veC5zcGlu')#line:51
FANART =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/addons/'+AddonID ,'fanart.jpg'))#line:52
FANARTsub =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/addons/'+AddonID +'/resources/media/','art.jpg'))#line:53
ICON =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/addons/'+AddonID ,'icon.png'))#line:54
MainTitle ="XvBMC Nederland"#line:55
mediaPath =OO0OO0000O000O000 .path .join (addonPath ,'resources/media')#line:56
U =ADDON .getSetting ('User')#line:57
USER_AGENT ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'#line:58
About ='[COLOR dimgray][B]X[/B]v[B]BMC[/B] disclaimer & usage policy[/COLOR]'#line:60
Terug ='[COLOR dimgray]<<<back[/COLOR]'#line:61
dialog =O00O0O00OO0OO0O0O .Dialog ()#line:63
dp =O00O0O00OO0OO0O0O .DialogProgress ()#line:64
BASEURL ="https://bit.ly/XvBMC-Pi"#line:65
buildinfotxt ='[COLOR gray][B] - [/B]your XvBMC build: [I]unknown[/I] [/COLOR]'#line:66
serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: [I]unknown[/I] [/COLOR]'#line:67
xbmcver =OOO00O0O00000O0OO .getInfoLabel ("System.BuildVersion")[:4 ]#line:68
EXCLUDES =[ADDON_ID ,'plugin.program.xvbmcinstaller.nl','repository.xvbmc']#line:70
HOME =OOO00O0O00000O0OO .translatePath ('special://home/')#line:71
skin =OOO00O0O00000O0OO .getSkinDir ()#line:72
USERDATA =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/userdata',''))#line:73
USERADDONDATA =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/userdata/addon_data',''))#line:74
xxxCheck =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join (USERADDONDATA ,'plugin.program.super.favourites','Super Favourites','xXx','favourites.xml'))#line:75
xxxIcon =OO0O0OO00OOO0OOOO .b64decode ('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMvdHJpcGxlLXgvYWR1bHQucG5n')#line:76
def resolver_settings ():#line:80
    import urlresolver as OO0O00OOOOOO00O0O #line:81
    OO0O00OOOOOO00O0O .display_settings ()#line:82
def mainMenu ():#line:85
    O00O0O0OOO0O0OO0O ,OOOOOOOOOO0000O0O =O0000OO0O0O0OOOOO .checkUpdate ()#line:87
    if O00O0O0OOO0O0OO0O =="update":#line:89
       OO0O000OO0O00O0O0 ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(OOOOOOOOOO0000O0O )+'[COLOR orange] (fork)[/COLOR]'#line:90
       O0O0O000O000000OO =OO0O0OO00OOO0OOOO .b64decode (OOOO0OO0OOO0OO0OO )+'update/sp/servicepack.zip'#line:91
       addDir ('%s'%OO0O000OO0O00O0O0 ,O0O0O000O000000OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:93
    elif O00O0O0OOO0O0OO0O =="wizupdate":#line:94
       OO0O000OO0O00O0O0 ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(OOOOOOOOOO0000O0O )+'[COLOR orange] (wizard)[/COLOR]'#line:95
       O0O0O000O000000OO =OO0O0OO00OOO0OOOO .b64decode (OO00OO0OOOO000O0O )+'wizardsp.zip'#line:96
       addDir ('%s'%OO0O000OO0O00O0O0 ,O0O0O000O000000OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:98
    elif O00O0O0OOO0O0OO0O =="rpiupdate":#line:99
       OO0O000OO0O00O0O0 ="[COLOR orange]XvBMC RPi update available[B]: %s[/B][/COLOR]"%(OOOOOOOOOO0000O0O )+'[COLOR orange] (forced)[/COLOR]'#line:100
       OO00OOOO0O00OO0OO =OO0O0OO00OOO0OOOO .b64decode (OOOO0OO0OOO0OO0OO )+'update/sp/'#line:101
       addDir ('%s'%OO0O000OO0O00O0O0 ,OO00OOOO0O00OO0OO ,100 ,ART +'xvbmc.png',FANART ,'')#line:103
    elif O00O0O0OOO0O0OO0O =="notinstalled":#line:107
       if OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon(%s)'%(artwork )):#line:108
          if OO0OO0000O000O000 .path .isfile (O0OO00O0O00OOOOO0 .bldversietxt ):#line:109
             OO0O000OO0O00O0O0 ="[COLOR orange]Sorry (portable) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:110
             O0O0O000O000000OO =OO0O0OO00OOO0OOOO .b64decode (OOOO0OO0OOO0OO0OO )+'update/sp/servicepack.zip'#line:111
             addDir ('%s'%OO0O000OO0O00O0O0 ,O0O0O000O000000OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:113
          elif OO0OO0000O000O000 .path .isfile (O0OO00O0O00OOOOO0 .bldversietxtwiz ):#line:114
               OO0O000OO0O00O0O0 ="[COLOR orange]Sorry (wizard) update status [B]unknown[/B], attempt to continue anyway[B]?[/B][/COLOR]"#line:115
               O0O0O000O000000OO =OO0O0OO00OOO0OOOO .b64decode (OO00OO0OOOO000O0O )+'wizardsp.zip'#line:116
               addDir ('%s'%OO0O000OO0O00O0O0 ,O0O0O000O000000OO ,1 ,ART +'xvbmc.png',FANART ,'')#line:118
          elif OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon("service.openelec.settings")')+OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:120
               OO0O000OO0O00O0O0 ="[COLOR orange]unknown [B]RPi[/B] version; force update[B]?[/B][/COLOR] [COLOR lime] (continue?)[/COLOR]"#line:121
               OO00OOOO0O00OO0OO =OO0O0OO00OOO0OOOO .b64decode (OOOO0OO0OOO0OO0OO )+'update/sp/'#line:122
               addDir ('%s'%OO0O000OO0O00O0O0 ,OO00OOOO0O00OO0OO ,100 ,ART +'xvbmc.png',FANART ,'')#line:124
          else :#line:125
               OO0O000OO0O00O0O0 ="[COLOR orange]unknown build status; force update?[/COLOR] [COLOR red][B](continue at your own risk)[/B][/COLOR]"#line:126
               O00O0OOOO0OO0O0O0 =OO0O0OO00OOO0OOOO .b64decode (OOOO0OO0OOO0OO0OO )+'update/sp/servicepack.zip'#line:127
               addDir ('%s'%OO0O000OO0O00O0O0 ,O00O0OOOO0OO0O0O0 ,1 ,ART +'xvbmc.png',FANART ,'')#line:129
       else :#line:130
          OO0O000OO0O00O0O0 ="[COLOR orange]Sorry, [B]unknown[/B] build/servicepack/update status [B] :[/B]\'-([/COLOR]"#line:131
          addItem ('%s'%OO0O000OO0O00O0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:132
    elif O00O0O0OOO0O0OO0O =="noupdaterpi":#line:133
         if OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon("service.openelec.settings")')+OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:135
            OO0O000OO0O00O0O0 ="[COLOR orange]You have the [B]latest[/B] [COLOR red]XvBMC[/COLOR] [COLOR lime][B]RPi[/B][/COLOR] forced updates [B] 3:[/B]-)[/COLOR]"#line:136
            addItem ('%s'%OO0O000OO0O00O0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:137
         else :#line:138
            OO0O000OO0O00O0O0 ="[COLOR orange]You [B]somehow[/B] have the latest [COLOR lime]XvBMC[/COLOR] [COLOR red][B]RPi[/B][/COLOR] forced updates [B]???[/B][/COLOR]"#line:139
            addItem ('%s'%OO0O000OO0O00O0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:140
    else :#line:141
       OO0O000OO0O00O0O0 ="[COLOR orange]You have the [B]latest[/B] XvBMC updates [B] :[/B]-)[/COLOR]"#line:142
       addItem ('%s'%OO0O000OO0O00O0O0 ,BASEURL ,4 ,ART +'xvbmc.png')#line:143
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:145
    addDir ('[COLOR red]XvBMC Tools[/COLOR]',BASEURL ,10 ,ART +'tools.png',OO0OO0000O000O000 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:146
    addDir ('[COLOR white]XvBMC Maintenance[/COLOR]',BASEURL ,20 ,ART +'maint.png',OO0OO0000O000O000 .path .join (mediaPath ,"onderhoud.jpg"),'')#line:147
    addDir ('[COLOR dodgerblue]XvBMC About[/COLOR]',BASEURL ,2 ,ART +'wtf.png',OO0OO0000O000O000 .path .join (mediaPath ,"over.jpg"),'')#line:148
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:149
    addItem ('[COLOR gray]system information (kodi %s):[/COLOR]'%xbmcver ,BASEURL ,16 ,ART +'xvbmc.png')#line:150
    global serviceinfotxt #line:151
    OO000O000OO000000 ,OO00OO0000O00O000 =O0OO00O0O00OOOOO0 .checkSPversie ()#line:152
    if OO000O000OO000000 =="uwspversietxt":#line:153
       O00OOO0O00O0O0000 =O0000OO0O0O0OOOOO .getHtml2 (O0OO0OOOOO00000O0 )#line:154
       serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OO00OO0000O00O000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O00OOO0O00O0O0000 )#line:155
    elif OO000O000OO000000 =="uwspversietxtwiz":#line:156
         O00OOO0O00O0O0000 =O0000OO0O0O0OOOOO .getHtml2 (O0OOO0O0O0O000OOO )#line:157
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OO00OO0000O00O000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O00OOO0O00O0O0000 )#line:158
    elif OO000O000OO000000 =="uwspversietxtrpi":#line:159
         O00OOO0O00O0O0000 =O0000OO0O0O0OOOOO .getHtml2 (O0000O00O00OOO0OO )#line:160
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OO00OO0000O00O000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O00OOO0O00O0O0000 )#line:161
    addItem ('%s'%serviceinfotxt ,BASEURL ,'',OO0OO0000O000O000 .path .join (mediaPath ,"wtf.png"))#line:162
    global buildinfotxt #line:163
    OO0OOOOOOO0O0O00O ,O0O0O0O00O0000000 =O0OO00O0O00OOOOO0 .checkXvbmcversie ()#line:164
    if OO0OOOOOOO0O0O00O =="bldversietxt":#line:165
       O0000O000OOOO0O00 =O0000OO0O0O0OOOOO .getHtml2 (OOOO0OO0OO0OOOOOO )#line:166
       buildinfotxt ='[COLOR gray][B] - [/B]your system build: %s [/COLOR]'%(O0O0O0O00O0000000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0000O000OOOO0O00 )#line:167
    elif OO0OOOOOOO0O0O00O =="bldversietxtwiz":#line:168
         O0000O000OOOO0O00 =O0000OO0O0O0OOOOO .getHtml2 (OOO00O0OOO0OO0O0O )#line:169
         buildinfotxt ='[COLOR gray][B] - [/B]your wizard build: %s [/COLOR]'%(O0O0O0O00O0000000 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0000O000OOOO0O00 )#line:170
    addItem ('%s'%buildinfotxt ,BASEURL ,'',OO0OO0000O000O000 .path .join (mediaPath ,"wtf.png"))#line:171
    if OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon("service.openelec.settings")')+OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:173
       addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:174
       addDir ('[COLOR orange]XvBMC Raspberry Pi [B] -[/B] Tools, DEV. & Maintenance[/COLOR]',BASEURL ,30 ,ART +'RPi.png',FANARTsub ,'')#line:175
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:177
    addItem (Terug ,BASEURL ,3 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:178
    O0OO00O0O00OOOOO0 .setView ('movies','EPiC')#line:179
def XvBMCmaint ():#line:181
    addItem ('[B]B[/B]uild [COLOR red]purge[/COLOR] [COLOR dimgray](build [B]c[/B]rap[B]c[/B]leaner & fix evil addons/repos)[/COLOR]',BASEURL ,21 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:182
    addItem ('[B]C[/B]lear cache',BASEURL ,22 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:183
    addItem ('[B]D[/B]elete thumbnails',BASEURL ,23 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:184
    addItem ('[B]F[/B]lush add-ons [COLOR dimgray](salts HD/RD lite & Exodus \'cache+temp\' files)[/COLOR]',BASEURL ,24 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:185
    addItem ('[B]F[/B]ull clean [COLOR dimgray](cache, crashlogs, packages & thumbnails)[/COLOR]',BASEURL ,25 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:186
    addItem ('[B]P[/B]urge packages',BASEURL ,26 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:187
    addItem ('[B]R[/B]efresh addons[COLOR white]+[/COLOR]repos',BASEURL ,27 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:188
    if int (O0000OO0O0O0OOOOO .kodiver )<=16.7 :#line:189
       addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s remove addons.db',BASEURL ,28 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:190
    elif int (O0000OO0O0O0OOOOO .kodiver )>16.7 :#line:191
         addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s enable all add-ons [COLOR dimgray](Kodi 17+ Krypton)[/COLOR]',BASEURL ,29 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:192
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:194
    addItem (About ,BASEURL ,2 ,OO0OO0000O000O000 .path .join (mediaPath ,"wtf.png"))#line:195
    addItem (Terug ,BASEURL ,3 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:196
    O0OO00O0O00OOOOO0 .setView ('movies','EPiC')#line:197
def XvBMCtools1 ():#line:199
    addItem ('[B]C[/B]onvert physical paths (\'home\') to \'special\'',BASEURL ,11 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:200
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]most[/COLOR] add-ons)[/COLOR]',BASEURL ,12 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:201
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]all[/COLOR] add-ons)[/COLOR]',BASEURL ,13 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:202
    addItem ('[B]E[/B]nable Kodi Live Streams [COLOR dimgray](17+ Krypton; [COLOR white]RTMP[/COLOR])[/COLOR]',BASEURL ,14 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:203
    addItem ('[B]F[/B]orce close Kodi  [COLOR dimgray](Kill Kodi)[/COLOR]',BASEURL ,15 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:204
    addItem ('[B]L[/B]og viewer [COLOR dimgray](show \'kodi.log\')[/COLOR]',BASEURL ,17 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:206
    addItem ('[B]U[/B]RLResolver -> settings',BASEURL ,18 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:207
    addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s Advancedsettings unlocker [COLOR dimgray](reset)[/COLOR]',BASEURL ,19 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:208
    addDir ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s [COLOR white][B]H[/B]idden [B]g[/B]ems[B] & [/B][B]M[/B]ore [B]t[/B]ools[/COLOR] [COLOR dimgray](TiP[B]!![/B])[/COLOR]',BASEURL ,40 ,ART +'xvbmc.png',OO0OO0000O000O000 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:209
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:211
    addItem (About ,BASEURL ,2 ,OO0OO0000O000O000 .path .join (mediaPath ,"wtf.png"))#line:212
    addItem (Terug ,BASEURL ,3 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:213
    O0OO00O0O00OOOOO0 .setView ('movies','EPiC')#line:214
def XvBMCrpi ():#line:216
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] extreme crapcleaner [COLOR dimgray]([B]no[/B] factory reset)[/COLOR]',BASEURL ,31 ,OO0OO0000O000O000 .path .join (mediaPath ,"tools.png"))#line:217
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] overclock [COLOR dimgray](raspberry Pi ***only***)[/COLOR]',BASEURL ,32 ,OO0OO0000O000O000 .path .join (mediaPath ,"overclock.png"))#line:218
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] #dev# corner [COLOR dimgray](firmware, OS, etc.)[/COLOR]',BASEURL ,33 ,OO0OO0000O000O000 .path .join (mediaPath ,"firmware.png"))#line:219
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:221
    addItem (About ,BASEURL ,2 ,OO0OO0000O000O000 .path .join (mediaPath ,"wtf.png"))#line:222
    addItem (Terug ,BASEURL ,3 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:223
    O0OO00O0O00OOOOO0 .setView ('movies','EPiC')#line:224
def XvBMCtools2 ():#line:226
    addItem ('[B]K[/B]odi Quick Reset [COLOR dimgray](\"rejuvenate\" XvBMC-NL build)[/COLOR]',BASEURL ,41 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:228
    addItem ('[B]K[/B]odi Factory Reset [COLOR dimgray](complete Kodi Krypton wipe)[/COLOR]',BASEURL ,42 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:229
    addItem ('[B]K[/B]odi Fresh Start [COLOR dimgray](remove older Kodi\'s)[/COLOR]',BASEURL ,43 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:230
    addItem ('[B]P[/B]ush Fixes [COLOR dimgray](for XvBMC builds)[/COLOR]',BASEURL ,44 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:231
    addItem ('[B]P[/B]ush XvBMC REPOsitory [COLOR dimgray](install or fix repo)[/COLOR]',BASEURL ,45 ,OO0OO0000O000O000 .path .join (mediaPath ,"maint.png"))#line:232
    if OO0OO0000O000O000 .path .isfile (xxxCheck ):#line:233
       if OOO00O0O00000O0OO .getCondVisibility ('System.HasAddon("plugin.program.super.favourites")'):#line:234
          addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:235
          addItem ('[COLOR hotpink]activated: [/COLOR][COLOR pink]XvBMC\'s [B] [COLOR hotpink]x[COLOR deeppink]X[/COLOR]x[/COLOR] [/B] section ([COLOR hotpink]18[/COLOR][COLOR deeppink][B]+[/B][/COLOR])[/COLOR]',BASEURL ,69 ,xxxIcon )#line:236
       else :#line:237
           addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:238
           addItem ('[COLOR red]\'Super Favourites\' is missing, [COLOR lime][I]click here [/I][/COLOR] to (re-)install & enable [B]18+[/B][/COLOR]',BASEURL ,70 ,xxxIcon )#line:239
    else :#line:240
        addItem ('[B]P[/B]ush x[B]X[/B]x [COLOR dimgray](\"dirty\"-up your box with some 69 and mo\')[/COLOR]',BASEURL ,46 ,xxxIcon )#line:241
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:243
    addItem (About ,BASEURL ,2 ,OO0OO0000O000O000 .path .join (mediaPath ,"wtf.png"))#line:244
    addItem (Terug ,BASEURL ,3 ,OO0OO0000O000O000 .path .join (mediaPath ,"xvbmc.png"))#line:245
    O0OO00O0O00OOOOO0 .setView ('movies','EPiC')#line:246
def wizard (name ,url ):#line:250
    O0OO000O0O000OO0O =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/addons','packages'))#line:251
    if not OO0OO0000O000O000 .path .exists (O0OO000O0O000OO0O ):#line:252
        OO0OO0000O000O000 .makedirs (O0OO000O0O000OO0O )#line:253
    OO000O0OOOO00OO00 =OO0OO0000O000O000 .path .join (O0OO000O0O000OO0O ,'default.zip')#line:254
    try :#line:255
       OO0OO0000O000O000 .remove (OO000O0OOOO00OO00 )#line:256
    except :#line:257
       pass #line:258
    OO0OO000OO00OOO00 .download (url ,OO000O0OOOO00OO00 )#line:259
    if OO0OO0000O000O000 .path .exists (OO000O0OOOO00OO00 ):#line:261
        O0OO000000O00OO00 =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://','home'))#line:262
        OOOO00OO0OO0OOOO0 .sleep (2 )#line:263
        dp .create (MainTitle ,'XvBMC-NL: pull update VoOdOo...','','Please Wait')#line:265
        dp .update (0 ,"","***Extract ZIP - Please Wait")#line:266
        O0OO00O0O00OOOOO0 .log ("==========================================================")#line:267
        O0OO00O0O00OOOOO0 .log (O0OO000000O00OO00 )#line:268
        O0OO00O0O00OOOOO0 .log ("==========================================================")#line:269
        OO000OOOO0OO0OO00 .all (OO000O0OOOO00OO00 ,O0OO000000O00OO00 ,dp )#line:270
        dp .close ()#line:271
        try :OO0OO0000O000O000 .remove (OO000O0OOOO00OO00 )#line:272
        except :pass #line:273
    if int (O0000OO0O0O0OOOOO .kodiver )<=16.7 :#line:274
       dialog .ok (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  HINT  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:275
       O0OO00O0O00OOOOO0 .forceRefresh (melding =False )#line:276
    elif int (O0000OO0O0O0OOOOO .kodiver )>16.7 :#line:277
         O0000OO0O0O0OOOOO .enableAddons (melding =False )#line:278
         OOOO00OO0OO0OOOO0 .sleep (0.5 )#line:279
         O0OO0OOOOO0O0OO00 =O00O0O00OO0OO0O0O .Dialog ().yesno (MainTitle +"[COLOR green][B] - success[/B][/COLOR]",' ','[B]IF[/B] add-ons do NOT work, you need to [B]reboot 1st[/B].','(een REBOOT van uw systeem is VEELAL wenselijk)',yeslabel ='[COLOR lime]Reboot[/COLOR]',nolabel ='[COLOR red]Continue[/COLOR]')#line:280
         if O0OO0OOOOO0O0OO00 ==1 :#line:281
            OOOO00OO0OO0OOOO0 .sleep (1 )#line:282
            O0OO00O0O00OOOOO0 .killKodi ()#line:283
         elif O0OO0OOOOO0O0OO00 ==0 :#line:284
              if int (O0000OO0O0O0OOOOO .kodiver )>16.7 :#line:285
                 O0000OO0O0O0OOOOO .enableAddons (melding =False )#line:286
                 OOOO00OO0OO0OOOO0 .sleep (0.5 )#line:287
                 dialog .ok (MainTitle +" : [COLOR red]add-ons[/COLOR] [COLOR green][B]enabled[/B][/COLOR]",'[COLOR orange][B]!!!  TIP  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:288
                 OOO00O0O00000O0OO .executebuiltin ('ReloadSkin()')#line:289
    OOO00O0O00000O0OO .executebuiltin ("Container.Refresh")#line:290
    OOO00O0O00000O0OO .sleep (5000 )#line:291
def fileexchange (url ,name ,locatie ):#line:295
    dp .create (MainTitle ,'XvBMC-NL: RPi update VoOdOo...','','Please Wait')#line:296
    if not OO0OO0000O000O000 .path .exists (locatie ):OO0OO0000O000O000 .makedirs (locatie )#line:297
    OO0OO0OO0000O0000 =OO0OO0000O000O000 .path .join (locatie ,name )#line:298
    dp .update (0 ,'','.file.VoOdOo.')#line:299
    try :OO0OO0000O000O000 .remove (OO0OO0OO0000O0000 )#line:300
    except :pass #line:301
    OO0OO000OO00OOO00 .download (url +name ,OO0OO0OO0000O0000 )#line:302
    OOOO00OO0OO0OOOO0 .sleep (1 )#line:303
    dp .close ()#line:304
    OOO00O0O00000O0OO .executebuiltin ("Container.Refresh")#line:306
    OOO00O0O00000O0OO .sleep (1000 )#line:307
def customwizard (name ,url ,storeLoc ,unzipLoc ):#line:309
    if not OO0OO0000O000O000 .path .exists (storeLoc ):OO0OO0000O000O000 .makedirs (storeLoc )#line:311
    OO0O00000000OOOO0 =OO0OO0000O000O000 .path .join (storeLoc ,name )#line:312
    try :OO0OO0000O000O000 .remove (OO0O00000000OOOO0 )#line:313
    except :pass #line:314
    OO0OO000OO00OOO00 .download (url +name ,OO0O00000000OOOO0 )#line:315
    if OO0OO0000O000O000 .path .exists (OO0O00000000OOOO0 ):#line:317
       OOOO00OO0OO0OOOO0 .sleep (2 )#line:319
       dp .create (MainTitle ,'XvBMC-NL: just doing our VoOdOo...','','Please Wait')#line:320
       dp .update (0 ,'','***Mo\' XvBMC magic...')#line:321
       O0OO00O0O00OOOOO0 .log (str ('UNWiZ@'+unzipLoc ))#line:322
       OO000OOOO0OO0OO00 .all (OO0O00000000OOOO0 ,unzipLoc ,dp )#line:323
       dp .close ()#line:324
       try :OO0OO0000O000O000 .remove (OO0O00000000OOOO0 )#line:325
       except :pass #line:326
    if int (O0000OO0O0O0OOOOO .kodiver )<=16.7 :#line:327
       dialog .ok (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  HINT  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:328
       O0OO00O0O00OOOOO0 .forceRefresh (melding =False )#line:329
    elif int (O0000OO0O0O0OOOOO .kodiver )>16.7 :#line:330
         O0000OO0O0O0OOOOO .enableAddons (melding =False )#line:331
         OOOO00OO0OO0OOOO0 .sleep (0.5 )#line:332
         O0O0O0OOOO0OOO000 =O00O0O00OO0OO0O0O .Dialog ().yesno (MainTitle +"[COLOR green][B] - success[/B][/COLOR]",' ','[B]IF[/B] add-ons do NOT work, you need to [B]reboot 1st[/B].','(een REBOOT van uw systeem is VEELAL wenselijk)',yeslabel ='[COLOR lime]Reboot[/COLOR]',nolabel ='[COLOR red]Continue[/COLOR]')#line:333
         if O0O0O0OOOO0OOO000 ==1 :#line:334
            OOOO00OO0OO0OOOO0 .sleep (1 )#line:335
            O0OO00O0O00OOOOO0 .killKodi ()#line:336
         elif O0O0O0OOOO0OOO000 ==0 :#line:337
              if int (O0000OO0O0O0OOOOO .kodiver )>16.7 :#line:338
                 O0000OO0O0O0OOOOO .enableAddons (melding =False )#line:339
                 OOOO00OO0OO0OOOO0 .sleep (0.5 )#line:340
                 dialog .ok (MainTitle +" : [COLOR red]add-ons[/COLOR] [COLOR green][B]enabled[/B][/COLOR]",'[COLOR orange][B]!!!  TIP  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:341
                 OOO00O0O00000O0OO .executebuiltin ('ReloadSkin()')#line:342
    OOO00O0O00000O0OO .executebuiltin ("Container.Refresh")#line:343
    OOO00O0O00000O0OO .sleep (5000 )#line:344
def unlocker ():#line:347
    dialog .ok (MainTitle +" - unlocker",' ','unlock advancedsettings for this build','[COLOR dimgray](+reset \'advancedsettings.xml\' -use at your own risk)[/COLOR]')#line:349
    OO0O0000OOO000OO0 =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/userdata/'))#line:350
    OOO00OOOO00OO0OOO =OO0O0OO00OOO0OOOO .b64decode ('YWR2YW5jZWRzZXR0aW5ncy54bWw=')#line:351
    OO0O00OO00O00O0OO =True #line:352
    try :#line:353
        OO0OO0000O000O000 .unlink (OO0O0000OOO000OO0 +OOO00OOOO00OO0OOO )#line:354
    except :#line:355
        OO0O00OO00O00O0OO =False #line:356
    if OO0O00OO00O00O0OO :#line:358
        dialog .ok (MainTitle +" - [B]UNLOCKED[/B]",'[COLOR green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Herstart[/B] Kodi ter afronding \'unlocker\' (force close)','[B]Reboot[/B] Kodi to complete \'unlocker\' (force close)')#line:359
        OO0OO0000O000O000 ._exit (1 )#line:360
    else :#line:361
        dialog .ok (MainTitle +" - [B]OOOOOOPS[/B]",'[COLOR red][B]!!!  Failed  !!![/B][/COLOR]','[B]Nope![/B] helaas geen succes (niks te \'unlocken\')','[B]Nope![/B] close but no cigar  (nothing to \'unlock\')')#line:362
def XvbmcOc ():#line:365
    O0O0O0000OO000O0O =O0000O0O000OO0000 ()#line:366
    O0OO00O0O00OOOOO0 .log ("Platform: "+str (O0O0O0000OO000O0O ))#line:367
    if not O0O0O0000OO000O0O =='linux':#line:368
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] OverClock!",O000O0O0OO0O000O0 ,O0000O0000OO00OO0 ,OOO0O000OO000OOOO )#line:369
       O0OO00O0O00OOOOO0 .log ("none Linux OS ie. Open-/LibreELEC")#line:370
    else :#line:371
        O0OO00O0O00OOOOO0 .log ("linux os")#line:372
        O00OOO0OO0OO0O000 .ocMenu ()#line:373
def XvbmcDev ():#line:376
    OOOOOOOO0OOOO0OO0 =O0000O0O000OO0000 ()#line:377
    O0OO00O0O00OOOOO0 .log ("Platform: "+str (OOOOOOOO0OOOO0OO0 ))#line:378
    if not OOOOOOOO0OOOO0OO0 =='linux':#line:379
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] #dev#",O000O0O0OO0O000O0 ,O0000O0000OO00OO0 ,OOO0O000OO000OOOO )#line:380
       O0OO00O0O00OOOOO0 .log ("none Linux OS ie. Open-/LibreELEC")#line:381
    else :#line:382
        O0OO00O0O00OOOOO0 .log ("linux os")#line:383
        OO000O00OO00OOOOO .devMenu ()#line:384
def disabled ():#line:387
    O0OO00O0O00OOOOO0 .okDialog ('[COLOR red][B]Sorry, disabled! [/B](for now)[/COLOR]','','[COLOR lime]goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')#line:388
def rejuvXvbmc ():#line:391
    OO0O0OO0OO00OOO00 =O0OO00O0O00OOOOO0 .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Wilt u uw XvBMC \'build\' volledig opschonen (wipe) en Kodi Krypton [B]leeg[/B] her-configureren?','[COLOR dimgray]Please confirm that you wish you wipe clean your current configuration and reconfigure Kodi.[/COLOR]')#line:392
    if OO0O0OO0OO00OOO00 :#line:393
        OO00OO0O0OOO0000O =O0OOOOO000O00000O .Addon (id =AddonID ).getAddonInfo ('path');OO00OO0O0OOO0000O =OOO00O0O00000O0OO .translatePath (OO00OO0O0OOO0000O );#line:394
        OO00OO0O000O0O00O =OO0OO0000O000O000 .path .join (OO00OO0O0OOO0000O ,"..","..");OO00OO0O000O0O00O =OO0OO0000O000O000 .path .abspath (OO00OO0O000O0O00O );O0OO00O0O00OOOOO0 .log ("rejuvXvbmc.main_XvBMC: xbmcPath="+OO00OO0O000O0O00O );#line:395
        OO000O0OOO0O00O00 =('addons','Database','packages','userdata')#line:397
        O0000O0OO000OO00O =('metadata.album.universal','metadata.artists.universal','metadata.common.imdb.com','metadata.common.musicbrainz.org','metadata.common.theaudiodb.com','metadata.common.themoviedb.org','metadata.themoviedb.org','metadata.tvdb.com','plugin.program.super.favourites','plugin.program.xvbmcinstaller.nl','repository.xvbmc','resource.language.nl_nl','script.xvbmc.updatertools','service.xbmc.versioncheck','skin.aeon.nox.spin','script.grab.fanart','service.library.data.provider','resource.images.recordlabels.white','resource.images.studios.coloured','resource.images.studios.white','xbmc.gui','script.skinshortcuts','script.module.simplejson','script.module.unidecode')#line:403
        O00O0O0OO000O0O0O =('Addons26.db','Addons27.db','guisettings.xml','kodi.log','Textures13.db')#line:405
        OOOOOO000O0OOOO0O =O0OO00O0O00OOOOO0 .message_yes_no ("[COLOR white][B]"+AddonTitle +"[/B][/COLOR]",'Wilt u het XvBMC-NL basis \'framework\' handhaven na reset? Verwijderd alles behalve XvBMC (aanbeveling).','[COLOR dimgray](do you wish to keep XvBMC\'s default framework?)[/COLOR]')#line:406
        if OOOOOO000O0OOOO0O :#line:407
            OO000O0OOO0O00O00 =OO000O0OOO0O00O00 +('addon_data','keymaps','media',)#line:408
            O0000O0OO000OO00O =O0000O0OO000OO00O +('inputstream.rtmp','keymaps','media','service.subtitles.addic7ed','service.subtitles.opensubtitles_by_opensubtitles','service.subtitles.opensubtitlesBeta','service.subtitles.podnapisi','service.subtitles.subscene',)#line:409
            O00O0O0OO000O0O0O =O00O0O0OO000O0O0O +('advancedsettings.xml','favourites.xml','profiles.xml','RssFeeds.xml','sources.xml','versiebld.txt','versiesp.txt','wizbld.txt','wizsp.txt',)#line:410
        else :#line:411
            OO000O0OOO0O00O00 =OO000O0OOO0O00O00 +('addon_data',)#line:412
            O0000O0OO000OO00O =O0000O0OO000OO00O +('inputstream.rtmp',)#line:413
            O00O0O0OO000O0O0O =O00O0O0OO000O0O0O +('advancedsettings.xml','RssFeeds.xml',)#line:414
            OO00OOOOO0O00OO0O =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join (USERADDONDATA ,'plugin.program.super.favourites','Super Favourites'))#line:415
            O0O0O00OOOOOOO0O0 =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join (USERDATA ,'addon_data','script.skinshortcuts'))#line:416
            try :#line:417
                OO0OO0000OOO0O0OO .rmtree (OO00OOOOO0O00OO0O )#line:418
            except Exception as O000OOOOOOO00OO0O :O0OO00O0O00OOOOO0 .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (O000OOOOOOO00OO0O ))#line:419
            try :#line:420
                OO0OO0000OOO0O0OO .rmtree (O0O0O00OOOOOOO0O0 )#line:421
            except Exception as O000OOOOOOO00OO0O :O0OO00O0O00OOOOO0 .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (O000OOOOOOO00OO0O ))#line:422
        dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Snelle XvBMC Krypton reset, even geduld...','','[COLOR dimgray](Quick XvBMC Krypton reset, please wait...)[/COLOR]')#line:423
        try :#line:424
            for OOO00OOO00O00OOO0 ,OO0O00O00O0OO0O0O ,O000OO00O0O00O0O0 in OO0OO0000O000O000 .walk (OO00OO0O000O0O00O ,topdown =True ):#line:425
                OO0O00O00O0OO0O0O [:]=[O0000OOOOOO00000O for O0000OOOOOO00000O in OO0O00O00O0OO0O0O if O0000OOOOOO00000O not in O0000O0OO000OO00O ]#line:426
                O000OO00O0O00O0O0 [:]=[OOOOO00O000OO00OO for OOOOO00O000OO00OO in O000OO00O0O00O0O0 if OOOOO00O000OO00OO not in O00O0O0OO000O0O0O ]#line:427
                for O00OO000O0O00OO00 in O000OO00O0O00O0O0 :#line:428
                    try :#line:429
                        dp .update (11 ,'','***Cleaning files...')#line:430
                        OO0OO0000O000O000 .remove (OO0OO0000O000O000 .path .join (OOO00OOO00O00OOO0 ,O00OO000O0O00OO00 ))#line:431
                    except Exception as O000OOOOOOO00OO0O :O0OO00O0O00OOOOO0 .log ("rejuvXvbmc.file_name: User files partially removed - "+str (O000OOOOOOO00OO0O ))#line:433
                for O0O0O0OOOO00000OO in OO0O00O00O0OO0O0O :#line:434
                    if O0O0O0OOOO00000OO not in OO000O0OOO0O00O00 :#line:435
                        try :#line:436
                            dp .update (33 ,'','***Cleaning folders...')#line:437
                            OO0OO0000OOO0O0OO .rmtree (OO0OO0000O000O000 .path .join (OOO00OOO00O00OOO0 ,O0O0O0OOOO00000OO ))#line:438
                        except Exception as O000OOOOOOO00OO0O :O0OO00O0O00OOOOO0 .log ("rejuvXvbmc.folder: User folders partially removed - "+str (O000OOOOOOO00OO0O ))#line:440
            dp .update (66 ,'','***Crap Cleaning...')#line:441
            O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ()#line:442
        except Exception as O000OOOOOOO00OO0O :#line:443
            O0OO00O0O00OOOOO0 .log ("rejuvXvbmc: User stuff partially removed - "+str (O000OOOOOOO00OO0O ))#line:444
            O0OO00O0O00OOOOO0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Error![/B][/COLOR]",'...DAT ging niet helemaal goed, controleer uw log...','[COLOR dimgray](XvBMC user files partially removed, please check log)[/COLOR]')#line:445
            O0O0000OO0O000OOO .exit ()#line:446
        dp .update (99 ,'','***Cleaning Crap...')#line:447
        O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:448
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:449
        OO0OO0000O000O000 ._exit (1 )#line:450
    else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:451
def WipeXBMC ():#line:454
    if skin !="skin.estuary":#line:455
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'selecteer eerst de standaard (Estuary) skin alvorens een volledige [B]\'wipe\'[/B] van uw Kodi uit te voeren.','','[COLOR dimgray](before Kodi wipe, select Estuary skin first)[/COLOR]')#line:456
        OOO00O0O00000O0OO .executebuiltin ("ActivateWindow(InterfaceSettings)")#line:457
        return #line:458
    else :#line:459
        OOO000OOO0OO0O0OO =O00O0O00OO0OO0O0O .Dialog ().yesno ("[COLOR lime][B]BELANGRIJK / IMPORTANT / HINT[/B][/COLOR]",'[B]let op: [/B]dit zal alles verwijderen van uw huidige Kodi installatie, weet u zeker dat u wilt doorgaan[B]?[/B]','','[COLOR dimgray](this will remove your current Kodi build, continue?)[/COLOR]',yeslabel ='[COLOR lime][B]JA/YES[/B][/COLOR]',nolabel ='[COLOR red]nee/nope[/COLOR]')#line:460
        if OOO000OOO0OO0O0OO ==1 :#line:461
           dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'verwijder alles, even geduld...','','[COLOR dimgray](remove everything, please wait...)[/COLOR]')#line:462
           try :#line:463
               for O00O0O00O0O0000O0 ,O0000OOO00O0OOO00 ,O00000000O00OOOOO in OO0OO0000O000O000 .walk (HOME ,topdown =True ):#line:464
                    O0000OOO00O0OOO00 [:]=[OOO0OOOOO0O0OO000 for OOO0OOOOO0O0OO000 in O0000OOO00O0OOO00 if OOO0OOOOO0O0OO000 not in EXCLUDES ]#line:465
                    for O0O0O0000O0O00O0O in O00000000O00OOOOO :#line:466
                        try :dp .update (11 ,'','***Cleaning files...');OO0OO0000O000O000 .remove (OO0OO0000O000O000 .path .join (O00O0O00O0O0000O0 ,O0O0O0000O0O00O0O ));OO0OO0000O000O000 .rmdir (OO0OO0000O000O000 .path .join (O00O0O00O0O0000O0 ,O0O0O0000O0O00O0O ))#line:467
                        except :pass #line:468
                    for O0O0O0000O0O00O0O in O0000OOO00O0OOO00 :#line:469
                        try :dp .update (33 ,'','***Cleaning folders...');OO0OO0000O000O000 .rmdir (OO0OO0000O000O000 .path .join (O00O0O00O0O0000O0 ,O0O0O0000O0O00O0O ));OO0OO0000O000O000 .rmdir (O00O0O00O0O0000O0 )#line:470
                        except :pass #line:471
               dp .update (66 ,'','***Crap Cleaning...')#line:472
               O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ()#line:473
           except :pass #line:474
           dp .update (99 ,'','***Cleaning Crap...')#line:475
           O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:476
           dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'Kodi zal nu afsluiten...','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:477
           OO0OO0000O000O000 ._exit (1 )#line:478
        elif OOO000OOO0OO0O0OO ==0 :#line:479
             dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen Kodi Krypton \'wipe\' uitgevoerd...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:480
def FRESHSTART (params ):#line:483
    if int (O0000OO0O0O0OOOOO .kodiver )>16.7 :#line:484
       dialog .ok ("[COLOR lime]"+MainTitle +"[/COLOR] [COLOR red][B]- NOPE![/B][/COLOR]",'[COLOR orange][B]NOTE:[/B][/COLOR]','[COLOR white]alleen voor oudere Kodi\'s dan Krypton (>17.0)[/COLOR]','[COLOR dimgray](for use with older Kodi\'s only (>17.0)[/COLOR]')#line:485
    else :#line:486
        O0OO00O0O00OOOOO0 .log ("freshstart.main_XvBMC: "+repr (params ));OO0O0OO0OOO00OOO0 =O0OO00O0O00OOOOO0 .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Remove[/B][/COLOR]",'Kodi terugzetten naar de standaard fabrieksinstellingen?','[COLOR dimgray](reset Kodi to factory defaults)[/COLOR]')#line:487
        if OO0O0OO0OOO00OOO0 :#line:488
            OOO00OO000OOOO00O =O0OOOOO000O00000O .Addon (id =AddonID ).getAddonInfo ('path');OOO00OO000OOOO00O =OOO00O0O00000O0OO .translatePath (OOO00OO000OOOO00O );#line:489
            OO00OO00OO000O000 =OO0OO0000O000O000 .path .join (OOO00OO000OOOO00O ,"..","..");OO00OO00OO000O000 =OO0OO0000O000O000 .path .abspath (OO00OO00OO000O000 );O0OO00O0O00OOOOO0 .log ("freshstart.main_XvBMC: xbmcPath="+OO00OO00OO000O000 );O0O0OOOO0000000OO =False #line:490
            dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- FreshStart![/B][/COLOR]",'terug naar fabrieksinstellingen, even geduld...','','[COLOR dimgray](factory reset Kodi, please wait...)[/COLOR]')#line:491
            try :#line:492
                for O0O000OO00OO0OO0O ,OO00O000OO0O0O00O ,OO00O0OO00000OO0O in OO0OO0000O000O000 .walk (OO00OO00OO000O000 ,topdown =True ):#line:493
                    OO00O000OO0O0O00O [:]=[OO0O0OOO0OOOO00OO for OO0O0OOO0OOOO00OO in OO00O000OO0O0O00O if OO0O0OOO0OOOO00OO not in EXCLUDES ]#line:494
                    dp .update (33 ,'','***Cleaning files+folders...')#line:495
                    for O000O0000OO0OOO0O in OO00O0OO00000OO0O :#line:496
                        try :OO0OO0000O000O000 .remove (OO0OO0000O000O000 .path .join (O0O000OO00OO0OO0O ,O000O0000OO0OOO0O ))#line:497
                        except :#line:498
                            if O000O0000OO0OOO0O not in ["Addons1.db","MyMusic7","MyVideos37.db","Textures1.db","xbmc.log"]:O0O0OOOO0000000OO =True #line:499
                            O0OO00O0O00OOOOO0 .log ("XvBMC-Error removing file: "+O0O000OO00OO0OO0O +" "+O000O0000OO0OOO0O )#line:500
                    for O000O0000OO0OOO0O in OO00O000OO0O0O00O :#line:501
                        try :OO0OO0000O000O000 .rmdir (OO0OO0000O000O000 .path .join (O0O000OO00OO0OO0O ,O000O0000OO0OOO0O ))#line:502
                        except :#line:503
                            if O000O0000OO0OOO0O not in ["Database","userdata"]:O0O0OOOO0000000OO =True #line:504
                            O0OO00O0O00OOOOO0 .log ("XvBMC-Error removing folder: "+O0O000OO00OO0OO0O +" "+O000O0000OO0OOO0O )#line:505
                dp .update (66 ,'','***Crap Cleaning...')#line:506
                O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ()#line:507
                if not O0O0OOOO0000000OO :O0OO00O0O00OOOOO0 .log ("freshstart.main_XvBMC: All user files removed, you now have a CLEAN install");O0OO00O0O00OOOOO0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:508
                else :O0OO00O0O00OOOOO0 .log ("freshstart.main_XvBMC: User files partially removed");O0OO00O0O00OOOOO0 .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:509
            except :O0OO00O0O00OOOOO0 .message ("[COLOR red][B]"+AddonTitle +"[/B][/COLOR]",'Problem found','Your settings have [B]not[/B] been changed');import traceback as O0O0O0O0OOOOO0OOO ;O0OO00O0O00OOOOO0 .log (O0O0O0O0OOOOO0OOO .format_exc ());O0OO00O0O00OOOOO0 .log ("freshstart.main_XvBMC: NOTHING removed");O0O0000OO0O000OOO .exit ()#line:510
            dp .update (99 ,'','***Cleaning Crap...')#line:511
            O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();O0OO00O0O00OOOOO0 .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:512
            dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:513
            OO0OO0000O000O000 ._exit (1 )#line:514
        else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:515
def addItem (name ,url ,mode ,iconimage ):#line:519
    O0O0OO00O0O00000O =O0O0000OO0O000OOO .argv [0 ]+"?url="+O0000OO00OOOOOOO0 .quote_plus (url )+"&mode="+str (mode )+"&name="+O0000OO00OOOOOOO0 .quote_plus (name )#line:520
    O00O0OOOO00O0OOO0 =True #line:521
    OO0O0OOO00OO000OO =O00O0O00OO0OO0O0O .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:522
    OO0O0OOO00OO000OO .setInfo (type ="Video",infoLabels ={"Title":name })#line:523
    OO0O0OOO00OO000OO .setArt ({'fanart':FANART })#line:524
    O00O0OOOO00O0OOO0 =O0O0O0000000OOOOO .addDirectoryItem (handle =int (O0O0000OO0O000OOO .argv [1 ]),url =O0O0OO00O0O00000O ,listitem =OO0O0OOO00OO000OO ,isFolder =False )#line:525
    return O00O0OOOO00O0OOO0 #line:526
def get_params ():#line:529
        OO0O0O00O0OOO0O00 =[]#line:530
        OOO0000OOO0O0O000 =O0O0000OO0O000OOO .argv [2 ]#line:531
        if len (OOO0000OOO0O0O000 )>=2 :#line:532
                OO0000O0O0O0OO000 =O0O0000OO0O000OOO .argv [2 ]#line:533
                O0OOO0OO0OOOO00OO =OO0000O0O0O0OO000 .replace ('?','')#line:534
                if (OO0000O0O0O0OO000 [len (OO0000O0O0O0OO000 )-1 ]=='/'):#line:535
                        OO0000O0O0O0OO000 =OO0000O0O0O0OO000 [0 :len (OO0000O0O0O0OO000 )-2 ]#line:536
                O000O000O0OO0OO0O =O0OOO0OO0OOOO00OO .split ('&')#line:537
                OO0O0O00O0OOO0O00 ={}#line:538
                for O00O0OOOO00O0O000 in range (len (O000O000O0OO0OO0O )):#line:539
                        OOO00O0O000O0000O ={}#line:540
                        OOO00O0O000O0000O =O000O000O0OO0OO0O [O00O0OOOO00O0O000 ].split ('=')#line:541
                        if (len (OOO00O0O000O0000O ))==2 :#line:542
                                OO0O0O00O0OOO0O00 [OOO00O0O000O0000O [0 ]]=OOO00O0O000O0000O [1 ]#line:543
        return OO0O0O00O0OOO0O00 #line:544
def addDir (name ,url ,mode ,iconimage ,fanart ,description ):#line:547
        OO0OOOO0OO0O00O0O =O0O0000OO0O000OOO .argv [0 ]+"?url="+O0000OO00OOOOOOO0 .quote_plus (url )+"&mode="+str (mode )+"&name="+O0000OO00OOOOOOO0 .quote_plus (name )+"&iconimage="+O0000OO00OOOOOOO0 .quote_plus (iconimage )+"&fanart="+O0000OO00OOOOOOO0 .quote_plus (fanart )+"&description="+O0000OO00OOOOOOO0 .quote_plus (description )#line:548
        O0OO0O000OOOO000O =True #line:549
        OO0O0000OOO00O0O0 =O00O0O00OO0OO0O0O .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:550
        OO0O0000OOO00O0O0 .setInfo (type ="Video",infoLabels ={"Title":name ,"Plot":description })#line:551
        OO0O0000OOO00O0O0 .setProperty ("Fanart_Image",fanart )#line:552
        if mode ==1 :#line:553
            O0OO0O000OOOO000O =O0O0O0000000OOOOO .addDirectoryItem (handle =int (O0O0000OO0O000OOO .argv [1 ]),url =OO0OOOO0OO0O00O0O ,listitem =OO0O0000OOO00O0O0 ,isFolder =False )#line:554
        elif mode ==2 :#line:555
            O0OO0O000OOOO000O =O0O0O0000000OOOOO .addDirectoryItem (handle =int (O0O0000OO0O000OOO .argv [1 ]),url =OO0OOOO0OO0O00O0O ,listitem =OO0O0000OOO00O0O0 ,isFolder =False )#line:556
        elif mode ==100 :#line:557
            O0OO0O000OOOO000O =O0O0O0000000OOOOO .addDirectoryItem (handle =int (O0O0000OO0O000OOO .argv [1 ]),url =OO0OOOO0OO0O00O0O ,listitem =OO0O0000OOO00O0O0 ,isFolder =False )#line:558
        else :#line:559
            O0OO0O000OOOO000O =O0O0O0000000OOOOO .addDirectoryItem (handle =int (O0O0000OO0O000OOO .argv [1 ]),url =OO0OOOO0OO0O00O0O ,listitem =OO0O0000OOO00O0O0 ,isFolder =True )#line:560
        return O0OO0O000OOOO000O #line:561
params =get_params ()#line:564
url =None #line:565
name =None #line:566
mode =None #line:567
iconimage =None #line:568
fanart =None #line:569
description =None #line:570
try :#line:573
        url =O0000OO00OOOOOOO0 .unquote_plus (params ["url"])#line:574
except :#line:575
        pass #line:576
try :#line:577
        name =O0000OO00OOOOOOO0 .unquote_plus (params ["name"])#line:578
except :#line:579
        pass #line:580
try :#line:581
        iconimage =O0000OO00OOOOOOO0 .unquote_plus (params ["iconimage"])#line:582
except :#line:583
        pass #line:584
try :#line:585
        mode =int (params ["mode"])#line:586
except :#line:587
        pass #line:588
try :#line:589
        fanart =O0000OO00OOOOOOO0 .unquote_plus (params ["fanart"])#line:590
except :#line:591
        pass #line:592
try :#line:593
        description =O0000OO00OOOOOOO0 .unquote_plus (params ["description"])#line:594
except :#line:595
        pass #line:596
O0OO00O0O00OOOOO0 .log ("EPiC "+str (AddonTitle ))#line:600
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
     O0OO00O0O00OOOOO0 .AboutXvBMC ()#line:625
elif mode ==3 :#line:627
     O0OO00O0O00OOOOO0 .closeandexit ()#line:628
elif mode ==4 :#line:630
     O0OO00O0O00OOOOO0 .okDialog (O000O0O0OO0O000O0 ,'sorry, nothing todo...','with kind regards, team [COLOR green]XvBMC Nederland[/COLOR]')#line:631
elif mode ==11 :#line:633
     O00OO0O00OOOOOO0O .Fix_Special (url )#line:634
elif mode ==12 :#line:636
     O00OO0O00OOOOOO0O .AddonsEnable ()#line:637
elif mode ==13 :#line:639
     O0O0O0O0000OO00OO .setall_enable ()#line:640
elif mode ==14 :#line:642
     O00OO0O00OOOOOO0O .EnableRTMP ()#line:643
elif mode ==15 :#line:645
     O0OO00O0O00OOOOO0 .killKodi ()#line:646
elif mode ==16 :#line:648
     O0OO00O0O00OOOOO0 .KODIVERSION (url )#line:649
elif mode ==17 :#line:651
     O00OO0O00OOOOOO0O .xvbmcLog ()#line:652
elif mode ==18 :#line:654
     resolver_settings ()#line:655
elif mode ==19 :#line:657
     unlocker ()#line:658
elif mode ==21 :#line:660
     OO0OOO00000OOOOO0 .purgeOLD ()#line:661
elif mode ==22 :#line:663
     O00OO0O00OOOOOO0O .clearCache ()#line:664
elif mode ==23 :#line:666
     O00OO0O00OOOOOO0O .deleteThumbnails ()#line:667
elif mode ==24 :#line:669
     OO0O0O00O0OOOOO00 .flushMenu ()#line:670
elif mode ==25 :#line:672
     O00OO0O00OOOOOO0O .autocleanask ()#line:673
elif mode ==26 :#line:675
     O00OO0O00OOOOOO0O .purgePackages ()#line:676
elif mode ==27 :#line:678
     O0OO00O0O00OOOOO0 .forceRefresh (melding =True )#line:679
elif mode ==28 :#line:681
     O00OO0O00OOOOOO0O .AddonsDatabaseRemoval ()#line:682
elif mode ==29 :#line:684
     O0000OO0O0O0OOOOO .enableAddons (melding =True )#line:685
elif mode ==31 :#line:687
     O00OO0O00OOOOOO0O .PiCCleaner ()#line:688
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
     url =OO0O0OO00OOO0OOOO .b64decode (O0OO000000OOOO0OO )#line:713
     storeLoc =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/addons','packages'))#line:714
     unzipLoc =OO0OO0000O000O000 .path .join (HOME ,'addons')#line:715
     customwizard (name ,url ,storeLoc ,unzipLoc )#line:717
elif mode ==46 :#line:719
     url =OO0O0OO00OOO0OOOO .b64decode (OOOO0OO0OOO0OO0OO )+'triple-x/xXxvbmc.zip'#line:720
     wizard (name ,url )#line:722
elif mode ==69 :#line:723
     OOO00O0O00000O0OO .executebuiltin ('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?folder=xXx",return)')#line:724
elif mode ==70 :#line:725
     name ='plugin.program.super.favourites-1.0.59.zip'#line:726
     url =OO0O0OO00OOO0OOOO .b64decode (OOOO0OO0OOO0OO0OO )+'plugin.program.super.favourites/'#line:727
     storeLoc =OOO00O0O00000O0OO .translatePath (OO0OO0000O000O000 .path .join ('special://home/addons','packages'))#line:728
     unzipLoc =OO0OO0000O000O000 .path .join (HOME ,'addons')#line:729
     customwizard (name ,url ,storeLoc ,unzipLoc )#line:731
elif mode ==100 :#line:733
     locatie =USERDATA #line:734
     name ='rpi-service'#line:735
     fileexchange (url ,name +'.txt',locatie )#line:737
     wizard (name ,url +name +'.zip')#line:739
"""
    IF you copy/paste XvBMC's -default.py- please keep the credits -2- XvBMC-NL, Thx.
"""#line:743
O0O0O0000000OOOOO .endOfDirectory (int (O0O0000OO0O000OOO .argv [1 ]))
