# Imported modules
import sys

# User input function, takes in the user's calculation and returns it, if the user types 'exit' the program will close
def User_Input():
    calc = input("Enter your calculation: ")
    if calc == "exit":
        sys.exit()
    else:
        return calc