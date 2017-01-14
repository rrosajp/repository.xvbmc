# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Documentaries on YouTube by coldkeys
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.Allesin1NL!'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCLFLMHOWrWo0j6BXa2sbzBA/playlists"
YOUTUBE_CHANNEL_ID_2 = "UC1IP4Z_Vk08aRXuund9JABQ/playlists"
YOUTUBE_CHANNEL_ID_3 = "UCRuMH46tSZKjkCgeOtBVJzA/playlists"
YOUTUBE_CHANNEL_ID_4 = "UCgolxyJTkhCUYXDTR758XxA/playlists"
YOUTUBE_CHANNEL_ID_5 = "UCvL4gb8hiw74-Os1hJyCLIg/playlists"
YOUTUBE_CHANNEL_ID_6 = "onlinefilmskijken"





# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Live Music",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://www.country-muzika.cz/ikona_3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NL serie ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://cdn.marketplaceimages.windowsphone.com/v8/images/72385295-b52e-40a5-b095-70d254592b7d?imageType=ws_icon_large",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NL kids",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://cms-tc.pbskids.org/global/show-icons/circle/400x400_oddSquad_show_circle.png?mtime=20160621150946",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NL docu",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://icons.iconarchive.com/icons/lajonard/movie-folder/256/Documentary-icon.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="NL Cabaret",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQaTcZhBZcPQV1ZOWPjIpEgfqzwyaTgCXtB40Jsxbwqf9jtfgKh",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Xvbmc handleidingen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-Kyyiux7fXFo/AAAAAAAAAAI/AAAAAAAAAAA/YdLc90hVGO8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
   
		
		

    
run()
