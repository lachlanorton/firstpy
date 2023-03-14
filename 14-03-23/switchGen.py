# Exercise 3 + Exercise 4
# Written by Lachlan Orton
# Date: 14/03/2023
# TAFE St Leonard's Campus

# Create a program to write basic network switch configurations into a text file.
# The files will be written to your current working directory as default.
# Ask the user to input the following: hostname, vlan1_ip, vlan1_subnet, default_gateway.
# Take the user input and add these values to a standard switch configuration.
# Write the values to a file named after the hostname.

import os

print("Welcome to the CISCO Network Switch Config Generator")
hostname = input("Hostname: ")
ip = input("VLAN 1 IP: ")
subnet = input("VLAN 1 Subnet: ")
gateway = input("Default Gateway: ")

f = open("%s.txt" % hostname, "a")
f.write("enable \nconf t \n")
f.write("host " + str(hostname) + "\n")
f.write("no ip domain lookup \nenable secret class \n")
f.write("banner motd #Authorised personnel only# \n")
f.write("line con 0 \npassword cisco \nlogging synchronous \nline vty 0 4 \n")
f.write("transport input all \npassword cisco \nlogin local \ninterface vlan 1 \n")
f.write("ip address " + ip + "" + subnet + "\n")
f.write("no shut \n")
f.write("ip default-gateway " + gateway + "\n")
f.write("do wr \n")
f.close()
