#!/usr/bin/python
""#line:6
import re as OO00O00OO0OOOOO0O ,base64 as O000OOO0O00OOO0O0 ,urllib as OOO000O00O000OO00 ,urllib2 as O0OOO0OOOO00O00O0 ,sys as O0OO000OOO00O00O0 ,xbmcvfs as O0OO000OOO000OOO0 #line:25
import xbmc as O00O0000OO0O0O000 ,xbmcaddon as OO00O0O00OO00OO0O ,xbmcgui as OO0O00OO0O00O0OO0 ,xbmcplugin as O0O0O0OOOOOOOOOO0 #line:26
import os as OO000OOO0OO0O0OO0 ,shutil as OOO000000O0O000O0 ,time as OOO0OO00O0O00O0OO #line:27
import sqlite3 as OOO0000OO0O0O00O0 #line:28
import utils as OOO000OO0000O0OO0 #line:29
from resources .lib import addon_able as OO0OO000O00O0O00O #line:32
from resources .lib import downloader as O0O000O00OOO0O00O ,extract as OOOO00O0OO0OO0000 #line:33
from resources .lib import common as OOO0000000OO0000O #line:34
from resources .lib .common import platform as O0OO00O00O00O0O00 ,subtitleNope as OO0O000O0O0O000OO ,nonlinux as OOO0OOOOO00OOOO00 ,nonelecNL as OO0OOOOOO0OOOO00O #line:35
from resources .lib .common import base as O0OOOO0000O0O0OO0 ,basewiz as OO00O00O00O000OOO ,currentbldtxt as OO0OO000OOOO0O00O ,currentsptxt as O00O0OOOO0OO00O0O ,currentbldtxtwiz as OOOO0O0O0OOO00OO0 ,currentsptxtwiz as O00O00OO0O0OO0OO0 #line:36
from resources .lib import flush as O0O0OO00OO0O00O0O #line:38
from resources .lib import huisvrouw as O0000O000OO00OOO0 #line:39
from resources .lib import purge as O0O0OOOO00OOO00OO #line:40
from resources .lib import rpioc as OO0O0OOO00O0OO00O #line:41
from resources .lib import rpidev as OOOO0O0O00OO0OO0O #line:42
ADDON =OOO000OO0000O0OO0 .ADDON #line:44
ADDON_ID =OO00O0O00OO00OO0O .Addon ().getAddonInfo ('id')#line:46
AddonID ='script.xvbmc.updatertools'#line:47
AddonTitle ='XvBMC Nederland'#line:48
addonPath =OO000OOO0OO0O0OO0 .path .join (OO000OOO0OO0O0OO0 .path .join (O00O0000OO0O0O000 .translatePath ('special://home'),'addons'),'script.xvbmc.updatertools')#line:49
ART =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/addons/'+AddonID +'/resources/media/'))#line:50
artwork =O000OOO0O00OOO0O0 .b64decode ('c2tpbi5hZW9uLm5veC5zcGlu')#line:51
FANART =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/addons/'+AddonID ,'fanart.jpg'))#line:52
FANARTsub =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/addons/'+AddonID +'/resources/media/','art.jpg'))#line:53
ICON =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/addons/'+AddonID ,'icon.png'))#line:54
MainTitle ="XvBMC Nederland"#line:55
mediaPath =OO000OOO0OO0O0OO0 .path .join (addonPath ,'resources/media')#line:56
U =ADDON .getSetting ('User')#line:57
USER_AGENT ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'#line:58
About ='[COLOR dimgray][B]X[/B]v[B]BMC[/B] disclaimer & usage policy[/COLOR]'#line:60
Terug ='[COLOR dimgray]<<<back[/COLOR]'#line:61
dialog =OO0O00OO0O00O0OO0 .Dialog ()#line:63
dp =OO0O00OO0O00O0OO0 .DialogProgress ()#line:64
BASEURL ="https://bit.ly/XvBMC-Pi"#line:65
buildinfotxt ='[COLOR gray][B] - [/B]your wizard build: [I]unknown[/I] [/COLOR]'#line:66
serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: [I]unknown[/I] [/COLOR]'#line:67
xbmcver =O00O0000OO0O0O000 .getInfoLabel ("System.BuildVersion")[:4 ]#line:68
EXCLUDES =[ADDON_ID ,'plugin.program.xvbmcinstaller.nl','repository.xvbmc']#line:70
HOME =O00O0000OO0O0O000 .translatePath ('special://home/')#line:71
skin =O00O0000OO0O0O000 .getSkinDir ()#line:72
USERDATA =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/userdata',''))#line:73
USERADDONDATA =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/userdata/addon_data',''))#line:74
def resolver_settings ():#line:78
    import urlresolver as O0O00O0OO00O00O00 #line:79
    O0O00O0OO00O00O00 .display_settings ()#line:80
def mainMenu ():#line:83
    OOOO00O0000O0O0O0 ,O0OO0O0000OOO0O00 =OOO000OO0000O0OO0 .checkUpdate ()#line:85
    if OOOO00O0000O0O0O0 =="update":#line:86
       OOOO0OOOO0OO00OOO ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(O0OO0O0000OOO0O00 )+'[COLOR orange] (fork)[/COLOR]'#line:87
       OOO00O00O00000OO0 =O000OOO0O00OOO0O0 .b64decode (O0OOOO0000O0O0OO0 )+'update/sp/servicepack.zip'#line:88
       addDir ('%s'%OOOO0OOOO0OO00OOO ,OOO00O00O00000OO0 ,1 ,ART +'xvbmc.png',FANART ,'')#line:90
    elif OOOO00O0000O0O0O0 =="wizupdate":#line:91
       OOOO0OOOO0OO00OOO ="[COLOR orange]XvBMC update available[B]: %s[/B][/COLOR]"%(O0OO0O0000OOO0O00 )+'[COLOR orange] (wizard)[/COLOR]'#line:92
       OOO00O00O00000OO0 =O000OOO0O00OOO0O0 .b64decode (OO00O00O00O000OOO )+'wizardsp.zip'#line:93
       addDir ('%s'%OOOO0OOOO0OO00OOO ,OOO00O00O00000OO0 ,1 ,ART +'xvbmc.png',FANART ,'')#line:95
    elif OOOO00O0000O0O0O0 =="notinstalled":#line:99
       if O00O0000OO0O0O000 .getCondVisibility ('System.HasAddon(%s)'%(artwork )):#line:100
          if OO000OOO0OO0O0OO0 .path .isfile (OOO0000000OO0000O .bldversietxt ):#line:101
             OOOO0OOOO0OO00OOO ="[COLOR orange]Sorry (system) update status [B]unknown[/B], attempt to continue anyway [B]?[/B][/COLOR]"#line:102
             OOO00O00O00000OO0 =O000OOO0O00OOO0O0 .b64decode (O0OOOO0000O0O0OO0 )+'update/sp/servicepack.zip'#line:103
             addItem ('%s'%OOOO0OOOO0OO00OOO ,OOO00O00O00000OO0 ,1 ,ART +'xvbmc.png')#line:105
          elif OO000OOO0OO0O0OO0 .path .isfile (OOO0000000OO0000O .bldversietxtwiz ):#line:106
               OOOO0OOOO0OO00OOO ="[COLOR orange]Sorry (wizard) update status [B]unknown[/B], attempt to continue anyway [B]?[/B][/COLOR]"#line:107
               OOO00O00O00000OO0 =O000OOO0O00OOO0O0 .b64decode (OO00O00O00O000OOO )+'wizardsp.zip'#line:108
               addItem ('%s'%OOOO0OOOO0OO00OOO ,OOO00O00O00000OO0 ,1 ,ART +'xvbmc.png')#line:110
          else :#line:111
               OOOO0OOOO0OO00OOO ="[COLOR orange]unknown build status; force update?[/COLOR] [COLOR red][B](continue at your own risk)[/B][/COLOR]"#line:112
               OOO0OO00OO00O0O00 =O000OOO0O00OOO0O0 .b64decode (O0OOOO0000O0O0OO0 )+'update/sp/servicepack.zip'#line:113
               addItem ('%s'%OOOO0OOOO0OO00OOO ,OOO0OO00OO00O0O00 ,1 ,ART +'xvbmc.png')#line:115
       else :#line:116
          OOOO0OOOO0OO00OOO ="[COLOR orange]Sorry, [B]unknown[/B] build/servicepack/update status [B] :[/B]\'-([/COLOR]"#line:117
          addItem ('%s'%OOOO0OOOO0OO00OOO ,BASEURL ,4 ,ART +'xvbmc.png')#line:118
    else :#line:119
       OOOO0OOOO0OO00OOO ="[COLOR orange]You have the [B]latest[/B] XvBMC updates [B] :[/B]-)[/COLOR]"#line:120
       addItem ('%s'%OOOO0OOOO0OO00OOO ,BASEURL ,4 ,ART +'xvbmc.png')#line:121
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:123
    addDir ('[COLOR red]XvBMC Tools[/COLOR]',BASEURL ,10 ,ART +'tools.png',OO000OOO0OO0O0OO0 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:124
    addDir ('[COLOR white]XvBMC Maintenance[/COLOR]',BASEURL ,20 ,ART +'maint.png',OO000OOO0OO0O0OO0 .path .join (mediaPath ,"onderhoud.jpg"),'')#line:125
    addDir ('[COLOR dodgerblue]XvBMC About[/COLOR]',BASEURL ,2 ,ART +'wtf.png',OO000OOO0OO0O0OO0 .path .join (mediaPath ,"over.jpg"),'')#line:126
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:127
    addItem ('[COLOR gray]system information (kodi %s):[/COLOR]'%xbmcver ,BASEURL ,16 ,ART +'xvbmc.png')#line:128
    global serviceinfotxt #line:129
    O0O0OO0OOO00000O0 ,OO0OOOO0OOO00O0O0 =OOO0000000OO0000O .checkSPversie ()#line:130
    if O0O0OO0OOO00000O0 =="uwspversietxt":#line:131
       O0OOO0OOOO0O000OO =OOO000OO0000O0OO0 .getHtml2 (O00O0OOOO0OO00O0O )#line:132
       serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OO0OOOO0OOO00O0O0 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0OOO0OOOO0O000OO )#line:133
    elif O0O0OO0OOO00000O0 =="uwspversietxtwiz":#line:134
         O0OOO0OOOO0O000OO =OOO000OO0000O0OO0 .getHtml2 (O00O00OO0O0OO0OO0 )#line:135
         serviceinfotxt ='[COLOR gray][B] - [/B]your service pack: %s [/COLOR]'%(OO0OOOO0OOO00O0O0 +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0OOO0OOOO0O000OO )#line:136
    addItem ('%s'%serviceinfotxt ,BASEURL ,'',OO000OOO0OO0O0OO0 .path .join (mediaPath ,"wtf.png"))#line:137
    global buildinfotxt #line:138
    O0OOO0O0O00000O0O ,OO0OO0O00OOO0OOOO =OOO0000000OO0000O .checkXvbmcversie ()#line:139
    if O0OOO0O0O00000O0O =="bldversietxt":#line:140
       O0O0O00O00O0OO00O =OOO000OO0000O0OO0 .getHtml2 (OO0OO000OOOO0O00O )#line:141
       buildinfotxt ='[COLOR gray][B] - [/B]your system build: %s [/COLOR]'%(OO0OO0O00OOO0OOOO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0O0O00O00O0OO00O )#line:142
    elif O0OOO0O0O00000O0O =="bldversietxtwiz":#line:143
         O0O0O00O00O0OO00O =OOO000OO0000O0OO0 .getHtml2 (OOOO0O0O0OOO00OO0 )#line:144
         buildinfotxt ='[COLOR gray][B] - [/B]your wizard build: %s [/COLOR]'%(OO0OO0O00OOO0OOOO +' [COLOR dimgray][I](online: %s)[/I][/COLOR]'%O0O0O00O00O0OO00O )#line:145
    addItem ('%s'%buildinfotxt ,BASEURL ,'',OO000OOO0OO0O0OO0 .path .join (mediaPath ,"wtf.png"))#line:146
    if O00O0000OO0O0O000 .getCondVisibility ('System.HasAddon("service.openelec.settings")')+O00O0000OO0O0O000 .getCondVisibility ('System.HasAddon("service.libreelec.settings")'):#line:148
       addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:149
       addDir ('[COLOR orange]XvBMC Raspberry Pi [B] -[/B] Tools, DEV. & Maintenance[/COLOR]',BASEURL ,30 ,ART +'RPi.png',FANARTsub ,'')#line:150
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:152
    addItem (Terug ,BASEURL ,3 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:153
    OOO0000000OO0000O .setView ('movies','EPiC')#line:154
def XvBMCmaint ():#line:156
    addItem ('[B]B[/B]uild [COLOR red]purge[/COLOR] [COLOR dimgray](build [B]c[/B]rap[B]c[/B]leaner & fix evil addons/repos)[/COLOR]',BASEURL ,21 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:157
    addItem ('[B]C[/B]lear cache',BASEURL ,22 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:158
    addItem ('[B]D[/B]elete thumbnails',BASEURL ,23 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:159
    addItem ('[B]F[/B]lush add-ons [COLOR dimgray](salts HD/RD lite & Exodus \'cache+temp\' files)[/COLOR]',BASEURL ,24 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:160
    addItem ('[B]F[/B]ull \"auto\" clean [COLOR dimgray](cache, crashlogs, packages & thumbnails)[/COLOR]',BASEURL ,25 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:161
    addItem ('[B]P[/B]urge packages',BASEURL ,26 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:162
    addItem ('[B]R[/B]efresh addons[COLOR white]+[/COLOR]repos',BASEURL ,27 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:163
    if int (OOO000OO0000O0OO0 .kodiver )<=16.7 :#line:164
       addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s remove addons.db',BASEURL ,28 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:165
    elif int (OOO000OO0000O0OO0 .kodiver )>16.7 :#line:166
         addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s enable all add-ons [COLOR dimgray](Kodi 17+ Krypton)[/COLOR]',BASEURL ,29 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:167
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:169
    addItem (About ,BASEURL ,2 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"wtf.png"))#line:170
    addItem (Terug ,BASEURL ,3 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:171
    OOO0000000OO0000O .setView ('movies','EPiC')#line:172
def XvBMCtools1 ():#line:174
    addItem ('[B]C[/B]onvert physical paths (\'home\') to \'special\'',BASEURL ,11 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:175
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]most[/COLOR] add-ons)[/COLOR]',BASEURL ,12 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:176
    addItem ('[B]E[/B]nable Kodi Addons [COLOR dimgray](Kodi 17+ Krypton; [COLOR white]all[/COLOR] add-ons)[/COLOR]',BASEURL ,13 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:177
    addItem ('[B]E[/B]nable Kodi Live Streams [COLOR dimgray](17+ Krypton; [COLOR white]RTMP[/COLOR])[/COLOR]',BASEURL ,14 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:178
    addItem ('[B]F[/B]orce close Kodi  [COLOR dimgray](Kill Kodi)[/COLOR]',BASEURL ,15 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:179
    addItem ('[B]L[/B]og viewer [COLOR dimgray](show \'kodi.log\')[/COLOR]',BASEURL ,17 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:181
    addItem ('[B]U[/B]RLResolver -> settings',BASEURL ,18 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:182
    addItem ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s Advancedsettings unlocker [COLOR dimgray](reset)[/COLOR]',BASEURL ,19 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:183
    addDir ('[B][COLOR lime]X[/COLOR][/B]vBMC\'s [COLOR white][B]H[/B]idden [B]g[/B]ems[B] & [/B][B]M[/B]ore [B]t[/B]ools[/COLOR] [COLOR dimgray](TiP[B]!![/B])[/COLOR]',BASEURL ,40 ,ART +'xvbmc.png',OO000OOO0OO0O0OO0 .path .join (mediaPath ,"gereedschap.jpg"),'')#line:184
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:186
    addItem (About ,BASEURL ,2 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"wtf.png"))#line:187
    addItem (Terug ,BASEURL ,3 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:188
    OOO0000000OO0000O .setView ('movies','EPiC')#line:189
def XvBMCrpi ():#line:191
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] extreme crapcleaner [COLOR dimgray]([B]no[/B] factory reset)[/COLOR]',BASEURL ,31 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"tools.png"))#line:192
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] overclock [COLOR dimgray](raspberry Pi ***only***)[/COLOR]',BASEURL ,32 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"overclock.png"))#line:193
    addItem ('[COLOR white][B]R[/B][/COLOR]aspberry [COLOR white]Pi[/COLOR] #dev# corner [COLOR dimgray](firmware, OS, etc.)[/COLOR]',BASEURL ,33 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"firmware.png"))#line:194
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:196
    addItem (About ,BASEURL ,2 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"wtf.png"))#line:197
    addItem (Terug ,BASEURL ,3 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:198
    OOO0000000OO0000O .setView ('movies','EPiC')#line:199
def XvBMCtools2 ():#line:201
    addItem ('[B]K[/B]odi Quick Reset [COLOR dimgray](\"rejuvenate\" XvBMC-NL build)[/COLOR]',BASEURL ,41 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:203
    addItem ('[B]K[/B]odi Factory Reset [COLOR dimgray](complete Kodi Krypton wipe)[/COLOR]',BASEURL ,42 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:204
    addItem ('[B]K[/B]odi Fresh Start [COLOR dimgray](remove older Kodi\'s)[/COLOR]',BASEURL ,43 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:205
    addItem ('[B]P[/B]ush Fixes [COLOR dimgray](for XvBMC builds)[/COLOR]',BASEURL ,44 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"maint.png"))#line:206
    addItem ('',BASEURL ,'',ART +'xvbmc.png')#line:208
    addItem (About ,BASEURL ,2 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"wtf.png"))#line:209
    addItem (Terug ,BASEURL ,3 ,OO000OOO0OO0O0OO0 .path .join (mediaPath ,"xvbmc.png"))#line:210
    OOO0000000OO0000O .setView ('movies','EPiC')#line:211
def wizard (name ,url ):#line:215
    O0O0000O0OO00O0O0 =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/addons','packages'))#line:216
    if not OO000OOO0OO0O0OO0 .path .exists (O0O0000O0OO00O0O0 ):#line:217
        OO000OOO0OO0O0OO0 .makedirs (O0O0000O0OO00O0O0 )#line:218
    O00OO0O000OOO00OO =OO000OOO0OO0O0OO0 .path .join (O0O0000O0OO00O0O0 ,'default.zip')#line:219
    try :#line:220
       OO000OOO0OO0O0OO0 .remove (O00OO0O000OOO00OO )#line:221
    except :#line:222
       pass #line:223
    O0O000O00OOO0O00O .download (url ,O00OO0O000OOO00OO )#line:224
    if OO000OOO0OO0O0OO0 .path .exists (O00OO0O000OOO00OO ):#line:226
        O00O0O00O000OOO0O =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://','home'))#line:227
        OOO0OO00O0O00O0OO .sleep (2 )#line:228
        dp .create (MainTitle ,'XvBMC-NL: pull update VoOdOo...','','Please Wait')#line:230
        dp .update (0 ,"","***Extract ZIP - Please Wait")#line:231
        OOO0000000OO0000O .log ("==========================================================")#line:232
        OOO0000000OO0000O .log (O00O0O00O000OOO0O )#line:233
        OOO0000000OO0000O .log ("==========================================================")#line:234
        OOOO00O0OO0OO0000 .all (O00OO0O000OOO00OO ,O00O0O00O000OOO0O ,dp )#line:235
        dp .close ()#line:236
        try :OO000OOO0OO0O0OO0 .remove (O00OO0O000OOO00OO )#line:237
        except :pass #line:238
    if int (OOO000OO0000O0OO0 .kodiver )<=16.7 :#line:239
       dialog .ok (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  HINT  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:240
       OOO0000000OO0000O .forceRefresh (melding =False )#line:241
    elif int (OOO000OO0000O0OO0 .kodiver )>16.7 :#line:242
         OOO000OO0000O0OO0 .enableAddons (melding =False )#line:243
         OOO0OO00O0O00O0OO .sleep (0.5 )#line:244
         O000O0OOO0O0O0O00 =OO0O00OO0O00O0OO0 .Dialog ().yesno (MainTitle +" : Update [COLOR green][B]finished[/B][/COLOR]",'[COLOR orange][B]!!!  SUCCESS  !!![/B][/COLOR]','[B]IF[/B] add-ons do NOT work you probably should reboot.','(een REBOOT van uw systeem is VEELAL wenselijk)',yeslabel ='[COLOR lime]Reboot[/COLOR]',nolabel ='[COLOR red]Continue[/COLOR]')#line:245
         if O000O0OOO0O0O0O00 ==1 :#line:246
            OOO0OO00O0O00O0OO .sleep (1 )#line:247
            OOO0000000OO0000O .killKodi ()#line:248
         elif O000O0OOO0O0O0O00 ==0 :#line:249
              if int (OOO000OO0000O0OO0 .kodiver )>16.7 :#line:250
                 OOO000OO0000O0OO0 .enableAddons (melding =False )#line:251
                 OOO0OO00O0O00O0OO .sleep (0.5 )#line:252
                 dialog .ok (MainTitle +" : [COLOR red]add-ons[/COLOR] [COLOR green][B]enabled[/B][/COLOR]",'[COLOR orange][B]!!!  TIP  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete...','[B]Herstart[/B] Kodi ter afronding')#line:253
                 O00O0000OO0O0O000 .executebuiltin ('ReloadSkin()')#line:254
    O00O0000OO0O0O000 .executebuiltin ("Container.Refresh")#line:255
    O00O0000OO0O0O000 .sleep (5000 )#line:256
def unlocker ():#line:261
    dialog .ok (MainTitle +" - unlocker",' ','unlock advancedsettings for this build','[COLOR dimgray](+reset \'advancedsettings.xml\' -use at your own risk)[/COLOR]')#line:263
    OO00OOOO000OO00OO =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join ('special://home/userdata/'))#line:264
    O000O000OOO0O00OO =O000OOO0O00OOO0O0 .b64decode ('YWR2YW5jZWRzZXR0aW5ncy54bWw=')#line:265
    OO00OOO00000OO00O =True #line:266
    try :#line:267
        OO000OOO0OO0O0OO0 .unlink (OO00OOOO000OO00OO +O000O000OOO0O00OO )#line:268
    except :#line:269
        OO00OOO00000OO00O =False #line:270
    if OO00OOO00000OO00O :#line:272
        dialog .ok (MainTitle +" - [B]UNLOCKED[/B]",'[COLOR green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Herstart[/B] Kodi ter afronding \'unlocker\' (force close)','[B]Reboot[/B] Kodi to complete \'unlocker\' (force close)')#line:273
        OO000OOO0OO0O0OO0 ._exit (1 )#line:274
    else :#line:275
        dialog .ok (MainTitle +" - [B]OOOOOOPS[/B]",'[COLOR red][B]!!!  Failed  !!![/B][/COLOR]','[B]Nope![/B] helaas geen succes (niks te \'unlocken\')','[B]Nope![/B] close but no cigar  (nothing to \'unlock\')')#line:276
def XvbmcOc ():#line:279
    O00O0OO00OOO000OO =O0OO00O00O00O0O00 ()#line:280
    OOO0000000OO0000O .log ("Platform: "+str (O00O0OO00OOO000OO ))#line:281
    if not O00O0OO00OOO000OO =='linux':#line:282
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] OverClock!",OO0O000O0O0O000OO ,OOO0OOOOO00OOOO00 ,OO0OOOOOO0OOOO00O )#line:283
       OOO0000000OO0000O .log ("none Linux OS ie. Open-/LibreELEC")#line:284
    else :#line:285
        OOO0000000OO0000O .log ("linux os")#line:286
        OO0O0OOO00O0OO00O .ocMenu ()#line:287
def XvbmcDev ():#line:290
    O0O000OO00000000O =O0OO00O00O00O0O00 ()#line:291
    OOO0000000OO0000O .log ("Platform: "+str (O0O000OO00000000O ))#line:292
    if not O0O000OO00000000O =='linux':#line:293
       dialog .ok (MainTitle +" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] #dev#",OO0O000O0O0O000OO ,OOO0OOOOO00OOOO00 ,OO0OOOOOO0OOOO00O )#line:294
       OOO0000000OO0000O .log ("none Linux OS ie. Open-/LibreELEC")#line:295
    else :#line:296
        OOO0000000OO0000O .log ("linux os")#line:297
        OOOO0O0O00OO0OO0O .devMenu ()#line:298
def disabled ():#line:301
    OOO0000000OO0000O .okDialog ('[COLOR red][B]Sorry, disabled! [/B](for now)[/COLOR]','','[COLOR lime]goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')#line:302
def rejuvXvbmc ():#line:305
    O00OOOOO00OOOO00O =OOO0000000OO0000O .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Wilt u uw XvBMC \'build\' volledig opschonen (wipe) en Kodi Krypton [B]leeg[/B] her-configureren?','[COLOR dimgray]Please confirm that you wish you wipe clean your current configuration and reconfigure Kodi.[/COLOR]')#line:306
    if O00OOOOO00OOOO00O :#line:307
        O0O0O00OOO0O0OOO0 =OO00O0O00OO00OO0O .Addon (id =AddonID ).getAddonInfo ('path');O0O0O00OOO0O0OOO0 =O00O0000OO0O0O000 .translatePath (O0O0O00OOO0O0OOO0 );#line:308
        O000OO0OO000OOO00 =OO000OOO0OO0O0OO0 .path .join (O0O0O00OOO0O0OOO0 ,"..","..");O000OO0OO000OOO00 =OO000OOO0OO0O0OO0 .path .abspath (O000OO0OO000OOO00 );OOO0000000OO0000O .log ("rejuvXvbmc.main_XvBMC: xbmcPath="+O000OO0OO000OOO00 );#line:309
        O0000OOO0OOO000O0 =('addons','Database','packages','userdata')#line:311
        O000OOO00O000O0OO =('metadata.album.universal','metadata.artists.universal','metadata.common.imdb.com','metadata.common.musicbrainz.org','metadata.common.theaudiodb.com','metadata.common.themoviedb.org','metadata.themoviedb.org','metadata.tvdb.com','plugin.program.super.favourites','plugin.program.xvbmcinstaller.nl','repository.xvbmc','resource.language.nl_nl','script.xvbmc.updatertools','service.xbmc.versioncheck','skin.aeon.nox.spin','script.grab.fanart','service.library.data.provider','resource.images.recordlabels.white','resource.images.studios.coloured','resource.images.studios.white','xbmc.gui','script.skinshortcuts','script.module.simplejson','script.module.unidecode')#line:317
        OO0OO0OOO00OOO0O0 =('Addons26.db','Addons27.db','guisettings.xml','kodi.log','Textures13.db')#line:319
        OOOOOO000OOOOOO00 =OOO0000000OO0000O .message_yes_no ("[COLOR white][B]"+AddonTitle +"[/B][/COLOR]",'Wilt u het XvBMC-NL basis \'framework\' handhaven na reset? Verwijderd alles behalve XvBMC (aanbeveling).','[COLOR dimgray](do you wish to keep XvBMC\'s default framework?)[/COLOR]')#line:320
        if OOOOOO000OOOOOO00 :#line:321
            O0000OOO0OOO000O0 =O0000OOO0OOO000O0 +('addon_data','keymaps','media',)#line:322
            O000OOO00O000O0OO =O000OOO00O000O0OO +('inputstream.rtmp','keymaps','media','service.subtitles.addic7ed','service.subtitles.opensubtitles_by_opensubtitles','service.subtitles.opensubtitlesBeta','service.subtitles.podnapisi','service.subtitles.subscene',)#line:323
            OO0OO0OOO00OOO0O0 =OO0OO0OOO00OOO0O0 +('advancedsettings.xml','favourites.xml','profiles.xml','RssFeeds.xml','sources.xml','versiebld.txt','versiesp.txt','wizbld.txt','wizsp.txt',)#line:324
        else :#line:325
            O0000OOO0OOO000O0 =O0000OOO0OOO000O0 +('addon_data',)#line:326
            O000OOO00O000O0OO =O000OOO00O000O0OO +('inputstream.rtmp',)#line:327
            OO0OO0OOO00OOO0O0 =OO0OO0OOO00OOO0O0 +('advancedsettings.xml','RssFeeds.xml',)#line:328
            OOO0O0OOO0O00OO0O =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join (USERADDONDATA ,'plugin.program.super.favourites','Super Favourites'))#line:329
            OOO0O0O0OOO000OOO =O00O0000OO0O0O000 .translatePath (OO000OOO0OO0O0OO0 .path .join (USERDATA ,'addon_data','script.skinshortcuts'))#line:330
            try :#line:331
                OOO000000O0O000O0 .rmtree (OOO0O0OOO0O00OO0O )#line:332
            except Exception as O000OOOOO0O0OO00O :OOO0000000OO0000O .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (O000OOOOO0O0OO00O ))#line:333
            try :#line:334
                OOO000000O0O000O0 .rmtree (OOO0O0O0OOO000OOO )#line:335
            except Exception as O000OOOOO0O0OO00O :OOO0000000OO0000O .log ("rejuvXvbmc.keep_xvbmc: XvBMC-vOoDoO @ "+str (O000OOOOO0O0OO00O ))#line:336
        dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Reset![/B][/COLOR]",'Snelle XvBMC Krypton reset, even geduld...','','[COLOR dimgray](Quick XvBMC Krypton reset, please wait...)[/COLOR]')#line:337
        try :#line:338
            for OOO0O000OO0O0O0OO ,OOOO0OO0O00O0OO00 ,OOOO0000O0O0000O0 in OO000OOO0OO0O0OO0 .walk (O000OO0OO000OOO00 ,topdown =True ):#line:339
                OOOO0OO0O00O0OO00 [:]=[O0O0O00OOO00O0OO0 for O0O0O00OOO00O0OO0 in OOOO0OO0O00O0OO00 if O0O0O00OOO00O0OO0 not in O000OOO00O000O0OO ]#line:340
                OOOO0000O0O0000O0 [:]=[O0OO00OO00O0OO00O for O0OO00OO00O0OO00O in OOOO0000O0O0000O0 if O0OO00OO00O0OO00O not in OO0OO0OOO00OOO0O0 ]#line:341
                for O0O00O0OOOO0OO0OO in OOOO0000O0O0000O0 :#line:342
                    try :#line:343
                        dp .update (11 ,'','***Cleaning files...')#line:344
                        OO000OOO0OO0O0OO0 .remove (OO000OOO0OO0O0OO0 .path .join (OOO0O000OO0O0O0OO ,O0O00O0OOOO0OO0OO ))#line:345
                    except Exception as O000OOOOO0O0OO00O :OOO0000000OO0000O .log ("rejuvXvbmc.file_name: User files partially removed - "+str (O000OOOOO0O0OO00O ))#line:347
                for O0OOO0000O0OO0O00 in OOOO0OO0O00O0OO00 :#line:348
                    if O0OOO0000O0OO0O00 not in O0000OOO0OOO000O0 :#line:349
                        try :#line:350
                            dp .update (33 ,'','***Cleaning folders...')#line:351
                            OOO000000O0O000O0 .rmtree (OO000OOO0OO0O0OO0 .path .join (OOO0O000OO0O0O0OO ,O0OOO0000O0OO0O00 ))#line:352
                        except Exception as O000OOOOO0O0OO00O :OOO0000000OO0000O .log ("rejuvXvbmc.folder: User folders partially removed - "+str (O000OOOOO0O0OO00O ))#line:354
            dp .update (66 ,'','***Crap Cleaning...')#line:355
            OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ()#line:356
        except Exception as O000OOOOO0O0OO00O :#line:357
            OOO0000000OO0000O .log ("rejuvXvbmc: User stuff partially removed - "+str (O000OOOOO0O0OO00O ))#line:358
            OOO0000000OO0000O .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Error![/B][/COLOR]",'...DAT ging niet helemaal goed, controleer uw log...','[COLOR dimgray](XvBMC user files partially removed, please check log)[/COLOR]')#line:359
            O0OO000OOO00O00O0 .exit ()#line:360
        dp .update (99 ,'','***Cleaning Crap...')#line:361
        OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:362
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:363
        OO000OOO0OO0O0OO0 ._exit (1 )#line:364
    else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:365
def WipeXBMC ():#line:368
    if skin !="skin.estuary":#line:369
        dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'selecteer eerst de standaard (Estuary) skin alvorens een volledige [B]\'wipe\'[/B] van uw Kodi uit te voeren.','','[COLOR dimgray](before Kodi wipe, select Estuary skin first)[/COLOR]')#line:370
        O00O0000OO0O0O000 .executebuiltin ("ActivateWindow(InterfaceSettings)")#line:371
        return #line:372
    else :#line:373
        OO00OOOO000000OOO =OO0O00OO0O00O0OO0 .Dialog ().yesno ("[COLOR lime][B]BELANGRIJK / IMPORTANT / HINT[/B][/COLOR]",'[B]let op: [/B]dit zal alles verwijderen van uw huidige Kodi installatie, weet u zeker dat u wilt doorgaan[B]?[/B]','','[COLOR dimgray](this will remove your current Kodi build, continue?)[/COLOR]',yeslabel ='[COLOR lime][B]JA/YES[/B][/COLOR]',nolabel ='[COLOR red]nee/nope[/COLOR]')#line:374
        if OO00OOOO000000OOO ==1 :#line:375
           dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- Wipe![/B][/COLOR]",'verwijder alles, even geduld...','','[COLOR dimgray](remove everything, please wait...)[/COLOR]')#line:376
           try :#line:377
               for O0OOOOOO00OOOOO0O ,O00OOOO000OOOO0O0 ,O000O0O0O0OO0OO0O in OO000OOO0OO0O0OO0 .walk (HOME ,topdown =True ):#line:378
                    O00OOOO000OOOO0O0 [:]=[OO000OO00O0OO0O00 for OO000OO00O0OO0O00 in O00OOOO000OOOO0O0 if OO000OO00O0OO0O00 not in EXCLUDES ]#line:379
                    for OOOOO0O0OOOO0000O in O000O0O0O0OO0OO0O :#line:380
                        try :dp .update (11 ,'','***Cleaning files...');OO000OOO0OO0O0OO0 .remove (OO000OOO0OO0O0OO0 .path .join (O0OOOOOO00OOOOO0O ,OOOOO0O0OOOO0000O ));OO000OOO0OO0O0OO0 .rmdir (OO000OOO0OO0O0OO0 .path .join (O0OOOOOO00OOOOO0O ,OOOOO0O0OOOO0000O ))#line:381
                        except :pass #line:382
                    for OOOOO0O0OOOO0000O in O00OOOO000OOOO0O0 :#line:383
                        try :dp .update (33 ,'','***Cleaning folders...');OO000OOO0OO0O0OO0 .rmdir (OO000OOO0OO0O0OO0 .path .join (O0OOOOOO00OOOOO0O ,OOOOO0O0OOOO0000O ));OO000OOO0OO0O0OO0 .rmdir (O0OOOOOO00OOOOO0O )#line:384
                        except :pass #line:385
               dp .update (66 ,'','***Crap Cleaning...')#line:386
               OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ()#line:387
           except :pass #line:388
           dp .update (99 ,'','***Cleaning Crap...')#line:389
           OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:390
           dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'Kodi zal nu afsluiten...','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:391
           OO000OOO0OO0O0OO0 ._exit (1 )#line:392
        elif OO00OOOO000000OOO ==0 :#line:393
             dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen Kodi Krypton \'wipe\' uitgevoerd...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:394
def FRESHSTART (params ):#line:397
    if int (OOO000OO0000O0OO0 .kodiver )>16.7 :#line:398
       dialog .ok ("[COLOR lime]"+MainTitle +"[/COLOR] [COLOR red][B]- NOPE![/B][/COLOR]",'[COLOR orange][B]NOTE:[/B][/COLOR]','[COLOR white]alleen voor oudere Kodi\'s dan Krypton (>17.0)[/COLOR]','[COLOR dimgray](for use with older Kodi\'s only (>17.0)[/COLOR]')#line:399
    else :#line:400
        OOO0000000OO0000O .log ("freshstart.main_XvBMC: "+repr (params ));OO0OOOO0OO0O0O0O0 =OOO0000000OO0000O .message_yes_no ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Remove[/B][/COLOR]",'Kodi terugzetten naar de standaard fabrieksinstellingen?','[COLOR dimgray](reset Kodi to factory defaults)[/COLOR]')#line:401
        if OO0OOOO0OO0O0O0O0 :#line:402
            OOOO0O0O0O00000O0 =OO00O0O00OO00OO0O .Addon (id =AddonID ).getAddonInfo ('path');OOOO0O0O0O00000O0 =O00O0000OO0O0O000 .translatePath (OOOO0O0O0O00000O0 );#line:403
            OOOOOO0O0OO00O00O =OO000OOO0OO0O0OO0 .path .join (OOOO0O0O0O00000O0 ,"..","..");OOOOOO0O0OO00O00O =OO000OOO0OO0O0OO0 .path .abspath (OOOOOO0O0OO00O00O );OOO0000000OO0000O .log ("freshstart.main_XvBMC: xbmcPath="+OOOOOO0O0OO00O00O );OOOO0OO0O00000000 =False #line:404
            dp .create ("[COLOR white]"+AddonTitle +"[/COLOR] [COLOR red][B]- FreshStart![/B][/COLOR]",'terug naar fabrieksinstellingen, even geduld...','','[COLOR dimgray](factory reset Kodi, please wait...)[/COLOR]')#line:405
            try :#line:406
                for OO0O0O00O0000O00O ,OOOO0O0OO0O00OO00 ,OO00OO0OOOOO00000 in OO000OOO0OO0O0OO0 .walk (OOOOOO0O0OO00O00O ,topdown =True ):#line:407
                    OOOO0O0OO0O00OO00 [:]=[OOOO0O00OO0OO00OO for OOOO0O00OO0OO00OO in OOOO0O0OO0O00OO00 if OOOO0O00OO0OO00OO not in EXCLUDES ]#line:408
                    dp .update (33 ,'','***Cleaning files+folders...')#line:409
                    for O00000OO0OO00O0O0 in OO00OO0OOOOO00000 :#line:410
                        try :OO000OOO0OO0O0OO0 .remove (OO000OOO0OO0O0OO0 .path .join (OO0O0O00O0000O00O ,O00000OO0OO00O0O0 ))#line:411
                        except :#line:412
                            if O00000OO0OO00O0O0 not in ["Addons1.db","MyMusic7","MyVideos37.db","Textures1.db","xbmc.log"]:OOOO0OO0O00000000 =True #line:413
                            OOO0000000OO0000O .log ("XvBMC-Error removing file: "+OO0O0O00O0000O00O +" "+O00000OO0OO00O0O0 )#line:414
                    for O00000OO0OO00O0O0 in OOOO0O0OO0O00OO00 :#line:415
                        try :OO000OOO0OO0O0OO0 .rmdir (OO000OOO0OO0O0OO0 .path .join (OO0O0O00O0000O00O ,O00000OO0OO00O0O0 ))#line:416
                        except :#line:417
                            if O00000OO0OO00O0O0 not in ["Database","userdata"]:OOOO0OO0O00000000 =True #line:418
                            OOO0000000OO0000O .log ("XvBMC-Error removing folder: "+OO0O0O00O0000O00O +" "+O00000OO0OO00O0O0 )#line:419
                dp .update (66 ,'','***Crap Cleaning...')#line:420
                OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ()#line:421
                if not OOOO0OO0O00000000 :OOO0000000OO0000O .log ("freshstart.main_XvBMC: All user files removed, you now have a CLEAN install");OOO0000000OO0000O .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:422
                else :OOO0000000OO0000O .log ("freshstart.main_XvBMC: User files partially removed");OOO0000000OO0000O .message ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Voltooid![/B][/COLOR]",'\'FreshStart\' is klaar, verse Kodi beschikbaar na herstart...','[COLOR dimgray](\'FreshStart\' finished, fresh Kodi available after reboot)[/COLOR]')#line:423
            except :OOO0000000OO0000O .message ("[COLOR red][B]"+AddonTitle +"[/B][/COLOR]",'Problem found','Your settings have [B]not[/B] been changed');import traceback as OOOO00OOOOOOO0000 ;OOO0000000OO0000O .log (OOOO00OOOOOOO0000 .format_exc ());OOO0000000OO0000O .log ("freshstart.main_XvBMC: NOTHING removed");O0OO000OOO00O00O0 .exit ()#line:424
            dp .update (99 ,'','***Cleaning Crap...')#line:425
            OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();OOO0000000OO0000O .REMOVE_EMPTY_FOLDERS ();dp .close ()#line:426
            dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR lime][B]- Reboot![/B][/COLOR]",'Kodi zal nu afsluiten','','[COLOR dimgray](shutdown Kodi now)[/COLOR]')#line:427
            OO000OOO0OO0O0OO0 ._exit (1 )#line:428
        else :dialog .ok ("[COLOR dodgerblue]"+AddonTitle +"[/COLOR] [COLOR red][B]- Cancelled![/B][/COLOR]",'Er is geen schone installatie gedaan...','','[COLOR dimgray](interrupted by user)[/COLOR]')#line:429
def addItem (name ,url ,mode ,iconimage ):#line:433
    OO0OOOO0O0O00O00O =O0OO000OOO00O00O0 .argv [0 ]+"?url="+OOO000O00O000OO00 .quote_plus (url )+"&mode="+str (mode )+"&name="+OOO000O00O000OO00 .quote_plus (name )#line:434
    OO0OO00OOO0O0O000 =True #line:435
    OO000OO0OO0O0OOOO =OO0O00OO0O00O0OO0 .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:436
    OO000OO0OO0O0OOOO .setInfo (type ="Video",infoLabels ={"Title":name })#line:437
    OO000OO0OO0O0OOOO .setArt ({'fanart':FANART })#line:438
    OO0OO00OOO0O0O000 =O0O0O0OOOOOOOOOO0 .addDirectoryItem (handle =int (O0OO000OOO00O00O0 .argv [1 ]),url =OO0OOOO0O0O00O00O ,listitem =OO000OO0OO0O0OOOO ,isFolder =False )#line:439
    return OO0OO00OOO0O0O000 #line:440
def get_params ():#line:443
        OO00O0O0O0O0O0O00 =[]#line:444
        O00OOO00O0000O0OO =O0OO000OOO00O00O0 .argv [2 ]#line:445
        if len (O00OOO00O0000O0OO )>=2 :#line:446
                OOO0O0O0OO0OOO000 =O0OO000OOO00O00O0 .argv [2 ]#line:447
                OOOOO0O0O000OO00O =OOO0O0O0OO0OOO000 .replace ('?','')#line:448
                if (OOO0O0O0OO0OOO000 [len (OOO0O0O0OO0OOO000 )-1 ]=='/'):#line:449
                        OOO0O0O0OO0OOO000 =OOO0O0O0OO0OOO000 [0 :len (OOO0O0O0OO0OOO000 )-2 ]#line:450
                O00OOOOOOOO0O0OO0 =OOOOO0O0O000OO00O .split ('&')#line:451
                OO00O0O0O0O0O0O00 ={}#line:452
                for O0O00OO00OO00O0OO in range (len (O00OOOOOOOO0O0OO0 )):#line:453
                        OOO0000O00OOO0OO0 ={}#line:454
                        OOO0000O00OOO0OO0 =O00OOOOOOOO0O0OO0 [O0O00OO00OO00O0OO ].split ('=')#line:455
                        if (len (OOO0000O00OOO0OO0 ))==2 :#line:456
                                OO00O0O0O0O0O0O00 [OOO0000O00OOO0OO0 [0 ]]=OOO0000O00OOO0OO0 [1 ]#line:457
        return OO00O0O0O0O0O0O00 #line:458
def addDir (name ,url ,mode ,iconimage ,fanart ,description ):#line:461
        O0OOOOO00OOOOOO00 =O0OO000OOO00O00O0 .argv [0 ]+"?url="+OOO000O00O000OO00 .quote_plus (url )+"&mode="+str (mode )+"&name="+OOO000O00O000OO00 .quote_plus (name )+"&iconimage="+OOO000O00O000OO00 .quote_plus (iconimage )+"&fanart="+OOO000O00O000OO00 .quote_plus (fanart )+"&description="+OOO000O00O000OO00 .quote_plus (description )#line:462
        O00O0OOOO0O0OO0O0 =True #line:463
        O00O0OO0O0O0OOO0O =OO0O00OO0O00O0OO0 .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:464
        O00O0OO0O0O0OOO0O .setInfo (type ="Video",infoLabels ={"Title":name ,"Plot":description })#line:465
        O00O0OO0O0O0OOO0O .setProperty ("Fanart_Image",fanart )#line:466
        if mode ==1 :#line:467
            O00O0OOOO0O0OO0O0 =O0O0O0OOOOOOOOOO0 .addDirectoryItem (handle =int (O0OO000OOO00O00O0 .argv [1 ]),url =O0OOOOO00OOOOOO00 ,listitem =O00O0OO0O0O0OOO0O ,isFolder =False )#line:468
        elif mode ==2 :#line:469
            O00O0OOOO0O0OO0O0 =O0O0O0OOOOOOOOOO0 .addDirectoryItem (handle =int (O0OO000OOO00O00O0 .argv [1 ]),url =O0OOOOO00OOOOOO00 ,listitem =O00O0OO0O0O0OOO0O ,isFolder =False )#line:470
        else :#line:471
            O00O0OOOO0O0OO0O0 =O0O0O0OOOOOOOOOO0 .addDirectoryItem (handle =int (O0OO000OOO00O00O0 .argv [1 ]),url =O0OOOOO00OOOOOO00 ,listitem =O00O0OO0O0O0OOO0O ,isFolder =True )#line:472
        return O00O0OOOO0O0OO0O0 #line:473
params =get_params ()#line:476
url =None #line:477
name =None #line:478
mode =None #line:479
iconimage =None #line:480
fanart =None #line:481
description =None #line:482
try :#line:485
        url =OOO000O00O000OO00 .unquote_plus (params ["url"])#line:486
except :#line:487
        pass #line:488
try :#line:489
        name =OOO000O00O000OO00 .unquote_plus (params ["name"])#line:490
except :#line:491
        pass #line:492
try :#line:493
        iconimage =OOO000O00O000OO00 .unquote_plus (params ["iconimage"])#line:494
except :#line:495
        pass #line:496
try :#line:497
        mode =int (params ["mode"])#line:498
except :#line:499
        pass #line:500
try :#line:501
        fanart =OOO000O00O000OO00 .unquote_plus (params ["fanart"])#line:502
except :#line:503
        pass #line:504
try :#line:505
        description =OOO000O00O000OO00 .unquote_plus (params ["description"])#line:506
except :#line:507
        pass #line:508
OOO0000000OO0000O .log ("EPiC "+str (AddonTitle ))#line:512
if mode ==None or url ==None or len (url )<1 :#line:520
   mainMenu ()#line:521
elif mode ==1 :#line:523
     wizard (name ,url )#line:525
elif mode ==10 :#line:527
     XvBMCtools1 ()#line:528
elif mode ==20 :#line:530
     XvBMCmaint ()#line:531
elif mode ==30 :#line:533
     XvBMCrpi ()#line:534
elif mode ==2 :#line:536
     OOO0000000OO0000O .AboutXvBMC ()#line:537
elif mode ==3 :#line:539
     OOO0000000OO0000O .closeandexit ()#line:540
elif mode ==4 :#line:542
     OOO0000000OO0000O .okDialog (OO0O000O0O0O000OO ,'sorry, nothing todo...','with kind regards, team [COLOR green]XvBMC Nederland[/COLOR]')#line:543
elif mode ==11 :#line:545
     O0000O000OO00OOO0 .Fix_Special (url )#line:546
elif mode ==12 :#line:548
     O0000O000OO00OOO0 .AddonsEnable ()#line:549
elif mode ==13 :#line:551
     OO0OO000O00O0O00O .setall_enable ()#line:552
elif mode ==14 :#line:554
     O0000O000OO00OOO0 .EnableRTMP ()#line:555
elif mode ==15 :#line:557
     OOO0000000OO0000O .killKodi ()#line:558
elif mode ==16 :#line:560
     OOO0000000OO0000O .KODIVERSION (url )#line:561
elif mode ==17 :#line:563
     O0000O000OO00OOO0 .xvbmcLog ()#line:564
elif mode ==18 :#line:566
     resolver_settings ()#line:567
elif mode ==19 :#line:569
     unlocker ()#line:570
elif mode ==21 :#line:572
     O0O0OOOO00OOO00OO .purgeOLD ()#line:573
elif mode ==22 :#line:575
     O0000O000OO00OOO0 .clearCache ()#line:576
elif mode ==23 :#line:578
     O0000O000OO00OOO0 .deleteThumbnails ()#line:579
elif mode ==24 :#line:581
     O0O0OO00OO0O00O0O .flushMenu ()#line:582
elif mode ==25 :#line:584
     O0000O000OO00OOO0 .autocleanask ()#line:585
elif mode ==26 :#line:587
     O0000O000OO00OOO0 .purgePackages ()#line:588
elif mode ==27 :#line:590
     OOO0000000OO0000O .forceRefresh (melding =True )#line:591
elif mode ==28 :#line:593
     O0000O000OO00OOO0 .AddonsDatabaseRemoval ()#line:594
elif mode ==29 :#line:596
     OOO000OO0000O0OO0 .enableAddons (melding =True )#line:597
elif mode ==31 :#line:599
     O0000O000OO00OOO0 .PiCCleaner ()#line:600
elif mode ==32 :#line:602
     XvbmcOc ()#line:603
elif mode ==33 :#line:605
     XvbmcDev ()#line:606
elif mode ==40 :#line:608
     XvBMCtools2 ()#line:609
elif mode ==41 :#line:611
     rejuvXvbmc ()#line:612
elif mode ==42 :#line:614
     WipeXBMC ()#line:615
elif mode ==43 :#line:617
     FRESHSTART (params )#line:618
elif mode ==44 :#line:620
     disabled ()#line:621
O0O0O0OOOOOOOOOO0 .endOfDirectory (int (O0OO000OOO00O00O0 .argv [1 ]))