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
import argparse

# Parser config
parser = argparse.ArgumentParser(prog='grub2adm', description='A better way to Grub2')
# Primary Commands
subparsers = parser.add_subparsers(title='Available Commands')

parser_list = subparsers.add_parser('list', help='list available boot options')
parser_list.set_defaults(func=list)

#parser_set_default = subparsers.add_parser('set-default', help='set default boot option')
#parser_set_default.add_argument('string')
#parser_set_default.set_defaults(func=setd)

## /Primary Commands



# functions for work
def list():
        print "hit list"

#def setd(args):
#       print "hit set defaults " + args.string



#Begin program
args = parser.parse_args()
args.func(args)
