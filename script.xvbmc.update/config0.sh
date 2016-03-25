#!/bin/sh

mount -o remount,rw /flash/
cp -rav /storage/.kodi/addons/script.xvbmc.update/config-noclock.txt /flash/config.txt

# cp -rav /storage/.kodi/addons/script.xvbmc.update/xvbmc.py /storage/.kodi/userdata/scripts/xvbmc.py # duplicate script -2- /scripts/ #

kodi-send -a "Notification(XvBMC NL No-overclock Pi,FINISHED! PLEASE REBOOT...,4000,XvBMC.png)"

sleep 1
# reboot
