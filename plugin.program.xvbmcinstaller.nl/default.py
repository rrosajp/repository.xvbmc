#!/usr/bin/python
import xbmc as O0O0OO0OO0OO00OO0 ,xbmcaddon as O000OOO0OOOOO000O ,xbmcgui as OO0O00OOOOO000O0O ,xbmcplugin as OO0O00OOO0OOOO00O #line:4
import os as OO00OO0O00OO0O000 ,re as OO0OOO0O0OO000O0O ,sys as O0000OO00OO0O0OOO ,time as OOO0O0O0O0O00OOO0 ,urllib2 as O0O0OO0O0OOOO0000 ,urllib as OO0OO0O0O00OO0O0O #line:5
import addon_able as OO00OO0OO00O000OO #line:6
import downloader as O0O00OO0000OOOO0O #line:7
import extract as OOO0O000OO0O0O0OO #line:8
ADDON =O000OOO0OOOOO000O .Addon (id ='plugin.program.xvbmcinstaller.nl')#line:10
base ='http://bit.ly/XvBMC-NL'#line:11
BASEURL ='https://archive.org/download/xvbmcwizardz/wizard.txt'#line:12
U =ADDON .getSetting ('userlist')#line:14
USER_AGENT ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'#line:15
ADDON_ID =O000OOO0OOOOO000O .Addon ().getAddonInfo ('id')#line:16
ADDONTITLE ='XvBMC-NL wizard/installer'#line:17
dialog =OO0O00OOOOO000O0O .Dialog ()#line:19
dp =OO0O00OOOOO000O0O .DialogProgress ()#line:20
HOME =O0O0OO0OO0OO00OO0 .translatePath ('special://home/')#line:21
PATH ="XvBMC-NL"#line:22
VERSION ="wizard/installer"#line:23
skin =O0O0OO0OO0OO00OO0 .getSkinDir ()#line:24
EXCLUDES =[ADDON_ID ,'script.xvbmc.updatertools','repository.xvbmc','xvbmc.zip']#line:25
packagedir =O0O0OO0OO0OO00OO0 .translatePath (OO00OO0O00OO0O000 .path .join ('special://home/addons/packages',''))#line:26
def WIZARDS ():#line:28
    O0OO0O00O00OO0OO0 =OPEN_URL (BASEURL ).replace ('\n','').replace ('\r','')#line:29
    O00O00OO00O0000OO =OO0OOO0O0OO000O0O .compile ('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall (O0OO0O00O00OO0OO0 )#line:30
    for OOOOOO000OOO00O0O ,O0O00O0000OOOOO00 ,O000000O0O0OO000O ,OO0O0000000OO0OOO ,OO00OO0OOOO000OO0 in O00O00OO00O0000OO :#line:31
        addDir (OOOOOO000OOO00O0O ,O0O00O0000OOOOO00 ,1 ,O000000O0O0OO000O ,OO0O0000000OO0OOO ,OO00OO0OOOO000OO0 )#line:32
    setView ('movies','MAIN')#line:33
def QUICKREBOOT ():#line:35
		dialog .ok (ADDONTITLE +" [COLOR lime][B]-Finished![/B][/COLOR]",'herstart Kodi om uw nieuwe build te gebruiken','','[COLOR dimgray](reboot Kodi to use your new build)[/COLOR]')#line:36
		OO00OO0O00OO0O000 ._exit (1 )#line:37
def OPEN_URL (url ):#line:39
    O00O0OOO0OOO0OOOO =O0O0OO0O0OOOO0000 .Request (url )#line:40
    O00O0OOO0OOO0OOOO .add_header ('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')#line:41
    OOO0O000O00O0OOOO =O0O0OO0O0OOOO0000 .urlopen (O00O0OOO0OOO0OOOO )#line:42
    O00000OOOOOOO0OO0 =OOO0O000O00O0OOOO .read ()#line:43
    OOO0O000O00O0OOOO .close ()#line:44
    return O00000OOOOOOO0OO0 #line:45
def WipeXBMC ():#line:47
    if skin !="skin.estuary":#line:48
        dialog .ok ("[COLOR dodgerblue]"+ADDONTITLE +"[/COLOR] [COLOR red][B]\'WiPE\'[/B][/COLOR]",'selecteer eerst de standaard (Estuary) skin alvorens een volledige [B]\'wipe\'[/B] van uw Kodi uit te voeren.','','[COLOR dimgray](before Kodi wipe, select Estuary skin first)[/COLOR]')#line:49
        O0O0OO0OO0OO00OO0 .executebuiltin ("ActivateWindow(InterfaceSettings)")#line:50
        return #line:51
    else :#line:52
        O00O0O000OOO0OOO0 =OO0O00OOOOO000O0O .Dialog ().yesno ("[COLOR lime][B]BELANGRIJK / IMPORTANT / HINT[/B][/COLOR]",'[B]let op: [/B]dit zal alles verwijderen van uw huidige Kodi installatie, weet u zeker dat u wilt doorgaan[B]?[/B]','','[COLOR dimgray](this will remove your current Kodi build, continue?)[/COLOR]',yeslabel ='[COLOR lime][B]JA/YES[/B][/COLOR]',nolabel ='[COLOR red]nee/nope[/COLOR]')#line:53
        if O00O0O000OOO0OOO0 ==1 :dp .create ("[COLOR white]"+ADDONTITLE +"[/COLOR] [COLOR red]\'WiPiNG\'[/COLOR]","verwijder alles (remove everything)",'','even geduld... (please wait...)')#line:54
        try :#line:55
            for OO0000OO0OO00O0O0 ,O00OOO0OO00O00000 ,O0OOO00O0O0O00OO0 in OO00OO0O00OO0O000 .walk (HOME ,topdown =True ):#line:56
                O00OOO0OO00O00000 [:]=[O00OOOOOOOOO0OOOO for O00OOOOOOOOO0OOOO in O00OOO0OO00O00000 if O00OOOOOOOOO0OOOO not in EXCLUDES ]#line:57
                for OOO0OO0O0OO00OOO0 in O0OOO00O0O0O00OO0 :#line:58
                    try :#line:59
                        OO00OO0O00OO0O000 .remove (OO00OO0O00OO0O000 .path .join (OO0000OO0OO00O0O0 ,OOO0OO0O0OO00OOO0 ))#line:60
                        OO00OO0O00OO0O000 .rmdir (OO00OO0O00OO0O000 .path .join (OO0000OO0OO00O0O0 ,OOO0OO0O0OO00OOO0 ))#line:61
                    except :pass #line:62
                for OOO0OO0O0OO00OOO0 in O00OOO0OO00O00000 :#line:64
                    try :OO00OO0O00OO0O000 .rmdir (OO00OO0O00OO0O000 .path .join (OO0000OO0OO00O0O0 ,OOO0OO0O0OO00OOO0 ));OO00OO0O00OO0O000 .rmdir (OO0000OO0OO00O0O0 )#line:65
                    except :pass #line:66
        except :pass #line:67
    REMOVE_EMPTY_FOLDERS ()#line:68
    REMOVE_EMPTY_FOLDERS ()#line:69
    REMOVE_EMPTY_FOLDERS ()#line:70
    REMOVE_EMPTY_FOLDERS ()#line:71
    REMOVE_EMPTY_FOLDERS ()#line:72
    REMOVE_EMPTY_FOLDERS ()#line:73
    REMOVE_EMPTY_FOLDERS ()#line:74
    REMOVE_EMPTY_FOLDERS ()#line:75
    REMOVE_EMPTY_FOLDERS ()#line:76
    REMOVE_EMPTY_FOLDERS ()#line:77
    dialog .ok ("[COLOR dodgerblue]"+ADDONTITLE +"[/COLOR] [COLOR lime][B]Voltooid![/B][/COLOR]",'Kodi zal nu afsluiten, herstart Kodi en her-open deze \'installer\' om verder te gaan.','','[COLOR dimgray](shutdown Kodi, restart Kodi and re-open this installer)[/COLOR]')#line:78
    OO00OO0O00OO0O000 ._exit (1 )#line:79
def REMOVE_EMPTY_FOLDERS ():#line:81
    OO00OO0OO00O000OO .log ("########### Start Removing Empty Folders #########")#line:82
    O0O00O00O0O00OO00 =0 #line:83
    OOO0O0O0OO0000000 =0 #line:84
    for OOO0OO0OOO0O00O00 ,OOOOOOO0O00O00000 ,O00O0O00000O000OO in OO00OO0O00OO0O000 .walk (HOME ):#line:85
        if len (OOOOOOO0O00O00000 )==0 and len (O00O0O00000O000OO )==0 :#line:86
            O0O00O00O0O00OO00 +=1 #line:87
            OO00OO0O00OO0O000 .rmdir (OOO0OO0OOO0O00O00 )#line:88
            OO00OO0OO00O000OO .log ("successfully removed: "+OOO0OO0OOO0O00O00 )#line:89
        elif len (OOOOOOO0O00O00000 )>0 and len (O00O0O00000O000OO )>0 :#line:90
            OOO0O0O0OO0000000 +=1 #line:91
def Enabler ():#line:93
		try :OO00OO0OO00O000OO .set_enabled ("script.xvbmc.updatertools")#line:94
		except :pass #line:95
		OOO0O0O0O0O00OOO0 .sleep (0.5 )#line:96
		try :OO00OO0OO00O000OO .set_enabled ("repository.xvbmc")#line:97
		except :pass #line:98
		OOO0O0O0O0O00OOO0 .sleep (0.5 )#line:99
		try :OO00OO0OO00O000OO .set_enabled ("plugin.program.xvbmcinstaller.nl")#line:100
		except :pass #line:101
		OOO0O0O0O0O00OOO0 .sleep (0.5 )#line:102
		O0O0OO0OO0OO00OO0 .executebuiltin ('XBMC.UpdateLocalAddons()')#line:103
		dialog .ok ("[COLOR lime][B]Operation Complete![/B][/COLOR]",'Enabled some xvbmc add-ons!','    Brought To You By %s '%ADDONTITLE )#line:106
def wizard (name ,url ,description ):#line:108
    OO0O00OOOOOOO0OO0 =OO0O00OOOOO000O0O .Dialog ().yesno ("[COLOR red][B]\'Wipe\'[/B] Kodi First / Kodi verwijderen[/COLOR]",' ','wilt u eerst uw huidige \"oude\" Kodi verwijderen? [COLOR dimgray](1x)[/COLOR]','[COLOR dimgray](tip: remove your current \"old\" Kodi first, okay?)[/COLOR]',nolabel ='[COLOR red]nee/nope[/COLOR]',yeslabel ='[COLOR lime][B]JA/YES[/B][/COLOR]')#line:109
    if OO0O00OOOOOOO0OO0 :WipeXBMC ()#line:110
    if not OO00OO0O00OO0O000 .path .exists (packagedir ):OO00OO0O00OO0O000 .makedirs (packagedir )#line:111
    if skin !="skin.estuary":#line:112
        dialog .ok ("[COLOR orange]"+ADDONTITLE +" [B]-[/B]Switch Skin[/COLOR]",' ','schakel nu eerst naar de standaard (Estuary) skin aub','[COLOR dimgray](switch to the default Estuary skin please)[/COLOR]')#line:113
        O0O0OO0OO0OO00OO0 .executebuiltin ("ActivateWindow(InterfaceSettings)")#line:114
        return #line:115
    O0OOO0OO00OOOOO00 =O0O0OO0OO0OO00OO0 .translatePath (OO00OO0O00OO0O000 .path .join ('special://home/addons','packages'))#line:116
    OO0000O000O00O0OO =OO0O00OOOOO000O0O .DialogProgress ()#line:117
    OO0000O000O00O0OO .create (ADDONTITLE ,'...Downloading and Copying File(s)...','','even geduld / please wait')#line:118
    O0O0OOOOOO000O00O =OO00OO0O00OO0O000 .path .join (O0OOO0OO00OOOOO00 ,'xvbmc.zip')#line:119
    try :#line:120
       OO00OO0O00OO0O000 .remove (O0O0OOOOOO000O00O )#line:121
    except :#line:122
       pass #line:123
    O0O00OO0000OOOO0O .download (url ,O0O0OOOOOO000O00O ,OO0000O000O00O0OO )#line:124
    O0O0OO0O00OO00OO0 =O0O0OO0OO0OO00OO0 .translatePath (OO00OO0O00OO0O000 .path .join ('special://','home'))#line:125
    OOO0O0O0O0O00OOO0 .sleep (2 )#line:126
    OO0000O000O00O0OO .update (0 ,"","[I](uitpakken/extract Build)[/I]")#line:127
    OOO0O000OO0O0O0OO .all (O0O0OOOOOO000O00O ,O0O0OO0O00OO00OO0 ,OO0000O000O00O0OO )#line:128
    O0O0OO0OO0OO00OO0 .sleep (1000 )#line:129
    O0O0OO0OO0OO00OO0 .sleep (5000 )#line:130
    try :OO00OO0O00OO0O000 .remove (O0O0OOOOOO000O00O )#line:131
    except :pass #line:132
    OO0000O000O00O0OO .close ()#line:133
    Enabler ()#line:134
    QUICKREBOOT ()#line:135
def addDir (name ,url ,mode ,iconimage ,fanart ,description ):#line:137
        O000OOOOOOO00OO0O =O0000OO00OO0O0OOO .argv [0 ]+"?url="+OO0OO0O0O00OO0O0O .quote_plus (url )+"&mode="+str (mode )+"&name="+OO0OO0O0O00OO0O0O .quote_plus (name )+"&iconimage="+OO0OO0O0O00OO0O0O .quote_plus (iconimage )+"&fanart="+OO0OO0O0O00OO0O0O .quote_plus (fanart )+"&description="+OO0OO0O0O00OO0O0O .quote_plus (description )#line:138
        OO0O00O000O0OOOOO =True #line:139
        O0OO0OO00O0O0O000 =OO0O00OOOOO000O0O .ListItem (name ,iconImage ="DefaultFolder.png",thumbnailImage =iconimage )#line:140
        O0OO0OO00O0O0O000 .setInfo (type ="Video",infoLabels ={"Title":name ,"Plot":description })#line:141
        O0OO0OO00O0O0O000 .setProperty ("Fanart_Image",fanart )#line:142
        OO0O00O000O0OOOOO =OO0O00OOO0OOOO00O .addDirectoryItem (handle =int (O0000OO00OO0O0OOO .argv [1 ]),url =O000OOOOOOO00OO0O ,listitem =O0OO0OO00O0O0O000 ,isFolder =False )#line:143
        return OO0O00O000O0OOOOO #line:144
def get_params ():#line:146
        OO0OO000OO0O00O00 =[]#line:147
        O0O0OO0O00O0OOOOO =O0000OO00OO0O0OOO .argv [2 ]#line:148
        if len (O0O0OO0O00O0OOOOO )>=2 :#line:149
                O0000O00OO0O000O0 =O0000OO00OO0O0OOO .argv [2 ]#line:150
                OOO0000OOOOO0O00O =O0000O00OO0O000O0 .replace ('?','')#line:151
                if (O0000O00OO0O000O0 [len (O0000O00OO0O000O0 )-1 ]=='/'):#line:152
                        O0000O00OO0O000O0 =O0000O00OO0O000O0 [0 :len (O0000O00OO0O000O0 )-2 ]#line:153
                O0OO0O0OOO0O0O00O =OOO0000OOOOO0O00O .split ('&')#line:154
                OO0OO000OO0O00O00 ={}#line:155
                for O0OO0000OO0OOOO0O in range (len (O0OO0O0OOO0O0O00O )):#line:156
                        OOO0OOO0000OO00OO ={}#line:157
                        OOO0OOO0000OO00OO =O0OO0O0OOO0O0O00O [O0OO0000OO0OOOO0O ].split ('=')#line:158
                        if (len (OOO0OOO0000OO00OO ))==2 :#line:159
                                OO0OO000OO0O00O00 [OOO0OOO0000OO00OO [0 ]]=OOO0OOO0000OO00OO [1 ]#line:160
        return OO0OO000OO0O00O00 #line:162
params =get_params ()#line:164
url =None #line:165
name =None #line:166
mode =None #line:167
iconimage =None #line:168
fanart =None #line:169
description =None #line:170
try :#line:172
        url =OO0OO0O0O00OO0O0O .unquote_plus (params ["url"])#line:173
except :#line:174
        pass #line:175
try :#line:176
        name =OO0OO0O0O00OO0O0O .unquote_plus (params ["name"])#line:177
except :#line:178
        pass #line:179
try :#line:180
        iconimage =OO0OO0O0O00OO0O0O .unquote_plus (params ["iconimage"])#line:181
except :#line:182
        pass #line:183
try :#line:184
        mode =int (params ["mode"])#line:185
except :#line:186
        pass #line:187
try :#line:188
        fanart =OO0OO0O0O00OO0O0O .unquote_plus (params ["fanart"])#line:189
except :#line:190
        pass #line:191
try :#line:192
        description =OO0OO0O0O00OO0O0O .unquote_plus (params ["description"])#line:193
except :#line:194
        pass #line:195
OO00OO0OO00O000OO .log (str (PATH )+' '+str (VERSION ))#line:197
OO00OO0OO00O000OO .log ("Mode: "+str (mode ))#line:198
OO00OO0OO00O000OO .log ("Name: "+str (name ))#line:200
def setView (content ,viewType ):#line:203
    if content :#line:204
       OO0O00OOO0OOOO00O .setContent (int (O0000OO00OO0O0OOO .argv [1 ]),content )#line:205
    if ADDON .getSetting ('auto-view')=='true':#line:206
       O0O0OO0OO0OO00OO0 .executebuiltin ("Container.SetViewMode(%s)"%ADDON .getSetting (viewType ))#line:207
if mode ==None or url ==None or len (url )<1 :#line:209
   WIZARDS ()#line:210
elif mode ==1 :#line:212
     wizard (name ,url ,description )#line:213
OO0O00OOO0OOOO00O .endOfDirectory (int (O0000OO00OO0O0OOO .argv [1 ]))