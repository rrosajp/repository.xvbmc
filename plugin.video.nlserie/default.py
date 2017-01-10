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

addonID = 'plugin.video.nlserie'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLa2dv1s0m3fRZck3oOTlkO0zpoJcGbtcv"
YOUTUBE_CHANNEL_ID_2 = "PLW_Aiizr2108sLiCD8obnHQ4Y-ny7YOqn"
YOUTUBE_CHANNEL_ID_3 = "PLUu3ppNddjpr7ZnG-wfqH-D5plL2E-HMZ"




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
        title="als de dijken breken",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://shop.eo.nl/CmsData/Artikelen/Fotos/DDIJK01N/DDIJK01N_mainimage_183_297_1.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Baantjer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://vignette4.wikia.nocookie.net/clan-of-the-undead-civilization-v/images/3/35/Baantjer.png/revision/latest?cb=20141010190516",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="Penoza",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i1.wp.com/www.northflix.nl/wp-content/uploads/2015/08/penoza.png?w=640",
        folder=True )	
    

    
run()
