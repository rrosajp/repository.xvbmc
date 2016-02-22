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

addonID = 'plugin.video.party-time!'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLQjtO2fjgHKUL4U4iRmkui8hGxInQsAXU"
YOUTUBE_CHANNEL_ID_2 = "deenis51"
YOUTUBE_CHANNEL_ID_3 = "PLqW-xw4e2GrJCNMaHw-xaE1cN0hHVE_sk"
YOUTUBE_CHANNEL_ID_4 = "PL-yGk9VKloDbffol-LYXxNRQWNBbVEKdJ"
YOUTUBE_CHANNEL_ID_5 = "PLQf0QCXD0Npz2vEVu4qptWQ9HNOegIbad"
YOUTUBE_CHANNEL_ID_6 = "PLQf0QCXD0NpzWpm4n_292i2w7vNx0p1HL"
YOUTUBE_CHANNEL_ID_7 = "PL87A1C7EEBCE2C5BE"
YOUTUBE_CHANNEL_ID_8 = "PL241FDC0B0FC96C90"
YOUTUBE_CHANNEL_ID_9 = "PLdhR_67FhdOKSRGhr59NJfvAFhItSxcy7"
YOUTUBE_CHANNEL_ID_10 = "PLpa_NwtbLxpN0lK-KLCgsNZBu2ZzAC2fb"
YOUTUBE_CHANNEL_ID_11 = "PL6k36l76wA_L6BjumeytdXzOAc0c7LXU9"
YOUTUBE_CHANNEL_ID_12 = "PL96070F8B2DA7D298"
YOUTUBE_CHANNEL_ID_13 = "PLqQSyR3d-fevzP3whM58TzXtnBxE6lvv5"
YOUTUBE_CHANNEL_ID_14 = "PLuoriEIb_dmnaKbqbUdEi-l_yRJaA8eXo"
YOUTUBE_CHANNEL_ID_15 = "PL6_lnat_g-IitxPGVKp8ykrTRhhRmMNYA"
YOUTUBE_CHANNEL_ID_16 = "PLKOXXePgWciOO61ZUSzTDQQGyD_546BGA"
YOUTUBE_CHANNEL_ID_17 = "PLh5Y6tRBALKdBk9bdijJN4K9Lgisu3XUi"
YOUTUBE_CHANNEL_ID_18 = "UCYbAX5VSqgEcLwzJS4k-4Gg"
YOUTUBE_CHANNEL_ID_19 = "PLc7Yv2cfKlFPZiovMII5fAGWROGblgECx"
YOUTUBE_CHANNEL_ID_20 = "PLc7Yv2cfKlFOESUsrbD5RHOlupDd6WRPk"
YOUTUBE_CHANNEL_ID_21 = "PLc7Yv2cfKlFPfSr3AGmhF0mEoaO1mXOYf"
YOUTUBE_CHANNEL_ID_22 = "PLc7Yv2cfKlFO8aMD8cyK3p9aPkW3s8wY4"
YOUTUBE_CHANNEL_ID_23 = "UCDuy-lMZwCgl0m2MoR6r1JA"
YOUTUBE_CHANNEL_ID_24 = "UCG1DdsRO_Pgc45DlSUmL5Cg"
YOUTUBE_CHANNEL_ID_25 = "PLdhR_67FhdOIXcBvXFH61u4snn43br821"
YOUTUBE_CHANNEL_ID_26 = "PLECA8FA17D15EAD90"
YOUTUBE_CHANNEL_ID_27 = "PLDTZz_MRm8Alg9qRG0iIDzQ1R9XOVZcA7"
YOUTUBE_CHANNEL_ID_28 = "PLkW4U4l9-2eZ34E-74pli20NVs-oDgkET"
YOUTUBE_CHANNEL_ID_29 = "UCzLrqgcpWLnlfAmud_pvHkQ/playlists"
YOUTUBE_CHANNEL_ID_30 = "PLy2DZKzbsdAmUlWj7HVgGgz9LQ7kgw_ou"
YOUTUBE_CHANNEL_ID_31 = "PLQjtO2fjgHKWH_QVDAOYohZiJ21VdtLx-"
YOUTUBE_CHANNEL_ID_32 = "PLQjtO2fjgHKWnzrSjIox93Bl7r3GRunR3"
YOUTUBE_CHANNEL_ID_33 = "PLivfvcT4boPaQ5OkYkJuI2JntzrlUkhPf"
YOUTUBE_CHANNEL_ID_34 = "PLZyk5SQHwkKtgyvuZSFLhOOM_TUWPkUuD"
YOUTUBE_CHANNEL_ID_35 = "PL593E3A404EEE9829"
YOUTUBE_CHANNEL_ID_36 = "PL1828054F5D85FB02"
YOUTUBE_CHANNEL_ID_37 = "PLFnF0LpDmVwPfDbx7Ko5eUOgD1PvsKc4I"
YOUTUBE_CHANNEL_ID_38 = "PLoqIMZ8dn0SfDfILhQZQQAeswZeY6mIc1"
YOUTUBE_CHANNEL_ID_39 = "PLwSubaI0YUrsNUmHt-g3HdRsU2pgvrWAd"




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
        title="Qlimax 2015 Live sets",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-S9oh92ajGNM/AAAAAAAAAAI/AAAAAAAAAAA/V_r2_7yYskw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="World of Hardstyle",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-PB5a130en4s/AAAAAAAAAAI/AAAAAAAAAAA/hK03YQ55Tmg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Coone's Global Dedication Podcast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-krs7Db9iNAk/AAAAAAAAAAI/AAAAAAAAAAA/Ue_ZR6RHMlM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="inZanity - The Freestyle Podcast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-cjZJhDhsLEs/AAAAAAAAAAI/AAAAAAAAAAA/02pVp1Xag4w/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="B2S tv season 6",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-SDzReof35B4/AAAAAAAAAAI/AAAAAAAAAAA/HxsezOhV9zc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="B2S tv season 7",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-SDzReof35B4/AAAAAAAAAAI/AAAAAAAAAAA/HxsezOhV9zc/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="B2S Pussy lounge",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-SDzReof35B4/AAAAAAAAAAI/AAAAAAAAAAA/HxsezOhV9zc/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="HARD with STYLE | Presented by Audiofreq",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-n5L_dqv6wAI/AAAAAAAAAAI/AAAAAAAAAAA/SBmcXbiVStc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Brennan Heart presents WE R Hardstyle",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-Ichf908BXCg/AAAAAAAAAAI/AAAAAAAAAAA/YOv2q4JDaa4/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Prophet - Louder Podcast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-CjhVpwtP0H8/AAAAAAAAAAI/AAAAAAAAAAA/CysSwxenoKk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Mc Villain - The Future of Hardstyle*",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-LklIIYOxlwg/AAAAAAAAAAI/AAAAAAAAAAA/LRnGnUsGmps/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Isaac's Hardstyle Sessions",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-POoYrLaAZGU/AAAAAAAAAAI/AAAAAAAAAAA/V2yUMcOJ8zI/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Digital Punk - Unleashed",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-nigon9tvaOQ/AAAAAAAAAAI/AAAAAAAAAAA/MFRY2_jFPkw/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Stephanie's Pink Beats",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-ByBejYBhqug/AAAAAAAAAAI/AAAAAAAAAAA/sC1ZVBIWENQ/s100-c-k-no/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Audiotricz - Infinite",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-8GbPpayGHIA/AAAAAAAAAAI/AAAAAAAAAAA/yPH9T2asqwY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Masters of Hardcore podcast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://www.festivalinfo.nl/img/upload/4/e/Masters_of_Hardcore_2231.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Legendary Podcast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://i1.sndcdn.com/artworks-000089386289-9gi92v-t500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Offensive Hardcore",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://photo.partyflock.nl/images/236680/main/752980.jpg",
        folder=True )
		
	
plugintools.add_item( 
        #action="", 
        title="Offensive Hardcore Documentaires",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://groepje5.files.wordpress.com/2010/09/gabber2.jpg",
        folder=True )
		
		
plugintools.add_item( 
        #action="", 
        title="Nightmare Rotterdam",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://www.nightmare.nl/wordpress/wp-content/uploads/2015/05/240x240.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Project Hardcore",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://i.ytimg.com/vi/3K9ZOeQhT3U/maxresdefault.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Decibel Outdoor",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://www.paylogic.com/media/decibel-outdoor-festival.jpg?v=1396442700",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="GABBERS! 3Doc",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://s1.standaardcdn.be/Assets/Images_Upload/2015/12/03/punk1.jpg?maxheight=416&maxwidth=568&format=jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Gabber: Verleden tot Heden",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://www.mediafonds.nl/image/2013/12/5/schermafbeelding_2013_12_05_om_13_17_33.png(484x)(2C92A29654CE5EE21EA379852C1F8CF0).jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Evolution Of Style - The documentary",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://i.vimeocdn.com/video/443752319.jpg?mw=1920&mh=1080&q=70",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Endymion - Make Some Noise (Documentary & Tour)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://www.dance.nl/uploads/images/articles/org/3125.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="EDM DOCUMENTARIES",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://edmsauce.wpengine.netdna-cdn.com/wp-content/uploads/2014/04/Electronic.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="The Darkraver - More Than 20 years",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://wieno.nl/public_html/wp-content/foto1/2016/01/darkraver-logo.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="The Darkraver - Steve Sweet",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://i.ytimg.com/vi/e7zQF8g77bA/maxresdefault.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Reverze Illumination   (2015 Live Sets)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://www.reverze.be/reverze-illumination.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Defqon.1 2015 Live Sets",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://www.planetzone.nl/wp-content/uploads/2015/06/QCD010_Defqon.1-2015-cover-600x6001.jpeg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Defqon.1 2015 | The Gathering at BLACK",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="http://farm8.staticflickr.com/7124/7440605270_51c25aff56.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Hardcore Italia Podcast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://i.ytimg.com/vi/15JuFXLONek/maxresdefault.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Thunderdome die hard warmup & day",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/6/6c/Thunderdome_logo.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Gabber docu's",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://partyflock.nl/images/upload/11881_regularo.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Decibel Outdoor B2S",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="http://www.b2s.nl/v2/public/themes/decibel/images/news_default.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Hardcore Dvd's",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="http://cdn.discogs.com/RVQ2W9tnCCjN8aitrLv6vs3O8UQ=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb()/discogs-images/R-568046-1152190793.jpeg.jpg",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Qlimax 2013/2012/2011",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://www.jr24.in/wp-content/uploads/2014/05/cover2.png",
        folder=True )
		
plugintools.add_item( 
        #action="", 
        title="Hard Bass 2013/2012",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="http://s3-eu-west-1.amazonaws.com/btrb-prd-flyers/hx65ix70pi47.jpg",
        folder=True )
		
		

    
run()
