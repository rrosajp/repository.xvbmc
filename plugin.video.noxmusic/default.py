# -*- coding: utf-8 -*-
#----------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon, added some XvBMC vOoDoO
#----------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon

addonID  = 'plugin.video.noxmusic'
addon_id = 'plugin.video.noxmusic'
local    = xbmcaddon.Addon(id=addonID)
icon     = local.getAddonInfo('icon')


channellist=[
        
        ("Armin van Buuren", "user/arminvanbuuren", 'https://yt3.ggpht.com/-bp-G-1ubrMA/AAAAAAAAAAI/AAAAAAAAAAA/lysFIFc6AaQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DJ Kensel Official", "channel/UCSP9jzPSR8n4_BD15PJIyEA", 'https://yt3.ggpht.com/-6kRR5mlPbf4/AAAAAAAAAAI/AAAAAAAAAAA/tbEH9cBPh7c/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Hardwell", "user/robberthardwell", 'https://yt3.ggpht.com/-1T1SCHCg1FQ/AAAAAAAAAAI/AAAAAAAAAAA/8FY0PMmPr3I/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Martin Garrix", "user/MartinGarrix", 'https://yt3.ggpht.com/-KRv6BJdFwk8/AAAAAAAAAAI/AAAAAAAAAAA/pQpuy_-RPhE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Tiesto", "user/officialtiesto", 'https://yt3.ggpht.com/-IKUxTd9MtfU/AAAAAAAAAAI/AAAAAAAAAAA/b26T9-6Y2qU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Venus Music", "channel/UCwfMdhb-f02OsYR8T78aKeQ", 'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("W&W", "user/WandWmusic", 'https://yt3.ggpht.com/-XUlyqOk4meY/AAAAAAAAAAI/AAAAAAAAAAA/5I2gEh7OJ2Y/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DeepSense", "user/MrDeepSense", 'https://yt3.ggpht.com/-U15Ut65AO3I/AAAAAAAAAAI/AAAAAAAAAAA/wG_JGLcud7U/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Keep It Underground", "user/aliasmike2002", 'https://yt3.ggpht.com/--SezWJJO8q0/AAAAAAAAAAI/AAAAAAAAAAA/5SzkvVF1gZ8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Spectrum Music", "user/SpectrumRecordings", 'https://yt3.ggpht.com/-vzLxO7i5Qgk/AAAAAAAAAAI/AAAAAAAAAAA/NvJaOyJCRGE/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep Space House", "user/DeepSpaceHouse", 'https://yt3.ggpht.com/-YFwLXVl_Vqc/AAAAAAAAAAI/AAAAAAAAAAA/XjzlD4yTbNk/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep House Amsterdam", "user/DeepHouseAmsterdam", 'https://yt3.ggpht.com/-INq4Js7Kn4c/AAAAAAAAAAI/AAAAAAAAAAA/E1hfqVmqVu8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Indefinitely", "channel/UC3xS7KD-nL8dpireWEUIxNA", 'https://yt3.ggpht.com/-v-1eCp72Tfo/AAAAAAAAAAI/AAAAAAAAAAA/Ms6e0w5cEb8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Viet Melodic", "channel/UCqaay_q0YERQBEg4o5EjvZw", 'https://yt3.ggpht.com/-U9lOTob88oI/AAAAAAAAAAI/AAAAAAAAAAA/s-MRRhKbRxA/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep Territory", "channel/UCnfmB-zAnhvM13i8CczCA6g/featured", 'https://yt3.ggpht.com/-QTChEDkSUEk/AAAAAAAAAAI/AAAAAAAAAAA/EGo9VWg3jJk/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("XDeep Music", "channel/UCSSEXzYHBijpCPJdiZbS7mw", 'https://yt3.ggpht.com/-kS8xy0vSVDU/AAAAAAAAAAI/AAAAAAAAAAA/bggfl99bU7o/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Best Car Music Mixes", "channel/UC830NkyfSaql_EFNkmtSXxQ", 'https://yt3.ggpht.com/-yzl2Jg0nISI/AAAAAAAAAAI/AAAAAAAAAAA/Vy0ZnBcpNF4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DjRegard", "channel/UCw39ZmFGboKvrHv4n6LviCA", 'https://yt3.ggpht.com/-Z6Mnb8qdA7A/AAAAAAAAAAI/AAAAAAAAAAA/CeU6rdpFLHI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Dj Drop G", "channel/UCPg3xfvygstC-AkG2Fg3ZXw", 'https://yt3.ggpht.com/-0cirbz4I_PU/AAAAAAAAAAI/AAAAAAAAAAA/7nigAQzB9Tc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DJ ekki Music", "user/DJEkkiMusic", 'https://yt3.ggpht.com/-q2uL4uvohU8/AAAAAAAAAAI/AAAAAAAAAAA/dz13xu82IaA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep Mix Nation", "user/DeepMixNation", 'https://yt3.ggpht.com/-BA3TEtJOooQ/AAAAAAAAAAI/AAAAAAAAAAA/Jg3jjzr73Ec/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep House Nation", "channel/UCwfMdhb-f02OsYR8T78aKeQ", 'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("The Deep Sky", "channel/UCiwb-9kJYSsfLU23u6-67mw", 'https://yt3.ggpht.com/-OpItHD85Yek/AAAAAAAAAAI/AAAAAAAAAAA/Dxtacpi3R3U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Miss Deep Mix", "channel/UCT_v9nbT8As4mclOg_WK1-w", 'https://yt3.ggpht.com/-F6jOzGq1tlU/AAAAAAAAAAI/AAAAAAAAAAA/kTdpRJWn6bw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Maximise Deep", "channel/UC3oQei6hjfNt9PF3B0PnwAQ", 'https://yt3.ggpht.com/-IPOer-Fbz-Y/AAAAAAAAAAI/AAAAAAAAAAA/8NAHhG3Ho9s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Major Deep", "channel/UCuyc9llVi6_49OF_yx4NtZw", 'https://yt3.ggpht.com/-B3-wWU7pbaQ/AAAAAAAAAAI/AAAAAAAAAAA/_oXKAnEwopU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Deep House Club", "channel/UCDS_jKale8ThWLwGRB15oow", 'https://yt3.ggpht.com/-xnkcEn0aKIc/AAAAAAAAAAI/AAAAAAAAAAA/B_SyhGZZxak/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Pulse Musification", "user/PulseMusicification", 'https://yt3.ggpht.com/-OJ6LMm0FIPk/AAAAAAAAAAI/AAAAAAAAAAA/dw61QOyY8RA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Club House Music", "user/DJGosha4TdiRadio", 'https://yt3.ggpht.com/-6Y_rcQ4QotA/AAAAAAAAAAI/AAAAAAAAAAA/iHSKU-T1usg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),    
        ("Best Music", "channel/UComEqi_pJLNcJzgxk4pPz_A", 'https://yt3.ggpht.com/-xIs9J9XA4hQ/AAAAAAAAAAI/AAAAAAAAAAA/4ktYY9TcTb0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Electro Dance Mixes", "user/Spart2", 'https://yt3.ggpht.com/-nevFJT9TzUk/AAAAAAAAAAI/AAAAAAAAAAA/w8nCecBOHy0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Only Music Hits TV", "user/OnlyMusicHitsTV11", 'https://yt3.ggpht.com/-D_Dt4745g04/AAAAAAAAAAI/AAAAAAAAAAA/WDvmapj0Lic/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Dj Daniel Sky", "channel/UC7Jr5B5todkiLE-1l32JYDQ", 'https://yt3.ggpht.com/-cZo2zaoXK2w/AAAAAAAAAAI/AAAAAAAAAAA/iPXcyvOAXnc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Eric Clapman", "user/ericclapman", 'https://yt3.ggpht.com/-HIVzO-P_Rk4/AAAAAAAAAAI/AAAAAAAAAAA/XPzAMMq2EpY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Electro Dance Movement", "user/ElectroDanceMovement", 'https://yt3.ggpht.com/-rnymhxYBlaU/AAAAAAAAAAI/AAAAAAAAAAA/ECz2jWvUodA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Crunkz", "user/TheCrunkiiyz", 'https://yt3.ggpht.com/-Se6L7HBPnLU/AAAAAAAAAAI/AAAAAAAAAAA/aE3VbVfFvqc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("The Deep Sky", "channel/UCiwb-9kJYSsfLU23u6-67mw", 'https://yt3.ggpht.com/-OpItHD85Yek/AAAAAAAAAAI/AAAAAAAAAAA/Dxtacpi3R3U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Base Deep", "channel/UC6LRklglaoc2ywIwmcv21qQ", 'https://yt3.ggpht.com/-RzQd-nnVVHI/AAAAAAAAAAI/AAAAAAAAAAA/Iz9UCjJlcD4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("DEEP ZONE", "channel/UCfNwCpAb1ZH4rpKMyUsvRIg", 'https://yt3.ggpht.com/-FIpPIRSkYm8/AAAAAAAAAAI/AAAAAAAAAAA/_Wq0iMcwEbQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Feel The Sound", "channel/UCg5XZgxVytarljBn4ueKqkg", 'https://yt3.ggpht.com/-WNYR4e_2O9Y/AAAAAAAAAAI/AAAAAAAAAAA/5lnXVY-n_Bk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Ahmet KILIC", "user/djahmet008", 'https://yt3.ggpht.com/-c_Yi_sSVLDw/AAAAAAAAAAI/AAAAAAAAAAA/4jj4Z4_7Dbo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
]

# XvBMC_entry-point
def run():
    plugintools.log("XvBMC-NL_NoxMusic.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
    
    plugintools.close_item_list()

# XvBMC_main-menu
def main_list(params):
    plugintools.log("XvBMC-NL_NoxMusic.main_list "+repr(params))

for name, id, icon in channellist:
    plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )

# XvBMC_vOoDoO
run()