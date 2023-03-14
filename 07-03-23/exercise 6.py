# Use a while loop. Prompt the user to enter a number.
# If the user enters 0, end the loop and display the total of all numbers entered on the screen.

numTotal = 0
while True:
    num = int(input("Please enter a number (enter 0 to stop): "))
    if num == 0:
        break
    numTotal += num
print("Total: " + str(numTotal))
