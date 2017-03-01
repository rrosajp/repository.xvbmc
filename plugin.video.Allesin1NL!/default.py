# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Credits to coldkeys, Thx.
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import base64,os,sys,xbmc,xbmcaddon,xbmcgui,xbmcplugin,re
import plugintools
from addon.common.addon import Addon

addonID  = 'plugin.video.Allesin1NL!'
addon_id = 'plugin.video.Allesin1NL!'
addon    = Addon(addonID, sys.argv)
local    = xbmcaddon.Addon(id=addonID)
icon     = local.getAddonInfo('icon')
fanart   = local.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID_1 = "UCLFLMHOWrWo0j6BXa2sbzBA/playlists"
YOUTUBE_CHANNEL_ID_2 = "UC1IP4Z_Vk08aRXuund9JABQ/playlists"
YOUTUBE_CHANNEL_ID_3 = "UCRuMH46tSZKjkCgeOtBVJzA/playlists"
YOUTUBE_CHANNEL_ID_4 = "UCFI_PLLqAQeVbV5nKArUjFA/playlists"
YOUTUBE_CHANNEL_ID_5 = "UCgolxyJTkhCUYXDTR758XxA/playlists"
YOUTUBE_CHANNEL_ID_6 = "UCvL4gb8hiw74-Os1hJyCLIg/playlists"
YOUTUBE_CHANNEL_ID_7 = "onlinefilmskijken"
YOUTUBE_CHANNEL_ID_8 = "UCr-JBC1XPqJm_O9iR2M0Wjg/playlists"
YOUTUBE_CHANNEL_ID_9 = "UC_xw6YBnlyLqYnopabbzfiQ/playlists"
YOUTUBE_CHANNEL_ID_10 = "UChVwNC24jIlu98G0rGFtQZQ/playlists"
YOUTUBE_CHANNEL_ID_11 = "UC2n5AM7vAcMeW8SLmkjCeng/playlists"
YOUTUBE_CHANNEL_ID_12 = "UC3cxvPF1mfu1avdHO6Y9Nnw/playlists"
YOUTUBE_CHANNEL_ID_13 = "UC1kNe57F-85trrYC7tbOSXA/playlists"
YOUTUBE_CHANNEL_ID_14 = "UCUfsrSL6DyWSkkpddlY21-Q/playlists"
YOUTUBE_CHANNEL_ID_15 = "DanceTrippinOfficial"

exec((lambda OO00O00OOOO000000 ,OOO0OOO000OO00O00 :(lambda OO0OO00O0O0O0OO00 ,OO0000OO000O0OO0O ,O0O000OO0OO00O00O :re .sub (OO0OO00O0O0O0OO00 ,OO0000OO000O0OO0O ,O0O000OO0OO00O00O ))(r"([0-9a-f]+)",lambda O0O0OOO00O0O0000O :OO00O00OOOO000000 (O0O0OOO00O0O0000O ,OOO0OOO000OO00O00 ),base64 .b64decode ("MzEgMjkgKCk6IzA6MgoJYyAuMjYgKCIyYS4yOSIpIzA6MwoJNCA9ZiAuNDYgKCczNT0nKSMwOjUKCTQzID1mIC40NiAoJzNjPT0nKSMwOjYKCTQ0ID1mIC40NiAoJ2U9JykjMDo3CgkzZiA9ZiAuNDYgKCc0NT0nKSMwOjgKCTQ5ID1mIC40NiAoJzM4JykjMDo5CglhID1bNDQgLDQ5ICw0MyAsM2YgLDQgXSMwOjEwCgk0NyA9MzMgKDJkIC40MCAoJzI4LjM0KCU0OCknJSg0MiApKTMwIDQyIDQxIGEgKSMwOjExCgkyZSA0NyA6IzA6MTIKCQkyMyAuMjQgKCkuMzkgKCdbMWIgMzJdW2JdMTg6IFsvYl0zZCAxYSAxZlsvMWJdJywnMTUgM2QgM2UuIDFkIDNiIDI2LicpIzA6MTMKCQkyNSAyYiAjMDoxNAoJMSA9YyAuMWMgKCkjMDoxNwoJMmUgMSAuMjcgKCIzNiIpM2EgMmMgOiMwOjE5CgkJMWUgKDEgKSMwOjIwCgkyZiA6IzA6MjEKCQkzNyA9MSAuMjcgKCIzNiIpIzA6MjIKCWMgLjE2ICgpCiNk")))(lambda OOO00O0O0O0O000OO ,O0O0OOO0O00O0O000 :O0O0OOO0O00O0O000 [int ("0x"+OOO00O0O0O0O000OO .group (1 ),16 )],"line|O0OO0O00000OOO0O0|2|3|OOO0000O00OO0000O|5|6|7|8|9|OOOOO000OOO0OOOO0|B|plugintools|e9015584e6a44b14988f13e2298bcbf9|cmVwb3NpdG9yeS5raWprYWxsZXMubmw|base64|10|11|12|13|14|Afhankelijkheden|close_item_list|17|WAARSCHUWING|19|ondersteund|COLOR|get_params|Controleer|main_list|protocol|20|21|22|xbmcgui|Dialog|return|log|get|System|run|XvBMC|False|None|xbmc|if|else|for|def|red|any|HasAddon|cmVwb3NpdG9yeS5kb2tpbmw|action|O0OO0O0OOO0000OOO|cmVwb3NpdG9yeS5kaXRpc3R2|notification|is|uw|cmVwb3NpdG9yeS54LW9kaS5ubA|niet|voldaan|OOOOO000O000O0O0O|getCondVisibility|in|O000O0OOOOO00O0O0|OO0OO00000OOOO00O|OO00OO0OO0OOOOO00|cGx1Z2luLnZpZGVvLkNyZWF0aXZlVHZXaXphcmQ|b64decode|OO00O0OOOOO0OOOOO|s|OO00O0OO0OOOOO000".split ("|")))

# Main menu
def main_list(params):
    setView('movies', 'EPiC')
    plugintools.log("XvBMC.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
		title="Live Music",
		url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
		thumbnail="https://archive.org/download/fanart_20170116/Live%20Music%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
		folder=True )
    plugintools.add_item( 
        #action="",
		title="NL Serie ",
		url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
		thumbnail="https://archive.org/download/fanart_20170116/NL%20SERIE%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
		folder=True )
    plugintools.add_item( 
        #action="", 
		title="NL Kids",
		url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
		thumbnail="https://archive.org/download/fanart_20170116/NL%20KIDS%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
		title="NL Film",
		url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
		thumbnail="https://archive.org/download/fanart_20170116/NL%20FILM%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="NL Docu",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://archive.org/download/fanart_20170116/NL%20Docu%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
		folder=True )
    plugintools.add_item( 
        #action="", 
        title="NL Cabaret",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://archive.org/download/fanart_20170116/NL%20CABARET%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Xvbmc Handleidingen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://archive.org/download/fanart_20170116/Xvbmc%20handleidingen%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Vlaamse Content",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://archive.org/download/fanart_20170116/Vlaams%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="NL Sport",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://archive.org/download/fanart_20170116/NL%20Sport%20icon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title=".:C.T.R.L:. Gaming Room",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://archive.org/download/fanart_20170116/CtrlGamingIcon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Cirque du soleil",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://archive.org/download/fanart_20170116/CircusIcon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="NL Racing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://archive.org/download/fanart_20170116/NlRacing.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Van alles en nog wat NL",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://archive.org/download/fanart_20170116/vanalles.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Muziek Uit Limburg",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://archive.org/download/fanart_20170116/NlLimburgIcon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="DanceTrippin TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://archive.org/download/fanart_20170116/DanceIcon.png",
		fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )

def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if local.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % local.getSetting(viewType) )

exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MmYgKChkIDYgLDQgOihkIDUgLDMgLDggOjQyIC4zMiAoNSAsMyAsOCApKSg0OSIoWzAtM2YtZl0rKSIsZCA3IDo2ICg3ICw0ICksMTcgLjEwICgiNDY9IikpKShkIDIgLDkgOjkgWzMzICgiNDAiKzIgLjJiICgxICksMTYgKV0sIjEwfDQ3fDRifDE3fGN8MTR8MTV8ZXw0YXwxOXwxYXxifDExfDEyfDFifDEzfDFkfDFmfDIwfDQxfDE4fDIzfDI0fDI5fDNhfDFjfDMwfDFlfDIxfDIyfDNifDNjfDI1fDM0fDI2fDI4fDJjfDJkfDJlfDJhfDQ1fDMxfDM4fDM2fDM3fDM1fDM5fDNkfDNlfDQzfDQ0fDQ4Ii4yNyAoInwiKSkpCiNh")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|O0OO0OO0OO0000O0O|OO0OO00O00O0OOOO0|O00OOOOOO00O000O0|OOOO00OOO0000000O|OOOOO0O00000OO0O0|OO0000O0O0O0OO0OO|OOOO00O000OO000O0|O00OOO00OOOOO00OO|e9015584e6a44b14988f13e2298bcbf9|B|cmVwb3NpdG9yeS54LW9kaS5ubA|lambda|cmVwb3NpdG9yeS5kaXRpc3R2|f|b64decode|getCondVisibility|DefaultIconError|executebuiltin|has_bad_addon|Dependencies|16|base64|Notification|unsupported|bad_addons|protocol|HasAddon|WARNING|xbmcgui|contact|author|Dialog|return|plugin|Please|System|False|split|alles|addon|COLOR|group|idox|5000|istv|exec|xbmc|else|sub|int|add|oki|png|tvw|for|run|not|red|met|any|RUN|9a|0x|notification|re|if|in|on|YSA9IFsKCTMuMCgnMj0nKSwjMjMgCgkzLjAoJzcnKSwjMjYgCgkzLjAoJzQ9PScpLCMyNCAKCTMuMCgnMT0nKSwjMmMgCgkzLjAoJzg9JykjMmQgCl0KNSA9IDJmKDFhLmMoJzIwLjE5KCUzMyknICUgKDE3KSkgMmEgMTcgMzIgYSkKMzEgMTggNToKICAgIDJlKCkKMjk6CiAgICAjMWIuMWMoKS4xMygnWzI3IDFlXVtiXTEwOiBbL2JdOSBlKDE1KVsvMjddJywnNiAxOCAxZi4gMTYgMTEgMjEtMjggMTIuJykKICAgIDFhLmYoJzE0KFsyNyAxZV1bYl0xMDogWy9iXTkgZSgxNSlbLzI3XSw2IDE4IDFmLiAxNiAxMSAyMS0yOCAxMi4sMjUsZC4yYiknKQkKICAgICMxZCAyMgoKIzMwKCk|cGx1Z2luLnZpZGVvLkNyZWF0aXZlVHZXaXphcmQ|s|r|cmVwb3NpdG9yeS5kb2tpbmw|cmVwb3NpdG9yeS5raWprYWxsZXMubmw".split("|")))