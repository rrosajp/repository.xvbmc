#!/bin/sh

# kodi-send -a "Notification(XvBMC Firmware Update,Preparing and auto.reboot when done...,5000,special://home/addons/script.xvbmc.update/icon.png)"

mount -o remount,rw /flash/
cp -rav /storage/.kodi/addons/script.xvbmc.update/config-turbo.txt /flash/config.txt

curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/bootcode.bin -o /flash/bootcode.bin
curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/start_x.elf -o /flash/start.elf
curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/fixup_x.dat -o /flash/fixup.dat

# cp -rav /storage/.kodi/addons/script.xvbmc.update/firmware.sh /storage/.kodi/userdata/scripts/firmware.sh    #  duplicate script -2- /scripts/  #

kodi-send -a "Notification(XvBMC Firmware flashed,REBOOT in 5 seconds...,5000,special://home/addons/script.xvbmc.update/icon.png)"

sleep 1
reboot
