#!/usr/bin/python
"""
    IF you copy/paste XvBMC's -common.py- please keep the credits -2- XvBMC-NL, Thx.
"""#line:6
import xbmc ,xbmcaddon ,xbmcgui ,xbmcplugin #line:25
import base64 ,os ,sys ,time #line:26
import re ,urllib ,urllib2 #line:27
AddonID ='script.xvbmc.updatertools'#line:33
ADDON =xbmcaddon .Addon (id =AddonID )#line:34
addonInfo =xbmcaddon .Addon ().getAddonInfo #line:35
dialog =xbmcgui .Dialog ()#line:38
HOME =xbmc .translatePath ('special://home/')#line:39
MainTitle ="XvBMC Nederland"#line:40
waarschuwing ='[COLOR=red][B]!!!  WARNING  !!![/B][/COLOR]'#line:42
readme ='if you\'re seeing this message read this first[B]:[/B]'#line:43
noservicepack ='Sorry the [B]S[/B]ervice[B]P[/B]ack update is [COLOR=red]outdated[/COLOR] at this moment'#line:44
notforked ='[COLOR dimgray](the newest XvBMC\'s [B]Pi[/B]-image is not forked, [B]yet[/B]...)[/COLOR]'#line:45
subtitleNope ="[COLOR=red][B]!!!  NOPE  !!![/B][/COLOR]"#line:47
nonlinux ="[US] you\'re running a \'none linux os\' (Open-/LibreELEC)"#line:48
nonelecNL ="[NL] dit is geen Raspberry Pi met Open-/LibreELEC \'OS\'"#line:49
base ='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'#line:51
basewiz ='aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9OT1hFTkdXSVpBUkQv'#line:52
bldversietxt =xbmc .translatePath (os .path .join ('special://home/userdata','versiebld.txt'))#line:53
bldversietxtwiz =xbmc .translatePath (os .path .join ('special://home/userdata','wizbld.txt'))#line:54
currentbldtxt =base64 .b64decode (base )+'update/bld/versiebuild.txt'#line:55
currentsptxt =base64 .b64decode (base )+'update/sp/servicepack.txt'#line:56
currentsptxtrpi =base64 .b64decode (base )+'update/sp/rpi-service.txt'#line:57
currentbldtxtwiz =base64 .b64decode (basewiz )+'wizbld.txt'#line:58
currentsptxtwiz =base64 .b64decode (basewiz )+'wizsp.txt'#line:59
repos ='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL1JFUE9zaXRvcnkvemlwcy9yZXBvc2l0b3J5Lnh2Ym1jLw=='#line:60
uwspversietxt =xbmc .translatePath (os .path .join ('special://home/userdata','versiesp.txt'))#line:61
uwspversietxtrpi =xbmc .translatePath (os .path .join ('special://home/userdata','rpi-service.txt'))#line:62
uwspversietxtwiz =xbmc .translatePath (os .path .join ('special://home/userdata','wizsp.txt'))#line:63
def killKodi ():#line:69
    O0O00OOOO0OO000O0 =platform ()#line:75
    log ("XvBMC_Platform: "+str (O0O00OOOO0OO000O0 ))#line:76
    try :os ._exit (1 )#line:77
    except :pass #line:78
    if O0O00OOOO0OO000O0 =='osx':#line:79
        log ("############   try osx force close  #################")#line:80
        try :os .system ('killall -9 XBMC')#line:81
        except :pass #line:82
        try :os .system ('killall -9 Kodi')#line:83
        except :pass #line:84
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:85
        try :xbmc .executebuiltin ("Reboot")#line:86
        except :pass #line:87
    elif O0O00OOOO0OO000O0 =='linux':#line:88
        log ("############   try linux force close  #################")#line:89
        try :os .system ('killall XBMC')#line:92
        except :pass #line:93
        try :os .system ('killall Kodi')#line:94
        except :pass #line:95
        try :os .system ('killall -9 xbmc.bin')#line:96
        except :pass #line:97
        try :os .system ('killall -9 kodi.bin')#line:98
        except :pass #line:99
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:100
        try :xbmc .executebuiltin ("Reboot")#line:101
        except :pass #line:102
    elif O0O00OOOO0OO000O0 =='android':#line:103
        log ("############   try android force close  #################")#line:104
        try :os .system ('adb shell am force-stop com.jesusboxmedia')#line:105
        except :pass #line:106
        try :os .system ('adb shell am force-stop com.perfectzoneproductions.jesusboxmedia')#line:107
        except :pass #line:108
        try :os .system ('adb shell am force-stop com.semperpax.spmc')#line:109
        except :pass #line:110
        try :os .system ('adb shell am force-stop com.semperpax.spmc16')#line:111
        except :pass #line:112
        try :os .system ('adb shell am force-stop com.spmc')#line:113
        except :pass #line:114
        try :os .system ('adb shell am force-stop com.spmc16')#line:115
        except :pass #line:116
        try :os .system ('adb shell am force-stop org.kodi')#line:117
        except :pass #line:118
        try :os .system ('adb shell am force-stop org.lodi.mobi')#line:119
        except :pass #line:120
        try :os .system ('adb shell am force-stop org.xbmc')#line:121
        except :pass #line:122
        try :os .system ('adb shell am force-stop org.xbmc.cemc')#line:123
        except :pass #line:124
        try :os .system ('adb shell am force-stop org.xbmc.cemc_pro')#line:125
        except :pass #line:126
        try :os .system ('adb shell am force-stop org.xbmc.kodi')#line:127
        except :pass #line:128
        try :os .system ('adb shell am force-stop org.xbmc.xbmc')#line:129
        except :pass #line:130
        try :os .system ('adb shell am force-stop uk.dbmc')#line:131
        except :pass #line:132
        try :os .system ('adb shell am force-stop uk.droidbox.dbmc')#line:133
        except :pass #line:134
        try :os .system ('adb shell kill com.perfectzoneproductions.jesusboxmedia')#line:135
        except :pass #line:136
        try :os .system ('adb shell kill com.semperpax')#line:137
        except :pass #line:138
        try :os .system ('adb shell kill com.semperpax.spmc16')#line:139
        except :pass #line:140
        try :os .system ('adb shell kill org.kodi')#line:141
        except :pass #line:142
        try :os .system ('adb shell kill org.lodi.mobi')#line:143
        except :pass #line:144
        try :os .system ('adb shell kill org.xbmc')#line:145
        except :pass #line:146
        try :os .system ('adb shell kill org.xbmc.cemc')#line:147
        except :pass #line:148
        try :os .system ('adb shell kill org.xbmc.cemc_pro')#line:149
        except :pass #line:150
        try :os .system ('adb shell kill org.xbmc.kodi')#line:151
        except :pass #line:152
        try :os .system ('adb shell kill org.xbmc.xbmc')#line:153
        except :pass #line:154
        try :os .system ('Process.killProcess(android.os.Process.com.semperpax.spmc16());')#line:155
        except :pass #line:156
        try :os .system ('Process.killProcess(android.os.Process.org.fire());')#line:157
        except :pass #line:158
        try :os .system ('Process.killProcess(android.os.Process.org.fire.guru());')#line:159
        except :pass #line:160
        try :os .system ('Process.killProcess(android.os.Process.org.fire.guruv());')#line:161
        except :pass #line:162
        try :os .system ('Process.killProcess(android.os.Process.org.kodi());')#line:163
        except :pass #line:164
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc());')#line:165
        except :pass #line:166
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc.kodi());')#line:167
        except :pass #line:168
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc.xbmc());')#line:169
        except :pass #line:170
        dialog .ok (waarschuwing ,'Your system has been detected as Android, you ','[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Either close using Task Manager (If unsure pull the plug).')#line:171
        try :xbmc .executebuiltin ("Reboot")#line:172
        except :pass #line:173
    elif O0O00OOOO0OO000O0 =='windows':#line:174
        log ("############   try windows force close  #################")#line:175
        try :#line:176
            os .system ('@ECHO off')#line:177
            os .system ('tskill XBMC.exe')#line:178
        except :pass #line:179
        try :#line:180
            os .system ('@ECHO off')#line:181
            os .system ('tskill Kodi.exe')#line:182
        except :pass #line:183
        try :#line:184
            os .system ('@ECHO off')#line:185
            os .system ('tskill SMC.exe')#line:186
        except :pass #line:187
        try :#line:188
            os .system ('@ECHO off')#line:189
            os .system ('TASKKILL /im Kodi.exe /f')#line:190
        except :pass #line:191
        try :#line:192
            os .system ('@ECHO off')#line:193
            os .system ('TASKKILL /im XBMC.exe /f')#line:194
        except :pass #line:195
        try :#line:196
            os .system ('@ECHO off')#line:197
            os .system ('TASKKILL /im XBMC.exe /f')#line:198
        except :pass #line:199
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Use task manager and NOT ALT F4')#line:200
    else :#line:201
        log ("############   try atv force close  #################")#line:202
        try :os .system ('killall AppleTV')#line:203
        except :pass #line:204
        log ("############   try raspbmc force close  #################")#line:205
        try :os .system ('sudo initctl stop kodi')#line:206
        except :pass #line:207
        try :os .system ('sudo initctl stop xbmc')#line:208
        except :pass #line:209
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:210
        try :xbmc .executebuiltin ("Reboot")#line:211
        except :pass #line:212
def platform ():#line:219
    if xbmc .getCondVisibility ('system.platform.android'):return 'android'#line:220
    elif xbmc .getCondVisibility ('system.platform.linux'):return 'linux'#line:221
    elif xbmc .getCondVisibility ('system.platform.windows'):return 'windows'#line:222
    elif xbmc .getCondVisibility ('system.platform.osx'):return 'osx'#line:223
    elif xbmc .getCondVisibility ('system.platform.atv2'):return 'atv2'#line:224
    elif xbmc .getCondVisibility ('system.platform.ios'):return 'ios'#line:225
def verifyplatform ():#line:227
    OOOOOO00OO0000OOO =platform ()#line:228
    log ("XvBMC_Platform: "+str (OOOOOO00OO0000OOO ))#line:229
    if OOOOOO00OO0000OOO =='osx':#line:230
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees for OSX [B];-p[/B]')#line:231
        log ("=== OSX ===")#line:232
    elif OOOOOO00OO0000OOO =='linux':#line:233
        log ("=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ===")#line:235
    elif OOOOOO00OO0000OOO =='android':#line:236
        dialog .ok ('[COLOR=red][B]!!!  IMPORTANT  !!![/COLOR][/B]','[COLOR=lime]There\'s also a specific XvBMC\'s Android add-on update(r)[/COLOR]','...enkel voor specifieke bonus Android add-on updates...',noservicepack +' '+notforked )#line:237
        log ("=== Android ===")#line:238
    elif OOOOOO00OO0000OOO =='windows':#line:239
        log ("=== Download de laatste XvBMC (Windows) ServicePack ===")#line:241
    else :#line:242
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees though [B];-p[/B]')#line:243
        log ("=== ATV2/iOS/OSMC/Raspbmc/etc ===")#line:244
def KODIVERSION (url ):O0000O0O0O00OO0O0 =xbmc .getInfoLabel ("System.BuildVersion");OOO00O0OOOO0OOO00 =O0000O0O0O00OO0O0 [:4 ];log ("XvBMC_v"+OOO00O0OOOO0OOO00 );dialog .ok (MainTitle ,'Your Kodi Version : [COLOR lime][B]%s[/B][/COLOR]'%OOO00O0OOOO0OOO00 )#line:247
def checkSPversie ():#line:250
    if os .path .isfile (uwspversietxt ):#line:251
       O00O0O00000OOO0OO =open (uwspversietxt ,'r')#line:252
       O0OOOOO000OO0O0OO =O00O0O00000OOO0OO .read ()#line:253
       O00O0O00000OOO0OO .close ()#line:254
       return 'uwspversietxt','[COLOR gray]'+O0OOOOO000OO0O0OO +'[/COLOR]'#line:255
    elif os .path .isfile (uwspversietxtwiz ):#line:256
         O00O0O00000OOO0OO =open (uwspversietxtwiz ,'r')#line:257
         OOOOO00OOOO000O0O =O00O0O00000OOO0OO .read ()#line:258
         O00O0O00000OOO0OO .close ()#line:259
         return 'uwspversietxtwiz','[COLOR gray]'+OOOOO00OOOO000O0O +'[/COLOR]'#line:260
    elif os .path .isfile (uwspversietxtrpi ):#line:261
         O00O0O00000OOO0OO =open (uwspversietxtrpi ,'r')#line:262
         O00OOOOOOO0OOOOO0 =O00O0O00000OOO0OO .read ()#line:263
         O00O0O00000OOO0OO .close ()#line:264
         return 'uwspversietxtrpi','[COLOR gray]'+O00OOOOOOO0OOOOO0 +'[/COLOR]'#line:265
    else :#line:266
        return 'unknown',''#line:267
def checkXvbmcversie ():#line:269
    if os .path .isfile (bldversietxt ):#line:270
       O0O00O0OOOOOOO0O0 =open (bldversietxt ,'r')#line:271
       O00OOOO0O0OO00OOO =O0O00O0OOOOOOO0O0 .read ()#line:272
       O0O00O0OOOOOOO0O0 .close ()#line:273
       return 'bldversietxt','[COLOR gray]'+O00OOOO0O0OO00OOO +'[/COLOR]'#line:274
    elif os .path .isfile (bldversietxtwiz ):#line:275
         O0O00O0OOOOOOO0O0 =open (bldversietxtwiz ,'r')#line:276
         O00000OO00O0O00O0 =O0O00O0OOOOOOO0O0 .read ()#line:277
         O0O00O0OOOOOOO0O0 .close ()#line:278
         return 'bldversietxtwiz','[COLOR gray]'+O00000OO00O0O00O0 +'[/COLOR]'#line:279
    else :#line:280
        return 'unknown',''#line:281
def removefolder (map ,exclude =None ):#line:288
    for OOO00OO0OOO00O0OO ,OOO00O0OO000O0O00 ,OO0O0OO00OOOO00OO in os .walk (map ,topdown =False ):#line:289
        for OO0O00O0OO0O00000 in OO0O0OO00OOOO00OO :#line:290
            if (OOO00OO0OOO00O0OO .find (exclude )>0 ):#line:291
               continue #line:292
            try :os .remove (os .path .join (OOO00OO0OOO00O0OO ,OO0O00O0OO0O00000 ))#line:293
            except :pass #line:294
        for OO0O00O0OO0O00000 in OOO00O0OO000O0O00 :#line:295
            if (OO0O00O0OO0O00000 ==exclude ):#line:296
               continue #line:297
            try :os .rmdir (os .path .join (OOO00OO0OOO00O0OO ,OO0O00O0OO0O00000 ))#line:298
            except :pass #line:299
def REMOVE_EMPTY_FOLDERS ():#line:301
    log ("########### Start Removing Empty Folders #########")#line:303
    OOO0O0OOOOO00000O =0 #line:304
    O00O0O0O000O00OO0 =0 #line:305
    for OOO0O000OO0O00O0O ,O000OO0O0O0OOOO0O ,O00O00OOO00OO00O0 in os .walk (HOME ):#line:306
        if len (O000OO0O0O0OOOO0O )==0 and len (O00O00OOO00OO00O0 )==0 :#line:307
           OOO0O0OOOOO00000O +=1 #line:308
           os .rmdir (OOO0O000OO0O00O0O )#line:309
           log ("successfully removed: "+OOO0O000OO0O00O0O )#line:310
        elif len (O000OO0O0O0OOOO0O )>0 and len (O00O00OOO00OO00O0 )>0 :#line:311
             O00O0O0O000O00OO0 +=1 #line:312
def TextBoxes (announce ):#line:319
    class OOOO000OOO000O0OO ():#line:320
        WINDOW =10147 #line:321
        CONTROL_LABEL =1 #line:322
        CONTROL_TEXTBOX =5 #line:323
        def __init__ (self ,*OO0O00O00OOOOOOO0 ,**OOOOOOOO00OOOO000 ):#line:324
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:325
            self .win =xbmcgui .Window (self .WINDOW )#line:326
            xbmc .sleep (500 )#line:327
            self .setControls ()#line:328
        def setControls (self ):#line:329
            self .win .getControl (self .CONTROL_LABEL ).setLabel ('XvBMC - View Log[B]:[/B]')#line:330
            try :OOO0OOOO0O00O00O0 =open (announce );OO000OOOO000OOOOO =OOO0OOOO0O00O00O0 .read ()#line:331
            except :OO000OOOO000OOOOO =announce #line:332
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (OO000OOOO000OOOOO ))#line:333
            return #line:334
    OOOO000OOO000O0OO ()#line:335
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:336
          time .sleep (.5 )#line:337
def TextBoxesPlain (heading ,announce ):#line:339
    class OOO0OO0O0O0O0OOO0 ():#line:340
        WINDOW =10147 #line:341
        CONTROL_LABEL =1 #line:342
        CONTROL_TEXTBOX =5 #line:343
        def __init__ (self ,*O00000000OO000OOO ,**OOO0O0OO000OOO00O ):#line:344
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:345
            self .win =xbmcgui .Window (self .WINDOW )#line:346
            xbmc .sleep (500 )#line:347
            self .setControls ()#line:348
        def setControls (self ):#line:349
            self .win .getControl (self .CONTROL_LABEL ).setLabel (heading )#line:350
            try :O00OO0000000OO0O0 =open (announce );OO0000O000000OOO0 =O00OO0000000OO0O0 .read ()#line:351
            except :OO0000O000000OOO0 =announce #line:352
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (OO0000O000000OOO0 ))#line:353
            return #line:354
    OOO0OO0O0O0O0OOO0 ()#line:355
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:356
          time .sleep (.5 )#line:357
def facebook ():#line:359
    TextBoxesPlain ('XvBMC Nederland','[COLOR=red]NOTE:[/COLOR]\nXvBMC Nederland (xbmc nl) wij zijn geen helpdesk van/voor boxverkopers\n\nVoor meer informatie kijk op https://bit.ly/XvBMC-NL')#line:360
def AboutXvBMC ():#line:367
    O00O0O0000OOO00OO =''#line:368
    OO00OOOOO0O0OOOO0 ='https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/readme.xml'#line:369
    O00OOOOO0OOO000OO =urllib2 .Request (OO00OOOOO0O0OOOO0 )#line:370
    O00OOOOO0OOO000OO .add_header ('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')#line:371
    OO0O00OOO0OO00OO0 =urllib2 .urlopen (O00OOOOO0OOO000OO )#line:372
    O0O00O000O0OOO00O =OO0O00OOO0OO00OO0 .read ()#line:373
    OO0O00OOO0OO00OO0 .close ()#line:374
    O00O0O0000OO00O0O =re .compile ("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re .DOTALL ).findall (O0O00O000O0OOO00O )#line:375
    for OOO0OOO0O0O0000O0 ,OO0000O00000O0O0O in O00O0O0000OO00O0O :#line:376
        try :#line:377
                OOO0OOO0O0O0000O0 =OOO0OOO0O0O0000O0 .decode ('ascii','ignore')#line:378
        except :#line:379
                OOO0OOO0O0O0000O0 =OOO0OOO0O0O0000O0 .decode ('utf-8','ignore')#line:380
        OO0000O00000O0O0O =OO0000O00000O0O0O [:-15 ]#line:381
        OOO0OOO0O0O0000O0 =OOO0OOO0O0O0000O0 .replace ('&amp;','')#line:382
        OO0000O00000O0O0O ='[COLOR lime][B]'+OO0000O00000O0O0O +'[/B][/COLOR]'#line:383
        O00O0O0000OOO00OO =O00O0O0000OOO00OO +OO0000O00000O0O0O +'\n'+OOO0OOO0O0O0000O0 +'\n'+'\n'#line:384
    infoTXT ('[COLOR lime]Usage policy & Disclaimer [B]X[/B]v[B]BMC-[/B]NL[/COLOR]',O00O0O0000OOO00OO )#line:385
def infoTXT (heading ,text ):#line:387
    OOO0OO00O0OO0OO0O =10147 #line:388
    xbmc .executebuiltin ('ActivateWindow(%d)'%OOO0OO00O0OO0OO0O )#line:389
    xbmc .sleep (100 )#line:390
    O00OO0000O00OO0O0 =xbmcgui .Window (OOO0OO00O0OO0OO0O )#line:391
    O0000O0000OO0OOO0 =50 #line:392
    while (O0000O0000OO0OOO0 >0 ):#line:393
        try :#line:394
            xbmc .sleep (10 )#line:395
            O0000O0000OO0OOO0 -=1 #line:396
            O00OO0000O00OO0O0 .getControl (1 ).setLabel (heading )#line:397
            O00OO0000O00OO0O0 .getControl (5 ).setText (text )#line:398
            return #line:399
        except :#line:400
            pass #line:401
artwork =xbmc .translatePath (os .path .join ('special://home','addons',AddonID ,'/'))#line:408
fanart =artwork +'fanart.jpg'#line:409
def addonIcon ():#line:412
    return artwork +'icon.png'#line:413
def message (text1 ,text2 ="",text3 =""):#line:416
    if text3 =="":#line:417
       xbmcgui .Dialog ().ok (text1 ,text2 )#line:418
    elif text2 =="":#line:419
         xbmcgui .Dialog ().ok ("",text1 )#line:420
    else :#line:421
        xbmcgui .Dialog ().ok (text1 ,text2 ,text3 )#line:422
def message_yes_no (text1 ,text2 ="",text3 =""):#line:424
    if text3 =="":OO0000OO0O0O00000 =xbmcgui .Dialog ().yesno (text1 ,text2 )#line:425
    elif text2 =="":OO0000OO0O0O00000 =xbmcgui .Dialog ().yesno ("",text1 )#line:426
    else :OO0000OO0O0O00000 =xbmcgui .Dialog ().yesno (text1 ,text2 ,text3 )#line:427
    return OO0000OO0O0O00000 #line:428
def infoDialog (message ,heading =addonInfo ('name'),icon =addonIcon (),time =3000 ):#line:431
    try :#line:432
        dialog .notification (heading ,message ,icon ,time ,sound =False )#line:433
    except :#line:434
        execute ("Notification(%s,%s, %s, %s)"%(heading ,message ,time ,icon ))#line:435
def okDialog (line1 ,line2 ,line3 ,heading =addonInfo ('name')):#line:438
    return dialog .ok (heading ,line1 ,line2 ,line3 )#line:439
def yesnoDialog (line1 ,line2 ,line3 ,heading =addonInfo ('name'),nolabel ='',yeslabel =''):#line:441
    return dialog .yesno (heading ,line1 ,line2 ,line3 ,nolabel ,yeslabel )#line:442
def log (msg ,level =xbmc .LOGNOTICE ):#line:449
    O00000OO000OOO0OO ='XvBMC_NOTICE'#line:450
    level =xbmc .LOGNOTICE #line:452
    try :#line:461
        xbmc .log ('%s: %s'%(O00000OO000OOO0OO ,msg ),level )#line:462
    except :#line:463
        try :#line:464
            xbmc .log ('Logging Failure',level )#line:465
        except :#line:466
            pass #line:467
def forceRefresh (melding =None ):#line:470
    xbmc .executebuiltin ('UpdateLocalAddons()');log ("XvBMC_UpdateLocalAddons()")#line:471
    time .sleep (0.5 )#line:472
    xbmc .executebuiltin ('UpdateAddonRepos()');log ("XvBMC_UpdateAddonRepos()")#line:473
    time .sleep (0.5 )#line:474
    if melding :#line:475
       dialog .ok (MainTitle ,'Force Refresh Repos and Update LocalAddons')#line:476
       try :#line:477
           xbmc .executebuiltin ('ReloadSkin()');log ("XvBMC_ReloadSkin()")#line:478
       except :pass #line:479
       try :#line:480
           xbmc .executebuiltin ('Container.Refresh');log ("Container.Refresh")#line:481
       except :pass #line:482
def get_kversion ():#line:485
    O0OOOO00O0O0O0O0O =xbmc .getInfoLabel ('System.BuildVersion')#line:486
    OOO00O0OO0O00O0O0 =O0OOOO00O0O0O0O0O .split (".")#line:487
    O000OOO0O00OOOOOO =int (OOO00O0OO0O00O0O0 [0 ])#line:488
    return O000OOO0O00OOOOOO #line:493
def setView (content ,viewType ):#line:496
    if content :#line:498
       xbmcplugin .setContent (int (sys .argv [1 ]),content )#line:499
    if ADDON .getSetting ('auto-view')=='true':#line:500
       xbmc .executebuiltin ("Container.SetViewMode(%s)"%ADDON .getSetting (viewType ))#line:501
def closeandexit ():#line:508
    xbmc .executebuiltin ('Action(back)')#line:510
"""
    IF you copy/paste 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
