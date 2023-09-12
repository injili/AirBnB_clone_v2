#!/usr/bin/env bash
# A bash script that prepares the web servers for the deployment of web_static

# install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# create folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create the test html file
sudo sh -c "echo '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
' > /data/web_static/releases/test/index.html"

# create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# giving ownership of the /data/ folder to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data

# updating the Nginx configuration to serve the content to hbnb_static
sudo tee /etc/nginx/sites-available/default << EOF
server {
	listen 80;
	listen [::]:80 default_server;

	server_name _;

	location /hbnb_static/ {
                alias /data/web_static/current/;
        }

	location /redirect_me/ {
		return 301 https://github/injili;
	}

	root /var/www/html;
	index index.html index.htm;

	error_page 404 /custom_404.html;
	location = /custom_404.html {
		internal;
		return 404 "Ceci n'est pas une page\n";
	}

	location / {
		try_files \$uri \$uri/ =404;
	}
}
EOF

# restart nginx
sudo service nginx restart
