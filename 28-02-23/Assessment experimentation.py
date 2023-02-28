print("LOGIN")
print("REGISTER")
print("EXIT")
option = input("Please select an option: ")

if option == "LOGIN":
    print("Welcome to Login")
else:
    if option == "REGISTER":
        print("Welcome to Register")
    else:
        if option == "EXIT":
            print("Exiting...")
        else:
            print("Incorrect option! Please restart.")
