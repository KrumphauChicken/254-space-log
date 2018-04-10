#Mitchell Norseth
import re

def amount_terraformable_planets(content:str):
	pattern = re.compile("\"Terraformable\"")
	planetResult = pattern.findall(content)
	return len(planetResult)
