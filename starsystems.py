import re

def print_starsystems(content:str) -> str:
	pattern = re.compile("\"StarSystem\":\"(.+?)\"")
	result = pattern.findall(content)
	list = []

	if result:
		for r in result:
			list.append(r)
	return list
