
#lambda
#def cube(x): return x * x * x
cube = lambda x : x * x * x
print(cube(9))

""" 
def filter(list, predicate):
    result = []
    for item in list:
        if predicate(item):
            result.append(item)
    return result 
"""

# Functional APIs in python

nos_list = [3,1,4,2,5]
# builtin filter
even_nos = list(filter(lambda no : no % 2 == 0, nos_list))
print(even_nos)

# builtin map
print(list(map(lambda x : x * 2, nos_list)))

# builtin reduce
import functools
print(functools.reduce(lambda x,y: x + y, nos_list, 0))

# Find the number of odd & even numbers from nos_list using reduce
def count_odd_even(result, no):
    if no % 2 == 0:
        result['even'] += 1
    else:
        result['odd'] += 1
    return result

nos_stats = functools.reduce(count_odd_even, nos_list, {'even' : 0, 'odd' : 0})
print(nos_stats)

