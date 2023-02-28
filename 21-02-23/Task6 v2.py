import random

count = 0
smallest = 50   # max of random int generation
biggest = 0     # min of random int generation
numsGeneratedTotal = 0
while count < 10:
    ranNum = random.randint(0, 50)
    print(ranNum)
    numsGeneratedTotal += ranNum
    if ranNum < smallest:
        smallest = ranNum
    if ranNum > biggest:
        biggest = ranNum
    count += 1

avgNums = numsGeneratedTotal / 10

print("The smallest number is " + str(smallest) + "\n")
print("The biggest number is " + str(biggest) + "\n")
print("The average number is " + str(avgNums) + "\n")
