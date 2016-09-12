import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon
from datetime import datetime, timedelta
from time import time

import utils

def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)

def Main():
    utils.addDir('All','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C49%2C50%2C51%2C52%2C53%2C54%2C55%2C56%2C57%2C58%2C59%2C60%2C61%2C62%2C63%2C64%2C65%2C66%2C67%2C68%2C69%2C70%2C71%2C72%2C73%2C74%2C75%2C76%2C77%2C78%2C79%2C80%2C81%2C82%2C83%2C84%2C85%2C87%2C88%2C89%2C90%2C91%2C92%2C93%2C94%2C95%2C96%2C97%2C98%2C99%2C100&lng=en&partner=24',307,'http://sportstream365.com/img/logo_en.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Football','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=1&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m1.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Basketball','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=3&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m2.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Ice Hockey','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=2&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m3.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Volleyball','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=6&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m4.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('F1','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=26&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m5.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Tennis','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=4&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m6.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Boxing','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=9&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m7.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    utils.addDir('Others','http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=5%2C7%2C8%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C49%2C50%2C51%2C52%2C53%2C54%2C55%2C56%2C57%2C58%2C59%2C60%2C61%2C62%2C63%2C64%2C65%2C66%2C67%2C68%2C69%2C70%2C71%2C72%2C73%2C74%2C75%2C76%2C77%2C78%2C79%2C80%2C81%2C82%2C83%2C84%2C85%2C87%2C88%2C89%2C90%2C91%2C92%2C93%2C94%2C95%2C96%2C97%2C98%2C99%2C100&lng=en&partner=24',307,'http://sportstream365.com/img/menu/m8.jpg','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    


def List(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile(r'"FirstGameId":(\d+),.*?"Liga":"([^"]*)".*?"Opp1":"([^"]*)","Opp2":"([^"]*).*?Sport":"([^"]+)".*?"Start":(\d+)', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for id,liga,title1,title2,sport,time in match:  
        name = '[COLOR cyan] ' + sport +  '[COLOR lime] - [' + liga + '][/COLOR] ' + title1 + ' - ' + title2
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=http://sportstream365.com/viewer?game=' + id
        utils.addDownLink(name, videopage, 300, '', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)