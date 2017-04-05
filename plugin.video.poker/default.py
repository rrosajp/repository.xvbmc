# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
#from addon.common.addon import Addon

addonID  = 'plugin.video.poker'
addon_id = 'plugin.video.poker'#plugintools.py
#addon   = Addon(addonID, sys.argv)
local    = xbmcaddon.Addon(id=addonID)
icon     = local.getAddonInfo('icon')


channellist=[
        ("Big Slick AK", "channel/UCKOMhwQMA5IYHt4WsjM4nQQ", 'https://yt3.ggpht.com/-QGGIzT5ox-4/AAAAAAAAAAI/AAAAAAAAAAA/LJE7YhoQRyY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Party Time Poker", "channel/UCw-uVoosoY7HgxdhCxiyGGA", 'https://yt3.ggpht.com/-vHRWkkGBNQU/AAAAAAAAAAI/AAAAAAAAAAA/OcMVNqyVLw0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Pokerstars", "user/Pokerstars", 'https://yt3.ggpht.com/-bN8xA6QxFao/AAAAAAAAAAI/AAAAAAAAAAA/czFMxbvmSxU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),	
        ("Poker School TV", "user/kamnerobot", 'https://yt3.ggpht.com/-BMtx55pK3Fw/AAAAAAAAAAI/AAAAAAAAAAA/7VlriAq39ms/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("World Series", "channel/UCzOIPEa7XOs05Jvzoe1VtJA", 'https://yt3.ggpht.com/-37B_TT_6byg/AAAAAAAAAAI/AAAAAAAAAAA/vp-6KoQ-nOo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("2017 Live Poker", "channel/UC9zeONlldzJ9a98fAxb0z1A", 'https://yt3.ggpht.com/-xv7chgM-TY8/AAAAAAAAAAI/AAAAAAAAAAA/0LZlpkLmfV0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Live Poker", "user/LiveTournaments", 'https://yt3.ggpht.com/-NzQOyEWsfyM/AAAAAAAAAAI/AAAAAAAAAAA/HSj0kGqm5os/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Full Tilt", "user/poker", 'https://yt3.ggpht.com/-xN_LX44viqo/AAAAAAAAAAI/AAAAAAAAAAA/eqIgWOI0E6A/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Poker na Veia", "user/ManiaPoker", 'https://yt3.ggpht.com/-PlTVKzyYarU/AAAAAAAAAAI/AAAAAAAAAAA/Bjo1TkojdEw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("View On Poker", "user/ViewOnPoker", 'https://yt3.ggpht.com/-Z342RP3fHcw/AAAAAAAAAAI/AAAAAAAAAAA/F2OhkaOudB4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Poker Night", "user/PokerNightAmerica", 'https://yt3.ggpht.com/-pQ4boBFySpo/AAAAAAAAAAI/AAAAAAAAAAA/cc4JHomKcx4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
	    ("Allin Poker HD", "channel/UCSP3fXKcNeT23sCM_aQolkA", 'https://yt3.ggpht.com/-_6qpuDD_B7w/AAAAAAAAAAI/AAAAAAAAAAA/N8W0TLyON50/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Poker industry Video", "user/FreeGirlsCam", 'https://yt3.ggpht.com/-G6KQOKYTQ9U/AAAAAAAAAAI/AAAAAAAAAAA/OBaeaWuxoEY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Runner Runner", "channel/UC6jcWjuYmZ6H3vZCk67WHnw", 'https://yt3.ggpht.com/-exOZS8fyTUo/AAAAAAAAAAI/AAAAAAAAAAA/1wiLZmNz058/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Card Player", "user/CardPlayerDotCom", 'https://yt3.ggpht.com/-rUaZ-vi1nBI/AAAAAAAAAAI/AAAAAAAAAAA/CFINiDKTQN4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Texas Holdem", "channel/UCO7n79UL2oX6OtKL4ARRHpw", 'https://yt3.ggpht.com/-HdjbkjJ5iQM/AAAAAAAAAAI/AAAAAAAAAAA/Nm7z15UOBmY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),	
		("GUKPT", "user/GUKPT", 'https://yt3.ggpht.com/-W-SHigmc38g/AAAAAAAAAAI/AAAAAAAAAAA/dfhvyD1mSg4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Poker Mind", "channel/UCZFU04CibazF2h_FPnG_HOA", 'https://yt3.ggpht.com/-nBKBe-SqyTU/AAAAAAAAAAI/AAAAAAAAAAA/3wwnMPudRdE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("World Poker", "channel/UC3MLvEm61bfQQgJEI29ePcA", 'https://yt3.ggpht.com/-vXKnELxU6rg/AAAAAAAAAAI/AAAAAAAAAAA/Cr2xcjkKBdQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Dutch Boyd", "user/havoj", 'https://yt3.ggpht.com/-HTStRjnHN_Q/AAAAAAAAAAI/AAAAAAAAAAA/THmaP1eAM44/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Poker Tricks", "channel/UCOFVK6FWmVHqRB5LP7lWy0Q", 'https://yt3.ggpht.com/-Y-KU-M5CZXA/AAAAAAAAAAI/AAAAAAAAAAA/Ttp1SOcOjc8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Daily Poker HD", "channel/UCSJFhMZ-LGxO4jgzwBmu7Sg", 'https://yt3.ggpht.com/-K1RU8ir7vaY/AAAAAAAAAAI/AAAAAAAAAAA/XE2gYQWFos0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Play Poker", "channel/UCAhFt0iE91RuwEVDDeEKU8w", 'https://yt3.ggpht.com/-HjTaA0a6zPo/AAAAAAAAAAI/AAAAAAAAAAA/n5kdxfr0g9g/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("APAT", "user/apatpoker", 'https://yt3.ggpht.com/-thIQGe_YMIo/AAAAAAAAAAI/AAAAAAAAAAA/nGBZs5kcxfQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Smart Poker Study", "channel/UCNJqCsJjk8J_GMA6jMwP-0Q", 'https://yt3.ggpht.com/--qsEP36w5zo/AAAAAAAAAAI/AAAAAAAAAAA/wtGgk-RtqAk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Poker Xpress", "user/greekxpress", 'https://yt3.ggpht.com/-HJ0Rns_ReqU/AAAAAAAAAAI/AAAAAAAAAAA/Qxg-7Oh4PTw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Poker Plus TV", "channel/UC28MHu-_RvZsYbBCIrUhVmA", 'https://yt3.ggpht.com/-BsthcJlxt7k/AAAAAAAAAAI/AAAAAAAAAAA/_ArYfV1dfTc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Poker Channel", "user/sergeypoker", 'https://yt3.ggpht.com/-rrnoVZ-XNgg/AAAAAAAAAAI/AAAAAAAAAAA/7rUzCFDdttQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Poker VIP", "user/iPokerVIP", 'https://yt3.ggpht.com/-EENIpiZ0iNA/AAAAAAAAAAI/AAAAAAAAAAA/bo7iP6U8-Ws/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Kevin Martin", "user/KevinMartin31415", 'https://yt3.ggpht.com/-QnIUjlEXBuQ/AAAAAAAAAAI/AAAAAAAAAAA/-bxQHy5QcjY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Poker Strategy", "user/Mr50free", 'https://yt3.ggpht.com/-hyZk0O16lAw/AAAAAAAAAAI/AAAAAAAAAAA/3fl8E4xabnQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("PokerStars PSO", "user/PSOOfficial", 'https://yt3.ggpht.com/-fjesqMmGpFE/AAAAAAAAAAI/AAAAAAAAAAA/nFWMNjEvbMU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Alec Torelli", "channel/UCGCThbGQdVNe1llymw3-pxQ", 'https://yt3.ggpht.com/-aiWr2KOXXaY/AAAAAAAAAAI/AAAAAAAAAAA/U4StT_bkquc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Gripsed Poker", "user/gripsed", 'https://yt3.ggpht.com/-khe6sLdZEzs/AAAAAAAAAAI/AAAAAAAAAAA/CK_N8TrLGTA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Transform My Poker", "channel/UC0LMeYPslcEuLffOrn7SmEg", 'https://yt3.ggpht.com/-ewbbMCa-Fmc/AAAAAAAAAAI/AAAAAAAAAAA/ZkSHBv6tDHI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("School of Cards", "user/SchoolofCards", 'https://yt3.ggpht.com/-iW3JKlQ0-Gc/AAAAAAAAAAI/AAAAAAAAAAA/AhAzJ-6PKmM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Doug Polk Poker", "channel/UCyI7FNTudkyALBh9N7hwI9Q", 'https://yt3.ggpht.com/-hgximTQhNCY/AAAAAAAAAAI/AAAAAAAAAAA/bn444bayVf0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Team NeverLucky", "channel/UCfnDEiPDcVikMD-R1zS_lvA", 'https://yt3.ggpht.com/-jHzuHq3h780/AAAAAAAAAAI/AAAAAAAAAAA/GeOnR6ECsBE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Felix Schneiders", "user/teampsxflixx", 'https://yt3.ggpht.com/-XF8c2BC0f1M/AAAAAAAAAAI/AAAAAAAAAAA/YybIkZ0SA5A/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("PokerListings", "user/PokerListings", 'https://yt3.ggpht.com/-swJWPGp1TuE/AAAAAAAAAAI/AAAAAAAAAAA/7RkiGOnl-rI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("The Poker Bank", "user/thepokerbank", 'https://yt3.ggpht.com/-Ew9IQAETBDs/AAAAAAAAAAI/AAAAAAAAAAA/tUfVHeQHeVw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Daniel Negreanu", "user/DNegreanu", 'https://yt3.ggpht.com/-7etkN7vZsBc/AAAAAAAAAAI/AAAAAAAAAAA/-HmcTlINVJk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("wsop2010fvp", "user/wsop2010fvp", 'https://yt3.ggpht.com/-Kyyiux7fXFo/AAAAAAAAAAI/AAAAAAAAAAA/YdLc90hVGO8/s88-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("pokernewsdotcom", "user/pokernewsdotcom", 'https://yt3.ggpht.com/-bGLLPx_ppAo/AAAAAAAAAAI/AAAAAAAAAAA/-jAztPFXEGs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),		
]


# Entry point
def run():
    plugintools.log("POKER.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
    #   exec action+"(params)" ###### SEE: http://forum.kodi.tv/showthread.php?tid=254207&pid=2465855#pid2465855
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("POKER.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )


run()