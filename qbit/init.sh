#!/usr/bin/bash

groupadd -g 1002 tarrshares
useradd tarr -u1002 -g1002 -d/home/tarr -s/bin/bash 
