#!/bin/sh

mount -o remount,rw /flash/
cp -rav /storage/.kodi/addons/script.xvbmc.update/resources/bin/config-turbo.txt /flash/config.txt
 
kodi-send -a "Notification(XvBMC NL Turbo-overclock Pi,FINISHED! PLEASE REBOOT...,4000,special://home/addons/script.xvbmc.update/icon.png)"
 
sleep 1
# reboot
