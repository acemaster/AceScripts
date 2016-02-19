#!/bin/bash
i="1"
while [ $i ]
do
cmd=$(ifconfig | grep "inet addr"| tr -s ' '| cut -d ' ' -f 3 | grep '172.*')
if [[ -z $cmd ]]; then
	#sudo dhclient -r eth0
	#sudo dhclient eth0
	echo "Found"
else
	echo "It is fixed"
	break
fi
done
