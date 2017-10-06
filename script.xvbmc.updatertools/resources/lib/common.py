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
uwspversietxt =xbmc .translatePath (os .path .join ('special://home/userdata','versiesp.txt'))#line:60
uwspversietxtrpi =xbmc .translatePath (os .path .join ('special://home/userdata','rpi-service.txt'))#line:61
uwspversietxtwiz =xbmc .translatePath (os .path .join ('special://home/userdata','wizsp.txt'))#line:62
def killKodi ():#line:68
    OO00O000000OOOO00 =platform ()#line:74
    log ("XvBMC_Platform: "+str (OO00O000000OOOO00 ))#line:75
    try :os ._exit (1 )#line:76
    except :pass #line:77
    if OO00O000000OOOO00 =='osx':#line:78
        log ("############   try osx force close  #################")#line:79
        try :os .system ('killall -9 XBMC')#line:80
        except :pass #line:81
        try :os .system ('killall -9 Kodi')#line:82
        except :pass #line:83
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:84
        try :xbmc .executebuiltin ("Reboot")#line:85
        except :pass #line:86
    elif OO00O000000OOOO00 =='linux':#line:87
        log ("############   try linux force close  #################")#line:88
        try :os .system ('killall XBMC')#line:91
        except :pass #line:92
        try :os .system ('killall Kodi')#line:93
        except :pass #line:94
        try :os .system ('killall -9 xbmc.bin')#line:95
        except :pass #line:96
        try :os .system ('killall -9 kodi.bin')#line:97
        except :pass #line:98
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:99
        try :xbmc .executebuiltin ("Reboot")#line:100
        except :pass #line:101
    elif OO00O000000OOOO00 =='android':#line:102
        log ("############   try android force close  #################")#line:103
        try :os .system ('adb shell am force-stop com.jesusboxmedia')#line:104
        except :pass #line:105
        try :os .system ('adb shell am force-stop com.perfectzoneproductions.jesusboxmedia')#line:106
        except :pass #line:107
        try :os .system ('adb shell am force-stop com.semperpax.spmc')#line:108
        except :pass #line:109
        try :os .system ('adb shell am force-stop com.semperpax.spmc16')#line:110
        except :pass #line:111
        try :os .system ('adb shell am force-stop com.spmc')#line:112
        except :pass #line:113
        try :os .system ('adb shell am force-stop com.spmc16')#line:114
        except :pass #line:115
        try :os .system ('adb shell am force-stop org.kodi')#line:116
        except :pass #line:117
        try :os .system ('adb shell am force-stop org.lodi.mobi')#line:118
        except :pass #line:119
        try :os .system ('adb shell am force-stop org.xbmc')#line:120
        except :pass #line:121
        try :os .system ('adb shell am force-stop org.xbmc.cemc')#line:122
        except :pass #line:123
        try :os .system ('adb shell am force-stop org.xbmc.cemc_pro')#line:124
        except :pass #line:125
        try :os .system ('adb shell am force-stop org.xbmc.kodi')#line:126
        except :pass #line:127
        try :os .system ('adb shell am force-stop org.xbmc.xbmc')#line:128
        except :pass #line:129
        try :os .system ('adb shell am force-stop uk.dbmc')#line:130
        except :pass #line:131
        try :os .system ('adb shell am force-stop uk.droidbox.dbmc')#line:132
        except :pass #line:133
        try :os .system ('adb shell kill com.perfectzoneproductions.jesusboxmedia')#line:134
        except :pass #line:135
        try :os .system ('adb shell kill com.semperpax')#line:136
        except :pass #line:137
        try :os .system ('adb shell kill com.semperpax.spmc16')#line:138
        except :pass #line:139
        try :os .system ('adb shell kill org.kodi')#line:140
        except :pass #line:141
        try :os .system ('adb shell kill org.lodi.mobi')#line:142
        except :pass #line:143
        try :os .system ('adb shell kill org.xbmc')#line:144
        except :pass #line:145
        try :os .system ('adb shell kill org.xbmc.cemc')#line:146
        except :pass #line:147
        try :os .system ('adb shell kill org.xbmc.cemc_pro')#line:148
        except :pass #line:149
        try :os .system ('adb shell kill org.xbmc.kodi')#line:150
        except :pass #line:151
        try :os .system ('adb shell kill org.xbmc.xbmc')#line:152
        except :pass #line:153
        try :os .system ('Process.killProcess(android.os.Process.com.semperpax.spmc16());')#line:154
        except :pass #line:155
        try :os .system ('Process.killProcess(android.os.Process.org.fire());')#line:156
        except :pass #line:157
        try :os .system ('Process.killProcess(android.os.Process.org.fire.guru());')#line:158
        except :pass #line:159
        try :os .system ('Process.killProcess(android.os.Process.org.fire.guruv());')#line:160
        except :pass #line:161
        try :os .system ('Process.killProcess(android.os.Process.org.kodi());')#line:162
        except :pass #line:163
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc());')#line:164
        except :pass #line:165
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc.kodi());')#line:166
        except :pass #line:167
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc.xbmc());')#line:168
        except :pass #line:169
        dialog .ok (waarschuwing ,'Your system has been detected as Android, you ','[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Either close using Task Manager (If unsure pull the plug).')#line:170
        try :xbmc .executebuiltin ("Reboot")#line:171
        except :pass #line:172
    elif OO00O000000OOOO00 =='windows':#line:173
        log ("############   try windows force close  #################")#line:174
        try :#line:175
            os .system ('@ECHO off')#line:176
            os .system ('tskill XBMC.exe')#line:177
        except :pass #line:178
        try :#line:179
            os .system ('@ECHO off')#line:180
            os .system ('tskill Kodi.exe')#line:181
        except :pass #line:182
        try :#line:183
            os .system ('@ECHO off')#line:184
            os .system ('tskill SMC.exe')#line:185
        except :pass #line:186
        try :#line:187
            os .system ('@ECHO off')#line:188
            os .system ('TASKKILL /im Kodi.exe /f')#line:189
        except :pass #line:190
        try :#line:191
            os .system ('@ECHO off')#line:192
            os .system ('TASKKILL /im XBMC.exe /f')#line:193
        except :pass #line:194
        try :#line:195
            os .system ('@ECHO off')#line:196
            os .system ('TASKKILL /im XBMC.exe /f')#line:197
        except :pass #line:198
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Use task manager and NOT ALT F4')#line:199
    else :#line:200
        log ("############   try atv force close  #################")#line:201
        try :os .system ('killall AppleTV')#line:202
        except :pass #line:203
        log ("############   try raspbmc force close  #################")#line:204
        try :os .system ('sudo initctl stop kodi')#line:205
        except :pass #line:206
        try :os .system ('sudo initctl stop xbmc')#line:207
        except :pass #line:208
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:209
        try :xbmc .executebuiltin ("Reboot")#line:210
        except :pass #line:211
def platform ():#line:218
    if xbmc .getCondVisibility ('system.platform.android'):return 'android'#line:219
    elif xbmc .getCondVisibility ('system.platform.linux'):return 'linux'#line:220
    elif xbmc .getCondVisibility ('system.platform.windows'):return 'windows'#line:221
    elif xbmc .getCondVisibility ('system.platform.osx'):return 'osx'#line:222
    elif xbmc .getCondVisibility ('system.platform.atv2'):return 'atv2'#line:223
    elif xbmc .getCondVisibility ('system.platform.ios'):return 'ios'#line:224
def verifyplatform ():#line:226
    OO000O0O0O000O000 =platform ()#line:227
    log ("XvBMC_Platform: "+str (OO000O0O0O000O000 ))#line:228
    if OO000O0O0O000O000 =='osx':#line:229
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees for OSX [B];-p[/B]')#line:230
        log ("=== OSX ===")#line:231
    elif OO000O0O0O000O000 =='linux':#line:232
        log ("=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ===")#line:234
    elif OO000O0O0O000O000 =='android':#line:235
        dialog .ok ('[COLOR=red][B]!!!  IMPORTANT  !!![/COLOR][/B]','[COLOR=lime]There\'s also a specific XvBMC\'s Android add-on update(r)[/COLOR]','...enkel voor specifieke bonus Android add-on updates...',noservicepack +' '+notforked )#line:236
        log ("=== Android ===")#line:237
    elif OO000O0O0O000O000 =='windows':#line:238
        log ("=== Download de laatste XvBMC (Windows) ServicePack ===")#line:240
    else :#line:241
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees though [B];-p[/B]')#line:242
        log ("=== ATV2/iOS/OSMC/Raspbmc/etc ===")#line:243
def KODIVERSION (url ):OOO000OOOO0O0O0OO =xbmc .getInfoLabel ("System.BuildVersion");OO000OOO00OO0OOOO =OOO000OOOO0O0O0OO [:4 ];log ("XvBMC_v"+OO000OOO00OO0OOOO );dialog .ok (MainTitle ,'Your Kodi Version : [COLOR lime][B]%s[/B][/COLOR]'%OO000OOO00OO0OOOO )#line:246
def checkSPversie ():#line:249
    if os .path .isfile (uwspversietxt ):#line:250
       O0OOO0O0O000OOOOO =open (uwspversietxt ,'r')#line:251
       O00O000O0OO00OOO0 =O0OOO0O0O000OOOOO .read ()#line:252
       O0OOO0O0O000OOOOO .close ()#line:253
       return 'uwspversietxt','[COLOR gray]'+O00O000O0OO00OOO0 +'[/COLOR]'#line:254
    elif os .path .isfile (uwspversietxtwiz ):#line:255
         O0OOO0O0O000OOOOO =open (uwspversietxtwiz ,'r')#line:256
         O0OOO0O0OOO0O000O =O0OOO0O0O000OOOOO .read ()#line:257
         O0OOO0O0O000OOOOO .close ()#line:258
         return 'uwspversietxtwiz','[COLOR gray]'+O0OOO0O0OOO0O000O +'[/COLOR]'#line:259
    elif os .path .isfile (uwspversietxtrpi ):#line:260
         O0OOO0O0O000OOOOO =open (uwspversietxtrpi ,'r')#line:261
         OOOO00000OOO0O0OO =O0OOO0O0O000OOOOO .read ()#line:262
         O0OOO0O0O000OOOOO .close ()#line:263
         return 'uwspversietxtrpi','[COLOR gray]'+OOOO00000OOO0O0OO +'[/COLOR]'#line:264
    else :#line:265
        return 'unknown',''#line:266
def checkXvbmcversie ():#line:268
    if os .path .isfile (bldversietxt ):#line:269
       O0O0OO0000OOOO0OO =open (bldversietxt ,'r')#line:270
       OOOOOOOO00OOOO0OO =O0O0OO0000OOOO0OO .read ()#line:271
       O0O0OO0000OOOO0OO .close ()#line:272
       return 'bldversietxt','[COLOR gray]'+OOOOOOOO00OOOO0OO +'[/COLOR]'#line:273
    elif os .path .isfile (bldversietxtwiz ):#line:274
         O0O0OO0000OOOO0OO =open (bldversietxtwiz ,'r')#line:275
         OOO00O0O0O0O000OO =O0O0OO0000OOOO0OO .read ()#line:276
         O0O0OO0000OOOO0OO .close ()#line:277
         return 'bldversietxtwiz','[COLOR gray]'+OOO00O0O0O0O000OO +'[/COLOR]'#line:278
    else :#line:279
        return 'unknown',''#line:280
def removefolder (map ,exclude =None ):#line:287
    for O00OOO000O00OOO00 ,O0O0OOO00OO0O0000 ,OO0OOOO0OO0OO00O0 in os .walk (map ,topdown =False ):#line:288
        for OO0O00OOOOO0O0000 in OO0OOOO0OO0OO00O0 :#line:289
            if (O00OOO000O00OOO00 .find (exclude )>0 ):#line:290
               continue #line:291
            try :os .remove (os .path .join (O00OOO000O00OOO00 ,OO0O00OOOOO0O0000 ))#line:292
            except :pass #line:293
        for OO0O00OOOOO0O0000 in O0O0OOO00OO0O0000 :#line:294
            if (OO0O00OOOOO0O0000 ==exclude ):#line:295
               continue #line:296
            try :os .rmdir (os .path .join (O00OOO000O00OOO00 ,OO0O00OOOOO0O0000 ))#line:297
            except :pass #line:298
def REMOVE_EMPTY_FOLDERS ():#line:300
    log ("########### Start Removing Empty Folders #########")#line:302
    O0O0OOOOOOO000O0O =0 #line:303
    OO0OOOOO000OO0OO0 =0 #line:304
    for OOOO00O000OO0OO00 ,OO0O0OO0O0000O000 ,O00000OOOO0O00OO0 in os .walk (HOME ):#line:305
        if len (OO0O0OO0O0000O000 )==0 and len (O00000OOOO0O00OO0 )==0 :#line:306
           O0O0OOOOOOO000O0O +=1 #line:307
           os .rmdir (OOOO00O000OO0OO00 )#line:308
           log ("successfully removed: "+OOOO00O000OO0OO00 )#line:309
        elif len (OO0O0OO0O0000O000 )>0 and len (O00000OOOO0O00OO0 )>0 :#line:310
             OO0OOOOO000OO0OO0 +=1 #line:311
def TextBoxes (announce ):#line:318
    class OO0OO00000OO0O0O0 ():#line:319
        WINDOW =10147 #line:320
        CONTROL_LABEL =1 #line:321
        CONTROL_TEXTBOX =5 #line:322
        def __init__ (self ,*OO000OOO0O0OOO00O ,**OOO000OO00OOOOOO0 ):#line:323
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:324
            self .win =xbmcgui .Window (self .WINDOW )#line:325
            xbmc .sleep (500 )#line:326
            self .setControls ()#line:327
        def setControls (self ):#line:328
            self .win .getControl (self .CONTROL_LABEL ).setLabel ('XvBMC - View Log[B]:[/B]')#line:329
            try :OOOO0O000OO0OOOO0 =open (announce );OOO0OO00O000O0OOO =OOOO0O000OO0OOOO0 .read ()#line:330
            except :OOO0OO00O000O0OOO =announce #line:331
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (OOO0OO00O000O0OOO ))#line:332
            return #line:333
    OO0OO00000OO0O0O0 ()#line:334
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:335
          time .sleep (.5 )#line:336
def TextBoxesPlain (heading ,announce ):#line:338
    class O0OO0O0000O0O0OOO ():#line:339
        WINDOW =10147 #line:340
        CONTROL_LABEL =1 #line:341
        CONTROL_TEXTBOX =5 #line:342
        def __init__ (self ,*O00000OOO00O00OO0 ,**O0OOO0OOO0O0000OO ):#line:343
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:344
            self .win =xbmcgui .Window (self .WINDOW )#line:345
            xbmc .sleep (500 )#line:346
            self .setControls ()#line:347
        def setControls (self ):#line:348
            self .win .getControl (self .CONTROL_LABEL ).setLabel (heading )#line:349
            try :O0OO0OO0O000OO00O =open (announce );OO00OOO000OOOO00O =O0OO0OO0O000OO00O .read ()#line:350
            except :OO00OOO000OOOO00O =announce #line:351
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (OO00OOO000OOOO00O ))#line:352
            return #line:353
    O0OO0O0000O0O0OOO ()#line:354
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:355
          time .sleep (.5 )#line:356
def facebook ():#line:358
    TextBoxesPlain ('XvBMC Nederland','[COLOR=red]NOTE:[/COLOR]\nXvBMC Nederland (xbmc nl) wij zijn geen helpdesk van/voor boxverkopers\n\nVoor meer informatie kijk op https://bit.ly/XvBMC-NL')#line:359
def AboutXvBMC ():#line:366
    O00OO0OO000000O0O =''#line:367
    OOO0000000OO00000 ='https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/readme.xml'#line:368
    O0OO0OOOOOO0O00OO =urllib2 .Request (OOO0000000OO00000 )#line:369
    O0OO0OOOOOO0O00OO .add_header ('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')#line:370
    OO0OO0000O0O0O0OO =urllib2 .urlopen (O0OO0OOOOOO0O00OO )#line:371
    O00000O00OOO00OO0 =OO0OO0000O0O0O0OO .read ()#line:372
    OO0OO0000O0O0O0OO .close ()#line:373
    OOO000O00OO00000O =re .compile ("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re .DOTALL ).findall (O00000O00OOO00OO0 )#line:374
    for OOOOOOO0OOOO00OO0 ,OO0O0OOOO000000O0 in OOO000O00OO00000O :#line:375
        try :#line:376
                OOOOOOO0OOOO00OO0 =OOOOOOO0OOOO00OO0 .decode ('ascii','ignore')#line:377
        except :#line:378
                OOOOOOO0OOOO00OO0 =OOOOOOO0OOOO00OO0 .decode ('utf-8','ignore')#line:379
        OO0O0OOOO000000O0 =OO0O0OOOO000000O0 [:-15 ]#line:380
        OOOOOOO0OOOO00OO0 =OOOOOOO0OOOO00OO0 .replace ('&amp;','')#line:381
        OO0O0OOOO000000O0 ='[COLOR lime][B]'+OO0O0OOOO000000O0 +'[/B][/COLOR]'#line:382
        O00OO0OO000000O0O =O00OO0OO000000O0O +OO0O0OOOO000000O0 +'\n'+OOOOOOO0OOOO00OO0 +'\n'+'\n'#line:383
    infoTXT ('[COLOR lime]Usage policy & Disclaimer [B]X[/B]v[B]BMC-[/B]NL[/COLOR]',O00OO0OO000000O0O )#line:384
def infoTXT (heading ,text ):#line:386
    O0000000OO0O00OOO =10147 #line:387
    xbmc .executebuiltin ('ActivateWindow(%d)'%O0000000OO0O00OOO )#line:388
    xbmc .sleep (100 )#line:389
    O0000O0O00OOOOO00 =xbmcgui .Window (O0000000OO0O00OOO )#line:390
    O00O0O0O00O0O0O0O =50 #line:391
    while (O00O0O0O00O0O0O0O >0 ):#line:392
        try :#line:393
            xbmc .sleep (10 )#line:394
            O00O0O0O00O0O0O0O -=1 #line:395
            O0000O0O00OOOOO00 .getControl (1 ).setLabel (heading )#line:396
            O0000O0O00OOOOO00 .getControl (5 ).setText (text )#line:397
            return #line:398
        except :#line:399
            pass #line:400
artwork =xbmc .translatePath (os .path .join ('special://home','addons',AddonID ,'/'))#line:407
fanart =artwork +'fanart.jpg'#line:408
def addonIcon ():#line:411
    return artwork +'icon.png'#line:412
def message (text1 ,text2 ="",text3 =""):#line:415
    if text3 =="":#line:416
       xbmcgui .Dialog ().ok (text1 ,text2 )#line:417
    elif text2 =="":#line:418
         xbmcgui .Dialog ().ok ("",text1 )#line:419
    else :#line:420
        xbmcgui .Dialog ().ok (text1 ,text2 ,text3 )#line:421
def message_yes_no (text1 ,text2 ="",text3 =""):#line:423
    if text3 =="":OOOOO00O000000OOO =xbmcgui .Dialog ().yesno (text1 ,text2 )#line:424
    elif text2 =="":OOOOO00O000000OOO =xbmcgui .Dialog ().yesno ("",text1 )#line:425
    else :OOOOO00O000000OOO =xbmcgui .Dialog ().yesno (text1 ,text2 ,text3 )#line:426
    return OOOOO00O000000OOO #line:427
def infoDialog (message ,heading =addonInfo ('name'),icon =addonIcon (),time =3000 ):#line:430
    try :#line:431
        dialog .notification (heading ,message ,icon ,time ,sound =False )#line:432
    except :#line:433
        execute ("Notification(%s,%s, %s, %s)"%(heading ,message ,time ,icon ))#line:434
def okDialog (line1 ,line2 ,line3 ,heading =addonInfo ('name')):#line:437
    return dialog .ok (heading ,line1 ,line2 ,line3 )#line:438
def yesnoDialog (line1 ,line2 ,line3 ,heading =addonInfo ('name'),nolabel ='',yeslabel =''):#line:440
    return dialog .yesno (heading ,line1 ,line2 ,line3 ,nolabel ,yeslabel )#line:441
def log (msg ,level =xbmc .LOGNOTICE ):#line:448
    OO0O000000OO00000 ='XvBMC_NOTICE'#line:449
    level =xbmc .LOGNOTICE #line:451
    try :#line:460
        xbmc .log ('%s: %s'%(OO0O000000OO00000 ,msg ),level )#line:461
    except :#line:462
        try :#line:463
            xbmc .log ('Logging Failure',level )#line:464
        except :#line:465
            pass #line:466
def forceRefresh (melding =None ):#line:469
    xbmc .executebuiltin ('UpdateLocalAddons()');log ("XvBMC_UpdateLocalAddons()")#line:470
    time .sleep (0.5 )#line:471
    xbmc .executebuiltin ('UpdateAddonRepos()');log ("XvBMC_UpdateAddonRepos()")#line:472
    time .sleep (0.5 )#line:473
    if melding :#line:474
       dialog .ok (MainTitle ,'Force Refresh Repos and Update LocalAddons')#line:475
       try :#line:476
           xbmc .executebuiltin ('ReloadSkin()');log ("XvBMC_ReloadSkin()")#line:477
       except :pass #line:478
       try :#line:479
           xbmc .executebuiltin ('Container.Refresh');log ("Container.Refresh")#line:480
       except :pass #line:481
def get_kversion ():#line:484
    O0O00O0O000000O00 =xbmc .getInfoLabel ('System.BuildVersion')#line:485
    OOOO00OOO00O00O0O =O0O00O0O000000O00 .split (".")#line:486
    O00000000OOOOO000 =int (OOOO00OOO00O00O0O [0 ])#line:487
    return O00000000OOOOO000 #line:492
def setView (content ,viewType ):#line:495
    if content :#line:497
       xbmcplugin .setContent (int (sys .argv [1 ]),content )#line:498
    if ADDON .getSetting ('auto-view')=='true':#line:499
       xbmc .executebuiltin ("Container.SetViewMode(%s)"%ADDON .getSetting (viewType ))#line:500
def closeandexit ():#line:507
    xbmc .executebuiltin ('Action(back)')#line:509
"""
    IF you copy/paste 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
