# Module 4  Functions & Modules in Python
# task1 Calculate factorial using function


number = int(input("insert the no whose factorial you want : "))         # we are giving number firs

def factorial(n):                        # created function where we are passing this number
    if n < 2:                          #checking if that number is less than 2 if yes , it will print answer 1
        return 1
    else:                              #if number is greater than two else stateme nt trigger and it will calculate further
        return n * (factorial(n - 1))

Result = factorial(number)            # now we passing this functional function to variable and printing it
print(Result)




#task 2 :
#imported math module
import math

#Given value as input
number = float(input("Enter number : "))

#defined value and took from math module for square root
square_root=    math.sqrt(number)

#defined value and took from math module for log function
natural_log=    math.log(number)

#defined value and took from math module for sine function
sine_value=     math.sin(number)

#printing value through string and dynamic way
print(f"the square root of {number}is: {square_root}")
print(f"the nantural log of {number}is: {natural_log}")
print(f"the Sine value  of {number}is: {sine_value}")



