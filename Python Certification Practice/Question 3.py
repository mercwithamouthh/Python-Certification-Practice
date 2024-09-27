#You are writing a Python program to validate employee numbers.
#The employee number must have the format ddd-dd-dddd and consist only of numbers and dashes.
#The program must print True if the format is correct and print False if the format is incorrect.
#How should you complete the code?
from unittest.mock import sentinel

employee_number = " "
parts = " "
while employee_number != "sentinel":
    valid = False
    employee_number = input("Enter employee number (ddd-dd-dddd) : ")
    parts = employee_number.split('-')
    if len(parts) == 3:
        if len(parts[0]) == 3 and len(parts[1]) == 2 and len(parts[2]) == 4:
            if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                valid = True
    print(valid)