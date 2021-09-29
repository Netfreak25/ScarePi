#!/bin/bash
echo updating repository
sudo apt update

echo installing software
sudo apt-get --assume-yes install omxplayer screen apache2
sudo apt-get --assume-yes install samba samba-common smbclient
sudo apt-get --assume-yes install pigpio
sudo systemctl start pigpiod
sudo systemctl enable pigpiod
