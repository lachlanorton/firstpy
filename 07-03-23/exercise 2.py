# Write a program to draw a square of ‘ * ’ based on user input.
#
# Example output:
# Enter a number: 4
#
# * * * *
# * * * *
# * * * *
# * * * *

# V1 - use for loop
size = int(input("Square size: "))
for i in range(size):
    print("*" * size)

# V2 - use while loop
# count = 0
# size = int(input("Square size: "))
# count = size
# while count > 0:
#     print("*" * size)
#     count -= 1
