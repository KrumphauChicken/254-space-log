#!/usr/bin/env python3
#
# Use like `./space_log.py -s|-p|-t|-d|-f log_file

from sys import argv

import fuel, re, planets, terraform, systems

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
	'-s': systems.find_system_names, # NAMES OF SYSTEMS VISITED
	'-p': planets.find_planet_names, #NAMES OF PLANETS SCANNED
	'-t': terraform.amount_terraformable_planets #TOTAL NUMBER OF TERRAFORMABLE PLANETS SCANNED
#	'-d': TOTAL DISTANCE IN LIGHT YEARS
#	'-f': fuel.get_total_fuel,	# The example.
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
