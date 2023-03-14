# Experimenting with file system in Python
# Written by Lachlan Orton
# Date: 14/03/2023
# TAFE St Leonard's Campus
f = open("myfile.txt", "w")
f.close()

g = open("myfile.txt", "a")
g.write("\nMirage")
g.close()

h = open("myfile.txt", "r")
print(h.read())
# print(f.readline())
# print(f.readlines())
h.close()
