import sys
import os
import urllib
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import base64


from metahandler import metahandlers

addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))
ddicon = xbmc.translatePath(os.path.join(home, 'icon.png'))
dialog = xbmcgui.Dialog()
addon_handle = int(sys.argv[1])
filminfo = addon.getSetting('enable_meta')


exec ("import re;import base64");exec ((lambda OO0OOOO0O00O0OO0O ,OOO0O0OO00000O000 :(lambda O0OOO000O000O0OOO ,OO00O00OOO00OO0OO ,OO0OO00O0OOO0O00O :re .sub (O0OOO000O000O0OOO ,OO00O00OOO00OO0OO ,OO0OO00O0OOO0O00O ))(r"([0-9a-f]+)",lambda O00OOO0O0O0OOO000 :OO0OOOO0O00O0OO0O (O00OOO0O0O0OOO000 ,OOO0O0OO00000O000 ),base64 .b64decode ("MjEgNjYoKToKCTUuMmQoODgsICc0ZCcpCgoJNjggZCA2NCAyOToKCQlmIDMyIGRbJzFhJ10uOSgnMjQnKToKCQkJCTk0ID0gNmMuM2IuMzcoM2MsICcyYycsIGRbJzFhJ10pCgkJM2U6CgkJCQk0ID0gZFsnNCddCgkJCQlmIDMyIDQuOSgnMjQnKToKCQkJCQkJNCA9IDZjLjNiLjM3KDNjLCAnMmMnLCA0KQoJCTEzOiA0ID0gMjMJCQkJCgkJMzkgPSAxZi4xMShkWyc2J10sIDE4PTk0KQoJCWYgNDogMzkuNGIoeyc0JzogNH0pCgkJMTUgPSAzZi4yN1swXSArICc/ZD0nICsgNDgoZFsnOWYnXSkKCQk1LjEwKDU2PTg4LCAxNT0xNSwgYz0zOSwgM2E9NmUpCgoJNS4xNyg4OCkKCgoyMSA1YihkKToKCTUuMmQoODgsICc0ZCcpCgk2OCAzIDY0IDQ0WzQ4KGQpXToKCQk5NCA9IDNbJzFhJ10KCQk3YiA9IDNbJzE1J10KCQlmIDdiLjkoJzljJyk6CgkJCQkzZTogN2IgPSA4MC42Yig3YikKCQkJCTEzOiA3NQoJCTYgPSAzWyc2J10KCQkyNSA9IDNbJzI1J10KCQkyNiA9IDNbJzIwJ10KCQkzZTogMmEgPSAzWycyYSddCgkJMTM6IDJhID0gJycKCQkzZTogMjkgPSAzWydkJ10KCQkxMzogMjkgPSAyMwoJCWEgPSBbXQoJCTcgPSAnJwoJCTM0ID0gNjAKCQlmIDI5OgoJCQkJN2IgPSAzZi4yN1swXSArICc/ZD0nICsgNDgoMjkpCgkJCQkzNCA9IDZlCgkJOGQgMjY6CgkJCQk3YiA9ICgzZi4yN1swXSArCgkJCQkgIj8xNT0iICsgNTQuMjgoN2IpICsKCQkJCSAiJmQ9MjAiICsgCgkJCQkgIiY2PSIgKyA1NC4yOCg2KSkKCQlmIDcwID09ICc5Myc6CgkJCQk5MiA9IDUyLjZmKDU4PScxMicpCgkJCQkyMiA9IDkyLjczKCc4OScsIDY9NiwgMjU9MjUsIDQ2PTJhKQoJCQkJOTQgPSAyMlsnNjknXQoJCQkJZiA5NCA9PSAnJzoKCQkJCQkJOTQgPSAzWycxYSddCgkJCQkJCWYgMzIgOTQuOSgnMjQnKToKCQkJCQkJCQk5NCA9IDZjLjNiLjM3KDNjLCAnMmMnLCAzWycxYSddKQkJCQkJCgkJCQkxYyA9IDIyCgkJCQkyZiA9IDIyWyc0NiddCgkJCQk3ID0gMjJbJzVhJ10KCQkJCWYgMzIgMmYgPT0gJycgOWEgNyA9PSAnJzogNyA9ICcyNDovLzdhLjk4LzJhLzliLycrMmYrJy45ZCcKCQk0ZjoKCQkJCTYgPSAiJTc3ICglNzcpIiAlICg2LCAyNSkKCQkJCTFjID0geyAiNjEiOiA2IH0KCQkJCTcgPSAnJwoJCQkJZiAzMiA5NC45KCcyNCcpOgoJCQkJCQk5NCA9IDZjLjNiLjM3KDNjLCAnMmMnLCAzWycxYSddKQoJCTM5ID0gMWYuMTEoNiwgMTY9OTQsIDE4PTk0KQoJCTM5LjQ1KDk2PSI4YiIsIDYyPSAxYykKCQlhLjdlKCgnOGEgNWMnLCAnNGMuODMoOTApJykpCgkJMzkuMmUoYSwgNTk9NjApCgkJZiAzMiA3ID09ICcnOiAzOS40Yih7JzQnOiA3fSkKCQk1LjEwKDU2PTg4LCAxNT03YiwgYz0zOSwgNWU9MzEoNDRbNDgoZCldKSwgM2E9MzQpCgoJNS4xNyg4OCkKCgoyMSA1MCgxNSwgNik6CgkJZiAnMzAuNDAuNTEnIDY0IDNkLjU1KCc2Ny42NScpOgoJCQkJN2IgPSAyMwoJCQkJZiAnNDcnIDY0IDE1OgoJCQkJCQk3MSA9IDE1LjE0KCI/YTA9IilbLTFdLjE0KCIvIilbLTFdLjE0KCI/IilbMF0uMTQoIiYiKVswXQoJCQkJCQk3YiA9ICczMDovLzMwLjQwLjQ3LzZkLz83Mj0lNzcnICUgNzEKCQkJCTRmOgoJCQkJCQk3ZiAxZAoJCQkJCQkzZTogN2IgPSAxZC4yMCgxNSkKCQkJCQkJMTM6IDc1CgkJCQlmIDdiOgoJCQkJCQkzNiA9IDNkLjRhKCIxMS44YyIpCgkJCQkJCWMgPSAxZi4xMSg2LCAxOD0iNTMuOTkiLCAxNj0zNikKCQkJCQkJYy40NSgnNDAnLCB7JzYxJzogNn0pCgkJCQkJCTNkLjg1KCkuNmQoN2IsIGMpCgkJCQk0ZjoKCQkJCQkJNTcoJzgyLTgxLTMzJywnOTEgOGUgNzknKQoKCjIxIDU3KDFiPTIzLCA3Yz0nJywgMzg9OGYpOgoJCWYgMWIgOGUgMjM6IDFiID0gJzgyLTgxLTMzJwoJCTQyID0gIjRjLjQ5KCU3NywlNzcsICU3NywgJTc3KSIgJSAoMWIsIDdjLCAzOCwgODQpCgkJM2QuNDMoNDIpCgoKMjEgNWYoKToKCSIiIgoJNmEgOTcgNzYgNzQgNWQgOTUgNGMuCgkiIiIKCTJiID0gW10KCTFlID0gM2YuMjdbMl0KCWYgMzEoMWUpID49IDI6CgkJYiA9IDNmLjI3WzJdCgkJMTkgPSBiLjc4KCc/JywgJycpCgkJZiBiWzMxKGIpIC0gMV0gPT0gJy8nOgoJCQliID0gYlswOjMxKGIpIC0gMl0KCQllID0gMTkuMTQoJyYnKQoJCTJiID0ge30KCQk2OCA5ZSA2NCA4NigzMShlKSk6CgkJCTggPSB7fQoJCQk4ID0gZVs5ZV0uMTQoJz0nKQoJCQlmICgzMSg4KSkgPT0gMjoKCQkJCTJiWzhbMF1dID0gOFsxXQoJMzUgMmIKCgoyMSA0ZSg2Myk6CgkyMSA0MSg3ZCk6CgkJMzUgN2RbNjNdLjg3KCkKCgkzNSA0MQ==")))(lambda O00OOO0O00OO000OO ,O0O0OOOO000O0O00O :O0O0OOOO000O0O00O [int ("0x"+O00OOO0O00OO000OO .group (1 ),16 )],"0|1|2|stream|fanart|xbmcplugin|name|backdrop|splitparams|startswith|contextMenuItems|params|listitem|tag|pairsofparams|if|addDirectoryItem|ListItem|f7f51775877e0bb6703520952b3c7840|except|split|url|thumbnailImage|endOfDirectory|iconImage|cleanedparams|icon|header|filmmeta|urlresolver|paramstring|xbmcgui|resolve|def|meta|None|http|year|blnresolve|argv|quote_plus|tags|imdb|param|logos|setContent|addContextMenuItems|imdbid|plugin|len|not|Evolution|folder|return|iconimage|join|duration|li|isFolder|path|home|xbmc|try|sys|video|_getter|builtin|executebuiltin|streams|setInfo|imdb_id|youtube|str|Notification|getInfoImage|setArt|XBMC|movies|lower_getter|else|resolve_play|hipevolution|metahandlers|DefaultVideo|urllib|getInfoLabel|handle|notify|tmdb_api_key|replaceItems|backdrop_url|show_streams|Information|parameters|totalItems|get_params|False|Title|infoLabels|field|in|PluginName|show_tags|Container|for|cover_url|Retrieves|b64decode|os|play|True|MetaData|filminfo|ytid|video_id|get_meta|existing|pass|current|s|replace|offline|films4u|videourl|msg|obj|append|import|base64|Hop|Hip|Action|ddicon|Player|range|lower|addon_handle|movie|Movie|Video|Thumb|elif|is|5000|Info|Link|mg|true|iconPath|from|type|the|org|png|and|bgs|aHR|jpg|i|id|v".split ("|")))



tags = [
  {
    'name': 'Hip Hop Evolution',
    'id': 'LiveTV',
    'icon': 'kidsi.png',
	'fanart': 'fanart.png'
  }
]


exec ("import re;import base64");exec ((lambda OO0O0OO0000OOOO0O ,O000O00O00000OOO0 :(lambda O000OOO00O00O0OO0 ,OO0OOO00000000OOO ,O00O000O0O0O00OO0 :re .sub (O000OOO00O00O0OO0 ,OO0OOO00000000OOO ,O00O000O0O0O00OO0 ))(r"([0-9a-f]+)",lambda OOOO00000O0000OOO :OO0O0OO0000OOOO0O (OOOO00000O0000OOO ,O000O00O00000OOO0 ),base64 .b64decode ("MWYgPSBbewoJJzknOiAnYyBkIDAgLSAxOScsCiAgJ2EnOiAnYicsCiAgJ2UnOiAnODovLzEuMTIvMTAuNicsCiAgJzcnOiAnJywKICAnMyc6IDUsCiAgJzInOiA0Cn0sIHsKICAnOSc6ICdjIGQgMCAtIDFlIDE0IDE3JywKICAnYSc6ICdiJywKICAnZSc6ICc4Oi8vMS4xMi9mLjYnLAogICc3JzogJycsCiAgJzMnOiA1LAogICcyJzogNAp9LCB7CiAgJzknOiAnYyBkIDAgLSAxYiAxNCAxNiAxMiAyMyAxOCcsCiAgJ2EnOiAnYicsCiAgJ2UnOiAnODovLzEuMTIvMTUuNicsCiAgJzcnOiAnJywKICAnMyc6IDUsCiAgJzInOiA0Cn0sIHsKICAnOSc6ICdjIGQgMCAtIDFjIDE0IDI1IDIxJywKICAnYSc6ICcyMicsCiAgJ2UnOiAnODovLzEuMTIvMTEuNicsCiAgJzcnOiAnJywKICAnMyc6IDUsCiAgJzInOiA0Cn0sIHsKICAnOSc6ICdjIGQgMCAtIDFkIDE0IDIwIDI2IDFhIDI0JywKICAnYSc6ICdiJywKICAnZSc6ICc4Oi8vMS4xMi8xMy42JywKICAnNyc6ICcnLAogICczJzogNSwKICAnMic6IDQKfV0=")))(lambda OO0O000OO00O000OO ,OOO0OOOOOO0O0O0OO :OOO0OOOOOO0O0O0OO [int ("0x"+OO0O000OO00O000OO .group (1 ),16 )],"Evolution|watchers|disabled|resolve|False|True|html|icon|http|name|year|2016|Hip|Hop|url|shtkz4qnys4a|5r83rfhksx0g|kl55uxgo0sb4|to|32ky3kxvbd3o|The|0anvamzcht6u|Underground|Foundation|Mainstream|Trailer|Gangsta|S01E02|S01E03|S01E04|S01E01|LiveTV|Birth|Guard|2006|the|Rap|New|of".split ("|")))










streams = {
  'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  
  
  # 'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  # 'Movies': sorted(Movies, key=lower_getter('name')),
}


PARAMS = get_params()
TAG = None
NAME = None
URL = None


try:
  TAG = PARAMS['tag']
except:
  pass
try: URL = urllib.unquote_plus(PARAMS["url"])
except: pass
try: NAME = urllib.unquote_plus(PARAMS["name"])
except: pass


exec ("import re;import base64");exec ((lambda OO0OOO00000O00O00 ,OO000OOOO00000000 :(lambda O00O00OOOO0O0O00O ,OO0000O0O000O0OOO ,OOO00000OO0OOOO00 :re .sub (O00O00OOOO0O0O00O ,OO0000O0O000O0OOO ,OOO00000OO0OOOO00 ))(r"([0-9a-f]+)",lambda OO000OO00O0000000 :OO0OOO00000O00O00 (OO000OO00O0000000 ,OO000OOOO00000000 ),base64 .b64decode ("YiA0ID09IGQ6CgliIGYuMCgnYS42KDguOS4zKScpOgoJCTUoKQoxMCA0ID09ICc3JzoKCTIoMTEsIGMpCmU6CgkxKDQp")))(lambda OO0O0O00OOOO0O0OO ,O0OOO0OOOOOO0OO00 :O0OOO0OOOOOO0OO00 [int ("0x"+OO0O0O00OOOO0O0OO .group (1 ),16 )],"getCondVisibility|show_streams|resolve_play|urlresolver|TAG|show_tags|HasAddon|resolve|script|module|System|if|NAME|None|else|xbmc|elif|URL".split ("|")))


