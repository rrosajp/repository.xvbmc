#!/usr/bin/python
#-*- coding: utf-8 -*-
 
"""
    IF you copy/paste 'plugin.audio.ctrl-radio' please keep the credits -2- XvBMC-NL, Thx.
"""

#   EPiC '.:C.T.R.L:. radio' by XvBMC Nederland (NL)
#
#   Copyright (C) 2018
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import base64,os,re,sys
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
addon_handle=int(sys.argv[1])
xbmcplugin.setContent(addon_handle,'music')
addon=xbmcaddon.Addon('plugin.audio.ctrl-radio')
addonID='plugin.audio.ctrl-radio'
addonname=addon.getAddonInfo('name')
home=xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon=os.path.join(home,'icon.png')
fanart=os.path.join(home,'fanart.jpg')
local=xbmcaddon.Addon(id=addonID)
titel='.:C.T.R.L:. radio by XvBMC-NL'
artiest='various'
elpee='XvBMC-NL presents .:C.T.R.L:. radio'
rubriek='Retro VoOdOo'
jaar='2018'
songtekst='8bit retro gaming music for n00bs and nerdzZz'
xvbmc='[B][COLOR dodgerblue].[/COLOR][COLOR blue]:[/COLOR][COLOR darkgreen]C[/COLOR][COLOR limegreen].[/COLOR][COLOR yellow]T[/COLOR][COLOR orange].[/COLOR][COLOR purple]R[/COLOR][COLOR red].[/COLOR][COLOR hotpink]L[/COLOR][COLOR dodgerblue]:[/COLOR][COLOR blue].[/COLOR][/B] [COLOR dimgray][8bit][/COLOR][B] [COLOR white]-Retro Radio-[/COLOR][/B]'
def log(msg,level=xbmc.LOGNOTICE):
 name='XvBMC_NOTICE'
 level=xbmc.LOGNOTICE
 try:
  xbmc.log('%s: %s'%(name,msg),level)
 except:
  try:
   xbmc.log('Logging Failure',level)
  except:
   pass
module_log_enabled=False
def _log(message):
 if module_log_enabled:
  xbmc.log("ctrl-radio."+message)
def setView(content,viewType):
 if content:
  xbmcplugin.setContent(int(sys.argv[1]),content)
 if local.getSetting('auto-view')=='true':
  xbmc.executebuiltin("Container.SetViewMode(%s)"%local.getSetting(viewType))
url = base64.b64decode('aHR0cDovL2N0cmwtcmFkaW8ubmw6ODAwMC9hdXRvZGoubTN1')
li=xbmcgui.ListItem(xvbmc,iconImage="DefaultVideo.png",thumbnailImage=icon)
li.setInfo(type="Music",infoLabels={"Title":titel,"Artist":artiest,"Album":elpee,"Genre":rubriek,"year":jaar,"lyrics":songtekst})
audio_streaminfo={'codec':'DTS'}
li.addStreamInfo('Audio',audio_streaminfo)
li.setProperty("Fanart_Image",fanart)
setView('music','EPiC')
xbmcplugin.addDirectoryItem(handle=addon_handle,url=url,listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
def find_single_match(text,pattern):
 _log("find_single_match pattern="+pattern)
 result=""
 try:
  matches=re.findall(pattern,text,flags=re.DOTALL)
  result=matches[0]
 except:
  result=""
 return result
f=open(os.path.join(os.path.dirname(__file__),"addon.xml"))
data=f.read()
f.close()
addon_id=find_single_match(data,'id="([^"]+)"')
if addon_id=="":
 addon_id=find_single_match(data,"id='([^']+)'")
__settings__=xbmcaddon.Addon(id=addon_id)
__language__=__settings__.getLocalizedString
"""
    IF you copy/paste 'plugin.audio.ctrl-radio' please keep the credits -2- XvBMC-NL, Thx.
"""