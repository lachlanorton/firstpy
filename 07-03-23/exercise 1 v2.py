# Write a program to ask the use to guess a password that is written in your Python code.
# For example, the password is “Meadowbank”.
# The user can enter three guesses only. The program then ends and prints an access “Denied Message.”

password = "Meadowbank"
guesses = 3
found = False

# V! - use for loop
# for i in range(guesses):
#     attempt = input("Please enter the password: ")
#     if attempt == password:
#         found = True
#         break
#
# if not found:
#     print("Access Denied.")
# if found:
#     print("Access Granted")

# V2 - use while loop
while not found:
    if guesses > 0:
        attempt = input("Please enther the password: ")
        guesses -= 1
        if attempt == password:
            found = True
            break
    else:
        print("Access Denied")
        exit()
print("Access Granted")
