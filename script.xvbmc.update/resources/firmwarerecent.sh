#!/bin/sh

# kodi-send -a "Notification(XvBMC Firmware flash,Preparing and auto.Reboot when done...,5000,special://home/addons/script.xvbmc.update/icon.png)"

mount -o remount,rw /flash/
# cp -rav /storage/.kodi/addons/script.xvbmc.update/resources/bin/config-turbo.txt /flash/config.txt
 
curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/bootcode.bin -o /flash/bootcode.bin
curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/start_x.elf -o /flash/start.elf
curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/fixup_x.dat -o /flash/fixup.dat
 
kodi-send -a "Notification(XvBMC most recent Firmware flash,REBOOT in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)"
 
sleep 1
reboot
