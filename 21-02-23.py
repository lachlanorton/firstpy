# Classwork
# Written by Lachlan Orton
# Date: 21/02/2023
# TAFE St Leonard's Campus

import random

# Expression revisit
letter1 = ' '
letter2 = 'a'
string = 'elephant'

if letter1 in string:
    print("Yes. 1 is in string. \n")
elif letter2 in string:
    print("Yes. 2 is in string. \n")
else:
    print("No. Neither 1 or 2 are in string. \n")

# Iteration
x = 2
print(x)
while x < 1024:
    x = x * 2
    print(x)
print("\n")

count = 1
y = 2
while count < 11:
    print(y)
    y = y * 2
    count += 1
print("\n")

# import random used
ranCount = 0
biggest = 0
# ranNumsGenerated = []
while ranCount < 10:
    ranNum = random.randint(0, 100)
    print(ranNum)
    if ranNum > biggest:
        biggest = ranNum
    # ranNumsGenerated.append(ranNum)
    ranCount += 1
print("The biggest number is " + str(biggest) + "\n")


# print(ranNumsGenerated)
# print(max(ranNumsGenerated))
