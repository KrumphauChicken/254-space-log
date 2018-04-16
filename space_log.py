#!/usr/bin/env python3
#
# Use like `./space_log.py -s|-p|-t|-d|-f log_file

from sys import argv
import fuel
from systems import *
from planets import *

# Opens the log file and grabs the contents.
try:
	fh = open(argv[1], 'r')
	content = fh.read()
	fh.close()
except IndexError:
	exit("Missing name of log file.")
except:
	exit("Couldn't open file \""+argv[1]+"\".")

# Uncomment, and add your work in the appropriate spots.
argSwitcher = {
	'-s': get_system_names,
	'-p': get_planet_names,
	'-t': total_terraformable,
	'-d': total_jump_distance,
	'-f': fuel.get_total_fuel,	# The example.
}

try:
	func = argSwitcher.get(argv[2], lambda x: "Incorrect search argument.")
except IndexError:
	exit("Missing search argument.")

output = func(content)
if type(output) is list:
	for l in output:
		print(l)
else:
	print(output)
