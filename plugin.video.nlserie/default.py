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
YOUTUBE_CHANNEL_ID_10 = "PLyYNo9oKWshnDRCflX_23rDSUUfTWBgXO"
YOUTUBE_CHANNEL_ID_11 = "PLWBViXeuU3BQW9A0RQfOtcVkFxPzme40F"
YOUTUBE_CHANNEL_ID_12 = "PLaMj5vGrVDhb70q-Jrlptpg6rvM9DZCAI"
YOUTUBE_CHANNEL_ID_13 = "PLCIsXw_MafxzoLO19X133gfZTg13nQILS"
YOUTUBE_CHANNEL_ID_14 = "PLNxtqH1GOIexgloGsZlgDa8enrh0WA_RV"
YOUTUBE_CHANNEL_ID_15 = "PLNxtqH1GOIexMJRadpqURRR0KMeiJ5G9E"
YOUTUBE_CHANNEL_ID_16 = "PLNxtqH1GOIex_at9PFMGODNzvbv74JxDb"
YOUTUBE_CHANNEL_ID_17 = "PLvNkTAcwO96uXz9-YrWL68Xk5-6a4XMRi"
YOUTUBE_CHANNEL_ID_18 = "PLy5rcNpbQclYs5fwELE--O0yRsaDIT6CO"
YOUTUBE_CHANNEL_ID_19 = "PLCIsXw_MafxxDEFWg1mvGNETmsNuadOsb"
YOUTUBE_CHANNEL_ID_20 = "PLYnW3FZd9OHXVfyfrpgqFGrHgy07pBws7&jct"
YOUTUBE_CHANNEL_ID_21 = "PLIgOmwxt2ejARXgZtlHn15xaq9IPrXo3E"
YOUTUBE_CHANNEL_ID_22 = "PLCIsXw_Mafxymdpf7ORzXbm8oQ16nWggM"
YOUTUBE_CHANNEL_ID_23 = "PL9FADAFE0E13B9592"
YOUTUBE_CHANNEL_ID_24 = "PL93_4h9baNvOKPSwNPLc0ye9agfteowfq"
YOUTUBE_CHANNEL_ID_25 = "PL93_4h9baNvPqOASecEJl4H2XGZDoYq9N"
YOUTUBE_CHANNEL_ID_26 = "PLpQLeVJYet03N-edfQ4RY7P_CrT-YDGH5"
YOUTUBE_CHANNEL_ID_27 = "PLpQLeVJYet01BNcDeqwAmzO17w98T6Vm-"
YOUTUBE_CHANNEL_ID_28 = "PLWBViXeuU3BRj8AZtuJcILZzXVBqD4dLD"
YOUTUBE_CHANNEL_ID_29 = "PLCIsXw_Mafxx6seo-SMqX0DHr_mh5kCkB"


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
        title="De co-assistent Seizoen 4",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://www.studenten.net/images/default-source/legacy/recensie-de-co-assistent-seizoen-1.jpg",
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
    plugintools.add_item( 
        #action="", 
        title="zeg eens A",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/564x/22/43/ee/2243eee431a10c8e928544e8e550318f.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Overspel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/0/0/2/7/9200000021937200.jpg",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="Smeris s01",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://www.pupkin.com/media/images/thumbs/projectItem/a4-poster-smeris_projectItem_images3_poster.png",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Smeris s02",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://www.pupkin.com/media/images/thumbs/projectItem/a4-poster-smeris_projectItem_images3_poster.png",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="UNIT 13",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://www.tvvantoen.nl/wp-content/themes/website/data/php/timthumb.php?src=http://www.tvvantoen.nl/wp-content/uploads/unit-13.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Flikken Gent Seizoenen 1 t/m 10",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/4/8/4/9/9200000064469484.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="GTST week overzichten",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://www.startpagina.nl/athene/dochters/gtst/thumbs/GTST%20logo%202011.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="De ZevenSprong",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://www.nlfilmdoek.nl/wp-content/uploads/2011/09/hoes5.jpg",
        folder=True )				
    plugintools.add_item( 
        #action="", 
        title="FC De Kampioenen - Alle seizoenen 1-21",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/8/1/1/4/1002004010634118.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Witse s01-s09",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://tasted4you.be/wp-content/uploads/2015/12/witse-300x297.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Van Spijek",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://www.nlfilmdoek.nl/wp-content/uploads/2011/09/vanspeijk.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Toen was geluk heel gewoon s01 t/m s07 ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://cdn4.static.ovimg.com/m/0gfxt_r/?width=150",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Kinderen geen bezwaar ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase/large/FC/8/7/4/9/9200000014669478.jpg",
        folder=True )				
    plugintools.add_item( 
        #action="", 
        title="De allerslechte chauffeur van Nederland s1-2",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://isveni.com/upload/image/canadas_worst_driver_s07e06_5.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Najib Amhali",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://www.theatersinnederland.nl/wp-content/uploads/2014/11/Najib-Amhali.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Charlie Seizoen 1",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/2/1/4/8/9200000013998412.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Costa s01-03",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://s.s-bol.com/imgbase0/imagebase3/large/FC/3/5/0/1/9200000016321053.jpg",
        folder=True )		
run()
