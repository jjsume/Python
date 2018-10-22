#Palindrome class for Python. Made by jjsume@github (Jere Sumell)

import sys

def checkWord(word):
	wordT = word.lower()
	wordTB = wordT.replace(" ","")
	
	wordB = wordTB[::-1]
	if (wordB == wordTB):
		return True
	return False

	
we = input("Give me your String:" )
weB = checkWord(we)
if weB:
	print ("You found a palindrome!")
	
else:
	print ("The given string isn't palindrome!")