#!/bin/bash
mkdir /Videos
mkdir /opt/scarepi
mkdir /opt/scarepi/bin
mkdir /opt/scarepi/Playlists
mkdir /opt/scarepi/Options
mkdir /opt/scarepi/Trigger
mkdir /opt/scarepi/Playlists/Default
echo "HDMI" > /opt/scarepi/Options/sound
echo "loop" > /opt/scarepi/Options/playmode
echo "Default" > /opt/scarepi/Options/playlist

chown -R scarepi:www-data /opt/scarepi
chmod -R 770 /opt/scarepi
