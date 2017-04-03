#!/usr/bin/python
""#line:5
import xbmc as O0OOOOO0OOOO0O000 ,xbmcaddon as OO0OO0000OOOO0OOO ,xbmcgui as OOO0O0OO00OOO0OO0 ,xbmcplugin as OO0000000000O0OOO ,xbmcvfs as O0O0OO0000O00O0OO #line:25
import os as OO00O0O000000O00O ,re as OOO000O00OOOOO0OO ,base64 as O0OOO0OOO0O0000OO ,sys as O00OOO0O0000OOOOO ,shutil as OOOO0O000O00OOO00 #line:26
import common as O000O0OO0OO0OOOO0 #line:27
dialog =OOO0O0OO00OOO0OO0 .Dialog ()#line:30
class cacheEntry :#line:36
    def __init__ (O0OO00OO0000OO0O0 ,O0OO0OO0OO00OO0O0 ,OO0O0O00OO0O0OO0O ):#line:37
        O0OO00OO0000OO0O0 .name =O0OO0OO0OO00OO0O0 #line:38
        O0OO00OO0000OO0O0 .path =OO0O0O00OO0O0OO0O #line:39
def setupXvbmcEntries ():#line:46
    O0000O0OOOO0O0O0O =16 #line:47
    OO0000OO0OO0000OO =["jehrico","kidsplace","nlview","nl-viewer","nl-viewer2","nlv3","sportcenterhd","troma-copypaste","jehricorepo","nlviewrepo","doki","xodi","kijk","adelaar","geentv","tvad"]#line:48
    O0O0O00000OOOOO0O =["special://home/addons/"+"plugin.video.jericho","special://home/addons/"+"plugin.video.kidsplace","special://home/addons/"+"plugin.video.NLVIEW","special://home/addons/"+"plugin.video.nl-viewer","special://home/addons/"+"plugin.video.nl-viewer2","special://home/addons/"+"plugin.video.nlv3","special://home/addons/"+"plugin.video.sportcenterhd","special://home/addons/"+"plugin.video.troma","special://home/addons/"+"repository.jericho","special://home/addons/"+"repository.NLVIEW","special://home/addons/"+"repository.dokinl","special://home/addons/"+"repository.x-odi.nl","special://home/addons/"+"repository.kijkalles.nl","special://home/addons/"+"repository.eagle","special://home/addons/"+"repository.ditistv","special://home/addons/"+"repository.tvaddons.nl"]#line:65
    OOOO000OOOOOO0000 =[]#line:67
    for OO0OO00OOOOO0OO00 in range (O0000O0OOOO0O0O0O ):#line:69
        OOOO000OOOOOO0000 .append (cacheEntry (OO0000OO0OO0000OO [OO0OO00OOOOO0OO00 ],O0O0O00000OOOOO0O [OO0OO00OOOOO0OO00 ]))#line:70
    return OOOO000OOOOOO0000 #line:72
def purgeOLD ():#line:79
    O0OO0O000OO000OOO =setupXvbmcEntries ()#line:94
    for O0O00000000O00O0O in O0OO0O000OO000OOO :#line:96
        O000O0OO0OOOOOO0O =O0OOOOO0OOOO0O000 .translatePath (O0O00000000O00O0O .path )#line:97
        if OO00O0O000000O00O .path .exists (O000O0OO0OOOOOO0O )==True :#line:98
            for O0O0O0O0OOO0O00O0 ,OOOO00O00OOO000O0 ,O00O0OOO0O0O00OO0 in OO00O0O000000O00O .walk (O000O0OO0OOOOOO0O ):#line:99
                if len (OOOO00O00OOO000O0 )>0 and len (O00O0OOO0O0O00OO0 )>0 :#line:105
                    for O0O00O00OOOOO0O0O in O00O0OOO0O0O00OO0 :#line:106
                        try :#line:107
                            OO00O0O000000O00O .unlink (OO00O0O000000O00O .path .join (O0O0O0O0OOO0O00O0 ,O0O00O00OOOOO0O0O ))#line:108
                        except :pass #line:109
                    for O0O0OO0OO00O0OO00 in OOOO00O00OOO000O0 :#line:110
                        try :#line:111
                            OOOO0O000O00OOO00 .rmtree (OO00O0O000000O00O .path .join (O0O0O0O0OOO0O00O0 ,O0O0OO0OO00O0OO00 ))#line:112
                        except OSError :#line:113
                            OOOO0O000O00OOO00 .rmtree (O000O0OO0OOOOOO0O ,ignore_errors =True )#line:114
                        else :#line:115
                            OOOO0O000O00OOO00 .rmtree (O000O0OO0OOOOOO0O ,ignore_errors =True )#line:116
                            pass #line:117
                elif len (OOOO00O00OOO000O0 )==0 and len (O00O0OOO0O0O00OO0 )==0 :#line:119
                    for O0O00O00OOOOO0O0O in O00O0OOO0O0O00OO0 :#line:123
                        try :#line:124
                            OO00O0O000000O00O .unlink (OO00O0O000000O00O .path .join (O0O0O0O0OOO0O00O0 ,O0O00O00OOOOO0O0O ))#line:125
                        except :pass #line:126
                    for O0O0OO0OO00O0OO00 in OOOO00O00OOO000O0 :#line:127
                        try :#line:128
                            OOOO0O000O00OOO00 .rmtree (OO00O0O000000O00O .path .join (O0O0O0O0OOO0O00O0 ,O0O0OO0OO00O0OO00 ))#line:129
                        except OSError :#line:130
                            OOOO0O000O00OOO00 .rmtree (O000O0OO0OOOOOO0O ,ignore_errors =True )#line:131
                        else :#line:132
                            OOOO0O000O00OOO00 .rmtree (O000O0OO0OOOOOO0O ,ignore_errors =True )#line:133
                            pass #line:134
        try :#line:136
            OOOO0O000O00OOO00 .rmtree (O000O0OO0OOOOOO0O ,ignore_errors =True )#line:140
        except OSError :#line:141
            OOOO0O000O00OOO00 .rmtree (O000O0OO0OOOOOO0O ,ignore_errors =True )#line:142
        else :#line:143
            OOOO0O000O00OOO00 .rmtree (O000O0OO0OOOOOO0O ,ignore_errors =True )#line:144
            pass #line:145
    dialog .ok ("-= ALL DONE =- ",'your system is in good condition','','(everything is as clean as a whistle)')#line:147
    O0OOOOO0OOOO0O000 .executebuiltin ("UpdateLocalAddons")#line:149
    O0OOOOO0OOOO0O000 .executebuiltin ("UpdateAddonRepos")#line:150
    OOO0OO0O000O0OOOO =O0OOOOO0OOOO0O000 .translatePath (OO00O0O000000O00O .path .join ('special://home/addons/'))#line:152
    OO0OO00O0OO0O0OO0 =O0OOO0OOO0O0000OO .b64decode ('cmVwb3NpdG9yeS5kb2tpbmw=')#line:153
    OOOO0O000O00OOO00 .rmtree (OOO0OO0O000O0OOOO +OO0OO00O0OO0O0OO0 ,ignore_errors =True )#line:154
"""
	IF you copy/paste XvBMC's 'purge.py' please keep the credits -2- XvBMC Nederland, Thx.
"""#line:158
purgeOLD ()
