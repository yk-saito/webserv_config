#!/bin/bash

# fcgiwrap
/etc/init.d/fcgiwrap start

# nginx
echo "daemon off;" >> /etc/nginx/nginx.conf
/usr/sbin/nginx