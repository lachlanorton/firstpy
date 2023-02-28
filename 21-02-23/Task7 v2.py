import random
diceTotal = random.randint(1, 6) + random.randint(1, 6)
guess = int(input("What do you think the total of two six-sided die will be? "))
tries = 0
while guess != diceTotal:
    diceTotal = random.randint(1, 6) + random.randint(1, 6)
    print("The total sum was", diceTotal, ", try again!")
    guess = int(input("What do you think the total of two six-sided die will be? "))
    tries += 1
else:
    tries += 1
    print("That's right! The total sum was", diceTotal)
    print("That took you", tries, "times to get right!")
