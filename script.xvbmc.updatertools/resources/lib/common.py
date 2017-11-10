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
basewiz ='aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC94dmJtY3dpemFyZHov'#line:52
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
    OO0OO00OO0OOO00OO =platform ()#line:75
    log ("XvBMC_Platform: "+str (OO0OO00OO0OOO00OO ))#line:76
    try :os ._exit (1 )#line:77
    except :pass #line:78
    if OO0OO00OO0OOO00OO =='osx':#line:79
        log ("############   try osx force close  #################")#line:80
        try :os .system ('killall -9 XBMC')#line:81
        except :pass #line:82
        try :os .system ('killall -9 Kodi')#line:83
        except :pass #line:84
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:85
        try :xbmc .executebuiltin ("Reboot")#line:86
        except :pass #line:87
    elif OO0OO00OO0OOO00OO =='linux':#line:88
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
    elif OO0OO00OO0OOO00OO =='android':#line:103
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
    elif OO0OO00OO0OOO00OO =='windows':#line:174
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
    O00000000O000000O =platform ()#line:228
    log ("XvBMC_Platform: "+str (O00000000O000000O ))#line:229
    if O00000000O000000O =='osx':#line:230
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees for OSX [B];-p[/B]')#line:231
        log ("=== OSX ===")#line:232
    elif O00000000O000000O =='linux':#line:233
        log ("=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ===")#line:235
    elif O00000000O000000O =='android':#line:236
        dialog .ok ('[COLOR=red][B]!!!  IMPORTANT  !!![/COLOR][/B]','[COLOR=lime]There\'s also a specific XvBMC\'s Android add-on update(r)[/COLOR]','...enkel voor specifieke bonus Android add-on updates...',noservicepack +' '+notforked )#line:237
        log ("=== Android ===")#line:238
    elif O00000000O000000O =='windows':#line:239
        log ("=== Download de laatste XvBMC (Windows) ServicePack ===")#line:241
    else :#line:242
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees though [B];-p[/B]')#line:243
        log ("=== ATV2/iOS/OSMC/Raspbmc/etc ===")#line:244
def KODIVERSION (url ):O0OOO00O0O00O0O00 =xbmc .getInfoLabel ("System.BuildVersion");O000O00O0000OO0O0 =O0OOO00O0O00O0O00 [:4 ];log ("XvBMC_v"+O000O00O0000OO0O0 );dialog .ok (MainTitle ,'Your Kodi Version : [COLOR lime][B]%s[/B][/COLOR]'%O000O00O0000OO0O0 )#line:247
def checkSPversie ():#line:250
    if os .path .isfile (uwspversietxt ):#line:251
       OOOO0O0OOOO0O0O00 =open (uwspversietxt ,'r')#line:252
       O00O0O00O00OO0O00 =OOOO0O0OOOO0O0O00 .read ()#line:253
       OOOO0O0OOOO0O0O00 .close ()#line:254
       return 'uwspversietxt','[COLOR gray]'+O00O0O00O00OO0O00 +'[/COLOR]'#line:255
    elif os .path .isfile (uwspversietxtwiz ):#line:256
         OOOO0O0OOOO0O0O00 =open (uwspversietxtwiz ,'r')#line:257
         O0O000000OO0O00O0 =OOOO0O0OOOO0O0O00 .read ()#line:258
         OOOO0O0OOOO0O0O00 .close ()#line:259
         return 'uwspversietxtwiz','[COLOR gray]'+O0O000000OO0O00O0 +'[/COLOR]'#line:260
    elif os .path .isfile (uwspversietxtrpi ):#line:261
         OOOO0O0OOOO0O0O00 =open (uwspversietxtrpi ,'r')#line:262
         O00000OO0O000OO00 =OOOO0O0OOOO0O0O00 .read ()#line:263
         OOOO0O0OOOO0O0O00 .close ()#line:264
         return 'uwspversietxtrpi','[COLOR gray]'+O00000OO0O000OO00 +'[/COLOR]'#line:265
    else :#line:266
        return 'unknown',''#line:267
def checkXvbmcversie ():#line:269
    if os .path .isfile (bldversietxt ):#line:270
       OO00OOO0OOO0O0O00 =open (bldversietxt ,'r')#line:271
       OO0OO00O000OO0OO0 =OO00OOO0OOO0O0O00 .read ()#line:272
       OO00OOO0OOO0O0O00 .close ()#line:273
       return 'bldversietxt','[COLOR gray]'+OO0OO00O000OO0OO0 +'[/COLOR]'#line:274
    elif os .path .isfile (bldversietxtwiz ):#line:275
         OO00OOO0OOO0O0O00 =open (bldversietxtwiz ,'r')#line:276
         OOOOOOOOOO0O0OO00 =OO00OOO0OOO0O0O00 .read ()#line:277
         OO00OOO0OOO0O0O00 .close ()#line:278
         return 'bldversietxtwiz','[COLOR gray]'+OOOOOOOOOO0O0OO00 +'[/COLOR]'#line:279
    else :#line:280
        return 'unknown',''#line:281
def removefolder (map ,exclude =None ):#line:288
    for OOOO0O0OO0O0OO000 ,OOOO000OO0OOO0O00 ,OOOOO000O0OOO00O0 in os .walk (map ,topdown =False ):#line:289
        for OO0OO0000OOOO0O00 in OOOOO000O0OOO00O0 :#line:290
            if (OOOO0O0OO0O0OO000 .find (exclude )>0 ):#line:291
               continue #line:292
            try :os .remove (os .path .join (OOOO0O0OO0O0OO000 ,OO0OO0000OOOO0O00 ))#line:293
            except :pass #line:294
        for OO0OO0000OOOO0O00 in OOOO000OO0OOO0O00 :#line:295
            if (OO0OO0000OOOO0O00 ==exclude ):#line:296
               continue #line:297
            try :os .rmdir (os .path .join (OOOO0O0OO0O0OO000 ,OO0OO0000OOOO0O00 ))#line:298
            except :pass #line:299
def REMOVE_EMPTY_FOLDERS ():#line:301
    log ("########### Start Removing Empty Folders #########")#line:303
    O00000O000000OO0O =0 #line:304
    OOO0OO0OO00O0OO0O =0 #line:305
    for OOOOOO000O00O00OO ,O0000000000O0OO00 ,OO00O00O00O0O0O0O in os .walk (HOME ):#line:306
        if len (O0000000000O0OO00 )==0 and len (OO00O00O00O0O0O0O )==0 :#line:307
           O00000O000000OO0O +=1 #line:308
           os .rmdir (OOOOOO000O00O00OO )#line:309
           log ("successfully removed: "+OOOOOO000O00O00OO )#line:310
        elif len (O0000000000O0OO00 )>0 and len (OO00O00O00O0O0O0O )>0 :#line:311
             OOO0OO0OO00O0OO0O +=1 #line:312
def TextBoxes (announce ):#line:319
    class OO000O00OOO0O0OOO ():#line:320
        WINDOW =10147 #line:321
        CONTROL_LABEL =1 #line:322
        CONTROL_TEXTBOX =5 #line:323
        def __init__ (self ,*OO0OOOO0O0O000000 ,**O0OOO0O0OOOO0O0OO ):#line:324
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:325
            self .win =xbmcgui .Window (self .WINDOW )#line:326
            xbmc .sleep (500 )#line:327
            self .setControls ()#line:328
        def setControls (self ):#line:329
            self .win .getControl (self .CONTROL_LABEL ).setLabel ('XvBMC - View Log[B]:[/B]')#line:330
            try :O000000O0OO000O00 =open (announce );O00OOO00O000O0OOO =O000000O0OO000O00 .read ()#line:331
            except :O00OOO00O000O0OOO =announce #line:332
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (O00OOO00O000O0OOO ))#line:333
            return #line:334
    OO000O00OOO0O0OOO ()#line:335
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:336
          time .sleep (.5 )#line:337
def TextBoxesPlain (heading ,announce ):#line:339
    class O0OO0OO0OO00O000O ():#line:340
        WINDOW =10147 #line:341
        CONTROL_LABEL =1 #line:342
        CONTROL_TEXTBOX =5 #line:343
        def __init__ (self ,*O000OOO00000O00O0 ,**O0OOOOO00O0000O0O ):#line:344
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:345
            self .win =xbmcgui .Window (self .WINDOW )#line:346
            xbmc .sleep (500 )#line:347
            self .setControls ()#line:348
        def setControls (self ):#line:349
            self .win .getControl (self .CONTROL_LABEL ).setLabel (heading )#line:350
            try :OOOOO00OOO0O00O0O =open (announce );OO000O0O0OO0OOO00 =OOOOO00OOO0O00O0O .read ()#line:351
            except :OO000O0O0OO0OOO00 =announce #line:352
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (OO000O0O0OO0OOO00 ))#line:353
            return #line:354
    O0OO0OO0OO00O000O ()#line:355
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:356
          time .sleep (.5 )#line:357
def facebook ():#line:359
    TextBoxesPlain ('XvBMC Nederland','[COLOR=red]NOTE:[/COLOR]\nXvBMC Nederland (xbmc nl) wij zijn geen helpdesk van/voor boxverkopers\n\nVoor meer informatie kijk op https://bit.ly/XvBMC-NL')#line:360
def AboutXvBMC ():#line:367
    OO0O00000OO0OOOOO =''#line:368
    OOOO0O00O0OOOOO0O ='https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/readme.xml'#line:369
    OOO0000OO0O0OOOOO =urllib2 .Request (OOOO0O00O0OOOOO0O )#line:370
    OOO0000OO0O0OOOOO .add_header ('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')#line:371
    O0000O00OO000O000 =urllib2 .urlopen (OOO0000OO0O0OOOOO )#line:372
    OOOOO0OO0O0O0O0OO =O0000O00OO000O000 .read ()#line:373
    O0000O00OO000O000 .close ()#line:374
    O0O00O00OOO000OO0 =re .compile ("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re .DOTALL ).findall (OOOOO0OO0O0O0O0OO )#line:375
    for O0O0O0000O00OOO00 ,O00OOO0O00OOO00OO in O0O00O00OOO000OO0 :#line:376
        try :#line:377
                O0O0O0000O00OOO00 =O0O0O0000O00OOO00 .decode ('ascii','ignore')#line:378
        except :#line:379
                O0O0O0000O00OOO00 =O0O0O0000O00OOO00 .decode ('utf-8','ignore')#line:380
        O00OOO0O00OOO00OO =O00OOO0O00OOO00OO [:-15 ]#line:381
        O0O0O0000O00OOO00 =O0O0O0000O00OOO00 .replace ('&amp;','')#line:382
        O00OOO0O00OOO00OO ='[COLOR lime][B]'+O00OOO0O00OOO00OO +'[/B][/COLOR]'#line:383
        OO0O00000OO0OOOOO =OO0O00000OO0OOOOO +O00OOO0O00OOO00OO +'\n'+O0O0O0000O00OOO00 +'\n'+'\n'#line:384
    infoTXT ('[COLOR lime]Usage policy & Disclaimer [B]X[/B]v[B]BMC-[/B]NL[/COLOR]',OO0O00000OO0OOOOO )#line:385
def infoTXT (heading ,text ):#line:387
    O0000O0OOO0OO0OO0 =10147 #line:388
    xbmc .executebuiltin ('ActivateWindow(%d)'%O0000O0OOO0OO0OO0 )#line:389
    xbmc .sleep (100 )#line:390
    O0O0O0O00O0O0O00O =xbmcgui .Window (O0000O0OOO0OO0OO0 )#line:391
    OOOOOOO0O0000OOO0 =50 #line:392
    while (OOOOOOO0O0000OOO0 >0 ):#line:393
        try :#line:394
            xbmc .sleep (10 )#line:395
            OOOOOOO0O0000OOO0 -=1 #line:396
            O0O0O0O00O0O0O00O .getControl (1 ).setLabel (heading )#line:397
            O0O0O0O00O0O0O00O .getControl (5 ).setText (text )#line:398
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
    if text3 =="":O00O0O00O0OOO00OO =xbmcgui .Dialog ().yesno (text1 ,text2 )#line:425
    elif text2 =="":O00O0O00O0OOO00OO =xbmcgui .Dialog ().yesno ("",text1 )#line:426
    else :O00O0O00O0OOO00OO =xbmcgui .Dialog ().yesno (text1 ,text2 ,text3 )#line:427
    return O00O0O00O0OOO00OO #line:428
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
    O0O00000O00OOOOOO ='XvBMC_NOTICE'#line:450
    level =xbmc .LOGNOTICE #line:452
    try :#line:461
        xbmc .log ('%s: %s'%(O0O00000O00OOOOOO ,msg ),level )#line:462
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
    OOO0O0O000O000OO0 =xbmc .getInfoLabel ('System.BuildVersion')#line:486
    OOO000OO0OO00O000 =OOO0O0O000O000OO0 .split (".")#line:487
    OO0OO00O0O0O00OO0 =int (OOO000OO0OO00O000 [0 ])#line:488
    return OO0OO00O0O0O00OO0 #line:493
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