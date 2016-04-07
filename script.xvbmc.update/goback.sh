#!/bin/sh

# kodi-send -a "Notification(XvBMC Firmware Update,Preparing and auto.reboot when done...,5000,special://home/addons/script.xvbmc.update/icon.png)"

mount -o remount,rw /flash/
cp -rav /storage/.kodi/addons/script.xvbmc.update/config-turbo.txt /flash/config.txt

curl https://github.com/XvBMC/repository.xvbmc/blob/master/zips/update/firmware/20160404xvbmcRC4/bootcode.bin?raw=true -o /flash/bootcode.bin
curl https://github.com/XvBMC/repository.xvbmc/blob/master/zips/update/firmware/20160404xvbmcRC4/fixup_x.dat?raw=true -o /flash/fixup.dat
curl https://github.com/XvBMC/repository.xvbmc/blob/master/zips/update/firmware/20160404xvbmcRC4/start_x.elf?raw=true -o /flash/start.elf

# cp -rav /storage/.kodi/addons/script.xvbmc.update/goback.sh /storage/.kodi/userdata/scripts/goback.sh    #    duplicate script -2- /scripts/    #

kodi-send -a "Notification(XvBMC Firmware flashed,REBOOT in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)"

sleep 1
reboot