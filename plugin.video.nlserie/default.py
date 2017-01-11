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
YOUTUBE_CHANNEL_ID_4 = "PLWBViXeuU3BTbGFAA3b3wigJkdlWzHx2B"
YOUTUBE_CHANNEL_ID_5 = "PLWBViXeuU3BQFfmzy6SBF6tRaoPbSZpv9"
YOUTUBE_CHANNEL_ID_6 = "PLWBViXeuU3BQdtgDMMdFq4v8ueEgbeEqX"
YOUTUBE_CHANNEL_ID_7 = "PLWBViXeuU3BQcS44JLIXFSsJxPo0abOLp"
YOUTUBE_CHANNEL_ID_8 = "PLWBViXeuU3BTRDayyQ7XoPqLNNAjJJUrp"
YOUTUBE_CHANNEL_ID_9 = "PLWBViXeuU3BQTY8Kpa4Rrxrs5av0V_zlP"
YOUTUBE_CHANNEL_ID_10 = "PLWBViXeuU3BRj8AZtuJcILZzXVBqD4dLD"
YOUTUBE_CHANNEL_ID_11 = "PLWBViXeuU3BQW9A0RQfOtcVkFxPzme40F"
YOUTUBE_CHANNEL_ID_12 = "PLaMj5vGrVDhb70q-Jrlptpg6rvM9DZCAI"



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
    plugintools.add_item( 
        #action="", 
        title="All Stars Seizoen 1",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase/large/FC/2/4/7/5/1002004004295742.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="All Stars Seizoen 2",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/3/4/7/5/1002004004295743.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="All Stars Seizoen 3",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/4/4/7/5/1002004004295744.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="De co-assistent Seizoen 1",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://www.studenten.net/images/default-source/legacy/recensie-de-co-assistent-seizoen-1.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="De co-assistent Seizoen 2",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://www.studenten.net/images/default-source/legacy/recensie-de-co-assistent-seizoen-1.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="De co-assistent Seizoen 3",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://www.studenten.net/images/default-source/legacy/recensie-de-co-assistent-seizoen-1.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Charlie Seizoen 1",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/2/1/4/8/9200000013998412.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="De Hoofdprijs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://www.nlfilmdoek.nl/wp-content/uploads/2011/09/dehoofdprijs5.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Flodder",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/7/1/2/3/1002004000083217.jpg",
        folder=True )	
    
run()
