# custom_sort.py
    # by dev_chrysalis!
'''
Problem 2: Custom Sort Order
Objective: Given a list of strings, use a lambda function to sort the list in ascending order based on the length of the strings. In case of a tie, sort the strings alphabetically.
Hint: The sorted() function's key parameter can take a lambda function that returns a tuple indicating the primary and secondary sort keys.
'''

def custom_sort(list : list[str]):
    return sorted(list, key=lambda s : len(s))

t1_result = custom_sort(["len", "longer", "len2", "longestest", "longest", "l", "longerestest", "μ"])
t1_expected = ['l', 'μ', 'len', 'len2', 'longer', 'longest', 'longestest', 'longerestest']
