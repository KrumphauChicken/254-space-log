#David Luong
import re

def find_system_names(content:str):
    pattern = re.compile("\"StarSystem\":\"[-\w+\s\d+]+")
    planetResult = pattern.findall(content)
    return planetResult