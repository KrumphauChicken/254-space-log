"""
Chase Huante
Question 3
"""
import re

def is_it_terraformable(content):
    counter = 0
    #pattern = re.compile(r"\"event\":\"Scan\", \"BodyName\":\"(\w+\s\w+[-\s]\w+[-\s]\w+[-\s\w]\"?\w?\w?\w?\w?\s?\w?-?\w?-?\w?\w?), \"DistanceFromArrivalLS\":('\d*\.......'), \"TidalLock\":\"(true|false)\", \"TerraformState\":\"Terraformable\")\"")
    pattern = re.compile(r"Terraformable")
    matches = pattern.finditer(content)
    for match in matches:
        print("found one")
        counter += 1
    return(counter)
