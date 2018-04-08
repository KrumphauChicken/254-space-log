# Andrew Nomura

import re

def get_star_systems(content:str):
	pattern = re.compile("\"StarSystem\":\"\w+")
	result = pattern.findall(content)
	stars = 0

	return result
