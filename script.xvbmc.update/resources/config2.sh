#!/bin/sh

mount -o remount,rw /flash/
cp -rav /storage/.kodi/addons/script.xvbmc.update/resources/bin/config-x265.txt /flash/config.txt
 
kodi-send -a "Notification(XvBMC NL x265-overclock Pi,FINISHED! PLEASE REBOOT...,4000,special://home/addons/script.xvbmc.update/icon.png)"
 
sleep 1
# reboot
