OpenELEC RPi Codec Config
=========================

BUY:	http://www.raspberrypi.com/license-keys/
HowTo:	http://www.howtogeek.com/137654/how-to-add-mpeg-2-and-vc-1-video-codec-support-to-your-raspberry-pi/


#Retrieving the Serial Number: 
First, visit the command prompt either at the actual terminal or remotely connected to the terminal via an SSH tool such as PuTTY. 
If you have a keyboard attached to your Raspbmc machine, simply select “Exit” out of the Raspbmc interface via the power button in the lower left hand side of the GUI. 
Press ESC to load the command prompt instead of booting back into the Raspbmc GUI. This will deposit you at the command prompt.

Alternatively, 
if you would like to access the command prompt remotely, fire up your SSH client (such as PuTTY) and enter the IP address of your Rasperry Pi unit.

Whether you have pulled up the command prompt directly at the machine or via SSH you will be prompted to login. 
[B]The default login/password combination for:[/B]
[I]Raspberry is pi / raspberry 
OpenELEC is root / openeelec 
LibreELEC is root / libreelec[/I] 

Once at the command prompt enter the following command: [B]cat /proc/cpuinfo[/B]
Your Pi will spit back 11 lines of text, but the only one of interest to us is the last line labeled Serial. 
Copy the unique 16 digital serial number (partially obfuscated in the screenshot here).

Because the license is granted to each specific Raspberry Pi board, repeat the above process for all Raspberry Pi boards you wish to purchase a license for.
Once you have the the serial number for each individual unit, it’s time to purchase the licenses from the Raspberry Pi foundation.


#Purchasing the License: 
Visit the Raspberry Pi foundation’s purchase page for the MPEG-2 license and/or VC-1 license.  
Enter your Raspberry Pi serial number in the appropriate blank beneath the price. Add the license to your cart. 
Repeat this process for all the licenses on all the units you wish to add the codecs to.

Although the foundation indicates that it could take up to 72 hours for your license to arrive via email, we received ours in about 24 hours. 
When your email arrives it will include a code for each license formatted like such:
[I] decode_MPG2=0000000000[/I] 
[I] decode_WVC1=0000000000[/I] 

The [I]0000000000[/I] portion of the license is your unique 10-digit alphanumeric license code.


#Installing the Licenses:
Now that we have the license codes, it’s time to add them to your Raspberry Pi and get to enjoying enhanced media playback.

[B]Manually installing the licenses:[/B]
The manual installation technique works for any installation on the Raspberry Pi, including Raspbmc.
To manually install the codecs, you need to power down your Raspberry Pi device, remove the SD card, and mount the SD card on a computer with access to a simple text editor.

Raspberry Pi SD cards include a FAT formatted mini partition that holds startup tools including an easily edited configuration file labeled config.txt. 
[Note: Some operating systems builds may not automatically create a config.txt file; if there is no config.txt simply create your own.]

Locate the file and make a copy, renaming it config.old—this version will serve as a backup in case anything goes wrong during the editing process. 
Open up the original config.txt in your text editor of choice (we’re using Notepad++).
Depending on what operating system you’re running on your Pi, the configuration file may look slightly different. 
Leave the existing entries alone. Cut and paste the formatted license entries you received in your email.

Save the config.txt file and safely eject the SD card from your computer. Return the SD card to the Raspberry Pi and power up the device.

[B][U]Adding the licenses via this 'OpenELEC RPi Codec Config' tool[/U]:[/B]
If you’re running 'OpenELEC/LibreELEC Raspberry ([I]codec tool[/I])', you can skip the whole manually editing the config.txt step and take advantage of this 'Raspberry license codec-tool'...

To do so, head over to your Raspberry (XvBMC) and navigate from the main interface to Programs –> 'OpenELEC RPi Codec Config'. 
Open 'OpenELEC RPi Codec Config' Settings, here you can click on MPEG2 and VC1 and input your license number. 
[B]Don’t[/B] type in the entire string provided for you by Raspberry Pi, leave off the leading decode_MPG2= and decode_WVC1= portion. 
[B]Only[/B] input the 10-digit string after the equal sign into each codec’s respective slot.

Once you have added the appropriate codec licenses, head back to the main interface and reboot your device via the power selection menu in the lower left hand corner.


#Testing the codecs: 
The most enjoyable way to test your new codecs is to fire up a media file you know wouldn’t play without it, sit back, and watch it play perfectly.

The more technical way to check, should you run into any hiccups and wish to confirm that your license is recognized by the device, is to head to the command prompt and enter the following commands:
[I] vcgencmd codec_enabled MPG2[/I]
[I] vcgencmd codec_enabled WVC1[/I]

[B]The Pi should immediately return that the codec is enabled.[/B]

[I]Everything looks good at the command prompt and the previously audio-only files now play both their audio and video channels. 
For a few bucks and a few minutes of our time, we’re ready to enjoy the wide variety of videos encoded in MPEG-2 and VC-1 codecs.[/I]