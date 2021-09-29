#!/bin/bash
cp -rvf files/bin/* /opt/scarepi/bin/
chmod +x /opt/scarepi/bin/*

chown -R scarepi:www-data /opt/scarepi
chmod -R 770 /opt/scarepi

echo
echo "changing Video directory permissions"
chown -R scarepi:www-data /Videos
