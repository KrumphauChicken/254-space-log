#Upal Patel 
import re

def find_planet_names(content:str):
	pattern = re.compile("\"BodyName\":\"[-\w+\s\d+]+")
	planetResult = pattern.findall(content)
	return planetResult

