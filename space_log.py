#!/usr/bin/env python3
#
# Use like `./space_log.py -s|-p|-t|-d|-f log_file

from sys import argv
import fuel, re, planet_list

# Opens the log file and grabs the contents.
try:
	fh = open(argv[1], 'r')
	content = fh.read()
	fh.close()
except IndexError:
	exit("Missing name of log file.")
except:
	exit("Couldn't open file \""+argv[1]+"\".")

<<<<<<< HEAD
# Uncomment and your work in the appropriate spots.        
=======
# Uncomment, and add your work in the appropriate spots.
>>>>>>> ebae6177a9bfcac6f1a7cfb355198ae01b57c24f
argSwitcher = {
	'-s': planet_list.Names_of_system_visted, #NAMES OF SYSTEMS VISITED        
#	'-p': NAMES OF PLANETS SCANNED
#	'-t': TOTAL NUMBER OF TERRAFORMABLE PLANETS SCANNED
#	'-d': TOTAL DISTANCE IN LIGHT YEARS
	'-f': fuel.get_total_fuel,	# The example.
}

try:
	func = argSwitcher.get(argv[2], lambda x: "Incorrect search argument.")
except IndexError:
	exit("Missing search argument.")

<<<<<<< HEAD
print(func(content))    

=======
output = func(content)
if type(output) is list:
	for l in output:
		print(l)
else:
	print(output)
>>>>>>> ebae6177a9bfcac6f1a7cfb355198ae01b57c24f
