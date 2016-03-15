'''
    IF you copy/paste 'script.xvbmc.upper' please keep the credits -2- EPiC -4- XvBMC, Thx.
'''
 
import xbmc, xbmcgui
import shutil
import urllib2,urllib
import os
import xbmcaddon
 
if sys.version_info >=  (2, 7):
    import json as json
else:
    import simplejson as json 
 
########################################################################
__ScriptName__ = "script.XvBMC.upper"
__ScriptVersion__ = "2.0.0"
__Author__ = "EPiC"
__Website__ = "http://WatBenJeDan.nl/"
########################################################################
 
# Set the addon environment
addon = xbmcaddon.Addon('script.xvbmc.upper')
 
# Parse command parameters
try:
    # parse sys.argv for params
    try:
        params = dict(arg.split("=") for arg in sys.argv[1].split("&"))
    except:
        params =  dict(sys.argv[1].split("="))
except:
    # no params passed
    params = {}   
 
  
   
def showMenu():
    '''Set up our main menu.'''
    
    # Create list of menu items
    userchoice = []
    userchoice.append("Isengard Upgrade")
    userchoice.append("Jarvis Upgrade")
    userchoice.append("Beta OE8 Upgrade")
    userchoice.append("EPiC Tweak")
    userchoice.append("Exit")
    
    # Display the menu  
    inputchoice = xbmcgui.Dialog().select("XvBMC Kodi Upgrader", 
                                           userchoice)
    # Process menu actions
    
    # Isengard Upgrade    
    if userchoice[inputchoice] == "Isengard Upgrade":
        IsengardUpgrade()
    
    # Jarvis Upgrade
    elif userchoice[inputchoice] == "Jarvis Upgrade":
        JarvisUpgrade()

    # BETA's Upgrade
    elif userchoice[inputchoice] == "Beta OE8 Upgrade":
        BETAupgrade()
 
    # Edit user preferences
    elif userchoice[inputchoice] == "EPiC Tweak":
        xbmcgui.Dialog().ok("XvBMC Nederland", "EPiC Tweaking bitches", "Coming soon to a theater near you ;-P")
 
  
   
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create('XvBMC EPiC OpenELEC Upgrade','XvBMC Kodi upgrade downloaden','')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print 'Gedownload:'+str(percent)+'%'
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print 'Download Geannuleerd' # does it break, or does it not break, that is the question :-P
        dp.close()
 
 
class IsengardClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('EPiC XvBMC Upgrade','Upgrade -2- Isengard?'):
        url = 'http://milhouse.openelec.tv/builds/master/RPi2/OpenELEC-RPi2.arm-6.0-Milhouse-20150701210203-%230701-g96e5cfe.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/','')) # OpenELEC   (XvBMC Nederland : https://www.facebook.com/groups/XbmcVoorBeginnersRaspberryPi/)
    #   path = xbmc.translatePath(os.path.join('special://home',''))    # Standalone (https://www.facebook.com/groups/XvBMCnederland/)
        lib=os.path.join(path, 'isengard.tar')
        DownloaderClass(url,lib)
    
   	xbmc.executebuiltin("ReloadKeymaps")
   	xbmc.executebuiltin("ReloadSkin()")
   	xbmc.executebuiltin("Notification(XvBMC EPiC OpenELEC Upgrade,EPiC Isengard upgrade geslaagd,5000,special://skin/icon.png)")
 
class JarvisClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('EPiC XvBMC Upgrade','Upgrade -2- Jarvis?'):
        url = 'http://milhouse.openelec.tv/builds/master/RPi2/OpenELEC-RPi2.arm-7.0-Milhouse-20151204210207-%231204-gc5875ae.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/','')) # OpenELEC   (XvBMC Nederland : https://www.facebook.com/groups/XbmcVoorBeginnersRaspberryPi/)
    #   path = xbmc.translatePath(os.path.join('special://home',''))    # Standalone (https://www.facebook.com/groups/XvBMCnederland/)
        lib=os.path.join(path, 'jarvis.tar')
        DownloaderClass(url,lib)
     
   	xbmc.executebuiltin("ReloadKeymaps")
   	xbmc.executebuiltin("ReloadSkin()")
   	xbmc.executebuiltin("Notification(XvBMC EPiC OpenELEC Upgrade,EPiC Jarvis upgrade geslaagd,5000,special://skin/icon.png)")
 
class BetaClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('EPiC XvBMC Upgrade','Upgrade -2- OE8 BETA'):
        url = 'http://milhouse.openelec.tv/builds/master/RPi2/OpenELEC-RPi2.arm-8.0-Milhouse-20160314220202-%230314-g0026734.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/','')) # OpenELEC   (XvBMC Nederland : https://www.facebook.com/groups/XbmcVoorBeginnersRaspberryPi/)
    #   path = xbmc.translatePath(os.path.join('special://home',''))    # Standalone (https://www.facebook.com/groups/XvBMCnederland/)
        lib=os.path.join(path, 'betas.tar')
        DownloaderClass(url,lib)
     
   	xbmc.executebuiltin("ReloadKeymaps")
   	xbmc.executebuiltin("ReloadSkin()")
   	xbmc.executebuiltin("Notification(XvBMC EPiC OpenELEC Upgrade,EPiC OE8 upgrade geslaagd,5000,special://skin/icon.png)")
   
  
 
def IsengardUpgrade():
    mydisplay = IsengardClass()
    del mydisplay
 
def JarvisUpgrade():
    mydisplay = JarvisClass()
    del mydisplay
 
def BETAupgrade():
    mydisplay = BetaClass()
    del mydisplay
 
  
   
########################################################################
# This is where we start!
########################################################################
 
showMenu()