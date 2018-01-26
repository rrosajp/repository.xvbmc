import base64,os,re,sys,xbmc,xbmcaddon,xbmcgui,xbmcplugin
import plugintools
addonID='plugin.video.Allesin1NL!'
addon_id='plugin.video.Allesin1NL!'
local=xbmcaddon.Addon(id=addonID)
icon=local.getAddonInfo('icon')
fanart=local.getAddonInfo('fanart')
def gasdrop():
 plugintools.log("XvBMC.VoOdOo")
 params=plugintools.get_params()
 if params.get("action")is None:
  hoofdlijst(params)
 else:
  action=params.get("action")
 plugintools.close_item_list()
def hoofdlijst(params):
 setView('movies','EPiC')
 plugintools.log("XvBMC.hoofdlijst "+repr(params))
 addons=base64.b64decode('L3BsYXlsaXN0cw==')
 joetjoepkanaal01=base64.b64decode('VUNWWDZlRWVJSVNjd0Fwek5zN1V1dnVn')+addons
 joetjoepkanaal02=base64.b64decode('VUNCcERKVWxUeGR4bnI4b1FwNGZXOGpB')+addons
 joetjoepkanaal03=base64.b64decode('VUMtWjhua2hwRzdEUXZPOHdlZ01IR0lR')+addons
 joetjoepkanaal04=base64.b64decode('VUNfeHc2WUJubHlMcVlub3BhYmJ6ZmlR')+addons
 joetjoepkanaal05=base64.b64decode('VUNKWTRFRDdCb2NWa3RpekFUa0VMM0Z3')+addons
 joetjoepkanaal06=base64.b64decode('VUN2TDRnYjhoaXc3NC1PczFoSnlDTEln')+addons
 joetjoepkanaal07=base64.b64decode("b25saW5lZmlsbXNraWprZW4=")
 joetjoepkanaal08=base64.b64decode('VUNyLUpCQzFYUHFKbV9POWlSMk0wV2pn')+addons
 joetjoepkanaal10=base64.b64decode('VUNoVndOQzI0aklsdTk4RzByR0Z0UVpR')+addons
 joetjoepkanaal11=base64.b64decode('VUMybjVBTTd2QWNNZVc4U0xta2pDZW5n')+addons
 joetjoepkanaal12=base64.b64decode('VUMzY3h2UEYxbWZ1MWF2ZEhPNlk5Tm53')+addons
 joetjoepkanaal13=base64.b64decode('VUMxa05lNTdGLTg1dHJyWUM3dGJPU1hB')+addons
 joetjoepkanaal14=base64.b64decode('VUNVZnNyU0w2RHlXU2trcGRkbFkyMS1R')+addons
 joetjoepkanaal15=base64.b64decode('RGFuY2VUcmlwcGluT2ZmaWNpYWw=')
 gebruiker=base64.b64decode('L3VzZXIv')
 jijbuis=base64.b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmU=')
 kanaal=base64.b64decode('L2NoYW5uZWwv')
 poster=base64.b64decode('Lw==')
 plugintools.add_item(title="Live Music",url=jijbuis+kanaal+joetjoepkanaal01+poster,thumbnail="https://archive.org/download/fanart_20170116/Live%20Music%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="NL Series",url=jijbuis+kanaal+joetjoepkanaal02+poster,thumbnail="https://archive.org/download/fanart_20170116/NL%20SERIE%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="NL Kids",url=jijbuis+kanaal+joetjoepkanaal03+poster,thumbnail="https://archive.org/download/fanart_20170116/NL%20KIDS%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="NL Films",url=jijbuis+kanaal+joetjoepkanaal04+poster,thumbnail="https://archive.org/download/fanart_20170116/NL%20FILM%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="NL Docu",url=jijbuis+kanaal+joetjoepkanaal05+poster,thumbnail="https://archive.org/download/fanart_20170116/NL%20Docu%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="NL Cabaret",url=jijbuis+kanaal+joetjoepkanaal06+poster,thumbnail="https://archive.org/download/fanart_20170116/NL%20CABARET%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="Xvbmc Handleidingen",url=jijbuis+gebruiker+joetjoepkanaal07+poster,thumbnail="https://archive.org/download/fanart_20170116/Xvbmc%20handleidingen%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="Vlaamse Content",url=jijbuis+kanaal+joetjoepkanaal08+poster,thumbnail="https://archive.org/download/fanart_20170116/Vlaams%20icon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title=".:C.T.R.L:. Gaming Room",url=jijbuis+kanaal+joetjoepkanaal10+poster,thumbnail="https://archive.org/download/fanart_20170116/CtrlGamingIcon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="Cirque du soleil",url=jijbuis+kanaal+joetjoepkanaal11+poster,thumbnail="https://archive.org/download/fanart_20170116/CircusIcon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="NL Racing",url=jijbuis+kanaal+joetjoepkanaal12+poster,thumbnail="https://archive.org/download/fanart_20170116/NlRacing.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="Van alles en nog wat NL",url=jijbuis+kanaal+joetjoepkanaal13+poster,thumbnail="https://archive.org/download/fanart_20170116/vanalles.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="Muziek Uit Limburg",url=jijbuis+kanaal+joetjoepkanaal14+poster,thumbnail="https://archive.org/download/fanart_20170116/NlLimburgIcon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
 plugintools.add_item(title="DanceTrippin TV",url=jijbuis+gebruiker+joetjoepkanaal15+poster,thumbnail="https://archive.org/download/fanart_20170116/DanceIcon.png",fanart="https://archive.org/download/fanart_20170116/fanart.jpg",folder=True)
def setView(content,viewType):
 if content:
  xbmcplugin.setContent(int(sys.argv[1]),content)
 if local.getSetting('auto-view')=='true':
  xbmc.executebuiltin("Container.SetViewMode(%s)"%local.getSetting(viewType))
gasdrop()
"""
    IF you copy/paste this please keep the credits -2- XvBMC-NL (and Coldkeys), Thx.
"""
# Created by pyminifier (https://github.com/liftoff/pyminifier)
