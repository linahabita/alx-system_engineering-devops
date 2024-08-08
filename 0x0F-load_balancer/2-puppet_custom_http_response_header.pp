# 2-puppet_custom_http_response_header.pp

exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure => 'present',
} ->

file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => 'http {\\n\\tadd_header X-Served-By "$hostname";',
  match => 'http {',
} ->

exec { 'start_nginx':
  command => '/usr/sbin/service nginx start',
}

