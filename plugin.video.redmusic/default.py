# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/playlist/PLw-VjHDlEOgvtnnnqWlTqByAtC7tXBg6D
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.redmusic'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


# Entry point
def run():
    plugintools.log("redmusic.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("redmusic.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Music Hits 2017 - Best Songs Playlist",
        url="plugin://plugin.video.youtube/playlist/PLw-VjHDlEOgvtnnnqWlTqByAtC7tXBg6D/",
        thumbnail=icon,
        folder=True )

run()