#!/usr/bin/python
"""
    IF you copy/paste 'huisvrouw.py' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
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
    OO0O000OOOOO0OOOO =6 #line:67
    OO00O00O0O0000OOO =["MP3 Streams","Quasar","SportsDevil","Simple Downloader","Spotitube","SkinHelperService"]#line:68
    O00000O0OOOO00OO0 =["special://profile/addon_data/plugin.audio.mp3streams/temp_dl","special://profile/addon_data/plugin.video.quasar/cache","special://profile/addon_data/plugin.video.SportsDevil/cache","special://profile/addon_data/script.module.simple.downloader","special://profile/addon_data/plugin.video.spotitube/cache","special://profile/addon_data/script.skin.helper.service/musicartcache"]#line:74
    OO0OOO00O0O0O000O =[]#line:76
    for O0OOO0O0OOOO0O0O0 in range (OO0O000OOOOO0OOOO ):#line:78
        OO0OOO00O0O0O000O .append (cacheEntry (OO00O00O0O0000OOO [O0OOO0O0OOOO0O0O0 ],O00000O0OOOO00OO0 [O0OOO0O0OOOO0O0O0 ]))#line:79
    return OO0OOO00O0O0O000O #line:81
def clearCache ():#line:88
    if os .path .exists (cachePath )==True :#line:89
        for O0O0OO0OOOO0OOO00 ,OOOO0OO00O0OOOO00 ,OO000OOOO00O0O0O0 in os .walk (cachePath ):#line:90
            O000O0O0OO00000O0 =0 #line:91
            O000O0O0OO00000O0 +=len (OO000OOOO00O0O0O0 )#line:92
            if O000O0O0OO00000O0 >0 :#line:93
                if dialog .yesno ("Delete Cache Files",str (O000O0O0OO00000O0 )+' files found','Do you want to delete them?'):#line:95
                    for OOO000OOOO0OOOOO0 in OO000OOOO00O0O0O0 :#line:96
                        try :#line:97
                            if (OOO000OOOO0OOOOO0 .endswith (".log")):continue #line:99
                            os .unlink (os .path .join (O0O0OO0OOOO0OOO00 ,OOO000OOOO0OOOOO0 ))#line:100
                        except :#line:101
                            pass #line:102
                    for O0O0OOOOO0OOOO00O in OOOO0OO00O0OOOO00 :#line:103
                        try :#line:104
                            OOO00OO0OOOOO000O =(os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:106
                            if not "archive_cache"in str (OOO00OO0OOOOO000O ):#line:107
                                shutil .rmtree (os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:108
                        except :#line:109
                            pass #line:110
            else :#line:111
                pass #line:112
    if os .path .exists (tempPath )==True :#line:114
        for O0O0OO0OOOO0OOO00 ,OOOO0OO00O0OOOO00 ,OO000OOOO00O0O0O0 in os .walk (tempPath ):#line:115
            O000O0O0OO00000O0 =0 #line:116
            O000O0O0OO00000O0 +=len (OO000OOOO00O0O0O0 )#line:117
            if O000O0O0OO00000O0 >0 :#line:118
                if dialog .yesno ("Delete Temp Files",str (O000O0O0OO00000O0 )+' files found','Do you want to delete them?'):#line:120
                    for OOO000OOOO0OOOOO0 in OO000OOOO00O0O0O0 :#line:121
                        try :#line:122
                            if (OOO000OOOO0OOOOO0 .endswith (".log")):continue #line:124
                            os .unlink (os .path .join (O0O0OO0OOOO0OOO00 ,OOO000OOOO0OOOOO0 ))#line:125
                        except :#line:126
                            pass #line:127
                    for O0O0OOOOO0OOOO00O in OOOO0OO00O0OOOO00 :#line:128
                        try :#line:129
                            OOO00OO0OOOOO000O =(os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:131
                            if not "archive_cache"in str (OOO00OO0OOOOO000O ):#line:132
                                shutil .rmtree (os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:133
                        except :#line:134
                            pass #line:135
            else :#line:136
                pass #line:137
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:139
        OO000O00O00O00O00 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:140
        for O0O0OO0OOOO0OOO00 ,OOOO0OO00O0OOOO00 ,OO000OOOO00O0O0O0 in os .walk (OO000O00O00O00O00 ):#line:141
            O000O0O0OO00000O0 =0 #line:142
            O000O0O0OO00000O0 +=len (OO000OOOO00O0O0O0 )#line:143
            if O000O0O0OO00000O0 >0 :#line:144
                if dialog .yesno ("Delete ATV2 Cache Files",str (O000O0O0OO00000O0 )+" files found in 'Other'",'Do you want to delete them?'):#line:146
                    for OOO000OOOO0OOOOO0 in OO000OOOO00O0O0O0 :#line:147
                        try :#line:149
                            if (OOO000OOOO0OOOOO0 .endswith (".log")):continue #line:150
                            os .unlink (os .path .join (O0O0OO0OOOO0OOO00 ,OOO000OOOO0OOOOO0 ))#line:151
                        except :#line:152
                            pass #line:153
                    for O0O0OOOOO0OOOO00O in OOOO0OO00O0OOOO00 :#line:154
                        try :#line:156
                            OOO00OO0OOOOO000O =(os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:157
                            if not "archive_cache"in str (OOO00OO0OOOOO000O ):#line:158
                                shutil .rmtree (os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:159
                        except :#line:160
                            pass #line:161
            else :#line:162
                pass #line:163
        O0O00OO00O00OO0O0 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:165
        for O0O0OO0OOOO0OOO00 ,OOOO0OO00O0OOOO00 ,OO000OOOO00O0O0O0 in os .walk (O0O00OO00O00OO0O0 ):#line:166
            O000O0O0OO00000O0 =0 #line:167
            O000O0O0OO00000O0 +=len (OO000OOOO00O0O0O0 )#line:168
            if O000O0O0OO00000O0 >0 :#line:169
                if dialog .yesno ("Delete ATV2 Cache Files",str (O000O0O0OO00000O0 )+" files found in 'LocalAndRental'",'Do you want to delete them?'):#line:171
                    for OOO000OOOO0OOOOO0 in OO000OOOO00O0O0O0 :#line:172
                        try :#line:174
                            if (OOO000OOOO0OOOOO0 .endswith (".log")):continue #line:175
                            os .unlink (os .path .join (O0O0OO0OOOO0OOO00 ,OOO000OOOO0OOOOO0 ))#line:176
                        except :#line:177
                            pass #line:178
                    for O0O0OOOOO0OOOO00O in OOOO0OO00O0OOOO00 :#line:179
                        try :#line:181
                            OOO00OO0OOOOO000O =(os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:182
                            if not "archive_cache"in str (OOO00OO0OOOOO000O ):#line:183
                                shutil .rmtree (os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:184
                        except :#line:185
                            pass #line:186
            else :#line:187
                pass #line:188
    O00OOOO0OOO00O0O0 =setupCacheEntries ()#line:190
    for O00OO0OO0O00O000O in O00OOOO0OOO00O0O0 :#line:191
        OO0O000O0O0000O0O =xbmc .translatePath (O00OO0OO0O00O000O .path )#line:192
        if os .path .exists (OO0O000O0O0000O0O )==True :#line:193
            for O0O0OO0OOOO0OOO00 ,OOOO0OO00O0OOOO00 ,OO000OOOO00O0O0O0 in os .walk (OO0O000O0O0000O0O ):#line:194
                O000O0O0OO00000O0 =0 #line:195
                O000O0O0OO00000O0 +=len (OO000OOOO00O0O0O0 )#line:196
                if O000O0O0OO00000O0 >0 :#line:197
                    if dialog .yesno (MainTitle ,'%s cache files found'%(O00OO0OO0O00O000O .name ),'Do you want to delete them?'):#line:200
                        for OOO000OOOO0OOOOO0 in OO000OOOO00O0O0O0 :#line:201
                            try :#line:203
                                if (OOO000OOOO0OOOOO0 .endswith (".log")):continue #line:204
                                os .unlink (os .path .join (O0O0OO0OOOO0OOO00 ,OOO000OOOO0OOOOO0 ))#line:205
                            except :#line:206
                                pass #line:207
                        for O0O0OOOOO0OOOO00O in OOOO0OO00O0OOOO00 :#line:208
                            try :#line:210
                                OOO00OO0OOOOO000O =(os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:211
                                if not "archive_cache"in str (OOO00OO0OOOOO000O ):#line:212
                                    shutil .rmtree (os .path .join (O0O0OO0OOOO0OOO00 ,O0O0OOOOO0OOOO00O ))#line:213
                            except :#line:214
                                pass #line:215
                else :#line:216
                    pass #line:217
    dialog .ok (MainTitle ,'Done Clearing Cache files')#line:219
    xbmc .executebuiltin ("Container.Refresh")#line:220
def deleteThumbnails ():#line:227
    if os .path .exists (thumbnailPath )==True :#line:228
            if dialog .yesno ("Delete Thumbnails",'This option deletes all thumbnails','Are you sure you want to do this?'):#line:230
                for OO00OOO000O00000O ,O00OO000O000000OO ,O000O00O0O000OOOO in os .walk (thumbnailPath ):#line:231
                    O00OO000OOOO0O000 =0 #line:232
                    O00OO000OOOO0O000 +=len (O000O00O0O000OOOO )#line:233
                    if O00OO000OOOO0O000 >0 :#line:234
                        for OO0O0OOOO00OO0000 in O000O00O0O000OOOO :#line:235
                            try :#line:236
                                os .unlink (os .path .join (OO00OOO000O00000O ,OO0O0OOOO00OO0000 ))#line:237
                            except :#line:238
                                pass #line:239
    else :#line:240
        pass #line:241
    OOOOOOOOOOOO0O0OO =os .path .join (databasePath ,"Textures13.db")#line:243
    try :#line:244
        os .unlink (OOOOOOOOOOOO0O0OO )#line:245
    except OSError :#line:246
        try :#line:247
            OOOO00OO00O0OO000 =sqlite3 .connect (OOOOOOOOOOOO0O0OO )#line:248
            O0OO00OO0OO000OO0 =OOOO00OO00O0OO000 .cursor ()#line:249
            O0OO00OO0OO000OO0 .execute ('DROP TABLE IF EXISTS path')#line:250
            O0OO00OO0OO000OO0 .execute ('VACUUM')#line:251
            OOOO00OO00O0OO000 .commit ()#line:252
            O0OO00OO0OO000OO0 .execute ('DROP TABLE IF EXISTS sizes')#line:253
            O0OO00OO0OO000OO0 .execute ('VACUUM')#line:254
            OOOO00OO00O0OO000 .commit ()#line:255
            O0OO00OO0OO000OO0 .execute ('DROP TABLE IF EXISTS texture')#line:256
            O0OO00OO0OO000OO0 .execute ('VACUUM')#line:257
            OOOO00OO00O0OO000 .commit ()#line:258
            O0OO00OO0OO000OO0 .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:260
            OOOO00OO00O0OO000 .commit ()#line:261
            O0OO00OO0OO000OO0 .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:263
            OOOO00OO00O0OO000 .commit ()#line:264
            O0OO00OO0OO000OO0 .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:266
            OOOO00OO00O0OO000 .commit ()#line:267
        except :#line:268
            pass #line:269
    dialog .ok (MainTitle ,'Please reboot your system to rebuild thumbnail folder...')#line:271
    xbmc .executebuiltin ("Container.Refresh")#line:272
def PiCCleaner ():#line:279
    OO000O000OOO00000 =platform ()#line:280
    log ("XvBMC_Platform: "+str (OO000O000OOO00000 ))#line:281
    if not OO000O000OOO00000 =='linux':#line:282
       dialog .ok (MainTitle +SubTitle ,subtitleNope ,nonlinux ,nonelecNL )#line:283
       log ("none Linux OS ie. Open-/LibreELEC")#line:284
    else :#line:285
        log ("linux os")#line:286
        if dialog .yesno (MainTitle +SubTitle ,'about to do some extreme CrapCleaner voodoo...','[I]this will take a few seconds to complete, be patient![/I]','[B]are you sure[COLOR white]?[/COLOR][/B]'):#line:287
            O00O000O0O0000OOO ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/rpiecc.sh"#line:288
            os .system (O00O000O0O0000OOO )#line:289
            dialog .ok (MainTitle +SubTitle ,'[B]RPi[/B] CrapCleaner finished!','','Press OK to reboot...')#line:290
            xbmc .executebuiltin ("Reboot")#line:291
def purgePackages ():#line:298
    O0OO0O0OOO000OO0O =xbmc .translatePath ('special://home/addons/packages')#line:299
    for O0OOOOO00O000O0O0 ,O0O00O00OO0O0OO0O ,OOO0O00OOO0OO0000 in os .walk (O0OO0O0OOO000OO0O ):#line:301
            OO00OO00OO00OOOO0 =0 #line:302
            OO00OO00OO00OOOO0 +=len (OOO0O00OOO0OO0000 )#line:303
    if dialog .yesno ("Delete Package Cache Files",'%d packages found.'%OO00OO00OO00OOOO0 ,'Delete Them?'):#line:304
        for O0OOOOO00O000O0O0 ,O0O00O00OO0O0OO0O ,OOO0O00OOO0OO0000 in os .walk (O0OO0O0OOO000OO0O ):#line:305
            OO00OO00OO00OOOO0 =0 #line:306
            OO00OO00OO00OOOO0 +=len (OOO0O00OOO0OO0000 )#line:307
            if OO00OO00OO00OOOO0 >0 :#line:308
                try :#line:309
                    for OO0O00000OOOOOO0O in OOO0O00OOO0OO0000 :#line:310
                        os .unlink (os .path .join (O0OOOOO00O000O0O0 ,OO0O00000OOOOOO0O ))#line:311
                    for OO0O00O0OO0OOOO0O in O0O00O00OO0O0OO0O :#line:312
                        shutil .rmtree (os .path .join (O0OOOOO00O000O0O0 ,OO0O00O0OO0OOOO0O ))#line:313
                except :pass #line:314
                dialog .ok (MainTitle ,'Deleting Packages all done')#line:315
            else :#line:317
                dialog .ok (MainTitle ,'No Packages to Purge')#line:318
    xbmc .executebuiltin ("Container.Refresh")#line:320
def AddonsDatabaseRemoval ():#line:327
    OOO000OO000O0O0O0 =os .listdir (databasePath )#line:328
    O0O0OO0O000OOO0OO =[]#line:329
    OO00OOOO0O000O0OO =True #line:330
    if dialog .yesno ("[COLOR lime]"+MainTitle +"[/COLOR]",' ','[COLOR red]Are YOU Sure [B]?!?[/B][/COLOR]'):#line:338
        if int (kodiver )<=16.7 :#line:339
           try :#line:340
               for O00OO00000O0O0000 in OOO000OO000O0O0O0 :#line:341
                   if re .findall ('Addons(\d+)\.db',O00OO00000O0O0000 ):#line:342
                       O0O0OO0O000OOO0OO .append (O00OO00000O0O0000 )#line:343
               for O00OO00000O0O0000 in O0O0OO0O000OOO0OO :#line:344
                   O0OO0OO0O000OO0OO =os .path .join (databasePath ,O00OO00000O0O0000 )#line:345
                   O0OOOOOO0OOO000O0 =open (O0OO0OO0O000OO0OO ,'ab+')#line:346
                   try :#line:347
                       O0OOOOOO0OOO000O0 .close ()#line:349
                       os .remove (O0OOOOOO0OOO000O0 .name )#line:350
                   except :#line:351
                       OO00OOOO0O000O0OO =False #line:352
               if OO00OOOO0O000O0OO :#line:353
                   dialog .ok (MainTitle ,'Your system will [COLOR red]reboot[/COLOR] to rebuild addons.db...')#line:354
                   Common .killKodi #line:355
               else :#line:356
                   dialog .ok (MainTitle ,'Removal [COLOR red]failed![/COLOR]','try manual remove, see: [COLOR green]http://kodi.wiki/view/Database_version[/COLOR]')#line:357
           except :#line:358
               pass #line:359
        else :#line:360
           dialog .ok (MainTitle ,'This feature is not available in Kodi 17 Krypton','','[COLOR yellow]Thank you for using XvBMC Maintenance[/COLOR]')#line:361
def autocleanask ():#line:368
    O00OOOO000OO0OOO0 =xbmcgui .Dialog ().yesno (MainTitle ,'Select [COLOR green]YES[/COLOR] to delete your:','cache, crashlogs, packages & thumbnails all at once.','[I][COLOR white]Do you wish to continue[B]?[/B][/I][/COLOR]',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:370
    if O00OOOO000OO0OOO0 ==1 :#line:371
        autocleannow ()#line:372
def autocleannow ():#line:374
    OOOOO00O0OOO0OO00 =True #line:375
    if os .path .exists (cachePath )==True :#line:377
        for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (cachePath ):#line:378
            O00000OOO00O0O00O =0 #line:379
            O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:380
            if O00000OOO00O0O00O >0 :#line:381
                    for O000O00OOOOOOOOOO in OOOOO0OO0O00O000O :#line:382
                        try :#line:383
                            if (O000O00OOOOOOOOOO .endswith (".log")):continue #line:384
                            os .unlink (os .path .join (OO00O000OOO00O0OO ,O000O00OOOOOOOOOO ))#line:385
                        except :#line:386
                            pass #line:387
                    for OOOOO00OO0OO0O0O0 in O0OO0000O0000OOOO :#line:388
                        try :#line:389
                            O0O00000000OO0OOO =(os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:390
                            if not "archive_cache"in str (O0O00000000OO0OOO ):#line:391
                                shutil .rmtree (os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:392
                        except :#line:393
                            pass #line:394
            else :pass #line:395
    if os .path .exists (tempPath )==True :#line:397
        for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (tempPath ):#line:398
            O00000OOO00O0O00O =0 #line:399
            O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:400
            if O00000OOO00O0O00O >0 :#line:401
                    for O000O00OOOOOOOOOO in OOOOO0OO0O00O000O :#line:402
                        try :#line:403
                            if (O000O00OOOOOOOOOO .endswith (".log")):continue #line:404
                            os .unlink (os .path .join (OO00O000OOO00O0OO ,O000O00OOOOOOOOOO ))#line:405
                        except :#line:406
                            pass #line:407
                    for OOOOO00OO0OO0O0O0 in O0OO0000O0000OOOO :#line:408
                        try :#line:409
                            O0O00000000OO0OOO =(os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:410
                            if not "archive_cache"in str (O0O00000000OO0OOO ):#line:411
                                shutil .rmtree (os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:412
                        except :#line:413
                            pass #line:414
            else :pass #line:415
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:417
        OO0O00O0OO00O0OOO =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:418
        for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (OO0O00O0OO00O0OOO ):#line:419
            O00000OOO00O0O00O =0 #line:420
            O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:421
            if O00000OOO00O0O00O >0 :#line:423
                    for O000O00OOOOOOOOOO in OOOOO0OO0O00O000O :#line:424
                        try :#line:425
                            if (O000O00OOOOOOOOOO .endswith (".log")):continue #line:426
                            os .unlink (os .path .join (OO00O000OOO00O0OO ,O000O00OOOOOOOOOO ))#line:427
                        except :#line:428
                            pass #line:429
                    for OOOOO00OO0OO0O0O0 in O0OO0000O0000OOOO :#line:430
                        try :#line:431
                            O0O00000000OO0OOO =(os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:432
                            if not "archive_cache"in str (O0O00000000OO0OOO ):#line:433
                                shutil .rmtree (os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:434
                        except :#line:435
                            pass #line:436
            else :pass #line:437
        OO0O00OO00O0O000O =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:439
        for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (OO0O00OO00O0O000O ):#line:440
            O00000OOO00O0O00O =0 #line:441
            O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:442
            if O00000OOO00O0O00O >0 :#line:444
                    for O000O00OOOOOOOOOO in OOOOO0OO0O00O000O :#line:445
                        try :#line:446
                            if (O000O00OOOOOOOOOO .endswith (".log")):continue #line:447
                            os .unlink (os .path .join (OO00O000OOO00O0OO ,O000O00OOOOOOOOOO ))#line:448
                        except :#line:449
                            pass #line:450
                    for OOOOO00OO0OO0O0O0 in O0OO0000O0000OOOO :#line:451
                        try :#line:452
                            O0O00000000OO0OOO =(os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:453
                            if not "archive_cache"in str (O0O00000000OO0OOO ):#line:454
                                shutil .rmtree (os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:455
                        except :#line:456
                            pass #line:457
            else :pass #line:458
    OO00OOOO0OOO0000O =setupCacheEntries ()#line:460
    for OO00O0O0OOO0000OO in OO00OOOO0OOO0000O :#line:461
        OO00OOO0O0OO00000 =xbmc .translatePath (OO00O0O0OOO0000OO .path )#line:462
        if os .path .exists (OO00OOO0O0OO00000 )==True :#line:463
            for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (OO00OOO0O0OO00000 ):#line:464
                O00000OOO00O0O00O =0 #line:465
                O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:466
                if O00000OOO00O0O00O >0 :#line:467
                    for O000O00OOOOOOOOOO in OOOOO0OO0O00O000O :#line:468
                        try :#line:469
                            if (O000O00OOOOOOOOOO .endswith (".log")):continue #line:470
                            os .unlink (os .path .join (OO00O000OOO00O0OO ,O000O00OOOOOOOOOO ))#line:471
                        except :#line:472
                            pass #line:473
                    for OOOOO00OO0OO0O0O0 in O0OO0000O0000OOOO :#line:474
                        try :#line:475
                            O0O00000000OO0OOO =(os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:476
                            if not "archive_cache"in str (O0O00000000OO0OOO ):#line:477
                                shutil .rmtree (os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:478
                        except :#line:479
                            pass #line:480
                else :pass #line:481
    if dialog .yesno (MainTitle ,'[COLOR red]This option also deletes all your thumbnails...[/COLOR]','[COLOR green]Are you sure you want to do this[B]?[/B][/COLOR]'):#line:483
        if os .path .exists (thumbnailPath )==True :#line:484
                for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (thumbnailPath ):#line:485
                    O00000OOO00O0O00O =0 #line:486
                    O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:487
                    if O00000OOO00O0O00O >0 :#line:488
                        for O000O00OOOOOOOOOO in OOOOO0OO0O00O000O :#line:489
                            try :#line:490
                                os .unlink (os .path .join (OO00O000OOO00O0OO ,O000O00OOOOOOOOOO ))#line:491
                            except :#line:492
                                pass #line:493
        else :pass #line:494
        O0O0OO0O00000OO0O =os .path .join (databasePath ,"Textures13.db")#line:496
        try :#line:497
            os .unlink (O0O0OO0O00000OO0O )#line:498
        except OSError :#line:499
            try :#line:500
                OO00O000O0OOOO0O0 =sqlite3 .connect (O0O0OO0O00000OO0O )#line:501
                O00O0OOO0OOOO00O0 =OO00O000O0OOOO0O0 .cursor ()#line:502
                O00O0OOO0OOOO00O0 .execute ('DROP TABLE IF EXISTS path')#line:503
                O00O0OOO0OOOO00O0 .execute ('VACUUM')#line:504
                OO00O000O0OOOO0O0 .commit ()#line:505
                O00O0OOO0OOOO00O0 .execute ('DROP TABLE IF EXISTS sizes')#line:506
                O00O0OOO0OOOO00O0 .execute ('VACUUM')#line:507
                OO00O000O0OOOO0O0 .commit ()#line:508
                O00O0OOO0OOOO00O0 .execute ('DROP TABLE IF EXISTS texture')#line:509
                O00O0OOO0OOOO00O0 .execute ('VACUUM')#line:510
                OO00O000O0OOOO0O0 .commit ()#line:511
                O00O0OOO0OOOO00O0 .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:513
                OO00O000O0OOOO0O0 .commit ()#line:514
                O00O0OOO0OOOO00O0 .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:516
                OO00O000O0OOOO0O0 .commit ()#line:517
                O00O0OOO0OOOO00O0 .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:519
                OO00O000O0OOOO0O0 .commit ()#line:520
            except :#line:521
                pass #line:522
    O0O0O00OOO00O00O0 =xbmc .translatePath ('special://home/addons/packages')#line:524
    for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (O0O0O00OOO00O00O0 ):#line:525
            O00000OOO00O0O00O =0 #line:526
            O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:527
    for OO00O000OOO00O0OO ,O0OO0000O0000OOOO ,OOOOO0OO0O00O000O in os .walk (O0O0O00OOO00O00O0 ):#line:528
            O00000OOO00O0O00O =0 #line:529
            O00000OOO00O0O00O +=len (OOOOO0OO0O00O000O )#line:530
            if O00000OOO00O0O00O >0 :#line:531
                try :#line:532
                    for O000O00OOOOOOOOOO in OOOOO0OO0O00O000O :#line:533
                        os .unlink (os .path .join (OO00O000OOO00O0OO ,O000O00OOOOOOOOOO ))#line:534
                    for OOOOO00OO0OO0O0O0 in O0OO0000O0000OOOO :#line:535
                        shutil .rmtree (os .path .join (OO00O000OOO00O0OO ,OOOOO00OO0OO0O0O0 ))#line:536
                except :#line:537
                    pass #line:538
    if OOOOO00O0OOO0OO00 ==True :#line:540
        AutoCrash ()#line:542
    else :#line:543
        xbmc .log (str (OOOOO00O0OOO0OO00 ))#line:545
    O0OO0OOOO00O0O0O0 =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR white][B]A[/B]uto [B]C[/B]lean finished:[/COLOR]','[I]cache, crashlogs, packages & thumbnails are removed.[/I]','Reboot your device now to finish the process?',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:547
    if O0OO0OOOO00O0O0O0 ==1 :#line:548
         Common .killKodi ()#line:549
def AutoCrash ():#line:551
    O0O00OO0OO000OO00 =xbmc .translatePath ('special://home')#line:553
    OO00O0OOO0O000O00 =os .path .join (xbmc .translatePath ('special://home'),'cache')#line:554
    O0O000O0O00O0O0OO =os .path .join (xbmc .translatePath ('special://home'),'temp')#line:555
    if os .path .exists (O0O00OO0OO000OO00 )==True :#line:557
        O00O00O0O0OOOOOO0 =Windows #line:558
        import glob as O0O0000000O0OOO0O #line:559
        for O000OO0O0O0OO000O in O0O0000000O0OOO0O .glob (os .path .join (O00O00O0O0OOOOOO0 ,'*.dmp')):#line:560
            OOO0O0O00O0OO000O =O000OO0O0O0OO000O #line:561
            log (O000OO0O0O0OO000O )#line:562
            os .remove (O000OO0O0O0OO000O )#line:563
        for O000OO0O0O0OO000O in O0O0000000O0OOO0O .glob (os .path .join (O00O00O0O0OOOOOO0 ,'*.txt')):#line:565
            OOO0O0O00O0OO000O =O000OO0O0O0OO000O #line:566
            log (O000OO0O0O0OO000O )#line:567
            os .remove (O000OO0O0O0OO000O )#line:568
    if os .path .exists (OO00O0OOO0O000O00 )==True :#line:570
        O00O00O0O0OOOOOO0 =OO00O0OOO0O000O00 #line:571
        import glob as O0O0000000O0OOO0O #line:572
        for O000OO0O0O0OO000O in O0O0000000O0OOO0O .glob (os .path .join (O00O00O0O0OOOOOO0 ,'*.dmp')):#line:573
            OOO0O0O00O0OO000O =O000OO0O0O0OO000O #line:574
            log (O000OO0O0O0OO000O )#line:575
            os .remove (O000OO0O0O0OO000O )#line:576
        for O000OO0O0O0OO000O in O0O0000000O0OOO0O .glob (os .path .join (O00O00O0O0OOOOOO0 ,'*.txt')):#line:578
            OOO0O0O00O0OO000O =O000OO0O0O0OO000O #line:579
            log (O000OO0O0O0OO000O )#line:580
            os .remove (O000OO0O0O0OO000O )#line:581
    if os .path .exists (O0O000O0O00O0O0OO )==True :#line:583
        O00O00O0O0OOOOOO0 =O0O000O0O00O0O0OO #line:584
        import glob as O0O0000000O0OOO0O #line:585
        for O000OO0O0O0OO000O in O0O0000000O0OOO0O .glob (os .path .join (O00O00O0O0OOOOOO0 ,'*.dmp')):#line:586
            OOO0O0O00O0OO000O =O000OO0O0O0OO000O #line:587
            log (O000OO0O0O0OO000O )#line:588
            os .remove (O000OO0O0O0OO000O )#line:589
        for O000OO0O0O0OO000O in O0O0000000O0OOO0O .glob (os .path .join (O00O00O0O0OOOOOO0 ,'*.txt')):#line:591
            OOO0O0O00O0OO000O =O000OO0O0O0OO000O #line:592
            log (O000OO0O0O0OO000O )#line:593
            os .remove (O000OO0O0O0OO000O )#line:594
def Fix_Special (url ):#line:601
    OO0O0OO000OOO00O0 =xbmc .translatePath ('special://home')#line:602
    dp .create (MainTitle ,"Renaming paths...",'','Please Wait')#line:603
    for O0O0OO0OOO0OO0O00 ,O00O0O0OOOO0O0000 ,O00O000OOOO00OOOO in os .walk (OO0O0OO000OOO00O0 ):#line:604
        for OOO0O0O0O000OO00O in O00O000OOOO00OOOO :#line:605
            if OOO0O0O0O000OO00O .endswith (".xml"):#line:606
                 dp .update (0 ,"Fixing","[COLOR green]"+OOO0O0O0O000OO00O +"[/COLOR]","Please wait.....")#line:607
                 OOO00OO000O00OO0O =open ((os .path .join (O0O0OO0OOO0OO0O00 ,OOO0O0O0O000OO00O ))).read ()#line:608
                 OOO0O0000O000OO0O =OOO00OO000O00OO0O .replace (OO0O0OO000OOO00O0 ,'special://home/')#line:609
                 O0OO00O000000O0OO =open ((os .path .join (O0O0OO0OOO0OO0O00 ,OOO0O0O0O000OO00O )),mode ='w')#line:610
                 O0OO00O000000O0OO .write (str (OOO0O0000O000OO0O ))#line:611
                 O0OO00O000000O0OO .close ()#line:612
    dialog .ok (MainTitle ,'All physical (home) paths have been converted to special','To complete this process Kodi will force close now!')#line:614
    Common .killKodi ()#line:615
def xvbmcLog ():#line:622
    O00000O00O00OO0O0 =xbmc .translatePath ('special://logpath/kodi.log')#line:623
    O00OOOO00O0O0OO00 =xbmc .translatePath ('special://logpath/spmc.log')#line:624
    O0OOO0OO00OOO00OO =xbmc .translatePath ('special://logpath/spmc.log')#line:625
    OO0O000O000O0O00O =xbmc .translatePath ('special://logpath/kodi.old.log')#line:626
    OO00OOOOO0000O000 =xbmc .translatePath ('special://logpath/spmc.old.log')#line:627
    O000OO0O00OOOOO0O =xbmc .translatePath ('special://logpath/kodi.old.log')#line:628
    if os .path .exists (O00OOOO00O0O0OO00 ):#line:630
        if os .path .exists (O00OOOO00O0O0OO00 )and os .path .exists (OO00OOOOO0000O000 ):#line:631
            OO000O0O0OO00000O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:632
            if OO000O0O0OO00000O ==0 :#line:633
                O0OOO000OO00OO000 =open (O00OOOO00O0O0OO00 ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:634
                Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:635
            else :#line:636
                O0OOO000OO00OO000 =open (OO00OOOOO0000O000 ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:637
                Common .TextBoxes ("%s - spmc.old.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:638
        else :#line:639
            O0OOO000OO00OO000 =open (O00OOOO00O0O0OO00 ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:640
            Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:641
    if os .path .exists (O00000O00O00OO0O0 ):#line:643
        if os .path .exists (O00000O00O00OO0O0 )and os .path .exists (OO0O000O000O0O00O ):#line:644
            OO000O0O0OO00000O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:645
            if OO000O0O0OO00000O ==0 :#line:646
                O0OOO000OO00OO000 =open (O00000O00O00OO0O0 ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:647
                Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:648
            else :#line:649
                O0OOO000OO00OO000 =open (OO0O000O000O0O00O ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:650
                Common .TextBoxes ("%s - kodi.old.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:651
        else :#line:652
            O0OOO000OO00OO000 =open (O00000O00O00OO0O0 ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:653
            Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:654
    if os .path .exists (O0OOO0OO00OOO00OO ):#line:656
        if os .path .exists (O0OOO0OO00OOO00OO )and os .path .exists (O000OO0O00OOOOO0O ):#line:657
            OO000O0O0OO00000O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:658
            if OO000O0O0OO00000O ==0 :#line:659
                O0OOO000OO00OO000 =open (O0OOO0OO00OOO00OO ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:660
                Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:661
            else :#line:662
                O0OOO000OO00OO000 =open (O000OO0O00OOOOO0O ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:663
                Common .TextBoxes ("%s - dbmc.old.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:664
        else :#line:665
            O0OOO000OO00OO000 =open (O0OOO0OO00OOO00OO ,mode ='r');O00O00O0O0OO00O00 =O0OOO000OO00OO000 .read ();O0OOO000OO00OO000 .close ()#line:666
            Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O00O00O0O0OO00O00 +"[/COLOR]")#line:667
    if os .path .isfile (O00000O00O00OO0O0 )or os .path .isfile (O00OOOO00O0O0OO00 )or os .path .isfile (O0OOO0OO00OOO00OO ):#line:669
        return True #line:670
    else :#line:671
        dialog .ok (MainTitle ,'Sorry, No log file was found.','','[COLOR yellow]Sorry, er was geen log file gevonden.[/COLOR]')#line:672
if Common .get_kversion ()>16.5 :#line:679
    try :from sqlite3 import dbapi2 as db_lib #line:680
    except :from pysqlite2 import dbapi2 as db_lib #line:681
    db_dir =xbmc .translatePath ("special://profile/Database")#line:683
    db_path =os .path .join (db_dir ,'Addons27.db')#line:684
    conn =db_lib .connect (db_path )#line:685
    conn .text_factory =str #line:686
def AddonsEnable ():#line:688
    if Common .get_kversion ()>16.5 :#line:689
        OOO000O000O0OO000 =sqlite3 .connect (xbmc .translatePath ("special://database/Addons27.db"))#line:690
        OOOOOO0O0OOOOO000 =OOO000O000O0OO000 .cursor ()#line:691
        OOOOOO0O0OOOOO000 .execute ("UPDATE installed SET enabled = 1 WHERE addonID NOT LIKE '%audiodecoder.%' AND addonID NOT LIKE '%inputstream.%' AND addonID NOT LIKE '%pvr.%' AND addonID NOT LIKE '%screensaver.%' AND addonID NOT LIKE '%visualization.%';")#line:692
        OOO000O000O0OO000 .commit ()#line:693
        OOO000O000O0OO000 .close ()#line:694
        xbmc .executebuiltin ('UpdateLocalAddons()')#line:695
        xbmc .executebuiltin ('UpdateAddonRepos()')#line:696
        OOO0OOOO0000OOOOO =xbmcgui .Dialog ().yesno (MainTitle +' : add-ons [B]enabled[/B]','[COLOR=green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete (\'yes\' is force close)','[B]Herstart[/B] Kodi ter afronding (ja is \'force close\')',yeslabel ='[COLOR lime]Ja/Yes[/COLOR]',nolabel ='[COLOR red]Nee/No[/COLOR]')#line:697
        if OOO0OOOO0000OOOOO ==1 :#line:698
            os ._exit (1 )#line:699
        else :pass #line:700
    else :pass #line:701
def EnableRTMP ():#line:703
        try :addon_able .set_enabled ("inputstream.adaptive")#line:704
        except :pass #line:705
        time .sleep (0.5 )#line:706
        try :addon_able .set_enabled ("inputstream.rtmp")#line:707
        except :pass #line:708
        time .sleep (0.5 )#line:709
        xbmc .executebuiltin ('XBMC.UpdateLocalAddons()')#line:710
        dialog .ok ("Operation Complete!",'Live Streaming has been Enabled!','Brought To You By %s '%MainTitle )#line:712
"""
    IF you copy/paste 'huisvrouw.py' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""