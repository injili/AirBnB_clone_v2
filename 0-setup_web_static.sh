#!/usr/bin/env bash
# A bash script that prepares the web servers for the deployment of web_static

# install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# create folders
sudo mkdir -P /data/web_static/releases/test /data/web_static/shared

# create the test html file
sudo sh -c "echo '
The difference between a saint and a sinner is a good reason
' >> /data/web_static/releases/test/index.html"

# create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# giving ownership of the /data/ folder to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data

# updating the Nginx configuration to serve the content to hbnb_static
STATIC_WEB="\\
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
"

sudo sed -i "35i $STATIC_WEB" /etc/nginx/sites_available/default

# restart Nginx
sudo service nginx restart
