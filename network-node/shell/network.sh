grep "up ip link set dev $IFACE up" /etc/network/interfaces
rc=$?
if [[ $rc != 0 ]] ; then
	/usr/bin/perl -p -i -e "s/iface eth3 inet static/iface eth3 inet manual/g" /etc/network/interfaces
	/usr/bin/perl -p -i -e "s/address 10.0.2.21/up ip link set dev \\\$IFACE up \n\tdown ip link set dev \\\$IFACE down/g" /etc/network/interfaces
	/etc/init.d/networking restart
fi
