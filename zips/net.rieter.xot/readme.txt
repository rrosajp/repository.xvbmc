--------------------------------------------------------------------------------------------
 Retrospect 3.x.x
--------------------------------------------------------------------------------------------
 Contents
 0. License
 1. Introduction
 2. Changelog
 3. Skinning
 4. Known Issues
 4a.Some channels are not working? How come?
 5. Acknowledgements
 6. Donations
--------------------------------------------------------------------------------------------
 
--------------------------------------------------------------------------------------------
 0. License
--------------------------------------------------------------------------------------------
The Retrospect-Framework is licensed under the Creative Commons Attribution-Non-Commercial-No
Derivative Works 3.0 Unported License. To view a copy of this licence, visit 
http://creativecommons.org/licenses/by-nc-nd/3.0/ or send a letter to Creative Commons, 
171 Second Street, Suite 300, San Francisco, California 94105, USA. Files that belong to 
the Retrospect-Framework have a disclaimer stating that they are licensed under the Creative
Commons Attribution-Non-Commercial-No Derivative Works 3.0 Unported License.

All channels, skins and config.py (further called Retrospect Additions) are free software:
you can redistribute it and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, either version 3 of the License, or (at your 
option) any later version. Retrospect Additions are distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or 
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
details. You should have received a copy of the GNU General Public License along with 
Retrospect Additions. If not, see <http://www.gnu.org/licenses/>.
 
--------------------------------------------------------------------------------------------
 1. Introduction
--------------------------------------------------------------------------------------------
An XBox Media Center script which allows playback of streams from www.uitzendinggemist.nl. 
This version has options for streaming multiple past episodes from different TV Shows.
 
Discussion of the script can be done at this thread at the XBMC Forums. Please post any 
problems/suggestions in either of these threads:
 - http://www.xboxmediacenter.com/forum/showthread.php?p=130060) 
 - Most recent XBMC thread at http://gathering.tweakers.net (Dutch only)

Download the latest version at: 
 - http://www.rieter.net/content/ or use the official Retrospect repository (http://www.rieter.net/content/xot/downloads/#XBMC_Repository)

Direct contact can be done using the following e-mailadres: 
 - uitzendinggemist.vx[@t]gmail[d0t]com

--------------------------------------------------------------------------------------------
 2. Changelog
--------------------------------------------------------------------------------------------

See the changelog.txt file.

--------------------------------------------------------------------------------------------
 3. Skinning
--------------------------------------------------------------------------------------------
For future version of Uitzendinggemist.v2 a build that supports WindowXML is required. Such
a version can be found at the *ussual places*. 

For Developers: New skins need to follow these guidelines to function correctly:

* A skinfolder must be placed inside the folder 'skins'
* Uitzendinggemist uses the same folder-name to lookup the skin as the foldername XBMC is 
  using. So the skinfolder for Uitzendinggemist.v2 should have the same name as the folder 
  in which the XBMC-skin is present. E.g. for MC360: the XBMC skin-folder for MC360 is 
  called 'MC360'. So the folder that holds the skin for Uitzendinggemist.v2 should also be 
  called 'MC360' and should be located in the '<scriptfolder of uitzendinggemist>\skins\' 
  folder (which is usually scripts\uitzendinggemist\skins\'.
  If no identically named folder is found. The skin located in the 'Skins\Default' folder 
  is used.
* Inside the skin-folder should at least be a 'Media' and 'PAL' folder. The Media folder 
  holds all the images and the PAL folder the XML for the PAL oriented skins (See XBMC 
  Wiki for more info on skinning-folders).
* The XML files that need to be present are called 'progwindow.xml' and 'channelwindow.xml'. 
* IMPORTANT: Never remove the items which have ID's. These are mandatory for the script. 
  Their appearance can be changed. But they may NEVER be removed. They should keep their ID's. 
* The 'progwindow.xml' holds all the layout for the main window from where the channels
  can be chosen.
* The 'channelwindow.xml' holds all the layout for the episode windows. This is the windows
  from where you can select the episodes.

If you have made a skin, please mail it to me at uitzendinggemist.vx[@t]gmail[d0t]com so 
it can be included in future releases.

--------------------------------------------------------------------------------------------
 4. Known Limitations
--------------------------------------------------------------------------------------------
* Older XBMC builds do not completely support playing of ASF playlist files and streaming 
will fail. Updating to a more recent build of XBMC will solve the problem.
* Not all Kanalenkiezer channels are working. This is a limitation of the www.kanalenkiezer.nl
website. It cannot be fixed. I can override stream-urls. But therefore I need the correct 
URL's for the stream. You can mail them to: uitzendinggemist.vx[@t]gmail[d0t]com with a clear
description of the channel and stream URL.

--------------------------------------------------------------------------------------------
 4.a Some channels are not working? How come?
--------------------------------------------------------------------------------------------
Very often the problem is not the script but the site that is having the problems! So before
you start posting/writing-e-mails/sending-me-logfiles CHECK THE WEBSITES of the channels 
first. Go to www.uitzendinggemist.nl, www.tien.tv, www.rtl.nl, joox.net and/or 
www.pczapper.tv to see if the websites are up and running. If they are not working, neither
will Uitzendinggemist.v2!
If you have verified that the websites are up and running and the script is still not 
working then start posting/writing-e-mails/sending-me-logfiles, but please, always include
the COMPLETE uzg.log logfile so I can see what the problem is.

--------------------------------------------------------------------------------------------
 5. Acknowledgement
--------------------------------------------------------------------------------------------
The first idea for Retrospect/XBMC Online TV/XOT-Uzg came from a script by
by BaKMaN (http://xbox.readrss.com).

I would like to thank Ian Parker from Evanescent Light Photography 
(http://parkerlab.bio.uci.edu/evlight.htm) for allowing me to use one of his pictures as 
the channel background in the Confluece skin.  
