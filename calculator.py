# Imported Modules
import sys
import time

# Delayed print function, reduces the speed of the print function by creating a delay between each character
def delayed_print(message, delay=1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay) 
    print()

# Welcome message for the user, uses the delayed print function
def Welcome_Message():
    delayed_print("Welcome to the calculator program \n" \
    "Type in your calculation, ensuring spaces between all numbers and operators, then press enter \n" \
    "Example: 1 + 1 \n" \
    "Type 'exit' to close the program \n", delay=0.05)

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

# Function to calculate the user's calculation using BODMAS, using match statements to determine the operator and then performing the calculation
def BODMAS(calc):
    for x in calc:
        match x:
            case "**":
                index = calc.index("**")
                calc[index] = calc[index-1] ** calc[index+1]
                calc.pop(index-1)
                calc.pop(index)
            case "/":
                index = calc.index("/")
                calc[index] = calc[index-1] / calc[index+1]
                calc.pop(index-1)
                calc.pop(index)
            case "*":
                index = calc.index("*")
                calc[index] = calc[index-1] * calc[index+1]
                calc.pop(index-1)
                calc.pop(index)
            case "+":
                index = calc.index("+")
                calc[index] = calc[index-1] + calc[index+1]
                calc.pop(index-1)
                calc.pop(index)
            case "-":
                index = calc.index("-")
                calc[index] = calc[index-1] - calc[index+1]
                calc.pop(index-1)
                calc.pop(index)
            case int:
                continue
        return calc
# CURRENT ISSUE - The program is not calculating the correct answer if the equation is more then 2 numbers, it is only calculating the first two numbers in the list, Cause: The for loop is skipping over certain operators as the list has been modified and the index is no longer correct. Solution: Ask Sartak for help.


# Function to use the user input, split and cast, and BODMAS functions to run the calculator program
def Running():
    Welcome_Message()
    while True:
        user_calc = User_Input()
        split_calc = Split_Cast_Calculation(user_calc)
        completed_calc = BODMAS(split_calc)
        print(*completed_calc) # The * is used to unpack the list and print it as individual items, removing any brackets


Running()