# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Documentaries on YouTube by coldkeys used as source project
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Original author: coldkeys [This script is a MOD]
#------------------------------------------------------------

# ! TROMA movie-addon by EPiC 'XvBMC Nederland' (with special thanks to Patrick Dijkkamp) ... Please keep credits if you copy/paste links, THX !

import os,sys,urllib
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
import re,base64,plugintools
from addon.common.addon import Addon

import YDStreamExtractor

addonID = 'plugin.video.xvbmc.troma'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

tromavids = [
            ("A Nocturne : Night of the Vampire","https://www.youtube.com/watch?v=pdL4nK4iJUM","http://www.troma.com/wp-content/uploads/2011/01/A_NOCTURNE_COVER.jpg"),
            ("A Nymphoid Barbarian In Dinosaur Hell!","https://www.youtube.com/watch?v=7fw9a96Ei0k","http://www.troma.com/wp-content/uploads/2011/02/NYMPHOID_BARBARIAN_IN_DINOSAUR_HELL_web.jpg"),
            ("A Tale Of Two Sisters","https://www.youtube.com/watch?v=krTA9NPde04","http://www.troma.com/wp-content/uploads/2011/03/SHEEN_COVER.jpg"),
            ("Actium Maximus : War Of The Alien Dinosaurs","https://www.youtube.com/watch?v=6Zor9h7bfy8","https://www.tromashop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/t/r/tr9258.jpg"),
            ("Alien Blood","https://www.youtube.com/watch?v=PPvmgIo6Dc4","http://www.troma.com/wp-content/uploads/2011/02/COVER.jpg"),
            ("Angel Negro","https://www.youtube.com/watch?v=sLdtnI-QBgg","http://www.troma.com/wp-content/uploads/2011/02/ANGEL_NEGRO_COVER.jpg"),
            ("Another Space Daze","https://www.youtube.com/watch?v=2PdM8fci4iM","http://i.ebayimg.com/images/g/cfAAAMXQQQhRb6Vb/s-l1600.jpg"),
            ("Attack Of The Tromaggot!","https://www.youtube.com/watch?v=H0zBCjnEWuc","http://www.troma.com/wp-content/uploads/2012/10/TROMAGGOT.jpg"),
            ("Back Road Diner","https://www.youtube.com/watch?v=ys8uQvoKqB0","http://www.troma.com/wp-content/uploads/2011/01/BACK_ROAD_DINER_COVER.jpg"),
            ("Baconhead","https://www.youtube.com/watch?v=v3uQN53oHh0","http://www.troma.com/wp-content/uploads/2011/02/COVER1.jpg"),
            ("Banana Motherf*ck*r","https://www.youtube.com/watch?v=QOt0XjU1TqQ","http://www.troma.com/wp-content/uploads/2014/07/BMF_MOVIE-CATALOG.jpg"),
            ("Battle Of Love's Return","https://www.youtube.com/watch?v=RVKgsM6Eiug","http://www.troma.com/wp-content/uploads/2011/02/BATTLE_OF_LOVES_RETURN_COVER.jpg"),
            ("Beg!","https://www.youtube.com/watch?v=E1-FdZJokoo","http://www.troma.com/wp-content/uploads/2011/02/COVER3.jpg"),
            ("Belcebu","https://www.youtube.com/watch?v=ceXc_jk5vf4","http://www.troma.com/wp-content/uploads/2011/02/COVER4.jpg"),
            ("Beware Children At Play!","https://www.youtube.com/watch?v=3qkaI96Affc","http://www.troma.com/wp-content/uploads/2011/01/BEWARE_CHILDREN_AT_PLAY_COVER.jpg"),
            ("BEYOND EVIL","https://www.youtube.com/watch?v=zlMl-SUGBjI","http://www.troma.com/wp-content/uploads/2011/03/beyond-evil.jpg"),
            ("Big Gus What's The Fuss?","https://www.youtube.com/watch?v=zS2EgumLXXE","https://www.tromashop.com/media/catalog/product/cache/1/image/265x265/9df78eab33525d08d6e5fb8d27136e95/t/r/tr8888.gif"),
            ("Bigfoot","https://www.youtube.com/watch?v=b0wbdyGGsIc","http://www.troma.com/wp-content/uploads/2011/02/BIGFOOT_COVER.jpg"),
            ("Blondes Have More Guns","https://www.youtube.com/watch?v=QKs2NWVzEKE","http://www.troma.com/wp-content/uploads/2011/01/BLONDES_HAVE_MORE_GUNS_COVER.jpg"),
            ("Blood Hook","https://www.youtube.com/watch?v=4VI7ntoJNEk","http://www.troma.com/wp-content/uploads/2011/02/BLOOD_HOOD_.jpg"),
            ("Blood Junkie","https://www.youtube.com/watch?v=ttI4dpHfS_o","http://www.troma.com/wp-content/uploads/2011/01/BJ_COVER.jpg"),
            ("Blood Sisters of Lesbian Sin","https://www.youtube.com/watch?v=CNZYxwyzw9w","http://www.troma.com/wp-content/uploads/2011/02/COVER5.jpg"),
            ("Bloodspit","https://www.youtube.com/watch?v=Xcthxl8lVzA","http://www.troma.com/wp-content/uploads/2011/02/COVER6.jpg"),
            ("Body Parts","https://www.youtube.com/watch?v=IND4hJM7vfk","http://www.troma.com/wp-content/uploads/2011/02/COVER7.jpg"),
            ("Bride Of Killer Nerd!","https://www.youtube.com/watch?v=DcQDGfZqTwM","http://www.troma.com/wp-content/uploads/2011/02/COVER8.jpg"),
            ("Bugged!","https://www.youtube.com/watch?v=iCorDG3OHuU","http://www.troma.com/wp-content/uploads/2011/02/BUGGED_COVER.jpg"),
            ("Butchers, The","https://www.youtube.com/watch?v=C3SIIWbVhE4","http://www.troma.com/wp-content/uploads/2011/02/THE_BUTCHERS_COVER.jpg"),
            ("BUTTCRACK!","https://www.youtube.com/watch?v=4WfbOFDIyPs","http://www.troma.com/wp-content/uploads/2011/02/BUTTCRACK_COVER.jpg"),
            ("Cannibal: The Musical","https://www.youtube.com/watch?v=alqtKb17Ggo","http://www.troma.com/wp-content/uploads/2011/02/CANNIBAL_movie.jpg"),
            ("Cars 3","https://www.youtube.com/watch?v=x87j0u7uB3c","http://www.troma.com/wp-content/uploads/2012/10/CARS3-CATALOG.jpg"),
            ("Children, The","https://www.youtube.com/watch?v=OGEjRKlJJhI","http://www.troma.com/wp-content/uploads/2011/02/COVER9.jpg"),
            ("Class Of Nuke 'Em High","https://www.youtube.com/watch?v=CYWOevwr-zw","http://www.troma.com/wp-content/uploads/2011/02/CLASS_OF_NUKE_EM_HIGH_COVER.jpg"),
            ("Class of Nuke'Em High 2: Subhumanoid Meltdown","https://www.youtube.com/watch?v=ical5lbkOiE","http://www.troma.com/wp-content/uploads/2011/02/COVER10.jpg"),
            ("Class of Nuke'Em High Part 3: The Good, the Bad and the Subhumanoid","https://www.youtube.com/watch?v=X6yePgPD1Ls","http://www.troma.com/wp-content/uploads/2011/02/CLASS_OF_NUKE_EM_HIGH3_COVER.jpg"),
            ("Combat Shock - Director's Cut","https://www.youtube.com/watch?v=l9nX5Q1b1Hg","http://www.troma.com/wp-content/uploads/2011/02/COMBAT_SHOCK_COVER.jpg"),
            ("Connect 5","https://www.youtube.com/watch?v=cLUPeODKdtY","http://www.troma.com/wp-content/uploads/2011/02/LASTHORRORFILM1.jpg"),
            ("Contra Conspiracy","https://www.youtube.com/watch?v=JLoRFWyLkdQ","http://www.troma.com/wp-content/uploads/2011/03/contra-conspiracy.jpg"),
            ("Cybernator","https://www.youtube.com/watch?v=fuvUcKw4Ftk","http://www.troma.com/wp-content/uploads/2011/02/COVER13.jpg"),
            ("Dark Nature","https://www.youtube.com/watch?v=-IjvHgPYe98","http://www.troma.com/wp-content/uploads/2011/02/DARK_NATURE_COVER.jpg"),
            ("Decampitated","https://www.youtube.com/watch?v=FKQJkJpdCnI","http://www.troma.com/wp-content/uploads/2011/02/COVER16.jpg"),
            ("Def by Temptation","https://www.youtube.com/watch?v=uM4tOnWae0s","http://www.troma.com/wp-content/uploads/2011/02/DEF_BY_TEMPTATION_COVER.jpg"),
            ("Demented Death Farm Massacre","https://www.youtube.com/watch?v=zB5DaF46wZc","http://www.troma.com/wp-content/uploads/2011/02/DEMENTED_DEATH_FARM_MASSACRE_COVER.jpg"),
            ("DOCU: All The Love You Cannes","https://www.youtube.com/watch?v=ZuROkQC3fy4","http://www.troma.com/wp-content/uploads/2011/02/ALL_THE_LOVE_YOU_CANNES_COVER.jpg"),
            ("DOCU: APOCALYPSE SOON","https://www.youtube.com/watch?v=1_X9FnnhC8I","http://www.troma.com/wp-content/uploads/2011/03/apocalypsesoon.jpg"),
            ("DOCU: Bazaar Bizarre","https://www.youtube.com/watch?v=WpgV7pssPDA","http://www.troma.com/wp-content/uploads/2011/02/BAZAAR_BIZARRE_COVER.jpg"),
            ("DOCU: Blood Boobs & Beast!","https://www.youtube.com/watch?v=Z-CSIFoqJD4","http://www.troma.com/wp-content/uploads/2011/01/BLOOD_BOOBS_AND_BEAST_COVER.jpg"),
            ("DOCU: Farts of Darkness","https://www.youtube.com/watch?v=O4DiEz_1AIk","http://www.troma.com/wp-content/uploads/2011/03/fartsofdarkness.jpg"),
            ("DOCU: Jefftowne","https://www.youtube.com/watch?v=T1DbQbmc3Vg","http://www.troma.com/wp-content/uploads/2011/02/JEFFTOWNE_web.jpg"),
            ("DOCU: Poultry In Motion","https://www.youtube.com/watch?v=GJFICyxV7xA","http://ia.media-imdb.com/images/M/MV5BMjA2Njk3MDc5OV5BMl5BanBnXkFtZTgwNjk2NDg2NjE@._V1_.jpg"),
            ("DOCU: Splendor and Wisdom","https://www.youtube.com/watch?v=OlPP0-6qqVU","https://www.tromashop.com/media/catalog/product/cache/1/image/265x265/9df78eab33525d08d6e5fb8d27136e95/s/p/splendor[1].jpg"),
            ("DOCU: Story Of A Junkie","https://www.youtube.com/watch?v=21uJglN6siA","http://www.troma.com/wp-content/uploads/2011/02/STORY_OF_A_JUNKIE_web.jpg"),
            ("Doggie Tails","https://www.youtube.com/watch?v=VirQxX9QGHw","http://www.troma.com/wp-content/uploads/2011/02/DOGGIE_TAILS_COVER.jpg"),
            ("Dr. Hackenstein","https://www.youtube.com/watch?v=GyUMa9r8Yyk","http://www.troma.com/wp-content/uploads/2011/02/DR_HACKENSTEIN.jpg"),
            ("Dragon Fury","https://www.youtube.com/watch?v=pZZUa6lJQqM","http://www.troma.com/wp-content/uploads/2011/03/DRAGON_FURY.jpg"),
            ("Drawing Blood","https://www.youtube.com/watch?v=DoFt0j_eh0w","http://www.troma.com/wp-content/uploads/2011/02/DRAWING_BLOOD_COVER.jpg"),
            ("Electra Love 2000","https://www.youtube.com/watch?v=ScYhyaPzPPw","http://www.troma.com/wp-content/uploads/2011/03/ElectraLove2000.jpg"),
            ("Ellie","https://www.youtube.com/watch?v=6go1nfKE2b4","http://www.troma.com/wp-content/uploads/2011/02/ELLIE_COVER.jpg"),
            ("Eves Beach Fantasy","https://www.youtube.com/watch?v=VGi7iQvXk4I","http://www.troma.com/wp-content/uploads/2011/02/COVER20.jpg"),
            ("Evolved Part 1, The","https://www.youtube.com/watch?v=nThZe6hFkZo","http://www.troma.com/wp-content/uploads/2011/02/THE_EVOLVED.jpg"),
            ("Eye of the Stranger","https://www.youtube.com/watch?v=0f39OWEqJ24","http://www.troma.com/wp-content/uploads/2011/02/EYE_OF_THE_STRANGER_COVER.jpg"),
            ("Fag Hag","https://www.youtube.com/watch?v=h-Htv8y7xSA","http://www.troma.com/wp-content/uploads/2015/02/FH-poster.jpg"),
            ("Fatty Drives The Bus","https://www.youtube.com/watch?v=N0Dt9i9IUNg","http://www.troma.com/wp-content/uploads/2011/01/FATTY_DRIVES_THE_BUS_COVER.jpg"),
            ("Ferocious Female Freedom Fighters","https://www.youtube.com/watch?v=HCljpl9EOpw","http://www.troma.com/wp-content/uploads/2011/01/FEROCIOUS_FEMALE_FREEDOM_FIGHTERS_COVER.jpg"),
            ("Fertilize The Blaspheming Bombshell!","https://www.youtube.com/watch?v=gAA8c2kVXV4","http://www.troma.com/wp-content/uploads/2011/02/FERTILIZE_THE_BLASPHEMING_BOMBSHELL.jpg"),
            ("Flesh Eaters From Outer Space","https://www.youtube.com/watch?v=DfW0CArg6UY","http://www.troma.com/wp-content/uploads/2011/02/flesh-eaters-from-space-.jpg"),
            ("FOREPLAY","https://www.youtube.com/watch?v=GtbGeB9I52Q","http://www.troma.com/wp-content/uploads/2011/02/Foreplay.jpg"),
            ("Fortress Of Amerikkka!","https://www.youtube.com/watch?v=rMfjHjza7Lg","http://www.troma.com/wp-content/uploads/2011/02/FORTRESS_OF_AMERIKKKA.jpg"),
            ("Fraternity Demon","https://www.youtube.com/watch?v=Bhqr9MQRq1A","http://www.troma.com/wp-content/uploads/2011/03/fraternity-demon.jpg"),
            ("First Turn On!, The","https://www.youtube.com/watch?v=BTqDR0pLXaA","http://www.troma.com/wp-content/uploads/2011/02/FIRST_TURN-ON.jpg"),
            ("Frightmare","https://www.youtube.com/watch?v=tEJKx6SpXu0","http://www.troma.com/wp-content/uploads/2011/02/FRIGHTMARE.jpg"),
            ("G.I. Executioner, The","https://www.youtube.com/watch?v=fZCkspwzGQg","http://www.troma.com/wp-content/uploads/2011/02/GI_EXECUTIONER.jpg"),
            ("Getting Lucky","https://www.youtube.com/watch?v=3kwnQV5Q3Ao","http://www.troma.com/wp-content/uploads/2011/02/GETTING_LUCKY.jpg"),
            ("Ghosts of the Heartland","https://www.youtube.com/watch?v=cAVhLy5s7t8","http://www.troma.com/wp-content/uploads/2015/03/GHOSTS.jpg"),
            ("Girl Who Returned, The","https://www.youtube.com/watch?v=nRnfP222wIQ","https://www.tromashop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/t/r/tr8889.gif"),
            ("Go to Hell","https://www.youtube.com/watch?v=ALywujEtdUM","http://www.troma.com/wp-content/uploads/2011/02/go-to-hell.jpg"),
            ("Graduation Day","https://www.youtube.com/watch?v=QlmtF3oe1HM","http://www.troma.com/wp-content/uploads/2011/02/graduation-day.jpg"),
            ("GRIM","https://www.youtube.com/watch?v=FKLJ5zwUE80","http://www.troma.com/wp-content/uploads/2011/02/grim.jpg"),
            ("Hanging Woman, The","https://www.youtube.com/watch?v=0cdpb1iTsSE","http://www.troma.com/wp-content/uploads/2011/02/HANGING_WOMAN_web.jpg"),
            ("Heavy Mental","https://www.youtube.com/watch?v=8am8BrSTxvk","http://www.troma.com/wp-content/uploads/2011/02/heavy-mental.jpg"),
            ("Hemo","https://www.youtube.com/watch?v=aUPoll6fwtc","http://www.troma.com/wp-content/uploads/2012/10/HEMO.jpg"),
            ("Hollowgate","https://www.youtube.com/watch?v=KLsaZQrVYF8","http://www.troma.com/wp-content/uploads/2011/03/HOLLOW_GATE_web.jpg"),
            ("Horror Of The Hungry Humongous Hungan","https://www.youtube.com/watch?v=Jma_o6vX72Y","http://www.troma.com/wp-content/uploads/2011/03/HORROR_OF_THE_HUMUNGOUS_HUNGRY_HUNGAN_web.jpg"),
            ("Hot Summer in Barefoot County","https://www.youtube.com/watch?v=0SNPzXLxIvo","http://www.troma.com/wp-content/uploads/2011/02/HOT_SUMMER_IN_BAREFOOT_COUNTY_web.jpg"),
            ("I Was A Teenage TV Terrorist!","https://www.youtube.com/watch?v=Eay9cz3kXCI","http://www.troma.com/wp-content/uploads/2011/02/I_WAS_A_TEENAGE_TV_TERRORIST_web.jpg"),
            ("Igor and the Lunatics","https://www.youtube.com/watch?v=8fYtO8ohgb0","http://www.troma.com/wp-content/uploads/2011/02/IGOR_AND_THE_LUNATICS_web.jpg"),
            ("Jessicka Rabid","https://www.youtube.com/watch?v=2dE0MZrRbFk","http://www.troma.com/wp-content/uploads/2011/02/JRABID_COVER.jpg"),
            ("Jurassic Women","https://www.youtube.com/watch?v=scWyknOtfbs","https://image.tmdb.org/t/p/w300_and_h450_bestv2/ltte1HZ9byjx6PlHUrp739hc8x3.jpg"),
            ("Killer Nerd","https://www.youtube.com/watch?v=ShhENu0ZWQo","http://www.troma.com/wp-content/uploads/2011/01/KILLER_NERD_COVER.jpg"),
            ("Killer Yacht Party","https://www.youtube.com/watch?v=E-baG5IkmDY","http://www.troma.com/wp-content/uploads/2011/03/KYP_COVER.jpg"),
            ("Killing Twice","https://www.youtube.com/watch?v=vPZ8Oi5VN_Y","http://www.troma.com/wp-content/uploads/2012/10/KILLING-TWICE_MOVIE-CATALOG.jpg"),
            ("Klown Kamp Massacre","https://www.youtube.com/watch?v=_YksB7Cohwc","http://www.troma.com/wp-content/uploads/2011/02/KKM_COVER.jpg"),
            ("LA  Maniac","https://www.youtube.com/watch?v=KTd038GmUZg","http://www.troma.com/wp-content/uploads/2013/04/LAManiac.jpg"),
            ("LA Crackdown","https://www.youtube.com/watch?v=bsUVbzVYxGY","http://www.troma.com/wp-content/uploads/2011/03/LA_CRACKDOWN_web.jpg"),
            ("LA Crackdown 2","https://www.youtube.com/watch?v=lgMJWbeIWiQ","http://www.refused-classification.com/images/films/la-crackdown-2-dvd-flashback-entertainment.jpg"),
            ("Last Horror Film, The","https://www.youtube.com/watch?v=ZTHO5zNXKG4","https://www.tromashop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/l/h/lhf.jpg"),
            ("LEGEND OF THE CHUPACABRA","https://www.youtube.com/watch?v=JdM9CI7XaH0","http://www.troma.com/wp-content/uploads/2011/02/LEGEND_OF_CHUPACADRA_web.jpg"),
            ("Lollilove","https://www.youtube.com/watch?v=DJbk6eyM8UQ","http://www.troma.com/wp-content/uploads/2011/02/LOLLILOVE.jpg"),
            ("Loony in the Woods","https://www.youtube.com/watch?v=vCRhB5zZ9Qc","http://www.troma.com/wp-content/uploads/2013/04/LOONYINTHEWOODS.jpg"),
            ("Lust For Freedom","https://www.youtube.com/watch?v=Xo5mX3pNvxo","http://www.troma.com/wp-content/uploads/2011/02/LUST_FOR_FREEDOM_web.jpg"),
            ("Luther The Geek","https://www.youtube.com/watch?v=zNKPAibmS-M","http://www.troma.com/wp-content/uploads/2011/02/luther-the-geek.jpg"),
            ("Macabre Pair Of Shorts","https://www.youtube.com/watch?v=Maw_mpH0bp0","http://www.troma.com/wp-content/uploads/2011/02/macabra-pair-of-shorts.jpg"),
            ("Mad Dog Morgan","https://www.youtube.com/watch?v=utYuLCYV8l0","http://www.troma.com/wp-content/uploads/2011/02/MAD_DOG_MORGAN_web.jpg"),
            ("Madigan's Millions","https://www.youtube.com/watch?v=eleqXRSnUmY","http://www.troma.com/wp-content/uploads/2011/02/MADIGANS_MILLION_web.jpg"),
            ("MARCH MUSICAL MADNESS ON TROMA NOW!!!","https://www.youtube.com/watch?v=QRSclkjqttA","http://i2.wp.com/www.horrorsociety.com/wp-content/uploads/2016/03/309997b2-416b-4d31-a01f-c4ad91036958.jpg?resize=311%2C445"),
            ("Mommys Epitaph","https://www.youtube.com/watch?v=yjoZrJYEUxw","http://www.troma.com/wp-content/uploads/2011/03/mommys-epitah.jpg"),
            ("MR. BRICKS: A HEAVY METAL MURDER MUSICAL","https://www.youtube.com/watch?v=pC5V9xIZYWQ","http://www.troma.com/wp-content/uploads/2012/10/MRBRICKS.jpg"),
            ("Nerds Of A Feather","https://www.youtube.com/watch?v=ZPlMd9FOSmI","http://www.troma.com/wp-content/uploads/2011/03/NerdsOfAFeather.jpg"),
            ("Nightbeast","https://www.youtube.com/watch?v=5xHxS0bzIEg","http://www.troma.com/wp-content/uploads/2011/02/NIGHTBEAST_web.jpg"),
            ("Nightmare Weekend","https://www.youtube.com/watch?v=bEE1MJrZJdY","http://www.troma.com/wp-content/uploads/2011/03/NIGHTMARE_WEEKEND_web.jpg"),
            ("Open 24/7","https://www.youtube.com/watch?v=xaJB2wMfiPQ","http://www.troma.com/wp-content/uploads/2011/10/OPEN-24-7-MOVIE-CATALOG.jpg"),
            ("Parts of the Family","https://www.youtube.com/watch?v=wUq8ZwIXdHk","http://www.troma.com/wp-content/uploads/2011/02/PARTS_OF_THE_FAMILY_web.jpg"),
            ("Pep Squad","https://www.youtube.com/watch?v=CWssk2UTPJo","http://www.troma.com/wp-content/uploads/2011/02/pep-squad.jpg"),
            ("Poultrygeist: Night Of The Chicken Dead!","https://www.youtube.com/watch?v=UZxo9AwQxk8","http://www.troma.com/wp-content/uploads/2011/02/POULTRYGEIST_web.jpg"),
            ("Psycho Sleepover","https://www.youtube.com/watch?v=KqsAZvaGrbY","http://www.troma.com/wp-content/uploads/2011/03/PSYCHOS_COVER.jpg"),
            ("Purge","https://www.youtube.com/watch?v=_xI1ARTF0i8","http://www.troma.com/wp-content/uploads/2011/02/PURGE-CATALOG.jpg"),
            ("Rabid Grannies","https://www.youtube.com/watch?v=4joDVOIcfYM","http://www.troma.com/wp-content/uploads/2011/02/RABID_GRANNIES_web.jpg"),
            ("Redneck Zombies","https://www.youtube.com/watch?v=7l1JAAS8LPs","http://www.troma.com/wp-content/uploads/2011/02/RNZ_COVER.jpg"),
            ("Rowdy Girls, The","https://www.youtube.com/watch?v=wt3w6W4kxbo","http://www.troma.com/wp-content/uploads/2011/02/ROWDY_GIRLS_web.jpg"),
            ("SECRET OF THE MAGIC MUSHROOMS, The","https://www.youtube.com/watch?v=BC23Xuee4I8","http://www.troma.com/wp-content/uploads/2011/06/poster_01_354x500.jpg"),
            ("Seduction Of A Nerd","https://www.youtube.com/watch?v=_wGjom1wcEo","http://www.troma.com/wp-content/uploads/2011/02/seduction-of-a-.jpg"),
            ("Seduction Of Dr Fugazzi, The","https://www.youtube.com/watch?v=wiocnObbFlw","http://www.troma.com/wp-content/uploads/2011/02/SEDUCTION_OF_DR_FUGAZZI_web.jpg"),
            ("Sgt Kabukiman NYPD","https://www.youtube.com/watch?v=8ua2Rr85Gi4","http://www.troma.com/wp-content/uploads/2011/02/SGT_KABUKIMAN_V2_web.jpg"),
            ("Shakespeare In and Out","https://www.youtube.com/watch?v=WGgOjBdkTDY","http://www.troma.com/wp-content/uploads/2011/02/shakespear-in-out.jpg"),
            ("Space Zombie Bingo!","https://www.youtube.com/watch?v=W9bPOXpqq30","http://www.troma.com/wp-content/uploads/2011/02/SPACE-ZOMBIE-BINGO_FRONT.jpg"),
            ("Squeeze Play!","https://www.youtube.com/watch?v=aokaxlmnUN0","http://www.troma.com/wp-content/uploads/2011/02/SQUEEZE_PLAY_web.jpg"),
            ("Star Worms II: Attack of the Pleasure Pods","https://www.youtube.com/watch?v=n2FeUml30gU","http://www.troma.com/wp-content/uploads/2011/02/STAR_WORMS_2_web.jpg"),
            ("Strangest Dreams: Invasion of the Space Preachers","https://www.youtube.com/watch?v=-qqTkle1oG4","http://www.troma.com/wp-content/uploads/2011/02/STRANGEST_DREAMS_SPACE_PREACHERS_web.jpg"),
            ("Stuck On You!","https://www.youtube.com/watch?v=Oq6ntwLmWQ0","http://www.troma.com/wp-content/uploads/2011/02/STUCK_ON_YOU_web.jpg"),
            ("Sucker The Vampire","https://www.youtube.com/watch?v=2sCOHEcJ_YU","http://www.troma.com/wp-content/uploads/2011/02/SUCKER_THE_VAMPIRE_web.jpg"),
            ("SUPERSTARLET A D","https://www.youtube.com/watch?v=G_92vkP5YT4","http://www.troma.com/wp-content/uploads/2011/02/superstarlet-a.jpg"),
            ("Surf Nazis Must Die!","https://www.youtube.com/watch?v=qRk9yRdzgyc","http://www.troma.com/wp-content/uploads/2011/02/SURF_NAZIS_MUST_DIE_web.jpg"),
            ("Teenape Vs. The Monster Nazi Apocalypse","https://www.youtube.com/watch?v=KTGEcUBB44A","http://www.troma.com/wp-content/uploads/2012/10/TEENAPE.jpg"),
            ("TERROR FIRMER: The R-Rated Edition","https://www.youtube.com/watch?v=4JmZR7KAAz4","http://www.troma.com/wp-content/uploads/2011/02/TERROR_FIRMER_web.jpg"),
            ("There's Nothing Out There!","https://www.youtube.com/watch?v=jHUFU2gU35I","http://www.troma.com/wp-content/uploads/2011/02/TNOT.jpg"),
            ("They Call Me Macho Woman","https://www.youtube.com/watch?v=jnVtQb0NrgY","http://www.troma.com/wp-content/uploads/2011/02/THEY_CALL_ME_MATCHO_WOMAN_web.jpg"),
            ("Time Barbarians","https://www.youtube.com/watch?v=Y2yzdeLQaAc","http://www.troma.com/wp-content/uploads/2011/02/Time-Barbarians-.jpg"),
            ("Toxic Avenger, The","https://www.youtube.com/watch?v=AIRYFdPBVA8","http://www.troma.com/wp-content/uploads/2011/02/TOXIC_AVENGER_web.jpg"),
            ("Toxic Avenger Part II, The","https://www.youtube.com/watch?v=ewd6ZBKNBLw","http://www.troma.com/wp-content/uploads/2011/02/TOXIC_AVENGER_PART_II_web.jpg"),
            ("Toxic Avenger 3, The","https://www.youtube.com/watch?v=wtro6rR9PzY","http://www.troma.com/wp-content/uploads/2011/02/TOXIC_AVENGER_III_web.jpg"),
            ("Toxic Avenger 4, The","https://www.youtube.com/watch?v=UdsoyObJMgc","http://www.troma.com/wp-content/uploads/2011/02/CITIZEN_TOZIE_COVER.jpg"),
            ("Toxic Crusaders, The Movie","https://www.youtube.com/watch?v=h9iccHm2IVE","http://www.troma.com/wp-content/uploads/2011/02/TCM.jpg"),
            ("Tromas War!","https://www.youtube.com/watch?v=yfDzF2oN7Tc","http://www.troma.com/wp-content/uploads/2011/02/TWAR-poster.jpg"),
            ("Tromeo And Juliet","https://www.youtube.com/watch?v=QI3a_Gc9ddo","http://www.troma.com/wp-content/uploads/2011/02/tromeo_movie.jpg"),
            ("Vegas High Stakes","https://www.youtube.com/watch?v=CrMokG6xtWE","http://www.troma.com/wp-content/uploads/2011/02/VEGAS_HIGH_STAKES_web.jpg"),
            ("Vendetta","https://www.youtube.com/watch?v=mPZ0pCzVBAE","http://www.troma.com/wp-content/uploads/2011/02/Vendetta.jpg"),
            ("Video Demons Do Psychotown","https://www.youtube.com/watch?v=s65WCzwZaYc","http://www.troma.com/wp-content/uploads/2011/03/VIDEO_DEMONS_DO_PSYCHO_TOWN_web.jpg"),
            ("Viewer Discretion Advised","https://www.youtube.com/watch?v=YNMsPHmcLI0","http://www.troma.com/wp-content/uploads/2011/02/VIEWER_DISCRETION_ADVISED_web.jpg"),
            ("Viral Assasins","https://www.youtube.com/watch?v=t-W9TXDOpy0","http://www.troma.com/wp-content/uploads/2011/02/Viral-Assassin.jpg"),
            ("Waitress!","https://www.youtube.com/watch?v=zCEigz8x4eQ","http://www.troma.com/wp-content/uploads/2011/02/WAITRESS_web.jpg"),
            ("Wedding Party, The","https://www.youtube.com/watch?v=TEfHuo2MdKU","http://www.troma.com/wp-content/uploads/2011/02/WEDDING_PARTY_web.jpg"),
            ("When Nature Calls","https://www.youtube.com/watch?v=6m5ydGTauN4","http://www.troma.com/wp-content/uploads/2011/02/WHEN_NATURE_CALLS_web.jpg"),
            ("Where Evil Lives","https://www.youtube.com/watch?v=n0wiVCBVqOM","http://www.troma.com/wp-content/uploads/2011/06/WHERE-EVIL-LIVES-COVER.jpg"),
            ("White Zombie","https://www.youtube.com/watch?v=XbWUKNzcT0s","https://www.tromashop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/w/h/white_zombie.jpg"),
            ("WISEGUYS VS ZOMBIES","https://www.youtube.com/watch?v=V895cCmwcbU","http://www.troma.com/wp-content/uploads/2011/02/wg.jpg"),
            ("Witchcraft 5 : Dance with the Devil","https://www.youtube.com/watch?v=03QfmiI0Q70","http://ia.media-imdb.com/images/M/MV5BMTQ0Mjk4MzU1M15BMl5BanBnXkFtZTgwNDIzNzAxNjE@._V1_.jpg"),
            ("Wizards Of The Demon Sword","https://www.youtube.com/watch?v=HcmCl5esI78","http://www.troma.com/wp-content/uploads/2011/02/WIZARDS_OF_THE_DEMON_SWORD_web.jpg"),
            ("YETI: A GAY LOVE STORY","https://www.youtube.com/watch?v=RKDfkjBjsak","http://www.troma.com/wp-content/uploads/2011/02/yeti-love-story.jpg"),
            ("Zombie Werewolves Attack!","https://www.youtube.com/watch?v=JPrCEiVewyU","http://ia.media-imdb.com/images/M/MV5BMTg1ODE3NjU5MV5BMl5BanBnXkFtZTcwMTM2NTU3OQ@@._V1_.jpg"),
            ("Zombiegeddon","https://www.youtube.com/watch?v=kBjqK7syeU4","http://www.troma.com/wp-content/uploads/2011/02/Zombiegeddon.jpg")
]

# Entry point
exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("M2EgMjIgKCk6IzU1OjEKCTUzIC4zYyAoIjM4LjIyIikjNTU6MgoJMzkgMWQgMjggNTAgWycnLCcyMS40OC4yOS4yYyddOiM1NTozCgkJYiAuMjYgKCkuZSAoJ2YgMzYgM2QgMWMgMWYnLCczYiBmIDQzIDI4IDI0IDQyIDI3IDM0IDJhJykjNTU6NAoJCTI1IDJkICM1NTo1CgkwID01MyAuNDkgKCkjNTU6NwoJMzkgMCAuMWEgKCI0ZCIpNTEgMmYgOiM1NTo5CgkJMWIgKDAgKSM1NToxMAoJMzIgOiM1NToxMQoJCTUyID0wIC4xYSAoIjRkIikjNTU6MTIKCQk1NCA9MCAuMWEgKCIzMSIpIzU1OjEzCgkJNTcgPTQ1ICgyMyAuZCAoNTIgKSkjNTU6MTQKCQk2ID0zNSAuNGIgKCI4LjJiIikjNTU6MTUKCQk0ZiA9YiAuOCAoNTQgLDQ2ID0iNGUuNDAiLGEgPTYgKSM1NToxNgoJCTRmIC4xZSAoJzQ4Jyx7JzJlJzo1NCB9KSM1NToxNwoJCTRmIC40YyAoIjQ3IiwiMzciKSM1NToxOAoJCTRmIC40NCAoNDEgKDU3ICkpIzU1OjE5CgkJNGEgLmMgKDNmICgzZSAuMzAgWzEgXSksMzMgLDRmICkjNTU6MjAKCTUzIC41NiAoKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"O0OOOOOO00OO000OO|1|2|3|4|5|O00O0O0OOOO00OO0O|7|ListItem|9|thumbnailImage|xbmcgui|setResolvedUrl|unquote_plus|notification|please|10|11|12|13|14|15|16|17|18|19|get|main_list|original|addonID|setInfo|credits|20|plugin|run|urllib|change|return|Dialog|rename|not|xvbmc|addon|Thumb|troma|False|Title|None|argv|name|else|True|this|xbmc|keep|true|docu|if|def|and|log|the|sys|int|png|str|or|do|setPath|resolveYT|iconImage|IsPlayable|video|get_params|xbmcplugin|getInfoImage|setProperty|action|DefaultVideo|OO0O00OO00OOOOO00|in|is|O0OOO0O0O00OOOO0O|plugintools|OOOO00000O000O000|line|close_item_list|OO00OOOOOOO00OOO0".split("|")))


# Resolve
exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("OCA0KDcpOgoJNiA9IDAuMig3KQoJMSA9IDYuMygpCgk1IDE=")))(lambda a,b:b[int("0x"+a.group(1),16)],"YDStreamExtractor|videourl|getVideoInfo|streamURL|resolveYT|return|vid|url|def".split("|")))


# Main menu
exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MjYgMSg2KToKCTJjLjI1KCIyMS4xICIrMjIoNikpCgkyYiAxMCAxNSAyMyBbJycsICcxNi4zLjFkLjFiJ106CgkJZi4xOSgpLjQoJzInLCcxMiAyYSAxNSAxNCAyMCAxYSAyOSAxZSAyNCBlJykKCQkxMyA4CgkyNyBkLCAzLCAxMSAyMyBhOgoJCTcgPSA3ID0gMjguMWZbMF0gKyAiPzU9IiArIDE4LjkoMykKCQkyYy5jKCAKCQkJIzU9IiIsIAoJCQkxYz1kLAoJCQk3PTcsCgkJCWI9MTEsCgkJCTE3PTggKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|main_list|playback_limited|video|notification|action|params|url|False|quote_plus|tromavids|thumbnail|add_item|name|credits|xbmcgui|addonID|img|please|return|change|not|plugin|folder|urllib|Dialog|addon|troma|title|xvbmc|keep|argv|this|docu|repr|in|the|log|def|for|sys|and|do|if|plugintools".split("|")))


# Exec
exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MCgp")))(lambda a,b:b[int("0x"+a.group(1),16)],"run".split("|")))
