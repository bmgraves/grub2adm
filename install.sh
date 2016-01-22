#!/bin/bash

CONFIG_DIR="CONFIG"
BASE_DIR=`pwd`
BLESS_DIR="blessings-1.6/"


# check privledges
if [ "$(whoami)" != "root" ];then
	echo "Please Run with Elevated Privledges"
	exit
fi
	
# Begin actual configuration
cd $CONFIG_DIR

# Install Blessings
cd $BLESS_DIR
python setup.py install

# Return to config
cd $CONFIG_DIR


# return to base Directory
cd $BASE_DIR
