#Bryan Ho 
#CPSC 254

import re

def get_total_terraformable(content:str) -> int:
	pattern = re.compile("\"BodyName\":(\"(.*?)\")")
	result = pattern.findall(content)
	total = 0
	if result:
		for r in result:
			total+=1
	return total