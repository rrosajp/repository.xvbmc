#!/bin/sh

# kodi-send -a "Notification(XvBMC Firmware flash,Preparing and auto.Reboot when done...,5000,special://home/addons/script.xvbmc.dev/icon.png)"

mount -o remount,rw /flash/

curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/XvBMCimage/v3/v3.1/20-01-2017/bootcode.bin -o /flash/bootcode.bin
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/XvBMCimage/v3/v3.1/20-01-2017/fixup_x.dat -o /flash/fixup.dat
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/XvBMCimage/v3/v3.1/20-01-2017/start_x.elf -o /flash/start.elf

sleep 3

# kodi-send -a "Notification(XvBMC default Firmware re-flashed,REBOOT in 5 seconds...,5000,special://home/addons/script.xvbmc.dev/icon.png)"

# reboot
