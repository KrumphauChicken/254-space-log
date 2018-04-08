# Dylan Connors
import re

def get_planet_names(content:str) -> str:
        pattern = re.compile("\"BodyName\":\"(.+?)\"")
        result = pattern.findall(content)
        names = []
        if result:
                for r in result:
                        names.append(r)
        return names





