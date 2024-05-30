#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''
#Author ID: pacharya9(100706225)

# Defining a function to hold three different arguments.
def operate(num1, num2, operation):
    # Using control flow statements to perform desired mathematical calculations.
    if operation == 'add':
        result = num1 + num2
        return result
    if operation == 'subtract':
        result = num1 - num2
        return result
    if operation == 'multiply':
        result = num1 * num2
        return result
    # Displaying error message whenever user tries to call division calculation.
    if operation == 'divide':
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
        return result

# Main code to be executed.

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))

