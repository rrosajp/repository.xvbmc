# -*- coding: utf-8 -*-
#------------------------------------------------------------
# channels eredivisieclubs
#---------------------------------------------------------------------------
import os
import sys

import urlparse,re
import urllib
import datetime

from core import logger
from core import config
from core import scrapertools
from core.item import Item

import youtube_channel

DEBUG = True
CHANNELNAME = "eredivisieclubs"

def isGeneric():
    return True

# Entry point
def mainlist(item):
    logger.info("eredivisieclubs.main_list")
    itemlist=[]

    itemlist.append( Item(channel=CHANNELNAME, title="ADO Den Haag" , action="youtube_playlists" , url="ADODenHaagTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/701/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/ADO%20Den%20Haag.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="AZ" , action="youtube_playlists" , url="AZTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/313/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/AZ.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="AFC Ajax" , action="youtube_playlists" , url="ajax",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/215/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Ajax.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="S.V.B. Excelsior" , action="youtube_playlists" , url="sbvexcelsior",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/539/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Excelsior.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="FC Groningen" , action="youtube_playlists" , url="FCGroningenTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/425/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/FC%20Groningen.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="F.C. Twente" , action="youtube_playlists" , url="FCTwenteTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/324/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/FC%20Twente.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="FC Utrecht" , action="youtube_playlists" , url="fcutrecht",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/325/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/FC%20Utrecht.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="Feyenoord" , action="youtube_playlists" , url="FeyenoordRotterdamTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/198/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Feyenoord.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="Heracles" , action="youtube_playlists" , url="HeraclesAlmeloTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/2038/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Heracles%20Almelo.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="NAC" , action="youtube_playlists" , url="NACBredaNL",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/423/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/nac.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="PEC Zwolle" , action="youtube_playlists" , url="peczwolletv",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/424/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/PEC%20Zwolle.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="PSV" , action="youtube_playlists" , url="psveindhoven",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/204/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/PSV.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="Roda JC" , action="youtube_playlists" , url="RodaJCKerkradeTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/322/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Roda%20JC%20Kerkrade.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="Sparta" , action="test" , url="v=iK7zGDhvKEU",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/323/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Sparta%20Rotterdam.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="VVV Venlo" , action="youtube_playlists" , url="TheOfficialVVVVenlo",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/876/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/vvv%20venlo.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="Vitesse" , action="youtube_playlists" , url="VitesseTV",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/232/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Vitesse.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="Willem II" , action="youtube_playlists" , url="WillemII",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/207/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/Willem%20II.jpg', folder=True) )
    itemlist.append( Item(channel=CHANNELNAME, title="SV Heerenveen" , action="youtube_playlists" , url="scHeerenveen",thumbnail='https://eredivisie-images.s3.amazonaws.com/Eredivisie%20images/Eredivisie%20Badges/318/150x150.png',fanart='https://www.eredivisie.nl/DesktopModules/DotControl/DCEredivisieLive/Content/Image/Stadium/sc%20Heerenveen.jpg', folder=True) )
    

    return itemlist

# Show all YouTube playlists for the selected channel
def youtube_playlists(item):
    return youtube_channel.playlists(item,item.url)

def test(item):
    itemlist=[]
    url = "https://www.youtube.com/watch?v="+item.url
    itemlist.append( Item(channel=CHANNELNAME, action="play", server="youtube", title=item.title, url=url, folder=True))

    return itemlist


