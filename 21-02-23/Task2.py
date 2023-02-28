count = 12
output = ""
while count > 0:
    output += (str(count) + ",")
    count -= 1
final = output.rstrip(output[-1])
print(final)
