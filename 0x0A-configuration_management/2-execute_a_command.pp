#kill process
exec { 'Terminator':
command  => '/usr/bin/pkill -f killmenow'
}
