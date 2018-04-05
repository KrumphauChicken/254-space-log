# part 3  Print the total number of terraformable planets
#Tenzin Dorjee

import re

def get_planet_name(content:str) -> float:
	pattern = re.compile("\"FuelUsed\":(\d+\.\d+)")
	result = pattern.findall(content)
	fuel = 0
	if result:
		for r in result:
			fuel+=float(r)
	return fuel
