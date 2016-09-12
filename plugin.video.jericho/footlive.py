import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('All','http://www.foot-live.info/',116,'','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    listhtml = utils.getHtml('http://www.foot-live.info/','http://www.foot-live.info/')
    match = re.compile(r'.*?<li>.*?<a href="\?(.*?)".*?src="(.*?)".*?\n\t\t\t\t..(.*?)\t\t\t\t</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for page, img, name in match:
        page = 'http://www.foot-live.info/?' + page
        img = 'http://www.foot-live.info' + img
        utils.addDir(name,page,116,img,'',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
#match = re.compile('<h2>Racing News</h2>(.*?)<a href="http://www.hesgoals.sc/news/2066/Bad_day_for_Mercedes_ad_Lewis_Hamilton.html">', re.IGNORECASE | re.DOTALL).findall(listhtml)

def List(url):
    bvlspage = utils.getHtml(url,url)
    matchtotal = re.compile('<p class="Day">- (.*?)</html>', re.IGNORECASE | re.DOTALL).findall(bvlspage)[0]
    match = re.compile('src="(.*?)".*?date">(.*?)</span>.*?href="(.*?)".*?\n\t\n\t\n\t\n\t\t.(.*?) :', re.IGNORECASE | re.DOTALL).findall(matchtotal)
    for img, tijd, videopage, wedstrijd in match:
        name = tijd + wedstrijd
        utils.addDir(name,videopage,117,img,'',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def Liststreams(url):
    bvlspage = utils.getHtml(url,url)
    match = re.compile('<li class="list-group-item"><a href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(bvlspage)
    for videopage, name in match:
        name = tijd + wedstrijd
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + videopage
        utils.addDir(name,videopage,300,'','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))