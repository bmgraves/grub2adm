# Description
grub2adm is intended to be a single script that simplifies and streamlines the usage and administration of grub2.
When dealing with grub2 currently there are several different commands that must be used, and a few things involved
in the use of grub2 are not readily apparent. It is the intention of this program to allow users to manage their
grub2 boot options in a simple and pain free way.

NOTE: Latest Roadmap Will always be listed under the "alpha" branch. To check feature status, please look under that
      readme.

# STATUS
Current version is limited, but ready for use. Master version is currently the beta version, New features
will be tested and developed on the alpha version, before being pushed up for usage tests.

# Installation and usage
With elevated privledges run the "install.sh" script, this will install all the necessary files.
the default install location for the command is "/usr/sbin" this is changable within the install.sh script.

Currently there are two working features that can be used:

grub2adm list - Lists all the currently known boot options.
grub2adm set-default - This can be used with either a "string" value, or a numerical value as found in the "list" option.

# Roadmap
- (COMPLETE)  Get working Argument parsing.                 
- (COMPLETE)  List available boot options in intelligent way.
- (COMPLETE)  Ability to set-default boot options
- (COMPLETE)  List-boot Options
- (IN-PROG)   Manage grub2 users
- (IN-PROG)   Set grub2 Password
- (PENDING)   Set Boot Options
- (PENDING)   Set grub2 password for individual menu items
- (PENDING)   Add "-f|--force" option to "set-default" to allow unknown kernel option to be set as default.
- (PENDING)   Create "add" function for adding custom menu entries.


# Tested on:
- (COMPLETE)  CentOS: 7
- (PENDING)   Ubuntu <Any Version>

# Include
The following projects are included in this project, big thanks to them for their contributions to the open source world,
because without their projects this one would not work nearly as well!

- Blessings 1.6 : Python Module: https://pypi.python.org/pypi/blessings/ (Copyright (c) 2011 Erik Rose)
