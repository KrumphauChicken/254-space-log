# Tenzin Dorjee
# Terraformable Planets
# part 3


import re

def findPlanets(content):


    pattern = re.compile(r'Terraformable')
    results = pattern.findall(content)
    planetCounter = 0

    for result in results:
        planetCounter+=1

    return planetCounter
