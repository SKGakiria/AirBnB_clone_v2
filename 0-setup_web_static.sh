#!/usr/bin/env bash
# Script sets up the web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
     <p>Nginx test</p>
  </body>
</html>" | tee /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
service nginx restart
