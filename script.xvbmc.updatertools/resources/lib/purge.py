#!/usr/bin/python
""#line:6
import xbmc as O000O0000O00O0O0O ,xbmcaddon as O000O00OOO000OO0O ,xbmcgui as OO00000O0OO00O00O ,xbmcplugin as OOO0OO0000O00000O ,xbmcvfs as O000OO0OO0OOOO0O0 #line:26
import os as OO000000O000OO0OO ,re as OO0OO00OOOO00OOO0 ,base64 as O00O000OO000000O0 ,sys as OO000000O0OOO0OO0 ,shutil as O0O00OO0O000OO0O0 #line:27
import common as OOOOOOOOO000O00O0 #line:28
AddonID ='script.xvbmc.updatertools'#line:31
ADDON =O000O00OOO000OO0O .Addon (id =AddonID )#line:32
dialog =OO00000O0OO00O00O .Dialog ()#line:34
class cacheEntry :#line:40
    def __init__ (self ,namei ,pathi ):#line:41
        self .name =namei #line:42
        self .path =pathi #line:43
def setupXvbmcEntries ():#line:50
    OOOO00O000OO0000O =16 #line:51
    OOO0OO000O00OO0OO =["jehrico","kidsplace","nlview","nl-viewer","nl-viewer2","nlv3","sportcenterhd","troma-copypaste","jehricorepo","nlviewrepo","doki","xodi","kijk","adelaar","geentv","tvad"]#line:52
    OO00OOOO0000OO00O =["special://home/addons/"+"plugin.video.jericho","special://home/addons/"+"plugin.video.kidsplace","special://home/addons/"+"plugin.video.NLVIEW","special://home/addons/"+"plugin.video.nl-viewer","special://home/addons/"+"plugin.video.nl-viewer2","special://home/addons/"+"plugin.video.nlv3","special://home/addons/"+"plugin.video.sportcenterhd","special://home/addons/"+"plugin.video.troma","special://home/addons/"+"repository.jericho","special://home/addons/"+"repository.NLVIEW","special://home/addons/"+"repository.dokinl","special://home/addons/"+"repository.x-odi.nl","special://home/addons/"+"repository.kijkalles.nl","special://home/addons/"+"repository.eagle","special://home/addons/"+"repository.ditistv","special://home/addons/"+"repository.tvaddons.nl"]#line:69
    O0O0OOOOO0OO0O000 =[]#line:71
    for O0OO00OO000OO000O in range (OOOO00O000OO0000O ):#line:73
        O0O0OOOOO0OO0O000 .append (cacheEntry (OOO0OO000O00OO0OO [O0OO00OO000OO000O ],OO00OOOO0000OO00O [O0OO00OO000OO000O ]))#line:74
    return O0O0OOOOO0OO0O000 #line:76
def purgeOLD ():#line:83
    OO00OOOOO0OO0000O =setupXvbmcEntries ()#line:98
    for O00OOOOO0O0OOOOO0 in OO00OOOOO0OO0000O :#line:100
        OO000O0OO00O0000O =O000O0000O00O0O0O .translatePath (O00OOOOO0O0OOOOO0 .path )#line:101
        if OO000000O000OO0OO .path .exists (OO000O0OO00O0000O )==True :#line:102
            for O0O0OO0OO0000OO0O ,O0O00O00OO000OOOO ,OO00O0O00OOO00O00 in OO000000O000OO0OO .walk (OO000O0OO00O0000O ):#line:103
                if len (O0O00O00OO000OOOO )>0 and len (OO00O0O00OOO00O00 )>0 :#line:109
                    for OOOOOO0O00O0O00OO in OO00O0O00OOO00O00 :#line:110
                        try :#line:111
                            OO000000O000OO0OO .unlink (OO000000O000OO0OO .path .join (O0O0OO0OO0000OO0O ,OOOOOO0O00O0O00OO ))#line:112
                        except :pass #line:113
                    for O0O0O00000OOOOOOO in O0O00O00OO000OOOO :#line:114
                        try :#line:115
                            O0O00OO0O000OO0O0 .rmtree (OO000000O000OO0OO .path .join (O0O0OO0OO0000OO0O ,O0O0O00000OOOOOOO ))#line:116
                        except OSError :#line:117
                            O0O00OO0O000OO0O0 .rmtree (OO000O0OO00O0000O ,ignore_errors =True )#line:118
                        else :#line:119
                            O0O00OO0O000OO0O0 .rmtree (OO000O0OO00O0000O ,ignore_errors =True )#line:120
                            pass #line:121
                elif len (O0O00O00OO000OOOO )==0 and len (OO00O0O00OOO00O00 )==0 :#line:123
                    for OOOOOO0O00O0O00OO in OO00O0O00OOO00O00 :#line:127
                        try :#line:128
                            OO000000O000OO0OO .unlink (OO000000O000OO0OO .path .join (O0O0OO0OO0000OO0O ,OOOOOO0O00O0O00OO ))#line:129
                        except :pass #line:130
                    for O0O0O00000OOOOOOO in O0O00O00OO000OOOO :#line:131
                        try :#line:132
                            O0O00OO0O000OO0O0 .rmtree (OO000000O000OO0OO .path .join (O0O0OO0OO0000OO0O ,O0O0O00000OOOOOOO ))#line:133
                        except OSError :#line:134
                            O0O00OO0O000OO0O0 .rmtree (OO000O0OO00O0000O ,ignore_errors =True )#line:135
                        else :#line:136
                            O0O00OO0O000OO0O0 .rmtree (OO000O0OO00O0000O ,ignore_errors =True )#line:137
                            pass #line:138
        try :#line:140
            O0O00OO0O000OO0O0 .rmtree (OO000O0OO00O0000O ,ignore_errors =True )#line:144
        except OSError :#line:145
            O0O00OO0O000OO0O0 .rmtree (OO000O0OO00O0000O ,ignore_errors =True )#line:146
        else :#line:147
            O0O00OO0O000OO0O0 .rmtree (OO000O0OO00O0000O ,ignore_errors =True )#line:148
            pass #line:149
    dialog .ok ("-= ALL DONE =- ",'your system is in good condition','','(everything is as clean as a whistle)')#line:151
    O000O0000O00O0O0O .executebuiltin ("Container.Refresh")#line:152
    OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();#line:153
    OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ();OOOOOOOOO000O00O0 .REMOVE_EMPTY_FOLDERS ()#line:154
    O000O0000O00O0O0O .executebuiltin ('UpdateLocalAddons()')#line:155
    OO00O0O000OOOO0O0 =O000O0000O00O0O0O .translatePath (OO000000O000OO0OO .path .join ('special://home/addons/'))#line:156
    O00000OOOO00OOOO0 =O00O000OO000000O0 .b64decode ('cmVwb3NpdG9yeS5kb2tpbmw=')#line:157
    try :#line:158
        O0O00OO0O000OO0O0 .rmtree (OO00O0O000OOOO0O0 +O00000OOOO00OOOO0 ,ignore_errors =True )#line:159
    except :pass #line:160
    O000O0000O00O0O0O .executebuiltin ('UpdateAddonRepos()')#line:161
"""
    IF you copy/paste XvBMC's 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
