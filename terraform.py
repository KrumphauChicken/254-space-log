import re

def get_total_terraformable_planets(content:str):
	pattern = re.compile("\"TerraformState\":\"Terraformable\"")
	result = pattern.findall(content)
	count = len(result)
	return count
