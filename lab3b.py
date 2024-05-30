#!/usr/bin/env python3

'''Lab 3 Part 1 script - functions'''
#Author ID: pacharya9(100706225)

#Defining a function to add two numbers
def sum_numbers(number1, number2):
    sum = number1 + number2
    return sum

#Defining another function to subtract the numbers.
def subtract_numbers(number1, number2):
    subtract = number1 - number2
    return subtract

#Defining another function to perform multiplication of two numbers.
def multiply_numbers(number1, number2):
    multiplication = number1 * number2
    return multiplication

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10,5))
    print(multiply_numbers(10,5))
