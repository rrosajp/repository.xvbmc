#!/usr/bin/python
"""
    IF you copy/paste XvBMC's -common.py- please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
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
currentbldtxtwiz =base64 .b64decode (basewiz )+'wizbld.txt'#line:57
currentsptxtwiz =base64 .b64decode (basewiz )+'wizsp.txt'#line:58
uwspversietxt =xbmc .translatePath (os .path .join ('special://home/userdata','versiesp.txt'))#line:59
uwspversietxtwiz =xbmc .translatePath (os .path .join ('special://home/userdata','wizsp.txt'))#line:60
def killKodi ():#line:66
    OOOOO0000O0O00OOO =platform ()#line:72
    log ("XvBMC_Platform: "+str (OOOOO0000O0O00OOO ))#line:73
    try :os ._exit (1 )#line:74
    except :pass #line:75
    if OOOOO0000O0O00OOO =='osx':#line:76
        log ("############   try osx force close  #################")#line:77
        try :os .system ('killall -9 XBMC')#line:78
        except :pass #line:79
        try :os .system ('killall -9 Kodi')#line:80
        except :pass #line:81
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:82
        try :xbmc .executebuiltin ("Reboot")#line:83
        except :pass #line:84
    elif OOOOO0000O0O00OOO =='linux':#line:85
        log ("############   try linux force close  #################")#line:86
        try :os .system ('killall XBMC')#line:89
        except :pass #line:90
        try :os .system ('killall Kodi')#line:91
        except :pass #line:92
        try :os .system ('killall -9 xbmc.bin')#line:93
        except :pass #line:94
        try :os .system ('killall -9 kodi.bin')#line:95
        except :pass #line:96
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:97
        try :xbmc .executebuiltin ("Reboot")#line:98
        except :pass #line:99
    elif OOOOO0000O0O00OOO =='android':#line:100
        log ("############   try android force close  #################")#line:101
        try :os .system ('adb shell am force-stop com.jesusboxmedia')#line:102
        except :pass #line:103
        try :os .system ('adb shell am force-stop com.perfectzoneproductions.jesusboxmedia')#line:104
        except :pass #line:105
        try :os .system ('adb shell am force-stop com.semperpax.spmc')#line:106
        except :pass #line:107
        try :os .system ('adb shell am force-stop com.semperpax.spmc16')#line:108
        except :pass #line:109
        try :os .system ('adb shell am force-stop com.spmc')#line:110
        except :pass #line:111
        try :os .system ('adb shell am force-stop com.spmc16')#line:112
        except :pass #line:113
        try :os .system ('adb shell am force-stop org.kodi')#line:114
        except :pass #line:115
        try :os .system ('adb shell am force-stop org.lodi.mobi')#line:116
        except :pass #line:117
        try :os .system ('adb shell am force-stop org.xbmc')#line:118
        except :pass #line:119
        try :os .system ('adb shell am force-stop org.xbmc.cemc')#line:120
        except :pass #line:121
        try :os .system ('adb shell am force-stop org.xbmc.cemc_pro')#line:122
        except :pass #line:123
        try :os .system ('adb shell am force-stop org.xbmc.kodi')#line:124
        except :pass #line:125
        try :os .system ('adb shell am force-stop org.xbmc.xbmc')#line:126
        except :pass #line:127
        try :os .system ('adb shell am force-stop uk.dbmc')#line:128
        except :pass #line:129
        try :os .system ('adb shell am force-stop uk.droidbox.dbmc')#line:130
        except :pass #line:131
        try :os .system ('adb shell kill com.perfectzoneproductions.jesusboxmedia')#line:132
        except :pass #line:133
        try :os .system ('adb shell kill com.semperpax')#line:134
        except :pass #line:135
        try :os .system ('adb shell kill com.semperpax.spmc16')#line:136
        except :pass #line:137
        try :os .system ('adb shell kill org.kodi')#line:138
        except :pass #line:139
        try :os .system ('adb shell kill org.lodi.mobi')#line:140
        except :pass #line:141
        try :os .system ('adb shell kill org.xbmc')#line:142
        except :pass #line:143
        try :os .system ('adb shell kill org.xbmc.cemc')#line:144
        except :pass #line:145
        try :os .system ('adb shell kill org.xbmc.cemc_pro')#line:146
        except :pass #line:147
        try :os .system ('adb shell kill org.xbmc.kodi')#line:148
        except :pass #line:149
        try :os .system ('adb shell kill org.xbmc.xbmc')#line:150
        except :pass #line:151
        try :os .system ('Process.killProcess(android.os.Process.com.semperpax.spmc16());')#line:152
        except :pass #line:153
        try :os .system ('Process.killProcess(android.os.Process.org.fire());')#line:154
        except :pass #line:155
        try :os .system ('Process.killProcess(android.os.Process.org.fire.guru());')#line:156
        except :pass #line:157
        try :os .system ('Process.killProcess(android.os.Process.org.fire.guruv());')#line:158
        except :pass #line:159
        try :os .system ('Process.killProcess(android.os.Process.org.kodi());')#line:160
        except :pass #line:161
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc());')#line:162
        except :pass #line:163
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc.kodi());')#line:164
        except :pass #line:165
        try :os .system ('Process.killProcess(android.os.Process.org.xbmc.xbmc());')#line:166
        except :pass #line:167
        dialog .ok (waarschuwing ,'Your system has been detected as Android, you ','[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Either close using Task Manager (If unsure pull the plug).')#line:168
        try :xbmc .executebuiltin ("Reboot")#line:169
        except :pass #line:170
    elif OOOOO0000O0O00OOO =='windows':#line:171
        log ("############   try windows force close  #################")#line:172
        try :#line:173
            os .system ('@ECHO off')#line:174
            os .system ('tskill XBMC.exe')#line:175
        except :pass #line:176
        try :#line:177
            os .system ('@ECHO off')#line:178
            os .system ('tskill Kodi.exe')#line:179
        except :pass #line:180
        try :#line:181
            os .system ('@ECHO off')#line:182
            os .system ('tskill SMC.exe')#line:183
        except :pass #line:184
        try :#line:185
            os .system ('@ECHO off')#line:186
            os .system ('TASKKILL /im Kodi.exe /f')#line:187
        except :pass #line:188
        try :#line:189
            os .system ('@ECHO off')#line:190
            os .system ('TASKKILL /im XBMC.exe /f')#line:191
        except :pass #line:192
        try :#line:193
            os .system ('@ECHO off')#line:194
            os .system ('TASKKILL /im XBMC.exe /f')#line:195
        except :pass #line:196
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Use task manager and NOT ALT F4')#line:197
    else :#line:198
        log ("############   try atv force close  #################")#line:199
        try :os .system ('killall AppleTV')#line:200
        except :pass #line:201
        log ("############   try raspbmc force close  #################")#line:202
        try :os .system ('sudo initctl stop kodi')#line:203
        except :pass #line:204
        try :os .system ('sudo initctl stop xbmc')#line:205
        except :pass #line:206
        dialog .ok (waarschuwing ,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.','(trying \'reboot\' after OK, else pull power cable.)')#line:207
        try :xbmc .executebuiltin ("Reboot")#line:208
        except :pass #line:209
def platform ():#line:216
    if xbmc .getCondVisibility ('system.platform.android'):return 'android'#line:217
    elif xbmc .getCondVisibility ('system.platform.linux'):return 'linux'#line:218
    elif xbmc .getCondVisibility ('system.platform.windows'):return 'windows'#line:219
    elif xbmc .getCondVisibility ('system.platform.osx'):return 'osx'#line:220
    elif xbmc .getCondVisibility ('system.platform.atv2'):return 'atv2'#line:221
    elif xbmc .getCondVisibility ('system.platform.ios'):return 'ios'#line:222
def verifyplatform ():#line:224
    OOOO00OO000000OO0 =platform ()#line:225
    log ("XvBMC_Platform: "+str (OOOO00OO000000OO0 ))#line:226
    if OOOO00OO000000OO0 =='osx':#line:227
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees for OSX [B];-p[/B]')#line:228
        log ("=== OSX ===")#line:229
    elif OOOO00OO000000OO0 =='linux':#line:230
        log ("=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ===")#line:232
    elif OOOO00OO000000OO0 =='android':#line:233
        dialog .ok ('[COLOR=red][B]!!!  IMPORTANT  !!![/COLOR][/B]','[COLOR=lime]There\'s also a specific XvBMC\'s Android add-on update(r)[/COLOR]','...enkel voor specifieke bonus Android add-on updates...',noservicepack +' '+notforked )#line:234
        log ("=== Android ===")#line:235
    elif OOOO00OO000000OO0 =='windows':#line:236
        log ("=== Download de laatste XvBMC (Windows) ServicePack ===")#line:238
    else :#line:239
        dialog .ok (waarschuwing ,readme ,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees though [B];-p[/B]')#line:240
        log ("=== ATV2/iOS/OSMC/Raspbmc/etc ===")#line:241
def KODIVERSION (url ):O0OO0O0O0OO0OOOOO =xbmc .getInfoLabel ("System.BuildVersion");OO0O00O0OOO0O0O00 =O0OO0O0O0OO0OOOOO [:4 ];log ("XvBMC_v"+OO0O00O0OOO0O0O00 );dialog .ok (MainTitle ,'Your Kodi Version : [COLOR lime][B]%s[/B][/COLOR]'%OO0O00O0OOO0O0O00 )#line:244
def checkSPversie ():#line:247
    if os .path .isfile (uwspversietxt ):#line:248
       OO00O00OOOO0OO000 =open (uwspversietxt ,'r')#line:249
       OO0OO0OOO00O0OOOO =OO00O00OOOO0OO000 .read ()#line:250
       OO00O00OOOO0OO000 .close ()#line:251
       return 'uwspversietxt','[COLOR gray]'+OO0OO0OOO00O0OOOO +'[/COLOR]'#line:252
    elif os .path .isfile (uwspversietxtwiz ):#line:253
         OO00O00OOOO0OO000 =open (uwspversietxtwiz ,'r')#line:254
         OOO0O0O0OOOO00O0O =OO00O00OOOO0OO000 .read ()#line:255
         OO00O00OOOO0OO000 .close ()#line:256
         return 'uwspversietxtwiz','[COLOR gray]'+OOO0O0O0OOOO00O0O +'[/COLOR]'#line:257
    else :#line:258
        return 'unknown',''#line:259
def checkXvbmcversie ():#line:261
    if os .path .isfile (bldversietxt ):#line:262
       O00O0OOOOO0OOOO0O =open (bldversietxt ,'r')#line:263
       OOOO0OOO0O0OO000O =O00O0OOOOO0OOOO0O .read ()#line:264
       O00O0OOOOO0OOOO0O .close ()#line:265
       return 'bldversietxt','[COLOR gray]'+OOOO0OOO0O0OO000O +'[/COLOR]'#line:266
    elif os .path .isfile (bldversietxtwiz ):#line:267
         O00O0OOOOO0OOOO0O =open (bldversietxtwiz ,'r')#line:268
         OOO0OOO0O0OOO0000 =O00O0OOOOO0OOOO0O .read ()#line:269
         O00O0OOOOO0OOOO0O .close ()#line:270
         return 'bldversietxtwiz','[COLOR gray]'+OOO0OOO0O0OOO0000 +'[/COLOR]'#line:271
    else :#line:272
        return 'unknown',''#line:273
def removefolder (map ,exclude =None ):#line:280
    for O000OO0OO000OO000 ,O0O00O0OO00OOO000 ,O00000OO00O0O000O in os .walk (map ,topdown =False ):#line:281
        for O00O0O0OO000O0OOO in O00000OO00O0O000O :#line:282
            if (O000OO0OO000OO000 .find (exclude )>0 ):#line:283
               continue #line:284
            try :os .remove (os .path .join (O000OO0OO000OO000 ,O00O0O0OO000O0OOO ))#line:285
            except :pass #line:286
        for O00O0O0OO000O0OOO in O0O00O0OO00OOO000 :#line:287
            if (O00O0O0OO000O0OOO ==exclude ):#line:288
               continue #line:289
            try :os .rmdir (os .path .join (O000OO0OO000OO000 ,O00O0O0OO000O0OOO ))#line:290
            except :pass #line:291
def REMOVE_EMPTY_FOLDERS ():#line:293
    log ("########### Start Removing Empty Folders #########")#line:295
    OOO0O000O0O00OOOO =0 #line:296
    OO00O0000O0OO000O =0 #line:297
    for O0OO0OO0000OOOOO0 ,OOOO000OOOO0O000O ,OO0OOOOO00O000O0O in os .walk (HOME ):#line:298
        if len (OOOO000OOOO0O000O )==0 and len (OO0OOOOO00O000O0O )==0 :#line:299
           OOO0O000O0O00OOOO +=1 #line:300
           os .rmdir (O0OO0OO0000OOOOO0 )#line:301
           log ("successfully removed: "+O0OO0OO0000OOOOO0 )#line:302
        elif len (OOOO000OOOO0O000O )>0 and len (OO0OOOOO00O000O0O )>0 :#line:303
             OO00O0000O0OO000O +=1 #line:304
def TextBoxes (announce ):#line:311
    class O00O0OOOO0O0OO0O0 ():#line:312
        WINDOW =10147 #line:313
        CONTROL_LABEL =1 #line:314
        CONTROL_TEXTBOX =5 #line:315
        def __init__ (self ,*O000O00OOOO0O0OO0 ,**O0O00OOOOO0O0OO00 ):#line:316
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:317
            self .win =xbmcgui .Window (self .WINDOW )#line:318
            xbmc .sleep (500 )#line:319
            self .setControls ()#line:320
        def setControls (self ):#line:321
            self .win .getControl (self .CONTROL_LABEL ).setLabel ('XvBMC - View Log[B]:[/B]')#line:322
            try :OO0000000O0OOOOOO =open (announce );O0000OOO000OO0OOO =OO0000000O0OOOOOO .read ()#line:323
            except :O0000OOO000OO0OOO =announce #line:324
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (O0000OOO000OO0OOO ))#line:325
            return #line:326
    O00O0OOOO0O0OO0O0 ()#line:327
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:328
          time .sleep (.5 )#line:329
def TextBoxesPlain (heading ,announce ):#line:331
    class OO0OOO00O00O00O00 ():#line:332
        WINDOW =10147 #line:333
        CONTROL_LABEL =1 #line:334
        CONTROL_TEXTBOX =5 #line:335
        def __init__ (self ,*OOO0O0OOOOOO000O0 ,**OOOOO0O0O00O0O0OO ):#line:336
            xbmc .executebuiltin ("ActivateWindow(%d)"%(self .WINDOW ,))#line:337
            self .win =xbmcgui .Window (self .WINDOW )#line:338
            xbmc .sleep (500 )#line:339
            self .setControls ()#line:340
        def setControls (self ):#line:341
            self .win .getControl (self .CONTROL_LABEL ).setLabel (heading )#line:342
            try :O0O00O0OOO000O0O0 =open (announce );O00OOO000000O000O =O0O00O0OOO000O0O0 .read ()#line:343
            except :O00OOO000000O000O =announce #line:344
            self .win .getControl (self .CONTROL_TEXTBOX ).setText (str (O00OOO000000O000O ))#line:345
            return #line:346
    OO0OOO00O00O00O00 ()#line:347
    while xbmc .getCondVisibility ('Window.IsVisible(10147)'):#line:348
          time .sleep (.5 )#line:349
def facebook ():#line:351
    TextBoxesPlain ('XvBMC Nederland','[COLOR=red]NOTE:[/COLOR]\nXvBMC Nederland (xbmc nl) wij zijn geen helpdesk van/voor boxverkopers\n\nVoor meer informatie kijk op https://bit.ly/XvBMC-NL')#line:352
def AboutXvBMC ():#line:359
    OO0OOOOO0O00O00OO =''#line:360
    OOO0O0OOO0O0OOOO0 ='https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/readme.xml'#line:361
    O0O000000OO000OOO =urllib2 .Request (OOO0O0OOO0O0OOOO0 )#line:362
    O0O000000OO000OOO .add_header ('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')#line:363
    O0O0O000OOOO00O00 =urllib2 .urlopen (O0O000000OO000OOO )#line:364
    O0O0O0OOO00OO0000 =O0O0O000OOOO00O00 .read ()#line:365
    O0O0O000OOOO00O00 .close ()#line:366
    OO000O0O0OO000O00 =re .compile ("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re .DOTALL ).findall (O0O0O0OOO00OO0000 )#line:367
    for O0OO00OO00000O000 ,OOOOOO00O00OO0OOO in OO000O0O0OO000O00 :#line:368
        try :#line:369
                O0OO00OO00000O000 =O0OO00OO00000O000 .decode ('ascii','ignore')#line:370
        except :#line:371
                O0OO00OO00000O000 =O0OO00OO00000O000 .decode ('utf-8','ignore')#line:372
        OOOOOO00O00OO0OOO =OOOOOO00O00OO0OOO [:-15 ]#line:373
        O0OO00OO00000O000 =O0OO00OO00000O000 .replace ('&amp;','')#line:374
        OOOOOO00O00OO0OOO ='[COLOR lime][B]'+OOOOOO00O00OO0OOO +'[/B][/COLOR]'#line:375
        OO0OOOOO0O00O00OO =OO0OOOOO0O00O00OO +OOOOOO00O00OO0OOO +'\n'+O0OO00OO00000O000 +'\n'+'\n'#line:376
    infoTXT ('[COLOR lime]Usage policy & Disclaimer [B]X[/B]v[B]BMC-[/B]NL[/COLOR]',OO0OOOOO0O00O00OO )#line:377
def infoTXT (heading ,text ):#line:379
    OOOOO0OOO0O0O000O =10147 #line:380
    xbmc .executebuiltin ('ActivateWindow(%d)'%OOOOO0OOO0O0O000O )#line:381
    xbmc .sleep (100 )#line:382
    O0OOO0O00O00O00O0 =xbmcgui .Window (OOOOO0OOO0O0O000O )#line:383
    O0OOOOO000O0OOO0O =50 #line:384
    while (O0OOOOO000O0OOO0O >0 ):#line:385
        try :#line:386
            xbmc .sleep (10 )#line:387
            O0OOOOO000O0OOO0O -=1 #line:388
            O0OOO0O00O00O00O0 .getControl (1 ).setLabel (heading )#line:389
            O0OOO0O00O00O00O0 .getControl (5 ).setText (text )#line:390
            return #line:391
        except :#line:392
            pass #line:393
artwork =xbmc .translatePath (os .path .join ('special://home','addons',AddonID ,'/'))#line:400
fanart =artwork +'fanart.jpg'#line:401
def addonIcon ():#line:404
    return artwork +'icon.png'#line:405
def message (text1 ,text2 ="",text3 =""):#line:408
    if text3 =="":#line:409
       xbmcgui .Dialog ().ok (text1 ,text2 )#line:410
    elif text2 =="":#line:411
         xbmcgui .Dialog ().ok ("",text1 )#line:412
    else :#line:413
        xbmcgui .Dialog ().ok (text1 ,text2 ,text3 )#line:414
def message_yes_no (text1 ,text2 ="",text3 =""):#line:416
    if text3 =="":O0O000O0OO00O000O =xbmcgui .Dialog ().yesno (text1 ,text2 )#line:417
    elif text2 =="":O0O000O0OO00O000O =xbmcgui .Dialog ().yesno ("",text1 )#line:418
    else :O0O000O0OO00O000O =xbmcgui .Dialog ().yesno (text1 ,text2 ,text3 )#line:419
    return O0O000O0OO00O000O #line:420
def infoDialog (message ,heading =addonInfo ('name'),icon =addonIcon (),time =3000 ):#line:423
    try :#line:424
        dialog .notification (heading ,message ,icon ,time ,sound =False )#line:425
    except :#line:426
        execute ("Notification(%s,%s, %s, %s)"%(heading ,message ,time ,icon ))#line:427
def okDialog (line1 ,line2 ,line3 ,heading =addonInfo ('name')):#line:430
    return dialog .ok (heading ,line1 ,line2 ,line3 )#line:431
def yesnoDialog (line1 ,line2 ,line3 ,heading =addonInfo ('name'),nolabel ='',yeslabel =''):#line:433
    return dialog .yesno (heading ,line1 ,line2 ,line3 ,nolabel ,yeslabel )#line:434
def log (msg ,level =xbmc .LOGNOTICE ):#line:441
    OO000O0OO0O0OO000 ='XvBMC_NOTICE'#line:442
    level =xbmc .LOGNOTICE #line:444
    try :#line:453
        xbmc .log ('%s: %s'%(OO000O0OO0O0OO000 ,msg ),level )#line:454
    except :#line:455
        try :#line:456
            xbmc .log ('Logging Failure',level )#line:457
        except :#line:458
            pass #line:459
def forceRefresh (melding =None ):#line:462
    xbmc .executebuiltin ('UpdateLocalAddons()');log ("XvBMC_UpdateLocalAddons()")#line:463
    time .sleep (0.5 )#line:464
    xbmc .executebuiltin ('UpdateAddonRepos()');log ("XvBMC_UpdateAddonRepos()")#line:465
    time .sleep (0.5 )#line:466
    if melding :#line:467
       dialog .ok (MainTitle ,'Force Refresh Repos and Update LocalAddons')#line:468
       try :#line:469
           xbmc .executebuiltin ('ReloadSkin()');log ("XvBMC_ReloadSkin()")#line:470
       except :pass #line:471
       try :#line:472
           xbmc .executebuiltin ('Container.Refresh');log ("Container.Refresh")#line:473
       except :pass #line:474
def get_kversion ():#line:477
    O000OOOO0O0O0O000 =xbmc .getInfoLabel ('System.BuildVersion')#line:478
    O0OO0000O0O00OOOO =O000OOOO0O0O0O000 .split (".")#line:479
    OO0O0OOOOOO00O0O0 =int (O0OO0000O0O00OOOO [0 ])#line:480
    return OO0O0OOOOOO00O0O0 #line:485
def setView (content ,viewType ):#line:488
    if content :#line:490
       xbmcplugin .setContent (int (sys .argv [1 ]),content )#line:491
    if ADDON .getSetting ('auto-view')=='true':#line:492
       xbmc .executebuiltin ("Container.SetViewMode(%s)"%ADDON .getSetting (viewType ))#line:493
def closeandexit ():#line:500
    xbmc .executebuiltin ('Action(back)')#line:502
"""
    IF you copy/paste 'common.py' please keep the credits -2- EPiC -4- XvBMC-NL, Thx.
"""