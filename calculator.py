# Imported modules
import sys

# User input function, takes in the user's calculation and returns it, if the user types 'exit' the program will close
def User_Input():
    calc = input("Enter your calculation: ")
    if calc == "exit":
        sys.exit()
    else:
        return calc
    
# Function to split the user's calculation into a list, then cast all numbers as integers while leaving the operators as strings
def Split_Cast_Calculation(calculation):
    split_calc = calculation.split(" ")
    for item in split_calc:
        if item.isdigit():
            split_calc[split_calc.index(item)] = int(item)
        else:
            continue
    return split_calc

result = Split_Cast_Calculation(User_Input())
print(result)