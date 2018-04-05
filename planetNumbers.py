# Tenzin Dorjee
# Print the total number of terraformable planets


import re

def findPlanets(content):


    pattern = re.compile(r'Terraformable')
    results = pattern.findall(content)
    planetCounter = 0

    for result in results:
        planetCounter+=1

    return planetCounter
