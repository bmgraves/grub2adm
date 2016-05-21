#!/bin/bash

CONFIG_DIR="CONFIG"
BASE_DIR=`pwd`
BLESS_DIR="blessings-1.6"
PASSLIB_DIR="passlib-1.6.5"
NAME="grub2adm"
BASE_PY="$NAME.py"
INST_PATH="/usr/sbin"
USERS="/etc/grub.d/01_users"
USER_TEMP="users.template"
DATE=$( date +'%Y%m%d' )


# check privledges
if [ "$(whoami)" != "root" ];then
	echo "Please Run with Elevated Privledges"
	exit
fi
	
# Begin actual configuration
cd $CONFIG_DIR

# Install Blessings
echo "---------"
echo "Installing required python modules:"
echo "---------"

# install blessings
cd $BLESS_DIR
python setup.py install

# Install bcrypt
cd ..
cd $PASSLIB_DIR
python setup.py install

# Return to config
cd $CONFIG_DIR


# return to base Directory
cd $BASE_DIR
echo "---------"
echo "Installing $NAME to: $INST_PATH/$NAME"
echo "---------"
cp $BASE_PY $INST_PATH/$NAME
chown root $INST_PATH/$NAME

echo "COMPLETE"

echo "---------"
echo "Backing up old config file: $USERS"
echo "---------"
mkdir $BASE_DIR/backups
mv $USERS $BASE_DIR/backups/01_users.bak-$DATE
echo "COMPLETE"

echo "---------"
echo "Copying Users template to: $USERS"
echo "---------"
cp $CONFIG_DIR/$USER_TEMP $USERS
echo "COMPLETE"
