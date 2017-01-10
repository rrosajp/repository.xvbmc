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

addonID = 'plugin.video.livemusic!'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLBg1SJiXSxfLVPyurUABbIMUkhphmq7i5"
YOUTUBE_CHANNEL_ID_2 = "PLCIsXw_Mafxz59cG6Jmgqn-Z03CghrL-N"
YOUTUBE_CHANNEL_ID_3 = "PLCIsXw_MafxxDlt5LYbJNiuMKs-uZeWC6"



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
        title="ULTRA LIVE SETS",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://www.house4dj.com/wp-content/uploads/2013/03/Ultra-600x300.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="POP",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK8Ggpq60snVO5qtortwkAxUaMaCIGjdfUOOhprtM8QWvgZpj5hw",
	    folder=True )
		
		
    plugintools.add_item( 
        #action="", 
        title="Metal hardcore ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQtNXw8sCKXLhapEsTrrZ7kRkcPU02JCNx37_oNqX1cJFevibXUOL6Tkpo",
        folder=True )	
    

    
run()
