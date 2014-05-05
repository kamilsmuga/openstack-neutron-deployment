grep eth3 /etc/network/interfaces
rc=$?
if [[ $rc != 0 ]] ; then
	echo -e "auto eth3 \niface eth3 inet manual \n\t\tup ip link set dev \$IFACE up \n\t\tdown ip link set dev \$IFACE down" >> /etc/network/interfaces
	/etc/init.d/networking restart
fi
