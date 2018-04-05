# Tenzin Dorjee
<<<<<<< HEAD
# Terraformable Planets
# part 3
=======
# Print the total number of terraformable planets
>>>>>>> ebecf366fd89814a9f17dcb8fbe2910da4708d00


import re

def findPlanets(content):


    pattern = re.compile(r'Terraformable')
    results = pattern.findall(content)
    planetCounter = 0

    for result in results:
        planetCounter+=1

    return planetCounter
