#!/usr/bin/python

import xbmc,xbmcaddon,xbmcgui,xbmcplugin
#import os,shutil,time
#import urllib2,urllib

addon_id		= 'script.xvbmc.dev'
AddonID			= 'script.xvbmc.dev'
ADDON			= xbmcaddon.Addon(id=AddonID)
addonInfo		= xbmcaddon.Addon().getAddonInfo
dialog			= xbmcgui.Dialog()

def okDialog(line1, line2, line3, heading=addonInfo('name')):
    return dialog.ok(heading, line1, line2, line3)

okDialog('[COLOR red][B]Sorry, this addon is abandoned![/B][/COLOR]','','[COLOR lime]Goto [COLOR dodgerblue]http://bit.ly/XvBMC-NL[/COLOR], [COLOR dodgerblue]http://bit.ly/XvBMC-Pi[/COLOR] or [COLOR dodgerblue]https://bit.ly/XvBMC-Android[/COLOR] for more information...[/COLOR]')