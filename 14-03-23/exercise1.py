# Create a folder making program which makes a series of folders in your current working directory.
# Take input from the user. Keep asking for input until the user presses the enter key.
# Written by Lachlan Orton
# Date: 14/03/2023
# TAFE St Leonard's Campus

# First Iteration
#
# import os
#
# while True:
#     response = input("Enter a folder name (Press ENTER to stop): ")
#     if response == "":
#         break;
#     os.mkdir(response)
#     print("Successfully made new directory", response, "inside of", os.getcwd())

# Modify the first iteration of your code.
# Now check first if the folder exists before attempting to create it.

import os

while True:
    response = input("Enter a folder name (Press ENTER to stop): ")
    if response == "":
        break;
    if os.path.exists(response):
        print(response, "directory already exists.")
    else:
        os.mkdir(response)
        print("Successfully made new directory", response, "inside of", os.getcwd())
