#!/usr/bin/python
""#line:6
import xbmc as O0OOO0O00O00OO0OO ,xbmcaddon as O000O00OOO000OO0O ,xbmcgui as O0O00O0OOOO0000OO ,xbmcplugin as OOO000O000O0O0O0O #line:25
import os as O00OO0O0O000OO0OO ,shutil as O00OOO00O0O00OO00 #line:26
import common as OO0O0O0O00O0OO00O #line:27
AddonID ='script.xvbmc.updatertools'#line:35
ADDON =O000O00OOO000OO0O .Addon (id =AddonID )#line:36
dialog =O0O00O0OOOO0000OO .Dialog ()#line:38
MainTitle ="XvBMC Nederland"#line:39
def flushMenu ():#line:41
    ""#line:42
    OO0OOO0000000OOO0 =[]#line:44
    OO0OOO0000000OOO0 .append ("Salts [B]HD[/B] Lite - flush cache")#line:45
    OO0OOO0000000OOO0 .append ("Salts [B]HD[/B] Lite - reset db")#line:46
    OO0OOO0000000OOO0 .append ("Salts [B]RD[/B] Lite - flush cache")#line:47
    OO0OOO0000000OOO0 .append ("Salts [B]RD[/B] Lite - reset db")#line:48
    OO0OOO0000000OOO0 .append ("Exodus - flush cache")#line:49
    OO0OOO0000000OOO0 .append ("Exodus - flush sources")#line:50
    OO0OOO0000000OOO0 .append ("[COLOR red]Remove[/COLOR] [COLOR lime]ALL[/COLOR] [COLOR red]these DataBases (Pi optimized)[/COLOR] [COLOR dimgray][I][B]\'[/B]alpha phase[B]\'[/B][/I][/COLOR]")#line:51
    OO0OOO0000000OOO0 .append ("[B][COLOR white]Exit[/COLOR][/B]")#line:52
    O00O0OOO0OOO0000O =O0O00O0OOOO0000OO .Dialog ().select (MainTitle +" [B]-[/B] Flush addon cache/database",OO0OOO0000000OOO0 )#line:55
    if OO0OOO0000000OOO0 [O00O0OOO0OOO0000O ]=="Salts [B]HD[/B] Lite - flush cache":#line:57
        HDflush ()#line:58
    elif OO0OOO0000000OOO0 [O00O0OOO0OOO0000O ]=="Salts [B]HD[/B] Lite - reset db":#line:60
        HDreset ()#line:61
    elif OO0OOO0000000OOO0 [O00O0OOO0OOO0000O ]=="Salts [B]RD[/B] Lite - flush cache":#line:63
        RDflush ()#line:64
    elif OO0OOO0000000OOO0 [O00O0OOO0OOO0000O ]=="Salts [B]RD[/B] Lite - reset db":#line:66
        RDreset ()#line:67
    elif OO0OOO0000000OOO0 [O00O0OOO0OOO0000O ]=="Exodus - flush cache":#line:69
        ExodusCache ()#line:70
    elif OO0OOO0000000OOO0 [O00O0OOO0OOO0000O ]=="Exodus - flush sources":#line:72
        ExodusSources ()#line:73
    elif OO0OOO0000000OOO0 [O00O0OOO0OOO0000O ]=="[COLOR red]Remove[/COLOR] [COLOR lime]ALL[/COLOR] [COLOR red]these DataBases (Pi optimized)[/COLOR] [COLOR dimgray][I][B]\'[/B]alpha phase[B]\'[/B][/I][/COLOR]":#line:75
        RemoveAllDB ()#line:76
class HDflushClass (O0O00O0OOOO0000OO .Window ):#line:78
  def __init__ (self ):#line:79
    OOO0OOOO00O000000 =O00OO0O0O000OO0OO .path .exists (O0OOO0O00O00OO0OO .translatePath (O00OO0O0O000OO0OO .path .join ('special://home','addons','plugin.video.saltshd.lite')))#line:80
    if OOO0OOOO00O000000 :O0OOO0O00O00OO0OO .executebuiltin ("RunPlugin(plugin://plugin.video.saltshd.lite/?mode=flush_cache)")#line:81
    else :#line:82
        dialog .ok (MainTitle ,'Salts HD Lite bevindt zich niet op uw systeem','','(...Salts HD Lite not found...)')#line:83
class HDresetClass (O0O00O0OOOO0000OO .Window ):#line:85
  def __init__ (self ):#line:86
    OO00O0OO00O00000O =O00OO0O0O000OO0OO .path .exists (O0OOO0O00O00OO0OO .translatePath (O00OO0O0O000OO0OO .path .join ('special://home','addons','plugin.video.saltshd.lite')))#line:87
    if OO00O0OO00O00000O :O0OOO0O00O00OO0OO .executebuiltin ("RunPlugin(plugin://plugin.video.saltshd.lite/?mode=reset_db)")#line:88
    else :#line:89
        dialog .ok (MainTitle ,'Salts HD Lite bevindt zich niet op uw systeem','','(...Salts HD Lite not found...)')#line:90
class RDflushClass (O0O00O0OOOO0000OO .Window ):#line:92
  def __init__ (self ):#line:93
    OOO00000O0OO0O000 =O00OO0O0O000OO0OO .path .exists (O0OOO0O00O00OO0OO .translatePath (O00OO0O0O000OO0OO .path .join ('special://home','addons','plugin.video.saltsrd.lite')))#line:94
    if OOO00000O0OO0O000 :O0OOO0O00O00OO0OO .executebuiltin ("RunPlugin(plugin://plugin.video.saltsrd.lite/?mode=flush_cache)")#line:95
    else :#line:96
        dialog .ok (MainTitle ,'Salts RD Lite bevindt zich niet op uw systeem','','(...Salts RD Lite not found...)')#line:97
class RDresetClass (O0O00O0OOOO0000OO .Window ):#line:99
  def __init__ (self ):#line:100
    O0000O0O00O0O0OO0 =O00OO0O0O000OO0OO .path .exists (O0OOO0O00O00OO0OO .translatePath (O00OO0O0O000OO0OO .path .join ('special://home','addons','plugin.video.saltsrd.lite')))#line:101
    if O0000O0O00O0O0OO0 :O0OOO0O00O00OO0OO .executebuiltin ("RunPlugin(plugin://plugin.video.saltsrd.lite/?mode=reset_db)")#line:102
    else :#line:103
        dialog .ok (MainTitle ,'Salts RD Lite bevindt zich niet op uw systeem','','(...Salts RD Lite not found...)')#line:104
class ExodusCacheClass (O0O00O0OOOO0000OO .Window ):#line:106
  def __init__ (self ):#line:107
    OO0OO00OOO0000O0O =O00OO0O0O000OO0OO .path .exists (O0OOO0O00O00OO0OO .translatePath (O00OO0O0O000OO0OO .path .join ('special://home','addons','plugin.video.exodus')))#line:108
    if OO0OO00OOO0000O0O :O0OOO0O00O00OO0OO .executebuiltin ("RunAddon(plugin.video.exodus,/?action=clearCache)")#line:111
    else :#line:112
        dialog .ok (MainTitle ,'Exodus bevindt zich niet op uw systeem','','(...Exodus not found...)')#line:113
class ExodusSourcesClass (O0O00O0OOOO0000OO .Window ):#line:115
  def __init__ (self ):#line:116
    OOOOOOO000OO0O0O0 =O00OO0O0O000OO0OO .path .exists (O0OOO0O00O00OO0OO .translatePath (O00OO0O0O000OO0OO .path .join ('special://home','addons','plugin.video.exodus')))#line:117
    if OOOOOOO000OO0O0O0 :O0OOO0O00O00OO0OO .executebuiltin ("RunPlugin(plugin://plugin.video.exodus/?action=clearSources)")#line:118
    else :#line:119
        dialog .ok (MainTitle ,'Exodus bevindt zich niet op uw systeem','','(...Exodus not found...)')#line:120
class RemoveAllDbClass (O0O00O0OOOO0000OO .Window ):#line:122
  def __init__ (self ):#line:123
    dialog .ok (MainTitle ,'[COLOR white][B]*[/B]DataBase CrapCleaner extreme[B]*[/B][/COLOR]','','(Raspberry Pi optimized, [B]can[/B] work cross-platform)')#line:124
    import os as OO0O0OO000O000OO0 ,xbmc as OOOOO00000O000000 ,shutil as OO0O00OO0O0000000 #line:125
    O000OO0O0000OOOOO =OO0O0OO000O000OO0 .listdir (OOOOO00000O000000 .translatePath (OO0O0OO000O000OO0 .path .join ('special://home/userdata/Database/')))#line:127
    OO0OO00OOO00OO0O0 =OOOOO00000O000000 .translatePath (OO0O0OO000O000OO0 .path .join ('special://home/userdata/Database/'))#line:128
    O00OO00O00O00O000 =OO0O0OO000O000OO0 .listdir (OOOOO00000O000000 .translatePath (OO0O0OO000O000OO0 .path .join ('special://home/userdata/addon_data/plugin.video.exodus/')))#line:129
    OO0O00OO0000O0000 =OOOOO00000O000000 .translatePath (OO0O0OO000O000OO0 .path .join ('special://home/userdata/addon_data/plugin.video.exodus/'))#line:130
    for OO0O00O00O00OO000 in O000OO0O0000OOOOO :#line:131
        if ('saltsrd.lite')in OO0O00O00O00OO000 :#line:132
            OO0O0O0O00O0OO00O .log (str (O000OO0O0000OOOOO )+str (OO0O00O00O00OO000 ))#line:133
            OO0O0O0OO0O00O00O =OO0O0OO000O000OO0 .path .join (OO0OO00OOO00OO0O0 ,OO0O00O00O00OO000 )#line:135
            try :#line:136
                OOOOO00000O000000 .log (str (OO0O0O0OO0O00O00O ))#line:137
                OO0O0OO000O000OO0 .unlink (OO0O0O0OO0O00O00O )#line:138
            except :pass #line:139
        elif ('saltshd.lite')in OO0O00O00O00OO000 :#line:140
            OO0O0O0O00O0OO00O .log (str (O000OO0O0000OOOOO )+str (OO0O00O00O00OO000 ))#line:141
            OO0O0O0OO0O00O00O =OO0O0OO000O000OO0 .path .join (OO0OO00OOO00OO0O0 ,OO0O00O00O00OO000 )#line:143
            try :#line:144
                OOOOO00000O000000 .log (str (OO0O0O0OO0O00O00O ))#line:145
                OO0O0OO000O000OO0 .remove (OO0O0O0OO0O00O00O )#line:146
            except :pass #line:147
        elif ('mig_export_')in OO0O00O00O00OO000 :#line:148
            OO0O0O0O00O0OO00O .log (str (O000OO0O0000OOOOO )+str (OO0O00O00O00OO000 ))#line:149
            OO0O0O0OO0O00O00O =OO0O0OO000O000OO0 .path .join (OO0OO00OOO00OO0O0 ,OO0O00O00O00OO000 )#line:151
            try :#line:152
                OOOOO00000O000000 .log (str (OO0O0O0OO0O00O00O ))#line:153
                OO0O0OO000O000OO0 .remove (OO0O0O0OO0O00O00O )#line:154
            except :pass #line:155
        else :#line:156
            pass #line:157
    for OO0O00O00O00OO000 in O00OO00O00O00O000 :#line:159
        if ('cache')in OO0O00O00O00OO000 :#line:160
            OO0O0O0O00O0OO00O .log (str (O00OO00O00O00O000 )+str (OO0O00O00O00OO000 ))#line:161
            OO0O0O0OO0O00O00O =OO0O0OO000O000OO0 .path .join (OO0O00OO0000O0000 ,OO0O00O00O00OO000 )#line:163
            try :#line:164
                OOOOO00000O000000 .log (str (OO0O0O0OO0O00O00O ))#line:165
                OO0O0OO000O000OO0 .remove (OO0O0O0OO0O00O00O )#line:166
            except :pass #line:167
        elif ('providers.8')in OO0O00O00O00OO000 :#line:168
            OO0O0O0O00O0OO00O .log (str (O00OO00O00O00O000 )+str (OO0O00O00O00OO000 ))#line:169
            OO0O0O0OO0O00O00O =OO0O0OO000O000OO0 .path .join (OO0O00OO0000O0000 ,OO0O00O00O00OO000 )#line:171
            try :#line:172
                OOOOO00000O000000 .log (str (OO0O0O0OO0O00O00O ))#line:173
                OO0O0OO000O000OO0 .remove (OO0O0O0OO0O00O00O )#line:174
            except :pass #line:175
        else :#line:176
            pass #line:177
def HDflush ():#line:179
    OOO00OOOOOO0OOOOO =HDflushClass ()#line:180
    del OOO00OOOOOO0OOOOO #line:181
def HDreset ():#line:183
    OOOO0OOOOO000O00O =HDresetClass ()#line:184
    del OOOO0OOOOO000O00O #line:185
def RDflush ():#line:187
    OOO0OO0000OO0OOOO =RDflushClass ()#line:188
    del OOO0OO0000OO0OOOO #line:189
def RDreset ():#line:191
    O00OOO000O0000O0O =RDresetClass ()#line:192
    del O00OOO000O0000O0O #line:193
def ExodusCache ():#line:195
    OO0O00000O00OO000 =ExodusCacheClass ()#line:196
    del OO0O00000O00OO000 #line:197
def ExodusSources ():#line:199
    O00O0O0OOO0000O0O =ExodusSourcesClass ()#line:200
    del O00O0O0OOO0000O0O #line:201
def RemoveAllDB ():#line:203
    OOOOOO000000OO000 =RemoveAllDbClass ()#line:204
    del OOOOOO000000OO000 #line:205
"""
    IF you copy/paste XvBMC's 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""
