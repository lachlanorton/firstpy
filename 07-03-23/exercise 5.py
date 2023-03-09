# Ask the user to enter a number between 1 and 10.
# Then display the number’s times table.
# Example output:
#
# If the user enters 9 then display:
# 9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# and so on ...

# V1 - use for loop
# num = int(input("Enter a number between 1 and 10: "))
# for i in range(11):
#     if i < 1:
#         continue
#     print(str(num) + " * " + str(i) + " = " + str(num * i))

# V2 - use while loop
num = int(input("Enter a number between 1 and 10: "))
count = 1
while count < 11:
    print(str(num) + " * " + str(count) + " = " + str(count * num))
    count += 1
