print("This program will determine your interest rate level based on")
print("the amount of time the money has been in your bank account.")
print(" ")
time = float(input("How many years has the money been in your bank account?: "))
interest = 0

if time < 1:
    interest = 2.0
else:
    if time >= 1 and time < 3:
        interest = 3.5
    else:
        interest = 4.5
print("Your interest rate is: " + str(interest) + "%")
