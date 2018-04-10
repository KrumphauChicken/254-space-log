#Brett Mansell

import re

def scanned_planets(content):
    pattern = re.compile(r"\"event\":\"Scan\", \"BodyName\":\"(\w+\s\w+[-\s]\w+[-\s]\w+[-\s\w]\"?\w?\w?\w?\w?\s?\w?-?\w?-?\w?\w?)\"?")  
    matches = pattern.findall(content)
    for match in matches:
        return (matches) 
