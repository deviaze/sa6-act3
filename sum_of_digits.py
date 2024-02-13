# functional_practice.py
    # by dev chrysalis!

'''
Problem 1: Sum of Digits
Objective: Write a Python program that uses a lambda function to compute the sum of the digits of a given number.
Hint: You may need to convert the number to a string to iterate over its digits, then back to integers to sum them.
'''

from functools import reduce

def Σ_digits(number : int):
    return reduce(lambda a, b : a + b, map(int, list(str(number))))
    # I'm using the python typechecker so I get a TypeError if I pass str(number) as my 2nd argument without the map()

print(Σ_digits(122))