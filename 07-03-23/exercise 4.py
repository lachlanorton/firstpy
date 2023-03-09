# Write a program to add up all numbers up to the user input number.
# Example output:
#
# Enter a number: 5
#
# 1
# 2
# 3
# 4
# 5
# Total is: 15

# V1 - use for loop
# num = int(input("Enter a number: "))
# totalNum = 0
# for i in range(num + 1):
#     if i < 1:
#         continue
#     print(i)
#     totalNum += i
# print("Total is:", totalNum)

# V2 - use while loop
num = int(input("Enter a number: "))
totalNum = 0
count = 1
while count <= num:
    print(count)
    totalNum += count
    count += 1
print("Total is", totalNum)


