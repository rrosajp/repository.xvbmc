#!/bin/sh

# kodi-send -a "Notification(XvBMC Firmware flash,Preparing and auto.Reboot when done...,5000,special://home/addons/script.xvbmc.dev/icon.png)"

mount -o remount,rw /flash/

curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/verified/v3/v3.1/20161229_LE703/bootcode.bin -o /flash/bootcode.bin
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/verified/v3/v3.1/20161229_LE703/fixup_x.dat -o /flash/fixup.dat
curl https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/zips/update/firmware/verified/v3/v3.1/20161229_LE703/start_x.elf -o /flash/start.elf

sleep 3

# kodi-send -a "Notification(XvBMC advised Firmware flashed,REBOOT in 5 seconds...,5000,special://home/addons/script.xvbmc.dev/icon.png)"

# reboot
