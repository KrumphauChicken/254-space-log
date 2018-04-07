# Created by Gary Kam
import re

def get_total_light_years(content:str) -> float:
	pattern = re.compile("\"JumpDist\":(\d+\.\d+)")
	result = pattern.findall(content)
	light_years = 0
	if result:
		for r in result:
			light_years += float(r)
	return light_years
