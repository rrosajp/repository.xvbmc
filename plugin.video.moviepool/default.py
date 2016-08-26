# -*- coding: utf-8 -*-
import moviepool,plugintools,urllib,xbmcplugin,xbmc,xbmcgui,re
from metahandler import metahandlers
metaget = metahandlers.MetaData()

def show_categories():
    plugintools.add_item(title=u"Search",action='search')
    plugintools.add_item(title=u"All Movies",url="http://moviepool.net/?filtre=date&cat=0",action='page')
    plugintools.add_item(title=u"Categories",url="http://moviepool.net/categories",action='categories')
    plugintools.close_item_list()
    
def show_page(url,action):
    items = moviepool.getPage(url)
    
    for item in items:
        if item.get("title") != "Next":
            if action!="page":
                plugintools.add_item(itemcount=len(items),meta=metaget.get_meta('movie',re.sub(r" \([0-9]*\)","",item.get('title').encode("utf-8")),''),title=item.get('title'),extra=item.get('title'),url=item.get('url'),thumbnail=item.get("thumbnail"),action=action)
            else:
                plugintools.add_item(itemcount=len(items),title=item.get('title'),extra=item.get('title'),url=item.get('url'),thumbnail=item.get("thumbnail"),action=action)
        else:
            plugintools.add_item(title=item.get('title'),url=item.get('url'),action="page")
    plugintools.close_item_list()

def get_search():
    searchtext=""
    keyboard = xbmc.Keyboard(searchtext,"Enter search query")
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        results = moviepool.search(keyboard.getText())
        try:
            for movie in results:
                plugintools.add_item(meta=metaget.get_meta('movie',re.sub(r" \([0-9]*\)","",movie.get('title')),''),title=movie.get('title'),extra=movie.get('title'),action='movie',url=movie.get('url'),thumbnail=movie.get("thumbnail"))
            plugintools.close_item_list()
        except:
            xbmcgui.Dialog().ok("Error","Could not find the movie")
        
    
def get_streams(url,extra):
    streams = moviepool.getStreams(url)
    for strm in streams:
        plugintools.add_item(title=strm.get('label'),url=strm.get('file'),action='stream',extra=extra)
    plugintools.close_item_list()

def stream(url,title):
    try:
        meta = metaget.get_meta('movie',re.sub(r" \([0-9]*\)","",title))
        listitem = xbmcgui.ListItem( title, iconImage="DefaultVideo.png", thumbnailImage=meta.get('cover_url') )
        meta['title']=title
        listitem.setProperty('fanart_image', meta.get('backdrop_url'))
        listitem.setInfo('video',meta)
        
        xbmc.Player().play(url,listitem)
    except:
        li = xbmcgui.ListItem(label=title,path=url)
        li.setInfo(type='Video', infoLabels={ "Title": str(title) })
        xbmc.Player().play(url,li)
        
def run():
    params = plugintools.get_params()
    action = params.get('action')
    if action == None:
        show_categories()
    elif action == 'page':
        show_page(params.get("url"),"movie")
    elif action == 'categories':
        show_page(params.get("url"),"page")
    elif action == 'search':
        get_search()
    elif action == 'movie':
        get_streams(params.get('url'),params.get('extra'))
    elif action == 'stream':
        stream(params.get('url'),params.get('extra'))
    
run()