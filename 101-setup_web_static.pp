# Puppet manifest to prepare web server

# Install Nginx package
package { 'nginx':
	ensure => installed,
}

# Configure the fake html file
file{ '/data/web_static/releases/test/index.html':
	ensure  => file,
	content => "The difference between a saint and a sinner is a good reason",
	require => Package['nginx'],
}

file_line { '/etc/nginx/sites_available/default':
	line       => '
	localhost /hbnb_static/ {
		alias /data/web_static/current/;
	}
',
	match      => '.*',
	line_match => '^.{34}$',
}
