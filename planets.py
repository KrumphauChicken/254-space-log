import re

def get_planet_names(content:str):
	pattern = re.compile("\"event\":\"Scan\", \"BodyName\":\"(.*?)\".*?(?=PlanetClass)")
	result = pattern.findall(content)
	return result

def total_terraformable(content:str):
	pattern = re.compile("\"event\":\"Scan\".+\"TerraformState\":\"Terraformable\"")
	return len(pattern.findall(content))
