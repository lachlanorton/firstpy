# Create a program to construct the following pattern based on user input.
#
# Example output:
# Enter a number: 4
#
# *
# **
# ***
# ****

# V1 - use for loop
# size = int(input("Square size: "))
# for i in range(size):
#     print("*" * (i + 1))

# V2 - use while loop
count = 0
size = int(input("Square size: "))
while count < size:
    print("*" * (count + 1))
    count += 1
