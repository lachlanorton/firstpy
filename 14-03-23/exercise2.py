# Write a program to record hostnames and IP addresses in a text file.
# Ask the user to input a certain number of hosts.
# For each host, enter a hostname and IP address.
# Write the data to a file called hosts.txt, creating a new line for each entry.
# If you run the program again make sure the existing data is not overwritten.
#
# Written by Lachlan Orton
# Date: 14/03/2023
# TAFE St Leonard's Campus

f = open("hosts.txt", "a")

hostname1 = input("Hostname: ")
f.write(hostname1 + ": ")
address1 = input("IP Address: ")
f.write(address1 + "\n")

hostname2 = input("Hostname: ")
f.write(hostname2 + ": ")
address2 = input("IP Address: ")
f.write(address2 + "\n")
f.close()