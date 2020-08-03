# execute command

exec { 'pkill -f killmenow':
  path => '/usr/bin/'
}
