import random

print ("Welcome to Rock, Paper, Scissors!")

while user_wins < 3 and computer_wins < 3:
	user_wins = 0
	computer_wins = 0
	user_choice = raw_input("Rock, Paper, or scissors?")

	for x in range(3):
		computer_choice = random.randint(1,3),

	computer_word = ""
	if computer_choice == 1:
		computer_word = "rock"
	elif conputer_choice == 2:
		computer_word = "paper"
	elif conputer_choice == 3:
		computer_word = "scissors"

	if user_choice == "rock" and computer_word == "paper":
		print ("COMPUTER WINS")
		COMPUTER_WINS = COMPUTER_WINS + 1
	elif user_choice == "rock" and computer_word == "scissors":
		print ("YOU WIN")
		YOU_WIN = YOU_WIN + 1
	elif user_choice == "rock" and computer_word == "rock":
		print ("TIE")
	elif user_choice == "paper" and computer_word == "rock":
		print ("YOU WIN")
		YOU_WIN = YOU_WIN + 1
	elif user_choice == "paper" and computer_word == "scissors":
		print ("COMPUTER WINS")
		COMPUTER_WINS = COMPUTER_WINS + 1
	elif user_choice == "paper" and computer_word == "paper":
		print ("TIE")
	elif user_choice == "scissors" and computer_word == "paper":
		print ("YOU WIN")
		YOU_WIN = YOU_WIN + 1
	elif user_choice == "scissors" and computer_word == "scissors":
		print ("TIE")
	elif user_choice == "scissors" and computer_word == "rock":
		print ("COMPUTER WINS")
		COMPUTER_WINS = COMPUTER_WINS + 1
	else:
		print ("Error")
