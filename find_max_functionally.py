# find_max_functionally.py
    # by dev chrysalis!
'''
Problem 3: Find Maximum
Objective: Implement a function that takes a list of numbers and a lambda function as arguments. The lambda function should compare two numbers and return the greater of the two. 
Use this lambda function to find the maximum number in the list without using the built-in max() function.
Hint: Initialize your maximum with the first element of the list and then iterate over the list, using the lambda function to update the maximum.
'''
from functools import reduce
from typing import Callable # apparently python doesn't ship with functions-as-parameter annotations

def maximum(num_list : list[int], f : Callable[[int, int], int] ): # honestly, probs shouldn't be named "maximum" since the thing doing the maximuming is parameter f
    return reduce(f, num_list)

print(maximum([10, 20, 12, 21, 21, 22, -17], lambda a, b : b if b > a else a))


