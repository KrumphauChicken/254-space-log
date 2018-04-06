# THomas Brenner 
import re
def names_of_planets(content:str):
		pattern = re.compile("\"BodyName\":\"[A-Za-z0-9 -]+")
		result = pattern.findall(content)
		
		return result
