#!/bin/bash
export username="tarr"
export groupname="tarrshares"
export tarrid=1002
export tarrhome="/home/tarr"
export tarrdata="$tarrhome/docker/data"
export tarrconf="$tarrhome/docker/appconfig"
echo $tarrdata
echo $tarrconf
sudo groupadd -g $tarrid $groupname
sudo useradd -m -d $tarrhome $tarrid -g $tarrid $username
