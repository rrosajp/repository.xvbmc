#!/usr/bin/python
"""
    IF you copy/paste please keep the credits -2- XvBMC-NL, Thx.
"""#line:6
import os #line:8
import xbmc ,xbmcaddon ,xbmcgui ,xbmcplugin #line:9
import common as Common #line:11
AddonID ='script.xvbmc.updatertools'#line:13
ADDON =xbmcaddon .Addon (id =AddonID )#line:14
if Common .get_kversion ()>16.5 :#line:16
    try :from sqlite3 import dbapi2 as db_lib #line:17
    except :from pysqlite2 import dbapi2 as db_lib #line:18
    db_dir =xbmc .translatePath ("special://profile/Database")#line:20
    db_path =os .path .join (db_dir ,'Addons27.db')#line:21
    conn =db_lib .connect (db_path )#line:22
    conn .text_factory =str #line:23
def set_enabled (newaddon ,data =None ):#line:25
    if Common .get_kversion ()>16.5 :#line:26
        Common .log ("Enabling "+newaddon )#line:27
        OO00OO0OO0OO0OO00 =1 #line:28
        if data is None :data =''#line:29
        OO0O0O0O00000O0OO ='REPLACE INTO installed (addonID,enabled) VALUES(?,?)'#line:30
        conn .execute (OO0O0O0O00000O0OO ,(newaddon ,OO00OO0OO0OO0OO00 ,))#line:31
        conn .commit ()#line:32
    else :pass #line:33
def setall_enable ():#line:35
    if Common .get_kversion ()>16.5 :#line:36
        OOOOOO000000OOO0O =xbmc .translatePath (os .path .join ('special://home','addons'))#line:37
        OO000OOO000OO0O00 =os .listdir (OOOOOO000000OOO0O )#line:38
        Common .log (OO000OOO000OO0O00 )#line:39
        conn .executemany ('update installed set enabled=1 WHERE addonID = (?)',((O0O00O00O0OO00O00 ,)for O0O00O00O0OO00O00 in OO000OOO000OO0O00 ))#line:40
        conn .commit ()#line:41
        OOO00OOOO00O00000 =xbmcgui .Dialog ()#line:42
        OOO00OOOO00O00000 .ok ("[COLOR lime][B]Addons enabled[/COLOR][/B]",'[COLOR white]ALL[/COLOR] addons are [B]enabled![/B]')#line:43
        xbmc .executebuiltin ('UpdateLocalAddons()')#line:44
        xbmc .executebuiltin ('UpdateAddonRepos()')#line:45
    else :pass 
