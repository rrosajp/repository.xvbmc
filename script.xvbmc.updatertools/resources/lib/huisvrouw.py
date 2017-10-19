#!/usr/bin/python
"""
    IF you copy/paste 'huisvrouw.py' please keep the credits -2- XvBMC-NL, Thx.
"""#line:6
import xbmc ,xbmcaddon ,xbmcgui ,xbmcplugin #line:25
import os ,re ,shutil ,time #line:26
import sqlite3 #line:27
import addon_able #line:28
import common as Common #line:29
from common import platform ,subtitleNope ,nonlinux ,nonelecNL #line:30
from common import log #line:31
AddonID ='script.xvbmc.updatertools'#line:35
ADDON =xbmcaddon .Addon (id =AddonID )#line:36
thumbnailPath =xbmc .translatePath ('special://thumbnails');#line:38
cachePath =os .path .join (xbmc .translatePath ('special://home'),'cache')#line:39
tempPath =xbmc .translatePath ('special://temp')#line:40
databasePath =xbmc .translatePath ('special://database')#line:41
dialog =xbmcgui .Dialog ()#line:42
dp =xbmcgui .DialogProgress ()#line:43
kodiver =xbmc .getInfoLabel ("System.BuildVersion").split (".")[0 ]#line:44
MainTitle ="XvBMC Nederland"#line:45
SubTitle =" [B]-[/B] [COLOR lime]RPi[/COLOR] [B]-[/B] CrapCleaner!"#line:46
Windows =xbmc .translatePath ('special://home')#line:47
WindowsCache =xbmc .translatePath ('special://home')#line:48
OtherCache =xbmc .translatePath ('special://home/temp')#line:49
class cacheEntry :#line:56
    def __init__ (self ,namei ,pathi ):#line:57
        self .name =namei #line:58
        self .path =pathi #line:59
def setupCacheEntries ():#line:66
    O000OOOOO00OO000O =6 #line:67
    OOOOO0000000O0OO0 =["MP3 Streams","Quasar","SportsDevil","Simple Downloader","Spotitube","SkinHelperService"]#line:68
    OOOO0O0OO00OOO00O =["special://profile/addon_data/plugin.audio.mp3streams/temp_dl","special://profile/addon_data/plugin.video.quasar/cache","special://profile/addon_data/plugin.video.SportsDevil/cache","special://profile/addon_data/script.module.simple.downloader","special://profile/addon_data/plugin.video.spotitube/cache","special://profile/addon_data/script.skin.helper.service/musicartcache"]#line:74
    O00O0O0OO000OO0OO =[]#line:76
    for O00OO0000O0OOOO00 in range (O000OOOOO00OO000O ):#line:78
        O00O0O0OO000OO0OO .append (cacheEntry (OOOOO0000000O0OO0 [O00OO0000O0OOOO00 ],OOOO0O0OO00OOO00O [O00OO0000O0OOOO00 ]))#line:79
    return O00O0O0OO000OO0OO #line:81
def clearCache ():#line:88
    if os .path .exists (cachePath )==True :#line:89
        for O0O0O0000OOO00O00 ,O00O0O0OOOOOO0000 ,OO0OO00O0O0000O00 in os .walk (cachePath ):#line:90
            O00O0O0000OOOOO0O =0 #line:91
            O00O0O0000OOOOO0O +=len (OO0OO00O0O0000O00 )#line:92
            if O00O0O0000OOOOO0O >0 :#line:93
                if dialog .yesno ("Delete Cache Files",str (O00O0O0000OOOOO0O )+' files found','Do you want to delete them?'):#line:95
                    for OOOOOO000OOOOOO0O in OO0OO00O0O0000O00 :#line:96
                        try :#line:97
                            if (OOOOOO000OOOOOO0O .endswith (".log")):continue #line:99
                            os .unlink (os .path .join (O0O0O0000OOO00O00 ,OOOOOO000OOOOOO0O ))#line:100
                        except :#line:101
                            pass #line:102
                    for OOOO00O0000O0OO00 in O00O0O0OOOOOO0000 :#line:103
                        try :#line:104
                            OOO00OOO0OO000000 =(os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:106
                            if not "archive_cache"in str (OOO00OOO0OO000000 ):#line:107
                                shutil .rmtree (os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:108
                        except :#line:109
                            pass #line:110
            else :#line:111
                pass #line:112
    if os .path .exists (tempPath )==True :#line:114
        for O0O0O0000OOO00O00 ,O00O0O0OOOOOO0000 ,OO0OO00O0O0000O00 in os .walk (tempPath ):#line:115
            O00O0O0000OOOOO0O =0 #line:116
            O00O0O0000OOOOO0O +=len (OO0OO00O0O0000O00 )#line:117
            if O00O0O0000OOOOO0O >0 :#line:118
                if dialog .yesno ("Delete Temp Files",str (O00O0O0000OOOOO0O )+' files found','Do you want to delete them?'):#line:120
                    for OOOOOO000OOOOOO0O in OO0OO00O0O0000O00 :#line:121
                        try :#line:122
                            if (OOOOOO000OOOOOO0O .endswith (".log")):continue #line:124
                            os .unlink (os .path .join (O0O0O0000OOO00O00 ,OOOOOO000OOOOOO0O ))#line:125
                        except :#line:126
                            pass #line:127
                    for OOOO00O0000O0OO00 in O00O0O0OOOOOO0000 :#line:128
                        try :#line:129
                            OOO00OOO0OO000000 =(os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:131
                            if not "archive_cache"in str (OOO00OOO0OO000000 ):#line:132
                                shutil .rmtree (os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:133
                        except :#line:134
                            pass #line:135
            else :#line:136
                pass #line:137
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:139
        O0O000000O00OOO0O =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:140
        for O0O0O0000OOO00O00 ,O00O0O0OOOOOO0000 ,OO0OO00O0O0000O00 in os .walk (O0O000000O00OOO0O ):#line:141
            O00O0O0000OOOOO0O =0 #line:142
            O00O0O0000OOOOO0O +=len (OO0OO00O0O0000O00 )#line:143
            if O00O0O0000OOOOO0O >0 :#line:144
                if dialog .yesno ("Delete ATV2 Cache Files",str (O00O0O0000OOOOO0O )+" files found in 'Other'",'Do you want to delete them?'):#line:146
                    for OOOOOO000OOOOOO0O in OO0OO00O0O0000O00 :#line:147
                        try :#line:149
                            if (OOOOOO000OOOOOO0O .endswith (".log")):continue #line:150
                            os .unlink (os .path .join (O0O0O0000OOO00O00 ,OOOOOO000OOOOOO0O ))#line:151
                        except :#line:152
                            pass #line:153
                    for OOOO00O0000O0OO00 in O00O0O0OOOOOO0000 :#line:154
                        try :#line:156
                            OOO00OOO0OO000000 =(os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:157
                            if not "archive_cache"in str (OOO00OOO0OO000000 ):#line:158
                                shutil .rmtree (os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:159
                        except :#line:160
                            pass #line:161
            else :#line:162
                pass #line:163
        O00OO0OO000OOO0OO =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:165
        for O0O0O0000OOO00O00 ,O00O0O0OOOOOO0000 ,OO0OO00O0O0000O00 in os .walk (O00OO0OO000OOO0OO ):#line:166
            O00O0O0000OOOOO0O =0 #line:167
            O00O0O0000OOOOO0O +=len (OO0OO00O0O0000O00 )#line:168
            if O00O0O0000OOOOO0O >0 :#line:169
                if dialog .yesno ("Delete ATV2 Cache Files",str (O00O0O0000OOOOO0O )+" files found in 'LocalAndRental'",'Do you want to delete them?'):#line:171
                    for OOOOOO000OOOOOO0O in OO0OO00O0O0000O00 :#line:172
                        try :#line:174
                            if (OOOOOO000OOOOOO0O .endswith (".log")):continue #line:175
                            os .unlink (os .path .join (O0O0O0000OOO00O00 ,OOOOOO000OOOOOO0O ))#line:176
                        except :#line:177
                            pass #line:178
                    for OOOO00O0000O0OO00 in O00O0O0OOOOOO0000 :#line:179
                        try :#line:181
                            OOO00OOO0OO000000 =(os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:182
                            if not "archive_cache"in str (OOO00OOO0OO000000 ):#line:183
                                shutil .rmtree (os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:184
                        except :#line:185
                            pass #line:186
            else :#line:187
                pass #line:188
    O00OOOOOOOOO00O0O =setupCacheEntries ()#line:190
    for OOOOO00OOO0OO0O00 in O00OOOOOOOOO00O0O :#line:191
        OO00O000OOO000O0O =xbmc .translatePath (OOOOO00OOO0OO0O00 .path )#line:192
        if os .path .exists (OO00O000OOO000O0O )==True :#line:193
            for O0O0O0000OOO00O00 ,O00O0O0OOOOOO0000 ,OO0OO00O0O0000O00 in os .walk (OO00O000OOO000O0O ):#line:194
                O00O0O0000OOOOO0O =0 #line:195
                O00O0O0000OOOOO0O +=len (OO0OO00O0O0000O00 )#line:196
                if O00O0O0000OOOOO0O >0 :#line:197
                    if dialog .yesno (MainTitle ,'%s cache files found'%(OOOOO00OOO0OO0O00 .name ),'Do you want to delete them?'):#line:200
                        for OOOOOO000OOOOOO0O in OO0OO00O0O0000O00 :#line:201
                            try :#line:203
                                if (OOOOOO000OOOOOO0O .endswith (".log")):continue #line:204
                                os .unlink (os .path .join (O0O0O0000OOO00O00 ,OOOOOO000OOOOOO0O ))#line:205
                            except :#line:206
                                pass #line:207
                        for OOOO00O0000O0OO00 in O00O0O0OOOOOO0000 :#line:208
                            try :#line:210
                                OOO00OOO0OO000000 =(os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:211
                                if not "archive_cache"in str (OOO00OOO0OO000000 ):#line:212
                                    shutil .rmtree (os .path .join (O0O0O0000OOO00O00 ,OOOO00O0000O0OO00 ))#line:213
                            except :#line:214
                                pass #line:215
                else :#line:216
                    pass #line:217
    dialog .ok (MainTitle ,'Done Clearing Cache files')#line:219
    xbmc .executebuiltin ("Container.Refresh")#line:220
def deleteThumbnails ():#line:227
    if dialog .yesno ("Delete Thumbnails",'This option deletes all thumbnails','Are you sure you want to do this?'):#line:228
       O000OO0O0O0000O00 =True #line:229
       if os .path .exists (thumbnailPath )==True :#line:230
          for OO00OOOOO000OO0O0 ,O0000OOO0OO00O000 ,O0OO0O000O0OOO0O0 in os .walk (thumbnailPath ):#line:231
              OOO0O00O0OO0O000O =0 #line:232
              OOO0O00O0OO0O000O +=len (O0OO0O000O0OOO0O0 )#line:233
              if OOO0O00O0OO0O000O >0 :#line:234
                 for OO000OO0000O000O0 in O0OO0O000O0OOO0O0 :#line:235
                     try :#line:236
                        os .unlink (os .path .join (OO00OOOOO000OO0O0 ,OO000OO0000O000O0 ))#line:237
                     except :#line:238
                        pass #line:239
       else :#line:240
          pass #line:241
    else :#line:242
        O000OO0O0O0000O00 =False #line:243
    if O000OO0O0O0000O00 :#line:245
        O0O0OO0O0000O0O0O =os .path .join (databasePath ,"Textures13.db")#line:246
        try :#line:247
            os .unlink (O0O0OO0O0000O0O0O )#line:248
        except OSError :#line:249
               OOOO0O00OOOOO00OO =platform ()#line:250
               if OOOO0O00OOOOO00OO =='android':#line:252
                  Common .log ("XvBMC *check* -4- Android")#line:253
               else :#line:255
                   Common .log ("XvBMC Platform: "+str (OOOO0O00OOOOO00OO ))#line:256
                   try :#line:257
                      OO0OOO0OO00OOOOO0 =sqlite3 .connect (O0O0OO0O0000O0O0O )#line:258
                      OO0O0O0O00OOO00OO =OO0OOO0OO00OOOOO0 .cursor ()#line:259
                      OO0O0O0O00OOO00OO .execute ('DROP TABLE IF EXISTS path')#line:260
                      OO0O0O0O00OOO00OO .execute ('VACUUM')#line:261
                      OO0OOO0OO00OOOOO0 .commit ()#line:262
                      OO0O0O0O00OOO00OO .execute ('DROP TABLE IF EXISTS sizes')#line:263
                      OO0O0O0O00OOO00OO .execute ('VACUUM')#line:264
                      OO0OOO0OO00OOOOO0 .commit ()#line:265
                      OO0O0O0O00OOO00OO .execute ('DROP TABLE IF EXISTS texture')#line:266
                      OO0O0O0O00OOO00OO .execute ('VACUUM')#line:267
                      OO0OOO0OO00OOOOO0 .commit ()#line:268
                      OO0O0O0O00OOO00OO .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:270
                      OO0OOO0OO00OOOOO0 .commit ()#line:271
                      OO0O0O0O00OOO00OO .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:273
                      OO0OOO0OO00OOOOO0 .commit ()#line:274
                      OO0O0O0O00OOO00OO .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:276
                      OO0OOO0OO00OOOOO0 .commit ()#line:277
                   except :#line:278
                      pass #line:279
        dialog .ok (MainTitle ,'Please [COLOR lime][B]reboot[/B][/COLOR] your system to rebuild thumbnail folder...')#line:281
        xbmc .executebuiltin ("Container.Refresh")#line:282
    else :#line:284
        dialog .ok (MainTitle ,'[COLOR red][B]Skipped:[/B] Delete Thumbnails...[/COLOR]')#line:285
def PiCCleaner ():#line:292
    OO00O000000OO00OO =platform ()#line:293
    log ("XvBMC_Platform: "+str (OO00O000000OO00OO ))#line:294
    if not OO00O000000OO00OO =='linux':#line:295
       dialog .ok (MainTitle +SubTitle ,subtitleNope ,nonlinux ,nonelecNL )#line:296
       log ("none Linux OS ie. Open-/LibreELEC")#line:297
    else :#line:298
        log ("linux os")#line:299
        if dialog .yesno (MainTitle +SubTitle ,'about to do some extreme CrapCleaner voodoo...','[I]this will take a few seconds to complete, be patient![/I]','[B]are you sure[COLOR white]?[/COLOR][/B]'):#line:300
            OO00OOO0O00O00O0O ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/rpiecc.sh"#line:301
            os .system (OO00OOO0O00O00O0O )#line:302
            dialog .ok (MainTitle +SubTitle ,'[B]RPi[/B] CrapCleaner finished!','','Press OK to reboot...')#line:303
            xbmc .executebuiltin ("Reboot")#line:304
def purgePackages ():#line:311
    OOOOOO0OO0OOO0000 =xbmc .translatePath ('special://home/addons/packages')#line:312
    for OO00OO000000O0O0O ,OO0O000O00O0OOO00 ,O000O0O00OO00OOOO in os .walk (OOOOOO0OO0OOO0000 ):#line:314
            OOO0OOOO000OO00OO =0 #line:315
            OOO0OOOO000OO00OO +=len (O000O0O00OO00OOOO )#line:316
    if dialog .yesno ("Delete Package Cache Files",'%d packages found.'%OOO0OOOO000OO00OO ,'Delete Them?'):#line:317
        for OO00OO000000O0O0O ,OO0O000O00O0OOO00 ,O000O0O00OO00OOOO in os .walk (OOOOOO0OO0OOO0000 ):#line:318
            OOO0OOOO000OO00OO =0 #line:319
            OOO0OOOO000OO00OO +=len (O000O0O00OO00OOOO )#line:320
            if OOO0OOOO000OO00OO >0 :#line:321
                try :#line:322
                    for O0O000OO000O000O0 in O000O0O00OO00OOOO :#line:323
                        os .unlink (os .path .join (OO00OO000000O0O0O ,O0O000OO000O000O0 ))#line:324
                    for OO0000O0O00O0OOOO in OO0O000O00O0OOO00 :#line:325
                        shutil .rmtree (os .path .join (OO00OO000000O0O0O ,OO0000O0O00O0OOOO ))#line:326
                except :pass #line:327
                dialog .ok (MainTitle ,'Deleting Packages all done')#line:328
            else :#line:330
                dialog .ok (MainTitle ,'No Packages to Purge')#line:331
    xbmc .executebuiltin ("Container.Refresh")#line:333
def AddonsDatabaseRemoval ():#line:340
    O0O0OO000O0OO00O0 =os .listdir (databasePath )#line:341
    OOOO00OOO00O00000 =[]#line:342
    OOOO000O0000OO000 =True #line:343
    if dialog .yesno ("[COLOR lime]"+MainTitle +"[/COLOR]",' ','[COLOR red]Are YOU Sure [B]?!?[/B][/COLOR]'):#line:351
        if int (kodiver )<=16.7 :#line:352
           try :#line:353
               for OOOOO0OOO00O00000 in O0O0OO000O0OO00O0 :#line:354
                   if re .findall ('Addons(\d+)\.db',OOOOO0OOO00O00000 ):#line:355
                       OOOO00OOO00O00000 .append (OOOOO0OOO00O00000 )#line:356
               for OOOOO0OOO00O00000 in OOOO00OOO00O00000 :#line:357
                   OO0OOO0OO0O00O000 =os .path .join (databasePath ,OOOOO0OOO00O00000 )#line:358
                   O0O0O00O000O00OOO =open (OO0OOO0OO0O00O000 ,'ab+')#line:359
                   try :#line:360
                       O0O0O00O000O00OOO .close ()#line:362
                       os .remove (O0O0O00O000O00OOO .name )#line:363
                   except :#line:364
                       OOOO000O0000OO000 =False #line:365
               if OOOO000O0000OO000 :#line:366
                   dialog .ok (MainTitle ,'Your system will [COLOR red]reboot[/COLOR] to rebuild addons.db...')#line:367
                   Common .killKodi #line:368
               else :#line:369
                   dialog .ok (MainTitle ,'Removal [COLOR red]failed![/COLOR]','try manual remove, see: [COLOR green]http://kodi.wiki/view/Database_version[/COLOR]')#line:370
           except :#line:371
               pass #line:372
        else :#line:373
           dialog .ok (MainTitle ,'This feature is not available in Kodi 17 Krypton','','[COLOR yellow]Thank you for using XvBMC Maintenance[/COLOR]')#line:374
def autocleanask ():#line:381
    OO0O00OOOO000O0O0 =xbmcgui .Dialog ().yesno (MainTitle ,'Select [COLOR green]YES[/COLOR] to delete your:','cache, crashlogs, packages & thumbnails all at once.','[I][COLOR white]Do you wish to continue[B]?[/B][/I][/COLOR]',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:383
    if OO0O00OOOO000O0O0 ==1 :#line:384
        autocleannow ()#line:385
def autocleannow ():#line:387
    O0OO0OO0O000OO00O =True #line:388
    if os .path .exists (cachePath )==True :#line:390
        for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (cachePath ):#line:391
            O0O0OOO0O000OOOOO =0 #line:392
            O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:393
            if O0O0OOO0O000OOOOO >0 :#line:394
                    for O00OOOOOO0OOO0OO0 in O0O0OO00OOOOO0O00 :#line:395
                        try :#line:396
                            if (O00OOOOOO0OOO0OO0 .endswith (".log")):continue #line:397
                            os .unlink (os .path .join (O000OO0OO0OOOOOO0 ,O00OOOOOO0OOO0OO0 ))#line:398
                        except :#line:399
                            pass #line:400
                    for OOOO00O0OOOOO0O0O in O0OO0000O00O00O0O :#line:401
                        try :#line:402
                            OOO0O00000O0OOO0O =(os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:403
                            if not "archive_cache"in str (OOO0O00000O0OOO0O ):#line:404
                                shutil .rmtree (os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:405
                        except :#line:406
                            pass #line:407
            else :pass #line:408
    if os .path .exists (tempPath )==True :#line:410
        for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (tempPath ):#line:411
            O0O0OOO0O000OOOOO =0 #line:412
            O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:413
            if O0O0OOO0O000OOOOO >0 :#line:414
                    for O00OOOOOO0OOO0OO0 in O0O0OO00OOOOO0O00 :#line:415
                        try :#line:416
                            if (O00OOOOOO0OOO0OO0 .endswith (".log")):continue #line:417
                            os .unlink (os .path .join (O000OO0OO0OOOOOO0 ,O00OOOOOO0OOO0OO0 ))#line:418
                        except :#line:419
                            pass #line:420
                    for OOOO00O0OOOOO0O0O in O0OO0000O00O00O0O :#line:421
                        try :#line:422
                            OOO0O00000O0OOO0O =(os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:423
                            if not "archive_cache"in str (OOO0O00000O0OOO0O ):#line:424
                                shutil .rmtree (os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:425
                        except :#line:426
                            pass #line:427
            else :pass #line:428
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:430
        OO0O000OOOO00OO0O =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:431
        for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (OO0O000OOOO00OO0O ):#line:432
            O0O0OOO0O000OOOOO =0 #line:433
            O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:434
            if O0O0OOO0O000OOOOO >0 :#line:436
                    for O00OOOOOO0OOO0OO0 in O0O0OO00OOOOO0O00 :#line:437
                        try :#line:438
                            if (O00OOOOOO0OOO0OO0 .endswith (".log")):continue #line:439
                            os .unlink (os .path .join (O000OO0OO0OOOOOO0 ,O00OOOOOO0OOO0OO0 ))#line:440
                        except :#line:441
                            pass #line:442
                    for OOOO00O0OOOOO0O0O in O0OO0000O00O00O0O :#line:443
                        try :#line:444
                            OOO0O00000O0OOO0O =(os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:445
                            if not "archive_cache"in str (OOO0O00000O0OOO0O ):#line:446
                                shutil .rmtree (os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:447
                        except :#line:448
                            pass #line:449
            else :pass #line:450
        O0000O0OO00OO0O00 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:452
        for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (O0000O0OO00OO0O00 ):#line:453
            O0O0OOO0O000OOOOO =0 #line:454
            O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:455
            if O0O0OOO0O000OOOOO >0 :#line:457
                    for O00OOOOOO0OOO0OO0 in O0O0OO00OOOOO0O00 :#line:458
                        try :#line:459
                            if (O00OOOOOO0OOO0OO0 .endswith (".log")):continue #line:460
                            os .unlink (os .path .join (O000OO0OO0OOOOOO0 ,O00OOOOOO0OOO0OO0 ))#line:461
                        except :#line:462
                            pass #line:463
                    for OOOO00O0OOOOO0O0O in O0OO0000O00O00O0O :#line:464
                        try :#line:465
                            OOO0O00000O0OOO0O =(os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:466
                            if not "archive_cache"in str (OOO0O00000O0OOO0O ):#line:467
                                shutil .rmtree (os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:468
                        except :#line:469
                            pass #line:470
            else :pass #line:471
    O00O00OO0OO0000OO =setupCacheEntries ()#line:473
    for O0O0O0O0OOOOO00OO in O00O00OO0OO0000OO :#line:474
        OO0O00OOOO00000O0 =xbmc .translatePath (O0O0O0O0OOOOO00OO .path )#line:475
        if os .path .exists (OO0O00OOOO00000O0 )==True :#line:476
            for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (OO0O00OOOO00000O0 ):#line:477
                O0O0OOO0O000OOOOO =0 #line:478
                O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:479
                if O0O0OOO0O000OOOOO >0 :#line:480
                    for O00OOOOOO0OOO0OO0 in O0O0OO00OOOOO0O00 :#line:481
                        try :#line:482
                            if (O00OOOOOO0OOO0OO0 .endswith (".log")):continue #line:483
                            os .unlink (os .path .join (O000OO0OO0OOOOOO0 ,O00OOOOOO0OOO0OO0 ))#line:484
                        except :#line:485
                            pass #line:486
                    for OOOO00O0OOOOO0O0O in O0OO0000O00O00O0O :#line:487
                        try :#line:488
                            OOO0O00000O0OOO0O =(os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:489
                            if not "archive_cache"in str (OOO0O00000O0OOO0O ):#line:490
                                shutil .rmtree (os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:491
                        except :#line:492
                            pass #line:493
                else :pass #line:494
    if dialog .yesno (MainTitle ,'[COLOR red]This option also deletes all your thumbnails...[/COLOR]','[COLOR green]Are you sure you want to do this[B]?[/B][/COLOR]'):#line:496
       OOOOO0O0O0OOOO000 =True #line:497
       if os .path .exists (thumbnailPath )==True :#line:498
          for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (thumbnailPath ):#line:499
              O0O0OOO0O000OOOOO =0 #line:500
              O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:501
              if O0O0OOO0O000OOOOO >0 :#line:502
                 for O00OOOOOO0OOO0OO0 in O0O0OO00OOOOO0O00 :#line:503
                     try :#line:504
                        os .unlink (os .path .join (O000OO0OO0OOOOOO0 ,O00OOOOOO0OOO0OO0 ))#line:505
                     except :#line:506
                        pass #line:507
       else :#line:508
          pass #line:509
    else :#line:510
        OOOOO0O0O0OOOO000 =False #line:511
    if OOOOO0O0O0OOOO000 :#line:512
        O00OO0000000OO0OO =os .path .join (databasePath ,"Textures13.db")#line:513
        try :#line:514
            os .unlink (O00OO0000000OO0OO )#line:515
        except OSError :#line:516
               O0O000O0O0OO0OO00 =platform ()#line:517
               if O0O000O0O0OO0OO00 =='android':#line:519
                  Common .log ("XvBMC *check* -4- Android")#line:520
               else :#line:522
                   Common .log ("XvBMC Platform: "+str (O0O000O0O0OO0OO00 ))#line:523
                   try :#line:524
                      OO0OOOOOOO0O00O0O =sqlite3 .connect (O00OO0000000OO0OO )#line:525
                      OOO00O00O00OOOOO0 =OO0OOOOOOO0O00O0O .cursor ()#line:526
                      OOO00O00O00OOOOO0 .execute ('DROP TABLE IF EXISTS path')#line:527
                      OOO00O00O00OOOOO0 .execute ('VACUUM')#line:528
                      OO0OOOOOOO0O00O0O .commit ()#line:529
                      OOO00O00O00OOOOO0 .execute ('DROP TABLE IF EXISTS sizes')#line:530
                      OOO00O00O00OOOOO0 .execute ('VACUUM')#line:531
                      OO0OOOOOOO0O00O0O .commit ()#line:532
                      OOO00O00O00OOOOO0 .execute ('DROP TABLE IF EXISTS texture')#line:533
                      OOO00O00O00OOOOO0 .execute ('VACUUM')#line:534
                      OO0OOOOOOO0O00O0O .commit ()#line:535
                      OOO00O00O00OOOOO0 .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:537
                      OO0OOOOOOO0O00O0O .commit ()#line:538
                      OOO00O00O00OOOOO0 .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:540
                      OO0OOOOOOO0O00O0O .commit ()#line:541
                      OOO00O00O00OOOOO0 .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:543
                      OO0OOOOOOO0O00O0O .commit ()#line:544
                   except :#line:545
                      pass #line:546
    else :#line:547
        Common .log ("XvBMC skipped remove thumbnails.")#line:548
    OO000OOO00OOO000O =xbmc .translatePath ('special://home/addons/packages')#line:550
    for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (OO000OOO00OOO000O ):#line:551
            O0O0OOO0O000OOOOO =0 #line:552
            O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:553
    for O000OO0OO0OOOOOO0 ,O0OO0000O00O00O0O ,O0O0OO00OOOOO0O00 in os .walk (OO000OOO00OOO000O ):#line:554
            O0O0OOO0O000OOOOO =0 #line:555
            O0O0OOO0O000OOOOO +=len (O0O0OO00OOOOO0O00 )#line:556
            if O0O0OOO0O000OOOOO >0 :#line:557
                try :#line:558
                    for O00OOOOOO0OOO0OO0 in O0O0OO00OOOOO0O00 :#line:559
                        os .unlink (os .path .join (O000OO0OO0OOOOOO0 ,O00OOOOOO0OOO0OO0 ))#line:560
                    for OOOO00O0OOOOO0O0O in O0OO0000O00O00O0O :#line:561
                        shutil .rmtree (os .path .join (O000OO0OO0OOOOOO0 ,OOOO00O0OOOOO0O0O ))#line:562
                except :#line:563
                    pass #line:564
    if O0OO0OO0O000OO00O ==True :#line:566
        AutoCrash ()#line:568
    else :#line:569
        xbmc .log (str (O0OO0OO0O000OO00O ))#line:571
    O0000OOO0OOO000O0 =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR white][B]A[/B]uto [B]C[/B]lean finished:[/COLOR]','[I]cache, crashlogs, packages & thumbnails are removed.[/I]','Reboot your device now to finish the process?',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:573
    if O0000OOO0OOO000O0 ==1 :#line:574
         Common .killKodi ()#line:575
def AutoCrash ():#line:577
    OOO0OOOO0O0OO0000 =xbmc .translatePath ('special://home')#line:579
    O000OOO000O000OO0 =os .path .join (xbmc .translatePath ('special://home'),'cache')#line:580
    O0000OOO0000OOO00 =os .path .join (xbmc .translatePath ('special://home'),'temp')#line:581
    if os .path .exists (OOO0OOOO0O0OO0000 )==True :#line:583
        OO00OOO0O000OO0OO =Windows #line:584
        import glob as O00OO0O00OOO00O0O #line:585
        for O00000O0O00000000 in O00OO0O00OOO00O0O .glob (os .path .join (OO00OOO0O000OO0OO ,'*.dmp')):#line:586
            O000O0OOO0O0O0O0O =O00000O0O00000000 #line:587
            log (O00000O0O00000000 )#line:588
            os .remove (O00000O0O00000000 )#line:589
        for O00000O0O00000000 in O00OO0O00OOO00O0O .glob (os .path .join (OO00OOO0O000OO0OO ,'*.txt')):#line:591
            O000O0OOO0O0O0O0O =O00000O0O00000000 #line:592
            log (O00000O0O00000000 )#line:593
            os .remove (O00000O0O00000000 )#line:594
    if os .path .exists (O000OOO000O000OO0 )==True :#line:596
        OO00OOO0O000OO0OO =O000OOO000O000OO0 #line:597
        import glob as O00OO0O00OOO00O0O #line:598
        for O00000O0O00000000 in O00OO0O00OOO00O0O .glob (os .path .join (OO00OOO0O000OO0OO ,'*.dmp')):#line:599
            O000O0OOO0O0O0O0O =O00000O0O00000000 #line:600
            log (O00000O0O00000000 )#line:601
            os .remove (O00000O0O00000000 )#line:602
        for O00000O0O00000000 in O00OO0O00OOO00O0O .glob (os .path .join (OO00OOO0O000OO0OO ,'*.txt')):#line:604
            O000O0OOO0O0O0O0O =O00000O0O00000000 #line:605
            log (O00000O0O00000000 )#line:606
            os .remove (O00000O0O00000000 )#line:607
    if os .path .exists (O0000OOO0000OOO00 )==True :#line:609
        OO00OOO0O000OO0OO =O0000OOO0000OOO00 #line:610
        import glob as O00OO0O00OOO00O0O #line:611
        for O00000O0O00000000 in O00OO0O00OOO00O0O .glob (os .path .join (OO00OOO0O000OO0OO ,'*.dmp')):#line:612
            O000O0OOO0O0O0O0O =O00000O0O00000000 #line:613
            log (O00000O0O00000000 )#line:614
            os .remove (O00000O0O00000000 )#line:615
        for O00000O0O00000000 in O00OO0O00OOO00O0O .glob (os .path .join (OO00OOO0O000OO0OO ,'*.txt')):#line:617
            O000O0OOO0O0O0O0O =O00000O0O00000000 #line:618
            log (O00000O0O00000000 )#line:619
            os .remove (O00000O0O00000000 )#line:620
def Fix_Special (url ):#line:627
    O0OOO0000OOOO0OOO =xbmc .translatePath ('special://home')#line:628
    dp .create (MainTitle ,"Renaming paths...",'','Please Wait')#line:629
    for OOOOOOOOOOO0OO0OO ,OOO00O00O00O0O0O0 ,OO0O0O000OO000OOO in os .walk (O0OOO0000OOOO0OOO ):#line:630
        for O0O00O0OOOOOO0OOO in OO0O0O000OO000OOO :#line:631
            if O0O00O0OOOOOO0OOO .endswith (".xml"):#line:632
                 dp .update (0 ,"Fixing","[COLOR green]"+O0O00O0OOOOOO0OOO +"[/COLOR]","Please wait.....")#line:633
                 OO0OO0OOO0O0000OO =open ((os .path .join (OOOOOOOOOOO0OO0OO ,O0O00O0OOOOOO0OOO ))).read ()#line:634
                 OOOO000O0OOOO0OO0 =OO0OO0OOO0O0000OO .replace (O0OOO0000OOOO0OOO ,'special://home/')#line:635
                 OOOO0O00OO00O000O =open ((os .path .join (OOOOOOOOOOO0OO0OO ,O0O00O0OOOOOO0OOO )),mode ='w')#line:636
                 OOOO0O00OO00O000O .write (str (OOOO000O0OOOO0OO0 ))#line:637
                 OOOO0O00OO00O000O .close ()#line:638
    dialog .ok (MainTitle ,'All physical (home) paths have been converted to special','To complete this process Kodi will force close now!')#line:640
    Common .killKodi ()#line:641
def xvbmcLog ():#line:648
    OOOO0O0OOOO000OO0 =xbmc .translatePath ('special://logpath/kodi.log')#line:649
    O0OO000OOO00O0OOO =xbmc .translatePath ('special://logpath/spmc.log')#line:650
    O0O000O0OOO0OOOO0 =xbmc .translatePath ('special://logpath/spmc.log')#line:651
    O0OO0O00OO0OOOO00 =xbmc .translatePath ('special://logpath/kodi.old.log')#line:652
    O0000OO00O00000O0 =xbmc .translatePath ('special://logpath/spmc.old.log')#line:653
    OOO00OOOO000O0O0O =xbmc .translatePath ('special://logpath/kodi.old.log')#line:654
    if os .path .exists (O0OO000OOO00O0OOO ):#line:656
        if os .path .exists (O0OO000OOO00O0OOO )and os .path .exists (O0000OO00O00000O0 ):#line:657
            O0OOO0O0OOOOO0OOO =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:658
            if O0OOO0O0OOOOO0OOO ==0 :#line:659
                OO00OO0O000O0OOOO =open (O0OO000OOO00O0OOO ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:660
                Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:661
            else :#line:662
                OO00OO0O000O0OOOO =open (O0000OO00O00000O0 ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:663
                Common .TextBoxes ("%s - spmc.old.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:664
        else :#line:665
            OO00OO0O000O0OOOO =open (O0OO000OOO00O0OOO ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:666
            Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:667
    if os .path .exists (OOOO0O0OOOO000OO0 ):#line:669
        if os .path .exists (OOOO0O0OOOO000OO0 )and os .path .exists (O0OO0O00OO0OOOO00 ):#line:670
            O0OOO0O0OOOOO0OOO =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:671
            if O0OOO0O0OOOOO0OOO ==0 :#line:672
                OO00OO0O000O0OOOO =open (OOOO0O0OOOO000OO0 ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:673
                Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:674
            else :#line:675
                OO00OO0O000O0OOOO =open (O0OO0O00OO0OOOO00 ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:676
                Common .TextBoxes ("%s - kodi.old.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:677
        else :#line:678
            OO00OO0O000O0OOOO =open (OOOO0O0OOOO000OO0 ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:679
            Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:680
    if os .path .exists (O0O000O0OOO0OOOO0 ):#line:682
        if os .path .exists (O0O000O0OOO0OOOO0 )and os .path .exists (OOO00OOOO000O0O0O ):#line:683
            O0OOO0O0OOOOO0OOO =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:684
            if O0OOO0O0OOOOO0OOO ==0 :#line:685
                OO00OO0O000O0OOOO =open (O0O000O0OOO0OOOO0 ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:686
                Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:687
            else :#line:688
                OO00OO0O000O0OOOO =open (OOO00OOOO000O0O0O ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:689
                Common .TextBoxes ("%s - dbmc.old.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:690
        else :#line:691
            OO00OO0O000O0OOOO =open (O0O000O0OOO0OOOO0 ,mode ='r');O0O000OO00O0OO0OO =OO00OO0O000O0OOOO .read ();OO00OO0O000O0OOOO .close ()#line:692
            Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O0O000OO00O0OO0OO +"[/COLOR]")#line:693
    if os .path .isfile (OOOO0O0OOOO000OO0 )or os .path .isfile (O0OO000OOO00O0OOO )or os .path .isfile (O0O000O0OOO0OOOO0 ):#line:695
        return True #line:696
    else :#line:697
        dialog .ok (MainTitle ,'Sorry, No log file was found.','','[COLOR yellow]Sorry, er was geen log file gevonden.[/COLOR]')#line:698
if Common .get_kversion ()>16.5 :#line:705
    try :from sqlite3 import dbapi2 as db_lib #line:706
    except :from pysqlite2 import dbapi2 as db_lib #line:707
    db_dir =xbmc .translatePath ("special://profile/Database")#line:709
    db_path =os .path .join (db_dir ,'Addons27.db')#line:710
    conn =db_lib .connect (db_path )#line:711
    conn .text_factory =str #line:712
def AddonsEnable ():#line:714
    if Common .get_kversion ()>16.5 :#line:715
        OOO000OO0000O0OO0 =sqlite3 .connect (xbmc .translatePath ("special://database/Addons27.db"))#line:716
        O00OO00O0O0O0O0OO =OOO000OO0000O0OO0 .cursor ()#line:717
        O00OO00O0O0O0O0OO .execute ("UPDATE installed SET enabled = 1 WHERE addonID NOT LIKE '%audiodecoder.%' AND addonID NOT LIKE '%inputstream.%' AND addonID NOT LIKE '%pvr.%' AND addonID NOT LIKE '%screensaver.%' AND addonID NOT LIKE '%visualization.%';")#line:718
        OOO000OO0000O0OO0 .commit ()#line:719
        OOO000OO0000O0OO0 .close ()#line:720
        xbmc .executebuiltin ('UpdateLocalAddons()')#line:721
        xbmc .executebuiltin ('UpdateAddonRepos()')#line:722
        OO0O0000OO0OOOOO0 =xbmcgui .Dialog ().yesno (MainTitle +' : add-ons [B]enabled[/B]','[COLOR=green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete (\'yes\' is force close)','[B]Herstart[/B] Kodi ter afronding (ja is \'force close\')',yeslabel ='[COLOR lime]Ja/Yes[/COLOR]',nolabel ='[COLOR red]Nee/No[/COLOR]')#line:723
        if OO0O0000OO0OOOOO0 ==1 :#line:724
            os ._exit (1 )#line:725
        else :pass #line:726
    else :pass #line:727
def EnableRTMP ():#line:729
        try :addon_able .set_enabled ("inputstream.adaptive")#line:730
        except :pass #line:731
        time .sleep (0.5 )#line:732
        try :addon_able .set_enabled ("inputstream.rtmp")#line:733
        except :pass #line:734
        time .sleep (0.5 )#line:735
        xbmc .executebuiltin ('XBMC.UpdateLocalAddons()')#line:736
        dialog .ok ("Operation Complete!",'Live Streaming has been Enabled!','Brought To You By %s '%MainTitle )#line:738
"""
    IF you copy/paste 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
