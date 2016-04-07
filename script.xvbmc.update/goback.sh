#!/bin/sh

# kodi-send -a "Notification(XvBMC Firmware Update,Preparing and auto.reboot when done...,5000,special://home/addons/script.xvbmc.update/icon.png)"

mount -o remount,rw /flash/
cp -rav /storage/.kodi/addons/script.xvbmc.update/config-turbo.txt /flash/config.txt

curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/20160404xvbmcRC4/bootcode.bin -o /flash/bootcode.bin
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/20160404xvbmcRC4/fixup_x.dat -o /flash/fixup.dat
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/20160404xvbmcRC4/start_x.elf -o /flash/start.elf

# cp -rav /storage/.kodi/addons/script.xvbmc.update/goback.sh /storage/.kodi/userdata/scripts/goback.sh    #    duplicate script -2- /scripts/    #

kodi-send -a "Notification(XvBMC Firmware RE-Flashed,REBOOT in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)"

sleep 1
reboot