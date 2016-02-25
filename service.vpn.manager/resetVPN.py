#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2016 Zomboided
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
#    This module validates a resets all VPN connections from the VPN
#    Manager for OpenVPN addon settings page.

import xbmcgui
import xbmcaddon
import xbmcvfs
from libs.common import resetVPNConfig, updateService, stopVPNConnection, setVPNLastConnectedProfile, setVPNLastConnectedProfileFriendly
from libs.common import getAddonPath, getVPNLocation, getIconPath
from libs.utility import debugTrace, errorTrace, infoTrace
from libs.vpnproviders import cleanPassFiles, removeGeneratedFiles


debugTrace("-- Entered resetVPN.py --")

# Get info about the addon that this script is pretending to be attached to
addon = xbmcaddon.Addon("service.vpn.manager")
addon_name = addon.getAddonInfo("name")


# Reset the VPN connection values stored in the settings.xml
if xbmcgui.Dialog().yesno(addon_name, "Updating the VPN settings will reset all VPN connections.\nConnections must be re-validated before use.\nContinue with reset?"):
    infoTrace("resetVPN.py", "Resetting all validated VPN settings and disconnected existing VPN connections")
    resetVPNConfig(addon)
    # Remove any last connect settings
    setVPNLastConnectedProfile("")
    setVPNLastConnectedProfileFriendly("")
        
    # Removal any password files that were created (they'll get recreated if needed)
    debugTrace("Deleting all pass.txt files")
    cleanPassFiles()
    
    # No need to stop/start monitor, just need to let it know that things have changed.
    # Because this is a reset of the VPN, the monitor should just work out it has no good connections
    updateService()
    debugTrace("Stopping any active VPN connections")
    stopVPNConnection()
    xbmcgui.Dialog().notification(addon_name, "Disconnected", getIconPath()+"disconnected.png", 5000, False)

xbmc.executebuiltin("Addon.OpenSettings(service.vpn.manager)")    

debugTrace("-- Exit resetVPN.py --")    