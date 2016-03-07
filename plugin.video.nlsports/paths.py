import os
import xbmc, xbmcaddon

__settings__ = xbmcaddon.Addon(id='plugin.video.nlsports')
__icon__ = xbmcaddon.Addon(id='plugin.video.nlsports').getAddonInfo('icon')

rootDir = xbmc.translatePath(__settings__.getAddonInfo('path')).decode('utf-8')
resDir = os.path.join(rootDir, 'resources')
imageDir = os.path.join(resDir, 'images')
videoDir = os.path.join(resDir, 'videos')
iconDir = os.path.join(imageDir, 'icons')
fanartDir = os.path.join(imageDir, 'fanarts')
