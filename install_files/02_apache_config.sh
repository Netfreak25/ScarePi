#!/bin/bash
#mv /var/www/html/index.html /var/www/html/default.html
cp -rvf files/apache_config/000-default.conf /etc/apache2/sites-available/

cp -rvf files/www/* /var/www/html/
chown -R www-data:www-data /var/www/html/*
chmod +x /var/www/html/*.cgi

rm /var/www/html/index.html

a2enmod cgi
echo "restaring apache2 now"
systemctl restart apache2
