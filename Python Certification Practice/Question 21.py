#You are creating a Python script to evaluate input and check for upper and lower case
#Out of these 6 code segments, which 4 segments should you use to develop the solution

name = input("Enter your name:")
if name.lower() == name:print(name, "is all lowercase.")
elif name.upper() == name: print(name, "is all uppercase.")
else: print(name, "is mixed case.")