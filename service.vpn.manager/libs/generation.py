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
#    Generate the template and location files based on whatever info 
#    available.  Minimal error coding as it's only to run once (infrequently)
#    and not by the end user.


import xbmc
import xbmcgui
import xbmcvfs
import glob
from libs.utility import debugTrace, errorTrace, infoTrace
from libs.platform import getAddonPath, fakeConnection
from libs.common import getFriendlyProfileName

def generateAll():
    infoTrace("generation.py", "Generating Location files")
    generateIvacy()
    return
    generatePureVPN()
    generateLiquidVPN()
    generatetigerVPN()
    generateHMA()    
    generateVyprVPN()
    generateIPVanish()
    generatePIA()
    generateibVPN()
    generateNordVPN()
    

def getLocations(vpn_provider, path_ext):
    if path_ext == "":
        location_path = "/LOCATIONS.txt"
    else:
        location_path = "/LOCATIONS " + path_ext + ".txt"
    return open(getAddonPath(True, vpn_provider + location_path), 'w')


def getProfileList(vpn_provider):
    path = getAddonPath(True, "providers/" + vpn_provider + "/*.ovpn")
    return glob.glob(path)  


def generateIvacy():
    # Data is stored in a flat text file
    # Location, City, ignore, TCP server, UDP server
    location_file = getLocations("Ivacy", "")
    source_file = open(getAddonPath(True, "providers/Ivacy/Servers.txt"), 'r')
    source = source_file.readlines()
    source_file.close()
    for line in source:
        tokens = line.split("\t")        
        for t in tokens:
            if "-tcp" in t:                
                server = t.strip(' \t\n\r')
                geo = tokens[0].strip(' \t\n\r') 
                #+ " - " + tokens[1].strip(' \t\n\r')
                output_line = geo + " (TCP)," + server + "," + "tcp,80,#REMOVE=1" + "\n"
                location_file.write(output_line)
            if "-udp" in t:                
                server = t.strip(' \t\n\r')
                geo = tokens[0].strip(' \t\n\r')
                #+ " - " + tokens[1].strip(' \t\n\r')
                output_line = geo + " (UDP)," + server + "," + "udp,53,#REMOVE=2" + "\n"
                location_file.write(output_line)
    location_file.close()    
    
    
def generateLiquidVPN():
    directories = ["Canada", "Netherlands", "Romania", "Singapore", "Sweden", "Switzerland", "United Kingdom", "USA"]
    location_file = getLocations("LiquidVPN", "Connections recommended use with Kodi")
    location_file_all = getLocations("LiquidVPN", "All connections")
    for directory in directories:
        profiles = getProfileList("LiquidVPN/" + directory)
        for profile in profiles:
            profile_file = open(profile, 'r')
            lines = profile_file.readlines()
            profile_file.close()
            server = ""
            tls_auth_flag1 = False
            keepalive_flag2 = False
            key_method_flag3 = False
            reneg_sec_flag4 = False
            auth_SHA512_flag5 = False
            remote_random_flag6 = False
            for line in lines:
                if line.startswith("tls-auth") : tls_auth_flag1 = True
                if line.startswith("keepalive") : keepalive_flag2 = True
                if line.startswith("key-method") : key_method_flag3 = True
                if line.startswith("reneg-sec") : reneg_sec_flag4 = True
                if line.startswith("auth SHA512") : auth_SHA512_flag5 = True
                if line.startswith("remote-random") : remote_random_flag6 = True
                tokens = line.split()
                if len(tokens) > 2:
                    if tokens[0] == "remote" : 
                        if not server == "" : server = server + " "
                        server = server + tokens[1]
            line = profile[profile.rfind("\\")+1:profile.index(".ovpn")]
            if directory == "Netherlands": line = line[2:]
            tokens = line.split()
            geo = directory + " - " + tokens[0] + " " + tokens[2] + " (" + tokens[3] + " " + tokens[4] + ")"
            tokens[3] = tokens[3].lower()
            extra = ""
            if directory == "Romania": extra = ",#CERT=ca_romania.crt "
            flags = ""
            if not tls_auth_flag1 : flags = flags + "1"
            if not keepalive_flag2 : flags = flags + "2"
            if not key_method_flag3 : flags = flags + "3"
            if not reneg_sec_flag4 : flags = flags + "4"
            if not auth_SHA512_flag5 : flags = flags + "5"
            if not remote_random_flag6 : flags = flags + "6"
            if extra == "" and not flags == "": extra = ","
            if not flags == "":
                extra = extra + "#REMOVE=" + flags
            output_line = geo + "," + server + "," + tokens[3] + "," + tokens[4] + extra + "\n"
            if not tokens[2] == "Modulating" : location_file.write(output_line)
            location_file_all.write(output_line)
    location_file.close()
    

def generateibVPN():
    # Data is stored as a bunch of ovpn files
    # File name has location.  File has the server
    profiles = getProfileList("ibVPN")
    location_file = getLocations("ibVPN", "")
    for profile in profiles:
        geo = profile[profile.index("ibVPN ")+6:]
        geo = geo.replace(".ovpn", "")
        geo = geo.replace("-", " - ")
        profile_file = open(profile, 'r')
        lines = profile_file.readlines()
        profile_file.close()
        servers = ""
        ports = ""
        for line in lines:
            if line.startswith("remote "):
                _, server, port,_ = line.split()
                if not servers == "" : servers = servers + " "
                servers = servers + server
                if not ports == "" : ports = ports + " "
                ports = ports + port
        output_line = geo + " (UDP)," + servers + "," + "udp," + ports + "\n"
        location_file.write(output_line)
    location_file.close()  

    
def generatePIA():
    # Data is stored as a bunch of ovpn files
    # File name has location.  File has the server
    profiles = getProfileList("PIA")
    location_file = getLocations("PIA", "")
    for profile in profiles:
        geo = profile[profile.index("PIA")+4:]
        geo = geo.replace(".ovpn", "")
        profile_file = open(profile, 'r')
        lines = profile_file.readlines()
        profile_file.close()
        for line in lines:
            if line.startswith("remote "):
                _, server, port = line.split()  
        output_line_udp = geo + " (UDP)," + server + "," + "udp,1194" + "\n"
        output_line_tcp = geo + " (TCP)," + server + "," + "tcp,443" + "\n"
        location_file.write(output_line_udp)
        location_file.write(output_line_tcp)
    location_file.close()
        
    
def generateIPVanish():
    # Data is stored as a bunch of ovpn files
    # File name has location and most of ip address, etc
    # ipvanish-US-Seattle-sea-a04
    profiles = getProfileList("IPVanish")
    location_file = getLocations("IPVanish", "")
    for profile in profiles:
        profile = profile.replace("New-York", "New York")
        profile = profile.replace("San-Jose", "San Jose")
        profile = profile.replace("Los-Angeles", "Los Angeles")
        profile = profile.replace("LosAngeles", "Los Angeles")
        profile = profile.replace("Hong-Kong", "Hong Kong")
        profile = profile.replace("Las-Vegas", "Las Vegas")
        profile = profile.replace("Kuala-Lumpur", "Kuala Lumpur")
        profile = profile.replace("New-Delhi", "New Delhi")
        profile = profile.replace("Sao-Paulo", "Sao Paulo")
        profile = profile.replace("Buenos-Aires", "Buenos Aires")        
        tokens = profile.split("-")
        server = tokens[3] + "-" + tokens[4].replace(".ovpn", "") + ".ipvanish.com"
        output_line_udp = tokens[1] + " - " + tokens[2] + " (UDP)," + server + "," + "udp,443" + "\n"
        output_line_tcp = tokens[1] + " - " + tokens[2] + " (TCP)," + server + "," + "tcp,443" + "\n"
        location_file.write(output_line_udp)
        location_file.write(output_line_tcp)
    location_file.close()
    
    
def generateVyprVPN():
    # Data is stored in a flat text file
    # <Something>  xx.yy.nordvpn.com
    location_file = getLocations("VyprVPN", "")
    source_file = open(getAddonPath(True, "providers/VyprVPN/Servers.txt"), 'r')
    source = source_file.readlines()
    source_file.close()
    for line in source:
        tokens = line.split()        
        for t in tokens:
            if ".goldenfrog.com" in t:                
                server = t.strip(' \t\n\r')
                geo = line.replace(server, "")
                geo = geo.strip(' \t\n\r')
                server = server.replace("vpn.goldenfrog.com", "vyprvpn.com")
                if "," in geo: geo = "USA - " + geo[:geo.index(",")]
                output_line_udp = geo + " (UDP)," + server + "," + "udp,1194" + "\n"
                # VyprVPN doesn't appear to support TCP, so UDP option only
                #output_line_tcp = geo + " (TCP 443)," + server + "," + "tcp,443"  + "\n"
                location_file.write(output_line_udp)
                #location_file.write(output_line_tcp) 
    location_file.close()
    
    
def generateHMA():
    # Data is stored in a flat text file
    # <Continent> - <Country>  xx.yy.rocks  random.xx.yy.rocks
    location_file = getLocations("HMA", "")
    source_file = open(getAddonPath(True, "providers/HMA/Servers.txt"), 'r')
    source = source_file.readlines()
    source_file.close()
    for line in source:
        tokens = line.split()        
        for t in tokens:
            if ".rocks" in t and not "random." in t:
                server = t.strip(' \t\n\r')
                geo = line.replace(server, "")
                geo = geo.replace("random.", "")
                geo = geo.strip(' \t\n\r')
                geo = geo.replace("USA,", "USA -")
                geo = geo.replace("UK,", "UK -")
                output_line_udp = geo + " (UDP)," + server + "," + "udp,53" + "\n"
                output_line_tcp = geo + " (TCP)," + server + "," + "tcp,443"  + "\n"
                location_file.write(output_line_udp)
                location_file.write(output_line_tcp) 
    location_file.close()
        
    
def generatetigerVPN():
    # Data is stored in a flat text file, each line representing a connection
    # valid for UDP and TCP using the standard ports
    location_file_full = getLocations("tigerVPN", "tigerVPN Full Account")
    location_file_lite = getLocations("tigerVPN", "tigerVPN Lite Account")
    source_file = open(getAddonPath(True, "providers/tigerVPN/tigerVPN.csv"), 'r')
    source = source_file.readlines()
    source_file.close()
    for line in source:
        server = line.split(',')
        output_line_udp = server[1] + " " + server[0] + " (UDP)," + server[2] + "," + "udp,1194" + "\n"
        output_line_tcp = server[1] + " " + server[0] + " (TCP)," + server[2] + "," + "tcp,443"  + "\n"
        location_file_full.write(output_line_udp)
        location_file_full.write(output_line_tcp)        
        if server[4].startswith("Lite"):
            location_file_lite.write(output_line_udp)
            location_file_lite.write(output_line_tcp)
    location_file_full.close()
    location_file_lite.close()
    

def generatePureVPN():
    # Data is stored as a bunch of ovpn files
    profiles = getProfileList("PureVPN")
    location_file = getLocations("PureVPN", "")
    for profile in profiles:
        geo = profile[profile.index("PureVPN\\")+8:]
        geo = geo.replace(".ovpn", "")
        geo = geo.replace("ISLE-OF-MAN", "ISLE OF MAN")
        udp_found = False
        tcp_found = False
        virtual_found = False
        if "UDP" in profile: 
            udp_found = True
            proto = "udp"
            geo = geo.replace("-UDP", "")            
        if "TCP" in profile: 
            tcp_found = True
            proto = "tcp"
            geo = geo.replace("-TCP", "")
        if "(V)" in profile:
            virtual_found = True
            geo = geo.replace("(V)", "")
        geo = geo.replace("-", " - ")
        if virtual_found: geo = geo + " Virtual"
        if udp_found: geo = geo + " (UDP)"
        if tcp_found: geo = geo + " (TCP)"
        profile_file = open(profile, 'r')
        lines = profile_file.readlines()
        profile_file.close()
        for line in lines:
            if line.startswith("remote "):
                _, server, port = line.split()             
        output_line = geo + "," + server + "," + proto + "," + port
        if udp_found : output_line = output_line + ",#REMOVE=1"
        if tcp_found : output_line = output_line + ",#REMOVE=2"
        output_line = output_line + "\n"
        location_file.write(output_line)
    location_file.close()


def generateNordVPN():
    # Can't use a template here as NordVPN use multiple certificate and keys. 
    # Copy the file to the target directory and rename it to something more tidy
    # Use the file name to find the country in the servers file
    # Remove what's there to start with
    existing_profiles = glob.glob(getAddonPath(True, "NordVPN" + "/*.ovpn"))
    for connection in existing_profiles:
        xbmcvfs.delete(connection)
    # Get the list from the provider data directory
    profiles = getProfileList("NordVPN")
    destination_path = getAddonPath(True, "NordVPN" + "/")
    source_file = open(getAddonPath(True, "providers/NordVPN/Servers.txt"), 'r')
    servers = source_file.readlines()
    source_file.close()    
    for profile in profiles:
        shortname = profile[profile.index("NordVPN")+9:]
        server = shortname[:shortname.index(".com")+4]
        geo = ""
        for line in servers:
            if server in line:
                geo = line[:line.index(server)-1]
                geo = geo.replace("#", "")
        geo = geo.strip(' \t\n\r')
        if "tcp443" in shortname: proto = "(TCP)"
        if "udp1194" in shortname: proto = "(UDP)"
        filename = geo + " " + proto + ".ovpn"
        profile_file = open(profile, 'r')
        output_file = open(destination_path + filename, 'w')
        profile_contents = profile_file.readlines()
        profile_file.close()
        output = ""
        i = 0
        for line in profile_contents:
            line = line.strip(' \t\n\r')
            if not line == "" and not line.startswith("#mute") and not (i < 15 and line.startswith("#")):
                output_file.write(line + "\n")
            i = i + 1
   