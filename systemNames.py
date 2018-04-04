#Matthew Camarena
#Function to get ALl StarSystem Naes which you have FSDJumped to
#imports
import re

def get_FSDJump_names(content): 

	list = []
	
	FSDJump = False
	StarSystem = False

	quoted = re.compile('"[^"]*"')

	for value in quoted.findall(content):
	    
		if(value == "\"FSDJump\""):
			
			FSDJump = True
		elif(value == "\"StarSystem\""):
			StarSystem = True
			
		elif(FSDJump and StarSystem):
			
			list.append(value)

			FSDJump = False
			StarSystem = False
		else:
			FSDJump = False
			StarSystem = False

	return list 