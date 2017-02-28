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

addonID   = 'plugin.video.epicjijbuis'
addon_id  = 'plugin.video.epicjijbuis'
#ADDON    = xbmcaddon.Addon(id=addon_id)
addon     = Addon(addonID, sys.argv)
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'plugin.video.epicjijbuis')
base      = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'
local     = xbmcaddon.Addon(id=addonID)
icon      = local.getAddonInfo('icon')
fanart    = local.getAddonInfo('fanart')
artwork   = base64.b64decode(base)+'plugin.video.epicjijbuis/ART/'
#fanart   = os.path.join(addonPath, 'fanart.jpg')


YOUTUBE_CHANNEL_ID_1 = "UCeR1Vv0VULfsNDIk0-lO4pA/playlists"
YOUTUBE_CHANNEL_ID_2 = "UCLFLMHOWrWo0j6BXa2sbzBA/playlists"
YOUTUBE_CHANNEL_ID_3 = "DanceTrippinOfficial"
YOUTUBE_CHANNEL_ID_4 = "UCw39ZmFGboKvrHv4n6LviCA"
YOUTUBE_CHANNEL_ID_5 = "PLZ1f3amS4y1ffYEhGZDtawaEyRQQu69Bw"
YOUTUBE_CHANNEL_ID_6 = "detop40"
YOUTUBE_CHANNEL_ID_7 = "PLFgquLnL59alDqvbikpe5jUhFa_lLl8_H"


exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MzYgKChkIDUgLDIgOihkIDggLDMgLDYgOjQwIC4zZSAoOCAsMyAsNiApKSg0OCIoWzAtNDYtZl0rKSIsZCA0IDo1ICg0ICwyICksMWEgLjEwICgiNGQiKSkpKGQgOSAsNyA6NyBbM2EgKCI0MiIrOSAuMmYgKDEgKSwxNiApXSwiMTB8NGN8MWV8NGF8MWF8MTR8Y3wxNXw0M3wxYnwxN3xifGV8MmN8MWR8NDl8Mjh8MTF8MTJ8MTN8MjV8MWN8MTh8MWZ8MjB8MzB8MjF8MmV8MjJ8MjN8MjR8Mzd8MjZ8Mjd8M2Z8MmF8Mjl8M2R8MmJ8MmR8MzJ8MzN8NDd8MzV8MzR8Mzl8M2N8Mzh8M2J8NDR8NDF8NDV8MTl8NGIiLjMxICgifCIpKSkKI2E=")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|O00000O00000OOO0O|O00000OO00OO00OO0|OO000O00O00OO0OO0|OO00000O0OOOOO000|O00O00OOOO0O0O000|OO0OOO00OO00000OO|O00O00O0O0O0OOO00|O00OOOO0O00O00OO0|e9015584e6a44b14988f13e2298bcbf9|B|cmVwb3NpdG9yeS54LW9kaS5ubA|lambda|cmVwb3NpdG9yeS5kaXRpc3R2|f|b64decode|getCondVisibility|Afhankelijkheden|close_item_list|has_crap_stuff|CHANNEL_ID_1|16|CHANNEL_ID_4|WAARSCHUWING|CHANNEL_ID_5|base64|CHANNEL_ID_3|notification|crap_blocker|plugintools|ondersteund|Controleer|get_params|main_list|protocol|HasAddon|gasdrop|xbmcgui|voldaan|action|System|Dialog|return|params|False|COLOR|group|addon|split|XvBMC|xbmc|None|else|exec|niet|for|any|int|def|red|log|sub|get|re|in|0x|CHANNEL_ID_2|is|uw|9a|if|r|cmVwb3NpdG9yeS5kb2tpbmw|cmVwb3NpdG9yeS5raWprYWxsZXMubmw|s|cGx1Z2luLnZpZGVvLkNyZWF0aXZlVHZXaXphcmQ|MzAgMTQoKToKCTIuMjUoIjI4LjE0IikKCgk3ID0gNC4wKCdmPScpCgk4ID0gNC4wKCc2PT0nKQoJOSA9IDQuMCgnMz0nKQoJYSA9IDQuMCgnMT0nKQoJMzQgPSA0LjAoJ2MnKQoJZSAgID0gWzksIDM0LCA4LCBhLCA3XQoJNSA9IDJkKDI5LjExKCcyNC4xZSglMzUpJyAlICgxOSkpIDJmIDE5IDMyIGUpCgkyYSA1OgoJCTIwLjIzKCkuMTUoJ1sxYiAyZV1bYl0xNjogWy9iXTFmIDE3IDFkWy8xYl0nLCcxMiAxZiAyMS4gMTggMzMgMjUuJykgCgkJMjYgMjcKCQoJZCA9IDIuMWEoKQoJCgkyYSBkLjIyKCIxMCIpIDMxIDJjOgoJCTFjKGQpCgkyYjoKCQkxMCA9IGQuMjIoIjEwIikKCQoJMi4xMygp".split("|")))

	
# Main menu
def main_list(params):
    setView('movies', 'EPiC')
    plugintools.log("XvBMC.main_list "+repr(params))

    plugintools.add_item(
        #action="",
        title="[COLOR dimgray]‹^› ‹(•_•)› ‹^›[/COLOR]    [COLOR white]EPiC[/COLOR] JijBuis [COLOR white][B]C[/B][/COLOR]an't [COLOR white][B]B[/B][/COLOR]e [COLOR white][B]S[/B][/COLOR]topped [COLOR red][8bit][/COLOR]    [COLOR dimgray]‹^› ‹(•_•)› ‹^›[/COLOR]",
        url="",
        thumbnail=icon,
        fanart=fanart,
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="EP[COLOR blue][B]i[/B][/COLOR]C [COLOR dimgray]channel[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail=icon,
        fanart=fanart,
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Rockabilly/Psychobilly",
        url="plugin://plugin.video.youtube/playlist/PLCIsXw_MafxyiNLnmwhjIAGRw-5wqD4ch/",
        thumbnail=artwork+'Rockabella.png',
        fanart=artwork+'Rockabilly.jpg',
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Rock AM Ring",
        url="plugin://plugin.video.youtube/playlist/PLCIsXw_Mafxw89kSR93TiqwMax7uVux82/",
        thumbnail=artwork+'rockAMring.png',
        fanart=artwork+'RaR.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red][8bit][/COLOR] RetroBit Music [COLOR dimgray](.:C.T.R.L:.)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/PLxQ6orh4rPn6F2ZkpEYlZ6VyopXNuGmQT/",
        thumbnail=artwork+'8bit.png',
        fanart=artwork+'RetroBits.jpg',
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Miscellaneous \'Full Concerts\' [COLOR dimgray](ik doe een gok [B];-p[/B])[/COLOR]",
        url='plugin://plugin.video.youtube/search/?q=full+concert&sp=CAMSBhABGAIgAQ%253D%253D',
        thumbnail=icon,
        fanart=fanart,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NL[B] - [/B]Top 40 [COLOR dimgray](kies \'playlist\\afspeellijst\' voor complete overzicht)[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail=artwork+'top40.png',
        fanart=artwork+'LP40.jpg',
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="NL[B] - [/B]Populairste \"random\" youtube tracks [COLOR dimgray](popular music)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail=artwork+'topNL.png',
        fanart=artwork+'headphones40.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="\'Allesin[COLOR orange][B]1[/B][/COLOR]NL!\'[B] - [/B]Live Music [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://archive.org/download/fanart_20170116/Live%20Music%20icon.png",
        fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="\'Allesin[COLOR orange][B]1[/B][/COLOR]NL!\' [B]-[/B] DanceTrippin TV [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://archive.org/download/fanart_20170116/DanceIcon.png",
        fanart="https://archive.org/download/fanart_20170116/fanart.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Carpool Karaoke by James Corden & special guests [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://i4.mirror.co.uk/incoming/article4843959.ece/ALTERNATES/s615b/James-Corden.jpg",
        fanart=base64.b64decode(base)+'plugin.video.carpool-karaoke/'+'fanart.jpg',
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="DjRegard Official [COLOR dimgray](XvBMC-NL)[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-Z6Mnb8qdA7A/AAAAAAAAAAI/AAAAAAAAAAA/CeU6rdpFLHI/s900-c-k-no-rj-c0xffffff/photo.jpg",
        fanart=base64.b64decode(base)+'plugin.video.djRegard/'+'fanart.jpg',
        folder=True )


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if local.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % local.getSetting(viewType) )


exec((lambda OO00OO00O000OOO0O ,OOO00OO00OOOOO0O0 :(lambda OO00O0000O0000OO0 ,OO0O0O0O0OO0O00O0 ,OOO00OO0000O0OOOO :re .sub (OO00O0000O0000OO0 ,OO0O0O0O0OO0O00O0 ,OOO00OO0000O0OOOO ))(r"([0-9a-f]+)",lambda O0OO0O00O0OO0OOO0 :OO00OO00O000OOO0O (O0OO0O00O0OO0OOO0 ,OOO00OO00OOOOO0O0 ),base64 .b64decode ("MmMgPVs1IC4wICgnND0nKSw1IC4wICgnMmUnKSw1IC4wICgnMzA9PScpLDUgLjAgKCcxPScpLDUgLjAgKCdhPScpXSMyZjo3CjYgPTIwICgyOCAuYyAoJzFiLjE0KCUyZCknJSgyICkpMjMgMiAyYiAyYyApIzJmOjgKMmEgMWQgNiA6IzJmOjkKCTE3ICgpIzJmOjEwCjFmIDojMmY6MTEKCTI4IC5lICgnMjkoWzEyIDIxXVtiXTE4OiBbL2JdMjcgMTUoMTkpWy8xMl0sZiAxZCAyNS4gMWEgMTYgMjItMjYgMWMuLDFlLGQuMjQpJykjMmY6MTMKCiMz")))(lambda OOOO00O00O0OOOO0O ,O0OOO00O00OOO0OOO :O0OOO00O00OOO0OOO [int ("0x"+OOOO00O00O0OOOO0O .group (1 ),16 )],"b64decode|cGx1Z2luLnZpZGVvLkNyZWF0aXZlVHZXaXphcmQ|OO00OO00OOOO0OOOO|e9015584e6a44b14988f13e2298bcbf9|cmVwb3NpdG9yeS5raWprYWxsZXMubmw|base64|has_bad_addon|7|8|9|cmVwb3NpdG9yeS5kb2tpbmw|B|getCondVisibility|DefaultIconError|executebuiltin|Dependencies|10|11|COLOR|13|HasAddon|protocol|contact|gasdrop|WARNING|plugin|Please|System|author|not|5000|else|any|red|add|for|png|met|on|unsupported|xbmc|Notification|if|in|bad_addons|s|cmVwb3NpdG9yeS5kaXRpc3R2|line|cmVwb3NpdG9yeS54LW9kaS5ubA".split ("|")))