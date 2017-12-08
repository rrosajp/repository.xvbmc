import base64 as O000OO00O0O0O0OOO ,os as OOOOO0OOO00O00OOO ,re as O00OOOO0O000OO0O0 ,sys as O0000OO0OOO0OO00O ,time as OOOO0O000OO00OO0O ,xbmc as O0O0000OO0000O0O0 ,xbmcaddon as O00O0000O0OOO0OOO ,xbmcgui as O00O0O000O0O0000O ,xbmcplugin as OO0OOOO0OO0O000OO #line:9
import plugintools as OOO0O0OO000OOO0O0 #line:10
import urllib as OO000O0000000OOO0 ,urllib2 as O0OOOOOO0OO00000O #line:11
addonID ='plugin.video.epicjijbuis'#line:13
ADDON =O00O0000O0OOO0OOO .Addon (id =addonID )#line:14
addon_id ='plugin.video.epicjijbuis'#line:16
addonInfo =O00O0000O0OOO0OOO .Addon ().getAddonInfo #line:17
AddonTitle ='XvBMC Nederland'#line:18
addonPath =OOOOO0OOO00O00OOO .path .join (OOOOO0OOO00O00OOO .path .join (O0O0000OO0000O0O0 .translatePath ('special://home'),'addons'),'plugin.video.epicjijbuis')#line:19
base ='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'#line:20
BASEURL ="https://bit.ly/XvBMC-Pi"#line:21
dialog =O00O0O000O0O0000O .Dialog ()#line:22
local =O00O0000O0OOO0OOO .Addon (id =addonID )#line:23
icon =local .getAddonInfo ('icon')#line:24
icondir =local .getAddonInfo ('icon')#line:25
fanart =local .getAddonInfo ('fanart')#line:26
fanartdir =local .getAddonInfo ('fanart')#line:27
artwork =O0O0000OO0000O0O0 .translatePath (OOOOO0OOO00O00OOO .path .join ('special://home','addons',addonID ,'/'))#line:29
epicartwrk =O000OO00O0O0O0OOO .b64decode (base )+'plugin.video.epicjijbuis/ART/'#line:31
noxartwork =O000OO00O0O0O0OOO .b64decode (base )+'plugin.video.noxmusic/'#line:32
redartwork =O000OO00O0O0O0OOO .b64decode (base )+'plugin.video.redmusic/'#line:33
Terug ="[COLOR dimgray]<<<back[/COLOR]"#line:34
whoami ="[COLOR dimgray]\[B],,[/B]/ (^_^) \[B],,[/B]/[/COLOR]    [COLOR white]EPiC[/COLOR] JijBuis [COLOR white][B]C[/B][/COLOR]an't [COLOR white][B]B[/B][/COLOR]e [COLOR white][B]S[/B][/COLOR]topped    [COLOR dimgray]\[B],,[/B]/ (^_^) \[B],,[/B]/[/COLOR]"#line:35
def addonIcon ():#line:37
    return artwork +'icon.png'#line:38
YOUTUBE_CHANNEL_ID_1 ="UCeR1Vv0VULfsNDIk0-lO4pA/playlists"#line:40
YOUTUBE_CHANNEL_ID_2 ="UCVX6eEeIIScwApzNs7Uuvug/playlists"#line:41
YOUTUBE_CHANNEL_ID_3 ="DanceTrippinOfficial"#line:42
YOUTUBE_CHANNEL_ID_4 ="UCw39ZmFGboKvrHv4n6LviCA"#line:43
YOUTUBE_CHANNEL_ID_5 ="PLZ1f3amS4y1ffYEhGZDtawaEyRQQu69Bw"#line:44
YOUTUBE_CHANNEL_ID_6 ="detop40"#line:45
YOUTUBE_CHANNEL_ID_7 ="PLFgquLnL59alDqvbikpe5jUhFa_lLl8_H"#line:46
def infoDialog (OOO00000OOO0O0000 ,OO0OO0O0O0000O0OO =addonInfo ('name'),O0OO00O00OO0O0OOO =addonIcon (),O0000OOO0O000OOO0 =3000 ):#line:48
    try :#line:49
        dialog .notification (OO0OO0O0O0000O0OO ,OOO00000OOO0O0000 ,O0OO00O00OO0O0OOO ,O0000OOO0O000OOO0 ,sound =False )#line:50
    except :#line:51
        execute ("Notification(%s,%s, %s, %s)"%(OO0OO0O0O0000O0OO ,OOO00000OOO0O0000 ,O0000OOO0O000OOO0 ,O0OO00O00OO0O0OOO ))#line:52
def okDialog (O0O0O0O0OO00O0O00 ,OO000O000O00OOO0O ,OOOO0OOO0O0O0OOOO ,O0O0O0O00O000O0O0 =addonInfo ('name')):#line:54
    return dialog .ok (O0O0O0O00O000O0O0 ,O0O0O0O0OO00O0O00 ,OO000O000O00OOO0O ,OOOO0OOO0O0O0OOOO )#line:55
def yesnoDialog (OOOO0OO0OOOO000OO ,OOOOOOOO00OOOOOOO ,O0000O0OOOOO0OOOO ,OOO0000OOO00OO000 =addonInfo ('name'),O0O0O0OOOOO0OOOO0 ='',OOOOOOO0OO0O00000 =''):#line:57
    return dialog .yesno (OOO0000OOO00OO000 ,OOOO0OO0OOOO000OO ,OOOOOOOO00OOOOOOO ,O0000O0OOOOO0OOOO ,O0O0O0OOOOO0OOOO0 ,OOOOOOO0OO0O00000 )#line:58
noxmusicchannellist =[("Armin van Buuren","user/arminvanbuuren",'https://yt3.ggpht.com/-bp-G-1ubrMA/AAAAAAAAAAI/AAAAAAAAAAA/lysFIFc6AaQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),("DJ Kensel Official","channel/UCSP9jzPSR8n4_BD15PJIyEA",'https://yt3.ggpht.com/-6kRR5mlPbf4/AAAAAAAAAAI/AAAAAAAAAAA/tbEH9cBPh7c/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Hardwell","user/robberthardwell",'https://yt3.ggpht.com/-1T1SCHCg1FQ/AAAAAAAAAAI/AAAAAAAAAAA/8FY0PMmPr3I/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Martin Garrix","user/MartinGarrix",'https://yt3.ggpht.com/-KRv6BJdFwk8/AAAAAAAAAAI/AAAAAAAAAAA/pQpuy_-RPhE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Tiesto","user/officialtiesto",'https://yt3.ggpht.com/-IKUxTd9MtfU/AAAAAAAAAAI/AAAAAAAAAAA/b26T9-6Y2qU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Venus Music","channel/UCwfMdhb-f02OsYR8T78aKeQ",'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),("W&W","user/WandWmusic",'https://yt3.ggpht.com/-XUlyqOk4meY/AAAAAAAAAAI/AAAAAAAAAAA/5I2gEh7OJ2Y/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),("DeepSense","user/MrDeepSense",'https://yt3.ggpht.com/-U15Ut65AO3I/AAAAAAAAAAI/AAAAAAAAAAA/wG_JGLcud7U/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Keep It Underground","user/aliasmike2002",'https://yt3.ggpht.com/--SezWJJO8q0/AAAAAAAAAAI/AAAAAAAAAAA/5SzkvVF1gZ8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Spectrum Music","user/SpectrumRecordings",'https://yt3.ggpht.com/-vzLxO7i5Qgk/AAAAAAAAAAI/AAAAAAAAAAA/NvJaOyJCRGE/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Deep Space House","user/DeepSpaceHouse",'https://yt3.ggpht.com/-YFwLXVl_Vqc/AAAAAAAAAAI/AAAAAAAAAAA/XjzlD4yTbNk/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Deep House Amsterdam","user/DeepHouseAmsterdam",'https://yt3.ggpht.com/-INq4Js7Kn4c/AAAAAAAAAAI/AAAAAAAAAAA/E1hfqVmqVu8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Indefinitely","channel/UC3xS7KD-nL8dpireWEUIxNA",'https://yt3.ggpht.com/-v-1eCp72Tfo/AAAAAAAAAAI/AAAAAAAAAAA/Ms6e0w5cEb8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Viet Melodic","channel/UCqaay_q0YERQBEg4o5EjvZw",'https://yt3.ggpht.com/-U9lOTob88oI/AAAAAAAAAAI/AAAAAAAAAAA/s-MRRhKbRxA/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Deep Territory","channel/UCnfmB-zAnhvM13i8CczCA6g/featured",'https://yt3.ggpht.com/-QTChEDkSUEk/AAAAAAAAAAI/AAAAAAAAAAA/EGo9VWg3jJk/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("XDeep Music","channel/UCSSEXzYHBijpCPJdiZbS7mw",'https://yt3.ggpht.com/-kS8xy0vSVDU/AAAAAAAAAAI/AAAAAAAAAAA/bggfl99bU7o/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Best Car Music Mixes","channel/UC830NkyfSaql_EFNkmtSXxQ",'https://yt3.ggpht.com/-yzl2Jg0nISI/AAAAAAAAAAI/AAAAAAAAAAA/Vy0ZnBcpNF4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("DjRegard","channel/UCw39ZmFGboKvrHv4n6LviCA",'https://yt3.ggpht.com/-Z6Mnb8qdA7A/AAAAAAAAAAI/AAAAAAAAAAA/CeU6rdpFLHI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Dj Drop G","channel/UCPg3xfvygstC-AkG2Fg3ZXw",'https://yt3.ggpht.com/-0cirbz4I_PU/AAAAAAAAAAI/AAAAAAAAAAA/7nigAQzB9Tc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("DJ ekki Music","user/DJEkkiMusic",'https://yt3.ggpht.com/-q2uL4uvohU8/AAAAAAAAAAI/AAAAAAAAAAA/dz13xu82IaA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Deep Mix Nation","user/DeepMixNation",'https://yt3.ggpht.com/-BA3TEtJOooQ/AAAAAAAAAAI/AAAAAAAAAAA/Jg3jjzr73Ec/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Deep House Nation","channel/UCwfMdhb-f02OsYR8T78aKeQ",'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("The Deep Sky","channel/UCiwb-9kJYSsfLU23u6-67mw",'https://yt3.ggpht.com/-OpItHD85Yek/AAAAAAAAAAI/AAAAAAAAAAA/Dxtacpi3R3U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Miss Deep Mix","channel/UCT_v9nbT8As4mclOg_WK1-w",'https://yt3.ggpht.com/-F6jOzGq1tlU/AAAAAAAAAAI/AAAAAAAAAAA/kTdpRJWn6bw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Maximise Deep","channel/UC3oQei6hjfNt9PF3B0PnwAQ",'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Major Deep","channel/UCuyc9llVi6_49OF_yx4NtZw",'https://yt3.ggpht.com/-B3-wWU7pbaQ/AAAAAAAAAAI/AAAAAAAAAAA/_oXKAnEwopU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Deep House Club","channel/UCDS_jKale8ThWLwGRB15oow",'https://yt3.ggpht.com/-xnkcEn0aKIc/AAAAAAAAAAI/AAAAAAAAAAA/B_SyhGZZxak/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Pulse Musification","user/PulseMusicification",'https://yt3.ggpht.com/-OJ6LMm0FIPk/AAAAAAAAAAI/AAAAAAAAAAA/dw61QOyY8RA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Club House Music","user/DJGosha4TdiRadio",'https://yt3.ggpht.com/-6Y_rcQ4QotA/AAAAAAAAAAI/AAAAAAAAAAA/iHSKU-T1usg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Best Music","channel/UComEqi_pJLNcJzgxk4pPz_A",'https://yt3.ggpht.com/-xIs9J9XA4hQ/AAAAAAAAAAI/AAAAAAAAAAA/4ktYY9TcTb0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Electro Dance Mixes","user/Spart2",'https://yt3.ggpht.com/-nevFJT9TzUk/AAAAAAAAAAI/AAAAAAAAAAA/w8nCecBOHy0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Only Music Hits TV","user/OnlyMusicHitsTV11",'https://yt3.ggpht.com/-D_Dt4745g04/AAAAAAAAAAI/AAAAAAAAAAA/WDvmapj0Lic/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Dj Daniel Sky","channel/UC7Jr5B5todkiLE-1l32JYDQ",'https://yt3.ggpht.com/-cZo2zaoXK2w/AAAAAAAAAAI/AAAAAAAAAAA/iPXcyvOAXnc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Eric Clapman","user/ericclapman",'https://yt3.ggpht.com/-HIVzO-P_Rk4/AAAAAAAAAAI/AAAAAAAAAAA/XPzAMMq2EpY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Electro Dance Movement","user/ElectroDanceMovement",'https://yt3.ggpht.com/-rnymhxYBlaU/AAAAAAAAAAI/AAAAAAAAAAA/ECz2jWvUodA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Crunkz","user/TheCrunkiiyz",'https://yt3.ggpht.com/-Se6L7HBPnLU/AAAAAAAAAAI/AAAAAAAAAAA/aE3VbVfFvqc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("The Deep Sky","channel/UCiwb-9kJYSsfLU23u6-67mw",'https://yt3.ggpht.com/-OpItHD85Yek/AAAAAAAAAAI/AAAAAAAAAAA/Dxtacpi3R3U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Base Deep","channel/UC6LRklglaoc2ywIwmcv21qQ",'https://yt3.ggpht.com/-RzQd-nnVVHI/AAAAAAAAAAI/AAAAAAAAAAA/Iz9UCjJlcD4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("DEEP ZONE","channel/UCfNwCpAb1ZH4rpKMyUsvRIg",'https://yt3.ggpht.com/-FIpPIRSkYm8/AAAAAAAAAAI/AAAAAAAAAAA/_Wq0iMcwEbQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Feel The Sound","channel/UCg5XZgxVytarljBn4ueKqkg",'https://yt3.ggpht.com/-WNYR4e_2O9Y/AAAAAAAAAAI/AAAAAAAAAAA/5lnXVY-n_Bk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),("Ahmet KILIC","user/djahmet008",'https://yt3.ggpht.com/-c_Yi_sSVLDw/AAAAAAAAAAI/AAAAAAAAAAA/4jj4Z4_7Dbo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),]#line:103
def addDir (O00O0O0O000O000O0 ,O00O0OO0O0O00OOO0 ,O000000O000O00OO0 ,OOO0O0OO00O0O0OO0 ,O0O0000OOO00OOO00 ,OO0OOOOOOOO0OOOOO ):#line:105
        O0O0O00OOO00O0OO0 =O0000OO0OOO0OO00O .argv [0 ]+"?url="+OO000O0000000OOO0 .quote_plus (O00O0OO0O0O00OOO0 )+"&mode="+str (O000000O000O00OO0 )+"&name="+OO000O0000000OOO0 .quote_plus (O00O0O0O000O000O0 )+"&iconimage="+OO000O0000000OOO0 .quote_plus (OOO0O0OO00O0O0OO0 )+"&fanart="+OO000O0000000OOO0 .quote_plus (O0O0000OOO00OOO00 )+"&description="+OO000O0000000OOO0 .quote_plus (OO0OOOOOOOO0OOOOO )#line:106
        OOO000O00O0OO0OO0 =True #line:107
        O0OO0OOO000OOO0OO =O00O0O000O0O0000O .ListItem (O00O0O0O000O000O0 ,iconImage ="DefaultFolder.png",thumbnailImage =OOO0O0OO00O0O0OO0 )#line:108
        O0OO0OOO000OOO0OO .setInfo (type ="Video",infoLabels ={"Title":O00O0O0O000O000O0 ,"Plot":OO0OOOOOOOO0OOOOO })#line:109
        O0OO0OOO000OOO0OO .setProperty ("Fanart_Image",O0O0000OOO00OOO00 )#line:110
        if O000000O000O00OO0 ==1 :#line:111
            OOO000O00O0OO0OO0 =OO0OOOO0OO0O000OO .addDirectoryItem (handle =int (O0000OO0OOO0OO00O .argv [1 ]),url =O0O0O00OOO00O0OO0 ,listitem =O0OO0OOO000OOO0OO ,isFolder =False )#line:112
        elif O000000O000O00OO0 ==2 :#line:113
            OOO000O00O0OO0OO0 =OO0OOOO0OO0O000OO .addDirectoryItem (handle =int (O0000OO0OOO0OO00O .argv [1 ]),url =O0O0O00OOO00O0OO0 ,listitem =O0OO0OOO000OOO0OO ,isFolder =False )#line:114
        elif O000000O000O00OO0 ==69 :#line:115
            OOO000O00O0OO0OO0 =OO0OOOO0OO0O000OO .addDirectoryItem (handle =int (O0000OO0OOO0OO00O .argv [1 ]),url =O0O0O00OOO00O0OO0 ,listitem =O0OO0OOO000OOO0OO ,isFolder =False )#line:116
        else :#line:117
            OOO000O00O0OO0OO0 =OO0OOOO0OO0O000OO .addDirectoryItem (handle =int (O0000OO0OOO0OO00O .argv [1 ]),url =O0O0O00OOO00O0OO0 ,listitem =O0OO0OOO000OOO0OO ,isFolder =True )#line:118
        return OOO000O00O0OO0OO0 #line:119
def disabled ():#line:121
    okDialog ('[COLOR orange]add-on by [B]X[/B]v[B]BMC Nederland[/B]:[/COLOR]','','[COLOR lime]goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')#line:122
def epicxvbmcnl ():#line:125
    OOO0O0OO000OOO0O0 .log ("XvBMC.epicxvbmcnl")#line:126
    O0O000O0OOO0000OO =OOO0O0OO000OOO0O0 .get_params ()#line:129
    OO00000O00000OO00 =None #line:131
    OO00OO00O0OO0O0O0 =None #line:132
    OO00O0OO0000OOOO0 =None #line:133
    OO00O0OO00OO0OOOO =None #line:134
    OO0OO0O0OOO0OO0OO =None #line:135
    O00OOOO0OOOO0O000 =None #line:136
    try :OO00000O00000OO00 =OO000O0000000OOO0 .unquote_plus (O0O000O0OOO0000OO ["url"])#line:137
    except :pass #line:138
    try :OO00OO00O0OO0O0O0 =OO000O0000000OOO0 .unquote_plus (O0O000O0OOO0000OO ["name"])#line:139
    except :pass #line:140
    try :OO00O0OO00OO0OOOO =OO000O0000000OOO0 .unquote_plus (O0O000O0OOO0000OO ["iconimage"])#line:141
    except :pass #line:142
    try :OO00O0OO0000OOOO0 =int (O0O000O0OOO0000OO ["mode"])#line:143
    except :pass #line:144
    try :OO0OO0O0OOO0OO0OO =OO000O0000000OOO0 .unquote_plus (O0O000O0OOO0000OO ["fanart"])#line:145
    except :pass #line:146
    try :O00OOOO0OOOO0O000 =OO000O0000000OOO0 .unquote_plus (O0O000O0OOO0000OO ["description"])#line:147
    except :pass #line:148
    OOO0O0OO000OOO0O0 .log ("EPiC "+str (AddonTitle ))#line:150
    if OO00O0OO0000OOOO0 ==None or OO00000O00000OO00 ==None or len (OO00000O00000OO00 )<1 :main_list (O0O000O0OOO0000OO )#line:157
    elif OO00O0OO0000OOOO0 ==1 :O0O0000OO0000O0O0 .executebuiltin ('Action(back)')#line:158
    elif OO00O0OO0000OOOO0 ==2 :disabled ()#line:159
    elif OO00O0OO0000OOOO0 ==3 :NoxMusic ()#line:160
    elif OO00O0OO0000OOOO0 ==4 :randomizer (O0O000O0OOO0000OO )#line:161
    else :#line:162
        pass #line:165
    OOO0O0OO000OOO0O0 .close_item_list ()#line:167
def main_list (OO00O0OO0O00OO0OO ):#line:171
    setView ('movies','EPiC')#line:172
    OOO0O0OO000OOO0O0 .log ("XvBMC.main_list "+repr (OO00O0OO0O00OO0OO ))#line:173
    addDir (whoami ,BASEURL ,2 ,icondir ,fanartdir ,'')#line:174
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:175
    OOO0O0OO000OOO0O0 .add_item (title ="[B][COLOR white]EP[/B][COLOR dodgerblue]i[/COLOR][B]C[/B][/COLOR] [COLOR dimgray][B]M[/B]usic [B]V[/B]ideo [B]C[/B]hannel[/COLOR]",url ="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1 +"/",thumbnail =icon ,fanart =epicartwrk +'hooligan.jpg',folder =True )#line:183
    OOO0O0OO000OOO0O0 .add_item (title ="  -  Rockabilly/Psychobilly [COLOR dimgray](allesin1nl)[/COLOR]",url ="plugin://plugin.video.youtube/playlist/PLPXmmKS-D--bd_OBbxpqVAQPiCXnFacx7/",thumbnail =epicartwrk +'rockabella.png',fanart =epicartwrk +'rockabilly.jpg',folder =True )#line:190
    OOO0O0OO000OOO0O0 .add_item (title ="  -  Rock AM Ring [COLOR dimgray](allesin1nl)[/COLOR]",url ="plugin://plugin.video.youtube/playlist/PLPXmmKS-D--aRKdAID0t_7t6hP_FLncPj/",thumbnail =epicartwrk +'rockAMring.png',fanart =epicartwrk +'RaR.jpg',folder =True )#line:197
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:198
    addDir ('TOP40 | Miscellaneous | Various | Full Concerts | and more...',BASEURL ,4 ,epicartwrk +'cbs.png',epicartwrk +'CBS.jpg','')#line:200
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:202
    OOO0O0OO000OOO0O0 .add_item (title ="[COLOR red][8bit][/COLOR] RetroBit Music [COLOR dimgray](.:C.T.R.L:.)[/COLOR]",url ="plugin://plugin.video.youtube/playlist/PLxQ6orh4rPn6F2ZkpEYlZ6VyopXNuGmQT/",thumbnail =epicartwrk +'8bit.png',fanart =epicartwrk +'RetroBits.jpg',folder =True )#line:209
    addDir ('[COLOR dimgray][B]\'[/B][/COLOR][COLOR white]N[/COLOR]ox [COLOR white]M[/COLOR]usic[COLOR dimgray][B]\'[/B][/COLOR][B]  - [/B]Deep House, trance, electro... [COLOR dimgray](XvBMC-NL)[/COLOR]',BASEURL ,3 ,noxartwork +'icon.png',noxartwork +'fanart.jpg','')#line:210
    OOO0O0OO000OOO0O0 .add_item (title ="Alles in [COLOR orange] [B]1 [/B][/COLOR]NL[B] - [/B]Live Music [COLOR dimgray](XvBMC-NL)[/COLOR]",url ="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2 +"/",thumbnail ="https://archive.org/download/fanart_20170116/Live%20Music%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:217
    OOO0O0OO000OOO0O0 .add_item (title ="Alles in [COLOR orange] [B]1 [/B][/COLOR]NL[B] - [/B]DanceTrippin TV [COLOR dimgray](XvBMC-NL)[/COLOR]",url ="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3 +"/",thumbnail ="https://archive.org/download/fanart_20170116/DanceIcon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:224
    OOO0O0OO000OOO0O0 .add_item (title ="Carpool Karaoke by James Corden & guests [COLOR dimgray](XvBMC-NL)[/COLOR]",url ="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5 +"/",thumbnail ="http://i4.mirror.co.uk/incoming/article4843959.ece/ALTERNATES/s615b/James-Corden.jpg",fanart =O000OO00O0O0O0OOO .b64decode (base )+'plugin.video.carpool-karaoke/'+'fanart.jpg',folder =True )#line:231
    OOO0O0OO000OOO0O0 .add_item (title ="DjRegard Official [COLOR dimgray](XvBMC-NL)[/COLOR]",url ="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4 +"/",thumbnail ="https://yt3.ggpht.com/-Z6Mnb8qdA7A/AAAAAAAAAAI/AAAAAAAAAAA/CeU6rdpFLHI/s900-c-k-no-rj-c0xffffff/photo.jpg",fanart =O000OO00O0O0O0OOO .b64decode (base )+'plugin.video.djRegard/'+'fanart.jpg',folder =True )#line:238
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:240
    addDir (Terug ,BASEURL ,1 ,icondir ,fanartdir ,'')#line:241
    addDir ('',BASEURL ,69 ,icondir ,fanartdir ,'')#line:242
def NoxMusic ():#line:244
    setView ('movies','EPiC')#line:245
    OOO0O0OO000OOO0O0 .log ("XvBMC.Nox_list")#line:246
    addDir (whoami ,BASEURL ,2 ,icondir ,fanartdir ,'')#line:247
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:248
    for O0O0OO00O0OO00OOO ,OOO00000OOOOOOOOO ,O000000000OOOO0OO in noxmusicchannellist :#line:250
        OOO0O0OO000OOO0O0 .add_item (title =O0O0OO00O0OO00OOO ,url ="plugin://plugin.video.youtube/"+OOO00000OOOOOOOOO +"/",thumbnail =O000000000OOOO0OO ,fanart =O000000000OOOO0OO ,folder =True )#line:251
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:253
    addDir (Terug ,BASEURL ,1 ,icondir ,fanartdir ,'')#line:254
    addDir ('',BASEURL ,69 ,icondir ,fanartdir ,'')#line:255
def randomizer (OOOO0O0000O0O0OO0 ):#line:257
    setView ('movies','EPiC')#line:258
    OOO0O0OO000OOO0O0 .log ("XvBMC.Random_list "+repr (OOOO0O0000O0O0OO0 ))#line:259
    addDir (whoami ,BASEURL ,2 ,icondir ,fanartdir ,'')#line:260
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:261
    OOO0O0OO000OOO0O0 .add_item (title ="Miscellaneous \'Full Concerts\' [COLOR dimgray](\'ik doe een gok\' [COLOR white];-p[/COLOR])[/COLOR]",url ='plugin://plugin.video.youtube/search/?q=full+concert&sp=CAMSBhABGAIgAQ%253D%253D',thumbnail =icon ,fanart =fanart ,folder =True )#line:269
    OOO0O0OO000OOO0O0 .add_item (title ="[COLOR white]NL[/COLOR][B] - [/B]Top 40 [COLOR dimgray](\'playlist\\afspeellijst\' is het complete overzicht)[/COLOR]",url ="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6 +"/",thumbnail =epicartwrk +'top40.png',fanart =epicartwrk +'LP40.jpg',folder =True )#line:276
    OOO0O0OO000OOO0O0 .add_item (title ="[COLOR white]NL[/COLOR][B] - [/B]Populairste \"random\" youtube tracks [COLOR dimgray]  (popular music)[/COLOR]",url ="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7 +"/",thumbnail =epicartwrk +'topNL.png',fanart =epicartwrk +'headphones40.jpg',folder =True )#line:283
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:284
    OOO0O0OO000OOO0O0 .add_item (title ="[COLOR red][B]R[/B][/COLOR]ed[COLOR red] [B]M[/B][/COLOR]usic -MusicHits[B]\'[/B]17- Best Songs Playlist [COLOR dimgray](OneLoveCunt)[/COLOR]",url ="plugin://plugin.video.youtube/playlist/PLw-VjHDlEOgvtnnnqWlTqByAtC7tXBg6D/",thumbnail =redartwork +'icon.png',fanart =redartwork +'fanart.jpg',folder =True )#line:291
    addDir ('',BASEURL ,2 ,icondir ,fanartdir ,'')#line:293
    addDir (Terug ,BASEURL ,1 ,icondir ,fanartdir ,'')#line:294
    addDir ('',BASEURL ,69 ,icondir ,fanartdir ,'')#line:295
def setView (OO0000OO0O0OO00OO ,O00000OOO00OO0000 ):#line:297
    if OO0000OO0O0OO00OO :#line:299
        OO0OOOO0OO0O000OO .setContent (int (O0000OO0OOO0OO00O .argv [1 ]),OO0000OO0O0OO00OO )#line:300
    if local .getSetting ('auto-view')=='true':#line:301
        O0O0000OO0000O0O0 .executebuiltin ("Container.SetViewMode(%s)"%local .getSetting (O00000OOO00OO0000 ))#line:302
epicxvbmcnl ()#line:304
"""
    IF you copy/paste this please keep the credits -2- XvBMC-NL (and Coldkeys), Thx.
"""