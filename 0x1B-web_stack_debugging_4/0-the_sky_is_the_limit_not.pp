#This script increases number of worker_processes
exec { 'increase nginx worker processes':
  command => "sed -i 's/worker_processes 5;/worker_processes 8;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
  }
