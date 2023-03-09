# Experimentation playground for assessment
# Written by Lachlan Orton
# Date: 28/02/2023
# TAFE St Leonard's Campus

print("1) LOGIN")
print("2) REGISTER")
print("3) EXIT")

option = float(input("Please select an option (#): "))

if option == 1:
    print("Welcome to Login")
elif option == 2:
    print("Welcome to Register")
elif option == 3:
    print("Exiting...")
elif option > 3:
    print("Incorrect option! Please restart.")
