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
YOUTUBE_CHANNEL_ID_4 = "PLCIsXw_Mafxx50E-2BIwk_yD86SuKGqqr"
YOUTUBE_CHANNEL_ID_5 = "PLCIsXw_Mafxzz4RJHR66XBW6Qwn4Q8k_8"
YOUTUBE_CHANNEL_ID_6 = "PLCIsXw_Mafxy9_YqhXMmZHvbiX_vXRPep"
YOUTUBE_CHANNEL_ID_7 = "PLCIsXw_MafxxV9Nsc3YP8Bzo5i3YxdjXY"
YOUTUBE_CHANNEL_ID_8 = "PLCIsXw_MafxyRrqIAwnQ-TFR-WERh9Y_k"
YOUTUBE_CHANNEL_ID_9 = "PLCIsXw_Mafxyuhsf3et4Jk8pExifLUilA"
YOUTUBE_CHANNEL_ID_10 = "PLCIsXw_MafxyIqugrkv2r7273MfqL576I"
YOUTUBE_CHANNEL_ID_11 = "PLCIsXw_Mafxy0RIr3VcrAlDeyau5PjAhR"
YOUTUBE_CHANNEL_ID_12 = "PLCIsXw_Mafxz9Ir1j6IrkkAGigB1yGc-C"
YOUTUBE_CHANNEL_ID_13 = "PLCIsXw_MafxxFuSfvvO8Gu_UXkxOIQuob"


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
    plugintools.add_item( 
        #action="", 
        title="Psychedelic Trance ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://www.cloudbooster.net/files/covers/art-301264-1374372607.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="RAP/HIP HOP",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://rappingmanual.com/wp-content/uploads/2013/01/black-and-white-rapper.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="R and B",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.ytimg.com/vi/m9-28iScx-E/hqdefault.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Electric ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://static1.squarespace.com/static/55dbc2ede4b022e7c5f90797/t/55dca91ee4b058c024dc9ffb/1440524578656/?format=300w",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="PUNK ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://d.ibtimes.co.uk/en/full/1393518/rebellion-punk-festival-blackpool.jpg?w=800",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Dance ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://i.ytimg.com/vi/LgCdQS3p04Y/maxresdefault.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="trance",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://i.ytimg.com/vi/2Q6e9GmIe-4/maxresdefault.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Heavy metal ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://comicsalliance.com/files/2014/03/Heavy-Metal-Magazine.png",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="alternative Rock ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://www.emute-music.com/wp-content/uploads/photo1-2-600x600.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://i.ytimg.com/vi/ohvFCSTgTus/maxresdefault.jpg",
        folder=True )
    
run()
