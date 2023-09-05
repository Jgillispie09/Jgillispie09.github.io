# Rock Paper Scissors
# Rock Crushes Scissors
# Scissors Cut Paper
# Paper Covers Rock

import random
import time

roles = ['rock', 'paper', 'scissors']
points_p1 = 0
points_p2 = 0
max_point = 3

print("Welcome to the game!")
while points_p1 < max_point or points_p2 < max_point:
    print("The current score is: \nPlayer 1: " + str(points_p1) + " Player 2: " + str(points_p2))
    player1 = input("Rock, Paper, or Scissors?: ")
    player2 = random.randint(0,3)
    if player1 == 'rock' or player1 == 'Rock':
        if player2 == 0:
            print("Player 1 chose rock!")
            time.sleep(1)
            print("Player 2 also chose rock!")
            time.sleep(1)
            print("It's a draw!")
            time.sleep(1)
        elif player2 == 1:
            print("player 1 chose rock!")
            time.sleep(1)
            print("Player 2 chose paper!")
            time.sleep(1)
            print("Paper covers rock! A point for player 2!")
            time.sleep(1)
            points_p2 += 1
        else:
            print("Player 1 chose rock!")
            time.sleep(1)
            print("Player 2 chose scissors!")
            time.sleep(1)
            print("Rock crushes scissors! A point for player 1!")
            time.sleep(1)
            points_p1 += 1
    if player1 == 'paper' or player1 == 'Paper':
        if player2 == 0:
            print("Player 1 chose paper!")
            time.sleep(1)
            print("Player 2 chose rock!")
            time.sleep(1)
            print("Paper covers rock! A point for player 1!")
            time.sleep(1)
            points_p1 += 1
        elif player2 == 1:
            print("Player 1 chose paper!")
            time.sleep(1)
            print("Player 2 also chose paper!")
            time.sleep(1)
            print("It's a draw!")
            time.sleep(1)
        else:
            print("Player 1 chose paper!")
            time.sleep(1)
            print("Player 2 chose scissors!")
            time.sleep(1)
            print("Scissors cuts rock! A point for player 2!")
            time.sleep(1)
            points_p2 += 1
    if player1 == 'scissors' or player1 == 'Scissors':
        if player2 == 0:
            print("Player 1 chose scissors!")
            time.sleep(1)
            print("Player 2 chose rock!")
            time.sleep(1)
            print("Rock crushes scissors! A point for player 2!")
            time.sleep(1)
            points_p2 += 1
        elif player2 == 1:
            print("Player 1 chose scissors!")
            time.sleep(1)
            print("Player 2 chose paper!")
            time.sleep(1)
            print("Scissors cuts paper! A point for player 1!")
            time.sleep(1)
            points_p1 += 1
        else:
            print("Player 1 chose scissors!")
            time.sleep(1)
            print("Player 2 chose scissors!")
            time.sleep(1)
            print("It's a draw!")
            time.sleep(1)
    if points_p1 == max_point or points_p2 == max_point:
        print("Final Score: Player 1: " + str(points_p1) + " Player 2: " + str(points_p2))
        time.sleep(1)
        print("Goodbye!")
        break



