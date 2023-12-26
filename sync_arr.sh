#!/bin/bash

server="pi.controller.desktop"
HOSTPATH="${RADARR}"
user="nabil"
destination="/home/$user/media"
doRsync () {
   eval "echo 'copying $HOSTPATH to $server @ location $destination @ with username $user'"
   rsync -azP $HOSTPATH $user@$server:$destination
   rc=$?
   return 0
}

if ! [ -d $HOSTPATH ]; then 
	echo "failure finding path"
	exit 1
fi

if  nc -z $server 22 2>/dev/null; then
   echo "$server reachable"
   commit=$(doRsync)
   echo "return code $commit"
   exit 0
else
   echo "not working"
   exit 1
fi
