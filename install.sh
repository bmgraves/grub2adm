#!/bin/bash

CONFIG_DIR="CONFIG"
BASE_DIR=`pwd`
BLESS_DIR="blessings-1.6"
NAME="grub2adm"
BASE_PY="$NAME.py"
INST_PATH="/usr/sbin"


# check privledges
if [ "$(whoami)" != "root" ];then
	echo "Please Run with Elevated Privledges"
	exit
fi
	
# Begin actual configuration
cd $CONFIG_DIR

# Install Blessings
cd $BLESS_DIR
echo "---------"
echo "Installing required python modules:"
echo "---------"

python setup.py install

# Return to config
cd $CONFIG_DIR


# return to base Directory
cd $BASE_DIR
echo "---------"
echo "Installing $NAME to: $INST_PATH/$NAME"
echo "---------"
cp $BASE_PY $INST_PATH/$NAME
