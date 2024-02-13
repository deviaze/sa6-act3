# instersect.py
    # by dev chrysalis!

'''
Problem 4: Intersection of Two Lists
Objective: Write a Python program that finds the intersection of two lists using a lambda function and the filter() function. The program should return a list of elements that are present in both lists.
Hint: You may want to use the filter() function to keep only the elements in one list that are also contained in the other list.
'''

def intersect(a : list, b : list) -> list:
    return list(filter(lambda n : n in b, a))

# should work on lists of basically anything:
l1  = [0x14, "string", "local function(a : string, b : number) end", print, 47]
l2 = ["string", "47", int("47"), lambda x : x // 2, intersect]

print(intersect(l1, l2))