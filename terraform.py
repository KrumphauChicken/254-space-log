#Mitchell Norseth
import re

def amount_terraformable_planets(content:str):
	pattern = re.compile("\"Terraformable\"[-\w+\s\d+]+")
	planetResult = pattern.findall(content)
	return len(planetResult)