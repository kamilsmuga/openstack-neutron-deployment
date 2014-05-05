host { 'localhost':
    ensure => "absent",
}
host { 'precise64':
    ensure => "absent",
}
host { 'ip6-localhost':
    ensure => "absent",
}
host { 'ip6-localnet':
    ensure => "absent",
}
host { 'ip6-mcastprefix':
    ensure => "absent",
}
host { 'ip6-allnodes':
    ensure => "absent",
}
host { 'ip6-allrouters':
    ensure => "absent",
}
host { 'controller':
    ip => '10.0.0.11',
}
host { 'network':
    ip => '10.0.0.21',
}
host { 'compute1':
    ip => '10.0.0.31',
}
