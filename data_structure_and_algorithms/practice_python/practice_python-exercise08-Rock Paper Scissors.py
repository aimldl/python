# -*- coding: utf-8 -*-
"""
2018-10-26 (Thu)
PRACTICE PYTHON, https://www.practicepython.org/

Exercise 8. Rock Paper Scissors
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of 
congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

Solution
https://www.practicepython.org/solution/2014/04/02/08-rock-paper-scissors-solutions.html
"""
player1 = input("Player 1 enters rock (1), scissors (2), or paper (3):")
player2 = input("Player 1 enters rock (1), scissors (2), or paper (3):")

p1 = int(player1)
p2 = int(player2)

# The smaller number wins
if p1 == 1 && p2 == 2:
    print("Player 1 wins!")
elif p1 == p2:
    print("Draw.")
else:
    print("Player 2 wins!")
