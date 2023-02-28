import random

count = 0
smallest = 50   # max of random int generation
while count < 10:
    ranNum = random.randint(0, 50)
    print(ranNum)
    if ranNum < smallest:
        smallest = ranNum
    count += 1
print("The smallest number is " + str(smallest) + "\n")