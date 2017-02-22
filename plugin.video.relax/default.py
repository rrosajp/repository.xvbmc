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

addonID = 'plugin.video.Relax'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Relaxing Music", "user/YellowBrickCinema", 'https://yt3.ggpht.com/-MAYy5YouIXg/AAAAAAAAAAI/AAAAAAAAAAA/qpCDyPMDnuM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Nature Relaxation", "user/dhuting", 'https://yt3.ggpht.com/-DrqWEcklUKU/AAAAAAAAAAI/AAAAAAAAAAA/c3i0B_gB9hY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Meditation", "user/YourRelaxMusic1", 'https://yt3.ggpht.com/-c1LV6kl8nls/AAAAAAAAAAI/AAAAAAAAAAA/GIR8nHEOO-k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),	
        ("Soothing Relaxation", "channel/UCjzHeG1KWoonmf9d5KBvSiw", 'https://yt3.ggpht.com/-vq0QH82gHCE/AAAAAAAAAAI/AAAAAAAAAAA/vPmQ10nrrUc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Nu Meditation", "user/numeditationmusic", 'https://yt3.ggpht.com/-vWMRDWyczbg/AAAAAAAAAAI/AAAAAAAAAAA/IbcK0dLp7Ag/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Body Mind Zone", "user/BodyMindZone", 'https://yt3.ggpht.com/-DjmKRBI7MiA/AAAAAAAAAAI/AAAAAAAAAAA/bAZPeF66u0g/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("321 Relaxing", "user/Relax321Relaxing", 'https://yt3.ggpht.com/-3WE-xNfaDHs/AAAAAAAAAAI/AAAAAAAAAAA/vxI81rrm5kg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Relax", "user/roiavision", 'https://yt3.ggpht.com/-oUVTHQocraY/AAAAAAAAAAI/AAAAAAAAAAA/HiyhlnRAvTY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Dr SaxLove", "channel/UCNJFXYXkXt_P8bJUxb21MpA", 'https://yt3.ggpht.com/-EYGprZEMDoo/AAAAAAAAAAI/AAAAAAAAAAA/xjYDFiH8sqM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Love Songs", "channel/UCjcboTJVbOL53katjX79r8A", 'https://yt3.ggpht.com/-j-xkJHRlVzM/AAAAAAAAAAI/AAAAAAAAAAA/oi4HR1KzwLk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Cafe Music", "user/cafemusicbgmchannel", 'https://yt3.ggpht.com/-J7GRtoYtWXk/AAAAAAAAAAI/AAAAAAAAAAA/487XVrL-Z8s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
	    ("Relaxation Cafe", "user/lewisluongrelaxation", 'https://yt3.ggpht.com/-8cW6HMCgfr4/AAAAAAAAAAI/AAAAAAAAAAA/tHSVttlLHZg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("HDnatureTV", "user/HDnatureTV", 'https://yt3.ggpht.com/-Z3WEDGVGgyg/AAAAAAAAAAI/AAAAAAAAAAA/6MdxbTotZJM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Relax daily", "user/relaxdaily", 'https://yt3.ggpht.com/-VDIImvYvEC4/AAAAAAAAAAI/AAAAAAAAAAA/3sM6Dn7t4WU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("LoungeV Films", "user/LoungeVstudio", 'https://yt3.ggpht.com/-UCc_OGvq0eU/AAAAAAAAAAI/AAAAAAAAAAA/Na2cSmJOLfk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Escape One", "user/EscapeOneChannel", 'https://yt3.ggpht.com/-KYaSyQE56BE/AAAAAAAAAAI/AAAAAAAAAAA/vfPaGNqv8Dk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),	
		("Relax Tube", "channel/UCBPCI8cUaa3tcUACQO-P1yQ",  'https://yt3.ggpht.com/-a1IMwPZk1cE/AAAAAAAAAAI/AAAAAAAAAAA/AMJUTo9zbU8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Pulse 8", "user/Pulse8Music", 'https://yt3.ggpht.com/-FTExCdRIPTI/AAAAAAAAAAI/AAAAAAAAAAA/8CBc_z66FBs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Dream Tv", "channel/UC--eCztYYvsbi7E8cDi3dgg", 'https://yt3.ggpht.com/-spFkL-__i7A/AAAAAAAAAAI/AAAAAAAAAAA/c7zDayeW7mE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Relax Channel", "user/michal78964", 'https://yt3.ggpht.com/-WlMvDwdzdVM/AAAAAAAAAAI/AAAAAAAAAAA/n9f7F_mtOsc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Relax Music", "user/Geelbes", 'https://yt3.ggpht.com/-gkM8RPr4rqw/AAAAAAAAAAI/AAAAAAAAAAA/kleRSBhfBUg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Best Relaxing", "channel/UCgJHyhd5a2fE0oK_rOHH-sA", 'https://yt3.ggpht.com/-Z79HXjtgosY/AAAAAAAAAAI/AAAAAAAAAAA/AISMdK8BLuU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("BGM channel", "user/bgmchannelbgm", 'https://yt3.ggpht.com/-_jqaNAUWwik/AAAAAAAAAAI/AAAAAAAAAAA/TNB-3aMdYbM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Relax Meditation", "channel/UCvwiKt4P7kmVGM_HvDlQ7pw", 'https://yt3.ggpht.com/-URy7h6XjSIY/AAAAAAAAAAI/AAAAAAAAAAA/fvUYChlhRfs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Musical Aura", "user/TheMusicalAura", 'https://yt3.ggpht.com/-mx6TLhX8cCs/AAAAAAAAAAI/AAAAAAAAAAA/4RBMhAQ8jD4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("New Age", "channel/UCFLz8dBZcOj-zxI-OqCxm-g", 'https://yt3.ggpht.com/-7m4pBtbQeVI/AAAAAAAAAAI/AAAAAAAAAAA/Lu2GLhfV7fE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("My Relaxing Music", "channel/UCezR_snAMVrNl7WtX0h_93Q", 'https://yt3.ggpht.com/-qvCnFx2Ab-I/AAAAAAAAAAI/AAAAAAAAAAA/-oHKdxB1e1A/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("music synthesis", "channel/UCzRfwwCsARESSz4_a2iDGbg", 'https://yt3.ggpht.com/-SuvMPXRahe8/AAAAAAAAAAI/AAAAAAAAAAA/xBaZQlsna4k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Japan Relaxing", "user/japanrelaxingmusic", 'https://yt3.ggpht.com/-wmwzh9icN8E/AAAAAAAAAAI/AAAAAAAAAAA/2aSkCU99_g4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Collection One", "UC6-HwJBZFez8DhBx8Uwkeiw", 'https://yt3.ggpht.com/-yqECuST62PA/AAAAAAAAAAI/AAAAAAAAAAA/pI90Vf4z_Ok/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("OCB Relax Music", "user/simplyJF", 'https://yt3.ggpht.com/-9tc1pIq51Ck/AAAAAAAAAAI/AAAAAAAAAAA/3fS6JlPqtxw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Meditation", "channel/UCDD7W0KTFFXB9xbgjkt4yog", 'https://yt3.ggpht.com/-vQ1IcGeiwYg/AAAAAAAAAAI/AAAAAAAAAAA/yfCzMgprlYI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("johnnielawson", "user/johnnielawson", 'https://yt3.ggpht.com/-6AXQfZZ9JUo/AAAAAAAAAAI/AAAAAAAAAAA/RAnwvGTKiGU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Nature Sounds", "user/wavesdvdcom", 'https://yt3.ggpht.com/-bJhPLMPwAiw/AAAAAAAAAAI/AAAAAAAAAAA/pB8R2V73ClI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		("Peaceful Scenes", "channel/UC8az6OzymjQfTWFzsTuOfYw", 'https://yt3.ggpht.com/-ZXhWRJFO1-M/AAAAAAAAAAI/AAAAAAAAAAA/IeYKiUnI6pQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
]



# Entry point
def run():
    plugintools.log("Relax.run")
    
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
    plugintools.log("Relax.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()