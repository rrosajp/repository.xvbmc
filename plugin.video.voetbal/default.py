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
from addon.common.addon import Addon

addonID = 'plugin.video.voetbal'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("[COLOR darkorange]Voetbal >>[/COLOR] ONS ORANJE", "user/onsoranje", "https://yt3.ggpht.com/-NccNRZ6I1Xc/AAAAAAAAAAI/AAAAAAAAAAA/3UubOd2GgSo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] BETWETERS", "user/betweters", "https://yt3.ggpht.com/-ayoqN002Tz8/AAAAAAAAAAI/AAAAAAAAAAA/Q_EfSfT3ktQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] BUREAU SPORT", "channel/UCcjdJz1HBSb260XkDcbpvkQ", "https://yt3.ggpht.com/-iihDfFSLrZ4/AAAAAAAAAAI/AAAAAAAAAAA/j96gOzDLL-E/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] FC AFKICKEN", "channel/UCSLrWHz1jExjoTPUntmTwJg", "https://yt3.ggpht.com/-jc2dbPRB0ZM/AAAAAAAAAAI/AAAAAAAAAAA/prQN68dHDFA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Voetbal >>[/COLOR] ONLY FOOTBALL", "channel/UCKVpF-YHU2cthmBxb4omFbw", "https://yt3.ggpht.com/-KLdyDLwOMVA/AAAAAAAAAAI/AAAAAAAAAAA/lnBoSVvg9m4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Voetbal >>[/COLOR] FREESTYLE VOETBAL", "user/leerfreestylevoetbal", "https://yt3.ggpht.com/-Mcj_jDoRplA/AAAAAAAAAAI/AAAAAAAAAAA/4VZegUMvxtc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR darkorange]Voetbal >>[/COLOR] OER VOETBAL VLOGS", "channel/UCcy_dYrIJpF_K_ZLv_ZoJ0A", "https://yt3.ggpht.com/-qvtQwMmFiHA/AAAAAAAAAAI/AAAAAAAAAAA/ddsqo07zeBo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR darkorange]Voetbal >>[/COLOR] VIRAL SPORT VINES", "channel/UC_j7sV7_CIbTgD9qX4ZRgbw", "https://yt3.ggpht.com/-ZB5nnHBqxB0/AAAAAAAAAAI/AAAAAAAAAAA/ALto4i6YnuU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR darkorange]Voetbal >>[/COLOR] HEIlRJ 2", "user/HeilRJ04", "https://yt3.ggpht.com/-WYZoliQYCaw/AAAAAAAAAAI/AAAAAAAAAAA/mwNWq79gLl8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR darkorange]Voetbal >>[/COLOR] HAAGLANDEN VOETBAL TV", "user/HaaglandenVoetbalTV", "https://yt3.ggpht.com/-8dj-lIjIytk/AAAAAAAAAAI/AAAAAAAAAAA/raaHlUDADdw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] VOETBAL ROTTERDAM TV", "user/VoetbalRotterdamTV", "https://yt3.ggpht.com/-egCSsELfCc4/AAAAAAAAAAI/AAAAAAAAAAA/eFMemSz05AQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] VOETBAL INSIDE", "user/VITVRTL", "https://yt3.ggpht.com/-DyY4GzC0FBc/AAAAAAAAAAI/AAAAAAAAAAA/84mnYa6x8dU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] ALLES OP SWART", "channel/UCsYx8ULsWkue2a3VflaNAeQ", "https://yt3.ggpht.com/-7d-KfiuXs9k/AAAAAAAAAAI/AAAAAAAAAAA/TS1zlFzjb5k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] FOX SPORTS", "user/EredivisieLive/videos", "https://yt3.ggpht.com/-UB8-sc_B1Kg/AAAAAAAAAAI/AAAAAAAAAAA/vxlLGekBYxU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] FIFALOSOPHY", "user/Fifalosophy", "https://yt3.ggpht.com/-Qu9GBaRjERs/AAAAAAAAAAI/AAAAAAAAAAA/ApZmuVQfOvY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] TAFEL VOETBAL", "channel/UCRtugJkSFMQgp_22sqkFC4g", "https://yt3.ggpht.com/-mfI_wmAD5Ow/AAAAAAAAAAI/AAAAAAAAAAA/_9o5LxB9Z9w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] AJAX VENTOS", "user/AjaxVentos", "https://yt3.ggpht.com/-2UgXUJoFUNw/AAAAAAAAAAI/AAAAAAAAAAA/6TokAPR0ygo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] PSV SUPPORT", "channel/UCCsXdzoG9Wptlj0LZZ2ujbA", "https://yt3.ggpht.com/-d-0nN7iNEo0/AAAAAAAAAAI/AAAAAAAAAAA/ZdbFfDLdtXo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal >>[/COLOR] ADIDAS FOOTBALL", "user/adidasfootballtv", "https://yt3.ggpht.com/-NYASkFCW5VQ/AAAAAAAAAAI/AAAAAAAAAAA/BKBOQjCUvi0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		
		("[COLOR red]Algemeen >>[/COLOR] ATV-NETWORKS SURINAME", "user/atvsuriname", "https://yt3.ggpht.com/-qfXi_tRiH30/AAAAAAAAAAI/AAAAAAAAAAA/-PZmPHf-cH8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Algemeen >>[/COLOR] RTV RIJNMOND", "user/rtvrijnmond/videos", "https://yt3.ggpht.com/-MlBAC9zJtfg/AAAAAAAAAAI/AAAAAAAAAAA/Tl9iJl1OWZY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Algemeen >>[/COLOR] VANAF DE ZIJLIJN", "channel/UCi4g0oO4xj7TcbF2Nws8tBQ", "https://yt3.ggpht.com/-g7IjMItM6jc/AAAAAAAAAAI/AAAAAAAAAAA/7ogSGL-0JWU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Algemeen >>[/COLOR] HW MEDIA", "channel/UCWswkrNh7CsGf6Cq5dHIl0w", "https://yt3.ggpht.com/-4KGvNA3ML2o/AAAAAAAAAAI/AAAAAAAAAAA/82o1hZ47aKU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
		
		("[COLOR darkorange]Clubs >>[/COLOR] ADO Den Haag TV", "user/ADODenHaagTV", "https://yt3.ggpht.com/-6RvgIEV9WhI/AAAAAAAAAAI/AAAAAAAAAAA/eYEVcEyJTHU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] Ajax TV", "user/ajax", "https://yt3.ggpht.com/-jqrIEltgE1U/AAAAAAAAAAI/AAAAAAAAAAA/AhkDhss9X4w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] AZ TV", "user/AZTV", "https://yt3.ggpht.com/-yyhnHNLCPp8/AAAAAAAAAAI/AAAAAAAAAAA/xlm_pFvukqI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] Excelsior TV", "user/sbvexcelsior", "https://yt3.ggpht.com/-32h9c3Rz-ao/AAAAAAAAAAI/AAAAAAAAAAA/1ANEn8xjySU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] Feyenoord TV", "user/FeyenoordRotterdamTV", "https://yt3.ggpht.com/-sfO41QeVlw4/AAAAAAAAAAI/AAAAAAAAAAA/hDDl3jwRL1k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] Go Ahead Eagles TV", "channel/UCD3rTNWI-2AdprNnsXlC0nQ", "https://yt3.ggpht.com/-XpEC8EjW2iQ/AAAAAAAAAAI/AAAAAAAAAAA/QH0_WVdqESo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] FC Groningen TV", "user/FCGroningenTV", "https://yt3.ggpht.com/-vatxowB6e2o/AAAAAAAAAAI/AAAAAAAAAAA/PySf0KkU7ZM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] SC Heerenveen TV", "user/scHeerenveen", "https://yt3.ggpht.com/-BizAfzcJo3o/AAAAAAAAAAI/AAAAAAAAAAA/oKDW9Lu1PI8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] Heracles TV", "user/HeraclesAlmeloTV", "https://yt3.ggpht.com/-4syNFL3i7WA/AAAAAAAAAAI/AAAAAAAAAAA/9uxdYzc6z-8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] NEC TV", "user/NECTVkanaal", "https://yt3.ggpht.com/-KpZ8RDTeTfQ/AAAAAAAAAAI/AAAAAAAAAAA/pVeT-DTm5kk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] PSV TV", "user/psveindhoven", "https://yt3.ggpht.com/-gsIfLVnOfgY/AAAAAAAAAAI/AAAAAAAAAAA/XzNYpZVmEFY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] Roda JC TV", "user/RodaJCKerkradeTV", "https://yt3.ggpht.com/-LhF3zdjpng4/AAAAAAAAAAI/AAAAAAAAAAA/peTKp7TXFYQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR darkorange]Clubs >>[/COLOR] Sparta Rotterdam TV", "channel/UCwABRT8M4wG7JB7jhSv9J7Q", "https://yt3.ggpht.com/-hwTMjGyGx-E/AAAAAAAAAAI/AAAAAAAAAAA/wRa4oatgoWQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR darkorange]Clubs >>[/COLOR] FC Twente TV", "user/FCTwenteTV", "https://yt3.ggpht.com/-TKHbRZL1kb4/AAAAAAAAAAI/AAAAAAAAAAA/cyqeyk8i8RM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR darkorange]Clubs >>[/COLOR] FC Utrecht TV", "user/fcutrecht", "https://yt3.ggpht.com/-3RaZ5yClYxg/AAAAAAAAAAI/AAAAAAAAAAA/R4o-6Jk6x8M/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] Vitesse TV",  "user/VitesseTV", "https://yt3.ggpht.com/-ewXQBcFk6ZE/AAAAAAAAAAI/AAAAAAAAAAA/1_nJq7G_iqo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
		("[COLOR darkorange]Clubs >>[/COLOR] Willem II TV", "user/WillemII", "https://yt3.ggpht.com/-738-M5uYXlg/AAAAAAAAAAI/AAAAAAAAAAA/0k0wAIqPq30/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs >>[/COLOR] PEC Zwolle TV", "user/peczwolletv", "https://yt3.ggpht.com/-ShDWQyu69vk/AAAAAAAAAAI/AAAAAAAAAAA/klALDUBVkFs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		
		("[COLOR red]Buitenland >>[/COLOR] FC BARCELONA", "user/fcbarcelona", "https://yt3.ggpht.com/-cbuwcRBtVFE/AAAAAAAAAAI/AAAAAAAAAAA/Cd4EmB0AO6E/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR red]Buitenland >>[/COLOR] REAL MADRID", "user/realmadridcf", "https://yt3.ggpht.com/-zvPqz5WM4EE/AAAAAAAAAAI/AAAAAAAAAAA/fh1Q0Ycpv2M/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR red]Buitenland >>[/COLOR] FC BAYERN MUNICH", "user/fcbayern", "https://yt3.ggpht.com/-C7AqhweKVz8/AAAAAAAAAAI/AAAAAAAAAAA/_P-2X1lOkcM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR red]Buitenland >>[/COLOR] MAN CITY", "user/mcfcofficial", "https://yt3.ggpht.com/-WQH-4G14xyQ/AAAAAAAAAAI/AAAAAAAAAAA/8ND75PLcsH4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR red]Buitenland >>[/COLOR] LIVERPOOL", "user/LiverpoolFC", "https://yt3.ggpht.com/-TrtEHOgcMFE/AAAAAAAAAAI/AAAAAAAAAAA/K547x_dy1bY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR red]Buitenland >>[/COLOR] MAN UNITED FC", "channel/UCYF2FotHeGO6cNcldrTHN1g", "https://yt3.ggpht.com/-5Zf2AtAYP-g/AAAAAAAAAAI/AAAAAAAAAAA/svSKYRMInGc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR red]Buitenland >>[/COLOR] FOOTOZ", "channel/UC7TEzgIRQVei9kAVZuC9fNA", "https://yt3.ggpht.com/-GFtoTKZK5UM/AAAAAAAAAAI/AAAAAAAAAAA/hQEB8Av9ggU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR red]Buitenland >>[/COLOR] MATCH DAY REPLAYS", "user/BaitovComps", "https://yt3.ggpht.com/-5bDkzJ_rHE0/AAAAAAAAAAI/AAAAAAAAAAA/UL0RCFyqShc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] IGABR", "user/MrLeagueofNation", "https://yt3.ggpht.com/-QwY3lCqm-mY/AAAAAAAAAAI/AAAAAAAAAAA/tWn3AldeMxc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] MAJOR LEAGUE SOCCER", "user/mls", "https://yt3.ggpht.com/-E-P3owrEULM/AAAAAAAAAAI/AAAAAAAAAAA/HKmwsg82u30/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] WE SPEAK FOOTBALL", "channel/UCXhnj8YEuibr6Tn7hJqHg0Q", "https://yt3.ggpht.com/-V9a9p8V13a4/AAAAAAAAAAI/AAAAAAAAAAA/nRZdQBSHcKw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] ROM7000", "user/rom7oooHD1", "https://yt3.ggpht.com/-qP2sEBAiNdw/AAAAAAAAAAI/AAAAAAAAAAA/QFK79oi_K8w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
]



# Entry point
def run():
    plugintools.log("voetbal.run")
    
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
    plugintools.log("voetbal.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()