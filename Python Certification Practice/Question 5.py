#What is the expected output of the following snippet?
i = 250
while len(str(i)) > 72:
    i *= 2
else:
    i //= 2

print(i)