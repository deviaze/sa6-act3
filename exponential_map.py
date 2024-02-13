# exponential_map.py
    # by dev chrysalis!
'''
Problem 5: Exponential Mapping
Objective: Given a list of numbers and a constant value n, use a lambda function with map() to raise each number in the list to the power of n.
Hint: The lambda function should take one argument and use the constant n within its expression to compute the power.
'''

def exponential_in_place(numbers : list[int | float], n : int) -> None:
    numbers[:] = list(map(lambda i : i ** n, numbers)) # need to assign the slice (elements) to mutate original array
    
    
t1_list = [1, 2, 4, 9, 10.125]

print(f"Original list: {t1_list}")
print("printing result of function: ", exponential_in_place(t1_list, 2), " <- should be None")

print(f"mutated list: {t1_list}")
