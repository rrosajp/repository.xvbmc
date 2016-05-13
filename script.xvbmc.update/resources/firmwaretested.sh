#!/bin/sh

# kodi-send -a "Notification(XvBMC Firmware flash,Preparing and auto.Reboot when done...,5000,special://home/addons/script.xvbmc.update/icon.png)"

mount -o remount,rw /flash/
# cp -rav /storage/.kodi/addons/script.xvbmc.update/resources/data/config-turbo.txt /flash/config.txt
 
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/verified/20160412v3rc5+6+Final/bootcode.bin -o /flash/bootcode.bin
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/verified/20160412v3rc5+6+Final/fixup_x.dat -o /flash/fixup.dat
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/verified/20160412v3rc5+6+Final/start_x.elf -o /flash/start.elf
 
kodi-send -a "Notification(XvBMC advised Firmware flashed,REBOOT in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)"
 
sleep 1
reboot
