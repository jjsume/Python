#recursive calculating method by jjsume@github (Jere Sumell)

#Next method is recursive

import sys
def calculate(value):
	if (value == 0):
		return 1
	else:
		return value*calculate(int(value)-1)
#next is the main program
var = int(5)
#next line return 5! = 120.
print ("" +str(calculate(var)))
