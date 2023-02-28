# Programming concepts
# Written by Lachlan Orton
# Date: 14/02/2023
# TAFE St Leonard's Campus

# Example of a 'constant'
# A variable that should not be changed, written in UPPER_CASE
GST = 0.1
NEW_TAX = 0.12

# Example of string concatenation
result = "hello" + "world"
print(result)


# To find what data type a variable is, use type()
x = 5
print(type(x))

y = True
print(type(y))


# To find the length of an array or total characters in a string use len()
print(len("Hello"))


# TAFE EXERCISE : Calculating the user's Age given their date of birth.
from datetime import datetime
Year = int(input("Please enter the year you were born: "))
Month = int(input("Please input the number of the month you were born. (For example 8 = August): "))
Day = int(input("Please enter the day you were born "))
DateOfBirth = datetime(Year, Month, Day)
Age = datetime.now() - DateOfBirth
print("You are " + str(Age.days) + " days old")
convertDays = int(Age.days)
AgeYears = convertDays/365
print("Or " + str(AgeYears) + " years old to be less precise")
print(type(AgeYears))