import re

def get_total_fuel(content:str) -> float:
	pattern = re.compile("\"FuelUsed\":(\d+\.\d+)")
	result = pattern.findall(content)
	fuel = 0
	if result:
		for r in result:
			fuel+=float(r)
	return fuel
