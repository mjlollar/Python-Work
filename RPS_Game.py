#!/usr/bin/env python

import random
import sys

print("Would you like to play a game?")

while True:
	play_game = input("Answer Yes or No:\n").lower()
	if not play_game in ['yes', 'no']:
		print('\nSorry, I did not catch that.')
		continue
	elif play_game in ['no']:
		print("OK, see you later.")
		sys.exit()
	else:
		break
		
print("\nOK, Lets' play rock paper scissors.")

while True: 
	choice = ['rock', 'paper', 'scissors']
	computer_choice = (random.choice(choice))
	while True:
		user_choice = input("\nEnter rock, paper, or scissors:\n").lower()
		if not user_choice in ['rock', 'paper', 'scissors']:
			print('\nThat is not a choice, try again')
		else:
			break
	
	print('\nONE, TWO, THREE, SHOOT!: ' + '(' + computer_choice + ')')
	
	if computer_choice == user_choice:
		print('TIE!!!\n')
	elif user_choice == 'rock' and computer_choice == 'scissors':
		print('YOU WIN!!\n')
	elif user_choice == 'paper' and computer_choice == 'rock':
		print('YOU WIN!!\n')
	elif user_choice == 'scissors' and computer_choice == 'paper':
		print('YOU WIN!!\n')
	else:
		print('I WIN!!!\n')

	while True:
		user_choice2 = input("\nWould you like to play again? Enter Yes or No:\n").lower()
		if not user_choice2 in ['yes', 'no']:
			expression = str(user_choice2)
			print ('You said: {}'.format(expression))
			print('Please answer correctly numbskull')
		else:
			break
	
	if user_choice2 in ['no']:
		print("Thanks for playing! See you next time!")
		sys.exit()
	else: 
		continue
		
		
	
	
			
	
	
	
