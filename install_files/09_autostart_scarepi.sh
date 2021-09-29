#!/bin/bash
echo adding scarepi to autostart

sed -i '$ d' /etc/rc.local
echo "screen -d -m -S ScarePi /opt/scarepi/bin/scarepi.sh  &" >> /etc/rc.local
echo "exit 0" >> /etc/rc.local
echo
echo
echo "restarting in 60 seconds to complete the installation"
sleep 60
reboot