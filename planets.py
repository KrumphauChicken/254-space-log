import re

def get_planet_names(content:str) -> list:
        pattern = re.compile("\"BodyNames\":(\d+\.\d+)")
        result = pattern.findall(content)
        planets 
        if result:
                for r in result:
                        planets.append(r)
		print(result)
        return planets
