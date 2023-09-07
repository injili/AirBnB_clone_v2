#!/usr/bin/env bash
# A bash script that prepares the web servers for the deployment of web_static

# install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# create folders
[ ! -d "/data" ] && mkdir /data
[ ! -d "/data/web_static" ] && mkdir /data/web_static
[ ! -d "/data/web_static/releases" ] && mkdir /data/web_static/releases
[ ! -d "/data/web_static/releases/test" ] && mkdir /data/web_static/releases/test

[ ! -d "/data/web_static/shared" ] && mkdir /data/web_static/shared

# create the test html file
sudo sh -c "echo '
<!DOCTYPE HTML>
<html>
        <head>
		<meta charset='UTF-8'>
                <title>FakeHTMLFile</title>
        </head>
        <body>
                <p>The difference between a saint and a sinner is a good reason</p>
        </body>
</html>
' >> /data/web_static/releases/test/index.html"

#create symbolic link
