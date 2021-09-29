#!/bin/bash
echo "creating user"
yes scarepi | adduser --gecos "" scarepi

echo
echo "creating samba config"
echo "[global]
workgroup = SCARE"$((1 + $RANDOM % 10000)) > /etc/samba/smb.conf
echo "security = user
encrypt passwords = yes
client min protocol = SMB2
client max protocol = SMB3

[ScarePi]
comment = ScarePi-Videos
path = /Videos
read only = no

" >> /etc/samba/smb.conf


echo
echo "creating samba password for user scarepi"
yes scarepi | smbpasswd -a scarepi


echo
echo "Restarting Samba"
sudo service smbd restart
sudo service nmbd restart
