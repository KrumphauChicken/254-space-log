'''
{ "timestamp":"2018-01-20T18:40:41Z", "event":"Scan", "BodyName":"Droju KZ-J b1-1 A",
 "DistanceFromArrivalLS":0.000000, "StarType":"M", "StellarMass":0.382813, "Radius":391728128.000000,
  "AbsoluteMagnitude":8.778915, "Age_MY":2378, "SurfaceTemperature":3102.000000, "Luminosity":"Va",
   "SemiMajorAxis":48316866560.000000, "Eccentricity":0.044001, "OrbitalInclination":63.564106,
    "Periapsis":328.910339, "OrbitalPeriod":61702440.000000, "RotationPeriod":173118.625000,
     "AxialTilt":0.000000 }
'''

import re

def get_total_terraformable(content:str) -> int:
	pattern = re.compile("\"JumpDist\":(\d+\.\d+)")
	result = pattern.findall(content)
	total = 0
	if result:
		for r in result:
			total+=1
	return total