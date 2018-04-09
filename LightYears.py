#Total Light Years
import re

def get_total_light_years(content:str) -> float:
	pattern = re.compile("\"JumpDist\":(\d+\.\d+)")
	result = pattern.findall(content)
	dist = 0
	if result:
		for r in result:
			dist+=float(r)
	return dist
