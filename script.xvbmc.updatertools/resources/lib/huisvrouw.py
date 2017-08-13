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
    OO0OOO00OOO0O0O0O =6 #line:67
    OO0OOOO0OO000OOO0 =["MP3 Streams","Quasar","SportsDevil","Simple Downloader","Spotitube","SkinHelperService"]#line:68
    OOO0O0OOOO0O0OO0O =["special://profile/addon_data/plugin.audio.mp3streams/temp_dl","special://profile/addon_data/plugin.video.quasar/cache","special://profile/addon_data/plugin.video.SportsDevil/cache","special://profile/addon_data/script.module.simple.downloader","special://profile/addon_data/plugin.video.spotitube/cache","special://profile/addon_data/script.skin.helper.service/musicartcache"]#line:74
    O0O000000O00OO00O =[]#line:76
    for OOOO0OOO00O0O00O0 in range (OO0OOO00OOO0O0O0O ):#line:78
        O0O000000O00OO00O .append (cacheEntry (OO0OOOO0OO000OOO0 [OOOO0OOO00O0O00O0 ],OOO0O0OOOO0O0OO0O [OOOO0OOO00O0O00O0 ]))#line:79
    return O0O000000O00OO00O #line:81
def clearCache ():#line:88
    if os .path .exists (cachePath )==True :#line:89
        for O000OOO00O0O00OO0 ,OO00OO00O0OO00OO0 ,O0O00O0O0O0O0000O in os .walk (cachePath ):#line:90
            O00O00OO00OOO0OOO =0 #line:91
            O00O00OO00OOO0OOO +=len (O0O00O0O0O0O0000O )#line:92
            if O00O00OO00OOO0OOO >0 :#line:93
                if dialog .yesno ("Delete Cache Files",str (O00O00OO00OOO0OOO )+' files found','Do you want to delete them?'):#line:95
                    for OO00OO000OO0OO0O0 in O0O00O0O0O0O0000O :#line:96
                        try :#line:97
                            if (OO00OO000OO0OO0O0 .endswith (".log")):continue #line:99
                            os .unlink (os .path .join (O000OOO00O0O00OO0 ,OO00OO000OO0OO0O0 ))#line:100
                        except :#line:101
                            pass #line:102
                    for OOO000OO00OOO0OOO in OO00OO00O0OO00OO0 :#line:103
                        try :#line:104
                            O00O0O00OOO0OO0OO =(os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:106
                            if not "archive_cache"in str (O00O0O00OOO0OO0OO ):#line:107
                                shutil .rmtree (os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:108
                        except :#line:109
                            pass #line:110
            else :#line:111
                pass #line:112
    if os .path .exists (tempPath )==True :#line:114
        for O000OOO00O0O00OO0 ,OO00OO00O0OO00OO0 ,O0O00O0O0O0O0000O in os .walk (tempPath ):#line:115
            O00O00OO00OOO0OOO =0 #line:116
            O00O00OO00OOO0OOO +=len (O0O00O0O0O0O0000O )#line:117
            if O00O00OO00OOO0OOO >0 :#line:118
                if dialog .yesno ("Delete Temp Files",str (O00O00OO00OOO0OOO )+' files found','Do you want to delete them?'):#line:120
                    for OO00OO000OO0OO0O0 in O0O00O0O0O0O0000O :#line:121
                        try :#line:122
                            if (OO00OO000OO0OO0O0 .endswith (".log")):continue #line:124
                            os .unlink (os .path .join (O000OOO00O0O00OO0 ,OO00OO000OO0OO0O0 ))#line:125
                        except :#line:126
                            pass #line:127
                    for OOO000OO00OOO0OOO in OO00OO00O0OO00OO0 :#line:128
                        try :#line:129
                            O00O0O00OOO0OO0OO =(os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:131
                            if not "archive_cache"in str (O00O0O00OOO0OO0OO ):#line:132
                                shutil .rmtree (os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:133
                        except :#line:134
                            pass #line:135
            else :#line:136
                pass #line:137
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:139
        OO000OO0OOO0O000O =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:140
        for O000OOO00O0O00OO0 ,OO00OO00O0OO00OO0 ,O0O00O0O0O0O0000O in os .walk (OO000OO0OOO0O000O ):#line:141
            O00O00OO00OOO0OOO =0 #line:142
            O00O00OO00OOO0OOO +=len (O0O00O0O0O0O0000O )#line:143
            if O00O00OO00OOO0OOO >0 :#line:144
                if dialog .yesno ("Delete ATV2 Cache Files",str (O00O00OO00OOO0OOO )+" files found in 'Other'",'Do you want to delete them?'):#line:146
                    for OO00OO000OO0OO0O0 in O0O00O0O0O0O0000O :#line:147
                        try :#line:149
                            if (OO00OO000OO0OO0O0 .endswith (".log")):continue #line:150
                            os .unlink (os .path .join (O000OOO00O0O00OO0 ,OO00OO000OO0OO0O0 ))#line:151
                        except :#line:152
                            pass #line:153
                    for OOO000OO00OOO0OOO in OO00OO00O0OO00OO0 :#line:154
                        try :#line:156
                            O00O0O00OOO0OO0OO =(os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:157
                            if not "archive_cache"in str (O00O0O00OOO0OO0OO ):#line:158
                                shutil .rmtree (os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:159
                        except :#line:160
                            pass #line:161
            else :#line:162
                pass #line:163
        O000O0O00000OO00O =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:165
        for O000OOO00O0O00OO0 ,OO00OO00O0OO00OO0 ,O0O00O0O0O0O0000O in os .walk (O000O0O00000OO00O ):#line:166
            O00O00OO00OOO0OOO =0 #line:167
            O00O00OO00OOO0OOO +=len (O0O00O0O0O0O0000O )#line:168
            if O00O00OO00OOO0OOO >0 :#line:169
                if dialog .yesno ("Delete ATV2 Cache Files",str (O00O00OO00OOO0OOO )+" files found in 'LocalAndRental'",'Do you want to delete them?'):#line:171
                    for OO00OO000OO0OO0O0 in O0O00O0O0O0O0000O :#line:172
                        try :#line:174
                            if (OO00OO000OO0OO0O0 .endswith (".log")):continue #line:175
                            os .unlink (os .path .join (O000OOO00O0O00OO0 ,OO00OO000OO0OO0O0 ))#line:176
                        except :#line:177
                            pass #line:178
                    for OOO000OO00OOO0OOO in OO00OO00O0OO00OO0 :#line:179
                        try :#line:181
                            O00O0O00OOO0OO0OO =(os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:182
                            if not "archive_cache"in str (O00O0O00OOO0OO0OO ):#line:183
                                shutil .rmtree (os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:184
                        except :#line:185
                            pass #line:186
            else :#line:187
                pass #line:188
    O00O0000O0O0O0OOO =setupCacheEntries ()#line:190
    for O0O00000000O00000 in O00O0000O0O0O0OOO :#line:191
        OO0O0000O000OO00O =xbmc .translatePath (O0O00000000O00000 .path )#line:192
        if os .path .exists (OO0O0000O000OO00O )==True :#line:193
            for O000OOO00O0O00OO0 ,OO00OO00O0OO00OO0 ,O0O00O0O0O0O0000O in os .walk (OO0O0000O000OO00O ):#line:194
                O00O00OO00OOO0OOO =0 #line:195
                O00O00OO00OOO0OOO +=len (O0O00O0O0O0O0000O )#line:196
                if O00O00OO00OOO0OOO >0 :#line:197
                    if dialog .yesno (MainTitle ,'%s cache files found'%(O0O00000000O00000 .name ),'Do you want to delete them?'):#line:200
                        for OO00OO000OO0OO0O0 in O0O00O0O0O0O0000O :#line:201
                            try :#line:203
                                if (OO00OO000OO0OO0O0 .endswith (".log")):continue #line:204
                                os .unlink (os .path .join (O000OOO00O0O00OO0 ,OO00OO000OO0OO0O0 ))#line:205
                            except :#line:206
                                pass #line:207
                        for OOO000OO00OOO0OOO in OO00OO00O0OO00OO0 :#line:208
                            try :#line:210
                                O00O0O00OOO0OO0OO =(os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:211
                                if not "archive_cache"in str (O00O0O00OOO0OO0OO ):#line:212
                                    shutil .rmtree (os .path .join (O000OOO00O0O00OO0 ,OOO000OO00OOO0OOO ))#line:213
                            except :#line:214
                                pass #line:215
                else :#line:216
                    pass #line:217
    dialog .ok (MainTitle ,'Done Clearing Cache files')#line:219
    xbmc .executebuiltin ("Container.Refresh")#line:220
def deleteThumbnails ():#line:227
    if os .path .exists (thumbnailPath )==True :#line:228
            if dialog .yesno ("Delete Thumbnails",'This option deletes all thumbnails','Are you sure you want to do this?'):#line:230
                for O0OOO0OOO0O0O000O ,O0O0O000O000O0O0O ,OO00000OOO0O0O00O in os .walk (thumbnailPath ):#line:231
                    OO0OO0OO00O0OO000 =0 #line:232
                    OO0OO0OO00O0OO000 +=len (OO00000OOO0O0O00O )#line:233
                    if OO0OO0OO00O0OO000 >0 :#line:234
                        for OOOOO00O00O0O0OO0 in OO00000OOO0O0O00O :#line:235
                            try :#line:236
                                os .unlink (os .path .join (O0OOO0OOO0O0O000O ,OOOOO00O00O0O0OO0 ))#line:237
                            except :#line:238
                                pass #line:239
    else :#line:240
        pass #line:241
    O00000O00OOO0O00O =os .path .join (databasePath ,"Textures13.db")#line:243
    try :#line:244
        os .unlink (O00000O00OOO0O00O )#line:245
    except OSError :#line:246
        try :#line:247
            OO0OOO000O0O0O00O =sqlite3 .connect (O00000O00OOO0O00O )#line:248
            OO000OOO0O000O000 =OO0OOO000O0O0O00O .cursor ()#line:249
            OO000OOO0O000O000 .execute ('DROP TABLE IF EXISTS path')#line:250
            OO000OOO0O000O000 .execute ('VACUUM')#line:251
            OO0OOO000O0O0O00O .commit ()#line:252
            OO000OOO0O000O000 .execute ('DROP TABLE IF EXISTS sizes')#line:253
            OO000OOO0O000O000 .execute ('VACUUM')#line:254
            OO0OOO000O0O0O00O .commit ()#line:255
            OO000OOO0O000O000 .execute ('DROP TABLE IF EXISTS texture')#line:256
            OO000OOO0O000O000 .execute ('VACUUM')#line:257
            OO0OOO000O0O0O00O .commit ()#line:258
            OO000OOO0O000O000 .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:260
            OO0OOO000O0O0O00O .commit ()#line:261
            OO000OOO0O000O000 .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:263
            OO0OOO000O0O0O00O .commit ()#line:264
            OO000OOO0O000O000 .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:266
            OO0OOO000O0O0O00O .commit ()#line:267
        except :#line:268
            pass #line:269
    dialog .ok (MainTitle ,'Please reboot your system to rebuild thumbnail folder...')#line:271
    xbmc .executebuiltin ("Container.Refresh")#line:272
def PiCCleaner ():#line:279
    OO000O000OO0OOOOO =platform ()#line:280
    log ("XvBMC_Platform: "+str (OO000O000OO0OOOOO ))#line:281
    if not OO000O000OO0OOOOO =='linux':#line:282
       dialog .ok (MainTitle +SubTitle ,subtitleNope ,nonlinux ,nonelecNL )#line:283
       log ("none Linux OS ie. Open-/LibreELEC")#line:284
    else :#line:285
        log ("linux os")#line:286
        if dialog .yesno (MainTitle +SubTitle ,'about to do some extreme CrapCleaner voodoo...','[I]this will take a few seconds to complete, be patient![/I]','[B]are you sure[COLOR white]?[/COLOR][/B]'):#line:287
            O0O00O0O0O0OOO00O ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/rpiecc.sh"#line:288
            os .system (O0O00O0O0O0OOO00O )#line:289
            dialog .ok (MainTitle +SubTitle ,'[B]RPi[/B] CrapCleaner finished!','','Press OK to reboot...')#line:290
            xbmc .executebuiltin ("Reboot")#line:291
def purgePackages ():#line:298
    OOOOOO0OO00OOO000 =xbmc .translatePath ('special://home/addons/packages')#line:299
    for OO00O0OO0O0O0000O ,OOOO0O0O0OOO000O0 ,OO00000OOO000OOO0 in os .walk (OOOOOO0OO00OOO000 ):#line:301
            OO0OO0000O0O000OO =0 #line:302
            OO0OO0000O0O000OO +=len (OO00000OOO000OOO0 )#line:303
    if dialog .yesno ("Delete Package Cache Files",'%d packages found.'%OO0OO0000O0O000OO ,'Delete Them?'):#line:304
        for OO00O0OO0O0O0000O ,OOOO0O0O0OOO000O0 ,OO00000OOO000OOO0 in os .walk (OOOOOO0OO00OOO000 ):#line:305
            OO0OO0000O0O000OO =0 #line:306
            OO0OO0000O0O000OO +=len (OO00000OOO000OOO0 )#line:307
            if OO0OO0000O0O000OO >0 :#line:308
                try :#line:309
                    for O0O00OO0OO0O0OO0O in OO00000OOO000OOO0 :#line:310
                        os .unlink (os .path .join (OO00O0OO0O0O0000O ,O0O00OO0OO0O0OO0O ))#line:311
                    for O0O0OOO0OOOOO0OO0 in OOOO0O0O0OOO000O0 :#line:312
                        shutil .rmtree (os .path .join (OO00O0OO0O0O0000O ,O0O0OOO0OOOOO0OO0 ))#line:313
                except :pass #line:314
                dialog .ok (MainTitle ,'Deleting Packages all done')#line:315
            else :#line:317
                dialog .ok (MainTitle ,'No Packages to Purge')#line:318
    xbmc .executebuiltin ("Container.Refresh")#line:320
def AddonsDatabaseRemoval ():#line:327
    OO0O0OO000OO0OO0O =os .listdir (databasePath )#line:328
    OOO0OO0000OO000OO =[]#line:329
    O000O00O0000O0OO0 =True #line:330
    if dialog .yesno ("[COLOR lime]"+MainTitle +"[/COLOR]",' ','[COLOR red]Are YOU Sure [B]?!?[/B][/COLOR]'):#line:338
        if int (kodiver )<=16.7 :#line:339
           try :#line:340
               for OO0O0O0OOO00O000O in OO0O0OO000OO0OO0O :#line:341
                   if re .findall ('Addons(\d+)\.db',OO0O0O0OOO00O000O ):#line:342
                       OOO0OO0000OO000OO .append (OO0O0O0OOO00O000O )#line:343
               for OO0O0O0OOO00O000O in OOO0OO0000OO000OO :#line:344
                   O0O0OOOOOO000OOOO =os .path .join (databasePath ,OO0O0O0OOO00O000O )#line:345
                   OOOOO0000O00O0000 =open (O0O0OOOOOO000OOOO ,'ab+')#line:346
                   try :#line:347
                       OOOOO0000O00O0000 .close ()#line:349
                       os .remove (OOOOO0000O00O0000 .name )#line:350
                   except :#line:351
                       O000O00O0000O0OO0 =False #line:352
               if O000O00O0000O0OO0 :#line:353
                   dialog .ok (MainTitle ,'Your system will [COLOR red]reboot[/COLOR] to rebuild addons.db...')#line:354
                   Common .killKodi #line:355
               else :#line:356
                   dialog .ok (MainTitle ,'Removal [COLOR red]failed![/COLOR]','try manual remove, see: [COLOR green]http://kodi.wiki/view/Database_version[/COLOR]')#line:357
           except :#line:358
               pass #line:359
        else :#line:360
           dialog .ok (MainTitle ,'This feature is not available in Kodi 17 Krypton','','[COLOR yellow]Thank you for using XvBMC Maintenance[/COLOR]')#line:361
def autocleanask ():#line:368
    O00OOOO000O0000O0 =xbmcgui .Dialog ().yesno (MainTitle ,'Select [COLOR green]YES[/COLOR] to delete your:','cache, crashlogs, packages & thumbnails all at once.','[I][COLOR white]Do you wish to continue?[/I][/COLOR]',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:370
    if O00OOOO000O0000O0 ==1 :#line:371
        autocleannow ()#line:372
def autocleannow ():#line:374
    O00OOOOO0OOOOO000 =True #line:375
    if os .path .exists (cachePath )==True :#line:377
        for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (cachePath ):#line:378
            O000OOOOOO00OOOO0 =0 #line:379
            O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:380
            if O000OOOOOO00OOOO0 >0 :#line:381
                    for OOO0O0OO00OO000OO in OO0O00OO0OOOO00OO :#line:382
                        try :#line:383
                            if (OOO0O0OO00OO000OO .endswith (".log")):continue #line:384
                            os .unlink (os .path .join (O0O0O000OOOOOOOOO ,OOO0O0OO00OO000OO ))#line:385
                        except :#line:386
                            pass #line:387
                    for OOO0000OOOO0OOOO0 in OOO000OO0O00O0OO0 :#line:388
                        try :#line:389
                            O00OO000000O0OO0O =(os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:390
                            if not "archive_cache"in str (O00OO000000O0OO0O ):#line:391
                                shutil .rmtree (os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:392
                        except :#line:393
                            pass #line:394
            else :pass #line:395
    if os .path .exists (tempPath )==True :#line:397
        for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (tempPath ):#line:398
            O000OOOOOO00OOOO0 =0 #line:399
            O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:400
            if O000OOOOOO00OOOO0 >0 :#line:401
                    for OOO0O0OO00OO000OO in OO0O00OO0OOOO00OO :#line:402
                        try :#line:403
                            if (OOO0O0OO00OO000OO .endswith (".log")):continue #line:404
                            os .unlink (os .path .join (O0O0O000OOOOOOOOO ,OOO0O0OO00OO000OO ))#line:405
                        except :#line:406
                            pass #line:407
                    for OOO0000OOOO0OOOO0 in OOO000OO0O00O0OO0 :#line:408
                        try :#line:409
                            O00OO000000O0OO0O =(os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:410
                            if not "archive_cache"in str (O00OO000000O0OO0O ):#line:411
                                shutil .rmtree (os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:412
                        except :#line:413
                            pass #line:414
            else :pass #line:415
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:417
        O000O0000O0O00OOO =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:418
        for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (O000O0000O0O00OOO ):#line:419
            O000OOOOOO00OOOO0 =0 #line:420
            O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:421
            if O000OOOOOO00OOOO0 >0 :#line:423
                    for OOO0O0OO00OO000OO in OO0O00OO0OOOO00OO :#line:424
                        try :#line:425
                            if (OOO0O0OO00OO000OO .endswith (".log")):continue #line:426
                            os .unlink (os .path .join (O0O0O000OOOOOOOOO ,OOO0O0OO00OO000OO ))#line:427
                        except :#line:428
                            pass #line:429
                    for OOO0000OOOO0OOOO0 in OOO000OO0O00O0OO0 :#line:430
                        try :#line:431
                            O00OO000000O0OO0O =(os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:432
                            if not "archive_cache"in str (O00OO000000O0OO0O ):#line:433
                                shutil .rmtree (os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:434
                        except :#line:435
                            pass #line:436
            else :pass #line:437
        O00OOO0OOOO0O00O0 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:439
        for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (O00OOO0OOOO0O00O0 ):#line:440
            O000OOOOOO00OOOO0 =0 #line:441
            O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:442
            if O000OOOOOO00OOOO0 >0 :#line:444
                    for OOO0O0OO00OO000OO in OO0O00OO0OOOO00OO :#line:445
                        try :#line:446
                            if (OOO0O0OO00OO000OO .endswith (".log")):continue #line:447
                            os .unlink (os .path .join (O0O0O000OOOOOOOOO ,OOO0O0OO00OO000OO ))#line:448
                        except :#line:449
                            pass #line:450
                    for OOO0000OOOO0OOOO0 in OOO000OO0O00O0OO0 :#line:451
                        try :#line:452
                            O00OO000000O0OO0O =(os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:453
                            if not "archive_cache"in str (O00OO000000O0OO0O ):#line:454
                                shutil .rmtree (os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:455
                        except :#line:456
                            pass #line:457
            else :pass #line:458
    O00OOOOO00OO0O000 =setupCacheEntries ()#line:460
    for OO000OO00O0OOO0O0 in O00OOOOO00OO0O000 :#line:461
        OOOOO0O00O000O0OO =xbmc .translatePath (OO000OO00O0OOO0O0 .path )#line:462
        if os .path .exists (OOOOO0O00O000O0OO )==True :#line:463
            for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (OOOOO0O00O000O0OO ):#line:464
                O000OOOOOO00OOOO0 =0 #line:465
                O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:466
                if O000OOOOOO00OOOO0 >0 :#line:467
                    for OOO0O0OO00OO000OO in OO0O00OO0OOOO00OO :#line:468
                        try :#line:469
                            if (OOO0O0OO00OO000OO .endswith (".log")):continue #line:470
                            os .unlink (os .path .join (O0O0O000OOOOOOOOO ,OOO0O0OO00OO000OO ))#line:471
                        except :#line:472
                            pass #line:473
                    for OOO0000OOOO0OOOO0 in OOO000OO0O00O0OO0 :#line:474
                        try :#line:475
                            O00OO000000O0OO0O =(os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:476
                            if not "archive_cache"in str (O00OO000000O0OO0O ):#line:477
                                shutil .rmtree (os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:478
                        except :#line:479
                            pass #line:480
                else :pass #line:481
    if os .path .exists (thumbnailPath )==True :#line:483
                for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (thumbnailPath ):#line:484
                    O000OOOOOO00OOOO0 =0 #line:485
                    O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:486
                    if O000OOOOOO00OOOO0 >0 :#line:487
                        for OOO0O0OO00OO000OO in OO0O00OO0OOOO00OO :#line:488
                            try :#line:489
                                os .unlink (os .path .join (O0O0O000OOOOOOOOO ,OOO0O0OO00OO000OO ))#line:490
                            except :#line:491
                                pass #line:492
    else :pass #line:493
    O00OOOOO0O00O0O0O =os .path .join (databasePath ,"Textures13.db")#line:495
    try :#line:496
        os .unlink (O00OOOOO0O00O0O0O )#line:497
    except :#line:498
        pass #line:499
    O00O0O0OOO0OOO0OO =xbmc .translatePath ('special://home/addons/packages')#line:501
    for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (O00O0O0OOO0OOO0OO ):#line:502
            O000OOOOOO00OOOO0 =0 #line:503
            O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:504
    for O0O0O000OOOOOOOOO ,OOO000OO0O00O0OO0 ,OO0O00OO0OOOO00OO in os .walk (O00O0O0OOO0OOO0OO ):#line:505
            O000OOOOOO00OOOO0 =0 #line:506
            O000OOOOOO00OOOO0 +=len (OO0O00OO0OOOO00OO )#line:507
            if O000OOOOOO00OOOO0 >0 :#line:508
                try :#line:509
                    for OOO0O0OO00OO000OO in OO0O00OO0OOOO00OO :#line:510
                        os .unlink (os .path .join (O0O0O000OOOOOOOOO ,OOO0O0OO00OO000OO ))#line:511
                    for OOO0000OOOO0OOOO0 in OOO000OO0O00O0OO0 :#line:512
                        shutil .rmtree (os .path .join (O0O0O000OOOOOOOOO ,OOO0000OOOO0OOOO0 ))#line:513
                except :#line:514
                    pass #line:515
    if O00OOOOO0OOOOO000 ==True :#line:517
        AutoCrash ()#line:519
    else :#line:520
        xbmc .log (str (O00OOOOO0OOOOO000 ))#line:522
    O000OOO00000O00O0 =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR white][B]A[/B]uto [B]C[/B]lean finished:[/COLOR]','[I]cache, crashlogs, packages & thumbnails are removed.[/I]','Reboot your device now to finish the process?',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:524
    if O000OOO00000O00O0 ==1 :#line:525
         Common .killKodi ()#line:526
def AutoCrash ():#line:528
    O0O0OO0000OO0O0O0 =xbmc .translatePath ('special://home')#line:530
    O0OO000O0O00O0OOO =os .path .join (xbmc .translatePath ('special://home'),'cache')#line:531
    O000OO0O0OO0O0OO0 =os .path .join (xbmc .translatePath ('special://home'),'temp')#line:532
    if os .path .exists (O0O0OO0000OO0O0O0 )==True :#line:534
        OO0OOOO000000OO0O =Windows #line:535
        import glob as O000O0O00O00O0OOO #line:536
        for OOO00O0000OOO00O0 in O000O0O00O00O0OOO .glob (os .path .join (OO0OOOO000000OO0O ,'*.dmp')):#line:537
            OOO0OOOOOOOO0OO00 =OOO00O0000OOO00O0 #line:538
            log (OOO00O0000OOO00O0 )#line:539
            os .remove (OOO00O0000OOO00O0 )#line:540
        for OOO00O0000OOO00O0 in O000O0O00O00O0OOO .glob (os .path .join (OO0OOOO000000OO0O ,'*.txt')):#line:542
            OOO0OOOOOOOO0OO00 =OOO00O0000OOO00O0 #line:543
            log (OOO00O0000OOO00O0 )#line:544
            os .remove (OOO00O0000OOO00O0 )#line:545
    if os .path .exists (O0OO000O0O00O0OOO )==True :#line:547
        OO0OOOO000000OO0O =O0OO000O0O00O0OOO #line:548
        import glob as O000O0O00O00O0OOO #line:549
        for OOO00O0000OOO00O0 in O000O0O00O00O0OOO .glob (os .path .join (OO0OOOO000000OO0O ,'*.dmp')):#line:550
            OOO0OOOOOOOO0OO00 =OOO00O0000OOO00O0 #line:551
            log (OOO00O0000OOO00O0 )#line:552
            os .remove (OOO00O0000OOO00O0 )#line:553
        for OOO00O0000OOO00O0 in O000O0O00O00O0OOO .glob (os .path .join (OO0OOOO000000OO0O ,'*.txt')):#line:555
            OOO0OOOOOOOO0OO00 =OOO00O0000OOO00O0 #line:556
            log (OOO00O0000OOO00O0 )#line:557
            os .remove (OOO00O0000OOO00O0 )#line:558
    if os .path .exists (O000OO0O0OO0O0OO0 )==True :#line:560
        OO0OOOO000000OO0O =O000OO0O0OO0O0OO0 #line:561
        import glob as O000O0O00O00O0OOO #line:562
        for OOO00O0000OOO00O0 in O000O0O00O00O0OOO .glob (os .path .join (OO0OOOO000000OO0O ,'*.dmp')):#line:563
            OOO0OOOOOOOO0OO00 =OOO00O0000OOO00O0 #line:564
            log (OOO00O0000OOO00O0 )#line:565
            os .remove (OOO00O0000OOO00O0 )#line:566
        for OOO00O0000OOO00O0 in O000O0O00O00O0OOO .glob (os .path .join (OO0OOOO000000OO0O ,'*.txt')):#line:568
            OOO0OOOOOOOO0OO00 =OOO00O0000OOO00O0 #line:569
            log (OOO00O0000OOO00O0 )#line:570
            os .remove (OOO00O0000OOO00O0 )#line:571
def Fix_Special (url ):#line:578
    O00OOOOOO0OOO00OO =xbmc .translatePath ('special://home')#line:579
    dp .create (MainTitle ,"Renaming paths...",'','Please Wait')#line:580
    for OOOOO0O0O000O0O0O ,O0OOO00O0OO00000O ,OOOO00O0OOOOOOOOO in os .walk (O00OOOOOO0OOO00OO ):#line:581
        for OO000O0O0O00OO0O0 in OOOO00O0OOOOOOOOO :#line:582
            if OO000O0O0O00OO0O0 .endswith (".xml"):#line:583
                 dp .update (0 ,"Fixing","[COLOR green]"+OO000O0O0O00OO0O0 +"[/COLOR]","Please wait.....")#line:584
                 O0OO0O0000O00OOO0 =open ((os .path .join (OOOOO0O0O000O0O0O ,OO000O0O0O00OO0O0 ))).read ()#line:585
                 O000O000O00O0OO0O =O0OO0O0000O00OOO0 .replace (O00OOOOOO0OOO00OO ,'special://home/')#line:586
                 OO0OO00O0O000OO0O =open ((os .path .join (OOOOO0O0O000O0O0O ,OO000O0O0O00OO0O0 )),mode ='w')#line:587
                 OO0OO00O0O000OO0O .write (str (O000O000O00O0OO0O ))#line:588
                 OO0OO00O0O000OO0O .close ()#line:589
    dialog .ok (MainTitle ,'All physical (home) paths have been converted to special','To complete this process Kodi will force close now!')#line:591
    Common .killKodi ()#line:592
def xvbmcLog ():#line:599
    OO000O000000OO00O =xbmc .translatePath ('special://logpath/kodi.log')#line:600
    O0O00OO00OOOOO0O0 =xbmc .translatePath ('special://logpath/spmc.log')#line:601
    O0OO00O0OO0OOOOO0 =xbmc .translatePath ('special://logpath/spmc.log')#line:602
    O00OO0000OOO000OO =xbmc .translatePath ('special://logpath/kodi.old.log')#line:603
    O0O0000OOOO00O00O =xbmc .translatePath ('special://logpath/spmc.old.log')#line:604
    OOO0OOOOOOOO0O00O =xbmc .translatePath ('special://logpath/kodi.old.log')#line:605
    if os .path .exists (O0O00OO00OOOOO0O0 ):#line:607
        if os .path .exists (O0O00OO00OOOOO0O0 )and os .path .exists (O0O0000OOOO00O00O ):#line:608
            OO0OOO00O00O0000O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:609
            if OO0OOO00O00O0000O ==0 :#line:610
                O0O00O0OO0OOO0O00 =open (O0O00OO00OOOOO0O0 ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:611
                Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:612
            else :#line:613
                O0O00O0OO0OOO0O00 =open (O0O0000OOOO00O00O ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:614
                Common .TextBoxes ("%s - spmc.old.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:615
        else :#line:616
            O0O00O0OO0OOO0O00 =open (O0O00OO00OOOOO0O0 ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:617
            Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:618
    if os .path .exists (OO000O000000OO00O ):#line:620
        if os .path .exists (OO000O000000OO00O )and os .path .exists (O00OO0000OOO000OO ):#line:621
            OO0OOO00O00O0000O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:622
            if OO0OOO00O00O0000O ==0 :#line:623
                O0O00O0OO0OOO0O00 =open (OO000O000000OO00O ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:624
                Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:625
            else :#line:626
                O0O00O0OO0OOO0O00 =open (O00OO0000OOO000OO ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:627
                Common .TextBoxes ("%s - kodi.old.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:628
        else :#line:629
            O0O00O0OO0OOO0O00 =open (OO000O000000OO00O ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:630
            Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:631
    if os .path .exists (O0OO00O0OO0OOOOO0 ):#line:633
        if os .path .exists (O0OO00O0OO0OOOOO0 )and os .path .exists (OOO0OOOOOOOO0O00O ):#line:634
            OO0OOO00O00O0000O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:635
            if OO0OOO00O00O0000O ==0 :#line:636
                O0O00O0OO0OOO0O00 =open (O0OO00O0OO0OOOOO0 ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:637
                Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:638
            else :#line:639
                O0O00O0OO0OOO0O00 =open (OOO0OOOOOOOO0O00O ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:640
                Common .TextBoxes ("%s - dbmc.old.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:641
        else :#line:642
            O0O00O0OO0OOO0O00 =open (O0OO00O0OO0OOOOO0 ,mode ='r');O000O0000O0OO0OO0 =O0O00O0OO0OOO0O00 .read ();O0O00O0OO0OOO0O00 .close ()#line:643
            Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O000O0000O0OO0OO0 +"[/COLOR]")#line:644
    if os .path .isfile (OO000O000000OO00O )or os .path .isfile (O0O00OO00OOOOO0O0 )or os .path .isfile (O0OO00O0OO0OOOOO0 ):#line:646
        return True #line:647
    else :#line:648
        dialog .ok (MainTitle ,'Sorry, No log file was found.','','[COLOR yellow]Sorry, er was geen log file gevonden.[/COLOR]')#line:649
if Common .get_kversion ()>16.5 :#line:656
    try :from sqlite3 import dbapi2 as db_lib #line:657
    except :from pysqlite2 import dbapi2 as db_lib #line:658
    db_dir =xbmc .translatePath ("special://profile/Database")#line:660
    db_path =os .path .join (db_dir ,'Addons27.db')#line:661
    conn =db_lib .connect (db_path )#line:662
    conn .text_factory =str #line:663
def AddonsEnable ():#line:665
    if Common .get_kversion ()>16.5 :#line:666
        OO000000O00000000 =sqlite3 .connect (xbmc .translatePath ("special://database/Addons27.db"))#line:667
        O000000OOO0O0O0O0 =OO000000O00000000 .cursor ()#line:668
        O000000OOO0O0O0O0 .execute ("UPDATE installed SET enabled = 1 WHERE addonID NOT LIKE '%audiodecoder.%' AND addonID NOT LIKE '%inputstream.%' AND addonID NOT LIKE '%pvr.%' AND addonID NOT LIKE '%screensaver.%' AND addonID NOT LIKE '%visualization.%';")#line:669
        OO000000O00000000 .commit ()#line:670
        OO000000O00000000 .close ()#line:671
        xbmc .executebuiltin ('UpdateLocalAddons()')#line:672
        xbmc .executebuiltin ('UpdateAddonRepos()')#line:673
        O00OOO0000OOOO00O =xbmcgui .Dialog ().yesno (MainTitle +' : add-ons [B]enabled[/B]','[COLOR=green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete (\'yes\' is force close)','[B]Herstart[/B] Kodi ter afronding (ja is \'force close\')',yeslabel ='[COLOR lime]Ja/Yes[/COLOR]',nolabel ='[COLOR red]Nee/No[/COLOR]')#line:674
        if O00OOO0000OOOO00O ==1 :#line:675
            os ._exit (1 )#line:676
        else :pass #line:677
    else :pass #line:678
def EnableRTMP ():#line:680
        try :addon_able .set_enabled ("inputstream.adaptive")#line:681
        except :pass #line:682
        time .sleep (0.5 )#line:683
        try :addon_able .set_enabled ("inputstream.rtmp")#line:684
        except :pass #line:685
        time .sleep (0.5 )#line:686
        xbmc .executebuiltin ('XBMC.UpdateLocalAddons()')#line:687
        dialog .ok ("Operation Complete!",'Live Streaming has been Enabled!','Brought To You By %s '%MainTitle )#line:689
"""
    IF you copy/paste 'huisvrouw.py' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""