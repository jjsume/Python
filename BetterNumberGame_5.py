#Simple number guessing game by jjsume@ Github(Jere Sumell)
import random

def game(guess): 
	comp = random.randint(1,5)
	if int(guess) == int(comp):
		print ("Well, we are on the same level now! My lucky number was " +str(comp) +" too!")
		print ("Exiting the game...")
		return True;
	else:
		print ("Fool, run me again, My lucky number was " +str(comp))
		user =input("Give your lucky number between 1 and 5: ") 

user = input("Give your lucky number between 1 and 5: ")
			
while game(user):
	game(user)
print ("Congrats! You finally exited the crypt maze!")	