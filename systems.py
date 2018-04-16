import re

def get_system_names(content:str):
	pattern = re.compile("\"event\":\"FSDJump\", \"StarSystem\":\"(.*?)\"")
	result = pattern.findall(content)
	return result

def total_jump_distance(content:str):
	pattern = re.compile("\"event\":\"FSDJump\",.*\"JumpDist\":([\d\.]+)")
	result = pattern.findall(content)
	distance = 0
	for n in result:
		distance += float(n)
	return distance
