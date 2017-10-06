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
    O00000000000O0OO0 =6 #line:67
    O00OOO0O0000000OO =["MP3 Streams","Quasar","SportsDevil","Simple Downloader","Spotitube","SkinHelperService"]#line:68
    OOO0O00O0OO00OOO0 =["special://profile/addon_data/plugin.audio.mp3streams/temp_dl","special://profile/addon_data/plugin.video.quasar/cache","special://profile/addon_data/plugin.video.SportsDevil/cache","special://profile/addon_data/script.module.simple.downloader","special://profile/addon_data/plugin.video.spotitube/cache","special://profile/addon_data/script.skin.helper.service/musicartcache"]#line:74
    O0O000O0O0O00O0OO =[]#line:76
    for O00O00OO0O000OOOO in range (O00000000000O0OO0 ):#line:78
        O0O000O0O0O00O0OO .append (cacheEntry (O00OOO0O0000000OO [O00O00OO0O000OOOO ],OOO0O00O0OO00OOO0 [O00O00OO0O000OOOO ]))#line:79
    return O0O000O0O0O00O0OO #line:81
def clearCache ():#line:88
    if os .path .exists (cachePath )==True :#line:89
        for O0O00OO0000O0OOOO ,O000OO000OOO00000 ,O000000O00OOO0O0O in os .walk (cachePath ):#line:90
            O000OOOOO0OO0O0O0 =0 #line:91
            O000OOOOO0OO0O0O0 +=len (O000000O00OOO0O0O )#line:92
            if O000OOOOO0OO0O0O0 >0 :#line:93
                if dialog .yesno ("Delete Cache Files",str (O000OOOOO0OO0O0O0 )+' files found','Do you want to delete them?'):#line:95
                    for OOOO0OOOO0O00000O in O000000O00OOO0O0O :#line:96
                        try :#line:97
                            if (OOOO0OOOO0O00000O .endswith (".log")):continue #line:99
                            os .unlink (os .path .join (O0O00OO0000O0OOOO ,OOOO0OOOO0O00000O ))#line:100
                        except :#line:101
                            pass #line:102
                    for O0OOO00OOOO00OO00 in O000OO000OOO00000 :#line:103
                        try :#line:104
                            O0OOOO0000O0OOO0O =(os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:106
                            if not "archive_cache"in str (O0OOOO0000O0OOO0O ):#line:107
                                shutil .rmtree (os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:108
                        except :#line:109
                            pass #line:110
            else :#line:111
                pass #line:112
    if os .path .exists (tempPath )==True :#line:114
        for O0O00OO0000O0OOOO ,O000OO000OOO00000 ,O000000O00OOO0O0O in os .walk (tempPath ):#line:115
            O000OOOOO0OO0O0O0 =0 #line:116
            O000OOOOO0OO0O0O0 +=len (O000000O00OOO0O0O )#line:117
            if O000OOOOO0OO0O0O0 >0 :#line:118
                if dialog .yesno ("Delete Temp Files",str (O000OOOOO0OO0O0O0 )+' files found','Do you want to delete them?'):#line:120
                    for OOOO0OOOO0O00000O in O000000O00OOO0O0O :#line:121
                        try :#line:122
                            if (OOOO0OOOO0O00000O .endswith (".log")):continue #line:124
                            os .unlink (os .path .join (O0O00OO0000O0OOOO ,OOOO0OOOO0O00000O ))#line:125
                        except :#line:126
                            pass #line:127
                    for O0OOO00OOOO00OO00 in O000OO000OOO00000 :#line:128
                        try :#line:129
                            O0OOOO0000O0OOO0O =(os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:131
                            if not "archive_cache"in str (O0OOOO0000O0OOO0O ):#line:132
                                shutil .rmtree (os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:133
                        except :#line:134
                            pass #line:135
            else :#line:136
                pass #line:137
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:139
        OOOO000O0OO00O0O0 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:140
        for O0O00OO0000O0OOOO ,O000OO000OOO00000 ,O000000O00OOO0O0O in os .walk (OOOO000O0OO00O0O0 ):#line:141
            O000OOOOO0OO0O0O0 =0 #line:142
            O000OOOOO0OO0O0O0 +=len (O000000O00OOO0O0O )#line:143
            if O000OOOOO0OO0O0O0 >0 :#line:144
                if dialog .yesno ("Delete ATV2 Cache Files",str (O000OOOOO0OO0O0O0 )+" files found in 'Other'",'Do you want to delete them?'):#line:146
                    for OOOO0OOOO0O00000O in O000000O00OOO0O0O :#line:147
                        try :#line:149
                            if (OOOO0OOOO0O00000O .endswith (".log")):continue #line:150
                            os .unlink (os .path .join (O0O00OO0000O0OOOO ,OOOO0OOOO0O00000O ))#line:151
                        except :#line:152
                            pass #line:153
                    for O0OOO00OOOO00OO00 in O000OO000OOO00000 :#line:154
                        try :#line:156
                            O0OOOO0000O0OOO0O =(os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:157
                            if not "archive_cache"in str (O0OOOO0000O0OOO0O ):#line:158
                                shutil .rmtree (os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:159
                        except :#line:160
                            pass #line:161
            else :#line:162
                pass #line:163
        OOO0O00O0000000OO =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:165
        for O0O00OO0000O0OOOO ,O000OO000OOO00000 ,O000000O00OOO0O0O in os .walk (OOO0O00O0000000OO ):#line:166
            O000OOOOO0OO0O0O0 =0 #line:167
            O000OOOOO0OO0O0O0 +=len (O000000O00OOO0O0O )#line:168
            if O000OOOOO0OO0O0O0 >0 :#line:169
                if dialog .yesno ("Delete ATV2 Cache Files",str (O000OOOOO0OO0O0O0 )+" files found in 'LocalAndRental'",'Do you want to delete them?'):#line:171
                    for OOOO0OOOO0O00000O in O000000O00OOO0O0O :#line:172
                        try :#line:174
                            if (OOOO0OOOO0O00000O .endswith (".log")):continue #line:175
                            os .unlink (os .path .join (O0O00OO0000O0OOOO ,OOOO0OOOO0O00000O ))#line:176
                        except :#line:177
                            pass #line:178
                    for O0OOO00OOOO00OO00 in O000OO000OOO00000 :#line:179
                        try :#line:181
                            O0OOOO0000O0OOO0O =(os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:182
                            if not "archive_cache"in str (O0OOOO0000O0OOO0O ):#line:183
                                shutil .rmtree (os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:184
                        except :#line:185
                            pass #line:186
            else :#line:187
                pass #line:188
    OO00OOO0000O0O0OO =setupCacheEntries ()#line:190
    for OOOO0O00OO00OO000 in OO00OOO0000O0O0OO :#line:191
        OO0OOOOO00O0OO00O =xbmc .translatePath (OOOO0O00OO00OO000 .path )#line:192
        if os .path .exists (OO0OOOOO00O0OO00O )==True :#line:193
            for O0O00OO0000O0OOOO ,O000OO000OOO00000 ,O000000O00OOO0O0O in os .walk (OO0OOOOO00O0OO00O ):#line:194
                O000OOOOO0OO0O0O0 =0 #line:195
                O000OOOOO0OO0O0O0 +=len (O000000O00OOO0O0O )#line:196
                if O000OOOOO0OO0O0O0 >0 :#line:197
                    if dialog .yesno (MainTitle ,'%s cache files found'%(OOOO0O00OO00OO000 .name ),'Do you want to delete them?'):#line:200
                        for OOOO0OOOO0O00000O in O000000O00OOO0O0O :#line:201
                            try :#line:203
                                if (OOOO0OOOO0O00000O .endswith (".log")):continue #line:204
                                os .unlink (os .path .join (O0O00OO0000O0OOOO ,OOOO0OOOO0O00000O ))#line:205
                            except :#line:206
                                pass #line:207
                        for O0OOO00OOOO00OO00 in O000OO000OOO00000 :#line:208
                            try :#line:210
                                O0OOOO0000O0OOO0O =(os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:211
                                if not "archive_cache"in str (O0OOOO0000O0OOO0O ):#line:212
                                    shutil .rmtree (os .path .join (O0O00OO0000O0OOOO ,O0OOO00OOOO00OO00 ))#line:213
                            except :#line:214
                                pass #line:215
                else :#line:216
                    pass #line:217
    dialog .ok (MainTitle ,'Done Clearing Cache files')#line:219
    xbmc .executebuiltin ("Container.Refresh")#line:220
def deleteThumbnails ():#line:227
    if os .path .exists (thumbnailPath )==True :#line:228
            if dialog .yesno ("Delete Thumbnails",'This option deletes all thumbnails','Are you sure you want to do this?'):#line:230
                for O0OO00O00OO0O000O ,O00O00OOOOOO0000O ,O00OO0O0000OOOOO0 in os .walk (thumbnailPath ):#line:231
                    OOOOO00OOOOOOOOO0 =0 #line:232
                    OOOOO00OOOOOOOOO0 +=len (O00OO0O0000OOOOO0 )#line:233
                    if OOOOO00OOOOOOOOO0 >0 :#line:234
                        for OO0O0OOOO000OO0OO in O00OO0O0000OOOOO0 :#line:235
                            try :#line:236
                                os .unlink (os .path .join (O0OO00O00OO0O000O ,OO0O0OOOO000OO0OO ))#line:237
                            except :#line:238
                                pass #line:239
    else :#line:240
        pass #line:241
    OO00000OO0O00OOO0 =os .path .join (databasePath ,"Textures13.db")#line:243
    try :#line:244
        os .unlink (OO00000OO0O00OOO0 )#line:245
    except OSError :#line:246
        try :#line:247
            O00OO0000O0000OOO =sqlite3 .connect (OO00000OO0O00OOO0 )#line:248
            OOO0O0O00OO0000O0 =O00OO0000O0000OOO .cursor ()#line:249
            OOO0O0O00OO0000O0 .execute ('DROP TABLE IF EXISTS path')#line:250
            OOO0O0O00OO0000O0 .execute ('VACUUM')#line:251
            O00OO0000O0000OOO .commit ()#line:252
            OOO0O0O00OO0000O0 .execute ('DROP TABLE IF EXISTS sizes')#line:253
            OOO0O0O00OO0000O0 .execute ('VACUUM')#line:254
            O00OO0000O0000OOO .commit ()#line:255
            OOO0O0O00OO0000O0 .execute ('DROP TABLE IF EXISTS texture')#line:256
            OOO0O0O00OO0000O0 .execute ('VACUUM')#line:257
            O00OO0000O0000OOO .commit ()#line:258
            OOO0O0O00OO0000O0 .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:260
            O00OO0000O0000OOO .commit ()#line:261
            OOO0O0O00OO0000O0 .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:263
            O00OO0000O0000OOO .commit ()#line:264
            OOO0O0O00OO0000O0 .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:266
            O00OO0000O0000OOO .commit ()#line:267
        except :#line:268
            pass #line:269
    dialog .ok (MainTitle ,'Please reboot your system to rebuild thumbnail folder...')#line:271
    xbmc .executebuiltin ("Container.Refresh")#line:272
def PiCCleaner ():#line:279
    OO00O00OOO0O00O0O =platform ()#line:280
    log ("XvBMC_Platform: "+str (OO00O00OOO0O00O0O ))#line:281
    if not OO00O00OOO0O00O0O =='linux':#line:282
       dialog .ok (MainTitle +SubTitle ,subtitleNope ,nonlinux ,nonelecNL )#line:283
       log ("none Linux OS ie. Open-/LibreELEC")#line:284
    else :#line:285
        log ("linux os")#line:286
        if dialog .yesno (MainTitle +SubTitle ,'about to do some extreme CrapCleaner voodoo...','[I]this will take a few seconds to complete, be patient![/I]','[B]are you sure[COLOR white]?[/COLOR][/B]'):#line:287
            O00OOO00O000OO0O0 ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/rpiecc.sh"#line:288
            os .system (O00OOO00O000OO0O0 )#line:289
            dialog .ok (MainTitle +SubTitle ,'[B]RPi[/B] CrapCleaner finished!','','Press OK to reboot...')#line:290
            xbmc .executebuiltin ("Reboot")#line:291
def purgePackages ():#line:298
    O0O00OO0OOO0OO0OO =xbmc .translatePath ('special://home/addons/packages')#line:299
    for O0OOO0O0O00OOO000 ,O00OO0O000000000O ,OOOO000O0OO00OO0O in os .walk (O0O00OO0OOO0OO0OO ):#line:301
            OO0OO00O00OOOO00O =0 #line:302
            OO0OO00O00OOOO00O +=len (OOOO000O0OO00OO0O )#line:303
    if dialog .yesno ("Delete Package Cache Files",'%d packages found.'%OO0OO00O00OOOO00O ,'Delete Them?'):#line:304
        for O0OOO0O0O00OOO000 ,O00OO0O000000000O ,OOOO000O0OO00OO0O in os .walk (O0O00OO0OOO0OO0OO ):#line:305
            OO0OO00O00OOOO00O =0 #line:306
            OO0OO00O00OOOO00O +=len (OOOO000O0OO00OO0O )#line:307
            if OO0OO00O00OOOO00O >0 :#line:308
                try :#line:309
                    for OOOOOOOOO0O00O0OO in OOOO000O0OO00OO0O :#line:310
                        os .unlink (os .path .join (O0OOO0O0O00OOO000 ,OOOOOOOOO0O00O0OO ))#line:311
                    for OO00O000000O00OO0 in O00OO0O000000000O :#line:312
                        shutil .rmtree (os .path .join (O0OOO0O0O00OOO000 ,OO00O000000O00OO0 ))#line:313
                except :pass #line:314
                dialog .ok (MainTitle ,'Deleting Packages all done')#line:315
            else :#line:317
                dialog .ok (MainTitle ,'No Packages to Purge')#line:318
    xbmc .executebuiltin ("Container.Refresh")#line:320
def AddonsDatabaseRemoval ():#line:327
    OOO000OO0O0O000OO =os .listdir (databasePath )#line:328
    O0OOOOO00O00OO00O =[]#line:329
    O00OOOOOO0O00000O =True #line:330
    if dialog .yesno ("[COLOR lime]"+MainTitle +"[/COLOR]",' ','[COLOR red]Are YOU Sure [B]?!?[/B][/COLOR]'):#line:338
        if int (kodiver )<=16.7 :#line:339
           try :#line:340
               for O0O0O000O00OOOO0O in OOO000OO0O0O000OO :#line:341
                   if re .findall ('Addons(\d+)\.db',O0O0O000O00OOOO0O ):#line:342
                       O0OOOOO00O00OO00O .append (O0O0O000O00OOOO0O )#line:343
               for O0O0O000O00OOOO0O in O0OOOOO00O00OO00O :#line:344
                   OOO0O0O0O00OOOO00 =os .path .join (databasePath ,O0O0O000O00OOOO0O )#line:345
                   OO00O0O0O0OO0000O =open (OOO0O0O0O00OOOO00 ,'ab+')#line:346
                   try :#line:347
                       OO00O0O0O0OO0000O .close ()#line:349
                       os .remove (OO00O0O0O0OO0000O .name )#line:350
                   except :#line:351
                       O00OOOOOO0O00000O =False #line:352
               if O00OOOOOO0O00000O :#line:353
                   dialog .ok (MainTitle ,'Your system will [COLOR red]reboot[/COLOR] to rebuild addons.db...')#line:354
                   Common .killKodi #line:355
               else :#line:356
                   dialog .ok (MainTitle ,'Removal [COLOR red]failed![/COLOR]','try manual remove, see: [COLOR green]http://kodi.wiki/view/Database_version[/COLOR]')#line:357
           except :#line:358
               pass #line:359
        else :#line:360
           dialog .ok (MainTitle ,'This feature is not available in Kodi 17 Krypton','','[COLOR yellow]Thank you for using XvBMC Maintenance[/COLOR]')#line:361
def autocleanask ():#line:368
    O00000000O0OOOO0O =xbmcgui .Dialog ().yesno (MainTitle ,'Select [COLOR green]YES[/COLOR] to delete your:','cache, crashlogs, packages & thumbnails all at once.','[I][COLOR white]Do you wish to continue[B]?[/B][/I][/COLOR]',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:370
    if O00000000O0OOOO0O ==1 :#line:371
        autocleannow ()#line:372
def autocleannow ():#line:374
    OO0OO00O00O0OO000 =True #line:375
    if os .path .exists (cachePath )==True :#line:377
        for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (cachePath ):#line:378
            OO0000OOOO0000OOO =0 #line:379
            OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:380
            if OO0000OOOO0000OOO >0 :#line:381
                    for O000OOOOO0OOOOO00 in O000OOOOOO00O0O0O :#line:382
                        try :#line:383
                            if (O000OOOOO0OOOOO00 .endswith (".log")):continue #line:384
                            os .unlink (os .path .join (OO00O0OOOO0OOO000 ,O000OOOOO0OOOOO00 ))#line:385
                        except :#line:386
                            pass #line:387
                    for O000OO0O0O00O0O00 in O0OOOO000OOOOOOOO :#line:388
                        try :#line:389
                            O0O0OOOO00OOO0O0O =(os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:390
                            if not "archive_cache"in str (O0O0OOOO00OOO0O0O ):#line:391
                                shutil .rmtree (os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:392
                        except :#line:393
                            pass #line:394
            else :pass #line:395
    if os .path .exists (tempPath )==True :#line:397
        for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (tempPath ):#line:398
            OO0000OOOO0000OOO =0 #line:399
            OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:400
            if OO0000OOOO0000OOO >0 :#line:401
                    for O000OOOOO0OOOOO00 in O000OOOOOO00O0O0O :#line:402
                        try :#line:403
                            if (O000OOOOO0OOOOO00 .endswith (".log")):continue #line:404
                            os .unlink (os .path .join (OO00O0OOOO0OOO000 ,O000OOOOO0OOOOO00 ))#line:405
                        except :#line:406
                            pass #line:407
                    for O000OO0O0O00O0O00 in O0OOOO000OOOOOOOO :#line:408
                        try :#line:409
                            O0O0OOOO00OOO0O0O =(os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:410
                            if not "archive_cache"in str (O0O0OOOO00OOO0O0O ):#line:411
                                shutil .rmtree (os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:412
                        except :#line:413
                            pass #line:414
            else :pass #line:415
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:417
        OO00OOOOO0O0O000O =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:418
        for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (OO00OOOOO0O0O000O ):#line:419
            OO0000OOOO0000OOO =0 #line:420
            OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:421
            if OO0000OOOO0000OOO >0 :#line:423
                    for O000OOOOO0OOOOO00 in O000OOOOOO00O0O0O :#line:424
                        try :#line:425
                            if (O000OOOOO0OOOOO00 .endswith (".log")):continue #line:426
                            os .unlink (os .path .join (OO00O0OOOO0OOO000 ,O000OOOOO0OOOOO00 ))#line:427
                        except :#line:428
                            pass #line:429
                    for O000OO0O0O00O0O00 in O0OOOO000OOOOOOOO :#line:430
                        try :#line:431
                            O0O0OOOO00OOO0O0O =(os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:432
                            if not "archive_cache"in str (O0O0OOOO00OOO0O0O ):#line:433
                                shutil .rmtree (os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:434
                        except :#line:435
                            pass #line:436
            else :pass #line:437
        O0O0O0O00000O00O0 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:439
        for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (O0O0O0O00000O00O0 ):#line:440
            OO0000OOOO0000OOO =0 #line:441
            OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:442
            if OO0000OOOO0000OOO >0 :#line:444
                    for O000OOOOO0OOOOO00 in O000OOOOOO00O0O0O :#line:445
                        try :#line:446
                            if (O000OOOOO0OOOOO00 .endswith (".log")):continue #line:447
                            os .unlink (os .path .join (OO00O0OOOO0OOO000 ,O000OOOOO0OOOOO00 ))#line:448
                        except :#line:449
                            pass #line:450
                    for O000OO0O0O00O0O00 in O0OOOO000OOOOOOOO :#line:451
                        try :#line:452
                            O0O0OOOO00OOO0O0O =(os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:453
                            if not "archive_cache"in str (O0O0OOOO00OOO0O0O ):#line:454
                                shutil .rmtree (os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:455
                        except :#line:456
                            pass #line:457
            else :pass #line:458
    OO0OO0OOO00OO0OOO =setupCacheEntries ()#line:460
    for OO0OOO0OOO0O00OO0 in OO0OO0OOO00OO0OOO :#line:461
        OO0OOO00000000O0O =xbmc .translatePath (OO0OOO0OOO0O00OO0 .path )#line:462
        if os .path .exists (OO0OOO00000000O0O )==True :#line:463
            for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (OO0OOO00000000O0O ):#line:464
                OO0000OOOO0000OOO =0 #line:465
                OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:466
                if OO0000OOOO0000OOO >0 :#line:467
                    for O000OOOOO0OOOOO00 in O000OOOOOO00O0O0O :#line:468
                        try :#line:469
                            if (O000OOOOO0OOOOO00 .endswith (".log")):continue #line:470
                            os .unlink (os .path .join (OO00O0OOOO0OOO000 ,O000OOOOO0OOOOO00 ))#line:471
                        except :#line:472
                            pass #line:473
                    for O000OO0O0O00O0O00 in O0OOOO000OOOOOOOO :#line:474
                        try :#line:475
                            O0O0OOOO00OOO0O0O =(os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:476
                            if not "archive_cache"in str (O0O0OOOO00OOO0O0O ):#line:477
                                shutil .rmtree (os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:478
                        except :#line:479
                            pass #line:480
                else :pass #line:481
    if dialog .yesno (MainTitle ,'[COLOR red]This option also deletes all your thumbnails...[/COLOR]','[COLOR green]Are you sure you want to do this[B]?[/B][/COLOR]'):#line:483
        if os .path .exists (thumbnailPath )==True :#line:484
                for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (thumbnailPath ):#line:485
                    OO0000OOOO0000OOO =0 #line:486
                    OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:487
                    if OO0000OOOO0000OOO >0 :#line:488
                        for O000OOOOO0OOOOO00 in O000OOOOOO00O0O0O :#line:489
                            try :#line:490
                                os .unlink (os .path .join (OO00O0OOOO0OOO000 ,O000OOOOO0OOOOO00 ))#line:491
                            except :#line:492
                                pass #line:493
        else :pass #line:494
        OO00OO00OOO0000O0 =os .path .join (databasePath ,"Textures13.db")#line:496
        try :#line:497
            os .unlink (OO00OO00OOO0000O0 )#line:498
        except OSError :#line:499
            try :#line:500
                OOO0OOO0OOOOO000O =sqlite3 .connect (OO00OO00OOO0000O0 )#line:501
                OO00OO00OOO0O0O0O =OOO0OOO0OOOOO000O .cursor ()#line:502
                OO00OO00OOO0O0O0O .execute ('DROP TABLE IF EXISTS path')#line:503
                OO00OO00OOO0O0O0O .execute ('VACUUM')#line:504
                OOO0OOO0OOOOO000O .commit ()#line:505
                OO00OO00OOO0O0O0O .execute ('DROP TABLE IF EXISTS sizes')#line:506
                OO00OO00OOO0O0O0O .execute ('VACUUM')#line:507
                OOO0OOO0OOOOO000O .commit ()#line:508
                OO00OO00OOO0O0O0O .execute ('DROP TABLE IF EXISTS texture')#line:509
                OO00OO00OOO0O0O0O .execute ('VACUUM')#line:510
                OOO0OOO0OOOOO000O .commit ()#line:511
                OO00OO00OOO0O0O0O .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:513
                OOO0OOO0OOOOO000O .commit ()#line:514
                OO00OO00OOO0O0O0O .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:516
                OOO0OOO0OOOOO000O .commit ()#line:517
                OO00OO00OOO0O0O0O .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:519
                OOO0OOO0OOOOO000O .commit ()#line:520
            except :#line:521
                pass #line:522
    OO0OO0OOO00OOO0O0 =xbmc .translatePath ('special://home/addons/packages')#line:524
    for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (OO0OO0OOO00OOO0O0 ):#line:525
            OO0000OOOO0000OOO =0 #line:526
            OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:527
    for OO00O0OOOO0OOO000 ,O0OOOO000OOOOOOOO ,O000OOOOOO00O0O0O in os .walk (OO0OO0OOO00OOO0O0 ):#line:528
            OO0000OOOO0000OOO =0 #line:529
            OO0000OOOO0000OOO +=len (O000OOOOOO00O0O0O )#line:530
            if OO0000OOOO0000OOO >0 :#line:531
                try :#line:532
                    for O000OOOOO0OOOOO00 in O000OOOOOO00O0O0O :#line:533
                        os .unlink (os .path .join (OO00O0OOOO0OOO000 ,O000OOOOO0OOOOO00 ))#line:534
                    for O000OO0O0O00O0O00 in O0OOOO000OOOOOOOO :#line:535
                        shutil .rmtree (os .path .join (OO00O0OOOO0OOO000 ,O000OO0O0O00O0O00 ))#line:536
                except :#line:537
                    pass #line:538
    if OO0OO00O00O0OO000 ==True :#line:540
        AutoCrash ()#line:542
    else :#line:543
        xbmc .log (str (OO0OO00O00O0OO000 ))#line:545
    O00OO00O0000000O0 =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR white][B]A[/B]uto [B]C[/B]lean finished:[/COLOR]','[I]cache, crashlogs, packages & thumbnails are removed.[/I]','Reboot your device now to finish the process?',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:547
    if O00OO00O0000000O0 ==1 :#line:548
         Common .killKodi ()#line:549
def AutoCrash ():#line:551
    OOO000OOO0O0O00OO =xbmc .translatePath ('special://home')#line:553
    O0O0O0OO00O00O0O0 =os .path .join (xbmc .translatePath ('special://home'),'cache')#line:554
    OO00OOO00000O0000 =os .path .join (xbmc .translatePath ('special://home'),'temp')#line:555
    if os .path .exists (OOO000OOO0O0O00OO )==True :#line:557
        OOO00O0O00O0OO00O =Windows #line:558
        import glob as OOOO000OOOOOOOO0O #line:559
        for O0O00O0OO0O0000O0 in OOOO000OOOOOOOO0O .glob (os .path .join (OOO00O0O00O0OO00O ,'*.dmp')):#line:560
            O0OOOO000O0OOO000 =O0O00O0OO0O0000O0 #line:561
            log (O0O00O0OO0O0000O0 )#line:562
            os .remove (O0O00O0OO0O0000O0 )#line:563
        for O0O00O0OO0O0000O0 in OOOO000OOOOOOOO0O .glob (os .path .join (OOO00O0O00O0OO00O ,'*.txt')):#line:565
            O0OOOO000O0OOO000 =O0O00O0OO0O0000O0 #line:566
            log (O0O00O0OO0O0000O0 )#line:567
            os .remove (O0O00O0OO0O0000O0 )#line:568
    if os .path .exists (O0O0O0OO00O00O0O0 )==True :#line:570
        OOO00O0O00O0OO00O =O0O0O0OO00O00O0O0 #line:571
        import glob as OOOO000OOOOOOOO0O #line:572
        for O0O00O0OO0O0000O0 in OOOO000OOOOOOOO0O .glob (os .path .join (OOO00O0O00O0OO00O ,'*.dmp')):#line:573
            O0OOOO000O0OOO000 =O0O00O0OO0O0000O0 #line:574
            log (O0O00O0OO0O0000O0 )#line:575
            os .remove (O0O00O0OO0O0000O0 )#line:576
        for O0O00O0OO0O0000O0 in OOOO000OOOOOOOO0O .glob (os .path .join (OOO00O0O00O0OO00O ,'*.txt')):#line:578
            O0OOOO000O0OOO000 =O0O00O0OO0O0000O0 #line:579
            log (O0O00O0OO0O0000O0 )#line:580
            os .remove (O0O00O0OO0O0000O0 )#line:581
    if os .path .exists (OO00OOO00000O0000 )==True :#line:583
        OOO00O0O00O0OO00O =OO00OOO00000O0000 #line:584
        import glob as OOOO000OOOOOOOO0O #line:585
        for O0O00O0OO0O0000O0 in OOOO000OOOOOOOO0O .glob (os .path .join (OOO00O0O00O0OO00O ,'*.dmp')):#line:586
            O0OOOO000O0OOO000 =O0O00O0OO0O0000O0 #line:587
            log (O0O00O0OO0O0000O0 )#line:588
            os .remove (O0O00O0OO0O0000O0 )#line:589
        for O0O00O0OO0O0000O0 in OOOO000OOOOOOOO0O .glob (os .path .join (OOO00O0O00O0OO00O ,'*.txt')):#line:591
            O0OOOO000O0OOO000 =O0O00O0OO0O0000O0 #line:592
            log (O0O00O0OO0O0000O0 )#line:593
            os .remove (O0O00O0OO0O0000O0 )#line:594
def Fix_Special (url ):#line:601
    O0OO00O0OOOOOO00O =xbmc .translatePath ('special://home')#line:602
    dp .create (MainTitle ,"Renaming paths...",'','Please Wait')#line:603
    for O0O00OO00000OOO00 ,O0000O000OO0O00O0 ,OOOOO0OO0O0000OO0 in os .walk (O0OO00O0OOOOOO00O ):#line:604
        for OO0OOO0OO0O00O000 in OOOOO0OO0O0000OO0 :#line:605
            if OO0OOO0OO0O00O000 .endswith (".xml"):#line:606
                 dp .update (0 ,"Fixing","[COLOR green]"+OO0OOO0OO0O00O000 +"[/COLOR]","Please wait.....")#line:607
                 OOO0O0OOOO0O0OO00 =open ((os .path .join (O0O00OO00000OOO00 ,OO0OOO0OO0O00O000 ))).read ()#line:608
                 O0OO0OOOO00000O00 =OOO0O0OOOO0O0OO00 .replace (O0OO00O0OOOOOO00O ,'special://home/')#line:609
                 OOO0O00O00OOO0O0O =open ((os .path .join (O0O00OO00000OOO00 ,OO0OOO0OO0O00O000 )),mode ='w')#line:610
                 OOO0O00O00OOO0O0O .write (str (O0OO0OOOO00000O00 ))#line:611
                 OOO0O00O00OOO0O0O .close ()#line:612
    dialog .ok (MainTitle ,'All physical (home) paths have been converted to special','To complete this process Kodi will force close now!')#line:614
    Common .killKodi ()#line:615
def xvbmcLog ():#line:622
    OOOOOOOO000OO0O0O =xbmc .translatePath ('special://logpath/kodi.log')#line:623
    O000000O0000OO00O =xbmc .translatePath ('special://logpath/spmc.log')#line:624
    O000OO0O0OO000OOO =xbmc .translatePath ('special://logpath/spmc.log')#line:625
    OO000OO0OOOOO0O00 =xbmc .translatePath ('special://logpath/kodi.old.log')#line:626
    O0OOO0O0O000OOOOO =xbmc .translatePath ('special://logpath/spmc.old.log')#line:627
    O0000O0OO0O000O00 =xbmc .translatePath ('special://logpath/kodi.old.log')#line:628
    if os .path .exists (O000000O0000OO00O ):#line:630
        if os .path .exists (O000000O0000OO00O )and os .path .exists (O0OOO0O0O000OOOOO ):#line:631
            OOOO0OOO000OOO00O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:632
            if OOOO0OOO000OOO00O ==0 :#line:633
                OOO00OOO0O000OO00 =open (O000000O0000OO00O ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:634
                Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:635
            else :#line:636
                OOO00OOO0O000OO00 =open (O0OOO0O0O000OOOOO ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:637
                Common .TextBoxes ("%s - spmc.old.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:638
        else :#line:639
            OOO00OOO0O000OO00 =open (O000000O0000OO00O ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:640
            Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:641
    if os .path .exists (OOOOOOOO000OO0O0O ):#line:643
        if os .path .exists (OOOOOOOO000OO0O0O )and os .path .exists (OO000OO0OOOOO0O00 ):#line:644
            OOOO0OOO000OOO00O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:645
            if OOOO0OOO000OOO00O ==0 :#line:646
                OOO00OOO0O000OO00 =open (OOOOOOOO000OO0O0O ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:647
                Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:648
            else :#line:649
                OOO00OOO0O000OO00 =open (OO000OO0OOOOO0O00 ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:650
                Common .TextBoxes ("%s - kodi.old.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:651
        else :#line:652
            OOO00OOO0O000OO00 =open (OOOOOOOO000OO0O0O ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:653
            Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:654
    if os .path .exists (O000OO0O0OO000OOO ):#line:656
        if os .path .exists (O000OO0O0OO000OOO )and os .path .exists (O0000O0OO0O000O00 ):#line:657
            OOOO0OOO000OOO00O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:658
            if OOOO0OOO000OOO00O ==0 :#line:659
                OOO00OOO0O000OO00 =open (O000OO0O0OO000OOO ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:660
                Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:661
            else :#line:662
                OOO00OOO0O000OO00 =open (O0000O0OO0O000O00 ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:663
                Common .TextBoxes ("%s - dbmc.old.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:664
        else :#line:665
            OOO00OOO0O000OO00 =open (O000OO0O0OO000OOO ,mode ='r');OO00000O00000O000 =OOO00OOO0O000OO00 .read ();OOO00OOO0O000OO00 .close ()#line:666
            Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+OO00000O00000O000 +"[/COLOR]")#line:667
    if os .path .isfile (OOOOOOOO000OO0O0O )or os .path .isfile (O000000O0000OO00O )or os .path .isfile (O000OO0O0OO000OOO ):#line:669
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
        O0O00O00OOO0OO00O =sqlite3 .connect (xbmc .translatePath ("special://database/Addons27.db"))#line:690
        O0OOO0O0OOO0OO000 =O0O00O00OOO0OO00O .cursor ()#line:691
        O0OOO0O0OOO0OO000 .execute ("UPDATE installed SET enabled = 1 WHERE addonID NOT LIKE '%audiodecoder.%' AND addonID NOT LIKE '%inputstream.%' AND addonID NOT LIKE '%pvr.%' AND addonID NOT LIKE '%screensaver.%' AND addonID NOT LIKE '%visualization.%';")#line:692
        O0O00O00OOO0OO00O .commit ()#line:693
        O0O00O00OOO0OO00O .close ()#line:694
        xbmc .executebuiltin ('UpdateLocalAddons()')#line:695
        xbmc .executebuiltin ('UpdateAddonRepos()')#line:696
        OOOOOO0O000000000 =xbmcgui .Dialog ().yesno (MainTitle +' : add-ons [B]enabled[/B]','[COLOR=green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete (\'yes\' is force close)','[B]Herstart[/B] Kodi ter afronding (ja is \'force close\')',yeslabel ='[COLOR lime]Ja/Yes[/COLOR]',nolabel ='[COLOR red]Nee/No[/COLOR]')#line:697
        if OOOOOO0O000000000 ==1 :#line:698
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
    IF you copy/paste 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
