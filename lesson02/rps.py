import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
# print(RPS(2))
# print(RPS.ROCK.value)

print("")
playerchoice = input("Enter...\n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

player = (int(playerchoice))

if player < 1 or player > 3:
    sys.exit("Enter the value of any 1, 2 and 3")
    
computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("you choose " + str(RPS(player)).replace('RPS.', '') + ".")
print("you choose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("Human wins! 🏆")
elif player == 2 and computer == 2:
    print("Human wins! 🏆")
elif player == 3 and computer == 1:
        print("Human wins! 🏆")
elif player == computer:
        print("Tie game! 👌")
else:
    print("Bot wins! 🤖")
