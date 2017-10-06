#!/usr/bin/python
"""
    IF you copy/paste XvBMC's -utils.py- please keep the credits -2- XvBMC-NL, Thx.
"""#line:6
import cookielib ,os ,urllib ,urllib2 #line:8
import xbmc ,xbmcaddon ,xbmcgui ,xbmcplugin #line:9
from resources .lib .common import currentsptxt ,currentsptxtrpi ,currentsptxtwiz ,uwspversietxt ,uwspversietxtrpi ,uwspversietxtwiz #line:10
ADDON =xbmcaddon .Addon (id ='script.xvbmc.updatertools')#line:12
USER_AGENT ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'#line:14
profileDir =ADDON .getAddonInfo ('profile')#line:15
profileDir =xbmc .translatePath (profileDir ).decode ("utf-8")#line:16
headers ={'User-Agent':USER_AGENT ,'Accept':'*/*','Connection':'keep-alive'}#line:19
cookiePath =os .path .join (profileDir ,'cookies.lwp')#line:20
dialog =xbmcgui .Dialog ()#line:22
kodiver =xbmc .getInfoLabel ("System.BuildVersion").split (".")[0 ]#line:23
versietxt =uwspversietxt #line:24
versieurl =currentsptxt #line:25
versietxtrpi =uwspversietxtrpi #line:26
versieurlrpi =currentsptxtrpi #line:27
versietxtwiz =uwspversietxtwiz #line:28
versieurlwiz =currentsptxtwiz #line:29
if not os .path .exists (profileDir ):#line:31
    os .makedirs (profileDir )#line:32
urlopen =urllib2 .urlopen #line:34
cj =cookielib .LWPCookieJar (xbmc .translatePath (cookiePath ))#line:35
Request =urllib2 .Request #line:36
if cj !=None :#line:38
    if os .path .isfile (xbmc .translatePath (cookiePath )):#line:39
        try :#line:40
            cj .load ()#line:41
        except :#line:42
            try :#line:43
                os .remove (xbmc .translatePath (cookiePath ))#line:44
                pass #line:45
            except :#line:46
                pass #line:47
    cookie_handler =urllib2 .HTTPCookieProcessor (cj )#line:48
    opener =urllib2 .build_opener (cookie_handler ,urllib2 .HTTPBasicAuthHandler (),urllib2 .HTTPHandler ())#line:49
else :#line:50
    opener =urllib2 .build_opener ()#line:51
urllib2 .install_opener (opener )#line:53
def getHtml2 (url ):#line:56
    O00O0OO00OOO00OO0 =Request (url )#line:57
    OO00O0O00OOOO0O00 =urlopen (O00O0OO00OOO00OO0 ,timeout =60 )#line:58
    OOOO0OO0OOOOO0OOO =OO00O0O00OOOO0O00 .read ()#line:59
    OO00O0O00OOOO0O00 .close ()#line:60
    return OOOO0OO0OOOOO0OOO #line:61
def postHtml (url ,form_data ={},headers ={},compression =True ,NoCookie =None ):#line:64
    _O0O0OO00OOOOO0O0O ='Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 '+'(KHTML, like Gecko) Chrome/13.0.782.99 Safari/535.1'#line:66
    OOO00OOOOO0OO0OOO =urllib2 .Request (url )#line:67
    if form_data :#line:68
        form_data =urllib .urlencode (form_data )#line:69
        OOO00OOOOO0OO0OOO =urllib2 .Request (url ,form_data )#line:70
    OOO00OOOOO0OO0OOO .add_header ('User-Agent',_O0O0OO00OOOOO0O0O )#line:71
    for O0OO0OO00000O0O0O ,OO0O0OOO000OO000O in headers .items ():#line:72
        OOO00OOOOO0OO0OOO .add_header (O0OO0OO00000O0O0O ,OO0O0OOO000OO000O )#line:73
    if compression :#line:74
        OOO00OOOOO0OO0OOO .add_header ('Accept-Encoding','gzip')#line:75
    OOO00OOO000000OO0 =urllib2 .urlopen (OOO00OOOOO0OO0OOO ,timeout =30 )#line:76
    O0000O0OO00OOOOOO =OOO00OOO000000OO0 .read ()#line:77
    if not NoCookie :#line:78
        try :#line:79
            cj .save (cookiePath )#line:80
        except :pass #line:81
    OOO00OOO000000OO0 .close ()#line:82
    return O0000O0OO00OOOOOO #line:83
def checkUpdate (onlycurrent =False ):#line:86
    if os .path .isfile (versietxt ):#line:87
       O00000O0OOOO0OOO0 =open (versietxt ,'r')#line:88
       OO000O00OOO0OOOO0 =O00000O0OOOO0OOO0 .read ()#line:89
       O00000O0OOOO0OOO0 .close ()#line:90
       if onlycurrent :return OO000O00OOO0OOOO0 ,''#line:91
       try :O0O0OOOO000000000 =getHtml2 (versieurl )#line:92
       except :return 'noupdate',OO000O00OOO0OOOO0 #line:93
       try :#line:94
           if int (O0O0OOOO000000000 )>int (OO000O00OOO0OOOO0 ):#line:95
              return 'update',O0O0OOOO000000000 #line:96
       except ValueError :#line:97
              return 'notinstalled',''#line:99
       else :return 'noupdate',OO000O00OOO0OOOO0 #line:100
    elif os .path .isfile (versietxtwiz ):#line:101
         O00000O0OOOO0OOO0 =open (versietxtwiz ,'r')#line:102
         OO000O00OOO0OOOO0 =O00000O0OOOO0OOO0 .read ()#line:103
         O00000O0OOOO0OOO0 .close ()#line:104
         if onlycurrent :return OO000O00OOO0OOOO0 ,''#line:105
         try :O0OO0O00000O00O0O =getHtml2 (versieurlwiz )#line:106
         except :return 'noupdate',OO000O00OOO0OOOO0 #line:107
         try :#line:108
             if int (O0OO0O00000O00O0O )>int (OO000O00OOO0OOOO0 ):#line:109
                return 'wizupdate',O0OO0O00000O00O0O #line:110
         except ValueError :#line:111
                return 'notinstalled',''#line:113
         else :return 'noupdate',OO000O00OOO0OOOO0 #line:114
    elif os .path .isfile (versietxtrpi ):#line:115
         O00000O0OOOO0OOO0 =open (versietxtrpi ,'r')#line:116
         OO000O00OOO0OOOO0 =O00000O0OOOO0OOO0 .read ()#line:117
         O00000O0OOOO0OOO0 .close ()#line:118
         if onlycurrent :return OO000O00OOO0OOOO0 ,''#line:119
         try :OO0O0OOO0OO0OOO0O =getHtml2 (versieurlrpi )#line:120
         except :return 'noupdate',OO000O00OOO0OOOO0 #line:121
         try :#line:122
             if int (OO0O0OOO0OO0OOO0O )>int (OO000O00OOO0OOOO0 ):#line:123
                return 'rpiupdate',OO0O0OOO0OO0OOO0O #line:124
         except ValueError :#line:125
                return 'notinstalled',''#line:127
         else :return 'noupdaterpi',OO000O00OOO0OOOO0 #line:128
    else :return 'notinstalled',''#line:129
def enableAddons (melding =None ,update =True ):#line:132
    if kodiver >16.5 :#line:133
        try :from sqlite3 import dbapi2 as OOO0O00O0O00OO00O #line:134
        except :from pysqlite2 import dbapi2 as OOO0O00O0O00OO00O #line:135
        O0O000O0OOO0000O0 =xbmc .translatePath ("special://profile/Database")#line:137
        O00O00OOO0OO0O000 =os .path .join (O0O000O0OOO0000O0 ,'Addons27.db')#line:138
        O0O0O00OO0OO0O0O0 =OOO0O00O0O00OO00O .connect (O00O00OOO0OO0O000 )#line:139
        O0O0O00OO0OO0O0O0 .text_factory =str #line:140
        OOOOO000OO0O0O0OO =xbmc .translatePath (os .path .join ('special://home','addons'))#line:142
        O000OOO0O00000O0O =os .listdir (OOOOO000OO0O0O0OO )#line:143
        O0O0O00OO0OO0O0O0 .executemany ('update installed set enabled=1 WHERE addonID = (?)',((OOO000OOO0O000O0O ,)for OOO000OOO0O000O0O in O000OOO0O00000O0O ))#line:144
        O0O0O00OO0OO0O0O0 .commit ()#line:145
        if update :#line:146
            xbmc .executebuiltin ('UpdateAddonRepos()')#line:147
            xbmc .executebuiltin ('UpdateLocalAddons()')#line:148
        if melding :#line:149
            dialog .ok ("[COLOR lime][B]Addons enabled[/COLOR][/B]",'[COLOR white]ALL[/COLOR] addons are [B]enabled![/B]')#line:150
    else :#line:151
        pass 
