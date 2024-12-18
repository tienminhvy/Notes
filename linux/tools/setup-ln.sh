#!/bin/bash

if [ -z $1 ] || [ -z $2 ]; then
	echo "FATAL: This script needs atleast 2 parameters";
	exit 1;
fi

DIR=$PWD;

cd /usr/local/bin;
sudo ln -s $DIR/$1 $2;
