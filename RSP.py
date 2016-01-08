#!/bin/python
from random import randint

def winner():
	print "You've won"

def draw():
	print "It's a draw"

def loser():
	print "You've lost"

def enemy(choice):
	print "Your enemy chose " + choice

def game():
	rN = randint(1,9)
	answer = raw_input("\n\n>>>")

	if rN > 0 and rN <= 3:
		enemy("rock")
		if answer == 'rock':
			draw()
		elif answer == 'paper':
			winner()
		else:
			loser()

	if rN > 3 and rN <= 6:
		enemy("paper")
		if answer == 'rock':
			loser()
		elif answer == 'scissor':
			winner()
		else:
			draw()
	
	if rN > 6 and rN <= 9:
		enemy("scissor")
		if answer == 'rock':
			winner()
		elif answer == 'paper':
			loser()
		else:
			draw()
	print "\n\n Wanna play again? (y or n)"
	ant = raw_input(">>>")	

	if ant == 'y':
		game()

	
print "Welcome to rock, paper, scissors"
print "--------------------------------------------------"
print "Type rock, paper or scissor and see if you can win"

game()
