#!/bin/python

# Author  : Brandon M. Graves
# Created : 20JAN2016
# Modified: 22JAN2016
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
import sys
import platform
from blessings import Terminal
from subprocess import call
# CONFIG:
###########
# Location of your grub2 files
BOOT_PATH = "/boot/grub2/"
GRUB_CFG = BOOT_PATH + "/grub.cfg"
GRUB_ENV = BOOT_PATH + "/grubenv"
VERSION = ".01a"



# Functions go here
#########################################
def show_version():
	print "grub2adm, VERSION: " + VERSION + ", http://metashell.net"
	print "PROJECT: https://github.com/bmgraves/grub2adm"
	print "AUTHOR: Brandon M. Graves"

# CHECK_INT():
#  Simple check to see if something is an integer or string.
def check_int(x):
	try:
		int(x)
		return True
	except ValueError:
		return False
# GET_DEFAULT()
# Gets the currently set default boot option.
def get_default():
	x = re.compile('^saved_entry')
	for line in open(GRUB_ENV):
		if x.match(line):
			return line.split('=')[1].rstrip('\n')

def get_current():
	return platform.release()	
	


# LIST_MENU(): 
#  This function is intended to get a list of all bootable kernels currently known by grub2
#  and display them in a sane way that can be used by the rest of the application to handle
#  boot options.
# "args = 0" is a sanity check to avoid complicated logic in  the program start, since other
# options other than "list" require arguments.
def list_menu(args = 0):
	# Note: This is currentingly Work In Progress
	items = get_menu()
	t = Terminal()
	print "---------------"
	print "Grub2 Boot Menu:"
	print "Current Kernel: " + t.red(get_current())
	print "Default Option: " + t.green(get_default())
	print "---------------"
	for line in items:
		if items.index(line) < 10:
			pad = 3
		else:
			pad = 2
			
		if line == get_default():
			print t.green("{") + t.red(str(items.index(line))) + t.green("}".ljust(pad) + line)
			
		else:
			print "[" + t.red(str(items.index(line))) + "]".ljust(pad) + line


	print "---------------"


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
# This will formatt out the undesirable parts of the menu display, and try to get just the description line that
# grub2 cares about for its config purposes.
def create_menu(menu_in):
	x = []
	for line in menu_in:
		x.append(line.split('\'')[1]) 
	return x
		

############################
# SET_DEFAULT():
# This checks to see if the entry is a numerical value, or string, if numerical
# it looks up the numerical entry based on the "get_menu" action, and uses
# that entry as the choice. It then will try and set the default boot option.
# it will then change the default boot option using grub2's "grub2-set-default" command
def set_default(args):
	x = args.string
	t = Terminal()
	if check_int(x):
		tmp = get_menu()
		#if (x <= (len(tmp) - 1)):
		if (int(x) <= (len(tmp) - 1)):
			choice = tmp[int(x)]
		else:
			print "[" + t.red("FAILURE") + "] Option Not Found" 
			return

	else:
		choice = x
	
	if choice in get_menu():
		call(['grub2-set-default', choice])
		print "[" + t.green("SUCCESS") + "] " + t.green(choice) 
			
	else:
		print "[" + t.red("FAILURE") + "] Option Not Found: " 
		print t.red(choice) 
		return
	
		

# END FUNCTIONS

# PARSER CONFIG. 
# This is the basic Parser config area.
parser = argparse.ArgumentParser(description='A better way to Grub2')
parser.add_argument('-v','--version', help='Display Version information', action='version', version='%(prog)s VERSION: ' + str(VERSION))
subparsers = parser.add_subparsers(title='Available Commands')
###

# LIST:
# Parser for the "list" option
parser_list = subparsers.add_parser('list', help='list available boot options')
parser_list.set_defaults(func=list_menu)
###

# SET-DEFAULT
# Parser for the "set-default" option.
parser_set_default = subparsers.add_parser('set-default', help='set default boot option')
parser_set_default.add_argument('<boot selection>', help='This can be either the numerical value listed in "grub2adm list" or the full string value of the boot option.')
parser_set_default.set_defaults(func=set_default)
###

# END PARSER CONFIG

# Begin program:  This is some basic start program logic,
# Likely nothing should go wrong below this line.
if len(sys.argv)==1:
	parser.print_usage()
	sys.exit(1)

args = parser.parse_args()
args.func(args)
