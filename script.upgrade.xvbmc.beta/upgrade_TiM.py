import xbmc, xbmcgui
import shutil
import urllib2,urllib
import os
import xbmcaddon

addon = xbmcaddon.Addon('script.upgrade.xvbmc.beta')

def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create('XvBMC EPiC Upgrade','XvBMC Jarvis upgrade downloaden','')
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
        print 'Download Geannuleerd' # still need to get this part working
        dp.close()

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno('EPiC XvBMC Upgrade','Upgrade -2- Jarvis?'):
        url = 'http://milhouse.openelec.tv/builds/master/RPi2/OpenELEC-RPi2.arm-7.0-Milhouse-20151204210207-%231204-gc5875ae.tar'
        path = xbmc.translatePath(os.path.join('/storage/.update/',''))
        lib=os.path.join(path, 'jarvis.tar')
        DownloaderClass(url,lib)
     
   	xbmc.executebuiltin("ReloadKeymaps")
   	xbmc.executebuiltin("ReloadSkin()")
   	xbmc.executebuiltin("Notification(XvBMC EPiC Upgrade,EPiC upgrade geslaagd,5000,special://skin/icon.png)")
      
mydisplay = MyClass()
del mydisplay