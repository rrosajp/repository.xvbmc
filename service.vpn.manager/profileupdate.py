#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2016 Zomboided
#
#    Connection script called by the VPN Manager for OpenVPN settings screen
#    to validate a connection to a VPN provider.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    This module will update the VPN profiles to point to the directory
#    in which the VPN Manager for OpenVPN plugin is installed.  It's only
#    called from the settings menu but shouldn't be needed as it's all
#    done during the connection change logic

import xbmcaddon
import xbmcgui
from libs.vpnproviders import removeGeneratedFiles, cleanPassFiles
from libs.utility import debugTrace, errorTrace, infoTrace
#from libs.generation import generateAll

addon = xbmcaddon.Addon("service.vpn.manager")
addon_name = addon.getAddonInfo("name")

debugTrace("-- Entered profileupdate.py --")

if xbmcgui.Dialog().yesno(addon_name, "Connections should be re-validated before use.\nAlso consider defaulting other settings.\nContinue with reset?"):

    # Only used during development to create location files
    #generateAll()

    debugTrace("Deleting all pass.txt files")
    cleanPassFiles()
        
    debugTrace("Deleting all generated ovpn files")
    removeGeneratedFiles()

xbmc.executebuiltin("Addon.OpenSettings(service.vpn.manager)")    
    
debugTrace("-- Exit profileupdate.py --")
