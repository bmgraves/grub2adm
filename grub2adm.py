#!/bin/python

# Author  : Brandon M. Graves
# Created : 20JAN2016
# Modified: 20JAN2016
#############################################################################
# COPYRIGHT (C) 2016, Brandon M. Graves, http://metashell.net
#
# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################
# IMPORTS:
###########
import argparse
import re

# CONFIG:
###########
# Location of your grub2 files
BOOT_PATH = "/boot/grub2/"
GRUB_CFG = BOOT_PATH + "/grub.cfg"

# Functions go here
#########################################

# LIST_MENU(): 
#  This function is intended to get a list of all bootable kernels currently known by grub2
#  and display them in a sane way that can be used by the rest of the application to handle
#  boot options.
def list_menu(args = 0):
	# Note: This is currentingly Work In Progress
	for line in get_menu():
		print line


# GET_MENU():
# This command is based on the fedoraprojects method of "grep -P "submenu|^menuentry" /boot/grub2/grub.cfg | cut -d "'" -f2"
# to list menu items.
# Check the GRUB_CFG file for lines containing the regex held in the "search" List
# Then send the results to "create_menu" to process them
def get_menu():
	search = []
	search.append(re.compile('^menuentry'))
	search.append(re.compile('submenu'))
	tmp = []
	for line in open(GRUB_CFG):
		if any(x.match(line) for x in search):
			tmp.append(line)
	return create_menu(tmp)

# CREATE_MENU():
#  This will formatt out the undesirable parts of the menu display, and try to get just the description line that
#  grub2 cares about for its config purposes.
def create_menu(menu_in):
	x = []
	for line in menu_in:
		x.append(line.split('\'')[1]) 
	return x
		

############################
def set_default(args):
        print "hit set defaults " + args.string

# /Functions

# Parser config
parser = argparse.ArgumentParser(description='A better way to Grub2')

# Primary Commands
subparsers = parser.add_subparsers(title='Available Commands')

parser_list = subparsers.add_parser('list', help='list available boot options')
parser_list.set_defaults(func=list_menu)

parser_set_default = subparsers.add_parser('set-default', help='set default boot option')
parser_set_default.add_argument('string')
parser_set_default.set_defaults(func=set_default)

## /Primary Commands




#Begin program
args = parser.parse_args()
args.func(args)
