import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Football','http://www.hesgoals.sc/',246,'https://2.bp.blogspot.com/-nPM2WTm78RY/V0I1k04gNUI/AAAAAAAAA-M/wWeh_Bwn63oW6QRQCJQiWV__IaCDscXXQCLcB/s1600/hesgoal.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Racing','http://www.hesgoals.sc/',245,'https://2.bp.blogspot.com/-nPM2WTm78RY/V0I1k04gNUI/AAAAAAAAA-M/wWeh_Bwn63oW6QRQCJQiWV__IaCDscXXQCLcB/s1600/hesgoal.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
#match = re.compile('<h2>Racing News</h2>(.*?)<a href="http://www.hesgoals.sc/news/2066/Bad_day_for_Mercedes_ad_Lewis_Hamilton.html">', re.IGNORECASE | re.DOTALL).findall(listhtml)

def ListRacing(url):
    referer = 'http://www.hesgoals.sc/'
    listhtml = utils.getHtml(url, '')
    match = re.compile('<h2>Racing News</h2>(.*?)<a href="http://www.hesgoals.sc/news/2066/Bad_day_for_Mercedes_ad_Lewis_Hamilton.html">', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for page in match:
        match2 = re.compile('<div class="icon">.*?href="(.*?)">.*?src="(.*?)".*?alt="(.*?)".*?<p>(.*?)</p>', re.IGNORECASE | re.DOTALL).findall(page)
        for videopage, img, name, tijdcompetitie in match2:
            tijdcompetitie = tijdcompetitie.replace('\n', '')
            name = tijdcompetitie + ' - ' + name
            iframe = utils.getHtml(videopage, videopage)
            iframe2 = re.compile('scrolling="no" src="//(.*?)"', re.IGNORECASE | re.DOTALL).findall(iframe)
            for videopagina in iframe2:
                videopagina = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://' + videopagina
                utils.addDir(name, videopagina, 300, img, '', fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/plugin.video.jericho/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListFootball(url):
    referer = 'http://www.hesgoals.sc/'
    listhtml = utils.getHtml(url, '')
    match = re.compile('<h2>Football News</h2>(.*?)Dylan_and_De_Smul_with_The_Blues.html"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for page in match:
        match2 = re.compile('<div class="icon">.*?href="(.*?)">.*?src="(.*?)".*?alt="(.*?)".*?<p>(.*?)</p>', re.IGNORECASE | re.DOTALL).findall(page)
        for videopage, img, name, tijdcompetitie in match2:
            tijdcompetitie = tijdcompetitie.replace('\n', '')
            name = tijdcompetitie + ' - ' + name
            iframe = utils.getHtml(videopage, videopage)
            iframe2 = re.compile('scrolling="no" src="//(.*?)"', re.IGNORECASE | re.DOTALL).findall(iframe)
            for videopagina in iframe2:
                videopagina = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://' + videopagina
                utils.addDir(name, videopagina, '', img, '', fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/plugin.video.jericho/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)