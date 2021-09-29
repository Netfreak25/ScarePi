#!/bin/bash
cd install_files
chmod +x *
echo "Installing ScarePi"

sudo ./01_install_software.sh
sudo ./02_apache_config.sh
sudo ./03_set_hostname.sh
sudo ./04_config_backup.sh
sudo ./05_configure_samba.sh
sudo ./06_create_directorys.sh
sudo ./07_silent_boot.sh
sudo ./08_install_scarepi.sh
sudo ./09_autostart_scarepi.sh
