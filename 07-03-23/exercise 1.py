# Write a program to ask the use to guess a password that is written in your Python code.
# For example, the password is “Meadowbank”.
# The user can enter three guesses only. The program then ends and prints an access “Denied Message.”

password = "Meadowbank"
guesses = 3
for guess in range(guesses):
    attempt = input("Enter password: ")
    if attempt != password:
        guesses -= 1
        print("Access Denied. Attempts left:", str(guesses))
    elif attempt == password:
        print("Access Granted.")
        exit()
