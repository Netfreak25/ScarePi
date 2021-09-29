# ScarePi
ScarePi is a console media player designed to play AtmosFX Sprites.

- This is a work in progress and has been created very quickly.
- In my opinion the code is quite ugly, but it works
- Keep errors or report them once you find one

## Test Evironment
- This has been tested on Raspberry Pi OS Lite 10.9
- This has been tested on a Raspberry Pi 3 Model A+

## Features
- Media Player
- Web Interface
- Browse and delete Files in the /Videos folder 
- File upload is possible through Samba or Web
- Creating or Deleting Playlists
- Active Playlist can be choosed
- 3,5mm Jack or HDMI Sound is supported
- Videos can be either played in a loop or get triggered
- At the Moment the Video can be triggered with a web hook (See FAQ)
- Silent Boot 
 


## Installation
#### 1) Install a fresh Raspberry Pi OS Lite 10.9
1) To Flash the Pi with the Image use Raspberry Pi Imager, or whatever you want
2) Make sure you are using a "Lite" Image without Desktop Environment
#### 2) Enable ssh
1) Copy the "ssh" file from the boot folder to the boot partition on your sd
#### 3) Configure you WiFi
1) Copy the "wpa_supplicant.conf" file from the boot folder to the boot partition on your sd
2) Modify the file to your needs
#### 4) Boot the Raspberry
#### 5) Login with the user "pi" and password "raspberry"
#### 6) Modify the "pi" User password
Use passwd to change the password
```
passwd
```
#### 7) Install ScarePi
```
sudo apt install git -y
git clone https://github.com/Netfreak25/ScarePi.git
cd ScarePi
/usr/bin/bash install.sh
```
#### 8) Change Hostname (optional)
1) Change the Hostname if wanted
```
echo "Your-new-Hostname" > /etc/hostname
```
2) Change the Samba Password (Windows File Share) if wanted, but take care of escaping 
```
yes "yournewpassword" | smbpasswd -a scarepi
```

## FAQ
#### 1) How can I trigger the Videos?
You need to call the url!
```
http://192.168.0.10/index.cgi?trigger=true
```
Use wget, your browser, or whatever you want
```
wget http://192.168.0.10/index.cgi?trigger=true
```
#### 2) What is the Trigger for?
- If you use Home-Automation you can call this url when a Event occurs, on for example a "Motion Sensor"
- I am using it in combination with IOBroker. As soon as a Motion Sensors gets triggered the URL gets called and the Playback starts
