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
#    VPN provider code used by the VPN Manager for OpenVPN add-on.

import xbmc
import xbmcgui
import xbmcvfs
import xbmcaddon
import glob
from libs.utility import debugTrace, errorTrace, infoTrace
from libs.platform import getAddonPath, fakeConnection


# **** ADD MORE VPN PROVIDERS HERE ****
# Directory names for each of the providers (in the root of the addon)
providers = ["PIA", "IPVanish", "VyprVPN", "ibVPN", "NordVPN", "tigerVPN", "HMA", "PureVPN", "LiquidVPN", "AirVPN", "CyberGhost", "Ivacy"]

# **** ADD MORE VPN PROVIDERS HERE ****
# Display names for each of the providers (matching the guff in setup.xml)
# Must be in the same order as the provider directory name above
provider_display = ["Private Internet Access", "IPVanish", "VyperVPN", "Invisible Browsing VPN", "NordVPN", "tigerVPN", "Hide My Ass", "PureVPN", "LiquidVPN", "AirVPN", "CyberGhost", "Ivacy"]

# **** ADD VPN PROVIDERS HERE IF THEY USE A KEY ****
providers_with_keys = ["CyberGhost"]
    
        
def getAddonPathWrapper(path):
    # This function resets the VPN profiles to the standard VPN Manager install
    # location as per OpenELEC, or to the platform install location
    force_default_install = fakeConnection()    
    if force_default_install:
        return "/storage/.kodi/addons/service.vpn.manager/" + path        
    else:
        return getAddonPath(True, path)


def getVPNLocation(vpn_provider):
    # This function translates between the display name and the directory name
    i=0
    for provider in provider_display:
        if vpn_provider == provider: return providers[i]
        if vpn_provider == providers[i]: return providers[i]
        i = i + 1
    return ""


def getProfileList(vpn_provider):
    # Return the list of ovpn files for a given provider (aka directory name...)
    path = getAddonPath(True, getVPNLocation(vpn_provider)+"/*.ovpn")
    debugTrace("Getting list of profiles in " + path)
    # Get the list of connection profiles and another list of strings to abuse for the selection screen
    return sorted(glob.glob(path))  


def usesUserKey(vpn_provider):
    if vpn_provider in providers_with_keys: return True
    return False

    
def getRegexPattern(vpn_provider):
    # Return a regex expression to make a file name look good.  Not using 
    # the input variable as all of the profiles are generated with good names
    return r'(?s).*/(.*).ovpn'

    
def cleanPassFiles():
    # Delete the pass.txt file from all of the VPN provider directorys
    for provider in providers:
        filename = getAddonPath(True, provider + "/pass.txt")
        if xbmcvfs.exists(filename) : xbmcvfs.delete(filename)   


def cleanGeneratedFiles():
    # Delete the GENERATED.txt file from all of the VPN provider directorys    
    for provider in providers:
        filename = getAddonPath(True, provider + "/GENERATED.txt")
        if xbmcvfs.exists(filename) : xbmcvfs.delete(filename)         


def removeGeneratedFiles():
    for provider in providers:
        if ovpnGenerated(provider):
            ovpn_connections = getProfileList(provider)    
            for connection in ovpn_connections:
                xbmcvfs.delete(connection)
        filename = getAddonPath(True, provider + "/GENERATED.txt")
        if xbmcvfs.exists(filename) : xbmcvfs.delete(filename)             

        
def ovpnFilesAvailable(vpn_provider):
    if xbmcvfs.exists(getAddonPath(True, vpn_provider + "/GENERATED.txt")): return True
    return False

    
def ovpnGenerated(vpn_provider):
    if xbmcvfs.exists(getAddonPath(True, vpn_provider + "/TEMPLATE.txt")): return True
    return False

    
def getLocationFiles(vpn_provider):
    return glob.glob(getAddonPath(True, vpn_provider + "/LOCATIONS*.txt"))
    

def fixOVPNFiles(vpn_provider, alternative_locations_name):
    # Generate or update the VPN files
    if ovpnGenerated(vpn_provider):
        return generateOVPNFiles(vpn_provider, alternative_locations_name)
    else:
        return updateVPNFiles(vpn_provider)
    
    
def generateOVPNFiles(vpn_provider, alternative_locations_name):
    # Generate the OVPN files for a VPN provider using the template and update with location info
    
    infoTrace("vpnproviders.py", "Generating OVPN files for " + vpn_provider + " using list " + alternative_locations_name)

    # See if there's a port override going on
    addon = xbmcaddon.Addon("service.vpn.manager")
    if addon.getSetting("default_udp") == "true":
        portUDP = ""
    else:
        portUDP = addon.getSetting("alternative_udp_port")
        
    if addon.getSetting("default_tcp") == "true":
        portTCP = ""
    else:
        portTCP = addon.getSetting("alternative_tcp_port")
        
    # Load ovpn template
    try:
        debugTrace("Opening template file for " + vpn_provider)
        template_file = open(getAddonPath(True, vpn_provider + "/TEMPLATE.txt"), 'r')
        debugTrace("Opened template file for " + vpn_provider)
        template = template_file.readlines()
        template_file.close()
    except:
        errorTrace("vpnproviders.py", "Couldn't open the template file for " + vpn_provider)
        return False
    
    # Load locations file
    if not alternative_locations_name == "":
        locations_name = getAddonPath(True, vpn_provider + "/LOCATIONS " + alternative_locations_name + ".txt")
    else:
        locations_name = getAddonPath(True, vpn_provider + "/LOCATIONS.txt")

    print locations_name    
        
    try:
        debugTrace("Opening locations file for " + vpn_provider + "/n" + locations_name)
        locations_file = open(locations_name, 'r')
        debugTrace("Opened locations file for " + vpn_provider)
        locations = locations_file.readlines()
        locations_file.close()
    except:
        errorTrace("vpnproviders.py", "Couldn't open the locations file for " + vpn_provider + "\n" + locations_name)
        return False

    # For each location, generate an OVPN file using the template
    for location in locations:
        try:
            location_values = location.split(",")
            geo = location_values[0]
            servers = location_values[1].split()
            proto = location_values[2]
            ports = (location_values[3].strip(' \t\n\r')).split()
            port = ""

            # Initialise the set of values that can be modified by the location file tuples
            ca_cert = "ca.crt"
            ta_key = "ta.key"
            user_key = "client.key"
            user_cert = "client.crt"
            remove_flags = ""
            
            if len(location_values) > 4: 
                # The final location value is a list of multiple x=y declarations.  These need
                # to be parsed out and modified.  Right now only ca.crt is supported...
                modifier_tuples = (location_values[4].strip(' \t\n\r')).split()
                # Loop through all of the values splitting them into x and y
                for modifier in modifier_tuples:
                    pair = modifier.split("=")
                    if "#CERT" in pair[0]: ca_cert = pair[1].strip()
                    if "#REMOVE" in pair[0]: remove_flags = pair[1].strip()
                    if "#TLSKEY" in pair[0]: ta_key = pair[1].strip()
                    if "#USERKEY" in pair[0]: user_key = pair[1].strip()
                    if "#USERCERT" in pair[0]: user_cert = pair[1].strip()
            if proto == "udp" and not portUDP == "": port = portUDP
            if proto == "tcp" and not portTCP == "": port = portTCP
            if port == "" and len(ports) == 1: port = ports[0]
        except:
            errorTrace("vpnproviders.py", "Location file for " + vpn_provider + " invalid on line\n" + location)
            return False
            
        try:
            ovpn_file = open(getAddonPath(True, vpn_provider + "/" + geo + ".ovpn"), 'w')
            if proto == "tcp":
                servprot = "tcp-client"
            else:
                servprot = proto

            # Do a replace on the tags in the template with data from the location file
            for line in template:
                output_line = line.strip(' \t\n\r')
                # Must check to see if there's a remove tag on the line before looking for other tags
                if "#REMOVE" in output_line:
                    if output_line[output_line.index("#REMOVE")+7] in remove_flags:
                        # Remove the line if it's a flag this location doesn't care about
                        output_line = ""
                    else:
                        # Delete the tag if this location doesn't want this line removed
                        output_line = output_line.replace("#REMOVE" + output_line[output_line.index("#REMOVE")+7], "")
                output_line = output_line.replace("#PROTO", proto)
                output_line = output_line.replace("#SERVPROT", servprot)
                # If there are multiple servers then we'll need to duplicate the server
                # line (which starts with 'remote ') and fix the server.  The rest of the
                # code will deal with the port which is the same for all lines (although
                # this assumption might not be true for all VPN providers...)
                if output_line.startswith("remote "):
                    server_template = output_line
                    server_lines = ""
                    i = 0
                    for server in servers:
                        if not server_lines == "" : server_lines = server_lines + "\n"
                        server_lines = server_lines + server_template.replace("#SERVER", server)
                        if port == "":
                            server_lines = server_lines.replace("#PORT", ports[i])
                        i = i + 1
                    output_line = server_lines
                # There might be other places we use server and port, so still the do the replace
                output_line = output_line.replace("#SERVER", servers[0])
                output_line = output_line.replace("#PORT", port)
                output_line = output_line.replace("#PASS", getAddonPathWrapper(vpn_provider + "/" + "pass.txt"))
                output_line = output_line.replace("#CERT", getAddonPathWrapper(vpn_provider + "/" + ca_cert))
                output_line = output_line.replace("#TLSKEY", getAddonPathWrapper(vpn_provider + "/" + ta_key))
                output_line = output_line.replace("#CRLVERIFY", getAddonPathWrapper(vpn_provider + "/" + "crl.pem"))
                output_line = output_line.replace("#USERKEY", getAddonPathWrapper(vpn_provider + "/" + user_key))
                output_line = output_line.replace("#USERCERT", getAddonPathWrapper(vpn_provider + "/" + user_cert))
                # This is a little hack to remove a tag that doesn't work with TCP but is needed for UDP
                # Could do this with a #REMOVE, but doing it here is less error prone.
                if "explicit-exit-notify" in line and proto == "tcp": output_line = ""
                if not output_line == "" : ovpn_file.write(output_line + "\n")
            ovpn_file.close()
            debugTrace("Wrote location " + geo + " " + proto)
        except:
            errorTrace("vpnproviders.py", "Can't write a location file for " + vpn_provider + " failed on line\n" + location)
            return False
    
    # Write a file to indicate successful generation of the ovpn files
    ovpn_file = open(getAddonPath(True, vpn_provider + "/GENERATED.txt"), 'w')
    ovpn_file.close()
    
    return True

    
def updateVPNFiles(vpn_provider):
    # If the OVPN files aren't generated then they need to be updated with location info    
    
    infoTrace("profileupdate.py", "Updating VPN profiles for " + vpn_provider)
    # Get the list of VPN profile files        
    ovpn_connections = getProfileList(vpn_provider)

    # See if there's a port override going on
    addon = xbmcaddon.Addon("service.vpn.manager")
    if addon.getSetting("default_udp") == "true":
        portUDP = ""
    else:
        portUDP = addon.getSetting("alternative_udp_port")
        
    if addon.getSetting("default_tcp") == "true":
        portTCP = ""
    else:
        portTCP = addon.getSetting("alternative_tcp_port")
    
    for connection in ovpn_connections:
        try:
            f = open(connection, 'r+')
            debugTrace("Processing file " + connection)
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            # Update the necessary values in the ovpn file
            for line in lines:
                
                if "auth-user-pass" in line:
                    line = "auth-user-pass " + getAddonPathWrapper(vpn_provider + "/" + "pass.txt\n")

                if "remote " in line:
                    port = ""
                    for newline in lines:
                        if "proto " in newline:
                            if "tcp" in newline and not portTCP == "": port = portTCP
                            if "udp" in newline and not portUDP == "": port = portUDP
                    if not port == "":
                        tokens = line.split()
                        line = "remote " + tokens[1] + " " + port + "\n"
                           
                f.write(line)
            f.close()
        except:
            errorTrace("profileupdate.py", "Failed to update ovpn file")
            return False

    # Write a file to indicate successful update of the ovpn files
    ovpn_file = open(getAddonPath(True, vpn_provider + "/GENERATED.txt"), 'w')
    ovpn_file.close()
            
    return True    
    