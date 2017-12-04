#!/usr/bin/python
import base64 as OO0000O0OO00O0O0O ,os as OO0OO0O0000O0OOO0 ,re as O00OO000OO0OO0O0O ,sys as O0000000O0OOOOO0O ,xbmc as OO0000O000OO00O00 ,xbmcaddon as OO0OOOO0O0O0000O0 ,xbmcgui as OOO00OO000O00O0O0 ,xbmcplugin as O00O00000O0OOOO00 #line:11
import plugintools as O000O0O0O00O0O00O #line:12
addonID ='plugin.video.Allesin1NL!'#line:14
addon_id ='plugin.video.Allesin1NL!'#line:15
AddonTitle ='plugin.video.Allesin1NL!'#line:17
local =OO0OOOO0O0O0000O0 .Addon (id =addonID )#line:18
icon =local .getAddonInfo ('icon')#line:19
fanart =local .getAddonInfo ('fanart')#line:20
def gasdrop ():#line:23
    O000O0O0O00O0O00O .log ("XvBMC.VoOdOo")#line:24
    if AddonTitle =="plugin.video.Allesin1NL!":#line:26
        O00O0O0O0000O0OO0 =OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5kb2tpbmw=')#line:27
        OO0O000OO000000O0 =OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS54LW9kaS5ubA==')#line:28
        OO000OO0000OOO000 =OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5raWprYWxsZXMubmw=')#line:29
        OOOOOO00O0O00O000 =OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5lYWdsZQ==')#line:30
        OO0O0O00OOO000000 =OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5kaXRpc3R2')#line:31
        OOO00OO0O000OOOOO =OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS50dmFkZG9ucy5ubA==')#line:32
        OO000O000OO0000OO =[OO000OO0000OOO000 ,OO0O0O00OOO000000 ,OO0O000OO000000O0 ,OOOOOO00O0O00O000 ,O00O0O0O0000O0OO0 ,OOO00OO0O000OOOOO ]#line:33
        O000O0O0OOOOO000O =any (OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O0O0000O00OO000OO ))for O0O0000O00OO000OO in OO000O000OO0000OO )#line:34
        if O000O0O0OOOOO000O :#line:35
            OOO00OO000O00O0O0 .Dialog ().notification ('[COLOR red][B]WAARSCHUWING: [/B]niet ondersteund protocol[/COLOR]','Afhankelijkheden niet voldaan. Verwijder [B]\'bad addons\'[/B].')#line:36
            return False #line:37
        OOO0000OOOO000OO0 =O000O0O0O00O0O00O .get_params ()#line:40
        if OOO0000OOOO000OO0 .get ("action")is None :#line:42
            hoofdlijst (OOO0000OOOO000OO0 )#line:43
        else :#line:44
            OO00O0O0OOOOO00O0 =OOO0000OOOO000OO0 .get ("action")#line:45
        O000O0O0O00O0O00O .close_item_list ()#line:47
    else :#line:49
        OOO0000OOOO000OO0 =O000O0O0O00O0O00O .get_params ()#line:52
        if OOO0000OOOO000OO0 .get ("action")is None :#line:54
            hoofdlijst (OOO0000OOOO000OO0 )#line:55
        else :#line:56
            OO00O0O0OOOOO00O0 =OOO0000OOOO000OO0 .get ("action")#line:57
        O000O0O0O00O0O00O .close_item_list ()#line:58
def hoofdlijst (OO000OOO0OOO0O000 ):#line:61
    if OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(repository.xvbmc)'):#line:62
        setView ('movies','EPiC')#line:64
        O00O00OOOOOO0OO0O =OO0000O0OO00O0O0O .b64decode ('L3BsYXlsaXN0cw==')#line:66
        O0O00000OOOOOO00O =OO0000O0OO00O0O0O .b64decode ('VUNWWDZlRWVJSVNjd0Fwek5zN1V1dnVn')+O00O00OOOOOO0OO0O #line:67
        OOOO00000OO0000OO =OO0000O0OO00O0O0O .b64decode ('VUNCcERKVWxUeGR4bnI4b1FwNGZXOGpB')+O00O00OOOOOO0OO0O #line:68
        OOO0O0O0O0OO0000O =OO0000O0OO00O0O0O .b64decode ('VUMtWjhua2hwRzdEUXZPOHdlZ01IR0lR')+O00O00OOOOOO0OO0O #line:69
        O0O00OO0OOOO00O0O =OO0000O0OO00O0O0O .b64decode ('VUNfeHc2WUJubHlMcVlub3BhYmJ6ZmlR')+O00O00OOOOOO0OO0O #line:71
        OO0O0000000O0O000 =OO0000O0OO00O0O0O .b64decode ('VUNKWTRFRDdCb2NWa3RpekFUa0VMM0Z3')+O00O00OOOOOO0OO0O #line:72
        OOO0000000OOOO0O0 =OO0000O0OO00O0O0O .b64decode ('VUN2TDRnYjhoaXc3NC1PczFoSnlDTEln')+O00O00OOOOOO0OO0O #line:73
        O00000OOOO00OO0O0 =OO0000O0OO00O0O0O .b64decode ("b25saW5lZmlsbXNraWprZW4=")#line:74
        O0OOOO000OO000OO0 =OO0000O0OO00O0O0O .b64decode ('VUNyLUpCQzFYUHFKbV9POWlSMk0wV2pn')+O00O00OOOOOO0OO0O #line:75
        O000OOOOO0OO0O0OO =OO0000O0OO00O0O0O .b64decode ('VUNoVndOQzI0aklsdTk4RzByR0Z0UVpR')+O00O00OOOOOO0OO0O #line:77
        OOO0O00OOO00OOO00 =OO0000O0OO00O0O0O .b64decode ('VUMybjVBTTd2QWNNZVc4U0xta2pDZW5n')+O00O00OOOOOO0OO0O #line:78
        O0OOOOOOOOOOO0OO0 =OO0000O0OO00O0O0O .b64decode ('VUMzY3h2UEYxbWZ1MWF2ZEhPNlk5Tm53')+O00O00OOOOOO0OO0O #line:79
        O0O000O0OO00O000O =OO0000O0OO00O0O0O .b64decode ('VUMxa05lNTdGLTg1dHJyWUM3dGJPU1hB')+O00O00OOOOOO0OO0O #line:80
        OO0OO000OOOOO0O0O =OO0000O0OO00O0O0O .b64decode ('VUNVZnNyU0w2RHlXU2trcGRkbFkyMS1R')+O00O00OOOOOO0OO0O #line:81
        O00OOO0OO0OOOO0O0 =OO0000O0OO00O0O0O .b64decode ('RGFuY2VUcmlwcGluT2ZmaWNpYWw=')#line:82
        O0OOOO00OOOO0OO00 =OO0000O0OO00O0O0O .b64decode ('L3VzZXIv')#line:83
        O0OO0O0O000O0OOO0 =OO0000O0OO00O0O0O .b64decode ('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmU=')#line:85
        O00OO0OO00OO0OOO0 =OO0000O0OO00O0O0O .b64decode ('L2NoYW5uZWwv')#line:86
        O000O0O0O00O0O00O .log ("XvBMC.hoofdlijst "+repr (OO000OOO0OOO0O000 ))#line:87
        O000O0O0O00O0O00O .add_item (title ="Live Music",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +O0O00000OOOOOO00O +poster ,thumbnail ="https://archive.org/download/fanart_20170116/Live%20Music%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:95
        O000O0O0O00O0O00O .add_item (title ="NL Series",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +OOOO00000OO0000OO +poster ,thumbnail ="https://archive.org/download/fanart_20170116/NL%20SERIE%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:102
        O000O0O0O00O0O00O .add_item (title ="NL Kids",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +OOO0O0O0O0OO0000O +poster ,thumbnail ="https://archive.org/download/fanart_20170116/NL%20KIDS%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:109
        O000O0O0O00O0O00O .add_item (title ="NL Films",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +O0O00OO0OOOO00O0O +poster ,thumbnail ="https://archive.org/download/fanart_20170116/NL%20FILM%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:123
        O000O0O0O00O0O00O .add_item (title ="NL Docu",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +OO0O0000000O0O000 +poster ,thumbnail ="https://archive.org/download/fanart_20170116/NL%20Docu%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:130
        O000O0O0O00O0O00O .add_item (title ="NL Cabaret",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +OOO0000000OOOO0O0 +poster ,thumbnail ="https://archive.org/download/fanart_20170116/NL%20CABARET%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:137
        O000O0O0O00O0O00O .add_item (title ="Xvbmc Handleidingen",url =O0OO0O0O000O0OOO0 +O0OOOO00OOOO0OO00 +O00000OOOO00OO0O0 +poster ,thumbnail ="https://archive.org/download/fanart_20170116/Xvbmc%20handleidingen%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:144
        O000O0O0O00O0O00O .add_item (title ="Vlaamse Content",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +O0OOOO000OO000OO0 +poster ,thumbnail ="https://archive.org/download/fanart_20170116/Vlaams%20icon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:151
        O000O0O0O00O0O00O .add_item (title =".:C.T.R.L:. Gaming Room",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +O000OOOOO0OO0O0OO +poster ,thumbnail ="https://archive.org/download/fanart_20170116/CtrlGamingIcon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:165
        O000O0O0O00O0O00O .add_item (title ="Cirque du soleil",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +OOO0O00OOO00OOO00 +poster ,thumbnail ="https://archive.org/download/fanart_20170116/CircusIcon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:172
        O000O0O0O00O0O00O .add_item (title ="NL Racing",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +O0OOOOOOOOOOO0OO0 +poster ,thumbnail ="https://archive.org/download/fanart_20170116/NlRacing.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:179
        O000O0O0O00O0O00O .add_item (title ="Van alles en nog wat NL",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +O0O000O0OO00O000O +poster ,thumbnail ="https://archive.org/download/fanart_20170116/vanalles.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:186
        O000O0O0O00O0O00O .add_item (title ="Muziek Uit Limburg",url =O0OO0O0O000O0OOO0 +O00OO0OO00OO0OOO0 +OO0OO000OOOOO0O0O +poster ,thumbnail ="https://archive.org/download/fanart_20170116/NlLimburgIcon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:193
        O000O0O0O00O0O00O .add_item (title ="DanceTrippin TV",url =O0OO0O0O000O0OOO0 +O0OOOO00OOOO0OO00 +O00OOO0OO0OOOO0O0 +poster ,thumbnail ="https://archive.org/download/fanart_20170116/DanceIcon.png",fanart ="https://archive.org/download/fanart_20170116/fanart.jpg",folder =True )#line:200
    else :#line:201
        OOO00OO000O00O0O0 .Dialog ().notification ('[COLOR red][B]WARNING: [/B]unsupported protocol(plugin)[/COLOR]','Dependencies not met. Missing XvBMC repo.')#line:202
        return False #line:203
def setView (O00OOO00OOO00000O ,OO0O00OOO0O00OOO0 ):#line:205
    global poster #line:209
    poster =OO0000O0OO00O0O0O .b64decode ('Lw==')#line:210
    if O00OOO00OOO00000O :#line:211
        O00O00000O0OOOO00 .setContent (int (O0000000O0OOOOO0O .argv [1 ]),O00OOO00OOO00000O )#line:212
    if local .getSetting ('auto-view')=='true':#line:213
        OO0000O000OO00O00 .executebuiltin ("Container.SetViewMode(%s)"%local .getSetting (OO0O00OOO0O00OOO0 ))#line:214
def cache ():#line:216
    global AddonTitle #line:218
    O0O0O00O0OOOOO000 =OO0000O0OO00O0O0O .b64decode ('c2tpbi5ub3g0YmVnaW5uZXJz')#line:219
    O00OOO00OO0OO0O0O =OO0000O0OO00O0O0O .b64decode ('c2tpbi5rYW9zYm94')#line:220
    if OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O0O0O00O0OOOOO000 )):#line:222
        AddonTitle ='plugin.video.Allesin1NL'#line:224
        gasdrop ()#line:225
    elif OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O00OOO00OO0OO0O0O +'.beta')):#line:226
        gasdrop ()#line:228
    elif OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O00OOO00OO0OO0O0O +'.helix')):#line:229
        gasdrop ()#line:231
    elif OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O00OOO00OO0OO0O0O +'2.jarvis')):#line:232
        gasdrop ()#line:234
    elif OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O00OOO00OO0OO0O0O +'.krypton')):#line:235
        gasdrop ()#line:237
    elif OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O00OOO00OO0OO0O0O +'2.krypton')):#line:238
        gasdrop ()#line:240
    else :#line:241
        OO000O00OO0O0O0OO =[OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5raWprYWxsZXMubmw='),OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5kaXRpc3R2'),OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS54LW9kaS5ubA=='),OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5lYWdsZQ=='),OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS5kb2tpbmw='),OO0000O0OO00O0O0O .b64decode ('cmVwb3NpdG9yeS50dmFkZG9ucy5ubA==')]#line:251
        O0OO0O00O00O00000 =any (OO0000O000OO00O00 .getCondVisibility ('System.HasAddon(%s)'%(O0OO00000O0OOOO00 ))for O0OO00000O0OOOO00 in OO000O00OO0O0O0OO )#line:252
        if not O0OO0O00O00O00000 :#line:253
            gasdrop ()#line:256
        else :#line:257
            OO0000O000OO00O00 .executebuiltin ('Notification([COLOR red][B]WARNING: [/B]unsupported \'build\\addon(s)\'.[/COLOR],Dependencies not met. Evil add-on(s) found.,5000,DefaultIconError.png)')#line:259
            return False #line:260
cache ()