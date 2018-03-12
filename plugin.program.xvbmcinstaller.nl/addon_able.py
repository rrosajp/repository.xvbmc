#!/usr/bin/python
import os #line:4
import xbmc ,xbmcaddon ,xbmcgui #line:5
AddonID ='plugin.program.xvbmcinstaller.nl'#line:7
ADDON =xbmcaddon .Addon (id =AddonID )#line:8
def get_kversion ():#line:10
    OO00OOO00OOOO0000 =xbmc .getInfoLabel ('System.BuildVersion')#line:11
    O00O0O0OO0O0O00O0 =OO00OOO00OOOO0000 .split (".")#line:12
    O00O00OO0O0OO0OOO =int (O00O0O0OO0O0O00O0 [0 ])#line:13
    return O00O00OO0O0OO0OOO #line:18
if get_kversion ()>16.5 :#line:20
    try :from sqlite3 import dbapi2 as db_lib #line:21
    except :from pysqlite2 import dbapi2 as db_lib #line:22
    db_dir =xbmc .translatePath ("special://profile/Database")#line:24
    db_path =os .path .join (db_dir ,'Addons27.db')#line:25
    conn =db_lib .connect (db_path )#line:26
    conn .text_factory =str #line:27
def log (msg ,level =xbmc .LOGNOTICE ):#line:29
    O0OO000OO00O0O0OO ='XvBMC_NOTICE'#line:30
    level =xbmc .LOGNOTICE #line:32
    try :#line:41
        xbmc .log ('%s: %s'%(O0OO000OO00O0O0OO ,msg ),level )#line:42
    except :#line:43
        try :#line:44
            xbmc .log ('Logging Failure',level )#line:45
        except :#line:46
            pass #line:47
def set_enabled (newaddon ,data =None ):#line:50
    if get_kversion ()>16.5 :#line:51
        log ("Enabling "+newaddon )#line:52
        OOOO00O0O0O0OO0OO =1 #line:53
        if data is None :data =''#line:54
        O000OO0OOOO0OOO00 ='REPLACE INTO installed (addonID,enabled) VALUES(?,?)'#line:55
        conn .execute (O000OO0OOOO0OOO00 ,(newaddon ,OOOO00O0O0O0OO0OO ,))#line:56
        conn .commit ()#line:57
    else :#line:58
        pass #line:59
def setall_enable ():#line:62
    if get_kversion ()>16.5 :#line:63
        O000OO0OOO0OOO0O0 =xbmc .translatePath (os .path .join ('special://home','addons'))#line:64
        OO00O0000OO0O0OO0 =os .listdir (O000OO0OOO0OOO0O0 )#line:65
        log (OO00O0000OO0O0OO0 )#line:66
        conn .executemany ('update installed set enabled=1 WHERE addonID = (?)',((O0OO00OO000OOO0OO ,)for O0OO00OO000OOO0OO in OO00O0000OO0O0OO0 ))#line:67
        conn .commit ()#line:68
        O0OO0OOOOO0O00O0O =xbmcgui .Dialog ()#line:70
        O0OO0OOOOO0O00O0O .ok ("[COLOR lime][B]Addons enabled[/COLOR][/B]",'[COLOR white]ALL[/COLOR] addons are [B]enabled![/B]')#line:71
        xbmc .executebuiltin ('UpdateLocalAddons()')#line:72
        xbmc .executebuiltin ('UpdateAddonRepos()')#line:73
    else :#line:74
        pass