#Tyler Danh

import re

def get_total_terraformable_planets(content:str):
	pattern = re.compile("\"TerrformState\":\"Terraformable\"")
	result = pattern.findall(content)
	count = len(result)
	
	return count
