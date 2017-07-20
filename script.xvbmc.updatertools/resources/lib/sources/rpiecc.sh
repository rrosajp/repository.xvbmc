#!/bin/sh

rm -rf /storage/.cache/connman/*/
rm -rf /storage/.cache/bluetooth
rm -rf /storage/.cache/cron
rm -rf /storage/.cache/services
rm -rf /storage/.cache/bluetooth
rm -rf /storage/.cache/ssh
rm -rf /storage/.kodi/temp
rm -rf /storage/.kodi/userdata/addon_data/script.artistslideshow/*/
rm -rf /storage/.kodi/userdata/Database/Textures*
rm -rf /storage/.kodi/userdata/Database/salts*
rm -rf /storage/.kodi/userdata/Thumbnails/*
rm -rf /storage/logfiles

sleep 1

kodi-send -a "Notification(RPi CrapCleaner,FINISHED! PLEASE REBOOT...,5000,special://home/addons/script.xvbmc.updatertools/icon.png)"

sleep 2

#reboot
