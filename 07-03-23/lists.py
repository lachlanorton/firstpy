# Working with lists
# Written by Lachlan Orton
# Date: 07/03/2023
# TAFE St Leonard's Campus

# Declare lists
my_list = [1, 5, 70, 420]
wordy_list = ["hello", "world"]
mixed_list = ["hello", 5, True]
empty_list = []

print(my_list)
print(wordy_list)
print(empty_list)

print("")

# Printing elements in list at index position
print(my_list[3])
my_list[3] = 360
print(my_list[3])
print(my_list[-2])

print("")

print("Length of wordy_list:", len(wordy_list))
cities = ["Sydney", "Melbourne", "Hobart", "Brisbane"]
# Add element to list
cities.append("Canberra")
print(cities)
# Removes the last element in the list
# cities.pop() stores what element has been removed
removed_suburb = cities.pop()
print(removed_suburb)
# Remove element from list at index position
# del does not store what element has been removed
del cities[1]
print(cities)

# FIFO - First In First Out - queue
# LIFO - Last In First Out - stack

# When modifying lists, remember that the length is changing
# This is important to remember when accessing lists later

# Range in list - acts as grabbing elements from A to B but not including B itself
some_cities = cities[0:2]
print(some_cities)

print("")

# For statement / loop
# for statements use an iterator to keep track of its position through a list
for city in cities:
    print(city)

print ("")

# Using while loop to do the same effect
index = 0
while index < len(cities):
    print(cities[index])
    index += 1

print("")

# Range() function
for i in range(10):
    print(i)

for i in range(len(cities)):
    print("Index:", i)
    print(cities[i])

# Uses (start, stop, step) values in range() function
# stop is exclusive
for num in range(1, 30, 3):
    print(num)

print("")

# If we need to leave loop early, use break and continue
# break leaves the loop, continue goes back to start line of loop
for i in range(6):
    if i == 3:
        break
print(i)

for i in range(10):
    if i == 3:
        continue
    text = text + str(i)
print(text)
