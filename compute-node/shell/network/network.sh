route -n | grep 10.0.0.1
rc=$?
if [[ $rc != 0 ]] ; then
	route add default gw 10.0.0.1 eth1
fi


