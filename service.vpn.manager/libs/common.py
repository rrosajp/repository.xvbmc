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
#    Shared code fragments used by the VPN Manager for OpenVPN add-on.

import xbmcaddon
import xbmcvfs
import xbmc
import os
import re
import urllib2
import xbmcgui
import xbmc
import glob
from libs.platform import getVPNLogFilePath, fakeConnection, isVPNTaskRunning, stopVPN, startVPN, getAddonPath
from libs.platform import getVPNConnectionStatus, connection_status, getPlatform, platforms, writeVPNLog, checkVPNInstall
from libs.utility import debugTrace, infoTrace, errorTrace
from libs.vpnproviders import getVPNLocation, getRegexPattern, getProfileList, provider_display
from libs.vpnproviders import ovpnFilesAvailable, fixOVPNFiles, getLocationFiles, removeGeneratedFiles
       

def getIconPath():
    return getAddonPath(True, "/resources/")    
    

def getFilteredProfileList(ovpn_connections, filter):
    # Filter out the profiles that we're not using
    if "TCP" in filter:
        filterTCP = "(TCP"
    else:
        filterTCP = "()"
    if "UDP" in filter:
        filterUDP = "(UDP"
    else:
        filterUDP = "()"

    connections = []
    for connection in ovpn_connections:
        if filterTCP in connection or filterUDP in connection:
            connections.append(connection)        
    return connections

    
def getFriendlyProfileList(vpn_provider, ovpn_connections):
    # Munge a ovpn full path name is something more friendly
    
    connections = []
    regex_str = getRegexPattern(vpn_provider)
    # Deal with some Windows nonsense
    if getPlatform() == platforms.WINDOWS:
        regex_str = regex_str.replace(r"/", r"\\")
    # Produce a compiled pattern and interate around the list of connections
    pattern = re.compile(regex_str)
    for connection in ovpn_connections:
        connections.append(pattern.search(connection).group(1))        
    return connections
    

def getFriendlyProfileName(vpn_provider, ovpn_connection):
    # Make the VPN profile names more readable to the user to select from
    regex_str = getRegexPattern(vpn_provider)
    # Deal with some Windows nonsense
    if getPlatform() == platforms.WINDOWS:
        regex_str = regex_str.replace(r"/", r"\\")
    # Return friendly version of string
    match = re.search(regex_str, ovpn_connection)
    return match.group(1)
    

def getIPInfo():
    # Based this code on a routine in the VPN for OPENELEC plugin
    # Generate request to find out where this IP is based
    # Return either the IP, the country or both
    try:
        url = "http://www.iplocation.net/"
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0")
        response = urllib2.urlopen(req)
        link=response.read()    
        response.close()
        # Parse the horrendous reply using a regular expression that I'm not sure I understand fully...
        match = re.compile("<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>").findall(link)
        if len(match) > 0:
            inc = 1
            retvalue = ""
            for ip, region, country, isp in match:
                if inc <2:
                    # Set the return value
                    return ip, country
                inc=inc+1    
        else:
            return "unknown", "unknown location"    
    except:
        return "unknown", "unknown location"

    
def resetVPNConfig(addon):    
    # Reset all of the connection config options
    addon.setSetting("1_vpn_validated", "")
    addon.setSetting("1_vpn_validated_friendly", "")
    addon.setSetting("2_vpn_validated", "")
    addon.setSetting("2_vpn_validated_friendly", "")
    addon.setSetting("3_vpn_validated", "")
    addon.setSetting("3_vpn_validated_friendly", "")
    addon.setSetting("4_vpn_validated", "")
    addon.setSetting("4_vpn_validated_friendly", "")
    addon.setSetting("5_vpn_validated", "")
    addon.setSetting("5_vpn_validated_friendly", "")
    

def connectionValidated(addon):
    if not addon.getSetting("1_vpn_validated") == "": return True
    return False


def stopVPNConnection():
    # Kill the running VPN task and reset the current VPN window properties
    setVPNProfile("")
    setVPNProfileFriendly("")
    debugTrace("Stopping VPN")

    # End any existing openvpn process
    waiting = True
    while waiting:
        # Send the kill command to end the openvpn process
        stopVPN()
    
        # Wait half a second just to make sure the process has time to die
        xbmc.sleep(500)

        # See if the openvpn process is still alive
        waiting = isVPNConnected()
            
    setVPNState("stopped")
    return

    
def startVPNConnection(vpn_profile):  
    # Start the VPN, wait for connection, return the result
    startVPN(vpn_profile)
    debugTrace("Waiting for VPN to connect")
    i = 0
    loop_max = 77
    if fakeConnection(): loop_max = 2
        
    while i <= loop_max:
        xbmc.sleep(2000)
        state = getVPNConnectionStatus()
        if not state == connection_status.UNKNOWN: break
        i = i + 2

    if fakeConnection(): state = connection_status.CONNECTED    
    
    if state == connection_status.CONNECTED:
        setVPNProfile(getVPNRequestedProfile())
        setVPNProfileFriendly(getVPNRequestedProfileFriendly())
        setVPNState("started")
        debugTrace("VPN connection to " + getVPNProfile() + " successful")

    return state
    

def isVPNConnected():
    # Return True if the VPN task is still running, or the VPN connection is still active
    # Return False if the VPN task is no longer running and the connection is not active
    
    # If there's no profile, then we're not connected (or should reconnect...)
    if getVPNProfile() == "" : return False
    
    # Make a call to the platform routine to detect if the VPN task is running
    return isVPNTaskRunning()
    
    
def setVPNLastConnectedProfile(profile_name):
    # Store full profile path name
    xbmcgui.Window(10000).setProperty("VPN_Manager_Last_Profile_Name", profile_name)
    return

    
def getVPNLastConnectedProfile():
    # Return full profile path name
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Last_Profile_Name")

    
def setVPNLastConnectedProfileFriendly(profile_name):
    # Store shortened profile name
    xbmcgui.Window(10000).setProperty("VPN_Manager_Last_Profile_Friendly_Name", profile_name)
    return 
    
    
def getVPNLastConnectedProfileFriendly():
    # Return shortened profile name
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Last_Profile_Friendly_Name")       
    
    
def setVPNRequestedProfile(profile_name):
    # Store full profile path name
    xbmcgui.Window(10000).setProperty("VPN_Manager_Requested_Profile_Name", profile_name)
    return

    
def getVPNRequestedProfile():
    # Return full profile path name
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Requested_Profile_Name")

    
def setVPNRequestedProfileFriendly(profile_name):
    # Store shortened profile name
    xbmcgui.Window(10000).setProperty("VPN_Manager_Requested_Profile_Friendly_Name", profile_name)
    return 
    
    
def getVPNRequestedProfileFriendly():
    # Return shortened profile name
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Requested_Profile_Friendly_Name")    


def setVPNProfile(profile_name):
    # Store full profile path name
    xbmcgui.Window(10000).setProperty("VPN_Manager_Connected_Profile_Name", profile_name)
    return

    
def getVPNProfile():
    # Return full profile path name
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Connected_Profile_Name")

    
def setVPNProfileFriendly(profile_name):
    # Store shortened profile name
    xbmcgui.Window(10000).setProperty("VPN_Manager_Connected_Profile_Friendly_Name", profile_name)
    return 
    
    
def getVPNProfileFriendly():
    # Return shortened profile name
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Connected_Profile_Friendly_Name")    


def setConnectionErrorCount(count):
    # Return the number of times a connection retry has failed
    xbmcgui.Window(10000).setProperty("VPN_Manager_Connection_Errors", str(count))


def getConnectionErrorCount():
    # Return the number of times a connection retry has failed
    err = xbmcgui.Window(10000).getProperty("VPN_Manager_Connection_Errors")
    if err == "": return 0
    return int(xbmcgui.Window(10000).getProperty("VPN_Manager_Connection_Errors"))

    
def setVPNState(state):
	# Store current state - "off" (deliberately), "stopped", "started", "" (at boot) or "unknown" (error)
    xbmcgui.Window(10000).setProperty("VPN_Manager_VPN_State", state)
    return

    
def getVPNState():
	# Store current state
    return xbmcgui.Window(10000).getProperty("VPN_Manager_VPN_State")
    
    
def startService():
    # Routine for config to call to request that service starts.  Can time out if there's no response
    # Check to see if service is not already running (shouldn't be...)
    if not xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Control") == "stopped": return True
    
    debugTrace("Requesting service restarts")
    # Update start property and wait for service to respond or timeout
    xbmcgui.Window(10000).setProperty("VPN_Manager_Service_Control", "start")
    for i in range (0, 30):
        xbmc.sleep(1000)
        if xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Control") == "started": return True
    # No response in 30 seconds, service is probably dead
    errorTrace("common.py", "Couldn't communicate with VPN monitor service, didn't acknowledge a start")
    return False

    
def ackStart():
    # Routine for service to call to acknowledge service has started
    xbmcgui.Window(10000).setProperty("VPN_Manager_Service_Control", "started")

    
def startRequested():
    # Service routine should call this to wait for permission to restart.  
    if xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Control") == "start": return True
    return False

    
def stopService():
    # Routine for config to call to request service stops and waits until that happens
    # Check to see if the service has stopped previously
    if xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Control") == "stopped": return True
    
    debugTrace("Requesting service stops")
    # Update start property and wait for service to respond or timeout
    xbmcgui.Window(10000).setProperty("VPN_Manager_Service_Control", "stop")
    for i in range (0, 30):
        xbmc.sleep(1000)
        if xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Control") == "stopped": return True
    # Haven't had a response in 30 seconds which is badness
    errorTrace("common.py", "Couldn't communicate with VPN monitor service, didn't acknowledge a stop")
    return False

    
def stopRequested():
    # Routine for service to call in order to determine whether to stop
    if xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Control") == "stop": return True
    return False
    
    
def ackStop():    
    # Routine for service to call to acknowledge service has stopped
    xbmcgui.Window(10000).setProperty("VPN_Manager_Service_Control", "stopped")

    
def updateService():
    # Set a windows property to tell the background service to update using the latest config data
    debugTrace("Update service requested")
    xbmcgui.Window(10000).setProperty("VPN_Manager_Service_Update", "update")

    
def ackUpdate():
    # Acknowledge that the update has been received
    xbmcgui.Window(10000).setProperty("VPN_Manager_Service_Update", "updated")
    
    
def updateServiceRequested():
    # Check to see if an update is requred
    return (xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Update") == "update")

    
def requestVPNCycle():
    # Don't know where this was called from so using plugin name to get addon handle
    addon = xbmcaddon.Addon("service.vpn.manager")
    addon_name = addon.getAddonInfo("name")
    
    # Don't cycle if there's nothing been set up to cycle around
    if connectionValidated(addon):
        if addon.getSetting("allow_cycle_disconnect") == "true":
            allow_disconnect = True
        else:
            allow_disconnect = False

        # Preload the cycle variable if this is the first time through
        if getVPNCycle() == "":
            if getVPNProfile() == "":
                setVPNCycle("Disconnect")
            else:
                setVPNCycle(getVPNProfile())
        else:
            # Build the list of profiles to cycle through
            profiles=[]
            found_current = False
            if allow_disconnect or ((not allow_disconnect) and getVPNProfile() == ""):
                profiles.append("Disconnect")
                if getVPNProfile() == "": found_current = True
            i=1
            while i<6:
                next_profile = addon.getSetting(str(i)+"_vpn_validated")
                if not next_profile == "":
                    profiles.append(next_profile)
                    if next_profile == getVPNProfile() : 
                        found_current = True
                i=i+1
            if not found_current:
                profiles.append(getVPNProfile())
                  
            # Work out where in the cycle we are and move to the next one
            current_profile = 0
            for profile in profiles:
                current_profile = current_profile + 1
                if getVPNCycle() == profile:            
                    if current_profile > (len(profiles)-1):
                        setVPNCycle(profiles[0])
                    else:
                        setVPNCycle(profiles[current_profile])
                    break
          
        # Display a notification message
        icon = getIconPath()+"locked.png"
        if getVPNCycle() == "Disconnect":
            if getVPNProfile() == "":
                dialog_message = "Disconnected"
                icon = getIconPath()+"disconnected.png"
            else:
                dialog_message = "Disconnect?"
                icon = getIconPath()+"unlocked.png"
        else:
            if getVPNProfile() == getVPNCycle():
                dialog_message = "Connected to " + getFriendlyProfileName(addon.getSetting("vpn_provider_validated"), getVPNCycle())
                icon = getIconPath()+"connected.png"
            else:
                dialog_message = "Connect to " + getFriendlyProfileName(addon.getSetting("vpn_provider_validated"), getVPNCycle()) + "?"
        
        debugTrace("Cycle request is " + dialog_message)
        xbmcgui.Dialog().notification(addon_name, dialog_message , icon, 3000, False)
    else:
        xbmcgui.Dialog().notification(addon_name, "VPN is not set up and authenticated.", xbmcgui.NOTIFICATION_ERROR, 10000, True)

    
def getVPNCycle():
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Service_Cycle")

    
def setVPNCycle(profile):
    xbmcgui.Window(10000).setProperty("VPN_Manager_Service_Cycle", profile)

    
def clearVPNCycle():
    setVPNCycle("")


def isVPNMonitorRunning():
    if xbmcgui.Window(10000).getProperty("VPN_Manager_Monitor_State") == "Started":
        return True
    else:
        return False
    
    
def setVPNMonitorState(state):
    xbmcgui.Window(10000).setProperty("VPN_Manager_Monitor_State", state)
    
    
def getVPNMonitorState():
    return xbmcgui.Window(10000).getProperty("VPN_Manager_Monitor_State")
    
    
def disconnectVPN():
    # Don't know where this was called from so using plugin name to get addon handle
    addon = xbmcaddon.Addon("service.vpn.manager")
    addon_name = addon.getAddonInfo("name")

    debugTrace("Disconnecting the VPN")
    
    # Show a progress box before executing stop
    progress = xbmcgui.DialogProgress()
    progress_title = "Disconnecting from VPN."
    progress.create(addon_name,progress_title)
    
    # Pause the monitor service
    progress_message = "Pausing VPN monitor."
    progress.update(1, progress_title, progress_message)
    if not stopService():
        progress.close()
        # Display error in an ok dialog, user will need to do something...
        errorTrace("common.py", "VPN monitor service is not running, can't stop VPN")
        xbmcgui.Dialog().ok(progress_title, "Error, Service not running.\nCheck log and re-enable.")
        return
    
    xbmc.sleep(500)
    
    progress_message = "Stopping any active VPN connection."
    progress.update(1, progress_title, progress_message)
    
    oldip = xbmc.getIPAddress()
    # Kill the VPN connection if the user hasn't gotten bored waiting
    if not progress.iscanceled():
        stopVPNConnection()
        newip = xbmc.getIPAddress()
        if fakeConnection(): newip = ""
        xbmc.sleep(500)    
        progress_message = "Disconnected from VPN, restarting VPN monitor"
        setVPNLastConnectedProfile("")
        setVPNLastConnectedProfileFriendly("")
        setVPNState("off")
    else:
        progress_message = "Disconnect cancelled, restarting VPN monitor"
        newip = oldip
        
    # Restart service
    if not startService():
        progress.close()
        errorTrace("common.py", "VPN monitor service is not running, VPN has stopped")
        dialog_message = "Error, Service not running.\nCheck log and re-enable."        
    else:
        # Close out the final progress dialog
        progress.update(100, progress_title, progress_message)
        xbmc.sleep(500)
        progress.close()
    
        # Update screen and display result in an ok dialog
        xbmc.executebuiltin('Container.Refresh')
        ip, country = getIPInfo()
        if not newip == oldip:        
            dialog_message = "Disconnected from VPN.\nNetwork location is " + country + ".\nIP address is " + ip + "."
            infoTrace("common.py", "Disconnected from the VPN")
        else:
            dialog_message = "Connected to a VPN in " + country + ".\nIP address is " + ip + ".\nUsing profile " + getVPNProfileFriendly() + "."
            errorTrace("common.py", "Tried to disconnect, but IP address didn't change")
        
    xbmcgui.Dialog().ok(addon_name, dialog_message)

    
def getCredentialsPath(addon):
    return getAddonPath(True, getVPNLocation(addon.getSetting("vpn_provider"))+"/pass.txt")
    
    
def writeCredentials(addon): 
   
    # Write the credentials file        
    try:
        credentials_path = getCredentialsPath(addon)
        debugTrace("Writing VPN credentials file to " + credentials_path)
        credentials = open(credentials_path,'w')
        credentials.truncate()
        credentials.close()
        credentials = open(credentials_path,'a')
        credentials.write(addon.getSetting("vpn_username")+"\n")
        credentials.write(addon.getSetting("vpn_password")+"\n")
        credentials.close()
    except:
        errorTrace("common.py", "Couldn't create credentials file " + credentials_path)
        return False
    xbmc.sleep(500)
    return True
    

def wizard():
    addon = xbmcaddon.Addon("service.vpn.manager")
    addon_name = addon.getAddonInfo("name")    

    # Indicate the wizard has been run, regardless of if it is to avoid asking again
    #addon.setSetting("vpn_wizard_run", "true")
    
    # Wizard or settings?
    if xbmcgui.Dialog().yesno(addon_name, "No primary VPN connection has been set up.  Would you like to do this using the set up wizard or using the Settings dialog?", "", "", "Settings", "Wizard"):
        
        # Select the VPN provider
        vpn = xbmcgui.Dialog().select("Select your VPN provider.", provider_display)
        vpn_provider = provider_display[vpn]
        
        # Get the username and password
        vpn_username = ""
        vpn_password = ""
        vpn_username = xbmcgui.Dialog().input("Enter your " + vpn_provider + " username.", type=xbmcgui.INPUT_ALPHANUM)
        if not vpn_username == "":
            vpn_password = xbmcgui.Dialog().input("Enter your " + vpn_provider + " password.", type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
        
        # Try and connect if we've gotten all the data
        if not vpn_password == "":
            addon.setSetting("vpn_provider", vpn_provider)
            addon.setSetting("vpn_username", vpn_username)
            addon.setSetting("vpn_password", vpn_password)
            connectVPN("1", vpn_provider)
            # Need to reinitialise addon here for some reason...
            addon = xbmcaddon.Addon("service.vpn.manager")
            if connectionValidated(addon):
                xbmcgui.Dialog().ok(addon_name, "Successfully connected to " + vpn_provider + ".  Use the Settings dialog to add additional VPN connections.  You can also define add-on filters to dynamically change the VPN connection being used.")
            else:
                xbmcgui.Dialog().ok(addon_name, "Could not connect to " + vpn_provider + ".  Use the Settings dialog to correct any issues and try connecting again.")
            
        else:
            xbmcgui.Dialog().ok(addon_name, "You need to enter both a VPN username and password to connect.")

    
def connectVPN(connection_order, vpn_profile):

    # Don't know where this was called from so using plugin name to get addon handle
    addon = xbmcaddon.Addon("service.vpn.manager")
    addon_name = addon.getAddonInfo("name")

    # If we've not arrived here though the addon (because we've used the add-on setting
    # on the option menu), we want to surpress running the wizard as there's no need.
    addon.setSetting("vpn_wizard_run", "true")

    # Check openvpn installed
    if not addon.getSetting("checked_openvpn") == "true":
        if checkVPNInstall(addon): addon.setSetting("checked_openvpn", "true")
        else: return

    
    vpn_protocol = addon.getSetting("vpn_protocol")
    
    # Do some stuff to set up text used in dialog windows
    connection_title = ""
    if connection_order == "0" : connection_title = ""
    if connection_order == "1" : connection_title = " primary"
    if connection_order == "2" : connection_title = " second"
    if connection_order == "3" : connection_title = " third"
    if connection_order == "4" : connection_title = " fourth"
    if connection_order == "5" : connection_title = " fifth"

    # Initialise the state of the connection
    state = ""
    
    # Display a progress dialog box (put this on the screen quickly before doing other stuff)
    progress = xbmcgui.DialogProgress()
    progress_title = "Connecting to" + connection_title + " VPN."
    progress.create(addon_name,progress_title) 

    debugTrace(progress_title)
        
    # Pause the monitor service
    progress_message = "Pausing VPN monitor."
    progress.update(1, progress_title, progress_message)
    if not stopService():
        progress.close()
        # Display error result in an ok dialog
        errorTrace("common.py", "VPN monitor service is not running, can't start VPN")
        xbmcgui.Dialog().ok(progress_title, "Error, Service not running.\nCheck log and re-enable.")
        return

    if not progress.iscanceled():
        progress_message = "VPN monitor paused."
        debugTrace(progress_message)
        progress.update(5, progress_title, progress_message)
        xbmc.sleep(500)
        
    # Stop any active VPN connection
    if not progress.iscanceled():
        progress_message = "Stopping any active VPN connection."    
        progress.update(6, progress_title, progress_message)
        stopVPNConnection()

    if not progress.iscanceled():
        progress_message = "Disconnected from VPN."
        progress.update(10, progress_title, progress_message)
        xbmc.sleep(500)
        
    # Install the VPN provider    
    if not progress.iscanceled():
    
        vpn_provider = addon.getSetting("vpn_provider")
    
        # This is some code to copy the user name from a default file rather than use the user entered values.
        # It exists to help development where swapping between providers constantly is tedious.
        default_path = getAddonPath(True, getVPNLocation(vpn_provider) + "/DEFAULT.txt")
        if connection_order == "1" and xbmcvfs.exists(default_path):
            default_file = open(default_path, 'r')
            default = default_file.readlines()
            default_file.close()
            default_value = default[0].strip(' \t\n\r')
            addon.setSetting("vpn_username", default_value)
            default_value = default[1].strip(' \t\n\r')
            addon.setSetting("vpn_password", default_value)  

        vpn_username = addon.getSetting("vpn_username")
        vpn_password = addon.getSetting("vpn_password")
        
        # Reset the setting indicating we've a good configuration for just this connection
        addon.setSetting(connection_order + "_vpn_validated", "")
        addon.setSetting(connection_order + "_vpn_validated_friendly", "")
        last_provider = addon.getSetting("vpn_provider_validated")
        last_credentials = addon.getSetting("vpn_username_validated") + " " + addon.getSetting("vpn_password_validated")
        if last_provider == "" : last_provider = "?"
        
        # Provider or credentials we've used previously have changed so we need to reset all validated connections
        vpn_credentials = vpn_username + " " + vpn_password
        if not last_provider == vpn_provider:
            last_credentials = "?"
        if not last_credentials == vpn_credentials:
            debugTrace("Credentials have changed since last time through so need to revalidate")
            resetVPNConfig(addon)   
    
    # Generate or fix the OVPN files if we've not done this previously
    provider_gen = True
    if not progress.iscanceled():
        if not ovpnFilesAvailable(getVPNLocation(vpn_provider)):

            # Fetch the list of locations available.  If there are multiple, the user can select
            locations = getLocationFiles(getVPNLocation(vpn_provider))            
            i = 0
            for location in locations:
                locations[i] = location[location.index("LOCATIONS")+10:location.index(".txt")]
                i = i + 1
            selected_profile = ""
            if len(locations) == 0: errorTrace("common.py", "No LOCATIONS.txt files found in VPN directory.  Cannot generate ovpn files.")
            if len(locations) > 1:
                selected_location = xbmcgui.Dialog().select("Select connections profile", locations)
                selected_profile = locations[selected_location]
            
            addon.setSetting("vpn_locations_list", selected_profile)
            progress_message = "Setting up VPN provider " + vpn_provider + "."
            progress.update(11, progress_title, progress_message)
            # Delete any old files in other directories
            debugTrace("Deleting all generated ovpn files")
            removeGeneratedFiles()
            # Generate new ones
            provider_gen = fixOVPNFiles(getVPNLocation(vpn_provider), selected_profile)        
            xbmc.sleep(500)

    if provider_gen:
        if not progress.iscanceled():
            progress_message = "Using VPN provider " + vpn_provider
            progress.update(15, progress_title, progress_message)
            xbmc.sleep(500)
                            
        # Set up user credentials file
        if not progress.iscanceled():
            credentials_path = getCredentialsPath(addon)
            debugTrace("Attempting to use the credentials in " + credentials_path)
            if (not last_credentials == vpn_credentials) or (not xbmcvfs.exists(credentials_path)) or (not connectionValidated(addon)):
                progress_message = "Configuring authentication settings for user " + vpn_username + "."
                progress.update(16, progress_title, progress_message)
                provider_gen = writeCredentials(addon)

    if provider_gen:            
        if not progress.iscanceled():
            progress_message = "Using authentication settings for user " + vpn_username + "."
            progress.update(19, progress_title, progress_message)
            xbmc.sleep(500)

        # Display the list of connections
        if not progress.iscanceled():

            if not connection_order == "0":
                debugTrace("Displaying list of connections")
                all_connections = getProfileList(vpn_provider)
                ovpn_connections = getFilteredProfileList(all_connections, vpn_protocol)
                connections = getFriendlyProfileList(vpn_provider, ovpn_connections)
                
                if len(connections) > 0:
                    selected_connection = xbmcgui.Dialog().select("Select " + connection_title + " VPN profile", connections)                  
                
                    # Based on the value selected, get the path name to the ovpn file
                    ovpn_name = connections[selected_connection]
                    ovpn_connection = ovpn_connections[selected_connection]
                else:
                    ovpn_name = ""
            else:
                ovpn_name = getFriendlyProfileName(vpn_provider, vpn_profile)
                ovpn_connection = vpn_profile

        # Try and connect to the VPN provider using the entered credentials        
        if not progress.iscanceled() and not ovpn_name == "":    
            progress_message = "Connecting using profile " + ovpn_name + "."
            debugTrace(progress_message)
            oldip = xbmc.getIPAddress()
            
            # Start the connection and wait a second before starting to check the state
            startVPN(ovpn_connection)
            
            i = 0
            # Bad network takes over a minute to spot so loop for a bit longer (each loop is 2 seconds)
            loop_max = 38
            if fakeConnection(): loop_max = 2
            percent = 20
            while i <= loop_max:
                progress.update(percent, progress_title, progress_message)
                xbmc.sleep(2000)
                state = getVPNConnectionStatus()
                if not (state == connection_status.UNKNOWN or state == connection_status.TIMEOUT) : break
                if progress.iscanceled(): break
                i = i + 1
                percent = percent + 2

    # Mess with the old IP to make it look as if we've connected to a VPN
    if fakeConnection() and not progress.iscanceled() and provider_gen and not ovpn_name == "" : state = connection_status.CONNECTED
    #state = connection_status.TIMEOUT
    
    # Determine what happened during the connection attempt        
    if state == connection_status.CONNECTED :
        # Success, VPN connected! Display an updated progress window whilst we work out where we're connected to
        progress_message = "Connected, restarting VPN monitor."
        progress.update(97, progress_title, progress_message)
        # Set the final message to indicate success
        progress_message = "Connected, VPN monitor restarted."
        ip, country = getIPInfo()
        dialog_message = "Connected to a VPN in " + country + ".\nIP address is " + ip + ".\nUsing profile " + ovpn_name  + "."
        infoTrace("common.py", dialog_message)
        # Store that setup has been validated and the credentials used
        setVPNProfile(ovpn_connection)
        setVPNProfileFriendly(ovpn_name)
        if not connection_order == "0":
            addon.setSetting("vpn_provider_validated", vpn_provider)
            addon.setSetting("vpn_username_validated", vpn_username)
            addon.setSetting("vpn_password_validated", vpn_password)
            addon.setSetting("vpn_connection_validated", "")
        addon.setSetting(connection_order + "_vpn_validated", ovpn_connection)
        addon.setSetting(connection_order + "_vpn_validated_friendly", ovpn_name)
        setVPNState("started")
        setVPNRequestedProfile("")
        setVPNRequestedProfileFriendly("")
        setVPNLastConnectedProfile("")
        setVPNLastConnectedProfileFriendly("")
        setConnectionErrorCount(0)
        # Indicate to the service that it should update its settings
        updateService()
    elif progress.iscanceled() :
        # User pressed cancel.  Don't change any of the settings as we've no idea how far we got
        # down the path of installing the VPN, configuring the credentials or selecting the connection
        # We're assuming here that if the VPN or user ID has been changed, then the connections are invalid
        # already.  If the cancel happens during the connection validation, we can just use the existing one.
        # Set the final message to indicate user cancelled operation
        progress_message = "Cancelling connection attempt, restarting VPN monitor."
        progress.update(97, progress_title, progress_message)
        # Set the final message to indicate cancellation
        progress_message = "Cancelling connection attempt, VPN monitor restarted."
        if connection_order == "0" :
            dialog_message = "Cancelled connection attempt."
        else :
            dialog_message = "Cancelled connection attempt, existing settings will be used."
    else :
        # An error occurred, The current connection is already invalidated.  The VPN credentials might 
        # be ok, but if they need re-entering, the user must update them which will force a reset.  
        progress_message = "Error connecting to VPN, restarting VPN monitor."
        progress.update(97, progress_title, progress_message)
        xbmc.sleep(500)
        # Set the final message to show an error occurred
        progress_message = "Error connecting to VPN, VPN monitor restarted."
        if not provider_gen:
            dialog_message = "Error creating OVPN or credentials file for provider\nCheck log to determine cause of failure."
        elif ovpn_name == "":
            dialog_message = "No VPN profiles were available for " + vpn_protocol + " protocol.\nChange VPN provider settings."
        elif state == connection_status.AUTH_FAILED: 
            dialog_message = "Error connecting to VPN, authentication failed.\nCheck your username and password."
            credentials_path = getCredentialsPath(addon)
            resetVPNConfig(addon)
            addon.setSetting("vpn_username_validated", "")
            addon.setSetting("vpn_password_validated", "")
        elif state == connection_status.NETWORK_FAILED: 
            dialog_message = "Error connecting to VPN, could not estabilish connection.\nCheck your network connectivity and retry."
        elif state == connection_status.TIMEOUT:
            dialog_message = "Error connecting to VPN, connection has timed out.\nTry using a different VPN profile or retry."
        else:
            dialog_message = "Error connecting to VPN, something bad happened.\nCheck log or retry."
        errorTrace("common.py", dialog_message)
        
        # Output what when wrong with the VPN to the log
        writeVPNLog()
        
        # The VPN might be having a spaz still so we want to ensure it's stopped
        stopVPN()

    # Restart service
    if not startService():
        progress.close()
        errorTrace("common.py", "VPN monitor service is not running, VPN has started")
        dialog_message = "Error, Service not running.\nCheck log and re-enable."        
    else:
        # Close out the final progress dialog
        progress.update(100, progress_title, progress_message)
        xbmc.sleep(500)
        progress.close()
    
    # Refresh the screen if this is not being done on settings screen
    if connection_order == "0" : xbmc.executebuiltin('Container.Refresh')
    
    # Display connection result in an ok dialog
    xbmcgui.Dialog().ok(progress_title, dialog_message)
  