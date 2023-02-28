import random
dice1 = 0
dice2 = 0
answer = False

while answer == False:
    guess = input("What do you think the total of two six-sided die will be? ")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1 + dice2
    if diceTotal == int(guess):
        answer == True
        print("Correct! The total was " + str(diceTotal))
    else:
        print("Try again! The total was " + str(diceTotal))
