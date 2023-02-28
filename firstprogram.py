# Introduction to PyCharm, reintroduction to Python
# Written by Lachlan Orton
# Date: 07/02/2023
# TAFE St Leonard's Campus

import math

print('Hello World!')
print('07/02/2023')
print('3x27=', 3*27)

tvShow = input("Favourite TV Show: ")
print('You said', tvShow)
print('')


# Question 1
print("The area of a rectangle with sides 2m and 6m is", 2*6, 'm^2')

# Ask for user input for length and height
length = int(input("Input a length: "))
height = int(input("Input a height: "))
# Calculate area
area = length * height
# Print calculation
print('The area of a rectangle with sides', length, 'm and', height, 'm equals', area, 'm^2')
print('')

# Question 2
print('The area of a circle with a radius of 3m is', math.pi*3*3, 'm^2')

# Ask for user input for radius and calculate area of circle and print
radius = int(input("Input a radius: "))
print("The area of a circle with a radius ", radius, 'm is', math.pi*radius*radius, 'm^2')
print('')

# Question 3
print('A product that costs $350.00 with GST added costs', 350.00+(350*0.1))

# Ask for user input for non-GST product price
productPrice = float(input('Input a price of a product (no GST): '))
# Calculate new product price with GST added
productPriceGST = float(productPrice + (productPrice * 0.1))
# Print result
print('A product that costs', productPrice, 'with no GST now costs', productPriceGST, 'with GST added.')
print('')

# Question 4
minutesWorked = int(input("How many minutes worked?: "))
hoursWorked = int(minutesWorked / 60)
# could use:    minutesWorked // 60
remainingMinutes = int(minutesWorked - (hoursWorked * 60))
# % = modulus, gives you the leftover of a division
# therefore I could use:    remainingMinutes = minutesWorked % 60
print(minutesWorked, 'minutes becomes', hoursWorked, 'hour(s) and', remainingMinutes, 'minute(s).')
print('')

# Question 5
tempF = float(input("Input a temperature in fahrenheit: "))
tempC = float((tempF - 32) * 5/9)
print('Fahrenheit: ', tempF, 'F')
print('Celsius: ', tempC, 'C')