import random

print("Welcome to Rock, Paper, Scissors!")
 
player = raw_input("Rock, Paper, or Scissors?")

computer = random.randint(1,3)

#int 1 = "Rock"
#int 2 = "Paper"
#int 3 = "Scissors"

computer_choice = 0
if computer == 1:
	computer_choice = ("Rock")
	print("Rock")
elif computer == 2:
	computer_choice = ("Paper")
	print("Paper")
elif computer == 3:
	computer_choice = ("Scissors")
	print("Scissors")
else: 
	print("Error")
 

	