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
#    Platform specific calls used by VPN Manager for OpenVPN add-on.

import os
import sys
import xbmc
import xbmcgui
import xbmcvfs
import xbmcaddon
from libs.utility import debugTrace, errorTrace, infoTrace, enum
from sys import platform


# **** ADD MORE PLATFORMS HERE ****
platforms = enum(UNKNOWN=0, WINDOWS=1, LINUX=2, RPI=3, ANDROID=4, MAC=5)  

use_sudo = False


def fakeConnection():
    # Return True to fake out any calls to openVPN to change the network
    if getPlatform() == platforms.WINDOWS: return True
    return False

    
def getPlatform():
    # Work out which platform is being used.
    if sys.platform == "win32" : return platforms.WINDOWS
    if sys.platform == "linux" or sys.platform == "linux2":
        if getAddonPath(True, "").startswith("/storage/.kodi/"):
            # Pi/OpenELEC doesn't use a user directory to store kodi things
            return platforms.RPI
        else:
            # Other Linux installs do use a user directory...
            return platforms.LINUX
    # **** ADD MORE PLATFORMS HERE ****
    #if sys.platform == "?": return platforms.ANDROID
    #if sys.platform == "darwin": return platforms.MAC
    return platforms.UNKNOWN    
        
    
def getVPNLogFilePath():
    # Return the full filename for the VPN log file
    p = getPlatform()
    if p == platforms.LINUX or p == platforms.RPI:
        return "/run/openvpn.log"
    # **** ADD MORE PLATFORMS HERE ****
    return ""
    

def stopVPN():
    # Stop the platform VPN task.
    if not fakeConnection():
        p = getPlatform()
        if p == platforms.LINUX or p == platforms.RPI:
            command="killall -9 openvpn"            
            #if p == platforms.LINUX and use_sudo : command = "sudo " + command
            debugTrace("Stopping VPN with " + command)
            os.system(command)
        # **** ADD MORE PLATFORMS HERE ****
    return
        
    
def startVPN(vpn_profile):
    # Call the platform VPN to start the VPN
    if not fakeConnection():
        p = getPlatform()
        if p == platforms.RPI:
            command=getAddonPath(False, "network.openvpn/bin/openvpn \"" + vpn_profile + "\" > " + getVPNLogFilePath() + " &")            
            debugTrace("Starting VPN with " + command)
            os.system(command)
        if p == platforms.LINUX:            
            command="/usr/sbin/openvpn \"" + vpn_profile + "\" > " + getVPNLogFilePath() + " &"
            #if use_sudo: command = "sudo " + command
            debugTrace("Starting VPN with " + command)
            os.system(command)
        # **** ADD MORE PLATFORMS HERE ****
    return

    
def checkVPNInstall(addon):
    # Check that openvpn is available otherwise generate an error message
    if not fakeConnection():
        p = getPlatform()
        dialog_msg = ""
        p=platforms.RPI
        if p == platforms.RPI:
            command_path = getAddonPath(False, "network.openvpn/bin/openvpn")
            if xbmcvfs.exists(command_path):
                # Check the version that's installed
                vpn_addon = xbmcaddon.Addon("network.openvpn")
                version =  vpn_addon.getAddonInfo("version")
                version = version.replace(".", "")
                if int(version) >= 601: return True
            dialog_msg = "OpenVPN executable not available.  Install the openvpn plugin, version 6.0.1 or greater from the OpenELEC unofficial repo."
        if p == platforms.LINUX:
            return True
        
        # **** ADD MORE PLATFORMS HERE ****

        # Display error message
        xbmcgui.Dialog().ok(addon.getAddonInfo("name"), dialog_msg)
        return False        
    else: return True
    
    return True

    
def isVPNTaskRunning():
    # Return True if the VPN task is still running, or the VPN connection is still active
    # Return False if the VPN task is no longer running and the connection is not active
    
    if fakeConnection(): return True
    
    p = getPlatform()
    if p == platforms.LINUX or p == platforms.RPI:
        try:
            command = "pidof openvpn"
            #if p == platforms.LINUX and use_sudo: command = "sudo " + command
            pid = os.system(command)
            # This horrible call returns 0 if it finds a process, it's not returning the PID number
            if pid == 0 : return True
            return False
        except:
            return False
    # **** ADD MORE PLATFORMS HERE ****
    return False


connection_status = enum(UNKNOWN=0, CONNECTED=1, AUTH_FAILED=2, NETWORK_FAILED=3, TIMEOUT=4, ERROR=5) 
    
def getVPNConnectionStatus():
    # Open the openvpn output file and parse it for known phrases
    # Return 'connected', 'auth failed', 'network failed', 'error' or ''

    if fakeConnection(): return connection_status.UNKNOWN

    # **** ADD MORE PLATFORMS HERE ****
    # Might not need to mess with this too much if the log output from openvpn is the same
    p = getPlatform()
    if p == platforms.LINUX or p == platforms.RPI:
        path = getVPNLogFilePath()
        state = connection_status.UNKNOWN
        if xbmcvfs.exists(path):
            debugTrace("Reading log file")
            log = open(path,'r')
            lines = log.readlines()
            for line in lines:
                if "Initialization Sequence Completed" in line:
                    state = connection_status.CONNECTED
                    break
                if "AUTH_FAILED" in line:
                    state = connection_status.AUTH_FAILED
                if "TLS Error" in line:
                    state = connection_status.NETWORK_FAILED
                if "Connection timed out" in line:
                    state = connection_status.TIMEOUT
            log.close()
            # Haven't found what's expected so return an empty stream
            if not state == connection_status.UNKNOWN: debugTrace("VPN connection status is " + str(state))
            return state
        else:
            errorTrace("platform.py", "Tried to get VPN connection status but log file didn't exist")
            return connection_status.ERROR

            
def writeVPNLog():
    # Write the openvpn output log to the error file
    try:
        error_file = open(getVPNLogFilePath(), 'r')
        error_output = error_file.readlines()
        error_file.close()
        errorTrace("platform.py", "VPN log file start >>>")
        for line in error_output:
            print line
        errorTrace("platform.py", "<<< VPN log file end")
    except:
        errorTrace("platform.py", "Couldn't write VPN error log")
                
                
def useSudo(option):
    # True or False...
    use_sudo = option

    
def getAddonPath(this_addon, path):
    # Return the URL of the addon directory, plus any addition path/file name.
    if this_addon:
        return xbmc.translatePath("special://home/addons/service.vpn.manager/" + path)
    else:
        return xbmc.translatePath("special://home/addons/" + path)
