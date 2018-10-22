#Simple number guessing game by jjsume@ Github(Jere Sumell)
import random
user = input("Give your lucky number between 1 and 5: ")
comp = random.randint(1,5)
if int(user) == int(comp):
	print ("Well, we are on the same level now! My lucky number was " +str(comp) +" too!")
else:
	print ("Fool, run me again, My lucky number was " +str(comp))