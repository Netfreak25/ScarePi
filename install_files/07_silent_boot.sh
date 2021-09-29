#!/bin/bash
echo hide raspberry pi icons
sudo sed -i "1 s|$| logo.nologo quiet|" /boot/cmdline.txt

#echo hide boot messages
#sudo sed -i "1 s|$| quiet splash|" /boot/cmdline.txt

echo disable login prompt
sudo systemctl disable getty@tty1.service

echo hide blinking cursor
sudo sed -i "1 s|$| vt.global_cursor_default=0|" /boot/cmdline.txt

echo hide undervoltage message
sudo sed -i "1 s|$| loglevel=1|" /boot/cmdline.txt

echo hide undervoltage lightning bolt icon
sudo echo "" >> /boot/config.txt
sudo echo "avoid_warnings=1" >> /boot/config.txt

echo hide splash
sudo echo "" >> /boot/config.txt
sudo echo "disable_splash=1" >> /boot/config.txt

echo move messages to tty3
sudo sed -i 's/console=tty1/console=tty3/g' /boot/cmdline.txt

echo hide splash
sudo echo "" >> /boot/config.txt
sudo echo "gpu_mem=256" >> /boot/config.txt
echo "hide login"
sudo systemctl disable getty@tty1.service
