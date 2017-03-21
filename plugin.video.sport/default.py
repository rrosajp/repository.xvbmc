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

addonID = 'plugin.video.sport'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("[COLOR darkorange]Voetbal NL>>[/COLOR] ONS ORANJE", "user/onsoranje", "https://yt3.ggpht.com/-NccNRZ6I1Xc/AAAAAAAAAAI/AAAAAAAAAAA/3UubOd2GgSo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] BETWETERS", "user/betweters", "https://yt3.ggpht.com/-ayoqN002Tz8/AAAAAAAAAAI/AAAAAAAAAAA/Q_EfSfT3ktQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] BUREAU SPORT", "channel/UCcjdJz1HBSb260XkDcbpvkQ", "https://yt3.ggpht.com/-iihDfFSLrZ4/AAAAAAAAAAI/AAAAAAAAAAA/j96gOzDLL-E/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] FC AFKICKEN", "channel/UCSLrWHz1jExjoTPUntmTwJg", "https://yt3.ggpht.com/-jc2dbPRB0ZM/AAAAAAAAAAI/AAAAAAAAAAA/prQN68dHDFA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Voetbal NL>>[/COLOR] ONLY FOOTBALL", "channel/UCKVpF-YHU2cthmBxb4omFbw", "https://yt3.ggpht.com/-KLdyDLwOMVA/AAAAAAAAAAI/AAAAAAAAAAA/lnBoSVvg9m4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Voetbal NL>>[/COLOR] FREESTYLE VOETBAL", "user/leerfreestylevoetbal", "https://yt3.ggpht.com/-Mcj_jDoRplA/AAAAAAAAAAI/AAAAAAAAAAA/4VZegUMvxtc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR darkorange]Voetbal NL>>[/COLOR] OER VOETBAL VLOGS", "channel/UCcy_dYrIJpF_K_ZLv_ZoJ0A", "https://yt3.ggpht.com/-qvtQwMmFiHA/AAAAAAAAAAI/AAAAAAAAAAA/ddsqo07zeBo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR darkorange]Voetbal NL>>[/COLOR] HEIlRJ 2", "user/HeilRJ04", "https://yt3.ggpht.com/-WYZoliQYCaw/AAAAAAAAAAI/AAAAAAAAAAA/mwNWq79gLl8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR darkorange]Voetbal NL>>[/COLOR] HAAGLANDEN VOETBAL TV", "user/HaaglandenVoetbalTV", "https://yt3.ggpht.com/-8dj-lIjIytk/AAAAAAAAAAI/AAAAAAAAAAA/raaHlUDADdw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] VOETBAL ROTTERDAM TV", "user/VoetbalRotterdamTV", "https://yt3.ggpht.com/-egCSsELfCc4/AAAAAAAAAAI/AAAAAAAAAAA/eFMemSz05AQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] VOETBAL INSIDE", "user/VITVRTL", "https://yt3.ggpht.com/-DyY4GzC0FBc/AAAAAAAAAAI/AAAAAAAAAAA/84mnYa6x8dU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] ALLES OP SWART", "channel/UCsYx8ULsWkue2a3VflaNAeQ", "https://yt3.ggpht.com/-7d-KfiuXs9k/AAAAAAAAAAI/AAAAAAAAAAA/TS1zlFzjb5k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] FOX SPORTS", "user/EredivisieLive", "https://yt3.ggpht.com/-UB8-sc_B1Kg/AAAAAAAAAAI/AAAAAAAAAAA/vxlLGekBYxU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] FIFALOSOPHY", "user/Fifalosophy", "https://yt3.ggpht.com/-Qu9GBaRjERs/AAAAAAAAAAI/AAAAAAAAAAA/ApZmuVQfOvY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] TAFEL VOETBAL", "channel/UCRtugJkSFMQgp_22sqkFC4g", "https://yt3.ggpht.com/-mfI_wmAD5Ow/AAAAAAAAAAI/AAAAAAAAAAA/_9o5LxB9Z9w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] AJAX VENTOS", "user/AjaxVentos", "https://yt3.ggpht.com/-2UgXUJoFUNw/AAAAAAAAAAI/AAAAAAAAAAA/6TokAPR0ygo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] PSV SUPPORT", "channel/UCCsXdzoG9Wptlj0LZZ2ujbA", "https://yt3.ggpht.com/-d-0nN7iNEo0/AAAAAAAAAAI/AAAAAAAAAAA/ZdbFfDLdtXo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Voetbal NL>>[/COLOR] ADIDAS FOOTBALL", "user/adidasfootballtv", "https://yt3.ggpht.com/-NYASkFCW5VQ/AAAAAAAAAAI/AAAAAAAAAAA/BKBOQjCUvi0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		
		("[COLOR red]Nieuws NL>>[/COLOR] ATV-NETWORKS SURINAME", "user/atvsuriname", "https://yt3.ggpht.com/-qfXi_tRiH30/AAAAAAAAAAI/AAAAAAAAAAA/-PZmPHf-cH8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Nieuws NL>>[/COLOR] RTV RIJNMOND", "user/rtvrijnmond", "https://yt3.ggpht.com/-MlBAC9zJtfg/AAAAAAAAAAI/AAAAAAAAAAA/Tl9iJl1OWZY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Nieuws NL>>[/COLOR] HW MEDIA", "channel/UCWswkrNh7CsGf6Cq5dHIl0w", "https://yt3.ggpht.com/-4KGvNA3ML2o/AAAAAAAAAAI/AAAAAAAAAAA/82o1hZ47aKU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
		
		("[COLOR darkorange]Clubs NL>>[/COLOR] ADO Den Haag TV", "user/ADODenHaagTV", "https://yt3.ggpht.com/-6RvgIEV9WhI/AAAAAAAAAAI/AAAAAAAAAAA/eYEVcEyJTHU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] Ajax TV", "user/ajax", "https://yt3.ggpht.com/-jqrIEltgE1U/AAAAAAAAAAI/AAAAAAAAAAA/AhkDhss9X4w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] AZ TV", "user/AZTV", "https://yt3.ggpht.com/-yyhnHNLCPp8/AAAAAAAAAAI/AAAAAAAAAAA/xlm_pFvukqI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] Excelsior TV", "user/sbvexcelsior", "https://yt3.ggpht.com/-32h9c3Rz-ao/AAAAAAAAAAI/AAAAAAAAAAA/1ANEn8xjySU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] Feyenoord TV", "user/FeyenoordRotterdamTV", "https://yt3.ggpht.com/-sfO41QeVlw4/AAAAAAAAAAI/AAAAAAAAAAA/hDDl3jwRL1k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] Go Ahead Eagles TV", "channel/UCD3rTNWI-2AdprNnsXlC0nQ", "https://yt3.ggpht.com/-XpEC8EjW2iQ/AAAAAAAAAAI/AAAAAAAAAAA/QH0_WVdqESo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] FC Groningen TV", "user/FCGroningenTV", "https://yt3.ggpht.com/-vatxowB6e2o/AAAAAAAAAAI/AAAAAAAAAAA/PySf0KkU7ZM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] SC Heerenveen TV", "user/scHeerenveen", "https://yt3.ggpht.com/-BizAfzcJo3o/AAAAAAAAAAI/AAAAAAAAAAA/oKDW9Lu1PI8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] Heracles TV", "user/HeraclesAlmeloTV", "https://yt3.ggpht.com/-4syNFL3i7WA/AAAAAAAAAAI/AAAAAAAAAAA/9uxdYzc6z-8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] NEC TV", "user/NECTVkanaal", "https://yt3.ggpht.com/-KpZ8RDTeTfQ/AAAAAAAAAAI/AAAAAAAAAAA/pVeT-DTm5kk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] PSV TV", "user/psveindhoven", "https://yt3.ggpht.com/-gsIfLVnOfgY/AAAAAAAAAAI/AAAAAAAAAAA/XzNYpZVmEFY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] Roda JC TV", "user/RodaJCKerkradeTV", "https://yt3.ggpht.com/-LhF3zdjpng4/AAAAAAAAAAI/AAAAAAAAAAA/peTKp7TXFYQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR darkorange]Clubs NL>>[/COLOR] Sparta Rotterdam TV", "channel/UCwABRT8M4wG7JB7jhSv9J7Q", "https://yt3.ggpht.com/-hwTMjGyGx-E/AAAAAAAAAAI/AAAAAAAAAAA/wRa4oatgoWQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR darkorange]Clubs NL>>[/COLOR] FC Twente TV", "user/FCTwenteTV", "https://yt3.ggpht.com/-TKHbRZL1kb4/AAAAAAAAAAI/AAAAAAAAAAA/cyqeyk8i8RM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR darkorange]Clubs NL>>[/COLOR] FC Utrecht TV", "user/fcutrecht", "https://yt3.ggpht.com/-3RaZ5yClYxg/AAAAAAAAAAI/AAAAAAAAAAA/R4o-6Jk6x8M/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] Vitesse TV",  "user/VitesseTV", "https://yt3.ggpht.com/-ewXQBcFk6ZE/AAAAAAAAAAI/AAAAAAAAAAA/1_nJq7G_iqo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
		("[COLOR darkorange]Clubs NL>>[/COLOR] Willem II TV", "user/WillemII", "https://yt3.ggpht.com/-738-M5uYXlg/AAAAAAAAAAI/AAAAAAAAAAA/0k0wAIqPq30/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR darkorange]Clubs NL>>[/COLOR] PEC Zwolle TV", "user/peczwolletv", "https://yt3.ggpht.com/-ShDWQyu69vk/AAAAAAAAAAI/AAAAAAAAAAA/klALDUBVkFs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		
		("[COLOR red]Buitenland >>[/COLOR] FC BARCELONA", "user/fcbarcelona", "https://yt3.ggpht.com/-cbuwcRBtVFE/AAAAAAAAAAI/AAAAAAAAAAA/Cd4EmB0AO6E/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR red]Buitenland >>[/COLOR] REAL MADRID", "user/realmadridcf", "https://yt3.ggpht.com/-zvPqz5WM4EE/AAAAAAAAAAI/AAAAAAAAAAA/fh1Q0Ycpv2M/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR red]Buitenland >>[/COLOR] FC BAYERN MUNICH", "user/fcbayern", "https://yt3.ggpht.com/-C7AqhweKVz8/AAAAAAAAAAI/AAAAAAAAAAA/_P-2X1lOkcM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR red]Buitenland >>[/COLOR] MAN CITY", "user/mcfcofficial", "https://yt3.ggpht.com/-WQH-4G14xyQ/AAAAAAAAAAI/AAAAAAAAAAA/8ND75PLcsH4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		("[COLOR red]Buitenland >>[/COLOR] LIVERPOOL", "user/LiverpoolFC", "https://yt3.ggpht.com/-TrtEHOgcMFE/AAAAAAAAAAI/AAAAAAAAAAA/K547x_dy1bY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR red]Buitenland >>[/COLOR] FOOTOZ", "channel/UC7TEzgIRQVei9kAVZuC9fNA", "https://yt3.ggpht.com/-GFtoTKZK5UM/AAAAAAAAAAI/AAAAAAAAAAA/hQEB8Av9ggU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
		("[COLOR red]Buitenland >>[/COLOR] MATCH DAY REPLAYS", "user/BaitovComps", "https://yt3.ggpht.com/-5bDkzJ_rHE0/AAAAAAAAAAI/AAAAAAAAAAA/UL0RCFyqShc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] IGABR", "user/MrLeagueofNation", "https://yt3.ggpht.com/-QwY3lCqm-mY/AAAAAAAAAAI/AAAAAAAAAAA/tWn3AldeMxc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] MAJOR LEAGUE SOCCER", "user/mls", "https://yt3.ggpht.com/-E-P3owrEULM/AAAAAAAAAAI/AAAAAAAAAAA/HKmwsg82u30/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] WE SPEAK FOOTBALL", "channel/UCXhnj8YEuibr6Tn7hJqHg0Q", "https://yt3.ggpht.com/-V9a9p8V13a4/AAAAAAAAAAI/AAAAAAAAAAA/nRZdQBSHcKw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] ROM7000", "user/rom7oooHD1", "https://yt3.ggpht.com/-qP2sEBAiNdw/AAAAAAAAAAI/AAAAAAAAAAA/QFK79oi_K8w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	
        ("[COLOR red]Buitenland >>[/COLOR] AMAZING FOOTBALL SKILLS", "channel/UCRHWk8JW4JQn1UjtUQPQfdA", "https://yt3.ggpht.com/-GDR7Gg9pIQs/AAAAAAAAAAI/AAAAAAAAAAA/75Pha1bi4mo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] FAZELI", "channel/UCUagJzaUxRT1YCTI_Zu0fsA", "https://yt3.ggpht.com/-I01vsdTv8rw/AAAAAAAAAAI/AAAAAAAAAAA/wLJ2ZWruPzE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] FOOTBALL DAILY", "user/TheFootballDaily", "https://yt3.ggpht.com/-enmySwhRKW4/AAAAAAAAAAI/AAAAAAAAAAA/XyJeO8eB-4E/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] EURO FOOTBALL DAILY", "channel/UCykERqO6KgqYF6t3l_hNVfQ", "https://yt3.ggpht.com/-nHfD_d2Z_F8/AAAAAAAAAAI/AAAAAAAAAAA/kuNrTs0kN0U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Buitenland >>[/COLOR] COPA90", "user/Copa90football", "https://yt3.ggpht.com/-AZbWU7KT3Yw/AAAAAAAAAAI/AAAAAAAAAAA/YfQCUPVWgMI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),	

        ("[COLOR darkgreen]Korfbal NL >>[/COLOR] AW DTV", "channel/UCqtFfD-kEo9mWSv1-YpAXlw", "https://yt3.ggpht.com/-lGrpjShDtbM/AAAAAAAAAAI/AAAAAAAAAAA/hQG5CE0q154/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkgreen]Korfbal NL >>[/COLOR] KNKV KORFBAL", "channel/UCRZX2aY0Sthva9zD3MS-aXw", "https://yt3.ggpht.com/-YVbgyEksTNk/AAAAAAAAAAI/AAAAAAAAAAA/QXS-wO9lltQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkgreen]Korfbal NL >>[/COLOR] PKC SWK GROEP", "user/pkckorfbal", "https://yt3.ggpht.com/-0unHqHIenyw/AAAAAAAAAAI/AAAAAAAAAAA/OzgVXVi-0dQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkgreen]Korfbal NL >>[/COLOR] TOP SASSENHEIM", "user/topsassenheim", "https://yt3.ggpht.com/-U57S7HiFGM8/AAAAAAAAAAI/AAAAAAAAAAA/5mRoYw7Uk-o/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkgreen]Korfbal NL >>[/COLOR] KVDSC", "channel/UCX7cl0fTwMzKgYR6luxISBg", "https://yt3.ggpht.com/-k6_-mbqCDYs/AAAAAAAAAAI/AAAAAAAAAAA/xHsLar1OK5c/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),

        ("[COLOR darkorange]Vissen NL >>[/COLOR] KARPERSNOEK", "channel/UCpYsSm7Hls5byfKiw3MLy7g", "https://yt3.ggpht.com/-WbWhnLGJnr4/AAAAAAAAAAI/AAAAAAAAAAA/14M1VL9G4iE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] MISHA", "user/aboebeloe1", "https://yt3.ggpht.com/-8gp2vMOXHog/AAAAAAAAAAI/AAAAAAAAAAA/BrFr5NbcUqw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] SK CARPFISHING", "user/rkop17", "https://yt3.ggpht.com/-fq6vE4GLEEU/AAAAAAAAAAI/AAAAAAAAAAA/1HZbzb16EeQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] SPORTVISSERIJ", "user/SportvisserijNL", "https://yt3.ggpht.com/-xXdCXSymrqM/AAAAAAAAAAI/AAAAAAAAAAA/yMD0XHW8SBY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] VIS TV", "user/VisTVNL", "https://yt3.ggpht.com/-MrZE2vQGDKU/AAAAAAAAAAI/AAAAAAAAAAA/UyjnaUjzT7U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] VMF FISHING", "channel/UC8O4EiVyAO-3OUnU2UzfU0w", "https://yt3.ggpht.com/-ESk2JsUKZks/AAAAAAAAAAI/AAAAAAAAAAA/PjxXO1yXukU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] WILLEM ROMEIJN", "user/MegaWallem", "https://yt3.ggpht.com/-QjlaGuG805s/AAAAAAAAAAI/AAAAAAAAAAA/zqhUxxQ-1Ag/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] FISHERMAN FRIENDS", "channel/UCmjFATDnbuCIUW06k66MttQ", "https://yt3.ggpht.com/-Gxpw3v-977Q/AAAAAAAAAAI/AAAAAAAAAAA/IDM8fFpxf4M/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] VISKID BOAZ", "user/ViskidBoaz", "https://yt3.ggpht.com/-qpimvzs1-LU/AAAAAAAAAAI/AAAAAAAAAAA/C_rSKUkLhuA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] FIEKE VAN DET", "user/AutoverlichtingReeuw", "https://yt3.ggpht.com/-z2pZ8_iszLI/AAAAAAAAAAI/AAAAAAAAAAA/0BwbwVHonhE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] JLPIKE BUSTER", "channel/UCeVCbkbu_24vuQ-3i-mTIiA", "https://yt3.ggpht.com/-busZf21-SIk/AAAAAAAAAAI/AAAAAAAAAAA/YfvMEzbXfJA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] ROBERT GROOTENBOER", "channel/UCpyLy7V9YOpoUuteA4seivw", "https://yt3.ggpht.com/-jS8Q_jyHsLE/AAAAAAAAAAI/AAAAAAAAAAA/nsTCVk2iJcM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] JB PREDATOR", "channel/UCO7H8eLr28CrbboMco4JeiA", "https://yt3.ggpht.com/-MHuh5lE-iVs/AAAAAAAAAAI/AAAAAAAAAAA/u6we4DSfbtA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] TWINCARP", "user/twincarpNL", "https://yt3.ggpht.com/-2KMxrHQPv_w/AAAAAAAAAAI/AAAAAAAAAAA/4fZd2VQ4fUY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] J en R CARPFISHING", "channel/UCQL0CwksH2E4d1toom_0kZg", "https://yt3.ggpht.com/-lifoXOCBtFI/AAAAAAAAAAI/AAAAAAAAAAA/ZNHm-IkFDWc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR darkorange]Vissen NL >>[/COLOR] BOEZEM BAITS", "channel/UCVvLWQ5qfGnqgLvYXSnjomQ", "https://yt3.ggpht.com/-oCLoLp6l1OQ/AAAAAAAAAAI/AAAAAAAAAAA/fbTat15wAuM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		
        ("[COLOR red]Cycling NL >>[/COLOR] CAS2001", "channel/UC3DWYiqOzFKKYR_eosSBn8A", "https://yt3.ggpht.com/-STON5pd5GiY/AAAAAAAAAAI/AAAAAAAAAAA/1cu3QcUZr_o/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR red]Cycling NL >>[/COLOR] CYCLING VIDS", "channel/UCl92NodlwKSVnGxEYYP3qGw", "https://yt3.ggpht.com/-6wqmlmBoP2Y/AAAAAAAAAAI/AAAAAAAAAAA/MnEr6LKhngc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR red]Cycling NL >>[/COLOR] CYCLOCROSSABLE", "user/cyclocrossable", "https://yt3.ggpht.com/-oyk2dVISWXU/AAAAAAAAAAI/AAAAAAAAAAA/bLpEvGUDMLs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR red]Cycling NL >>[/COLOR] HERMAN", "channel/UC5eo2uEFTSIUTZlnZ3bBJPQ", "https://yt3.ggpht.com/-MJOQM7ferrU/AAAAAAAAAAI/AAAAAAAAAAA/tGGmVQqMDMs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR red]Cycling NL >>[/COLOR] WESLEY", "user/TheMrCyclocross", "https://yt3.ggpht.com/-mu-FZkiPDhE/AAAAAAAAAAI/AAAAAAAAAAA/7K30KNiNRoQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),				

        ("[COLOR yellow]Volleybal NL >>[/COLOR] PVT ASSEN", "channel/UCBK-x9OAT5HECslfKWfJOmw", "https://yt3.ggpht.com/-hyDhmjzYrdQ/AAAAAAAAAAI/AAAAAAAAAAA/QjqJrb2iU9c/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR yellow]Volleybal NL >>[/COLOR] VOCASA", "user/vocasawebsite", "https://yt3.ggpht.com/-CMoTuz75ORk/AAAAAAAAAAI/AAAAAAAAAAA/jACSoHvVaSk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR yellow]Volleybal NL >>[/COLOR] WIM", "user/230WIM", "https://yt3.ggpht.com/-MXK_AZOnv6s/AAAAAAAAAAI/AAAAAAAAAAA/FzqDizvgXKk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		
        ("[COLOR white]POOL >>[/COLOR] GENIPOOL14", "user/genipool14", "https://yt3.ggpht.com/-A1oeZde-WeM/AAAAAAAAAAI/AAAAAAAAAAA/fZhdJAMmbhI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR white]POOL >>[/COLOR] CHINESE 8-BALL", "channel/UCrHMZd9ZQvYg-PzvtVTmQBg", "https://yt3.ggpht.com/-NMg71VX0QIo/AAAAAAAAAAI/AAAAAAAAAAA/E9j7ma4CREE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR white]POOL >>[/COLOR] SNOOKER PLANET", "user/mrEpicSponge", "https://yt3.ggpht.com/-fl_tviwrCbw/AAAAAAAAAAI/AAAAAAAAAAA/TJ4IgNV1kR4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR white]POOL >>[/COLOR] ORANGEFORKS", "channel/UCekv77iIYBL74IX1ttzKRyg", "https://yt3.ggpht.com/-gX8MBJ6EdXo/AAAAAAAAAAI/AAAAAAAAAAA/oZ6wgvBGGaY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR white]POOL >>[/COLOR] REELIVE TV", "channel/UCM1mh1AwN6C1b3l01SBoAOA", "https://yt3.ggpht.com/-muY9pRmk570/AAAAAAAAAAI/AAAAAAAAAAA/2zF93-fN0DU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR white]POOL >>[/COLOR] CUE SPORTS", "user/csipool", "https://yt3.ggpht.com/-VtyWk5JUPoE/AAAAAAAAAAI/AAAAAAAAAAA/x4AXd0i1DMs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR white]POOL >>[/COLOR] PROPOOLINFO", "user/propoolinfo", "https://yt3.ggpht.com/-vgiiWJGAL2s/AAAAAAAAAAI/AAAAAAAAAAA/dn0qyZS-btk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),

		("[COLOR darkorange]Darts NL >>[/COLOR] DUTCH DARTS", "channel/UCqWWHUn36FDxuzdxWUio-RQ", "https://yt3.ggpht.com/-zIWksRr1LmE/AAAAAAAAAAI/AAAAAAAAAAA/YdN_pyHBV3s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Darts >>[/COLOR] WORLD DARTS SPORT", "channel/UCw9EVU9D8k8jmPm8XZmKkiQ", "https://yt3.ggpht.com/-wJ_iQAxbCvQ/AAAAAAAAAAI/AAAAAAAAAAA/iVsfaJ4j28E/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Darts >>[/COLOR] DARTS 2017", "channel/UCqTR0cxt3icoSPKVlCIhIfQ", "https://yt3.ggpht.com/-4ItOF4zyKCs/AAAAAAAAAAI/AAAAAAAAAAA/M5AwZzaUJoQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Darts >>[/COLOR] ANATOLIJ", "channel/UCye3Uf18W9Zbs0OUvJon2yg", "https://yt3.ggpht.com/-snoH2dzxDI0/AAAAAAAAAAI/AAAAAAAAAAA/5y9HPtaLWfc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Darts >>[/COLOR] DARTS PLANET", "channel/UCdanEzz4jEcNU4OBZBQQXoA", "https://yt3.ggpht.com/-i7b1Y2yKZYs/AAAAAAAAAAI/AAAAAAAAAAA/SK_Jpc3i1zc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("[COLOR red]Darts >>[/COLOR] TOLLER77", "channel/UCiX05yXRUWO7_TT4XSNIpcg", "https://yt3.ggpht.com/-UiFrQB1tKOo/AAAAAAAAAAI/AAAAAAAAAAA/8u4LsIaHvms/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),				
		
        ("[COLOR orange]Basketbal >>[/COLOR] COLLEGE HOOPS", "channel/UCxuIRL5p9OD2FjNBlV9yXpQ", "https://yt3.ggpht.com/-2zYVChISFCU/AAAAAAAAAAI/AAAAAAAAAAA/F3cGKWaQhfc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR orange]Basketbal >>[/COLOR] NBA FULL MATCHES", "channel/UCS9mcmat7nxitymN5HbG-RQ", "https://yt3.ggpht.com/-hlU2FyXqorY/AAAAAAAAAAI/AAAAAAAAAAA/XcHVvEpm9WU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),		
        ("[COLOR orange]Basketbal >>[/COLOR] NBA FULL RECAP", "channel/UC0rDNVMafPWtpY63vFbxC3A", "https://yt3.ggpht.com/-YLtosy9kV3o/AAAAAAAAAAI/AAAAAAAAAAA/ZjYoS_dRFlc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),						
]



# Entry point
def run():
    plugintools.log("sport.run")
    
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
    plugintools.log("sport.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()