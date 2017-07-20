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
    OOOO0OO0OO0OOO000 =6 #line:67
    O00O0000OO0OOO0O0 =["MP3 Streams","Quasar","SportsDevil","Simple Downloader","Spotitube","SkinHelperService"]#line:68
    O00000OOO0O0OOOOO =["special://profile/addon_data/plugin.audio.mp3streams/temp_dl","special://profile/addon_data/plugin.video.quasar/cache","special://profile/addon_data/plugin.video.SportsDevil/cache","special://profile/addon_data/script.module.simple.downloader","special://profile/addon_data/plugin.video.spotitube/cache","special://profile/addon_data/script.skin.helper.service/musicartcache"]#line:74
    OO00OOOO0OOO0O000 =[]#line:76
    for OOO00OO00OO0OOO0O in range (OOOO0OO0OO0OOO000 ):#line:78
        OO00OOOO0OOO0O000 .append (cacheEntry (O00O0000OO0OOO0O0 [OOO00OO00OO0OOO0O ],O00000OOO0O0OOOOO [OOO00OO00OO0OOO0O ]))#line:79
    return OO00OOOO0OOO0O000 #line:81
def clearCache ():#line:88
    if os .path .exists (cachePath )==True :#line:89
        for O0O000000O00O000O ,O0OO000OO0O0O0O0O ,OO0000O0O000O0OO0 in os .walk (cachePath ):#line:90
            O0OO00OO000O0O000 =0 #line:91
            O0OO00OO000O0O000 +=len (OO0000O0O000O0OO0 )#line:92
            if O0OO00OO000O0O000 >0 :#line:93
                if dialog .yesno ("Delete Cache Files",str (O0OO00OO000O0O000 )+' files found','Do you want to delete them?'):#line:95
                    for OOO0000O000OO0000 in OO0000O0O000O0OO0 :#line:96
                        try :#line:97
                            if (OOO0000O000OO0000 .endswith (".log")):continue #line:99
                            os .unlink (os .path .join (O0O000000O00O000O ,OOO0000O000OO0000 ))#line:100
                        except :#line:101
                            pass #line:102
                    for O00OOO00O00OO00O0 in O0OO000OO0O0O0O0O :#line:103
                        try :#line:104
                            OO000O0O00OO0O00O =(os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:106
                            if not "archive_cache"in str (OO000O0O00OO0O00O ):#line:107
                                shutil .rmtree (os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:108
                        except :#line:109
                            pass #line:110
            else :#line:111
                pass #line:112
    if os .path .exists (tempPath )==True :#line:114
        for O0O000000O00O000O ,O0OO000OO0O0O0O0O ,OO0000O0O000O0OO0 in os .walk (tempPath ):#line:115
            O0OO00OO000O0O000 =0 #line:116
            O0OO00OO000O0O000 +=len (OO0000O0O000O0OO0 )#line:117
            if O0OO00OO000O0O000 >0 :#line:118
                if dialog .yesno ("Delete Temp Files",str (O0OO00OO000O0O000 )+' files found','Do you want to delete them?'):#line:120
                    for OOO0000O000OO0000 in OO0000O0O000O0OO0 :#line:121
                        try :#line:122
                            if (OOO0000O000OO0000 .endswith (".log")):continue #line:124
                            os .unlink (os .path .join (O0O000000O00O000O ,OOO0000O000OO0000 ))#line:125
                        except :#line:126
                            pass #line:127
                    for O00OOO00O00OO00O0 in O0OO000OO0O0O0O0O :#line:128
                        try :#line:129
                            OO000O0O00OO0O00O =(os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:131
                            if not "archive_cache"in str (OO000O0O00OO0O00O ):#line:132
                                shutil .rmtree (os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:133
                        except :#line:134
                            pass #line:135
            else :#line:136
                pass #line:137
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:139
        O0000OOO0OO0O0OOO =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:140
        for O0O000000O00O000O ,O0OO000OO0O0O0O0O ,OO0000O0O000O0OO0 in os .walk (O0000OOO0OO0O0OOO ):#line:141
            O0OO00OO000O0O000 =0 #line:142
            O0OO00OO000O0O000 +=len (OO0000O0O000O0OO0 )#line:143
            if O0OO00OO000O0O000 >0 :#line:144
                if dialog .yesno ("Delete ATV2 Cache Files",str (O0OO00OO000O0O000 )+" files found in 'Other'",'Do you want to delete them?'):#line:146
                    for OOO0000O000OO0000 in OO0000O0O000O0OO0 :#line:147
                        try :#line:149
                            if (OOO0000O000OO0000 .endswith (".log")):continue #line:150
                            os .unlink (os .path .join (O0O000000O00O000O ,OOO0000O000OO0000 ))#line:151
                        except :#line:152
                            pass #line:153
                    for O00OOO00O00OO00O0 in O0OO000OO0O0O0O0O :#line:154
                        try :#line:156
                            OO000O0O00OO0O00O =(os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:157
                            if not "archive_cache"in str (OO000O0O00OO0O00O ):#line:158
                                shutil .rmtree (os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:159
                        except :#line:160
                            pass #line:161
            else :#line:162
                pass #line:163
        O000O0OO00O0O00O0 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:165
        for O0O000000O00O000O ,O0OO000OO0O0O0O0O ,OO0000O0O000O0OO0 in os .walk (O000O0OO00O0O00O0 ):#line:166
            O0OO00OO000O0O000 =0 #line:167
            O0OO00OO000O0O000 +=len (OO0000O0O000O0OO0 )#line:168
            if O0OO00OO000O0O000 >0 :#line:169
                if dialog .yesno ("Delete ATV2 Cache Files",str (O0OO00OO000O0O000 )+" files found in 'LocalAndRental'",'Do you want to delete them?'):#line:171
                    for OOO0000O000OO0000 in OO0000O0O000O0OO0 :#line:172
                        try :#line:174
                            if (OOO0000O000OO0000 .endswith (".log")):continue #line:175
                            os .unlink (os .path .join (O0O000000O00O000O ,OOO0000O000OO0000 ))#line:176
                        except :#line:177
                            pass #line:178
                    for O00OOO00O00OO00O0 in O0OO000OO0O0O0O0O :#line:179
                        try :#line:181
                            OO000O0O00OO0O00O =(os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:182
                            if not "archive_cache"in str (OO000O0O00OO0O00O ):#line:183
                                shutil .rmtree (os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:184
                        except :#line:185
                            pass #line:186
            else :#line:187
                pass #line:188
    O0O0OO0000000OOO0 =setupCacheEntries ()#line:190
    for O00000O0O00OO0000 in O0O0OO0000000OOO0 :#line:191
        OO0O000OO00O000OO =xbmc .translatePath (O00000O0O00OO0000 .path )#line:192
        if os .path .exists (OO0O000OO00O000OO )==True :#line:193
            for O0O000000O00O000O ,O0OO000OO0O0O0O0O ,OO0000O0O000O0OO0 in os .walk (OO0O000OO00O000OO ):#line:194
                O0OO00OO000O0O000 =0 #line:195
                O0OO00OO000O0O000 +=len (OO0000O0O000O0OO0 )#line:196
                if O0OO00OO000O0O000 >0 :#line:197
                    if dialog .yesno (MainTitle ,'%s cache files found'%(O00000O0O00OO0000 .name ),'Do you want to delete them?'):#line:200
                        for OOO0000O000OO0000 in OO0000O0O000O0OO0 :#line:201
                            try :#line:203
                                if (OOO0000O000OO0000 .endswith (".log")):continue #line:204
                                os .unlink (os .path .join (O0O000000O00O000O ,OOO0000O000OO0000 ))#line:205
                            except :#line:206
                                pass #line:207
                        for O00OOO00O00OO00O0 in O0OO000OO0O0O0O0O :#line:208
                            try :#line:210
                                OO000O0O00OO0O00O =(os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:211
                                if not "archive_cache"in str (OO000O0O00OO0O00O ):#line:212
                                    shutil .rmtree (os .path .join (O0O000000O00O000O ,O00OOO00O00OO00O0 ))#line:213
                            except :#line:214
                                pass #line:215
                else :#line:216
                    pass #line:217
    dialog .ok (MainTitle ,'Done Clearing Cache files')#line:219
    xbmc .executebuiltin ("Container.Refresh")#line:220
def deleteThumbnails ():#line:227
    if os .path .exists (thumbnailPath )==True :#line:228
            if dialog .yesno ("Delete Thumbnails",'This option deletes all thumbnails','Are you sure you want to do this?'):#line:230
                for OOO0OO0O000000O00 ,OOOOO00OO00O00O0O ,OO0O0OO0OOOO00O00 in os .walk (thumbnailPath ):#line:231
                    OOOO000OO0000O000 =0 #line:232
                    OOOO000OO0000O000 +=len (OO0O0OO0OOOO00O00 )#line:233
                    if OOOO000OO0000O000 >0 :#line:234
                        for OO0OOOOO0OOOO0OO0 in OO0O0OO0OOOO00O00 :#line:235
                            try :#line:236
                                os .unlink (os .path .join (OOO0OO0O000000O00 ,OO0OOOOO0OOOO0OO0 ))#line:237
                            except :#line:238
                                pass #line:239
    else :#line:240
        pass #line:241
    O0000OOO00OOOOO0O =os .path .join (databasePath ,"Textures13.db")#line:243
    try :#line:244
        os .unlink (O0000OOO00OOOOO0O )#line:245
    except OSError :#line:246
        try :#line:247
            O0OOO0O0000000OOO =sqlite3 .connect (O0000OOO00OOOOO0O )#line:248
            O0OO0O00OO0O0O0O0 =O0OOO0O0000000OOO .cursor ()#line:249
            O0OO0O00OO0O0O0O0 .execute ('DROP TABLE IF EXISTS path')#line:250
            O0OO0O00OO0O0O0O0 .execute ('VACUUM')#line:251
            O0OOO0O0000000OOO .commit ()#line:252
            O0OO0O00OO0O0O0O0 .execute ('DROP TABLE IF EXISTS sizes')#line:253
            O0OO0O00OO0O0O0O0 .execute ('VACUUM')#line:254
            O0OOO0O0000000OOO .commit ()#line:255
            O0OO0O00OO0O0O0O0 .execute ('DROP TABLE IF EXISTS texture')#line:256
            O0OO0O00OO0O0O0O0 .execute ('VACUUM')#line:257
            O0OOO0O0000000OOO .commit ()#line:258
            O0OO0O00OO0O0O0O0 .execute ("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")#line:260
            O0OOO0O0000000OOO .commit ()#line:261
            O0OO0O00OO0O0O0O0 .execute ("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")#line:263
            O0OOO0O0000000OOO .commit ()#line:264
            O0OO0O00OO0O0O0O0 .execute ("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")#line:266
            O0OOO0O0000000OOO .commit ()#line:267
        except :#line:268
            pass #line:269
    dialog .ok (MainTitle ,'Please reboot your system to rebuild thumbnail folder...')#line:271
    xbmc .executebuiltin ("Container.Refresh")#line:272
def PiCCleaner ():#line:279
    O0O0O0OO00OO0O000 =platform ()#line:280
    log ("XvBMC_Platform: "+str (O0O0O0OO00OO0O000 ))#line:281
    if not O0O0O0OO00OO0O000 =='linux':#line:282
       dialog .ok (MainTitle +SubTitle ,subtitleNope ,nonlinux ,nonelecNL )#line:283
       log ("none Linux OS ie. Open-/LibreELEC")#line:284
    else :#line:285
        log ("linux os")#line:286
        if dialog .yesno (MainTitle +SubTitle ,'about to do some extreme CrapCleaner voodoo...','[I]this will take a few seconds to complete, be patient![/I]','[B]are you sure[COLOR white]?[/COLOR][/B]'):#line:287
            OO0OO0O0000000O00 ="/bin/bash /storage/.kodi/addons/script.xvbmc.updatertools/resources/lib/sources/rpiecc.sh"#line:288
            os .system (OO0OO0O0000000O00 )#line:289
            dialog .ok (MainTitle +SubTitle ,'[B]RPi[/B] CrapCleaner finished!','','Press OK to reboot...')#line:290
            xbmc .executebuiltin ("Reboot")#line:291
def purgePackages ():#line:298
    O0O0000O0O0OO00OO =xbmc .translatePath ('special://home/addons/packages')#line:299
    for O00OOOOOOO0OOO0O0 ,O000O0O0O0O0O0O00 ,O00000O000OOOOOO0 in os .walk (O0O0000O0O0OO00OO ):#line:301
            O0OO000OOO00OO0OO =0 #line:302
            O0OO000OOO00OO0OO +=len (O00000O000OOOOOO0 )#line:303
    if dialog .yesno ("Delete Package Cache Files",'%d packages found.'%O0OO000OOO00OO0OO ,'Delete Them?'):#line:304
        for O00OOOOOOO0OOO0O0 ,O000O0O0O0O0O0O00 ,O00000O000OOOOOO0 in os .walk (O0O0000O0O0OO00OO ):#line:305
            O0OO000OOO00OO0OO =0 #line:306
            O0OO000OOO00OO0OO +=len (O00000O000OOOOOO0 )#line:307
            if O0OO000OOO00OO0OO >0 :#line:308
                try :#line:309
                    for OOOO0OO00OO000OO0 in O00000O000OOOOOO0 :#line:310
                        os .unlink (os .path .join (O00OOOOOOO0OOO0O0 ,OOOO0OO00OO000OO0 ))#line:311
                    for OOO0O00OO0OO0O000 in O000O0O0O0O0O0O00 :#line:312
                        shutil .rmtree (os .path .join (O00OOOOOOO0OOO0O0 ,OOO0O00OO0OO0O000 ))#line:313
                except :pass #line:314
                dialog .ok (MainTitle ,'Deleting Packages all done')#line:315
            else :#line:317
                dialog .ok (MainTitle ,'No Packages to Purge')#line:318
    xbmc .executebuiltin ("Container.Refresh")#line:320
def AddonsDatabaseRemoval ():#line:327
    O000OO00O0OOOOO0O =os .listdir (databasePath )#line:328
    OOO00O0O0OO00OOO0 =[]#line:329
    O0O00O0O0O0O0OOOO =True #line:330
    if dialog .yesno ("[COLOR lime]"+MainTitle +"[/COLOR]",' ','[COLOR red]Are YOU Sure [B]?!?[/B][/COLOR]'):#line:338
        if int (kodiver )<=16.7 :#line:339
           try :#line:340
               for O00OO00O0O0O00OO0 in O000OO00O0OOOOO0O :#line:341
                   if re .findall ('Addons(\d+)\.db',O00OO00O0O0O00OO0 ):#line:342
                       OOO00O0O0OO00OOO0 .append (O00OO00O0O0O00OO0 )#line:343
               for O00OO00O0O0O00OO0 in OOO00O0O0OO00OOO0 :#line:344
                   O0O0O0000OO000OOO =os .path .join (databasePath ,O00OO00O0O0O00OO0 )#line:345
                   OOOO00O0OO000000O =open (O0O0O0000OO000OOO ,'ab+')#line:346
                   try :#line:347
                       OOOO00O0OO000000O .close ()#line:349
                       os .remove (OOOO00O0OO000000O .name )#line:350
                   except :#line:351
                       O0O00O0O0O0O0OOOO =False #line:352
               if O0O00O0O0O0O0OOOO :#line:353
                   dialog .ok (MainTitle ,'Your system will [COLOR red]reboot[/COLOR] to rebuild addons.db...')#line:354
                   Common .killKodi #line:355
               else :#line:356
                   dialog .ok (MainTitle ,'Removal [COLOR red]failed![/COLOR]','try manual remove, see: [COLOR green]http://kodi.wiki/view/Database_version[/COLOR]')#line:357
           except :#line:358
               pass #line:359
        else :#line:360
           dialog .ok (MainTitle ,'This feature is not available in Kodi 17 Krypton','','[COLOR yellow]Thank you for using XvBMC Maintenance[/COLOR]')#line:361
def autocleanask ():#line:368
	OOO00000000O0O0O0 =xbmcgui .Dialog ().yesno (MainTitle ,'Select [COLOR green]YES[/COLOR] to delete your:','cache, crashlogs, packages & thumbnails all at once.','[I][COLOR white]Do you wish to continue?[/I][/COLOR]',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:370
	if OOO00000000O0O0O0 ==1 :#line:371
		autocleannow ()#line:372
def autocleannow ():#line:374
    OOO0000O0O00OOO0O =True #line:375
    if os .path .exists (cachePath )==True :#line:377
        for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (cachePath ):#line:378
            O00O0O0OO0OOO00OO =0 #line:379
            O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:380
            if O00O0O0OO0OOO00OO >0 :#line:381
                    for OO0O0OO0OOO0000OO in OO0OO00OO00O000O0 :#line:382
                        try :#line:383
                            if (OO0O0OO0OOO0000OO .endswith (".log")):continue #line:384
                            os .unlink (os .path .join (OO00O00O0OO000O00 ,OO0O0OO0OOO0000OO ))#line:385
                        except :#line:386
                            pass #line:387
                    for OOOOOOOO00OO0OOOO in O0OOOO0OO00OOOO0O :#line:388
                        try :#line:389
                            OO0OO0O00O0OOOO00 =(os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:390
                            if not "archive_cache"in str (OO0OO0O00O0OOOO00 ):#line:391
                                shutil .rmtree (os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:392
                        except :#line:393
                            pass #line:394
            else :pass #line:395
    if os .path .exists (tempPath )==True :#line:397
        for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (tempPath ):#line:398
            O00O0O0OO0OOO00OO =0 #line:399
            O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:400
            if O00O0O0OO0OOO00OO >0 :#line:401
                    for OO0O0OO0OOO0000OO in OO0OO00OO00O000O0 :#line:402
                        try :#line:403
                            if (OO0O0OO0OOO0000OO .endswith (".log")):continue #line:404
                            os .unlink (os .path .join (OO00O00O0OO000O00 ,OO0O0OO0OOO0000OO ))#line:405
                        except :#line:406
                            pass #line:407
                    for OOOOOOOO00OO0OOOO in O0OOOO0OO00OOOO0O :#line:408
                        try :#line:409
                            OO0OO0O00O0OOOO00 =(os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:410
                            if not "archive_cache"in str (OO0OO0O00O0OOOO00 ):#line:411
                                shutil .rmtree (os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:412
                        except :#line:413
                            pass #line:414
            else :pass #line:415
    if xbmc .getCondVisibility ('system.platform.ATV2'):#line:417
        OO000O0O0OOO0OO00 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','Other')#line:418
        for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (OO000O0O0OOO0OO00 ):#line:419
            O00O0O0OO0OOO00OO =0 #line:420
            O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:421
            if O00O0O0OO0OOO00OO >0 :#line:423
                    for OO0O0OO0OOO0000OO in OO0OO00OO00O000O0 :#line:424
                        try :#line:425
                            if (OO0O0OO0OOO0000OO .endswith (".log")):continue #line:426
                            os .unlink (os .path .join (OO00O00O0OO000O00 ,OO0O0OO0OOO0000OO ))#line:427
                        except :#line:428
                            pass #line:429
                    for OOOOOOOO00OO0OOOO in O0OOOO0OO00OOOO0O :#line:430
                        try :#line:431
                            OO0OO0O00O0OOOO00 =(os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:432
                            if not "archive_cache"in str (OO0OO0O00O0OOOO00 ):#line:433
                                shutil .rmtree (os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:434
                        except :#line:435
                            pass #line:436
            else :pass #line:437
        O0O0OOOOOO0O00O00 =os .path .join ('/private/var/mobile/Library/Caches/AppleTV/Video/','LocalAndRental')#line:439
        for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (O0O0OOOOOO0O00O00 ):#line:440
            O00O0O0OO0OOO00OO =0 #line:441
            O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:442
            if O00O0O0OO0OOO00OO >0 :#line:444
                    for OO0O0OO0OOO0000OO in OO0OO00OO00O000O0 :#line:445
                        try :#line:446
                            if (OO0O0OO0OOO0000OO .endswith (".log")):continue #line:447
                            os .unlink (os .path .join (OO00O00O0OO000O00 ,OO0O0OO0OOO0000OO ))#line:448
                        except :#line:449
                            pass #line:450
                    for OOOOOOOO00OO0OOOO in O0OOOO0OO00OOOO0O :#line:451
                        try :#line:452
                            OO0OO0O00O0OOOO00 =(os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:453
                            if not "archive_cache"in str (OO0OO0O00O0OOOO00 ):#line:454
                                shutil .rmtree (os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:455
                        except :#line:456
                            pass #line:457
            else :pass #line:458
    OO0O000O00OOO0OO0 =setupCacheEntries ()#line:460
    for OOOOO0OOO0O0OO00O in OO0O000O00OOO0OO0 :#line:461
        OO0O0O0000OO00000 =xbmc .translatePath (OOOOO0OOO0O0OO00O .path )#line:462
        if os .path .exists (OO0O0O0000OO00000 )==True :#line:463
            for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (OO0O0O0000OO00000 ):#line:464
                O00O0O0OO0OOO00OO =0 #line:465
                O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:466
                if O00O0O0OO0OOO00OO >0 :#line:467
                    for OO0O0OO0OOO0000OO in OO0OO00OO00O000O0 :#line:468
                        try :#line:469
                            if (OO0O0OO0OOO0000OO .endswith (".log")):continue #line:470
                            os .unlink (os .path .join (OO00O00O0OO000O00 ,OO0O0OO0OOO0000OO ))#line:471
                        except :#line:472
                            pass #line:473
                    for OOOOOOOO00OO0OOOO in O0OOOO0OO00OOOO0O :#line:474
                        try :#line:475
                            OO0OO0O00O0OOOO00 =(os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:476
                            if not "archive_cache"in str (OO0OO0O00O0OOOO00 ):#line:477
                                shutil .rmtree (os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:478
                        except :#line:479
                            pass #line:480
                else :pass #line:481
    if os .path .exists (thumbnailPath )==True :#line:483
                for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (thumbnailPath ):#line:484
                    O00O0O0OO0OOO00OO =0 #line:485
                    O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:486
                    if O00O0O0OO0OOO00OO >0 :#line:487
                        for OO0O0OO0OOO0000OO in OO0OO00OO00O000O0 :#line:488
                            try :#line:489
                                os .unlink (os .path .join (OO00O00O0OO000O00 ,OO0O0OO0OOO0000OO ))#line:490
                            except :#line:491
                                pass #line:492
    else :pass #line:493
    OO0O000O0O0000O0O =os .path .join (databasePath ,"Textures13.db")#line:495
    try :#line:496
        os .unlink (OO0O000O0O0000O0O )#line:497
    except :#line:498
        pass #line:499
    OOOOOO0OOO0OOO00O =xbmc .translatePath ('special://home/addons/packages')#line:501
    for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (OOOOOO0OOO0OOO00O ):#line:502
            O00O0O0OO0OOO00OO =0 #line:503
            O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:504
    for OO00O00O0OO000O00 ,O0OOOO0OO00OOOO0O ,OO0OO00OO00O000O0 in os .walk (OOOOOO0OOO0OOO00O ):#line:505
            O00O0O0OO0OOO00OO =0 #line:506
            O00O0O0OO0OOO00OO +=len (OO0OO00OO00O000O0 )#line:507
            if O00O0O0OO0OOO00OO >0 :#line:508
                try :#line:509
                    for OO0O0OO0OOO0000OO in OO0OO00OO00O000O0 :#line:510
                        os .unlink (os .path .join (OO00O00O0OO000O00 ,OO0O0OO0OOO0000OO ))#line:511
                    for OOOOOOOO00OO0OOOO in O0OOOO0OO00OOOO0O :#line:512
                        shutil .rmtree (os .path .join (OO00O00O0OO000O00 ,OOOOOOOO00OO0OOOO ))#line:513
                except :#line:514
                    pass #line:515
    if OOO0000O0O00OOO0O ==True :#line:517
        AutoCrash ()#line:519
    else :#line:520
        xbmc .log (str (OOO0000O0O00OOO0O ))#line:522
    O0OOOOO0000O0O00O =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR white][B]A[/B]uto [B]C[/B]lean finished:[/COLOR]','[I]cache, crashlogs, packages & thumbnails are removed.[/I]','Reboot your device now to finish the process?',yeslabel ='[B][COLOR green]YES[/COLOR][/B]',nolabel ='[B][COLOR red]NO[/COLOR][/B]')#line:524
    if O0OOOOO0000O0O00O ==1 :#line:525
         Common .killKodi ()#line:526
def AutoCrash ():#line:528
	OO0O000OO0OOOO00O =xbmc .translatePath ('special://home')#line:530
	OOO0000OO000OOO0O =os .path .join (xbmc .translatePath ('special://home'),'cache')#line:531
	O00O0O000O000OO0O =os .path .join (xbmc .translatePath ('special://home'),'temp')#line:532
	if os .path .exists (OO0O000OO0OOOO00O )==True :#line:534
		OO0000OO0OOOO000O =Windows #line:535
		import glob as OO0OOO00O0OOOOOO0 #line:536
		for OO00O0OO000OOO0O0 in OO0OOO00O0OOOOOO0 .glob (os .path .join (OO0000OO0OOOO000O ,'*.dmp')):#line:537
			OOO000O000000OO0O =OO00O0OO000OOO0O0 #line:538
			log (OO00O0OO000OOO0O0 )#line:539
			os .remove (OO00O0OO000OOO0O0 )#line:540
		for OO00O0OO000OOO0O0 in OO0OOO00O0OOOOOO0 .glob (os .path .join (OO0000OO0OOOO000O ,'*.txt')):#line:542
			OOO000O000000OO0O =OO00O0OO000OOO0O0 #line:543
			log (OO00O0OO000OOO0O0 )#line:544
			os .remove (OO00O0OO000OOO0O0 )#line:545
	if os .path .exists (OOO0000OO000OOO0O )==True :#line:547
		OO0000OO0OOOO000O =OOO0000OO000OOO0O #line:548
		import glob as OO0OOO00O0OOOOOO0 #line:549
		for OO00O0OO000OOO0O0 in OO0OOO00O0OOOOOO0 .glob (os .path .join (OO0000OO0OOOO000O ,'*.dmp')):#line:550
			OOO000O000000OO0O =OO00O0OO000OOO0O0 #line:551
			log (OO00O0OO000OOO0O0 )#line:552
			os .remove (OO00O0OO000OOO0O0 )#line:553
		for OO00O0OO000OOO0O0 in OO0OOO00O0OOOOOO0 .glob (os .path .join (OO0000OO0OOOO000O ,'*.txt')):#line:555
			OOO000O000000OO0O =OO00O0OO000OOO0O0 #line:556
			log (OO00O0OO000OOO0O0 )#line:557
			os .remove (OO00O0OO000OOO0O0 )#line:558
	if os .path .exists (O00O0O000O000OO0O )==True :#line:560
		OO0000OO0OOOO000O =O00O0O000O000OO0O #line:561
		import glob as OO0OOO00O0OOOOOO0 #line:562
		for OO00O0OO000OOO0O0 in OO0OOO00O0OOOOOO0 .glob (os .path .join (OO0000OO0OOOO000O ,'*.dmp')):#line:563
			OOO000O000000OO0O =OO00O0OO000OOO0O0 #line:564
			log (OO00O0OO000OOO0O0 )#line:565
			os .remove (OO00O0OO000OOO0O0 )#line:566
		for OO00O0OO000OOO0O0 in OO0OOO00O0OOOOOO0 .glob (os .path .join (OO0000OO0OOOO000O ,'*.txt')):#line:568
			OOO000O000000OO0O =OO00O0OO000OOO0O0 #line:569
			log (OO00O0OO000OOO0O0 )#line:570
			os .remove (OO00O0OO000OOO0O0 )#line:571
def Fix_Special (url ):#line:578
    OOO0OO00000O0OO00 =xbmc .translatePath ('special://home')#line:579
    dp .create (MainTitle ,"Renaming paths...",'','Please Wait')#line:580
    for O0OO000O0000O0OO0 ,O0OO0O0OOO000O000 ,O000OOOOO00000OOO in os .walk (OOO0OO00000O0OO00 ):#line:581
        for O0O00O0000O0000OO in O000OOOOO00000OOO :#line:582
            if O0O00O0000O0000OO .endswith (".xml"):#line:583
                 dp .update (0 ,"Fixing","[COLOR green]"+O0O00O0000O0000OO +"[/COLOR]","Please wait.....")#line:584
                 OO000O00O0OO0O00O =open ((os .path .join (O0OO000O0000O0OO0 ,O0O00O0000O0000OO ))).read ()#line:585
                 OOOOOO0O000O000O0 =OO000O00O0OO0O00O .replace (OOO0OO00000O0OO00 ,'special://home/')#line:586
                 OOOOOO0000O0000O0 =open ((os .path .join (O0OO000O0000O0OO0 ,O0O00O0000O0000OO )),mode ='w')#line:587
                 OOOOOO0000O0000O0 .write (str (OOOOOO0O000O000O0 ))#line:588
                 OOOOOO0000O0000O0 .close ()#line:589
    dialog .ok (MainTitle ,'All physical (home) paths have been converted to special','To complete this process Kodi will force close now!')#line:591
    Common .killKodi ()#line:592
def xvbmcLog ():#line:599
	O0O0O0OO0O00OO000 =xbmc .translatePath ('special://logpath/kodi.log')#line:600
	OOO0OOOOO00OOOOOO =xbmc .translatePath ('special://logpath/spmc.log')#line:601
	O0O000O00O0OO00OO =xbmc .translatePath ('special://logpath/spmc.log')#line:602
	OO000O000O000OO0O =xbmc .translatePath ('special://logpath/kodi.old.log')#line:603
	O00OO0O000OO0OO00 =xbmc .translatePath ('special://logpath/spmc.old.log')#line:604
	OOO0OO0O00OO0O0O0 =xbmc .translatePath ('special://logpath/kodi.old.log')#line:605
	if os .path .exists (OOO0OOOOO00OOOOOO ):#line:607
		if os .path .exists (OOO0OOOOO00OOOOOO )and os .path .exists (O00OO0O000OO0OO00 ):#line:608
			OOOOOOOOO0O0O0OOO =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:609
			if OOOOOOOOO0O0O0OOO ==0 :#line:610
				OOO0000OO00000OO0 =open (OOO0OOOOO00OOOOOO ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:611
				Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:612
			else :#line:613
				OOO0000OO00000OO0 =open (O00OO0O000OO0OO00 ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:614
				Common .TextBoxes ("%s - spmc.old.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:615
		else :#line:616
			OOO0000OO00000OO0 =open (OOO0OOOOO00OOOOOO ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:617
			Common .TextBoxes ("%s - spmc.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:618
	if os .path .exists (O0O0O0OO0O00OO000 ):#line:620
		if os .path .exists (O0O0O0OO0O00OO000 )and os .path .exists (OO000O000O000OO0O ):#line:621
			OOOOOOOOO0O0O0OOO =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:622
			if OOOOOOOOO0O0O0OOO ==0 :#line:623
				OOO0000OO00000OO0 =open (O0O0O0OO0O00OO000 ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:624
				Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:625
			else :#line:626
				OOO0000OO00000OO0 =open (OO000O000O000OO0O ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:627
				Common .TextBoxes ("%s - kodi.old.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:628
		else :#line:629
			OOO0000OO00000OO0 =open (O0O0O0OO0O00OO000 ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:630
			Common .TextBoxes ("%s - kodi.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:631
	if os .path .exists (O0O000O00O0OO00OO ):#line:633
		if os .path .exists (O0O000O00O0OO00OO )and os .path .exists (OOO0OO0O00OO0O0O0 ):#line:634
			OOOOOOOOO0O0O0OOO =xbmcgui .Dialog ().yesno (MainTitle ,'[COLOR lime]Current-[/COLOR] & [COLOR red]old[/COLOR] [B]Log[/B]\'s detected on your system.','Which \'log file\' would you like to view?','NL: wilt u de oude/vorige- OF actuele log file bekijken?',yeslabel ='old/oud',nolabel ='current/recent')#line:635
			if OOOOOOOOO0O0O0OOO ==0 :#line:636
				OOO0000OO00000OO0 =open (O0O000O00O0OO00OO ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:637
				Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:638
			else :#line:639
				OOO0000OO00000OO0 =open (OOO0OO0O00OO0O0O0 ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:640
				Common .TextBoxes ("%s - dbmc.old.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:641
		else :#line:642
			OOO0000OO00000OO0 =open (O0O000O00O0OO00OO ,mode ='r');O00000O0000OOO0OO =OOO0000OO00000OO0 .read ();OOO0000OO00000OO0 .close ()#line:643
			Common .TextBoxes ("%s - dbmc.log"%"[COLOR white]"+O00000O0000OOO0OO +"[/COLOR]")#line:644
	if os .path .isfile (O0O0O0OO0O00OO000 )or os .path .isfile (OOO0OOOOO00OOOOOO )or os .path .isfile (O0O000O00O0OO00OO ):#line:646
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
        O000OOO0O00OOOO0O =sqlite3 .connect (xbmc .translatePath ("special://database/Addons27.db"))#line:667
        O0000O00O0000OOO0 =O000OOO0O00OOOO0O .cursor ()#line:668
        O0000O00O0000OOO0 .execute ("UPDATE installed SET enabled = 1 WHERE addonID NOT LIKE '%audiodecoder.%' AND addonID NOT LIKE '%inputstream.%' AND addonID NOT LIKE '%pvr.%' AND addonID NOT LIKE '%screensaver.%' AND addonID NOT LIKE '%visualization.%';")#line:669
        O000OOO0O00OOOO0O .commit ()#line:670
        O000OOO0O00OOOO0O .close ()#line:671
        xbmc .executebuiltin ('UpdateLocalAddons()')#line:672
        xbmc .executebuiltin ('UpdateAddonRepos()')#line:673
        O0OOO0000O0OOO0O0 =xbmcgui .Dialog ().yesno (MainTitle +' : add-ons [B]enabled[/B]','[COLOR=green][B]!!!  FINISHED  !!![/B][/COLOR]','[B]Reboot[/B] Kodi to complete (\'yes\' is force close)','[B]Herstart[/B] Kodi ter afronding (ja is \'force close\')',yeslabel ='[COLOR lime]Ja/Yes[/COLOR]',nolabel ='[COLOR red]Nee/No[/COLOR]')#line:674
        if O0OOO0000O0OOO0O0 ==1 :#line:675
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
		dialog .ok ("Operation Complete!",'Live Streaming has been Enabled!','    Brought To You By %s '%MainTitle )#line:690
"""
	IF you copy/paste 'huisvrouw.py' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""