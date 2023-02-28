value = 1.0
print(value)
while value > 0.001:
    value /= 2
    if value > 0.001:
        print(value)
