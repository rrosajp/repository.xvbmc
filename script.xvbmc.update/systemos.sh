#!/bin/sh

kodi-send -a "Notification(XvBMC LibreELEC OS Update,preparing v6.90.004 and reboot when done...,5000,special://home/addons/script.xvbmc.update/icon.png)"

# mount -o remount,rw /flash/                                                                                  #
# cp -rav /storage/.kodi/addons/script.xvbmc.firmware/config.txt /flash/config.txt                             #
# curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/bootcode.bin -o /flash/bootcode.bin  #
# curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/start_x.elf -o /flash/start.elf      #
# curl https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/fixup_x.dat -o /flash/fixup.dat      #

curl http://releases.libreelec.tv/LibreELEC-RPi2.arm-6.90.004.tar -o /storage/.update/LibreELECrpi2ARM690004.tar

kodi-send -a "Notification(XvBMC SYSTEM Update Done,Reboot in 5 seconds...,4000,special://home/addons/script.xvbmc.update/icon.png)"

sleep 1
reboot
