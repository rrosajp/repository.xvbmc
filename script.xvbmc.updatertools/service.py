#!/usr/bin/python
""#line:6
import os as O00O0OO0O00O0OOOO ,xbmc as OO00OO00OOO0OOO00 ,xbmcaddon as O0OO00OO0OOOO0OOO ,xbmcgui as O00OO0OO00O0OOO0O ,xbmcplugin as OO00O00000OO0OO00 #line:8
import utils as O00O00O0O0O00000O #line:9
AddonID ='script.xvbmc.updatertools'#line:11
ADDON =O0OO00OO0OOOO0OOO .Addon (id =AddonID )#line:12
dialog =O00OO0OO00O0OOO0O .Dialog ()#line:14
MainTitle ="[COLOR lime][B]XvBMC[/B] Update[/COLOR]"#line:15
Subtitle ='[COLOR white]There is a new [B]XvBMC[/B] update[/COLOR]'#line:16
Updatevraag ='[COLOR white]Do you whish to update XvBMC [COLOR orange][B]now[/B][/COLOR], or later[B]?[/B][/COLOR]'#line:17
NU ="[COLOR lime]NOW[/COLOR]"#line:19
misschien ="[COLOR red]Later [B] :'([/B][/COLOR]"#line:20
OO00OO00OOO0OOO00 .sleep (5000 )#line:22
updatechk ,versie =O00O00O0O0O00000O .checkUpdate ()#line:24
if updatechk =='update':#line:26
   yes_pressed =dialog .yesno (MainTitle ,Subtitle +'[COLOR white] for your Portable[/COLOR]',Updatevraag ,'',yeslabel =NU ,nolabel =misschien )#line:27
   if yes_pressed :#line:28
      OO00OO00OOO0OOO00 .executebuiltin ('ActivateWindow(10001,plugin://script.xvbmc.updatertools/,return)')#line:29
   else :#line:30
      dialog .ok (MainTitle ,'[COLOR white]You can update [B]XvBMC[/B] the next time you reboot...[/COLOR]','','')#line:31
elif updatechk =='wizupdate':#line:33
     yes_pressed =dialog .yesno (MainTitle ,Subtitle +'[COLOR white] for your Wizard[/COLOR]',Updatevraag ,'',yeslabel =NU ,nolabel =misschien )#line:34
     if yes_pressed :#line:35
        OO00OO00OOO0OOO00 .executebuiltin ('ActivateWindow(10001,plugin://script.xvbmc.updatertools/,return)')#line:36
     else :#line:37
        dialog .ok (MainTitle ,'[COLOR white]You can update [B]XvBMC[/B] the next time you reboot...[/COLOR]','','')#line:38
elif updatechk =='rpiupdate':#line:40
     yes_pressed =dialog .yesno (MainTitle ,Subtitle +'[COLOR white] for your RPi[/COLOR]',Updatevraag ,'',yeslabel =NU ,nolabel =misschien )#line:41
     if yes_pressed :#line:42
        OO00OO00OOO0OOO00 .executebuiltin ('ActivateWindow(10001,plugin://script.xvbmc.updatertools/,return)')#line:43
     else :#line:44
        dialog .ok (MainTitle ,'[COLOR white]You can update [B]XvBMC[/B] the next time you reboot...[/COLOR]','','')
